cmake_minimum_required(VERSION 3.18)
project(Qynva LANGUAGES CXX CUDA)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(CUDA QUIET)
find_package(OpenCL QUIET)

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)

# Add subdirectories
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../src)

# Optional: Add tests if enabled
option(BUILD_TESTS "Build tests" OFF)
if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../tests)
endif()

# Optional: Add examples if enabled
option(BUILD_EXAMPLES "Build examples" OFF)
if(BUILD_EXAMPLES)
    add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../examples)
endif()