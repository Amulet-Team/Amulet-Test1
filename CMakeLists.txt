cmake_minimum_required(VERSION 3.13)

project(amulet_test1 LANGUAGES CXX)
set(SRC_INSTALL_DIR "." CACHE PATH "The path to the amulet package to install into.")

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 20)
  set(CMAKE_CXX_STANDARD_REQUIRED ON)
  set(CMAKE_CXX_EXTENSIONS OFF)
endif(NOT CMAKE_CXX_STANDARD)

add_definitions(-DPYBIND11_DETAILED_ERROR_MESSAGES)
if (WIN32)
	# set windows 7 as the minimum version
	add_definitions(-D_WIN32_WINNT=0x0601)
elseif(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET "10.15")
endif()

# Add pybind11 fallback
if (NOT TARGET pybind11::headers)
    add_subdirectory(submodules/pybind11)
endif()

add_library(amulet_test1 SHARED)
target_compile_definitions(amulet_test1 PRIVATE ExportAmuletTest1)
target_include_directories(amulet_test1 PUBLIC src)
target_sources(amulet_test1 PRIVATE src/amulet_test1/test1.cpp)

pybind11_add_module(_ext src/amulet_test1/__init_amulet_test1.cpp)
target_link_libraries( _ext PRIVATE amulet_test1 )

install(TARGETS amulet_test1 DESTINATION "${SRC_INSTALL_DIR}/amulet_test1/bin")
install(TARGETS _ext DESTINATION "${SRC_INSTALL_DIR}/amulet_test1")
