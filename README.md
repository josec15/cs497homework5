# cs497homework5

## Question 1


## Question 2
To solve this, we would need to do an in order traversal of the binary search tree so that we  
can get the nodes values in sorted order. First we check if we have a valid tree by checking if the first node is null. Next, we do dfs on the left subtree which sets prev to the left most node. If that left most node is not null we take the minimum value of the result which is calculated by the current node value minus the previous node value. We do the same with the right subtree and return result.
Time complexity = O(n), since we visit every node once. 
Space complexity = O(1), since we do not use any extra space.

## Question 3
In order to solve this we would need to implement a breadth first search. First we calculate the number of nodes in the graph, calculate the bit mask which will be used to check if all nodes have been visited during the traversal. Initialize a double ended queue with lists that represents the state of each node and includes the node (i), the bit mask, and the path length. We also need to initialize a visited set with tuples that represents each visited node and their bit mask. While the queue is not empty, we want to dequeue a tuple from the left and check if the bit mask is equal to the final bit mask. If so we want to return the number of steps taken which will represent the shortest path to all visited nodes. The last for loop iterates over the neighbors of the current node and updates the bit mask. If it is not visited then we add it to the visited set and increment the steps. 
Time complexity = O(2^n * 2), where n is the number of nodes. 
Space complexity = O(2^n * n), since we create a visited set and queue.

## Question 4
We can solve this using a recursive depth first search that traverses a binary tree. Recursively calculate the max path sum of the left and right sides of the tree. We also need to add the root value to the left and right max sums and update the result.
Time complexity = O(n), n being the number of nodes in the tree
Space complexity = O(1), no extra space is used.