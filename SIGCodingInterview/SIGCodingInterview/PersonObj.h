#include "CarObj.h"
using namespace std;
#pragma once
class PersonObj
{
public:
	PersonObj();
	~PersonObj();

	//inserts car data for a particular person
	void InsertCar(string p, string c, int m, int g, int d);

	//gets a list of cars for a person between two date ranges
	map<string, float> GetListOfCarsWithinRange(string p, int s, int e);

private:
	unordered_map<string, CarObj> m_personHash;
};

