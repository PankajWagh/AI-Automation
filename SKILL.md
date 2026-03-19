---
name: "weather-cli"
description: "CLI for the weather MCP server. Call tools, list resources, and get prompts."
---

# weather CLI

## Tool Commands

### get_weather

Get current weather for a city.

```bash
uv run --with fastmcp python cli.py call-tool get_weather --city <value>
```

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--city` | string | yes |  |

## Utility Commands

```bash
uv run --with fastmcp python cli.py list-tools
uv run --with fastmcp python cli.py list-resources
uv run --with fastmcp python cli.py read-resource <uri>
uv run --with fastmcp python cli.py list-prompts
uv run --with fastmcp python cli.py get-prompt <name> [key=value ...]
```
