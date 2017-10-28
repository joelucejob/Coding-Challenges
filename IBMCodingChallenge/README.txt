# IBM Coding Challenge Question:
Develop a service to help a client quickly find a manager who can resolve the conflict between two employees.When there is a conflict between two employees, the closest common manager should help resolve the conflict.The developers plan to test the service by providing an example reporting hierarchy to enable the identification of the closest common manager for two employees.Your goal is to develop an algorithm for IBM to efficiently perform this task.To keep things simple, they just use a single relationship "isManagerOf" between any two employees.For example, consider a reporting structure represented as a set of triples :
Tom isManagerOf Mary
Mary isManagerOf Bob
Mary isManagerOf Sam
Bob isManagerOf John
Sam isManagerOf Pete
Sam isManagerOf Katie
The manager who should resolve the conflict between Bob and Mary is Tom(Mary's manager). The manager who should resolve the conflict between Pete and Katie is Sam(both employees' manager).The manager who should resolve the conflict between Bob and Pete is Mary(Bob's manager and Pete's manager's manager).
Assumptions:
There will be at least one isManagerOf relationship.
There can be a maximum of 15 team member to a single manager
No cross management would exist i.e., a person can have only one manager
There can be a maximum of 100 levels of manager relationships in the corporation
Input :
R1, R2, R3, R4...Rn, Person1, Person2 R1...Rn - A comma separated list of "isManagerOf" relationships.Each relationship being represented by an arrow "Manager->Person".Person1, Person2 - The name of the two employee that have conflict
Output :
The name of the manager who can resolve the conflict Note : Please be prepared to provide a video follow - up response to describe your approach to this exercise.
Test 1 :
Test Input
Frank->Mary, Mary->Sam, Mary->Bob, Sam->Katie, Sam->Pete, Bob->John, Bob, Katie
Expected Output
Mary
Test 2:
Test Input
Sam->Pete, Pete->Nancy, Sam->Katie, Mary->Bob, Frank->Mary, Mary->Sam, Bob->John, Sam, John
Expected Output
Mary

# One of several IBM coding challenges I did online.

This challenge was very strange, as to me, it didn't exactly test any algothrim I came across. When reading the question I immediately thought of Breath-First Search but after a bit I noticed the one-way relationships the managers had with the employees. As long as there is no cycle, the logic should work perfectly.

# EXPLANATION:
So using the idea that the relationships are only one way and there would not exist cycles. I basically tried to approach this as a graph problem but the attributes of the problem didn't quite fit well with adjacency matrixes or adjacency lists. It would be better if everything was placed into a hash map. First pass thru with employee1 would create a visited set down the chain of command by first reversing the relationships between employees to managers when inserting them into the map. Using the employees as the key. Second pass thru with employee2 would go down the chain and check the visited set from the first pass thru if that node was visited. If it was, then we found the node and output it. Simple and straight forward.

# UPDATE October 2017:
After my post whiteboarding preparation phrase, I've revisited this question and now I know a better answer to this question.
Instead of my orginal solution, create a tree of nodes with relations of parent and child nodes. In this case, manager and employee. You want the child nodes to have references to the parents so handle that with extra pointers to the parent from the child. It is also helpful to keep a hash table of all employees that point to the nodes on the tree so you can immediately go to that node and start searching. 

Similar to breath-first-search, you will use a queue but in this case two queues, one for employee1 and another for empolyee2. You will go up the parent nodes with BFS and keep track with a list of visited nodes. You can optimize this by not going performing a BFS one at a time but an altering sequence between the two queues. If there was a secnario that your first queue has 1000+ parents but your second queue only had 10. You don't want to iterate through all that when the common manager is just 2-3 nodes away. As you are alternating between the two BFS, check if the node was already visited, if it is, then that is your answer, if one of your queues is empty before you even find a visited node, then there is no answer.
