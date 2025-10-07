cmake_minimum_required(VERSION 3.15)
project(Qynva VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Set build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Compiler-specific options
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU" OR CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

if(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    add_compile_options(/W4)
endif()

# Include directories
include_directories(${CMAKE_SOURCE_DIR}/include)

# Source files
file(GLOB_RECURSE SOURCES "src/*.cpp")
file(GLOB_RECURSE HEADERS "include/*.h" "include/*.hpp")

# Create library or executable (adjust as needed)
# add_library(qynva ${SOURCES} ${HEADERS})
# add_executable(qynva_app ${SOURCES} ${HEADERS})

# Dependency management - fetch dependencies at build time
include(FetchContent)

# Example of fetching dependencies (uncomment and modify as needed)
# FetchContent_Declare(
#     googletest
#     GIT_REPOSITORY https://github.com/google/googletest.git
#     GIT_TAG        release-1.12.1
# )
# FetchContent_MakeAvailable(googletest)

# Enable testing
enable_testing()

# Add subdirectories
# add_subdirectory(src)
# add_subdirectory(tests)

# Installation rules
# install(TARGETS qynva DESTINATION lib)
# install(FILES ${HEADERS} DESTINATION include/qynva)