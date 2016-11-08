QUESTION: 
Given file with entries consisting of person name, car brand, miles driven, gallons filled, date of fill.
Example : Mike, Ford, 83, 4, 20160415
Create a method to output a list of objects of miles per gallon per car when for a person name, a start date, and end date.
Miles per gallon is total miles driven and gallons filled for a particular car brand.

Coding challenge I did on SIG's on-site interviews. 
I kinda botched the interview, even though I got a very optimized solution, I was too stressed in creating clean and maintainable code.
I was mainly struggling with not knowing that STL maps had lower and upper bound methods and wasn't using a binary tree to its full advantage. Instead I choose to use a binary search on an array which was a lot more work than what the question is asking.
I went back and attempted it a second time after with an entirely different approach I had during the interview after thinking about a better implementation.
This challenge tests your use of data structures, libraries, algothrims and most importantly your object oriented approach.
Great question to practice for interviews.

EXPLANATION:
So my answer trys to make searching for MPGs within a range as quick as possible. Worst case is n, n being all the entries and each entry has a unique date while searching for all dates. Best case is O(1) or Olog(n) lookup, when searching for one date using some optimizations I'll explain later.
Mainly designed a hash table of persons, with each person having another hash table of cars while each car has a BST ordered by dates that hold data to the miles and gallons used/filled on that date. Using some optimization and how the question is worded, the program will sum up the miles and gallons on that particular date instead of making multiple dates with other data. So we end up with one data point for each date in the BST.
Designing the classes this way will keep maintainability easy, as of October 2016, is the best approach I can come up with. I still need more improvements but this is what I have so far.

Keep practicing!
