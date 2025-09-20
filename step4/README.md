# Step 4 — Django Chat App with MCP Servers

Goal: Create a simple Django front end + back end chat app enhanced with MCP (Model Context Protocol) servers for database and testing capabilities. We'll first establish the Django architecture foundation, then enhance it with MCP servers for advanced capabilities.

## Prerequisites
- Python 3.11+, Git, and your preferred terminal. Optional: Docker (see root `docker-compose.yml`).
- Agents installed: Claude Code, Gemini CLI, or OpenAI Codex CLI.
- **MCP Servers**: Playwright and PostgreSQL MCP servers (setup in Part 2).

---

## Part 1: Django Chat App Foundation

### Step 1: Create Django Project Structure

First, let's create the basic Django chat application architecture in the `django-chat/` folder.

#### 1.1 Navigate to Step 4 Directory

```bash
cd step4/
```

#### 1.2 Set Up Development Environment

Before launching AI tools, set up a clean Python environment:

```bash
# Create a new conda environment for the project
conda create -n django-chat python=3.11

# Activate the environment
conda activate django-chat
```

#### 1.3 Launch AI Agent and Request Project Scaffolding

Now launch your preferred AI tool and create the Django project:

**Using Claude Code (Preferred):**
```bash
claude
```

**Using Gemini CLI:**
```bash
gemini
```

**Using OpenAI Codex CLI:**
```bash
codex
```

**Request Django Project Scaffolding**

Use this prompt with your AI tool to create the project structure and architecture:

```
Create a Django chat application in a folder called 'django-chat' with the following structure:

Project Requirements:
- Django project named 'chatproject'
- Django app named 'chat'
- Models: ChatSession, Message
- Views: chat room, message API endpoints
- Templates: chat interface with basic HTML/CSS
- URL routing for both web and API endpoints
- Basic WebSocket support for real-time messaging
- Requirements.txt with all dependencies
- Settings configured for development

Important:
1. Only create the project scaffolding and basic structure - do not implement features yet
2. Please also write an ARCHITECTURE.md document that describes:
   - Overall system design and components
   - Database schema and model relationships
   - API endpoints and routing structure
   - Frontend architecture and templates
   - WebSocket integration approach
   - Development and deployment considerations
3. Ensure you are working in the django-chat conda environment.

Focus on the architectural foundation before implementation.
```

#### 1.4 Verify Project Structure

After the AI creates the project, verify the structure:

```bash
cd django-chat/
tree -L 3 .
```

Expected structure:
```
django-chat/
├── manage.py
├── requirements.txt
├── ARCHITECTURE.md
├── chatproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── chat/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    ├── templates/
    └── static/
```

#### 1.5 Initialize AI Agent Project Context

Before proceeding with development, initialize your AI agents with project context so they can understand and work effectively with the codebase:

**Initialize AI Agent Understanding**

Ask your AI tool to analyze and build context about the project:

```
Please perform an /init analysis of this Django chat project:

1. Read and analyze the project structure I just created
2. Examine the ARCHITECTURE.md document
3. Review all configuration files (settings.py, urls.py, etc.)
4. Understand the app structure and models
5. Create your own internal documentation about:
   - Project purpose and goals
   - File organization and conventions
   - Database models and relationships
   - URL patterns and routing
   - Template and static file structure
   - Development workflow and standards

After analysis, provide a brief summary of your understanding and ask if there are any specific project conventions or preferences I'd like you to follow for this codebase.
```

**Expected AI Response**

Your AI agent should:
- ✅ Confirm understanding of the Django chat application purpose
- ✅ Identify the main components (chatproject, chat app, models, etc.)
- ✅ Understand the architecture and design patterns
- ✅ Ask about coding standards or preferences
- ✅ Be ready to help with implementation following project conventions

**Verify AI Understanding**

Ask follow-up questions to ensure your AI agent is properly initialized:

```
Quick test of your project understanding:
1. What is the main purpose of this application?
2. What are the key Django models we'll be working with?
3. How is the project structured (apps, urls, templates)?
4. What should you consider when adding new features to this codebase?
```

