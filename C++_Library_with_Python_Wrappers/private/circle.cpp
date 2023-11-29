#include "../public/circle.h"
#include <cmath>

Circle::Circle(double r) : radius(r) {}

double Circle::getArea() const {
    return pi * radius * radius;
}

double Circle::getPerimeter() const {
    return 2 * pi * radius;
}
