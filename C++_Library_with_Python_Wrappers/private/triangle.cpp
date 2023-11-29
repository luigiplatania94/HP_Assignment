#include "../public/triangle.h"
#include <cmath>

Triangle::Triangle(double s1, double s2, double s3) : side1(s1), side2(s2), side3(s3) {}

double Triangle::getArea() const {
    double s = (side1 + side2 + side3) / 2.0;
    return std::sqrt(s * (s - side1) * (s - side2) * (s - side3));
}

double Triangle::getPerimeter() const {
    return side1 + side2 + side3;
}
