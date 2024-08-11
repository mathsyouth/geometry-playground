cmake_minimum_required(VERSION 3.10)

# 项目名称和版本号
project(PlainKnit VERSION 1.0)

# 设置 C 标准
set(CMAKE_C_STANDARD 90)
set(CMAKE_C_STANDARD_REQUIRED True)

# 设置编译器标志
if (MSVC)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /O2 /Wall /Fe")
else ()
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O3 -ansi -pedantic -Wall -Werror")
endif()

# 添加可执行文件
add_executable(plain-knit code/plain-knit.c)

# 添加 clean_build 目标
add_custom_target(clean_build
    COMMAND ${CMAKE_COMMAND} -E rm -f plain-knit
    COMMENT "Cleaning up"
)

# 添加 clean_all 目标，删除 build 文件夹
add_custom_target(clean_all
    COMMAND ${CMAKE_COMMAND} -E remove_directory ${CMAKE_BINARY_DIR}
    COMMENT "Cleaning up build directory"
)