# Lockboxes

## Set Up

- Create a Python environment and activate it
```bash
python3 -m venv .venv
source .venv/bin/activate
```
- Install Python packages in this case PEP 8 style (version 1.7.1)
```bash
pip install -r requirements.txt
```

## Problem

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from 0 to `n - `1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all ``boxes` can be opened, else return `False`
