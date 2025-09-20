# Playwright MCP Server Installation Guide

The Playwright MCP server enables AI assistants to perform browser automation, end-to-end testing, and UI interactions for web applications.

## Prerequisites

- **Node.js**: Version 18 or higher
- **npm**: For package installation
- **Chrome/Chromium**: Browser binaries (installed automatically)

## Installation Steps

### 1. Install Playwright MCP Server

```bash
# Install globally (recommended)
npm install -g @modelcontextprotocol/server-playwright

# Verify installation
mcp-server-playwright --version
```

### 2. Install Browser Binaries

Playwright requires browser binaries to function:

```bash
# Install all supported browsers
npx playwright install

# Install only Chromium (lightweight option)
npx playwright install chromium

# Install specific browsers
npx playwright install chrome firefox safari
```

### 3. Verify Installation

```bash
# Check Playwright version
npx playwright --version

# Test browser installation
npx playwright open --help

# List installed browsers
npx playwright list-browsers
```

## Configuration for Claude Code

Add to your `~/.claude/config.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "mcp-server-playwright",
      "args": ["--headless"],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "",
        "PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD": "false"
      }
    }
  }
}
```

### Configuration Options

**Headless Mode** (recommended for CI/CD):
```json
"args": ["--headless"]
```

**Headed Mode** (for debugging):
```json
"args": ["--headed"]
```

**Specific Browser**:
```json
"args": ["--browser=chromium"]
```

**Custom Browser Path**:
```json
"env": {
  "PLAYWRIGHT_BROWSERS_PATH": "/opt/playwright-browsers"
}
```

## Django Development Setup

### 1. Django Server Configuration

Ensure your Django development server is accessible for testing:

```python
# settings.py
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# For development
DEBUG = True
```

### 2. Test Environment Setup

Create a test-specific settings file `settings_test.py`:

```python
from .settings import *

# Use in-memory database for faster tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Disable migrations for faster tests
class DisableMigrations:
    def __contains__(self, item):
        return True
    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()
```

### 3. Test Data Setup

Create fixtures or factories for consistent test data:

```python
# In your Django app
# fixtures/test_messages.json
[
  {
    "model": "chat.message",
    "pk": 1,
    "fields": {
      "session_id": "test-session-1",
      "role": "user",
      "content": "Hello, test message",
      "created_at": "2024-01-01T10:00:00Z"
    }
  }
]
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

3. **Test basic browser automation** (within Claude Code):
```
Open a browser and navigate to localhost:8000 to test the Playwright MCP server
```

## Common Issues and Solutions

### Installation Issues

**Error: "Browser download failed"**
```bash
# Retry browser installation
npx playwright install --force

# Check internet connection and proxy settings
npm config get proxy
npm config get https-proxy
```

**Error: "Permission denied" on Linux**
```bash
# Install dependencies for browser sandboxing
sudo npx playwright install-deps

# Or install system dependencies manually
sudo apt-get install libnss3 libatk-bridge2.0-0 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libxss1 libasound2
```

### Runtime Issues

**Error: "Browser not found"**
```bash
# Reinstall browser binaries
npx playwright install chromium

# Check browser path
npx playwright list-browsers
```

**Error: "Timeout waiting for browser"**
```bash
# Increase timeout in configuration
"args": ["--headless", "--timeout=60000"]

# Or check system resources
htop  # Linux/macOS
taskmgr  # Windows
```

### Django Integration Issues

**Error: "Connection refused to localhost:8000"**
```bash
# Ensure Django development server is running
python manage.py runserver 0.0.0.0:8000

# Check if port is available
lsof -i :8000  # macOS/Linux
netstat -an | findstr :8000  # Windows
```

**Error: "CSRF token missing"**
```bash
# Add CSRF exemption for tests
# In Django settings_test.py
MIDDLEWARE = [m for m in MIDDLEWARE if 'csrf' not in m.lower()]
```

## Performance Optimization

### Browser Resource Management

**Limit browser instances**:
```json
"args": ["--headless", "--max-instances=2"]
```

**Reduce resource usage**:
```json
"args": [
  "--headless",
  "--disable-gpu",
  "--no-sandbox",
  "--disable-dev-shm-usage"
]
```

### Test Optimization

**Faster test execution**:
- Use `chromium` instead of `chrome` for tests
- Enable headless mode for CI/CD
- Reuse browser contexts when possible
- Use fixtures for consistent test data

## Security Considerations

### Development Environment
- Use headless mode for automated testing
- Limit browser access to localhost/development domains
- Disable unnecessary browser features for testing

### CI/CD Environment
- Use containerized browsers in Docker
- Enable sandbox mode for security
- Limit network access to required domains only

## Next Steps

1. Configure Playwright MCP server with Claude Code
2. Create end-to-end tests for Django chat app
3. Use Playwright for UI development and debugging
4. Set up automated testing workflows

## Useful Commands

```bash
# Playwright management
npx playwright install                    # Install browsers
npx playwright list-browsers             # List installed browsers
npx playwright open --help               # Open browser for debugging
npx playwright codegen localhost:8000    # Generate test code

# MCP server testing
mcp-server-playwright --version          # Check version
mcp-server-playwright --help             # Show help options

# Browser debugging
npx playwright open localhost:8000       # Open site in Playwright browser
npx playwright screenshot --url=localhost:8000 --path=screenshot.png
```

## Troubleshooting Checklist

- [ ] Node.js 18+ installed
- [ ] Playwright MCP server installed globally
- [ ] Browser binaries installed (`npx playwright install`)
- [ ] Django development server running on port 8000
- [ ] Claude Code configuration updated
- [ ] Claude Code restarted after configuration
- [ ] MCP server appears in `claude mcp list`
- [ ] No port conflicts or firewall issues
- [ ] Sufficient system resources for browser automation