#!/usr/bin/python3
"""
You have `n` number of locked boxes in front of you. Each box is numbered
sequentially from 0 to `n - 1` and each box may contain keys to the other
boxes.

TASK:
Write a method that determines if all boxes can be opened.

CONSTRAINT:
- Function prototype: `def canUnlockAll(boxes):`
- `boxes` is a list of lists.
- A key with the same number as a box opens that box.
- You can assume all keys will be positive integers.
    - There can be keys that do not have boxes.
- The first box `boxes[0]` is unlocked.
- Return True if all boxes can be opened, else return False


STEPS:

1. Create a variable n which stores the length of the list.
2. Check if n is equal to 1, then we can simply return True since the
first box in the list is alway unlocked.
3. Generate set of box index ranging from 1, to `n - 1`. This unique set of
box index would then be stored in a variable `box_idx`.
4. Next is to iterate through the boxes, then within each box I'll also iterate
through the keys.
5. If key is found in it's own box reject key (i.e False), else True,
and if any key is found within the unique set of box indexs. Then
remove the key from the set of box index (i.e bunch of keys).
This mean that the box can be opened.
6. Check if `box_idx` is empty. If it is empty then return True, meaning that
each box can be opened
7. At the end of the loop, return False meaning that some boxes did not have
key to open them.
"""
from typing import Set, List, Optional


def canUnlockAll(boxes: List[List[Optional[int]]]) -> bool:
    """Check if boxes contains keys for all other boxes."""
    n = len(boxes)

    if n == 1:
        return True
    # These are boxes that needs to be opened
    set_box_idx: Set[int] = set(range(1, n))

    for box_idx, box in enumerate(boxes):
        for key in box:
            # The key to a box should not be found within it's own
            # box, also if key is found for another box remove it
            # from the set of box keys
            if key in set_box_idx and box_idx != key:
                set_box_idx.remove(key)
            # If all the keys have been found then return True
            if not set_box_idx:
                return True
    return False
