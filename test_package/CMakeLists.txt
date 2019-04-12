cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})

enable_testing()

add_test(
  NAME ${PROJECT_NAME}
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
  COMMAND $<TARGET_FILE:${PROJECT_NAME}>
)
