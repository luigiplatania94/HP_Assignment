#pragma once

class Triangle {
public:
    Triangle(double side1, double side2, double side3);
    double getArea() const;
    double getPerimeter() const;

private:
    double side1, side2, side3;
};
