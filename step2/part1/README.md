# Step 2 / Part 1: Claude Code Sub-Agents

Welcome to Part 1 of Step 2! In this section, you'll learn how to create and use specialized sub-agents in Claude Code to enhance your development workflow.

## What are Claude Code Sub-Agents?

Sub-agents are specialized AI assistants that you can create within Claude Code to handle specific tasks or domains. Think of them as expert consultants that you can call upon for specialized knowledge and capabilities.

## Key Benefits

- **Specialized Expertise**: Create agents focused on specific domains (React development, security reviews, testing, etc.)
- **Consistent Workflows**: Standardize how certain tasks are performed across your projects
- **Context Preservation**: Sub-agents can maintain context about your specific coding patterns and preferences
- **Team Collaboration**: Share agent configurations with team members for consistent code quality

## What You'll Learn

In this part, you'll:
1. Understand the sub-agent system in Claude Code
2. Create a specialized **Senior React Developer Code Review Agent**
3. Configure the agent with expert-level prompts and behaviors
4. Use the agent to review and improve your recipe sharing app from Step 1

## Prerequisites

- Completed Step 1 (Recipe Sharing App)
- Claude Code installed and authenticated
- Your recipe sharing app project available

---

## Official Documentation

For detailed information about Claude Code sub-agents, refer to the official documentation:

