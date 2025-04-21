"""
Binary Tree Traversal and Lowest Common Ancestor

This file implements:
1. In-order traversal of a binary tree.
2. Finding the Lowest Common Ancestor (LCA) of two nodes:
   - Brute-force approach.
   - Efficient optimized approach.

Author: [Your Name]
Date: [Submission Date]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

###############################################
# Part 1: In-Order Traversal (Recursive Method)
###############################################

def inorder_traversal(root):
    """
    Perform an in-order traversal of a binary tree.

    Args:
    root (TreeNode): The root node of the binary tree.

    Returns:
    List[int]: A list of values representing in-order traversal.
    """
    result = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)

    traverse(root)
    return result

###############################################
# Part 2: Lowest Common Ancestor
###############################################

# --- Brute Force Approach ---
# Step 1: Find the paths from root to p and q separately.
# Step 2: Compare the paths to find the last common node.

def find_path(root, target, path):
    """
    Helper function to find the path from root node to target node.

    Args:
    root (TreeNode): Current node.
    target (TreeNode): Target node to find.
    path (List[TreeNode]): Current path list.

    Returns:
    bool: True if path is found, False otherwise.
    """
    if not root:
        return False
    
    path.append(root)

    if root == target:
        return True

    if (find_path(root.left, target, path) or find_path(root.right, target, path)):
        return True

    path.pop()
    return False

def lowest_common_ancestor_bruteforce(root, p, q):
    """
    Find LCA using brute-force path comparison.

    Args:
    root (TreeNode): Root of the tree.
    p (TreeNode): First node.
    q (TreeNode): Second node.

    Returns:
    TreeNode: The LCA node.
    """
    path_p = []
    path_q = []

    find_path(root, p, path_p)
    find_path(root, q, path_q)

    lca = None
    for u, v in zip(path_p, path_q):
        if u == v:
            lca = u
        else:
            break

    return lca

# --- Efficient Approach (Single Traversal) ---

def lowest_common_ancestor_efficient(root, p, q):
    """
    Find LCA using a single DFS traversal (efficient method).

    Args:
    root (TreeNode): Root of the tree.
    p (TreeNode): First node.
    q (TreeNode): Second node.

    Returns:
    TreeNode: The LCA node.
    """
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor_efficient(root.left, p, q)
    right = lowest_common_ancestor_efficient(root.right, p, q)

    if left and right:
        return root

    return left if left else right

###############################################
# Optional: Utility to Build a Tree for Testing
###############################################

def build_sample_tree():
    """
    Build and return a sample binary tree for testing.

    Tree structure:
             3
            / \
           5   1
          / \ / \
         6  2 0 8
           / \
          7   4
    """
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    return root

###############################################
# Example Usage (Can be removed before submission)
###############################################

if __name__ == "__main__":
    # Build a sample tree
    root = build_sample_tree()
    p = root.left        # Node with value 5
    q = root.left.right.right  # Node with value 4

    # In-order Traversal
    print("In-order Traversal:", inorder_traversal(root))

    # Brute-force LCA
    lca_brute = lowest_common_ancestor_bruteforce(root, p, q)
    print("Brute-force LCA:", lca_brute.val)

    # Efficient LCA
    lca_efficient = lowest_common_ancestor_efficient(root, p, q)
    print("Efficient LCA:", lca_efficient.val)
