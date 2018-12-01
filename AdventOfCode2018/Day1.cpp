#include "pch.h"
#include "Day1.h"


Day1::Day1()
{
	sumFrequency();
	checkDublicate();
}

void Day1::sumFrequency() {
	int sum = 0;
	fs.open(filename);
	int row;
	while (fs >> row) {
		sum += row;
	}
	std::cout << "Part 1: Sum of the frequency, " << sum << "\n";
}

int Day1::checkDublicate() {
	int sum = 0;
	int row;
	fs.open(filename);

	while (fs.is_open()) {
		if (fs.eof()) {
			fs.clear();
			fs.seekg(0, std::ios::beg);
		}
		fs >> row;
		sum += row;
		for (auto v : vect) {
			if (v == sum) {
				fs.close();
				std::cout << "Part 2: First dublicate is, " << sum << "\n";
				return sum;
			}
		}
		vect.push_back(sum);
	}
}