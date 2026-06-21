"""Local-only placeholder auth module.

This branch intentionally removes remote authentication and AWS session
management from the CLI. The historical AuthContext API is kept only so
imports fail with a clear error message instead of an obscure ImportError.
"""

from typing import Dict, Optional


class AuthContext:
    deployment: Dict[str, str]

    def __init__(self, deployment: Optional[Dict[str, str]] = None):
        self.deployment = deployment or {}

    def authenticate(self, username: Optional[str] = None, password: Optional[str] = None):
        raise RuntimeError(
            'This cli-local-version branch is local-only. Remote authentication has been removed.'
        )

    def refresh(self):
        raise RuntimeError(
            'This cli-local-version branch is local-only. AWS session refresh is not available.'
        )
