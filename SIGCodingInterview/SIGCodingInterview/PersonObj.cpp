#include "stdafx.h"
#include "PersonObj.h"


PersonObj::PersonObj()
{
}


PersonObj::~PersonObj()
{
}

void PersonObj::InsertCar(string p, string c, int m, int g, int d)
{
	m_personHash[p].InsertData(c, m, g, d);
}

map<string, float> PersonObj::GetListOfCarsWithinRange(string p, int s, int e)
{
	//for a particular person, get all the MPGs for all his/her cars
	return m_personHash[p].GetListOfMPGs(s, e);
}