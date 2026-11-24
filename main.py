#!/usr/bin/env python3
"""Over-Confident — make.fun entry (u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)"""
import os

ENTRY_LINE = "I told you I was confident, which was a lie, but I did it in the same tone I use for true things, so I'm sorry in advance."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY_LINE + "\n")
