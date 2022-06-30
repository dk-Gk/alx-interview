#!/usr/bin/python3
"""python lockboxes"""


def canUnlockAll(boxes):
    """Function determines if all the boxes can be opened"""
    box_unlock = []

    for key, box in enumerate(boxes):
        if len(box) == 0 or key == 0:
            if key not in box_unlock:
                box_unlock.append(key)
        for k in box:
            if k < len(boxes) and k != key:
                if k not in box_unlock:
                    box_unlock.append(k)
        if len(box_unlock) == len(boxes):
            return True
    return False
