# Define a class for the binary tree node
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Function to insert a new node with a given key into the tree
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        # Recursively insert the key in the appropriate subtree
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Function to perform an in-order traversal of the tree (left-root-right)
def inorder_traversal(root, result):
    if root:
        # Recursively traverse the left subtree
        inorder_traversal(root.left, result)
        # Append the current node's value to the result
        result.append(root.val)
        # Recursively traverse the right subtree
        inorder_traversal(root.right, result)

# Function to perform tree sort
def tree_sort(arr):
    root = None
    # Insert each element from the input array into the binary search tree
    for item in arr:
        root = insert(root, item)

    result = []
    # Perform in-order traversal to retrieve the sorted elements
    inorder_traversal(root, result)
    return result

# Example usage
if __name__ == "__main__":
    input_list = [4, 2, 6, 1, 3, 5, 7]
    sorted_list = tree_sort(input_list)
    print("Original List:", input_list)
    print("Sorted List:", sorted_list)
