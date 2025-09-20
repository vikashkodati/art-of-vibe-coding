# Playwright MCP Server Usage Examples

This document provides practical examples of using the Playwright MCP server with Claude Code for Django chat app testing and development.

## Basic Browser Automation

### Page Navigation and Interaction

**Navigate to the Django chat app**:
```javascript
// Ask Claude Code with Playwright MCP:
// "Open the Django chat app and verify it loads correctly"

// Navigate to the chat app
await page.goto('http://localhost:8000');

// Wait for page to load
await page.waitForLoadState('networkidle');

// Verify the page title
const title = await page.title();
console.log('Page title:', title);
```

**Interact with the chat interface**:
```javascript
// "Test the chat interface by sending a message"

// Navigate to chat page
await page.goto('http://localhost:8000/chat/');

// Fill in message input
await page.fill('#message-input', 'Hello, this is a test message');

// Click send button
await page.click('#send-button');

// Wait for response
await page.waitForSelector('.message.assistant', { timeout: 5000 });

// Verify message was sent
const messages = await page.textContent('.chat-messages');
console.log('Chat messages:', messages);
```

### Form Testing

**Test the chat form submission**:
```javascript
// "Test form validation and submission"

// Navigate to chat page
await page.goto('http://localhost:8000/chat/');

// Test empty message submission
await page.click('#send-button');

// Check for validation message
const validationMessage = await page.textContent('.error-message');
console.log('Validation message:', validationMessage);

// Test valid message submission
await page.fill('#message-input', 'Valid test message');
await page.click('#send-button');

// Verify message appears in chat
await page.waitForSelector('.message.user:has-text("Valid test message")');
```

## End-to-End Testing Scenarios

### Complete Chat Flow Test

**Full conversation test**:
```javascript
// "Test a complete chat conversation flow"

// Start new chat session
await page.goto('http://localhost:8000/chat/');

// Send first message
await page.fill('#message-input', 'What is Django?');
await page.click('#send-button');

// Wait for assistant response
await page.waitForSelector('.message.assistant');

// Send follow-up message
await page.fill('#message-input', 'Can you tell me more?');
await page.click('#send-button');

// Verify conversation history
const messageCount = await page.locator('.message').count();
console.log('Total messages in conversation:', messageCount);

// Capture screenshot of conversation
await page.screenshot({ path: 'chat-conversation.png' });
```

### Session Management Testing

**Test session persistence**:
```javascript
// "Test that chat sessions persist across page reloads"

// Start conversation
await page.goto('http://localhost:8000/chat/');
await page.fill('#message-input', 'Test session persistence');
await page.click('#send-button');

// Get session ID from page
const sessionId = await page.getAttribute('#chat-container', 'data-session-id');

// Reload page
await page.reload();

// Verify message history is preserved
const messageExists = await page.isVisible('.message:has-text("Test session persistence")');
console.log('Message persisted after reload:', messageExists);

// Verify session ID is the same
const newSessionId = await page.getAttribute('#chat-container', 'data-session-id');
console.log('Session ID preserved:', sessionId === newSessionId);
```

## Visual Testing and Documentation

### Screenshot Generation

**Capture UI states for documentation**:
```javascript
// "Generate screenshots of different UI states"

// Landing page
await page.goto('http://localhost:8000/');
await page.screenshot({ path: 'landing-page.png', fullPage: true });

// Empty chat page
await page.goto('http://localhost:8000/chat/');
await page.screenshot({ path: 'empty-chat.png' });

// Chat with messages
await page.fill('#message-input', 'Sample message for screenshot');
await page.click('#send-button');
await page.waitForSelector('.message.assistant');
await page.screenshot({ path: 'chat-with-messages.png' });

// Mobile view
await page.setViewportSize({ width: 375, height: 667 });
await page.screenshot({ path: 'chat-mobile.png' });
```

### Responsive Design Testing

**Test responsive layout**:
```javascript
// "Test the chat app on different screen sizes"

const viewports = [
  { width: 320, height: 568, name: 'mobile-small' },
  { width: 375, height: 667, name: 'mobile-medium' },
  { width: 768, height: 1024, name: 'tablet' },
  { width: 1024, height: 768, name: 'tablet-landscape' },
  { width: 1920, height: 1080, name: 'desktop' }
];

for (const viewport of viewports) {
  await page.setViewportSize({ width: viewport.width, height: viewport.height });
  await page.goto('http://localhost:8000/chat/');

  // Check if mobile menu is visible on small screens
  const isMobileMenuVisible = await page.isVisible('.mobile-menu-toggle');

  // Capture screenshot
  await page.screenshot({ path: `chat-${viewport.name}.png` });

  console.log(`${viewport.name}: Mobile menu visible: ${isMobileMenuVisible}`);
}
```

## Performance Testing

### Load Time Analysis

**Measure page load performance**:
```javascript
// "Analyze page load performance"

const startTime = Date.now();

await page.goto('http://localhost:8000/chat/');
await page.waitForLoadState('networkidle');

const loadTime = Date.now() - startTime;
console.log('Page load time:', loadTime, 'ms');

// Measure time to interactive
const timeToInteractive = await page.evaluate(() => {
  return performance.timing.domInteractive - performance.timing.navigationStart;
});
console.log('Time to interactive:', timeToInteractive, 'ms');

// Check for performance issues
const performanceMetrics = await page.evaluate(() => {
  const navigation = performance.getEntriesByType('navigation')[0];
  return {
    dns: navigation.domainLookupEnd - navigation.domainLookupStart,
    connection: navigation.connectEnd - navigation.connectStart,
    response: navigation.responseEnd - navigation.responseStart,
    dom: navigation.domComplete - navigation.domLoading
  };
});
console.log('Performance metrics:', performanceMetrics);
```

