cmake_minimum_required(VERSION 3.9.1)
project(simplify)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add executable
add_executable(simplify Main.cpp Simplify.h)

# If there are any additional libraries or dependencies, add them here
# For example:
# find_package(SomeLibrary REQUIRED)
# target_link_libraries(simplify PRIVATE SomeLibrary)

# Set compiler flags if needed
if(MSVC)
    target_compile_options(simplify PRIVATE /W4)
else()
    target_compile_options(simplify PRIVATE -Wall -Wextra -Wpedantic)
endif()

# If you need to include additional directories
# target_include_directories(simplify PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)

# If you have any other source files, add them here
# target_sources(simplify PRIVATE OtherSource.cpp AnotherSource.cpp)


