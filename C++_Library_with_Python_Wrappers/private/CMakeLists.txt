# List your source files here
set(SOURCES circle.cpp rectangle.cpp triangle.cpp)

# Create a library from the source files
add_library(shapes_library STATIC ${SOURCES})

# Include the public directory to allow access to header files
target_include_directories(shapes_library PUBLIC ../public)
