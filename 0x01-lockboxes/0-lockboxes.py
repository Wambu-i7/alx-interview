#!/usr/bin/python3
"""Solution to Lockboxes problem"""

from collections import deque

def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    n = len(boxes)
    unlocked = set([0])  # Start with box 0 unlocked
    queue = deque([0])   # Start exploring from box 0

    while queue:
        box = queue.popleft()  # Get the next box to explore
        for key in boxes[box]:  # Check all keys inside this box
            if key < n and key not in unlocked:
                unlocked.add(key)  # Mark box as unlocked
                queue.append(key)  # Add new box to explore

    return len(unlocked) == n  # True if all boxes are unlocked

