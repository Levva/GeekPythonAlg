from binarytree import tree, Node, bst, build


a = tree(height=4, is_perfect=False)
print(a)

b = bst(height=3, is_perfect=True)
print(b)

c = build([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14])
print(c)

