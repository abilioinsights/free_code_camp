class TreeNode:
    """
    Represents a node in a Binary Search Tree (BST).

    Attributes:
        key (int): The value stored in the node.
        left (TreeNode): The left child of the node.
        right (TreeNode): The right child of the node.
    """
    def __init__(self, key):
        """
        Initializes a TreeNode with the given key.

        Args:
            key (int): The value to be stored in the node.
        """
        self.key = key
        self.left = None  # Left child
        self.right = None  # Right child

    def __str__(self):
        """
        Returns the string representation of the node's key.

        Returns:
            str: The key as a string.
        """
        return str(self.key)


class BinarySearchTree:
    """
    Represents a Binary Search Tree (BST).

    Attributes:
        root (TreeNode): The root node of the BST.
    """
    def __init__(self):
        """
        Initializes an empty BST.
        """
        self.root = None  # Root of the BST

    def _insert(self, node, key):
        """
        Inserts a new key into the BST recursively.

        Args:
            node (TreeNode): The current node being processed.
            key (int): The key to be inserted.

        Returns:
            TreeNode: The updated node after insertion.
        """
        if node is None:
            return TreeNode(key)  # Create a new node if the current node is None

        if key < node.key:
            node.left = self._insert(node.left, key)  # Insert into the left subtree
        elif key > node.key:
            node.right = self._insert(node.right, key)  # Insert into the right subtree

        return node  # Return the updated node

    def insert(self, key):
        """
        Public method to insert a key into the BST.

        Args:
            key (int): The key to be inserted.
        """
        self.root = self._insert(self.root, key)

    def _search(self, node, key):
        """
        Searches for a key in the BST recursively.

        Args:
            node (TreeNode): The current node being processed.
            key (int): The key to be searched.

        Returns:
            TreeNode: The node containing the key, or None if the key is not found.
        """
        if node is None or node.key == key:
            return node  # Return the node if found or if the current node is None

        if key < node.key:
            return self._search(node.left, key)  # Search in the left subtree
        return self._search(node.right, key)  # Search in the right subtree

    def search(self, key):
        """
        Public method to search for a key in the BST.

        Args:
            key (int): The key to be searched.

        Returns:
            TreeNode: The node containing the key, or None if the key is not found.
        """
        return self._search(self.root, key)

    def _delete(self, node, key):
        """
        Deletes a key from the BST recursively.

        Args:
            node (TreeNode): The current node being processed.
            key (int): The key to be deleted.

        Returns:
            TreeNode: The updated node after deletion.
        """
        if node is None:
            return node  # Return None if the node is not found

        if key < node.key:
            node.left = self._delete(node.left, key)  # Delete from the left subtree
        elif key > node.key:
            node.right = self._delete(node.right, key)  # Delete from the right subtree
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right  # Replace the node with its right child
            elif node.right is None:
                return node.left  # Replace the node with its left child

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)  # Delete the inorder successor

        return node  # Return the updated node

    def delete(self, key):
        """
        Public method to delete a key from the BST.

        Args:
            key (int): The key to be deleted.
        """
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        """
        Finds the minimum value in a subtree.

        Args:
            node (TreeNode): The root of the subtree.

        Returns:
            int: The minimum value in the subtree.
        """
        while node.left is not None:
            node = node.left  # Traverse to the leftmost node
        return node.key

    def _inorder_traversal(self, node, result):
        """
        Performs an inorder traversal of the BST recursively.

        Args:
            node (TreeNode): The current node being processed.
            result (list): A list to store the traversal result.
        """
        if node:
            self._inorder_traversal(node.left, result)  # Traverse the left subtree
            result.append(node.key)  # Visit the current node
            self._inorder_traversal(node.right, result)  # Traverse the right subtree

    def inorder_traversal(self):
        """
        Public method to perform an inorder traversal of the BST.

        Returns:
            list: A list of keys in ascending order.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result


# Example usage
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)

print('Search for 80:', bst.search(80))  # Output: 80
print("Inorder traversal:", bst.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 70, 80]

bst.delete(40)
print("Search for 40:", bst.search(40))  # Output: None
print('Inorder traversal after deleting 40:', bst.inorder_traversal())  # Output: [20, 30, 50, 60, 70, 80]
