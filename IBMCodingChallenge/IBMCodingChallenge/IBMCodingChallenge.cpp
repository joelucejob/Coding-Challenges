// IBMCodingChallenege.cpp : Defines the entry point for the console application.
//

//Author : Joseph Luce
//October 2016

/*
Programming Challenge Description :
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
*/

#include "stdafx.h"
#include <string>
#include <unordered_map>
#include <iostream>
#include <unordered_set>

using namespace std;


int main()
{
	static const string test1 = "Frank->Mary,Mary->Sam,Mary->Bob,Sam->Katie,Sam->Pete,Bob->John,Katie->Steve,Steve,Bob"; //answer = Mary
	static const string test2 = "Sam->Pete,Pete->Nancy,Sam->Katie,Mary->Bob,Frank->Mary,Mary->Sam,Bob->John,Pete,John"; // answer = Mary
	static const string test3 = "Frank->Mary,Mary->Sam,Mary->Bob,Sam->Katie,Sam->Pete,Bob->John,Pete,Katie"; // answer = Mary
	static const string test4 = "Sam->Pete,Pete->Nancy,Sam->Katie,Mary->Bob,Frank->Mary,Mary->Sam,Bob->John,Sam,John"; //answer = Mary
	static const string test5 = "Tom->Mary,Mary->Bob,Mary->Sam,Bob->John,Sam->Pete,Sam->Kate,Pete,Kate"; // answer = Sam

	//we will reverse the relationship since each employee can have only one manager, we will use a hashmap to represent this
	unordered_map<string, string> myMap;
	string stringToTest = test3; //change stringToTest to test another string
	string employee1, employee2;
	size_t posNext = 0;
	size_t posLast = 0;

	//parse thru the string
	while ((posNext = stringToTest.find(",", posLast)) != string::npos) {
		string tmpString = stringToTest.substr(posLast, posNext - posLast);
		size_t pos;
		string employee, manager;
		if ((pos = tmpString.find("->")) != string::npos) {
			manager = tmpString.substr(0, pos);
			employee = tmpString.substr(pos + 2);
			myMap.emplace(employee, manager);
		}
		else {
			if (employee1.empty()) {
				employee1 = tmpString;
			}
		}
		posLast = ++posNext;
	}
	employee2 = stringToTest.substr(posLast);

	//use this set to keep track of which nodes were visited
	unordered_set<string> visited;

	//traverse with employee1 and mark all managers as visited unless its employee1 or employee2
	auto it = myMap.find(employee1);
	while (it != myMap.end()) {
		if (it->second != employee1 || it->second != employee2) {
			visited.emplace(it->second);
		}
		it = myMap.find(it->second);
	}

	//continue searching with employee2 and find traces of employee1's footsteps, ignore instances of employee1 or employee2
	string result;
	it = myMap.find(employee2);
	while (it != myMap.end() ||
		it->first == employee1 &&
		it->first == employee2) {
		//if its visited, we know we found a match
		if (visited.find(it->second) != visited.end()) {
			result = it->second;
			break;
		}
		it = myMap.find(it->second);
	}

	//overall run-time is O(n) with O(n) extra space.
	//can have worst case scenario where its just a long chain of management and not a tree.
	cout << result << endl;
	return 0;
}