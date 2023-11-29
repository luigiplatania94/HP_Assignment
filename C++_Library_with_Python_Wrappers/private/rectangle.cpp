#include "../public/rectangle.h"

Rectangle::Rectangle(double l, double w) : length(l), width(w) {}

double Rectangle::getArea() const {
    return length * width;
}

double Rectangle::getPerimeter() const {
    return 2 * (length + width);
}