#### 1.6 Install Dependencies and Test

Now let's use your AI agent to help set up and test the Django project.

**Option A: Ask AI Agent to Guide Setup**

Ask your AI tool to help with the setup process:

```
Help me set up the Django chat project we just created:

1. Install all dependencies from requirements.txt
2. Run database migrations to create the necessary tables
3. Create a Django superuser for admin access
4. Start the development server and verify it's working
5. Test access to both the main site and Django admin

Please guide me through each step and help troubleshoot any issues.
```

**Option B: Manual Setup with AI Verification**

If you prefer to run commands manually, use these steps and ask AI to verify:

```bash
# Install dependencies
pip install -r requirements.txt

# Set up the database
python manage.py makemigrations
python manage.py migrate

# Create admin user (AI can help if you encounter issues)
python manage.py createsuperuser
```

When creating the superuser, enter:
- Username: `admin` (or your preferred username)
- Email: your email address
- Password: a secure password for development

**Ask AI to Verify Setup:**

After running the commands, ask your AI tool:

```
I've just set up the Django project. Can you help me:

1. Verify the setup was successful
2. Test that the development server starts properly
3. Check that both the main site and admin interface are accessible
4. Identify any potential issues or missing configurations

Current status: [describe what happened when you ran the commands]
```

Start the development server:

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to verify the basic Django app is working.

### Step 2: Enhance with Basic Chat Functionality

Now let's add the core chat functionality:

#### 2.1 Define Chat Models

Ask your AI tool to create the chat models:

```
Create Django models for the chat application:

1. ChatSession model:
   - id (auto)
   - name (CharField)
   - created_at (DateTimeField)
   - updated_at (DateTimeField)

2. Message model:
   - id (auto)
   - session (ForeignKey to ChatSession)
   - content (TextField)
   - role (CharField with choices: 'user', 'assistant')
   - created_at (DateTimeField)

Include proper string representations and ordering.
```

#### 2.2 Create Views and Templates

Request the basic chat interface:

```
Create Django views and templates for:

1. Chat room view that displays messages
2. API endpoint to send new messages
3. API endpoint to get messages for a session
4. Basic HTML template with:
   - Message display area
   - Message input form
   - Simple CSS styling
   - JavaScript for sending messages via AJAX

Make it functional but simple - we'll enhance with WebSockets later.
```

#### 2.3 Test Basic Chat Functionality

After implementation:

1. Run migrations: `python manage.py makemigrations && python manage.py migrate`
2. Start server: `python manage.py runserver`
3. Test sending and receiving messages through the web interface

### Step 3: Verify Foundation

At this point, you should have:

✅ Working Django project with chat app
✅ Database models for chat sessions and messages
✅ Basic web interface for sending/receiving messages
✅ API endpoints for message operations
✅ Proper project structure and dependencies

---

## Part 2: MCP Servers Enhancement

Now that we have a working Django foundation, let's enhance it with MCP (Model Context Protocol) servers for advanced database management and testing capabilities.

MCP servers extend AI assistants with specialized capabilities. For this Django chat app, we'll use:

- **PostgreSQL MCP Server**: Database management, schema operations, and queries
- **Playwright MCP Server**: Browser automation, end-to-end testing, and UI interactions

### Step 4: MCP Servers Setup

Before we can enhance our Django app with MCP capabilities, we need to set up the MCP servers and configure our AI tools to use them.

#### 4.1 MCP Servers Directory Structure

Your step4 directory should now look like this:

```
step4/
├── django-chat/                 # Django project (created in Part 1)
│   ├── manage.py
│   ├── requirements.txt
│   ├── chatproject/
│   └── chat/
└── mcp-servers/
    ├── README.md                 # MCP setup overview
    ├── claude-config.json        # Claude Code MCP configuration
    ├── gemini_settings.json      # Gemini CLI MCP configuration
    ├── codex_config.toml         # OpenAI Codex CLI MCP configuration
    ├── postgresql/
    │   ├── install.md           # PostgreSQL MCP installation guide
    │   ├── config.json          # MCP server configuration
    │   └── examples.md          # Usage examples and commands
    └── playwright/
        ├── install.md           # Playwright MCP installation guide
        ├── config.json          # MCP server configuration
        └── examples.md          # Usage examples and commands
```

