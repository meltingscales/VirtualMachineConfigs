// ppm-circles.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <string>
#include <fstream>
#include <cstddef>
#include <filesystem>
namespace fs = std::filesystem;

class Point {
public:
	double x, y;

	Point(double x1, double y1) {
		x = x1;
		y = y1;
	}

};

// Return the distance between two points.
int distance(Point p1, Point p2) {
	return sqrt(
		(pow((p2.x - p1.x), 2.0) + pow((p2.y - p1.y), 2.0))
	);
}

std::string generate_circle_ppm(int diameter, int colordepth) {

	using namespace std;

	string black = "0  0  0"; // Black.
	string white = to_string(colordepth) + " " + to_string(colordepth) + " " + to_string(colordepth); // Longest string.

	string ppmstr = "P3\n"; // Magic number
	ppmstr += to_string(diameter) + " " + to_string(diameter) + "\n"; // Dimensions
	ppmstr += to_string(colordepth) + "\n"; // Color depth

	Point middle = Point(diameter / 2.0, diameter / 2.0); // Middle of the circle
	double radius = (diameter - 1.0) / 2.0; // Radius is 1/2 of diameter

	for (int y = 0; y < diameter; y++) { // For all columns,

		for (int x = 0; x < diameter; x++) { // For all rows,

			Point p = Point(x, y); // Our point at x,y
			string to_add; // Pixel to add

			if (distance(p, middle) <= radius) {// If the distance from our point to the middle of the circle is within the radius of the circle,
				to_add = to_string(colordepth) + " 0  0"; // Red!
			}
			else { //It's outside the circle
				to_add = black; // Black!
			}

			ppmstr += to_add + " "; // Add pixel

		}
		ppmstr += "\n"; // New column
	}

	return ppmstr;
}

int main()
{
	using namespace std;
	using namespace filesystem;

	string filename = "image.ppm";
	string circle_data = generate_circle_ppm(20, 15);

	ofstream myfile;
	myfile.open(filename);
	myfile << circle_data;
	myfile.close();

	cout << "You can find your " << (circle_data.size()) << "-byte image at:\n" << fs::canonical(filename) << "\n";

	return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
