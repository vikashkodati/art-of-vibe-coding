# Step 2 / Part 2: Gemini CLI Custom Slash Commands

Welcome to Part 2 of Step 2! In this section, you'll learn how to create custom slash commands in Gemini CLI to streamline your development workflow with specialized, reusable commands.

## What are Gemini CLI Custom Slash Commands?

Custom slash commands in Gemini CLI allow you to create personalized shortcuts that execute complex prompts or workflows with simple commands. They're like having a personalized toolkit of expert consultants at your fingertips.

## Key Benefits

- **Instant Expertise**: Access specialized knowledge with simple commands
- **Workflow Automation**: Turn complex multi-step processes into single commands
- **Consistency**: Ensure the same high-quality analysis every time
- **Team Sharing**: Share useful commands with your development team
- **Context Awareness**: Commands can access your current project context

## What You'll Learn

In this part, you'll:
1. Understand Gemini CLI's custom slash command system
2. Create a **Senior React Developer Code Review** slash command
3. Configure the command for expert-level analysis
4. Use the command to complement your Claude Code workflow

## Prerequisites

- Completed Step 1 (Recipe Sharing App)
- Completed Step 2 Part 1 (Claude Code Sub-Agents)
- Gemini CLI installed and authenticated
- Your recipe sharing app project available

---

## Official Documentation

For detailed information about Gemini CLI custom slash commands, refer to the official documentation:

📚 **[Gemini CLI Custom Slash Commands Documentation](https://cloud.google.com/blog/topics/developers-practitioners/gemini-cli-custom-slash-commands)**

This documentation covers:
- How to create and manage custom commands
- Command configuration syntax
- Advanced command features
- Best practices and examples

---

## Instructions

### 1. Navigate to Your Project

Open a terminal and navigate to your recipe sharing app:

```bash
cd step1/recipe-sharing-app
# or wherever you created your project
```

### 2. Launch Gemini CLI

Start Gemini CLI in your project directory:

```bash
gemini
```

### 3. Create a Senior React Developer Code Review Command

Create a custom slash command for React code reviews using a `.toml` file.

**Step 1: Create the Commands Directory**

For global availability across all projects:
```bash
mkdir -p ~/.gemini/commands
```

For project-specific availability:
```bash
mkdir -p .gemini/commands
```

**Step 2: Create the React Review Command File**

Create `~/.gemini/commands/react-review.toml` (for global) or `.gemini/commands/react-review.toml` (for project):

```bash
# Copy the provided template
cp step2/part2/react-review.toml ~/.gemini/commands/react-review.toml

# Or copy the content manually
cat step2/part2/react-review.toml
```

The complete `react-review.toml` file is provided in this step's directory and contains:
- Senior React developer persona with 10+ years experience
- Comprehensive analysis scope for React projects
- Five key expertise areas (Modern React, Performance, Accessibility, Security, Code Quality)
- Severity-based feedback structure with emojis
- Detailed output format with code examples
- Positive pattern recognition

**Step 3: Test the Command**

Restart Gemini CLI and test:
```bash
gemini
/react-review
```

### 4. Create Additional Specialized Commands

Based on your experience, consider creating these additional commands as separate `.toml` files:

**Performance Analysis Command (`react-perf.toml`):**
```toml
description = "Analyze React components for performance bottlenecks and optimization opportunities"
prompt = """[Create similar detailed prompt focused on performance]"""
```

**Accessibility Audit Command (`a11y-check.toml`):**
```toml
description = "Comprehensive accessibility audit focusing on WCAG compliance"
prompt = """[Create similar detailed prompt focused on accessibility]"""
```

**Security Review Command (`security-audit.toml`):**
```toml
description = "Security-focused review of React components and dependencies"
prompt = """[Create similar detailed prompt focused on security]"""
```

### 5. Manage Your Commands

**List available commands:**
```bash
# In Gemini CLI
/help
```

**Edit existing commands:**
```bash
# Edit the .toml file directly
vim ~/.gemini/commands/react-review.toml
# or
code ~/.gemini/commands/react-review.toml
```

**Delete commands:**
```bash
rm ~/.gemini/commands/command-name.toml
```

**Share commands with team:**
```bash
# Copy the .toml file to share
cp ~/.gemini/commands/react-review.toml /path/to/shared/location/
```

---

## Integration with Claude Code

Now that you have both Claude Code sub-agents and Gemini custom commands, try this powerful workflow:

1. **Use Gemini's /react-review** command to get an independent analysis
2. **Copy the feedback** from Gemini
3. **Switch to Claude Code** with your react-code-reviewer agent
4. **Share Gemini's feedback** with Claude using this prompt:

```
My Gemini CLI analysis provided this feedback: [PASTE FEEDBACK HERE]

As the react-code-reviewer agent, what do you think about this analysis? Do you agree or disagree with any points? What would you prioritize differently?
```

This creates a powerful dialogue between different AI tools for comprehensive code improvement!

---

## Expected Outcome

By the end of Part 2, you should have:

✅ Understanding of Gemini CLI custom slash commands
✅ A configured /react-review custom command
✅ Additional specialized commands for your workflow
✅ Experience using commands for code analysis
✅ Integration workflow between Gemini and Claude Code

## Next Steps

You now have a powerful AI-assisted development toolkit! Consider:
- Creating project-specific commands for your team
- Building commands for other technologies you use
- Sharing your best commands with the development community

---

## Tips for Success

- **Start Simple**: Begin with basic commands and add complexity as you learn
- **Be Specific**: Detailed command descriptions lead to better results
- **Test Thoroughly**: Try commands on different projects to ensure reliability
- **Version Control**: Keep track of command changes and improvements
- **Share Knowledge**: Document useful commands for your team

## Troubleshooting

**Command not working as expected?**
- Review the command syntax and prompt clarity
- Test with simpler examples first
- Check Gemini CLI documentation for syntax updates

**Commands giving inconsistent results?**
- Make the command prompt more specific
- Add constraints about the type of analysis you want

**Can't find saved commands?**
- Check Gemini CLI's command management features
- Verify commands were saved with memorable names

Ready to supercharge your development workflow with custom AI commands? Let's build some intelligent shortcuts! ⚡