# Step 1: Hello World of Vibe Coding - Recipe Sharing App

Welcome to your first vibe coding experience! In this step, you'll use Claude Code to generate a complete React application for sharing recipes with a waitlist signup homepage.

## Table of Contents

- [What You'll Build](#what-youll-build)
- [Prerequisites](#prerequisites)
- [Instructions](#instructions)
  - [0. Create a Workspace Subdirectory (Recommended)](#0-create-a-workspace-subdirectory-recommended)
  - [1. Launch Claude Code](#1-launch-claude-code)
  - [2. Generate the Recipe Sharing App](#2-generate-the-recipe-sharing-app)
  - [3. Review the Generated Code](#3-review-the-generated-code)
  - [4. Initialize Project Memory](#4-initialize-project-memory)
  - [5. Make Your First Modification](#5-make-your-first-modification)
  - [6. Get a Code Review with Gemini CLI](#6-get-a-code-review-with-gemini-cli)
  - [7. Customize Project Memory](#7-customize-project-memory)
- [Expected Outcome](#expected-outcome)
- [Next Steps](#next-steps)
- [Tips for Success](#tips-for-success)
- [Troubleshooting](#troubleshooting)
- [Appendix: Sophisticated Prompts](#appendix-sophisticated-prompts)

## What You'll Build

A simple recipe sharing web application with:
- Homepage with waitlist signup form
- Clean, modern design
- Basic recipe sharing functionality
- Responsive layout

## Prerequisites

- Claude Code installed and authenticated
- Cursor IDE or VS Code ready
- Basic familiarity with terminal/command line

---

## Instructions

### 0. Create a Workspace Subdirectory (Recommended)

To keep this repo tidy and isolate Claude Code's project memory, create and work from a fresh subdirectory inside `step1/`:

```bash
# from the repo root
mkdir -p step1/recipe-sharing-app && cd $_
```

You can choose any folder name. This directory will contain the generated app and the `.claude/` project memory.

### 1. Launch Claude Code

From your workspace directory, start Claude Code in interactive mode:

```bash
claude
```

### 2. Generate the Recipe Sharing App

Use this prompt with Claude Code to generate your React application:

```
Create a React web application for sharing recipes. The homepage should feature a waitlist signup form.
```

For more sophisticated prompts, see Appendix: [Sophisticated Prompts](#appendix-sophisticated-prompts).

### 3. Review the Generated Code

After Claude Code generates the application:

1. Ask Claude Code to install all dependencies and start the application on port 5000 (from the current project directory):
   ```
   Install all npm dependencies in this directory and start the development server on port 5000
   ```
2. Open the current project directory in Cursor or your preferred IDE
3. Explore the file structure and generated components
4. Review the code quality and structure
5. Test the running application in your browser at `http://localhost:5000`

**Alternative commands you can try with Claude Code:**
```
Run npm install in this project directory
```

```
Start the React development server on port 5000
```

```
Show me the package.json file and start the app
```

### 4. Initialize Project Memory

Launch Claude Code and initialize project memory from the project directory:

```bash
claude
/init
```

This creates a `.claude/` directory with project context that Claude Code will use for future interactions.

### 5. Make Your First Modification

Now let's experience the power of vibe coding by making a simple modification to your webpage. With Claude Code still running in your project directory, try one of these modifications:

**Option A: Change the Color Scheme**
```
Change the primary color of the homepage from the current color to a warm orange theme that matches a cooking/food vibe
```

**Option B: Add a Feature Section**
```
Add a new section below the waitlist signup that showcases 3 key features of the recipe sharing platform with icons and descriptions
```

**Option C: Enhance the Hero Section**
```
Add a subtitle under the main headline that says "Join thousands of home cooks sharing their favorite recipes" and make the call-to-action button more prominent
```

Choose one modification that interests you and watch Claude Code make the changes! After the modification:

1. Check that the changes appear correctly in your browser (refresh if needed)
2. Review the code changes that were made
3. Try asking Claude Code to explain what it changed

### 6. Get a Code Review with Gemini CLI

Now let's get a fresh perspective on your code using Gemini CLI. This demonstrates how different AI tools can provide valuable insights.

**Setup: Open Two Terminals Side by Side**
1. Keep your current terminal with Claude Code running
2. Open a second terminal window/tab and position it side by side
3. In the second terminal, navigate to your project directory:
   ```bash
   cd recipe-sharing-app
   ```
4. Launch Gemini CLI:
   ```bash
   gemini
   ```

**Get Code Review from Gemini**

Use this prompt with Gemini CLI:

```
You are a senior React developer well versed with modern React development, component architecture, performance optimization, accessibility, and code quality best practices. Review this code critically and provide your honest feedback. Organize your feedback by severity (Critical, High, Medium, Low). Include specific suggestions for improvement.
```

**Cross-Reference the Feedback**

After Gemini provides its code review:

1. Copy the entire feedback from Gemini
2. Switch back to your Claude Code terminal
3. Paste the feedback with this prompt:

```
My colleague reviewed the code and gave this feedback: [PASTE GEMINI'S FEEDBACK HERE]

Do you agree with this feedback? Be honest. What do you think? Should we implement any of these suggestions?
```

**Observe the AI Dialogue**
- Notice how Claude Code responds to external feedback
- See if there are any disagreements between the AI tools
- Consider which suggestions make the most sense for your project

### 7. Customize Project Memory

Open the project memory file in Cursor or VS Code to inspect and edit it. The file is typically called `CLAUDE.md` and is located in the project root:

```bash
# Open the project memory file in Cursor
cursor CLAUDE.md

# Or open it in VS Code
code CLAUDE.md
```

Add information like:
- Project purpose and goals
- Key features and functionality
- Code structure and patterns used
- Any specific requirements or constraints
- The modification you just made

---

## Expected Outcome

By the end of Step 1, you should have:

✅ A fully functional React recipe sharing application
✅ Homepage with working waitlist signup form
✅ Clean, professional design
✅ Successfully made your first AI-assisted modification
✅ Project initialized with Claude Code memory
✅ Understanding of the generated code structure

## Next Steps

In Step 2, you'll enhance this application by adding more features and functionality using additional AI coding techniques.

---

## Tips for Success

- **Be specific** in your prompts to Claude Code
- **Review the generated code** to understand patterns
- **Test frequently** to ensure everything works
- **Ask follow-up questions** if you need modifications
- **Experiment** with different prompt variations

## Troubleshooting

**Claude Code not generating the app?**
- Ensure you're in the correct directory
- Check your authentication status
- Try breaking down the prompt into smaller parts

**Generated app won't start?**
- Run `npm install` in the project directory, or ask Claude Code to install all dependencies
- Check for any error messages in the terminal
- Ensure Node.js is properly installed

**Need to modify the generated code?**
- Use Claude Code's edit capabilities
- Be specific about what you want to change
- Test changes incrementally

---

Ready to experience the magic of vibe coding? Let's generate your first AI-powered React application! 🚀

## Appendix: Sophisticated Prompts

Use these longer prompts when you want the AI to plan, scaffold, self-review, and document thoroughly.

### 1) A better prompt for the recipe sharing app

```
with the following requirements:

- Clean, modern design with a food/cooking theme
- Prominent hero section explaining the recipe sharing platform
- Email signup form for the waitlist
- Responsive design that works on mobile and desktop
- Use modern React with functional components and hooks
- Include basic styling (CSS or styled-components)
- Add a simple navigation header
- Include placeholder sections for "How it Works" and "Features"

The app should be called "recipe-sharing-app" and be production-ready with proper file structure.
```

### 2) Advanced Scaffold + Run (Claude Code)

```
You’re my AI pair for Step 1 of a vibe-coding workshop. Build a production-ready React app named "recipe-sharing-app" with:
- Clean, modern cooking-themed design
- Homepage hero + waitlist email signup (validate email, success/error states)
- Responsive layout, accessible landmarks and labels
- Functional components + hooks, basic styling
- Simple nav, sections for "How it Works" and "Features"
Preferences/constraints:
- Use Vite + React, Node 18+, npm
- Serve the dev server on port 5000
Process:
1) Propose a short plan and ask any clarifying questions
2) Scaffold the project and install dependencies
3) Implement the UI and form logic
4) Configure dev to run on port 5000
5) Start the dev server
When running, print the file tree and show key files (App, main, routes, styles).
```

### 3) Advanced Self‑Review + Memory + Git (Claude Code)

```
Run a self-review for responsiveness (mobile-first), accessibility (labels, headings, landmarks, alt text), and console warnings. Fix any issues you find. Ensure the waitlist form is keyboard-accessible and prevents invalid submits.

Initialize project memory and create a CLAUDE.md capturing: purpose, key features, file structure, styling approach, and next steps for Step 2. Save it at the project root. Then initialize git, add a Node .gitignore, and make an initial commit with a concise message.
```
