CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

project("SAIS Yuta" CXX)


set(CMAKE_CONFIGURATION_TYPES "Release" CACHE STRING "" FORCE)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


if (CMAKE_VERSION VERSION_LESS "3.1")
    if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
      set (CMAKE_CXX_FLAGS "--std=c++11 -fno-permissive ${CMAKE_CXX_FLAGS}")
    endif ()
else ()
    set (CMAKE_CXX_STANDARD 11)
endif ()


set(CMAKE_VERBOSE_MAKEFILE on)
message(STATUS "Release mode")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS_RELEASE} -Wall")

include_directories(include)
add_library(sais_yuta STATIC lib/sais.cpp)

install(TARGETS sais_yuta DESTINATION lib)
install(FILES include/sais.hpp DESTINATION include)