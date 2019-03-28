project("SACA Benchmark")
include( ExternalProject )

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

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
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Wall")

# add_subdirectory(external/libdivsufsort)
# add_subdirectory(external/sais-lite-2.4.1)
# add_subdirectory(external/sais-nong)


ExternalProject_add(divsufsort_project
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/external/libdivsufsort
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}/external/libdivsufsort/build
    INSTALL_DIR = "${CMAKE_SOURCE_DIR}"
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_SOURCE_DIR})

ExternalProject_add(sais_yuta_project
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/external/sais-lite-2.4.1
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}//external/sais-lite-2.4.1/build
    INSTALL_DIR = "${CMAKE_SOURCE_DIR}"
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_SOURCE_DIR})

ExternalProject_add(sais_nong_project
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/external/sais-nong
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}/external/sais-nong-build
    INSTALL_DIR = "${CMAKE_SOURCE_DIR}"
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_SOURCE_DIR})


add_library(sais_nong STATIC IMPORTED)
set_property(TARGET sais_nong PROPERTY IMPORTED_LOCATION ${install_dir}/lib/libluajit-5.1.a)

add_subdirectory(src)

