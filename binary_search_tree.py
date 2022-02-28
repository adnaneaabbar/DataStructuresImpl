class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, newValue):
        if self.value is None:
            self.value = newValue
            return

        if self.value == newValue:  # ignoring duplicates
            return

        if self.value > newValue:  # if we add >= we will be placing duplicates on the left
            if self.left:
                self.left.insert(newValue)
            else:
                self.left = BST(newValue)
        else:
            if self.right:
                self.right.insert(newValue)
            else:
                self.right = BST(newValue)

    def search(self, searchValue):
        if self.value == searchValue:
            print(f"{searchValue} Found !")
            return

        if self.value > searchValue:
            if self.left:
                self.left.search(searchValue)
            else:
                print(f"{searchValue} Not Found !")
        else:
            if self.right:
                self.right.search(searchValue)
            else:
                print(f"{searchValue} Not Found !")

    def pre_order(self):  # root  ---> left ---> right
        print(self.value, end="   ")

        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def post_order(self):  # left  ---> right ---> root
        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()

        print(self.value, end="   ")

    def in_order(self):  # left  ---> root ---> right
        if self.left:
            self.left.in_order()

        print(self.value, end="   ")

        if self.right:
            self.right.in_order()

    def delete(self, deleteValue):
        if self.value is None:
            print("Tree is empty !")
            return

        if self.value > deleteValue:
            if self.left:
                self.left = self.left.delete(deleteValue)
            else:
                print(f"{deleteValue} is not in the Tree !")
        elif self.value < deleteValue:
            if self.right:
                self.right = self.right.delete(deleteValue)
            else:
                print(f"{deleteValue} is not in the Tree !")
        else:  # self is now pointing to the node we are deleting

            # if node has 1 child we replace with that child
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp

            # if node has 2 children, either replace it with bigger value of left or smallest value of right

            '''
            # replacing with smallest value of right
            node = self.right
            while node.left:
                node = node.left

            self.value = node.value # update the value of the node with smallest right
            self.right = self.right.delete(node.value)

            '''

            # replacing with bigger value of left
            node = self.left
            while node.right:
                node = node.right
            self.value = node.value  # update the value of the node with bigger left
            self.left = self.left.delete(node.value)

        return self

    def minimum(self):
        curr = self
        while curr.left:
            curr = curr.left
        print(f"{curr.value} is the MINIMUM !")

    def maximum(self):
        curr = self
        while curr.right:
            curr = curr.right
        print(f"{curr.value} is the MAXIMUM !")


def count(tree):
    if tree is None:
        return 0
    return 1 + count(tree.left) + count(tree.right)


def driver(name):
    print(f"{name} Driver Code")
    '''
        root = BST(10)
        root.left = BST(5)
        root.right = BST(20)
        root.right.left = BST(15)
        root.right.right = BST(25)
        '''

    print("\n\nInserting")
    root = BST(10)
    l = [5, 20, 15, 25, 2, 7, 1, 9]
    for value in l:
        root.insert(value)

    root.in_order()

    print("\n\nFinding minimum")
    root.minimum()

    print("\n\nFinding maximum")
    root.maximum()

    print("\n\nSearching")
    root.search(8)
    root.search(7)

    print("\n\nPre_order")
    root.pre_order()

    print("\n\nPost_order")
    root.post_order()

    print("\n\nIn_order")
    root.in_order()

    empty_tree = BST(None)
    print("\n\nDeleting from empty tree")
    empty_tree.delete(1)
    print("\n\nDeleting non existant")
    root.delete(8)

    print("\n\nBefore delete")
    root.pre_order()
    root.delete(2)
    print("\n\nAfter delete")
    root.pre_order()

    print("\n\nDeleting root")
    print("Before delete")
    root.pre_order()
    root.delete(10)
    print("\n\nAfter delete")
    root.pre_order()

    print("\n\nDeleting tree containing one node")
    root = BST(100)
    if count(root) <= 1:
        print("\n\nYou can't delete root of a tree containing only one node !")
    else:
        root.delete(100)


if __name__ == "__main__":
    driver("BST")