### AI Tool Configuration Files

The `mcp-servers/` directory includes configuration files for different AI tools to connect to the MCP servers:

- **`claude-config.json`** - Configuration for Claude Code MCP servers
  - Supports both PostgreSQL and Playwright servers
  - Use this for Claude Code MCP integration

- **`gemini_settings.json`** - Configuration for Gemini CLI MCP servers
  - Includes Playwright and PostgreSQL toolbox configurations
  - Contains IDE and theme preferences for Gemini CLI

- **`codex_config.toml`** - Configuration for OpenAI Codex CLI MCP servers
  - TOML format configuration for Codex integration
  - Defines server commands and environment variables

Choose the configuration file that matches your preferred AI tool and copy it to the appropriate location as described in the installation sections below.

#### 4.2 PostgreSQL MCP Server Setup

The PostgreSQL MCP server enables AI assistants to directly interact with your Django application's PostgreSQL database.

#### Installation

1. **Install the PostgreSQL MCP server**:
```bash
# Using npm (recommended)
npm install -g @modelcontextprotocol/server-postgres

# Or using npx for one-time use
npx @modelcontextprotocol/server-postgres
```

2. **Verify installation**:
```bash
mcp-server-postgres --version
```

#### Configuration

Create `step4/mcp-servers/postgresql/config.json`:

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

#### Usage Examples

**Database Schema Management**:
```bash
# Create tables
mcp postgres create-table messages "id SERIAL PRIMARY KEY, session_id VARCHAR(255), role VARCHAR(50), content TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"

# Query data
mcp postgres query "SELECT * FROM messages WHERE session_id = 'session-123' ORDER BY created_at"

# Database migrations
mcp postgres migrate --file ./migrations/001_initial.sql
```

**Integration with Django**:
- Use for database inspection during development
- Query data directly for debugging
- Manage migrations and schema changes
- Monitor database performance

### Playwright MCP Server

The Playwright MCP server provides browser automation capabilities for testing and UI interactions.

#### Installation

1. **Install the Playwright MCP server**:
```bash
# Using npm (recommended)
npm install -g @modelcontextprotocol/server-playwright

# Install browser binaries
npx playwright install
```

2. **Verify installation**:
```bash
mcp-server-playwright --version
npx playwright --version
```

#### Configuration

Create `step4/mcp-servers/playwright/config.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "mcp-server-playwright",
      "args": ["--headless"],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "/opt/playwright"
      }
    }
  }
}
```

#### Usage Examples

**End-to-End Testing**:
```bash
# Navigate and test the chat interface
mcp playwright navigate "http://localhost:8000/chat/"
mcp playwright fill "#message-input" "Hello, AI assistant!"
mcp playwright click "#send-button"
mcp playwright wait-for-text "Hello, AI assistant!"

# Capture screenshots for documentation
mcp playwright screenshot --path "./docs/chat-interface.png"

# Test form submissions
mcp playwright test-form "#chat-form" --submit
```

**UI Development**:
- Capture screenshots of different UI states
- Test responsive design across browser sizes
- Automate repetitive testing tasks
- Generate visual documentation

### Claude Code Integration

To use MCP servers with Claude Code, add them to your Claude configuration:

1. **Create or update `~/.claude/config.json`**:
```json
{
  "mcpServers": {
    "postgres": {
      "command": "mcp-server-postgres",
      "args": [],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://localhost:5432/django_chat_dev"
      }
    },
    "playwright": {
      "command": "mcp-server-playwright",
      "args": ["--headless"],
      "env": {}
    }
  }
}
```

2. **Restart Claude Code**:
```bash
claude restart
```

3. **Verify MCP servers are available**:
```bash
claude mcp list
```

### Development Workflow with MCP Servers

1. **Database-First Development**:
   - Use PostgreSQL MCP to design and create database schema
   - Query data directly during development
   - Debug database issues with direct SQL access

2. **Test-Driven UI Development**:
   - Use Playwright MCP to write tests before implementing features
   - Capture UI states for design review
   - Automate regression testing

