// SIGCodingInterview.cpp : Defines the entry point for the console application.
// Author : Joseph Luce
// October 2016

/*
Given file with entries consisting of person name, car brand, miles driven, gallons filled, date of fill.

Create a method to output a list of objects of miles per gallon per car when for a person name, a start date, and end date.
Miles per gallon is total miles driven and gallons filled for a particular car brand.

*/

#include "stdafx.h"
#include "PersonObj.h"
#include <map>
#include <iostream>

using namespace std;

int main()
{
	map<string, float> mapResult;
	PersonObj personHolder;

	//ignored parsing the data from a file, went straight to the construction of the data
	//person, car name, miles, gallons, date(year/month/day)
	personHolder.InsertCar("Jack", "Ford", 150, 5, 20160520);
	personHolder.InsertCar("Mike", "Hyundai", 55, 2, 20160503);
	personHolder.InsertCar("Jack", "Ford", 200, 2, 20160521);
	personHolder.InsertCar("Jack", "BMW", 75, 2, 20160521);
	personHolder.InsertCar("Jack", "BMW", 40, 1, 20160522);
	personHolder.InsertCar("Jack", "Ford", 125, 3, 20160522);
	personHolder.InsertCar("Mike", "Hyundai", 60, 1, 20160502);
	personHolder.InsertCar("Jack", "BMW", 200, 5, 20160525);
	personHolder.InsertCar("Mike", "Hyundai", 100, 4, 20160501);
	personHolder.InsertCar("Jack", "Ford", 20, 4, 20160521);

	mapResult = personHolder.GetListOfCarsWithinRange("Jack", 20160520, 20160522);
	for (auto m : mapResult) {
		cout << m.first.c_str() << " " << m.second << endl;
	}
	mapResult = personHolder.GetListOfCarsWithinRange("Mike", 20160501, 20160503);
	for (auto m : mapResult) {
		cout << m.first.c_str() << " " << m.second << endl;
	}

    return 0;
}

