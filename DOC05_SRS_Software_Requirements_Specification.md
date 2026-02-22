# DOC05 - Software Requirements Specification (SRS)

## 1. Software Functions
The MVP implements 5 core tabs reflecting the initial specifications:
1. **Risk Analysis Grid**: Provides a pandas datagrid loaded asynchronously parsing geopolitical constraints.
2. **Intelligence Reporting Module**: A fully operational form with `SQLAlchemy` mapping. Includes validation metrics and source reliability indexes.
3. **Strategic Foresight Placeholder**: UI interface intended for further mapping tools.
4. **EU Policy Monitroing View**: Regulatory awareness component.
5. **Technical Capabilities Hub**: Future integration for technical assessment tools.

## 2. API / Interface Structure
- SQLite DB (`intelligence_reports` table)
    - `id` (INTEGER, Primary Key)
    - `title` (TEXT)
    - `source` (TEXT)
    - `validity_score` (INTEGER, 1-10)
    - `content` (TEXT)

## 3. Security Quality Attributes
- Form actions explicitly route inserts via Parameterized Queries (`sqlAlechemy text()` parameters) fulfilling OWASP Top 10 mitigation guidelines (A03 Injection Defense).
- Error messages are handled gracefully by `loguru` rather than UI leaks to prevent reconnaissance.

## 4. Initialization Checks
Application must instantly provision its own DDL schemas using the built-in startup code if `europolitics.db` goes missing.
