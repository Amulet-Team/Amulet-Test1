#ifndef AMULET_TEST1_DLLX
    #ifdef _WIN32
        #ifdef ExportAmuletTest1
            #define AMULET_TEST1_DLLX __declspec(dllexport)
        #else
            #define AMULET_TEST1_DLLX __declspec(dllimport)
        #endif
    #else
        #define AMULET_TEST1_DLLX
    #endif
#endif
