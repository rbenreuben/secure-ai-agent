"""Scoped-identity / least-privilege stub.
In production this is where you'd resolve the caller's OIDC identity (e.g., Okta)
and the agent's own scoped service-account credentials.
"""
from dataclasses import dataclass, field

@dataclass
class Principal:
    user_id: str
    roles: list[str] = field(default_factory=list)

    def can_use_tool(self, tool_name: str, allowed: dict[str, list[str]]) -> bool:
        """Allow only tools permitted for one of the principal's roles."""
        return any(tool_name in allowed.get(role, []) for role in self.roles)

# Demo allow-list: which roles may call which tools (least privilege).
TOOL_ALLOWLIST = {
    "user": ["echo"],
    "admin": ["echo", "lookup"],
}
