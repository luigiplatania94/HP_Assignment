#pragma once

class Circle {
public:
    Circle(double radius);
    double getArea() const;
    double getPerimeter() const;

private:
    double radius;
    static constexpr double pi = 3.141592653589793;
};
