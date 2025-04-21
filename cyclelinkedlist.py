"""
Cycle Detection in Linked Lists

This file implements:
1. Detecting if a linked list has a cycle.
2. Approaches:
   - Brute-force approach using a hash set.
   - Optimized approach using Floyd's Tortoise and Hare algorithm.

Author: [Your Name]
Date: [Submission Date]
"""

# Definition for a singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

###############################################
# Part 1: Cycle Detection
###############################################

# --- Brute Force Approach ---
# Use a hash set to store visited nodes.
# If we see a node again, there is a cycle.

def has_cycle_bruteforce(head):
    """
    Detects a cycle in a linked list using a hash set (brute-force).

    Args:
    head (ListNode): Head node of the linked list.

    Returns:
    bool: True if there is a cycle, False otherwise.
    """
    visited = set()
    current = head

    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next

    return False

# --- Optimized Approach ---
# Use Floyd's Tortoise and Hare algorithm (two pointers).
# Fast pointer moves 2 steps, slow pointer moves 1 step.
# If there is a cycle, they will meet.

def has_cycle_floyd(head):
    """
    Detects a cycle in a linked list using Floyd's Tortoise and Hare algorithm.

    Args:
    head (ListNode): Head node of the linked list.

    Returns:
    bool: True if there is a cycle, False otherwise.
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

###############################################
# Optional: Utility to Build Lists for Testing
###############################################

def build_list(values, pos=-1):
    """
    Build a linked list from a list of values and create a cycle at position pos.

    Args:
    values (List[int]): List of node values.
    pos (int): Index where the cycle should start (-1 for no cycle).

    Returns:
    ListNode: Head of the linked list.
    """
    if not values:
        return None

    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]

###############################################
# Example Usage (Can be removed before submission)
###############################################

if __name__ == "__main__":
    # Create a linked list with a cycle
    head = build_list([3, 2, 0, -4], pos=1)

    print("Cycle detected (Brute-force):", has_cycle_bruteforce(head))
    print("Cycle detected (Floyd's):", has_cycle_floyd(head))

    # Create a linked list without a cycle
    head2 = build_list([1, 2, 3, 4, 5], pos=-1)

    print("Cycle detected (Brute-force):", has_cycle_bruteforce(head2))
    print("Cycle detected (Floyd's):", has_cycle_floyd(head2))