3. **Documentation Generation**:
   - Automatically capture screenshots of UI components
   - Generate database schema documentation
   - Create visual test reports

### Troubleshooting

**PostgreSQL MCP Server Issues**:
- Ensure PostgreSQL is running: `pg_ctl status`
- Check connection string format
- Verify database exists: `createdb django_chat_dev`

**Playwright MCP Server Issues**:
- Install browser binaries: `npx playwright install`
- Check for port conflicts on default Django port (8000)
- Verify headless mode works: `npx playwright --version`

**Claude Code Integration Issues**:
- Check config file syntax: `claude config validate`
- Restart Claude Code after config changes
- Verify MCP servers are in PATH: `which mcp-server-postgres`

---

## Part 3: Enhance Django App with MCP Powers

Now that we have both the Django foundation and MCP servers configured, let's enhance the chat application with advanced capabilities.

### Step 5: Database Enhancement with PostgreSQL MCP

Navigate back to your Django project and use your AI tool with MCP capabilities:

```bash
cd django-chat/
claude  # or gemini/codex with MCP enabled
```

#### 5.1 Database Schema Optimization

Use the PostgreSQL MCP server to analyze and optimize your Django models:

```
Using the PostgreSQL MCP server, help me:

1. Analyze the current Django chat app database schema
2. Add proper indexes for chat message queries
3. Create database views for common chat operations
4. Set up the production PostgreSQL database configuration

Current models: ChatSession and Message
Database: django_chat_dev (PostgreSQL)
```

#### 5.2 Advanced Database Operations

With MCP-enabled AI assistance:

```
Help me implement these database enhancements:

1. Add database triggers for automatic timestamp updates
2. Create a view for recent chat sessions with message counts
3. Add database-level constraints for data integrity
4. Implement efficient pagination for chat history

Use the PostgreSQL MCP server to create and test these directly.
```

### Step 6: Automated Testing with Playwright MCP

#### 6.1 E2E Test Creation

Use the Playwright MCP server to create comprehensive tests:

```
Using the Playwright MCP server, help me create end-to-end tests for:

1. Chat message sending and receiving
2. Chat session creation and management
3. UI responsiveness across different screen sizes
4. Form validation and error handling

Start Django server on localhost:8000 and test against it.
```

#### 6.2 Visual Testing and Documentation

Generate visual documentation with MCP:

```
Using Playwright MCP server:

1. Capture screenshots of the chat interface in different states
2. Test the UI across different browsers
3. Generate visual documentation for the chat flow
4. Create automated visual regression tests

Save screenshots to django-chat/docs/ folder.
```

### Step 7: Integrated Development Workflow

#### 7.1 AI-Powered Development Loop

With both MCP servers active, establish this workflow:

1. **Plan** new features with AI assistance
2. **Implement** using AI code generation
3. **Test** database changes with PostgreSQL MCP
4. **Validate** UI with Playwright MCP
5. **Document** automatically with both servers

#### 7.2 Example: Add Message Reactions Feature

Practice the full MCP-enhanced workflow:

```
Help me add a message reactions feature to the chat app:

1. Design database schema changes (use PostgreSQL MCP)
2. Implement Django models and views
3. Update frontend with reaction buttons
4. Create database indexes and queries (PostgreSQL MCP)
5. Test the feature end-to-end (Playwright MCP)
6. Generate documentation screenshots (Playwright MCP)

Walk me through each step using the appropriate MCP servers.
```

### Success Criteria

By the end of Step 4, you should have:

✅ **Working Django Chat Application**
- Complete project structure
- Chat sessions and messaging
- Basic web interface
- API endpoints

✅ **MCP Server Integration**
- PostgreSQL MCP server connected
- Playwright MCP server configured
- AI tools using MCP capabilities

✅ **Enhanced Development Workflow**
- Database operations through MCP
- Automated UI testing
- Visual documentation generation
- Integrated AI-assisted development

✅ **Production-Ready Features**
- Optimized database schema
- Comprehensive test coverage
- Visual documentation
- Performance monitoring
