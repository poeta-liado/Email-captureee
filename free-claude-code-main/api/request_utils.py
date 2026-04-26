"""Request utility functions for API route handlers.

Contains token counting for API requests.
"""

import json

import tiktoken
from loguru import logger

from providers.common import get_block_attr

ENCODER = tiktoken.get_encoding("cl100k_base")

__all__ = ["get_token_count"]



