# PostgreSQL MCP Server Installation Guide

The PostgreSQL MCP server enables AI assistants to directly interact with PostgreSQL databases for schema management, queries, and database operations.

## Prerequisites

- **PostgreSQL**: Version 12 or higher
- **Node.js**: Version 18 or higher
- **npm**: For package installation

## Installation Steps

### 1. Install PostgreSQL (if not already installed)

**macOS (Homebrew)**:
```bash
brew install postgresql@15
brew services start postgresql@15
```

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

**Windows**:
Download and install from [postgresql.org](https://www.postgresql.org/download/windows/)

### 2. Install PostgreSQL MCP Server

```bash
# Install globally (recommended)
npm install -g @modelcontextprotocol/server-postgres

# Verify installation
mcp-server-postgres --version
```

### 3. Create Django Chat Database

```bash
# Create development database
createdb django_chat_dev

# Create test database (optional)
createdb django_chat_test

# Verify databases exist
psql -l | grep django_chat
```

### 4. Configure Database Connection

Create a `.env` file in your Django project directory:

```bash
# Database connection for Django
DATABASE_URL=postgresql://localhost:5432/django_chat_dev

# MCP server connection string
POSTGRES_CONNECTION_STRING=postgresql://localhost:5432/django_chat_dev
```

### 5. Test Connection

```bash
# Test database connection
psql django_chat_dev -c "SELECT version();"

# Test MCP server
mcp-server-postgres --connection-string="postgresql://localhost:5432/django_chat_dev" --help
```

## Configuration for Claude Code

Add to your `~/.claude/config.json`:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "mcp-server-postgres",
      "args": [],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://localhost:5432/django_chat_dev"
      }
    }
  }
}
```

## Verification

1. **Restart Claude Code**:
```bash
claude restart
```

2. **Check MCP servers are loaded**:
```bash
claude mcp list
```

3. **Test basic database operations** (within Claude Code):
```
Create a simple test table and verify the PostgreSQL MCP server is working
```

## Common Issues and Solutions

### Connection Issues

**Error: "Connection refused"**
```bash
# Check if PostgreSQL is running
pg_ctl status

# Start PostgreSQL if not running
brew services start postgresql@15  # macOS
sudo systemctl start postgresql    # Linux
```

**Error: "Database does not exist"**
```bash
# Create the database
createdb django_chat_dev

# Or connect as postgres user first
sudo -u postgres createdb django_chat_dev
```

### Permission Issues

**Error: "Permission denied"**
```bash
# Create a PostgreSQL user (if needed)
createuser --superuser $USER

# Or grant permissions to existing user
sudo -u postgres psql -c "ALTER USER $USER CREATEDB;"
```

### MCP Server Issues

**Error: "Command not found: mcp-server-postgres"**
```bash
# Reinstall the MCP server
npm install -g @modelcontextprotocol/server-postgres

# Check global npm bin directory is in PATH
npm config get prefix
echo $PATH
```

## Security Considerations

1. **Development Environment**:
   - Use localhost connections for development
   - Consider using a dedicated PostgreSQL user for the Django app

2. **Production Environment**:
   - Use environment variables for connection strings
   - Enable SSL connections
   - Use connection pooling

## Next Steps

1. Configure the PostgreSQL MCP server with Claude Code
2. Create Django models using the MCP server for database operations
3. Use the MCP server for debugging and database inspection during development

## Useful Commands

```bash
# Database management
createdb <database_name>          # Create database
dropdb <database_name>            # Delete database
pg_dump <database_name>           # Backup database
psql <database_name>              # Connect to database

# PostgreSQL service management
brew services start postgresql@15    # Start (macOS)
brew services stop postgresql@15     # Stop (macOS)
sudo systemctl start postgresql      # Start (Linux)
sudo systemctl stop postgresql       # Stop (Linux)

# MCP server testing
mcp-server-postgres --version        # Check version
mcp-server-postgres --help           # Show help
```