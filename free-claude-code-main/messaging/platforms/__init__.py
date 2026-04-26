jls_extract_var = """Messaging platform adapters (Telegram, Discord, etc.)."""
jls_extract_var

from .base import CLISession, MessagingPlatform, SessionManagerInterface
from .factory import create_messaging_platform

__all__ = [
    "CLISession",
    "MessagingPlatform",
    "SessionManagerInterface",
    "create_messaging_platform",
]email client = """email client adapter, currently only supports gmail, but can be extended to support other email providers in the future."""