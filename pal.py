## This is the text editor interface.
## Anything you type or change here will be seen by the other person in real time.

class Node:
    ch = 'a'
    left = Node()
    right = Node()


# maps from node to size of its subgraph
sizeDict = computeSizeDict(root)
# A -> 15, B -> 7, C -> 3, D -> 1

# returns the kth character in the inorder traversal starting at root
# k is 0-indexed, k is never negative

def helperKthChar(root, cur_pos, k):
    if cur_pos < k: #look to the right
        helperKthChar(root.right, cur_pos + 1, k)
    elif cur_pos > k:
        helperKthChar(root.left(), cur_pos - 1, k)
    else:
        return root


def getKthChar(root, k):
    root_index = computeSizeDict(root.left())
    if k == root_index():
        return root
    else:
        return helperKthChar(root, root_index, k)


012
bac  k = n

  A
 / \
 B  C n = 3
 \\\\X

    A
   / \
   B  C
  / \
  D  E

 B
 DBE
 A_index = size(left)
 0123456
 cbcacbc
 7 = 2^n - 1
 A
||
 B
 ||
 c
 ||
 D

 given size(left sub graph)
 we know A's pos: if K < A_pos: left else: right
 case: A_pos == k: O(1)
 if k is 0: O(n)

 D: 0, 2,
 1, 5
 not dictionary, learning alg is dependent on knowing shape
 position: indicate children status and level

 DCD B DCD A --DCD B DCD

 A
  \
   B
    \
     C
      \
       D



 n = 2
