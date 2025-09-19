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

Create a custom slash command for React code reviews. Use this prompt in Gemini CLI:

```
I want to create a custom slash command called /react-review that acts as a senior React developer with 10+ years of experience. When I use this command, it should:

1. Analyze all React components in the current directory
2. Focus on:
   - Modern React best practices (hooks, functional components)
   - Performance optimization opportunities
   - Accessibility compliance (WCAG guidelines)
   - Security vulnerabilities
   - Code maintainability and structure
   - TypeScript usage (if applicable)

3. Organize feedback by severity: Critical, High, Medium, Low
4. Provide specific code examples for improvements
5. Suggest concrete next steps

Please help me create this custom slash command and show me how to save it for future use.
```

### 4. Test Your Custom Command

After creating the command, test it on your current project:

```
/react-review
```

### 5. Create Additional Specialized Commands

Based on your experience, consider creating these additional commands:

**Performance Analysis Command:**
```
/react-perf - Analyze React components for performance bottlenecks and optimization opportunities
```

**Accessibility Audit Command:**
```
/a11y-check - Comprehensive accessibility audit focusing on WCAG compliance
```

**Security Review Command:**
```
/security-audit - Security-focused review of React components and dependencies
```

### 6. Save and Manage Your Commands

Learn how to manage your custom commands:

```
Show me how to:
1. List all my custom slash commands
2. Edit existing commands
3. Delete commands I no longer need
4. Export my commands to share with team members
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