#!/usr/bin/env python3
"""Midnight roast of a smart fridge, for make.fun's
Midnight Fridge Roast bounty.

Writes the single winning line to /output/entry.txt.
"""
import os

TEXT = "Midnight hits and my smart fridge locks itself like it's guarding state secrets. Buddy, the only thing in there is last Tuesday's pasta."


def main():
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
