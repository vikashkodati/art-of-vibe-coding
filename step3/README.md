# Step 3: Architecture Sub-Agent (Claude Code)

In Step 3, we'll go deeper into the software development process by introducing an architecture-focused sub-agent in Claude Code. This agent will help with system decomposition, boundaries, data flow, and non-functional requirements.

## About ArchiBot

ArchiBot is an **opinionated architecture assistant** based on the author's experience building production software systems. It specializes in:

- **Frontend**: React-based applications (Next.js, Vite)
- **Backend**: Python ecosystems (FastAPI for APIs, Django for full-stack)
- **Architecture Patterns**: Three battle-tested approaches for different team skills and project requirements

ArchiBot doesn't just recommend technologies—it **scaffolds complete project structures** with:
- Production-ready configurations
- CI/CD pipelines
- Security best practices
- Monitoring and observability
- Development workflows and templates
- **Coding standards and conventions**
- **Sub-agent templates** for frontend and backend development

**Important Notes:**
1. This is **not a comprehensive or the world's best** architecture agent. The purpose of this step is to demonstrate a **user-level agent** and showcase the idea of **higher-level prompts**.
2. ArchiBot includes numerous **good software engineering practices** to help build **ready-to-productionize** projects.
3. Based on user requirements, it will recommend the best architecture pattern and scaffold the entire project structure for you.

The goal is to get you from requirements to a deployable, maintainable application as quickly as possible, while following industry best practices.

### ArchiBot's Three Architecture Patterns

ArchiBot recommends one of three proven patterns based on your team's skills and project requirements:

**Pattern A: Python-First (Django ASGI)**
- Best for: Python-strong teams, compliance requirements, complex background jobs
- Stack: Django + React + PostgreSQL + Celery
- Complexity: High | Deployment: Moderate

**Pattern B: All-TypeScript (Next.js + Supabase)**
- Best for: Frontend-heavy teams, rapid prototyping, simple deployment
- Stack: Next.js + Supabase + Vercel
- Complexity: Low | Deployment: Very Easy

**Pattern C: Hybrid (Next.js + Python AI Service)**
- Best for: Mixed TS/Python skills, leveraging Python AI libraries
- Stack: Next.js + FastAPI + Supabase + containerized services
- Complexity: Moderate-High | Deployment: Moderate

ArchiBot interviews you about your project requirements and automatically selects the best pattern, then scaffolds the entire project structure.

## Table of Contents

