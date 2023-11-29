#include <pybind11/pybind11.h>
#include "../public/triangle.h"
#include "../public/rectangle.h"
#include "../public/circle.h"

namespace py = pybind11;

PYBIND11_MODULE(shapes, m) {
    py::class_<Triangle>(m, "Triangle")
        .def(py::init<double, double, double>())
        .def("getArea", &Triangle::getArea)
        .def("getPerimeter", &Triangle::getPerimeter);

    py::class_<Rectangle>(m, "Rectangle")
        .def(py::init<double, double>())
        .def("getArea", &Rectangle::getArea)
        .def("getPerimeter", &Rectangle::getPerimeter);

    py::class_<Circle>(m, "Circle")
        .def(py::init<double>())
        .def("getArea", &Circle::getArea)
        .def("getPerimeter", &Circle::getPerimeter);
}
