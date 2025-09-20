# MCP Servers for Django Chat App

This directory contains Model Context Protocol (MCP) server configurations and documentation for the Django chat application in Step 4.

## Overview

MCP servers extend AI assistants like Claude Code with specialized capabilities. This setup includes:

- **PostgreSQL MCP Server**: Database operations, schema management, and queries
- **Playwright MCP Server**: Browser automation, testing, and UI interactions

## Quick Setup

1. **Install both MCP servers**:
```bash
# PostgreSQL MCP server
npm install -g @modelcontextprotocol/server-postgres

# Playwright MCP server
npm install -g @modelcontextprotocol/server-playwright
npx playwright install
```

2. **Configure Claude Code**:
```bash
# Copy configuration to Claude config
cp ./claude-config.json ~/.claude/config.json

# Restart Claude Code
claude restart
```

3. **Verify installation**:
```bash
claude mcp list
```

## Directory Structure

```
mcp-servers/
├── README.md                    # This file
├── claude-config.json           # Complete Claude configuration
├── postgresql/
│   ├── install.md              # Detailed PostgreSQL setup
│   ├── config.json             # Server configuration
│   └── examples.md             # Usage examples
└── playwright/
    ├── install.md              # Detailed Playwright setup
    ├── config.json             # Server configuration
    └── examples.md             # Usage examples
```

## Usage in Django Development

### Database Development
- Design and create database schemas
- Query data directly for debugging
- Manage migrations and schema changes
- Monitor database performance

### UI Testing and Development
- Write end-to-end tests
- Capture screenshots for documentation
- Test responsive design
- Automate regression testing

## Troubleshooting

**Common Issues**:
- Ensure PostgreSQL is running before using postgres MCP
- Install browser binaries for Playwright: `npx playwright install`
- Restart Claude Code after configuration changes

**Getting Help**:
- Check individual server documentation in subdirectories
- Verify MCP servers are available: `claude mcp list`
- Test individual servers: `mcp-server-postgres --version`

---

## Next Steps

1. Set up PostgreSQL database for Django chat app
2. Configure both MCP servers with Claude Code
3. Use MCP servers during Django development workflow