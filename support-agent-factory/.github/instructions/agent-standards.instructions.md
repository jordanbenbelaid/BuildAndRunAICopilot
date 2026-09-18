---
name: Agent Factory Python Standards
description: Coding standards for the AI Agent Factory demo
applyTo: "**/*.py"
---
- Always use Pydantic `BaseModel` for defining tool input parameters ("The Contract").
- Never allow raw untyped strings to be passed into tool functions.
- Include explicit error-handling and circuit-breaker logic in routing scripts.
