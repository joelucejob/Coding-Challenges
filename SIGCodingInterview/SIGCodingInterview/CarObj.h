#include "DataObj.h"
#include <map>
#pragma once
using namespace std;
class CarObj
{
public:
	CarObj();
	~CarObj();

	//insert data for a particular car name
	void InsertData(string c, int m, int g, int d );

	//get the total MPG for a particular carname between two dates
	float GetMPGForDateRange(string c, int s, int e);

	//returns a list of cars and MPGs between two dates
	map<string, float> GetListOfMPGs(int s, int e);

private:
	// carname as key for a map of dates and data
	unordered_map<string, map<int, DataObj>> m_carHash;
};