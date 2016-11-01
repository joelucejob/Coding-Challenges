#include <unordered_map>
#pragma once
class DataObj
{
public:
	DataObj();
	~DataObj();
	DataObj(int m, int g);

	//get functions
	int GetMilesDriven() { return m_milesDriven; }
	int GetGallonsFilled() { return m_gallonsFilled; }

	//total all miles and gallons for one date by incrementing them into one data node
	void AddData(int m, int g);

private:
	int m_milesDriven;
	int m_gallonsFilled;
};

