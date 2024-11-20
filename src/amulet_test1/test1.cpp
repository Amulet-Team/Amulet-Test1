#include <iostream>
#include "test1.hpp"

namespace Amulet {
    AMULET_TEST1_DLLX void test1_1(std::string s){
        std::cout << s << std::endl;
        std::cout << "test1_1abcdefghijk" << std::endl;
    }
    AMULET_TEST1_DLLX void test1_2(const std::string& s){
        std::cout << s << std::endl;
        std::cout << "test1_2abcdefghijk" << std::endl;
    }
}
