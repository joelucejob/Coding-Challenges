#include "stdafx.h"
#include "DataObj.h"


DataObj::DataObj()
{
	m_milesDriven = 0;
	m_gallonsFilled = 0;
}


DataObj::~DataObj()
{
}

DataObj::DataObj(int m, int g)
{
	m_milesDriven = m;
	m_gallonsFilled = g;
}

void DataObj::AddData(int m, int g) {
	m_milesDriven += m;
	m_gallonsFilled += g;
}