#! /usr/bin/env python3

"""
Sherlock: Find Usernames Across Social Networks Module

This module contains the main logic to search for usernames at social
networks.
"""

import sys


if __name__ == "__main__":
    # Check if the user is using the correct version of Python
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 9):
        print(f"Sherlock requires Python 3.9+\nYou are using Python {python_version}, which is not supported by Sherlock.")
        sys.exit(1)

    import asyncio
    from . import sherlock

    try:
        asyncio.run(sherlock.main())
    except KeyboardInterrupt:
        print("\nExiting... (Ctrl+C pressed)")
        sys.exit(0)
