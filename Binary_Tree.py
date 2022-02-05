# Brian Guevara
# StudentID: 001003681


# BST.py
# This is the Binary  Tree class. We use a binary tree data structures when we grab the packages
# from the input CSV file. We will use this structure to find the fastest route and update delivery times


class Node:
    # Creates a Node with empty left and right Nodes
    # Big-O: O(1)
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# This method gets the size of binary  tree
# Big-O: O(log N)
def get_size(node):
    if node is None:
        return 0
    else:
        # Adds up the number of successful iterations
        return get_size(node.left) + 1 + get_size(node.right)


# Following methods check to see if a package exists in a tree
# Big-O: O(log N)
def has_package(node, value=[]):
    # If the Node is empty, return false
    if node is None:
        return
    # If it contains our package then keep checking
    if node.data == value:
        return True
    # Else, check if it's in the left and right nodes
    else:
        if has_package(node.left, value):
            return True
        elif has_package(node.right, value):
            return True
    return False


# Method checks a tree for a specific address ID
# Big-O: O(log N)
def has_address(node, key):
    # If the node is None, then return
    if node is None:
        return
    # True if the address id is in the tree
    if int(node.data[0]) == key:
        return True
    # Else, keep checking and return true if it's somewhere
    else:
        if has_address(node.left, key):
            return True
        elif has_address(node.right, key):
            return True
    return False


class truck_bt:
    # Big-O: O(1)
    def __init__(self):
        self.root = None

    # Our insert method for the truck binary tree
    # Big-O: O(N)
    def insert(self, new_node):
        # If the tree is empty, then use the root
        if self.root is None:
            self.root = new_node
            new_node.left = None
            new_node.right = None
        else:
            # Set current note to the root node
            cur = self.root
            # while current is not none
            while cur is not None:
                # If the package ID is less than the current node
                if (new_node.data[0]) < (cur.data[0]):
                    # if the current left node is None then set it as the new node with our data
                    if cur.left is None:
                        cur.left = new_node
                        # current equals ends will end the loop
                        cur = None
                    else:
                        # Keep moving down the left side of the tree
                        cur = cur.left


                # Else, if the package ID is greater than the current
                else:
                    # if the right node is empty then set it as the new nodee
                    if cur.right is None:
                        cur.right = new_node
                        cur = None
                    else:
                        # Else keep moving down the list
                        cur = cur.right
            # Set the new node's left and right nodes to be none/empty
            new_node.left = None
            new_node.right = None


class address_bt:
    # Big-O: O(1)
    def __init__(self):
        self.root = None

    # Insertion method for our binary  tree. Procedure is the same as the other insertion method
    # main difference is that these nodes only have one piece of data (not an array of data like a package)
    # Big O: O(N)
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            new_node.left = None
            new_node.right = None
        else:
            current = self.root
            while current is not None:
                if new_node.data == current.data:
                    return
                if int(new_node.data) < int(current.data):
                    if current.left is None:
                        current.left = new_node
                        current = None
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        current = None
                    else:
                        current = current.right
            new_node.left = None
            new_node.right = None

    # This is our removal method
    # Big O: O(N)
    def remove_add_id(self, key):
        # Parent node is None
        parent = None
        # Current node is the root
        current = self.root
        # while the current node has data
        while current is not None:
            # if this is the node we are looking for
            if current.data == key:
                # If the Node does not have childrent
                if current.left is None and current.right is None:
                    # In case this is the first node, set the whole tree to None
                    if parent is None:
                        self.root = None
                    # else if this is the left node of the parent, then set that parent's left to None
                    elif parent.left == current:
                        parent.left = None
                    # do the same if it's the right node
                    else:
                        parent.right = None

                # Else if the left node has data
                elif current.left is not None and current.right is None:
                    # If the parent is None then set the left node as the root node
                    if parent is None:
                        self.root = current.left
                    # if this is the parent's left then set it as the current's left
                    elif parent.left == current:
                        parent.left = current.left
                    # do the same if it's the right side
                    else:
                        parent.right = current.left

                # Same logic as the left Node having data, but the right one being empty
                # only difference is we are assigning the current's right node to replace
                # the current node
                elif current.right is not None and current.left is None:
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right

                # If both nodes have data
                else:
                    # Successor node is move to the one on the right
                    successor = current.right
                    # Then, we continue to move down the left nodes/lower values
                    while successor.left is not None:
                        # Move to the left
                        successor = successor.left
                    # Create a temporary value of the successor
                    temp = successor.data
                    # recursively call this method
                    self.remove_add_id(temp)
                    # assign the current node's data with the temp
                    current.data = temp
                return
            # Move to the right if our current data is less than the ID we are searching for
            elif (current.data < key):
                parent = current
                current = current.right
            # Do the opposite if the current data is more than the ID
            else:
                parent = current
                current = current.left
        return
