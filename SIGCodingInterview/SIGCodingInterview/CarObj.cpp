#include "stdafx.h"
#include "CarObj.h"
#include <iostream>

using namespace std;

CarObj::CarObj()
{
}


CarObj::~CarObj()
{
}

void CarObj::InsertData(string c, int m, int g, int d)
{
	m_carHash[c][d].AddData(m, g);
}

float CarObj::GetMPGForDateRange(string c, int s, int e)
{
	//if we can't find the car or ranges are incorrect
	if (m_carHash.find(c) == m_carHash.end() ||
		s > e) 
	{
		return 0;
	}

	auto itLower = m_carHash[c].lower_bound(s);
	auto itUpper = m_carHash[c].upper_bound(e);
	
	float totalMiles = 0.0f;
	float totalGallons = 0.0f;

	//sum up all the miles and gallons for this car between the dates
	while (itLower != itUpper)
	{
		totalMiles += itLower->second.GetMilesDriven();
		totalGallons += itLower->second.GetGallonsFilled();
		//cout << totalMiles << " " << totalGallons << endl;
		itLower++;
	}

	return (totalMiles / totalGallons);
}

map<string, float> CarObj::GetListOfMPGs(int s, int e)
{
	map<string, float> result;

	//for all cars, get the MPGs
	for (auto it : m_carHash) {
		result.emplace(it.first, GetMPGForDateRange(it.first, s, e));
	}
	return result;
}