# Step 1: Hello World of Vibe Coding - Recipe Sharing App

Welcome to your first vibe coding experience! In this step, you'll use Claude Code to generate a complete React application for sharing recipes with a waitlist signup homepage.

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

### 1. Launch Claude Code

From this step1 directory, start Claude Code in interactive mode:

```bash
claude
```

### 2. Generate the Recipe Sharing App

Use this prompt with Claude Code to generate your React application:

```
Create a React web application for sharing recipes. The homepage should feature a waitlist signup form with the following requirements:

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

### 3. Review the Generated Code

After Claude Code generates the application:

1. Ask Claude Code to install all dependencies and start the application:
   ```
   Install the dependencies for this React app and start it on an available port
   ```
2. Open the newly created `recipe-sharing-app` directory in Cursor or your preferred IDE
3. Explore the file structure and generated components
4. Review the code quality and structure
5. Test the running application in your browser

### 4. Initialize Project Memory

Navigate into your new project directory:

```bash
cd recipe-sharing-app
```

Launch Claude Code and initialize project memory:

```bash
claude
/init
```

This creates a `.claude/` directory with project context that Claude Code will use for future interactions.

### 5. Customize Project Memory

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

---

## Expected Outcome

By the end of Step 1, you should have:

✅ A fully functional React recipe sharing application
✅ Homepage with working waitlist signup form
✅ Clean, professional design
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