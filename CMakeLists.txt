cmake_minimum_required(VERSION 3.9.1)
project(Wiffle)

add_library(paulslib paulslib.c)
target_include_directories(paulslib PUBLIC ${CMAKE_CURRENT_LIST_DIR}/paulslib.h)

add_library(bitmaplib bitmaplib.c)
target_include_directories(bitmaplib PUBLIC ${CMAKE_CURRENT_LIST_DIR}/bitmaplib.h)

add_executable(makewiffle makewiffle.c paulslib.h bitmaplib.h)
target_link_libraries(makewiffle paulslib bitmaplib)

set_property(TARGET makewiffle PROPERTY C_STANDARD 90)
# set_target_properties(makewiffle C_STANDARD 90)