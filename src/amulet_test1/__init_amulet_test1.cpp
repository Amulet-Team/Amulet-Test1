#include <amulet_test1/test1.hpp>

#include <pybind11/pybind11.h>
namespace py = pybind11;

static void init_module(py::module m){
    m.def("test1_1", &Amulet::test1_1);
    m.def("test1_2", &Amulet::test1_2);
}

PYBIND11_MODULE(_amulet_test1, m) {
    m.def("init", &init_module);
}
