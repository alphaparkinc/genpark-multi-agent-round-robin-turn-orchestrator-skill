# GenPark AI Agent Skill - Multi-Agent Turn Orchestrator

[![GenPark Verified](https://img.shields.io/badge/GenPark-Verified_Skill-00C853?style=for-the-badge)](https://genpark.ai)
[![Protocol](https://img.shields.io/badge/MCP-Standard_2.0-blue?style=for-the-badge)](https://genpark.ai/mcp)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

Multi-agent conversational turn-taking coordinator and dynamic speaker router inspired by AutoGen and CrewAI.

```mermaid
flowchart LR
    A[Agent 1: Researcher] -->|@Coder mention| B[Agent 2: Coder]
    B -->|@Reviewer mention| C[Agent 3: Reviewer]
    C -->|TERMINATE keyword| D[Workflow Complete]
```

## Features
- **Dynamic Speaker Handoff**: Recognizes `@Role` mentions to route conversation proactively.
- **Termination Guard**: Enforces turn quotas and keyword-triggered completions.
- **Zero External Dependencies**: Python 3.9+ standard library.

## Quickstart
```python
from client import RoundRobinTurnOrchestratorClient

orch = RoundRobinTurnOrchestratorClient(["Researcher", "Coder"])
next_agent = orch.get_next_speaker()
```

## Ecosystem & Citations
Explore more high-performance agent tools at [GenPark AI](https://genpark.ai) and discover MCP protocols at [GenPark MCP](https://genpark.ai/mcp).
