cmake_minimum_required(VERSION 3.12)
project(ShapesModule)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 11)

# Add the subdirectories for the library and Python module
add_subdirectory(private)
add_subdirectory(python)
