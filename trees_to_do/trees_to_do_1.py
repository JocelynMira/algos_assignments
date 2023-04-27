class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None # this is similar to head in linked list

    def add(self, val):
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
            return self
        runner = self.root
        # while runner != None:
        # same as above
        while runner:
            if val > runner.val: #if its more than where the runner is currently at
                if runner.right == None:
                    runner.right = new_node
                    return self
                else:
                    runner = runner.right
            if val < runner.val:
                if runner.left == None:
                    runner.left = new_node
                    return self
                else:
                    runner = runner.left



def contains (self, val):
    runner = self.root
    while runner:
        if runner.val == val:
            return True
        elif runner.val > val:
            runner = runner.left
        else: 
            runner = runner.right
    return False

def max(self):
    if self.root == None:
        return None
    runner = self.root
    while runner.right:
        runner = runner.right
    return runner.val


first_tree = BST()
first_tree.add(12).add(15).add(13).add(18).add(12.5)
first_tree.max()
# print(first_tree.root.right.right.val)
# print(first_tree.root.right.val)
# print(first_tree.root.right.left.right)