- [About ArchiBot](#about-archibot)
  - [ArchiBot's Three Architecture Patterns](#archibots-three-architecture-patterns)
- [Prerequisites](#prerequisites)
- [Workshop Sections](#workshop-sections)
  - [Quick Recap: Create a Sub‑Agent in Claude Code](#quick-recap-create-a-sub-agent-in-claude-code)
  - [Install ArchiBot in Claude Code (User‑Level)](#install-archibot-in-claude-code-user-level)
  - [Install ArchiBot as a Gemini CLI Custom Command](#install-archibot-as-a-gemini-cli-custom-command)
  - [Create the Main Workshop Project with ArchiBot](#create-the-main-workshop-project-with-archibot)
  - [Hands-On Exercise: Create Your Own Project (20 minutes)](#-hands-on-exercise-create-your-own-project-20-minutes)
- [Workshop Checklist](#workshop-checklist)

## Prerequisites

Before using ArchiBot, ensure you have the following tools installed:

### Required Tools
- **Node.js** (>= 18.17): [Download from nodejs.org](https://nodejs.org/)
- **Python** (>= 3.11): [Download from python.org](https://python.org/)
- **Docker** (>= 20.x) with Docker Compose v2: [Download from docker.com](https://www.docker.com/get-started/)

### Verify Installation
Run these commands to verify your setup:

```bash
# Check Node.js version
node -v

# Check Python version
python3 --version

# Check Docker and Docker Compose
docker --version
docker compose version
```

### Optional Tools
- **Make**: For simplified development commands (can use npm scripts as alternative)

**Note**: ArchiBot creates Docker-based development environments with `docker-compose.yml` files, so Docker is essential for the scaffolded projects to work properly.

---

## Workshop Sections

## Quick Recap: Create a Sub‑Agent in Claude Code

Follow Claude Code’s Quick Start flow to create a sub‑agent via the built‑in Agent Manager:

1. Launch Claude Code in your project directory:
   ```bash
   claude
   ```
2. Open the Agents/Sub‑agents manager in Claude Code.
3. Create a new sub‑agent: give it a clear name and concise purpose/instructions (what it specializes in and how it should work).
4. Save the agent, then switch to it to run tasks in your user context so that is is available across all your projects.


Reference: Claude Docs — Subagents (Quick Start)
https://docs.claude.com/en/docs/claude-code/sub-agents#quick-start

---

More detailed setup (agent definition and prompts) coming next.

## Install ArchiBot in Claude Code (User‑Level)

Make ArchiBot available across all your projects by installing it at the user level.

Option A — Using Claude Code UI (recommended)
- Open Claude Code in any project: `claude`
- Open the Agents/Sub‑agents manager
- Add new sub‑agent
  - Name: ArchiBot (Architecture Decisioning)
  - Paste contents of `step3/archibot-agent.md` into the agent’s instructions/definition field
  - Save the agent
- Switch to ArchiBot to verify it works
- Optional: Export the agent configuration for backup/share

Option B — Manual install to Claude user directory
- Create an agents folder under your Claude user config if it doesn’t exist
  - macOS/Linux:
    - `mkdir -p ~/.claude/agents`
    - `cp step3/archibot-agent.md ~/.claude/agents/archibot-agent.md`
  - Windows (PowerShell):
    - `New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\agents" | Out-Null`
    - `Copy-Item step3/archibot-agent.md "$env:USERPROFILE\.claude\agents\archibot-agent.md"`
- Restart Claude Code so it picks up user‑level agents
- Open the Agents/Sub‑agents manager and confirm ArchiBot appears

Note: Exact user‑config paths can vary by installation. If `~/.claude/agents` is not recognized in your setup, use Option A (UI) to import/paste the agent definition, then export from the UI to persist it.

## Install ArchiBot as a Gemini CLI Custom Command

Make ArchiBot callable from any project as a reusable slash command.

**Step 1: Create the ArchiBot Command Directory**

For global availability across all projects:
```bash
mkdir -p ~/.gemini/commands
```

For project-specific availability:
```bash
mkdir -p .gemini/commands
```

**Step 2: Create the ArchiBot Command File**

Create `~/.gemini/commands/archibot.toml` (for global) or `.gemini/commands/archibot.toml` (for project):

```bash
# Copy the provided template
cp step3/archibot.toml ~/.gemini/commands/archibot.toml

# Or copy the content manually
cat step3/archibot.toml
```

The complete `archibot.toml` file is provided in this step's directory and contains:
- Full ArchiBot persona and capabilities
- Interview strategy and key questions
- All three architecture patterns (Python-First, All-TypeScript, Hybrid)
- Architecture selection rubric
- Complete conversation flow
- Project scaffolding instructions

**Step 3: Test the Command**

Restart Gemini CLI and test:
```bash
gemini
/archibot
```

**Step 4: Verify Command Installation**

List available commands to confirm:
```bash
# In Gemini CLI
/help
```

Notes
- Keeping the command global ensures ArchiBot is available in all future projects without re-creation.
- If your CLI version doesn't support a global scope toggle, create the command once in a neutral directory and export it so you can re-import elsewhere on demand.

---

## Create the Main Workshop Project with ArchiBot

Now that ArchiBot is installed in both Claude Code and Gemini CLI, let's use it to create our main workshop project: an AI chat application. This will demonstrate ArchiBot's architecture decisioning and project scaffolding capabilities.

### Project Overview

We'll build an AI chat application that showcases:
- Real-time chat interface with AI responses
- Multiple AI model support (Claude, OpenAI, Gemini)
- Message history and conversation management
- Modern, responsive UI
- Production-ready architecture

### Using Claude Code ArchiBot

**Step 1: Launch Claude Code with ArchiBot**

Navigate to your workshop directory and start Claude Code:

```bash
cd /path/to/your/workshop/directory
claude
```

**Step 2: Activate ArchiBot Agent**

If ArchiBot doesn't activate automatically, explicitly request it:

```
Use the ArchiBot agent to help me create a new AI chat application project.
```

**Step 3: Project Requirements Interview**

When ArchiBot starts its interview, provide these responses to guide it toward the optimal architecture:

**Application Type & Users:**
```
I'm building an AI chat application - a SaaS tool for developers and teams to interact with multiple AI models (Claude, OpenAI, Gemini) in a single interface. Target users are B2B technical teams and individual developers.
```

**Scale & Monetization:**
```
Expected users: 1K-10K in first year. Planning a freemium model with usage-based paid tiers for advanced features and higher API limits.
```

**Technical Requirements:**
```
Team skills: Strong in Python for AI integrations and TypeScript/React for frontend. Timeline: 1-2 months for MVP. Need web platform initially, mobile later.

AI capabilities needed: Text chat with multiple providers, conversation history, real-time streaming responses. Will need background processing for usage analytics and billing.
```

**Infrastructure & UX:**
```
Auth: OAuth with Google/GitHub for developer users. Payments: Stripe for subscription billing. Email: Transactional emails for usage notifications. Design: Modern Tailwind-based system, clean chat interface.
```

### Using Gemini CLI ArchiBot

Alternatively, you can use the Gemini CLI version:

**Step 1: Launch Gemini CLI**

```bash
gemini
```

**Step 2: Use ArchiBot Command**

```
/archibot
```

**Step 3: Provide Same Requirements**

Follow the same interview responses as above.

### Expected Architecture Recommendation

Based on these requirements, ArchiBot should recommend either:

**Option A: Pattern C (Hybrid) - Most Likely**
- Next.js + Supabase for the main application
- Separate Python FastAPI service for AI integrations
- Optimal for: TypeScript frontend velocity + Python AI ecosystem

**Option B: Pattern B (All-TypeScript) - Alternative**
- Next.js + Supabase with JavaScript AI SDKs
- Simpler deployment, faster iteration
- Good for: Teams prioritizing speed over Python AI libraries

### Project Creation Process

**Step 1: Review Architecture Proposal**

ArchiBot will present a detailed architecture document with:
- System diagrams showing data flow
- Technology stack with rationale
- Deployment strategy and timeline estimates

**Step 2: Approve and Customize**

After reviewing, approve the architecture and customize specific technologies:
- Confirm FastAPI for AI service (if Hybrid pattern)
- Choose Tailwind for design system
- Select specific AI providers to integrate
- Confirm authentication and payment preferences

**Step 3: Watch the Magic Happen**

ArchiBot will create a complete project structure:

```
ai-chat-workshop/
├── README.md                    # Complete setup guide
├── AI_CONTEXT.md               # Project context for AI assistants
├── CODING_STANDARDS.md         # Development guidelines
├── PLAN.md                     # Feature development roadmap
├── docker-compose.yml          # Local development environment
├── .env.example               # Environment configuration
├── frontend/                  # Next.js application
│   ├── components/            # React components
│   ├── app/                   # App router pages
│   └── lib/                   # Utilities and hooks
├── ai-service/                # Python FastAPI service (if Hybrid)
│   ├── app/                   # FastAPI application
│   ├── models/                # AI provider integrations
│   └── requirements.txt       # Python dependencies
├── .github/workflows/         # CI/CD pipelines
└── templates/                 # Development templates
```

### Immediate Next Steps

After ArchiBot completes the scaffolding:

**Step 1: Start Development Environment**

```bash
cd ai-chat-workshop
make dev-up
# or
npm run dev
```

**Step 2: Verify Everything Works**

- Frontend should be running on localhost:3000
- AI service (if applicable) on localhost:8000
- Database and Redis containers started

**Step 3: Begin Feature Development**

Follow the generated `PLAN.md` to build features incrementally:
1. Basic chat interface
2. AI provider integration
3. Authentication setup
4. Message persistence
5. Real-time streaming

### Learning Objectives

This exercise demonstrates:
- **AI-Assisted Architecture Decisions**: How to use AI to choose optimal tech stacks
- **Rapid Project Scaffolding**: From requirements to working development environment in minutes
- **Production-Ready Setup**: Includes CI/CD, monitoring, and deployment configurations
- **AI Assistant Integration**: Generated `AI_CONTEXT.md` helps future AI interactions understand the project

### Troubleshooting

**ArchiBot not activating?**
- Make sure you're using the correct agent name
- Try explicitly mentioning "ArchiBot" or "architecture" in your request

**Different architecture recommended?**
- ArchiBot's recommendations depend on your specific answers
- You can ask it to explain why it chose a particular pattern
- Request to see alternative architectures if needed

**Project creation fails?**
- Check you have the required tools installed (Node.js, Python, Docker)
- Ensure you're in a directory where you have write permissions
- Verify the project name doesn't conflict with existing directories

Ready to build your AI chat application with enterprise-grade architecture? Let ArchiBot guide the way! 🚀

---

## 🎯 Hands-On Exercise: Create Your Own Project (20 minutes)

Now it's your turn! Use ArchiBot to create a project of your choice and get it running locally.

### Exercise Goals
- Practice using ArchiBot for architecture decisions
- Experience the complete project scaffolding process
- Get a working development environment running
- Explore the generated project structure and documentation

### Time Allocation
- **5 minutes**: Project planning and ArchiBot interview
- **10 minutes**: Project creation and initial setup
- **5 minutes**: Verification and exploration

### Step-by-Step Instructions

#### Step 1: Choose Your Project Idea (2 minutes)
Pick one of these project ideas or come up with your own:

**Option A: Personal Finance Tracker**
- AI-powered expense categorization
- Receipt scanning and data extraction
- Budget recommendations and insights
- Target users: Individuals managing personal finances

**Option B: Code Documentation Assistant**
- AI-powered code analysis and documentation generation
- Integration with Git repositories
- Automated README and API doc creation
- Target users: Development teams

**Option C: Learning Companion**
- AI tutoring for programming concepts
- Personalized learning paths
- Code challenge generation and evaluation
- Target users: Students and junior developers

**Option D: Your Own Idea**
- Think of an AI-enabled application you'd like to build
- Consider: What problem does it solve? Who uses it? What AI features?

#### Step 2: Launch ArchiBot (1 minute)

**Using Claude Code:**
```bash
# Navigate to your workshop directory
cd /path/to/your/workshop/directory

# Launch Claude Code
claude

# Request ArchiBot (if not auto-activated)
Use the ArchiBot agent to help me create a new project.
```

**Using Gemini CLI:**
```bash
# Launch Gemini CLI
gemini

# Use ArchiBot command
/archibot
```

#### Step 3: ArchiBot Interview (5 minutes)
Answer ArchiBot's questions thoughtfully. Here are some tips:

**For Application Type & Users:**
- Be specific about your target audience
- Mention if it's B2C, B2B, or internal use
- Give realistic user scale estimates

**For Technical Requirements:**
- Mention your team's strongest skills (Python, TypeScript, etc.)
- Be honest about timeline (suggest 1-2 months for MVP)
- List specific AI features you want

**For Infrastructure:**
- Choose simple auth (Google OAuth) for quick setup
- Consider if you need payments (most workshop projects won't)
- Pick modern design system (Tailwind for custom look)

#### Step 4: Review Architecture Recommendation (2 minutes)
- Read through ArchiBot's architecture proposal carefully
- Ask questions if anything is unclear
- Approve the architecture to proceed with scaffolding

#### Step 5: Project Creation (3 minutes)
- Let ArchiBot create the complete project structure
- Watch for any errors during file creation
- Note the generated directory structure

#### Step 6: Start Development Environment (5 minutes)
Navigate to your new project and start the development environment:

```bash
# Enter your project directory
cd your-project-name

# Start the development environment
# Option 1: Using Make (if available)
make dev-up

# Option 2: Using npm and Docker
npm run dev
# In another terminal:
docker compose up -d

# Option 3: Manual startup
# Start database and services
docker compose up -d
# Start frontend (in project/frontend/ if applicable)
npm install && npm run dev
# Start backend (in project/backend/ if applicable)
pip install -r requirements.txt && uvicorn app.main:app --reload
```

#### Step 7: Verification (3 minutes)
Verify everything is working:

```bash
# Check running containers
docker ps

# Test frontend (if applicable)
# Open http://localhost:3000 in browser

# Test backend API (if applicable)
# Open http://localhost:8000/docs in browser

# Check generated documentation
cat README.md
cat AI_CONTEXT.md
cat CODING_STANDARDS.md
```

#### Step 8: Explore Generated Structure (2 minutes)
Take a quick look at what ArchiBot created:

```bash
# View project structure
tree -L 3 .

# Check sub-agent templates
ls -la .claude/agents/

# Look at development templates
ls -la templates/

# Check configuration files
ls -la *.yml *.json *.md
```

### Success Criteria
By the end of the exercise, you should have:
- [ ] Successfully completed ArchiBot interview
- [ ] Generated a complete project structure
- [ ] Started the development environment without errors
- [ ] Accessed running frontend and/or backend
- [ ] Reviewed generated documentation and standards

### Common Issues & Quick Fixes

**ArchiBot not responding:**
- Try explicitly mentioning "ArchiBot" or "architecture" in your request
- Ensure you're in the correct agent/command mode

**Docker containers won't start:**
- Check Docker Desktop is running: `docker ps`
- Review logs: `docker compose logs`
- Try rebuilding: `docker compose down && docker compose up --build`

**Port conflicts:**
- Check what's running on ports 3000/8000: `lsof -i :3000`
- Modify ports in docker-compose.yml if needed

**Permission errors:**
- Ensure your user has Docker permissions
- Try: `sudo usermod -aG docker $USER` (then restart terminal)

### Bonus Challenges (If Time Permits)
1. **Explore Sub-Agents**: Try using the generated frontend/backend developer agents
2. **Make a Small Change**: Add a simple feature using the project's coding standards
3. **Test CI/CD**: Push to GitHub and see the generated workflows in action

### Reflection Questions
- How did ArchiBot's architecture choice compare to what you would have chosen?
- What surprised you about the generated project structure?
- How useful are the generated coding standards and documentation?
- Would you use this approach for your real projects?

### Share Your Results
If you're comfortable, share:
- What project you created
- Which architecture pattern ArchiBot recommended
- Any interesting insights from the generated structure
- How long it took to get everything running

**Time Check**: Aim to have a running development environment by the 15-minute mark, leaving 5 minutes for exploration and questions!

---

## 🎉 Congratulations!

You've successfully completed Step 3 and experienced the power of AI-assisted architecture decisions. You now have:

1. ✅ Understanding of ArchiBot's opinionated approach
2. ✅ Experience with the complete project scaffolding process
3. ✅ A working project with production-ready structure
4. ✅ Hands-on experience with Docker-based development environments
5. ✅ Generated sub-agents for ongoing development

**Next Steps**: Use your generated project as a foundation for further development, or apply these patterns to your real-world projects!

---

## Workshop Checklist

Use this checklist to track your progress through Step 3:

### 📋 Pre-Workshop Setup
- [ ] **Prerequisites verified**: Node.js, Python, Docker all installed and working
- [ ] **Claude Code authenticated**: Can run `claude --version` successfully
- [ ] **Gemini CLI working**: Can run `gemini --version` successfully
- [ ] **Docker functional**: `docker run hello-world` executes without errors

### 🤖 ArchiBot Installation
- [ ] **Method chosen**: Decided between Claude Code user-level or Gemini CLI custom command
- [ ] **Agent installed**: ArchiBot available and accessible
- [ ] **Initial test**: ArchiBot responds to architecture questions

### 🏗️ Main Workshop Project (Optional Demo)
- [ ] **ArchiBot interview completed**: Provided AI chat application requirements
- [ ] **Architecture recommended**: Received Pattern A, B, or C recommendation
- [ ] **Project scaffolded**: Complete directory structure created
- [ ] **Development environment started**: Frontend and/or backend running
- [ ] **Generated files explored**: Reviewed README, CODING_STANDARDS, AI_CONTEXT files

### 🎯 Hands-On Exercise (20 minutes)
#### Planning Phase (5 minutes)
- [ ] **Project idea selected**: Chose from provided options or created custom idea
- [ ] **ArchiBot launched**: Successfully activated ArchiBot agent
- [ ] **Interview completed**: Answered all ArchiBot questions thoughtfully
- [ ] **Architecture approved**: Reviewed and accepted recommended pattern

#### Implementation Phase (10 minutes)
- [ ] **Project created**: ArchiBot generated complete project structure
- [ ] **Directory verified**: Project folder created with proper structure
- [ ] **Dependencies started**: Database and services running via Docker
- [ ] **Frontend accessible**: Can reach frontend in browser (if applicable)
- [ ] **Backend accessible**: Can reach API documentation (if applicable)

#### Exploration Phase (5 minutes)
- [ ] **Documentation reviewed**: Read generated README and standards
- [ ] **Sub-agents found**: Located `.claude/agents/` directory with developer agents
- [ ] **Templates explored**: Checked `templates/` folder for development workflows
- [ ] **Structure understood**: Familiar with generated directory organization

### 🎉 Completion Criteria
- [ ] **Working project**: Full development environment running locally
- [ ] **Architecture understanding**: Can explain why ArchiBot chose specific pattern
- [ ] **Generated assets utilized**: Familiar with coding standards and sub-agents
- [ ] **Personal reflection**: Considered how to apply this to real projects

### 🚀 Bonus Achievements
- [ ] **Sub-agent tested**: Tried using generated frontend or backend developer agent
- [ ] **Feature added**: Made a small change following project standards
- [ ] **Customization applied**: Modified configuration or settings
- [ ] **Team sharing**: Discussed results with other workshop participants

### 📝 Key Takeaways
Record your insights from Step 3:

**Which architecture pattern did ArchiBot recommend for your project?**
```
□ Pattern A (Python-First)  □ Pattern B (All-TypeScript)  □ Pattern C (Hybrid)
```

**What surprised you most about the generated project structure?**
```
_____________________________________________________________
```

**How would you rate ArchiBot's usefulness for your real projects? (1-5)**
```
□ 1 (Not useful)  □ 2  □ 3  □ 4  □ 5 (Very useful)
```

**What would you change or improve about ArchiBot?**
```
_____________________________________________________________
```

---

### 🔄 What's Next?

After completing Step 3, you should have:
1. ✅ Hands-on experience with AI-assisted architecture decisions
2. ✅ A working project with production-ready structure
3. ✅ Understanding of opinionated vs. comprehensive AI agents
4. ✅ Practical knowledge of Docker-based development environments
5. ✅ Sub-agents ready for ongoing development

**Ready for Step 4?** You'll use these generated projects and sub-agents to dive deeper into AI-assisted feature development!