📚 **[Claude Code Sub-Agents Documentation](https://docs.claude.com/en/docs/claude-code/sub-agents)**

This documentation covers:
- How to create and configure sub-agents
- Advanced agent configuration options
- Best practices for agent design
- Examples and use cases

---

## Instructions

### 1. Navigate to Your Step 1 Project

Open a terminal and navigate to your recipe sharing app from Step 1:

```bash
cd step1/recipe-sharing-app
# or wherever you created your project
```

### 2. Explore Existing Agents

Launch Claude Code and first check what agents are available:

```bash
claude
```

Use the built-in agents command to see what's available:

```
/agents
```

This will show you:
- All available agents in your system
- How to create new agents
- How to switch between agents
- Agent management commands

### 3. Create a Senior React Developer Code Review Agent

Now let's create a specialized code review agent using the proper Claude Code workflow:

**Step 1: Open the agents interface**
```
/agents
```

**Step 2: Create New Agent**
- Select "Create New Agent" from the menu
- Choose **project-level** agent (recommended for this step)
  > **Tip**: Project-level agents (stored in `.claude/agents/`) are available only in this project, while user-level agents (`~/.claude/agents/`) work across all projects. For workshop purposes, project-level keeps things isolated.
<AB> add a small tip or indent about the different between project level and user level </AB>
- Select **"Generate with Claude"** option
- Keep all default options for now

**Step 3: Use this prompt for "Generate with Claude"**

Paste this prompt when Claude asks for the agent description:

```
Create a Senior React Developer Code Review Agent that proactively reviews React code for best practices, performance, accessibility, and maintainability.

Agent Name: react-code-reviewer

Purpose: This agent should proactively analyze React components and provide expert-level code reviews whenever React code is discussed or modified. The agent has 10+ years of React development experience and specializes in:

- Modern React patterns (React 18+, hooks, functional components)
- Performance optimization (re-renders, bundle size, memory)
- Accessibility compliance (WCAG 2.1 AA guidelines)
- Security vulnerabilities (XSS, input validation)
- Code architecture and maintainability
- Testing strategies and best practices

The agent should offer to review code and provide feedback organized by severity (Critical, High, Medium, Low) with specific, actionable recommendations and code examples.
```
<AB> `proactively` is an advanced tip. lets not include it right here. lets add that as an enhancement after the user has tested the agents once.</AB>
**Step 4: Complete Agent Creation**
- Accept the generated agent configuration
- Save the agent (it will be stored in `.claude/agents/` in your project)

### 4. Test Your Agent with Code Review

Now test your agent on your current project. First, let's see if the agent activates automatically:

**Try This Request:**
```
I'd like to improve the React code quality in this project. Can you review the code and give your feedback?
```

**If Agent Doesn't Activate Automatically:**
You can explicitly request your agent:

```
Use the react-code-reviewer agent to review all the React components in this project. Provide a comprehensive analysis organized by severity.
```

**Observe Agent Behavior:**
- Did Claude automatically switch to your custom agent?
- Does the response show agent-specific expertise?
- Is the feedback format matching your agent's configuration?

### 5. Fix Issues with OpenAI Codex CLI

Now let's use a different AI tool to implement the suggested improvements and see how they work together:

**Step 1: Use OpenAI Codex CLI**
Open a second terminal and navigate to your project:

```bash
cd step1/recipe-sharing-app
codex
```

**Step 2: Ask Codex to Fix Issues**
Share the feedback from your Claude Code agent with Codex:

```
My React code review identified these issues: [PASTE AGENT FEEDBACK HERE]

Please help me fix the critical and high-priority issues. Show me the specific code changes needed.
```

**Step 3: Implement Changes**
- Apply the code changes suggested by Codex
- Test that your application still works
- Make sure the changes address the original issues

**Step 4: Get a Follow-up Review**
Return to Claude Code and ask your agent to review the updated code:

```
I've made some improvements to the React code based on previous feedback. Please review the current state and see if the issues have been resolved.
```

*Alternative AI Tools: Feel free to use Cursor AI, GitHub Copilot, or other AI coding assistants instead of Codex CLI.*

### 6. Advanced Agent Enhancement

Now that you've tested your basic agent, let's make it more proactive:

**Edit Your Agent for Better Activation:**
1. Use `/agents` to find your agent file location
2. Open the agent file in your IDE
3. Add the word "proactively" to the agent description
4. Save and restart Claude Code

> **Pro Tip**: Using "proactively" in agent descriptions makes Claude invoke them more automatically during relevant conversations.

**Enhanced Agent Description Example:**

For a detailed example of an advanced agent configuration, see the [React Code Reviewer Agent Configuration](react-code-reviewer-agent.md) file.

### 7. Manage Your Agents

Learn to manage your agents effectively:

**List all agents:**
```
/agents
```

**Check agent status:**
```
/agents status
```

---

## Expected Outcome

By the end of Part 1, you should have:

✅ Understanding of Claude Code sub-agents and the `/agents` command
✅ Explored existing agents in your system
✅ A configured Senior React Developer Code Review Agent
✅ Experience switching between agents
✅ Completed code review of your recipe sharing app
✅ Implemented improvements based on expert feedback
✅ Knowledge of agent management commands

## Next Steps

Continue to [Part 2](../part2/README.md) to learn about Gemini CLI custom slash commands and create complementary tools for your development workflow.

---

## Tips for Success

- **Use "Generate with Claude"**: This option creates better agent configurations than manual setup
- **Include "proactively"**: Add this word to your agent description to make Claude invoke the agent more actively
- **Be Specific**: When creating agents, provide detailed instructions about their expertise and behavior
- **Test Both Modes**: Try both automatic activation and manual agent switching
- **Iterate**: Refine your agent configuration based on the quality of feedback you receive
- **Experiment**: Try different options when creating subsequent agents
- **Document**: Keep notes about which agents work well for which types of tasks

## Troubleshooting

**Agent not providing detailed feedback?**
- Make the agent prompt more specific about what to look for
- Add examples of the type of feedback you want

**Agent giving inconsistent advice?**
- Refine the agent's expertise description
- Add constraints about coding standards to follow

**Can't find saved agent?**
- Use `/agents` to list all available agents
- Check that the agent was created with the correct name
- Try `/agents status` to see the current active agent

**Agent not activating automatically?**
- Try rephrasing your request to be more specific about React code review
- Explicitly mention the agent name in your request: "Use the react-code-reviewer agent..."
- Edit your agent to include "proactively" in the description (see Advanced Agent Enhancement section)

**Agent commands not working?**
- Make sure you're using the correct syntax: `/agents` for the interface
- Verify you're in an active Claude Code session
- Check that your agent was saved properly in `.claude/agents/`

**Want to edit your agent?**
- Use `/agents` to find your agent file location
- Edit the agent file directly in your IDE
- Restart Claude Code to reload agent changes

Ready to create your specialized code review expert? Let's build some intelligent development tools! 🚀