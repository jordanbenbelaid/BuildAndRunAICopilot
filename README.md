# Build and Run an End-to-End AI Agent Factory

Live demo starter for building a customer support triage factory in **Visual Studio Code with GitHub Copilot**.

## Prerequisites

- Visual Studio Code
- GitHub Copilot and GitHub Copilot Chat extensions (this folder recommends them)
- Signed in to GitHub with Copilot access

## Open this demo

Open the `support-agent-factory` folder in VS Code so Copilot can load the workspace custom instructions:

```
support-agent-factory/
  tools.py
  .github/
    copilot-instructions.md
    instructions/
      agent-standards.instructions.md
  .vscode/
    extensions.json
```

`.github/copilot-instructions.md` applies to every Copilot Chat request in this workspace. `.github/instructions/agent-standards.instructions.md` applies automatically when Copilot works on Python files.

## What Copilot should follow

- Use Pydantic `BaseModel` for tool input parameters ("The Contract")
- Do not pass raw untyped strings into tool functions
- Include error-handling and circuit-breaker logic in routing scripts
# BuildAndRunAICopilot
