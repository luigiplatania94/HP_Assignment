find_package(Python COMPONENTS Development REQUIRED)
include_directories(${Python_INCLUDE_DIRS})
link_directories(${Python_LIBRARIES})

# Specify the path to pybind11 headers
set(pybind11_INCLUDE_DIR "C:/Users/luigi/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/local-packages/Python310/site-packages/pybind11/include")

# Include pybind11 headers
include_directories(${pybind11_INCLUDE_DIR})

# Create a Python module from the shapes_library
add_library(shapes MODULE shapes_module.cpp)

# Link the shapes_library to the Python library
target_link_libraries(shapes PRIVATE shapes_library python)


