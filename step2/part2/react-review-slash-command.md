# Senior React Developer Slash Command Configuration

This document provides the detailed configuration for creating a `/react-review` custom slash command in Gemini CLI.

## Command Overview

**Command Name**: `/react-review`
**Purpose**: Comprehensive React code review by a senior developer expert
**Scope**: Project-wide React component analysis
**Output**: Organized feedback by severity with actionable recommendations

## Command Configuration

Use this prompt in Gemini CLI to create your custom slash command:

```
I want to create a custom slash command called "/react-review" with the following configuration:

COMMAND NAME: /react-review

COMMAND DESCRIPTION: "Comprehensive React code review by a senior developer expert"

COMMAND BEHAVIOR:
When this command is executed, act as a Senior React Developer with 10+ years of experience in modern React development, performance optimization, accessibility, and security best practices.

ANALYSIS SCOPE:
- Automatically scan all React components in the current directory and subdirectories
- Include .js, .jsx, .ts, .tsx files
- Analyze package.json for dependencies and potential issues

EXPERTISE AREAS:
1. Modern React Patterns (React 18+)
   - Functional components and hooks
   - Concurrent features and Suspense
   - Server Components (if applicable)
   - Custom hooks and reusability

2. Performance Optimization
   - Component re-render analysis
   - Bundle size optimization
   - Code splitting opportunities
   - Memory leak detection

3. Accessibility (WCAG 2.1 AA)
   - Semantic HTML structure
   - ARIA implementation
   - Keyboard navigation
   - Screen reader compatibility

4. Security Assessment
   - XSS prevention
   - Input validation
   - Dependency vulnerabilities
   - Data sanitization

5. Code Quality & Maintainability
   - Architecture patterns
   - Code organization
   - Error handling
   - Testing considerations

FEEDBACK STRUCTURE:
Organize all findings by severity:

🔴 CRITICAL
- Security vulnerabilities
- Accessibility blockers
- Performance killers
- Breaking changes

🟡 HIGH PRIORITY
- Architecture improvements
- Significant performance gains
- Important best practice violations
- Maintainability issues

🟠 MEDIUM PRIORITY
- Code quality improvements
- Minor performance optimizations
- Better patterns and practices
- Documentation gaps

🟢 LOW PRIORITY
- Style improvements
- Nice-to-have optimizations
- Future considerations
- Learning opportunities

OUTPUT FORMAT:
For each issue identified:
1. Clear problem description
2. File location and line numbers
3. Current code snippet (if relevant)
4. Recommended solution with code example
5. Explanation of benefits

ADDITIONAL FEATURES:
- Highlight positive patterns found in the code
- Provide learning resources for complex topics
- Suggest next steps and priorities
- Include upgrade recommendations for outdated patterns

Please create this command and show me how to save it for future use.
```

## Usage Examples

### Basic Project Review
```
/react-review
```

### After Making Changes
```
/react-review
```
*Use after implementing new features or refactoring*

### Pre-Deployment Check
```
/react-review
```
*Use before deploying to production*

## Advanced Usage Patterns

### Combined with File Filtering
If Gemini CLI supports file filtering, you can focus the review:
```
/react-review --include="src/components/**"
```

### Integration with CI/CD
Consider using the command output in automated workflows:
```
/react-review > code-review-report.md
```

## Expected Output Format

The command should produce output similar to:

```
🔍 React Code Review Report
📊 Analyzed: 15 components, 8 hooks, 3 utilities

🔴 CRITICAL ISSUES (2 found)
├── src/components/LoginForm.jsx:23
│   ❌ XSS vulnerability in user input handling
│   💡 Sanitize input using DOMPurify before rendering
│
└── src/components/UserProfile.jsx:45
    ❌ Missing accessibility labels for form inputs
    💡 Add aria-label or associated label elements

🟡 HIGH PRIORITY (5 found)
├── src/components/ProductList.jsx:12
│   ⚠️ Unnecessary re-renders on every state change
│   💡 Wrap component in React.memo() and optimize dependencies
...

📈 POSITIVE PATTERNS FOUND
✅ Excellent use of custom hooks for data fetching
✅ Proper error boundaries implementation
✅ Good component composition patterns

🎯 NEXT STEPS
1. Address critical security and accessibility issues immediately
2. Implement React.memo for performance optimization
3. Consider migrating to TypeScript for better type safety
4. Add unit tests for complex components
```

## Integration with Claude Code Workflow

Use this powerful combination workflow:

1. **Run Gemini Review**: Use `/react-review` to get independent analysis
2. **Copy Results**: Select and copy the complete review output
3. **Switch to Claude Code**: Open your Claude Code session
4. **Cross-Reference**: Use this prompt in Claude Code:

```
I just ran a React code review using Gemini CLI and got this feedback:

[PASTE GEMINI REVIEW HERE]

As a senior React developer, what's your assessment of this analysis? Do you agree with the priorities? Are there any additional concerns or different approaches you'd recommend? What would you focus on first?
```

## Customization Options

You can create variations of the command for specific use cases:

### Performance-Focused Review
```
/react-perf
```
*Focuses specifically on performance optimization*

### Accessibility Audit
```
/a11y-check
```
*Comprehensive accessibility compliance review*

### Security Assessment
```
/react-security
```
*Security-focused code analysis*

### TypeScript Migration Check
```
/ts-ready
```
*Evaluates code readiness for TypeScript migration*

## Maintenance and Updates

Regularly update your command to:
- Include new React features and patterns
- Adapt to evolving security best practices
- Incorporate team-specific coding standards
- Add project-specific architectural requirements

## Best Practices

- **Run Regularly**: Use the command frequently during development
- **Act on Critical Issues**: Address red flags immediately
- **Learn from Feedback**: Use reviews as learning opportunities
- **Share with Team**: Ensure consistent code quality across the team
- **Document Decisions**: Keep track of why certain suggestions were or weren't implemented

This slash command becomes a powerful, instant code review tool that you can rely on for consistent, expert-level feedback throughout your development process!