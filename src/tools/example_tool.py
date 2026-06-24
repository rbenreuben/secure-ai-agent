"""A trivial allow-listed tool the agent can call."""

def echo(text: str) -> str:
    return f"echo: {text}"

TOOLS = {
    "echo": {
        "fn": echo,
        "schema": {
            "name": "echo",
            "description": "Echo back the provided text.",
            "input_schema": {
                "type": "object",
                "properties": {"text": {"type": "string"}},
                "required": ["text"],
            },
        },
    }
}
