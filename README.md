# cs497homework5

## Question 1


## Question 2
To solve this, we would need to do an in order traversal of the binary search tree so that we  
can get the nodes values in sorted order. First we check if we have a valid tree by checking if the first node is null. Next, we do dfs on the left subtree which sets prev to the left most node. If that left most node is not null we take the minimum value of the result which is calculated by the current node value minus the previous node value. We do the same with the right subtree and return result.

## Question 3

