# Installation Guide for Vibe Coding Workshop

This guide provides step-by-step instructions for setting up all the tools you'll need for the workshop. Please complete all installations before the workshop begins.

## Table of Contents

1. [📟 Terminal Tools](#-terminal-tools)
   - [Warp (Recommended)](#warp-recommended)
   - [iTerm2 (macOS Alternative)](#iterm2-macos-alternative)
   - [Windows Terminal (Windows)](#windows-terminal-windows)
2. [🖥️ Vibecoding CLI Tools](#️-vibecoding-cli-tools)
   - [Claude Code](#claude-code)
   - [OpenAI Codex CLI](#openai-codex-cli)
   - [Gemini CLI](#gemini-cli)
3. [💻 IDEs & Code Editors](#-ides--code-editors)
   - [Cursor IDE (Primary Recommendation)](#cursor-ide-primary-recommendation)
   - [VS Code (Alternative Option)](#vs-code-alternative-option)
4. [🐳 Docker & Containerization](#-docker--containerization)
5. [🐳 Containerized Dev Environment](#-containerized-dev-environment-macos--windowswsl2)
6. [🐍 Python Development Setup](#-python-development-setup)
7. [⚛️ Frontend Development Setup](#️-frontend-development-setup)
8. [🔧 Additional Tools](#-additional-tools)
9. [🛠️ Optional Tools](#️-optional-tools)
10. [✅ Pre-Workshop Checklist](#-pre-workshop-checklist)
11. [🆘 Troubleshooting](#-troubleshooting)
12. [📚 Useful Resources](#-useful-resources)

## Overview

You'll need to install and configure:
- **Modern Terminal** - Warp (recommended) or iTerm2 for enhanced terminal experience
- **Claude Code** - Anthropic's official CLI tool (requires paid subscription or API key)
- **OpenAI Codex CLI** - OpenAI's official CLI for code generation and assistance
- **Gemini CLI** - Google's AI assistant via official CLI tool
- **Docker** - Container platform for development environments (required for ArchiBot projects)
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

## 🖥️ Vibecoding CLI Tools

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
claude
> /login
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

### OpenAI Codex CLI

OpenAI's official Codex CLI provides powerful AI assistance directly in your terminal for code generation, explanation, and debugging.

#### Requirements
- Node.js (for npm installation) or Homebrew (for macOS)
- ChatGPT Plus, Pro, Team, Edu, or Enterprise subscription (recommended)
- macOS or Linux (Windows support is experimental, WSL recommended)

#### Installation

**Option 1: npm (Recommended)**
```bash
npm install -g @openai/codex
```

**Option 2: Homebrew (macOS)**
```bash
brew install codex
```

#### Authentication

When you first run `codex`, you'll be prompted to authenticate:

**Option 1: ChatGPT Subscription (Recommended)**
For users with ChatGPT Plus/Pro/Team/Edu/Enterprise subscriptions:

1. Run `codex` in your terminal
2. You'll be prompted to authenticate via browser
3. Sign in with your ChatGPT account credentials
4. Grant permissions when prompted
5. Return to terminal - authentication should be complete

**Option 2: Platform API Key (Alternative)**
If you prefer using OpenAI Platform API keys:

1. Get an API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Set it as an environment variable:
   ```bash
   # macOS/Linux
   export OPENAI_API_KEY="your-platform-api-key"

   # Windows PowerShell
   $env:OPENAI_API_KEY = "your-platform-api-key"
   ```
3. Run `codex` - it should use the API key automatically

> **Note:** ChatGPT subscription authentication is recommended for workshop participants as it's simpler and doesn't require managing API keys.

#### Verification and First Use
```bash
# Launch Codex CLI
codex

# Test with a simple prompt
codex "explain this codebase"
```

#### Upgrade
```bash
# npm
npm install -g @openai/codex@latest

# Homebrew
brew upgrade codex
```

> **Note:** For detailed documentation, visit the [OpenAI Codex GitHub repository](https://github.com/openai/codex)

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

## 🐳 Docker & Containerization

Docker is **required** for the workshop, especially when working with ArchiBot (Step 3) which creates Docker-based development environments for scaffolded projects.

### Why Docker is Required

- **ArchiBot Projects**: ArchiBot automatically creates `docker-compose.yml` files for all scaffolded projects
- **Consistent Development Environment**: Ensures all team members have identical setups
- **Simplified Dependencies**: Database, Redis, and service dependencies run in containers
- **Production Parity**: Local development mirrors production deployment

### Installation

#### macOS
**Option 1: Docker Desktop (Recommended)**
1. Download from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Install Docker Desktop
3. Launch and complete setup

**Option 2: Homebrew**
```bash
brew install --cask docker
```

#### Windows
**Option 1: Docker Desktop with WSL2 (Recommended)**
1. Install WSL2: `wsl --install`
2. Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/)
3. Install with WSL2 backend enabled

**Option 2: Package Manager**
```powershell
# Using winget
winget install Docker.DockerDesktop

# Using Chocolatey
choco install docker-desktop
```

#### Linux (Ubuntu/Debian)
```bash
# Install Docker Engine
sudo apt-get update
sudo apt-get install docker.io docker-compose-plugin

# Add user to docker group
sudo usermod -aG docker $USER

# Log out and back in, then verify
docker --version
docker compose version
```

### Verification
After installation, verify Docker is working:

```bash
# Check Docker version
docker --version

# Check Docker Compose
docker compose version

# Test Docker is running
docker run hello-world
```

### Required Versions
- **Docker**: 20.x or higher
- **Docker Compose**: v2.x (note: `docker compose`, not `docker-compose`)

### Troubleshooting
**Docker Desktop won't start:**
- Ensure virtualization is enabled in BIOS/UEFI
- On Windows: Verify WSL2 is installed and set as default

**Permission denied errors (Linux):**
```bash
sudo usermod -aG docker $USER
# Log out and back in
```

**Old docker-compose command:**
Use `docker compose` (space) instead of `docker-compose` (hyphen) for v2

---

## 🐳 Containerized Dev Environment (macOS & Windows/WSL2)

Prefer a one-and-done setup? Use the Docker dev container. It includes GitHub CLI, Node 20, Gemini CLI, Claude Code, Cursor **CLI**, OpenAI Codex CLI, and **VS Code in your browser** (code-server).  
> If you use the container, you can skip most native installs above.

### Prerequisites
- Docker Desktop
- **Windows only:** WSL2 with Ubuntu (`wsl --install -d Ubuntu`)
- A browser (to open `http://localhost:8080`)

### Repo Layout (root)
```

Dockerfile
docker-compose.yml
docker-compose.wsl.yml
.env                # NOT committed
.env.example        # committed (placeholders)

````

### Create `.env`
```dotenv
CODE_SERVER_PASSWORD=StrongPassword123!
WORKSPACE_HOST_DIR=.    # host folder to mount at /workspace (optional)

# Optional keys used inside the container:
GEMINI_API_KEY=
ANTHROPIC_API_KEY=
OPENAI_API_KEY=
GITHUB_TOKEN=
````

### Quick Start (from repo root)

```bash
# Clean old containers/volumes (avoids stale passwords/config):
docker compose -f docker-compose.yml -f docker-compose.wsl.yml down -v

# Build & run:
docker compose -f docker-compose.yml -f docker-compose.wsl.yml up -d --build
```

Open the editor:

* macOS: `open http://localhost:8080`
* Linux: `xdg-open http://localhost:8080`
* WSL: `wslview http://localhost:8080`

**Windows tips:** keep the repo **inside WSL** (e.g., `~/projects/app`) for fast I/O and run the commands from the WSL Ubuntu shell.

### Verify (in the code-server terminal)

```bash
git --version && node --version && npm --version && gh --version
gemini --version || gemini --help
claude --version || claude --help
which code && code --version      # 'code' maps to code-server
ls -la /workspace                 # should show your project files
```

### Stop / Reset

```bash
docker compose -f docker-compose.yml -f docker-compose.wsl.yml down
# Reset code-server config/extensions:
docker compose -f docker-compose.yml -f docker-compose.wsl.yml down -v
```

### Troubleshooting

* **Login loop:** ensure `.env` has `CODE_SERVER_PASSWORD=…`, then `down -v` and `up -d --build`.
* **Port busy:** change `ports:` in `docker-compose.wsl.yml` (e.g., `127.0.0.1:9090:8080`) and open `http://localhost:9090`.
* **Slow on Windows:** move the repo into WSL and run compose there.

---

## 🐍 Python Development Setup

### Python & FastAPI Tools

You'll be building a Python FastAPI backend during the workshop.

#### Requirements
- Python 3.8 or higher
- pip package manager
- Conda (recommended for virtual environments)

#### Install Conda (Recommended)

**Option 1: Miniconda (Lightweight)**
```bash
# macOS/Linux
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh

# Windows
# Download from: https://docs.conda.io/en/latest/miniconda.html
```

**Option 2: Anaconda (Full Distribution)**
Download from [anaconda.com](https://www.anaconda.com/download)

**Option 3: Package Managers**
```bash
# macOS
brew install --cask miniconda

# Windows (Chocolatey)
choco install miniconda3

# Windows (winget)
winget install Anaconda.Miniconda3
```

#### Setup Virtual Environment with Conda
```bash
# Create a new environment for the workshop
conda create -n vibe-coding python=3.11

# Activate the environment
conda activate vibe-coding

# Verify Python version
python --version
```

#### Install FastAPI and dependencies
```bash
# With the conda environment activated
pip install fastapi uvicorn python-multipart websockets

# Or using conda
conda install -c conda-forge fastapi uvicorn
pip install python-multipart websockets
```

#### Verify installation
```bash
python --version
pip list | grep fastapi
conda list | grep fastapi
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

## 🛠️ Optional Tools

These tools are not required but can significantly enhance your development experience, especially when working with AI coding assistants.

### ripgrep (Highly Recommended)

A blazing fast command-line search tool that dramatically improves performance with AI coding tools like OpenAI Codex, Claude Code, and other AI assistants. It's much faster than traditional grep and provides better search capabilities for large codebases.

**Why you need it:**
- 10-100x faster than grep for code searches
- Essential for AI tools to quickly understand your codebase
- Better integration with modern IDEs and AI assistants
- Improves response time when AI tools analyze your project

**Installation:**

**macOS (Homebrew):**
```bash
brew install ripgrep
```

**Ubuntu/Debian:**
```bash
sudo apt install ripgrep
```

**Windows:**
```bash
# Using Chocolatey
choco install ripgrep

# Using winget
winget install BurntSushi.ripgrep.MSVC
```

**Alternative:** Download from [GitHub releases](https://github.com/BurntSushi/ripgrep/releases)

**Verification:**
```bash
rg --version
```

**Quick test:**
```bash
# Search for "function" in your codebase
rg "function" --type js
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

# Docker (Required for ArchiBot)
docker --version
docker compose version
docker run hello-world

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

### Docker Check
- [ ] Docker Desktop running (if using Docker Desktop)
- [ ] `docker run hello-world` succeeds
- [ ] `docker compose version` shows v2.x
- [ ] No permission errors when running docker commands

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

**Docker issues:**
- Ensure Docker Desktop is running (if using Docker Desktop)
- Check Docker daemon is running: `docker ps`
- Permission errors on Linux: `sudo usermod -aG docker $USER` (then log out/in)
- WSL2 issues on Windows: Verify WSL2 is default (`wsl --set-default-version 2`)

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
- [OpenAI Codex GitHub repository](https://github.com/openai/codex)

Ready to transform your development workflow with AI? See you at the workshop! 🚀
