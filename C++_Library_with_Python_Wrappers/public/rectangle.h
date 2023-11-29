#pragma once

class Rectangle {
public:
    Rectangle(double length, double width);
    double getArea() const;
    double getPerimeter() const;

private:
    double length, width;
};
