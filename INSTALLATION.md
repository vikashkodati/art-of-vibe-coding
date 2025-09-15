# Installation Guide for Vibe Coding Workshop

This guide provides step-by-step instructions for setting up all the tools you'll need for the workshop. Please complete all installations before the workshop begins.

## Overview

You'll need to install and configure:
- **Modern Terminal** - Warp (recommended) or iTerm2 for enhanced terminal experience
- **Claude Code** - Anthropic's official CLI tool (requires paid subscription or API key)
- **Gemini CLI** - Google's AI assistant via official CLI tool
- **Cursor IDE** - AI-powered code editor (recommended primary IDE)
- **VS Code** (optional alternative)

---

## 📟 Terminal Tools

Modern terminals enhance your AI development experience with better features and integrations.

### Warp (Recommended)

Warp is a modern, AI-powered terminal with built-in features perfect for AI development workflows.

#### Installation

**macOS:**
```bash
brew install --cask warp
```

**Alternative:** Download from [warp.dev](https://warp.dev/)

#### Setup
1. Launch Warp
2. Sign in with your GitHub account (recommended)
3. The terminal includes built-in AI assistance and workflow features

#### Key Features for Workshop
- Built-in AI command suggestions
- Workflow automation
- Modern interface with themes
- Git integration
- Command palette (`Cmd + P`)

### iTerm2 (macOS Alternative)

A powerful terminal replacement for macOS with extensive customization options.

#### Installation

**Homebrew (Recommended):**
```bash
brew install --cask iterm2
```

**Direct Download:**
Download from [iterm2.com](https://iterm2.com/)

#### Recommended Setup
1. Install Oh My Zsh for enhanced shell experience:
```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

2. Configure useful features:
   - Split panes (`Cmd + D` / `Cmd + Shift + D`)
   - Profiles for different projects
   - Hotkey window (`Cmd + Space`)

#### Key Features
- Split panes and tabs
- Search and autocomplete
- Customizable profiles
- Hotkey window
- Integration with tmux

### Windows Terminal (Windows)

For Windows users, Windows Terminal provides a modern terminal experience.

#### Installation

**From Microsoft Store:**
Search for "Windows Terminal" in the Microsoft Store

**Using winget:**
```powershell
winget install Microsoft.WindowsTerminal
```

#### Setup
1. Launch Windows Terminal
2. Configure default shell (PowerShell, Command Prompt, or WSL)
3. Customize themes and profiles

---

## 🖥️ CLI Tools

### Claude Code

Claude Code is Anthropic's official CLI tool that provides powerful AI assistance directly in your terminal.

#### Requirements
- **Paid Claude subscription** (Pro or Team plan)
- macOS, Linux, or Windows
- Node.js 18+ installed

#### Installation

**Using the installer (Recommended):**
Visit [claude.ai/download](https://claude.ai/download) and download the installer for your operating system.

**Alternative: Using npm (if available):**
```bash
npm install -g @anthropic-ai/claude-cli
```

> **Note:** Claude Code is currently in limited release. The exact installation method may vary. Check the official Claude website for the latest installation instructions.

#### Authentication

**Login with your Claude account:**
```bash
claude auth login
```
This will open a browser window to authenticate with your Claude Pro/Team account.

**Alternative: API Key**
If you have an API key from [Anthropic Console](https://console.anthropic.com/):
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

#### Verification
```bash
claude --version
claude --help
```

### Gemini CLI

Access Google's Gemini models directly through the official Gemini CLI tool. Your personal Google account includes free daily usage limits.

#### Requirements
- Node.js 20 or higher
- Google account
- Internet connection

#### Installation

**Option 1: Quick Use (No Installation)**
```bash
npx @google/gemini-cli
```

**Option 2: Global Install via npm (Recommended)**
```bash
npm install -g @google/gemini-cli
```

**Option 3: Homebrew (macOS/Linux)**
```bash
brew install gemini-cli
```

#### Setup and Authentication

After installation, run the CLI:
```bash
gemini
```

**Authentication Options:**
1. **Google Login** (Recommended for workshop)
   - The CLI will prompt you to authenticate with your *personal* Google account
   - This provides free daily usage limits and is recommended for the workshop

2. **API Key** (Alternative)
   - Get an API key from [Google AI Studio](https://aistudio.google.com/)
   - Set it as an environment variable:
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

#### Verification
```bash
gemini --version
gemini --help
```

#### Workshop Usage Examples
```bash
# Basic usage
gemini

# Include specific directories for context
gemini --include-directories src,docs

# Use specific model
gemini -m gemini-2.0-flash-exp
```

---

## 💻 IDEs & Code Editors

### Cursor IDE (Primary Recommendation)

Cursor is an AI-native code editor built specifically for AI-assisted development.

#### Installation
1. Download from [cursor.com](https://cursor.com/)
2. Install the application for your operating system
3. Launch Cursor

#### Setup
1. Open Cursor
2. Sign in with your GitHub account (recommended)
3. Configure AI models:
   - Go to Settings → Models
   - Add your Anthropic API key for Claude access
   - Gemini will work through your Google account authentication

#### Key Features for Workshop
- `Cmd/Ctrl + K` - AI chat and code generation
- `Cmd/Ctrl + L` - Inline AI assistance
- AI-powered autocomplete
- Natural language code editing

### VS Code (Alternative Option)

If you prefer VS Code, you can set it up with AI extensions.

#### Installation
1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install for your operating system

#### Required Extensions
Install these extensions from the VS Code marketplace:

1. **Continue** (AI Assistant)
   - Search for "Continue" in Extensions
   - Install and configure with your API keys

2. **Google Cloud Code** (for Gemini integration)
   - Search for "Google Cloud Code"
   - Install and sign in with your Google account

#### Configuration
1. Open Continue extension settings
2. Add your Anthropic API key for Claude
3. Google Cloud Code will use your Google account authentication

---

## 🐍 Python Development Setup

### Python & FastAPI Tools

You'll be building a Python FastAPI backend during the workshop.

#### Requirements
- Python 3.8 or higher
- pip package manager

#### Install FastAPI and dependencies
```bash
pip install fastapi uvicorn python-multipart websockets
```

#### Verify installation
```bash
python --version
pip list | grep fastapi
```

---

## ⚛️ Frontend Development Setup

### Node.js & React Tools

You'll be building a React frontend during the workshop.

#### Install Node.js
**macOS (Homebrew)**
```bash
brew install node
```

**Windows/Linux**
Download from [nodejs.org](https://nodejs.org/en/download/)

#### Install development tools
```bash
npm install -g create-react-app
npm install -g vite
```

#### Verify installation
```bash
node --version
npm --version
```

---

## 🔧 Additional Tools

### Git
Ensure Git is installed and configured:
```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### GitHub CLI (Optional but helpful)
```bash
# macOS
brew install gh

# Windows/Linux
# Download from https://cli.github.com/
```

---

## ✅ Pre-Workshop Checklist

Before the workshop, verify all tools are working:

### Terminal Check
```bash
# Modern terminal installed (Warp/iTerm2/Windows Terminal)
# Claude Code
claude --version

# Gemini CLI
gemini --version

# Development tools
python --version
node --version
git --version
```

### IDE Check
- [ ] Cursor/VS Code launches successfully
- [ ] AI features respond to prompts
- [ ] Can create and edit files
- [ ] Terminal integration works

### Account Requirements
- [ ] Claude subscription active OR API key set
- [ ] Google account authenticated with Gemini CLI
- [ ] GitHub account ready (for cloning repositories)

---

## 🆘 Troubleshooting

### Common Issues

**Claude Code authentication fails:**
- Verify your subscription is active at [claude.ai](https://claude.ai)
- Check API key is correctly set: `echo $ANTHROPIC_API_KEY`

**Gemini CLI not working:**
- Run `gemini` and follow the authentication prompts
- Verify Node.js version: `node --version` (must be 20+)
- Check if you have API quotas remaining

**Cursor/VS Code AI not responding:**
- Check API keys in settings
- Restart the application
- Verify internet connection

### Getting Help
If you encounter issues during installation:
1. Check the error messages carefully
2. Consult the official documentation links provided
3. Bring questions to the workshop - we'll have time for troubleshooting

---

## 📚 Useful Resources

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Anthropic Console](https://console.anthropic.com/)
- [Gemini CLI Repository](https://github.com/google-gemini/gemini-cli)
- [Google AI Studio](https://aistudio.google.com/)
- [Cursor Documentation](https://docs.cursor.com/)
- [VS Code Documentation](https://code.visualstudio.com/docs)
- [Continue Extension](https://marketplace.visualstudio.com/items?itemName=Continue.continue)

Ready to transform your development workflow with AI? See you at the workshop! 🚀