### Network Analysis

**Monitor network requests**:
```javascript
// "Monitor API calls and network performance"

// Listen for network requests
page.on('request', request => {
  if (request.url().includes('/api/')) {
    console.log('API Request:', request.method(), request.url());
  }
});

page.on('response', response => {
  if (response.url().includes('/api/')) {
    console.log('API Response:', response.status(), response.url());
  }
});

// Perform actions that trigger API calls
await page.goto('http://localhost:8000/chat/');
await page.fill('#message-input', 'Test API monitoring');
await page.click('#send-button');

// Wait for API response
await page.waitForResponse(response =>
  response.url().includes('/chat/send/') && response.status() === 200
);
```

## Advanced Testing Scenarios

### Error Handling Testing

**Test error scenarios**:
```javascript
// "Test how the app handles server errors"

// Simulate server being down
await page.route('**/chat/send/', route => {
  route.fulfill({
    status: 500,
    contentType: 'application/json',
    body: JSON.stringify({ error: 'Internal server error' })
  });
});

await page.goto('http://localhost:8000/chat/');
await page.fill('#message-input', 'This should trigger an error');
await page.click('#send-button');

// Check error handling
const errorMessage = await page.textContent('.error-notification');
console.log('Error message displayed:', errorMessage);

// Verify user can retry
await page.click('.retry-button');
```

### Accessibility Testing

**Check accessibility features**:
```javascript
// "Test accessibility features of the chat app"

await page.goto('http://localhost:8000/chat/');

// Check if form elements have proper labels
const messageInputLabel = await page.getAttribute('#message-input', 'aria-label');
console.log('Message input label:', messageInputLabel);

// Test keyboard navigation
await page.keyboard.press('Tab');
const focusedElement = await page.evaluate(() => document.activeElement.id);
console.log('First focused element:', focusedElement);

// Test screen reader support
const chatRegion = await page.getAttribute('.chat-messages', 'role');
console.log('Chat region role:', chatRegion);

// Check color contrast (requires additional setup)
const backgroundColor = await page.locator('.chat-container').evaluate(el =>
  getComputedStyle(el).backgroundColor
);
const textColor = await page.locator('.chat-container').evaluate(el =>
  getComputedStyle(el).color
);
console.log('Background color:', backgroundColor);
console.log('Text color:', textColor);
```

## Common Claude Code Prompts

### Development Testing
- "Test the Django chat app and capture screenshots of the interface"
- "Verify that the chat form validation works correctly"
- "Check if messages are being saved and displayed properly"

### UI/UX Validation
- "Test the chat app on mobile devices and capture responsive screenshots"
- "Verify that the chat interface is accessible to users with disabilities"
- "Check the visual design and layout of the chat messages"

### Performance Monitoring
- "Measure the performance of the Django chat app page loading"
- "Monitor API response times for chat message submissions"
- "Check for any JavaScript errors or console warnings"

### Integration Testing
- "Test the complete user flow from landing page to active chat"
- "Verify that chat sessions work correctly across page reloads"
- "Test error handling when the server is unavailable"

## Test Organization

### Page Object Model

**Create reusable page objects**:
```javascript
// "Create a ChatPage class for reusable test methods"

class ChatPage {
  constructor(page) {
    this.page = page;
    this.messageInput = '#message-input';
    this.sendButton = '#send-button';
    this.chatMessages = '.chat-messages';
  }

  async goto() {
    await this.page.goto('http://localhost:8000/chat/');
  }

  async sendMessage(message) {
    await this.page.fill(this.messageInput, message);
    await this.page.click(this.sendButton);
  }

  async waitForResponse() {
    await this.page.waitForSelector('.message.assistant');
  }

  async getMessageCount() {
    return await this.page.locator('.message').count();
  }

  async screenshot(path) {
    await this.page.screenshot({ path });
  }
}

// Usage
const chatPage = new ChatPage(page);
await chatPage.goto();
await chatPage.sendMessage('Hello!');
await chatPage.waitForResponse();
await chatPage.screenshot('chat-test.png');
```

### Test Data Management

**Use fixtures for consistent testing**:
```javascript
// "Set up test data for consistent chat testing"

const testData = {
  messages: [
    { role: 'user', content: 'Hello, how are you?' },
    { role: 'assistant', content: 'I am doing well, thank you!' },
    { role: 'user', content: 'What can you help me with?' }
  ],
  sessions: {
    empty: 'test-session-empty',
    withHistory: 'test-session-history'
  }
};

// Use test data in tests
for (const message of testData.messages) {
  if (message.role === 'user') {
    await page.fill('#message-input', message.content);
    await page.click('#send-button');
    await page.waitForSelector('.message.assistant');
  }
}
```

## Tips for Using with Claude Code

1. **Descriptive Test Requests**: Be specific about what you want to test
   - "Test the chat form validation and error handling"
   - "Capture screenshots of the chat interface in mobile view"
   - "Verify that messages persist after page reload"

2. **Visual Documentation**: Use Playwright for generating documentation
   - "Create screenshots for the user manual"
   - "Generate visual regression test baselines"
   - "Document the user interface states"

3. **Continuous Integration**: Set up automated testing
   - "Create tests that can run in CI/CD pipeline"
   - "Set up headless browser testing for deployment verification"
   - "Monitor the app health with automated tests"

4. **Debugging Support**: Use Playwright for development debugging
   - "Help me debug why the chat form isn't submitting"
   - "Check if there are any console errors on the chat page"
   - "Verify that the JavaScript is loading correctly"