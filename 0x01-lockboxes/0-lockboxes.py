#!/usr/bin/python3

"""
n number of locked boxes in front of you. Each box is numbered sequentially
from 0 to n - 1 and each box may contain keys to the other boxes.
a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Checks if all boxes are reachable."""
    if not isinstance(boxes, list):
        return False

    seen = [False for _ in range(len(boxes))]
    seen[0] = True

    useBFS(boxes, seen)

    # The `seen` array tracks all the visited nodes. We can then see which
    # nodes were unvisited by inspecting for False values. However, for this
    # task we only need to know if any node was unreached, which is easier.
    return all(seen)


def useBFS(boxes, seen):
    """Uses iteration to visit nodes breadth-first
        and populate the seen array as each new node is visited.
    """
    for i, box in enumerate(boxes):
        if not isinstance(box, list):
            continue

        for key in box:
            if not isinstance(key, int):
                continue

            # Guard against out-of-bounds array access
            if key >= len(boxes):
                continue

            if i == key:
                continue

            seen[key] = True


def useDFS(boxes, seen, currentBoxIdx):
    """Uses recursion to visit nodes depth-first
        and populate the seen array as each new node is visited.
    """
    currentBox = boxes[currentBoxIdx]

    if not isinstance(currentBox, list):
        return

    for key in currentBox:
        if not isinstance(key, int):
            continue

        # Guard against out-of-bounds array access
        if key >= len(boxes):
            continue

        if seen[key]:
            continue

        seen[key] = True
        useDFS(boxes, seen, key)
