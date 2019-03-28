project("SACA Benchmark")
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
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS_RELEASE} -Wall")

add_executable(divsufsort_saca ${CMAKE_CURRENT_SOURCE_DIR}/divsufsort_saca.cpp)
add_executable(sais_nong_saca ${CMAKE_CURRENT_SOURCE_DIR}/sais_nong_saca.cpp)
add_executable(sais_yuta_saca ${CMAKE_CURRENT_SOURCE_DIR}/sais_yuta_saca.cpp)
add_executable(sais_test ${CMAKE_CURRENT_SOURCE_DIR}/sais_test.cpp)

include_directories(${CMAKE_SOURCE_DIR}/include)




target_link_libraries(sais_nong_saca ${CMAKE_SOURCE_DIR}/lib/libsais_nong.a)
target_link_libraries(sais_yuta_saca ${CMAKE_SOURCE_DIR}/lib/libsais_yuta.a)
target_link_libraries(divsufsort_saca ${CMAKE_SOURCE_DIR}/lib/libdivsufsort.a)
target_link_libraries(sais_test ${CMAKE_SOURCE_DIR}/lib/libsais_nong.a ${CMAKE_SOURCE_DIR}/lib/libsais_yuta.a ${CMAKE_SOURCE_DIR}/lib/libdivsufsort.a)

install(TARGETS sais_nong_saca sais_yuta_saca divsufsort_saca sais_test RUNTIME DESTINATION ${CMAKE_SOURCE_DIR}/bin)

