# Step 4 — Django Chat App with MCP Servers

Goal: Create a simple Django front end + back end chat app enhanced with MCP (Model Context Protocol) servers for database and testing capabilities. Start with documentation and agent collaboration; code comes after the plan. Do not pre‑create folders—use agents to author files as you go.

## Prerequisites
- Python 3.11+, Git, and your preferred terminal. Optional: Docker (see root `docker-compose.yml`).
- Agents installed: Claude Code, Gemini CLI, or OpenAI Codex CLI.
- **MCP Servers**: Playwright and PostgreSQL MCP servers (setup instructions below).

---

## MCP Servers Setup

MCP (Model Context Protocol) servers extend Claude Code and other AI assistants with specialized capabilities. For this Django chat app, we'll use:

- **PostgreSQL MCP Server**: Database management, schema operations, and queries
- **Playwright MCP Server**: Browser automation, end-to-end testing, and UI interactions

### What are MCP Servers?

MCP servers are specialized tools that AI assistants can use to perform specific tasks:
- **Database operations**: Query, migrate, and manage databases
- **Browser automation**: Test web interfaces, capture screenshots, fill forms
- **File operations**: Read, write, and manipulate files with context
- **API integrations**: Connect to external services and APIs

### MCP Servers Directory Structure

Create the following structure in your step4 directory:

```
step4/
├── mcp-servers/
│   ├── README.md                 # MCP setup overview
│   ├── postgresql/
│   │   ├── install.md           # PostgreSQL MCP installation guide
│   │   ├── config.json          # MCP server configuration
│   │   └── examples.md          # Usage examples and commands
│   └── playwright/
│       ├── install.md           # Playwright MCP installation guide
│       ├── config.json          # MCP server configuration
│       └── examples.md          # Usage examples and commands
└── django-chat/                 # Main project (created later)
```

### PostgreSQL MCP Server

The PostgreSQL MCP server enables AI assistants to directly interact with PostgreSQL databases.

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

## Part 1: Docs‑First Workflow
1) Architecture (Claude)
- Prompt Claude to create `step4/django-chat/ARCHITECTURE.md` and describe:
  - Stack: Django 5, server templates, SQLite (dev) → Postgres (later).
  - Model: `Message(session_id, role: user|assistant, content, created_at, user_id?)` with index `(session_id, created_at)`.
  - Routes: `GET /` (landing), `GET /chat/`, `POST /chat/send/`.
  - Session: cookie‑based `session_id`. Assistant reply: deterministic random stub.

2) One‑Round Review (Gemini/Codex)
- Run: `gemini review step4/django-chat/ARCHITECTURE.md` or `codex review ...`.
- Apply feedback and finalize a single revised version.

3) Plan (Claude)
- Ask Claude to write `step4/django-chat/PLAN.md` with small steps:
  - Bootstrap project/app, add `Message` model, templates, endpoints, assistant stub, basic tests.

4) Documentation Templates
- Create `step4/django-chat/documents/meta-template-prompt.md` (placeholder for now).
- Generate `documents/templates/{feature,enhancement,bugfix}-template.md` from the meta prompt.

5) Feature Design Docs
- Create two docs in `step4/django-chat/features/` using the templates:
  - `landing-page-design.md` — `/` page with project info and links.
  - `chat-page-design.md` — `/chat/` UI; `POST /chat/send/`; persist messages; stub assistant.

6) Secondary Agent Review
- Use Gemini or Codex to review each design doc; append reviewer notes to the bottom and refine once.

7) GitHub Workflow Agent
- Add `step4/django-chat/agents/github-workflow-agent.md` with rules:
  - Never commit to `main`; branch per task (`feat/<slug>`), rebase before PR, stage only relevant files.

When Part 1 is done, proceed to implementation following `PLAN.md`.
