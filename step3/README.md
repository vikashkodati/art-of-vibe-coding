# Step 3: Architecture Sub-Agent (Claude Code)

In Step 3, we’ll go deeper into the software development process by introducing an architecture-focused sub-agent in Claude Code. This agent will help with system decomposition, boundaries, data flow, and non-functional requirements.

## Table of Contents

- [Quick Recap: Create a Sub‑Agent in Claude Code](#quick-recap-create-a-sub-agent-in-claude-code)
- [Install ArchiBot in Claude Code (User‑Level)](#install-archibot-in-claude-code-user-level)
- [Install ArchiBot as a Gemini CLI Custom Command](#install-archibot-as-a-gemini-cli-custom-command)

## Quick Recap: Create a Sub‑Agent in Claude Code

Follow Claude Code’s Quick Start flow to create a sub‑agent via the built‑in Agent Manager:

1. Launch Claude Code in your project directory:
   ```bash
   claude
   ```
2. Open the Agents/Sub‑agents manager in Claude Code.
3. Create a new sub‑agent: give it a clear name and concise purpose/instructions (what it specializes in and how it should work).
4. Save the agent, then switch to it to run tasks in your current project context.
5. Optional: export the agent configuration for reuse across projects.

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

Option A — Create via Gemini CLI (recommended)
1) Launch Gemini CLI in any project directory:
   ```bash
   gemini
   ```
2) In Gemini, paste this prompt to create a global command:
   ```
   I want to create a custom slash command called /archibot that acts as an Architecture Decisioning assistant. It should:
   - Interview me briefly to gather requirements
   - Propose one of three architecture patterns with rationale
   - Output concise docs and mermaid diagrams
   - After approval, scaffold a project structure under a new subdirectory with README, env, docker, templates, and CI basics
   Use the following document as the base instruction/spec. Incorporate its structure and behavior:
   [PASTE CONTENTS OF step3/archibot-agent.md HERE]

   Please set this command as global (available across all projects), provide a short help/description, and confirm how to run and edit it later.
   ```
3) Confirm the command is registered and global. Ask Gemini:
   ```
   Show me how to list, edit, and export my custom slash commands. Verify /archibot is available globally.
   ```
4) Test it:
   ```
   /archibot
   ```

Option B — Import or save manually (when supported)
- Some Gemini CLI builds support exporting/importing commands or storing them in a user config directory. If available on your version, ask Gemini:
  ```
  Where are custom slash commands stored on this system, and how do I import one from a file? I want /archibot to be available globally.
  ```
- Follow its instructions to import a command backed by the contents of `step3/archibot-agent.md` and mark it global. Then restart Gemini CLI and verify `/archibot` appears in the commands list.

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
