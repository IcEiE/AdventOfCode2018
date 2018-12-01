#pragma once
#include <iostream>
#include <fstream>
#include <vector>
class Day1
{
public:
	Day1();
	void sumFrequency();
	int checkDublicate();
private:
	int sum = 0;
	std::string filename = ".\\..\\Textfiles\\d1p1.txt";
	std::fstream fs;
	std::vector<int> vect;
};