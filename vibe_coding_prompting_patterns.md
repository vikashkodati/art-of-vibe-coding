# Vibe Coding: Essential Prompting Patterns

*A collection of battle-tested prompting techniques for AI-assisted development*

## Core Prompting Patterns

### 1. Role-Based Expertise ("Like a...")
**Pattern**: `"Like a [specific role], [request]"`

**Purpose**: Activates specific domain knowledge and professional standards

**Examples**:
- `"Like a senior React developer, review this component for performance issues"`
- `"Like a senior Django developer, critique this API design"`
- `"Like a DevOps engineer, evaluate this deployment configuration"`
- `"Like a security expert, audit this authentication flow"`

**Why it works**: Models have extensive training on role-specific knowledge and best practices. This pattern helps access the right "mental model" for the task.

**Best practices**:
- Be specific with seniority level (senior, lead, principal)
- Include relevant specializations when needed
- Use for code reviews, architecture decisions, and technical guidance

---

### 2. Permission to Push Back ("Critically" / "Honest Feedback")
**Pattern**: `"Give me [critical/honest] feedback on..."`

**Purpose**: Encourages the model to provide genuine critique rather than polite agreement

**Examples**:
- `"Give me critical feedback on this API design"`
- `"Provide honest feedback about this component structure"`
- `"Critically evaluate this database schema"`
- `"Give me brutal honesty about this code quality"`

**Why it works**: Models are often trained to be helpful and agreeable. These words signal that constructive criticism is wanted and valued.

**Best practices**:
- Use when you want genuine assessment, not validation
- Combine with role-based prompts for expert-level critique
- Be prepared to iterate based on the feedback received

---

### 3. Collaborative Discovery ("Ask Clarifying Questions")
**Pattern**: `"Ask clarifying questions about [requirement] before implementing"`

**Purpose**: Prevents assumptions and ensures proper understanding of requirements

**Examples**:
- `"Ask clarifying questions about this feature before writing the code"`
- `"Before implementing this API, ask me clarifying questions about the requirements"`
- `"Help me think through this - ask clarifying questions about the user flow"`

**Why it works**: Forces the model to think through ambiguities and edge cases rather than making potentially incorrect assumptions.

**Best practices**:
- Use early in development process
- Encourage questions about user experience, error handling, edge cases
- Follow up with additional context based on questions asked

---

### 4. Third-Party Attribution ("My Colleague Suggested")
**Pattern**: `"My colleague suggested [approach/solution]. What do you think?"`

**Purpose**: Makes it easier for models to provide honest critique of ideas

**Examples**:
- `"My colleague suggested we use Redux for this simple form. What's your take?"`
- `"A teammate proposed this database design. How would you improve it?"`
- `"My coworker thinks we should microservice this. Good idea?"`

**Why it works**: Removes personal attachment and social pressure, allowing for more objective evaluation.

**Best practices**:
- Use when you want unbiased evaluation of your own ideas
- Great for architectural decisions and technology choices
- Helps get past "politeness bias" in AI responses

---

## Advanced Combinations

### Expert + Critical Review
```
"Like a senior full-stack developer, give me critical feedback on this 
authentication system. Ask clarifying questions about security requirements 
if anything seems unclear."
```

### Third-Party + Role-Based Critique
```
"My team lead suggested this React component pattern. Like a senior React 
developer, what's your honest assessment of this approach?"
```

### Discovery + Expertise
```
"Like a senior DevOps engineer, ask me clarifying questions about our 
deployment requirements before suggesting a CI/CD pipeline."
```

---

## Workshop Application Notes

These patterns will be demonstrated throughout the vibe coding workshop:

- **Part 1**: Use role-based prompts for initial code reviews
- **Part 2**: Apply clarifying questions pattern for feature development
- **Part 3**: Combine critical feedback with expert roles for MCP server evaluation

*More patterns will be added as we discover them during workshop development...*