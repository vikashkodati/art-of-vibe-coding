# PostgreSQL MCP Server Usage Examples

This document provides practical examples of using the PostgreSQL MCP server with Claude Code for Django chat app development.

## Basic Database Operations

### Schema Management

**Create the messages table for Django chat app**:
```sql
-- Ask Claude Code with PostgreSQL MCP:
-- "Create a messages table for the Django chat app with the following schema"

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL CHECK (role IN ('user', 'assistant')),
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id VARCHAR(255)
);

-- Create index for efficient queries
CREATE INDEX idx_messages_session_created
ON messages (session_id, created_at);
```

**View table structure**:
```sql
-- "Show me the structure of the messages table"
\d messages

-- Or using SQL
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'messages';
```

### Data Queries

**Insert sample messages**:
```sql
-- "Add some sample messages for testing"
INSERT INTO messages (session_id, role, content, user_id) VALUES
('session-123', 'user', 'Hello, how are you?', 'user-1'),
('session-123', 'assistant', 'I am doing well, thank you! How can I help you today?', NULL),
('session-456', 'user', 'What is the weather like?', 'user-2'),
('session-456', 'assistant', 'I do not have access to real-time weather data, but I can help you find weather information online.', NULL);
```

**Query messages by session**:
```sql
-- "Show me all messages for session-123 in chronological order"
SELECT session_id, role, content, created_at
FROM messages
WHERE session_id = 'session-123'
ORDER BY created_at ASC;
```

**Get recent conversations**:
```sql
-- "Show me the 10 most recent messages across all sessions"
SELECT session_id, role, LEFT(content, 50) as preview, created_at
FROM messages
ORDER BY created_at DESC
LIMIT 10;
```

### Performance Analysis

**Check table statistics**:
```sql
-- "Analyze the messages table performance"
SELECT
    schemaname,
    tablename,
    n_tup_ins as inserts,
    n_tup_upd as updates,
    n_tup_del as deletes,
    n_live_tup as live_rows,
    n_dead_tup as dead_rows
FROM pg_stat_user_tables
WHERE tablename = 'messages';
```

**Check index usage**:
```sql
-- "Show index usage statistics for the messages table"
SELECT
    indexname,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes
WHERE tablename = 'messages';
```

## Django Integration Examples

### Database Inspection During Development

**Check if Django migrations are applied**:
```sql
-- "Show me the current Django migration status"
SELECT app, name, applied
FROM django_migrations
ORDER BY applied DESC
LIMIT 10;
```

**View Django's auth tables**:
```sql
-- "List all Django authentication users"
SELECT id, username, email, is_active, date_joined
FROM auth_user
ORDER BY date_joined DESC;
```

### Development Debugging

**Find orphaned sessions**:
```sql
-- "Find chat sessions that have no user messages"
SELECT DISTINCT session_id
FROM messages
WHERE session_id NOT IN (
    SELECT DISTINCT session_id
    FROM messages
    WHERE role = 'user'
);
```

**Message statistics**:
```sql
-- "Give me statistics about our chat messages"
SELECT
    role,
    COUNT(*) as message_count,
    AVG(LENGTH(content)) as avg_length,
    MAX(LENGTH(content)) as max_length
FROM messages
GROUP BY role;
```

**Session activity**:
```sql
-- "Show chat session activity by day"
SELECT
    DATE(created_at) as chat_date,
    COUNT(DISTINCT session_id) as unique_sessions,
    COUNT(*) as total_messages
FROM messages
GROUP BY DATE(created_at)
ORDER BY chat_date DESC;
```

## Common Claude Code Prompts

### Schema Operations
- "Create the Django chat app database schema using PostgreSQL MCP"
- "Add an index to improve message query performance"
- "Show me the current database structure for the messages table"

### Data Analysis
- "Analyze the chat message patterns in the database"
- "Find the most active chat sessions"
- "Show me examples of user vs assistant message lengths"

### Development Support
- "Check if the database is ready for Django development"
- "Verify that the messages table matches our Django model"
- "Help me debug why messages aren't being saved properly"

### Migration Support
- "Generate SQL to add a new column to the messages table"
- "Help me prepare the database for a new Django feature"
- "Check what changes need to be made for the latest Django model"

## Advanced Examples

### Full-Text Search Setup

**Add full-text search capability**:
```sql
-- "Set up full-text search for chat messages"
ALTER TABLE messages
ADD COLUMN content_search_vector tsvector;

UPDATE messages
SET content_search_vector = to_tsvector('english', content);

CREATE INDEX idx_messages_search
ON messages USING gin(content_search_vector);

-- Create trigger to keep search vector updated
CREATE OR REPLACE FUNCTION update_content_search_vector()
RETURNS TRIGGER AS $$
BEGIN
    NEW.content_search_vector = to_tsvector('english', NEW.content);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_content_search_vector
    BEFORE INSERT OR UPDATE ON messages
    FOR EACH ROW
    EXECUTE FUNCTION update_content_search_vector();
```

**Search messages**:
```sql
-- "Search for messages containing specific keywords"
SELECT session_id, role, content, created_at
FROM messages
WHERE content_search_vector @@ to_tsquery('english', 'weather | help')
ORDER BY created_at DESC;
```

### Data Export for Analysis

**Export conversation data**:
```sql
-- "Export chat conversation data for analysis"
COPY (
    SELECT
        session_id,
        role,
        content,
        created_at,
        LENGTH(content) as message_length
    FROM messages
    ORDER BY session_id, created_at
) TO '/tmp/chat_export.csv' WITH CSV HEADER;
```

## Tips for Using with Claude Code

1. **Natural Language Queries**: Ask Claude Code to translate your needs into SQL
   - "Show me conversations from yesterday"
   - "Find the longest chat session"
   - "Count messages by user"

2. **Schema Evolution**: Use Claude Code to help with database changes
   - "Add a sentiment column to track message tone"
   - "Create a table for user preferences"
   - "Modify the schema to support message threading"

3. **Performance Monitoring**: Regular health checks
   - "Check database performance for the messages table"
   - "Identify slow queries related to chat functionality"
   - "Optimize the database for our chat app usage patterns"

4. **Data Validation**: Ensure data integrity
   - "Check for any data inconsistencies in the messages table"
   - "Validate that all sessions have proper message sequences"
   - "Find any messages with unusual characteristics"