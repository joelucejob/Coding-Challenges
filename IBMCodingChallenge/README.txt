One of several IBM coding challenges I did online.

This challenge was very strange, as to me, it didn't exactly test any algothrim I came across. When reading the question I immediately thought of Breath-First Search but after a bit I noticed the one-way relationships the managers had with the employees. As long as there is no cycle, the logic should work perfectly.

EXPLANATION:
So using the idea that the relationships are only one way and there would not exist cycles. I basically tried to approach this as a graph problem but the attributes of the problem didn't quite fit will with adjacency matrixes or adjacency lists. It would be better if everything was placed into a hash map. First pass thru with employee1 would create a visited set down the chain of command by first reversing the relationships between employees to managers when inserting them into the map. Using the employees as the key. Second pass thru with employee2 would go down the chain and check the visited set from the first pass thru if that node was visited. If it was, then we found the node and output it. Simple and straight forward.
