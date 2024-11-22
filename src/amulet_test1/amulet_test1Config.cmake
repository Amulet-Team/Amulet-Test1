if (NOT TARGET amulet_test1)
    message(STATUS "Finding amulet_test1")

    set(amulet_test1_INCLUDE_DIR "${CMAKE_CURRENT_LIST_DIR}/..")
    find_library(amulet_test1_LIBRARY NAMES amulet_test1 PATHS "${CMAKE_CURRENT_LIST_DIR}/bin")
    message(STATUS "amulet_test1_LIBRARY: ${amulet_test1_LIBRARY}")

    add_library(amulet_test1 SHARED IMPORTED)
    set_target_properties(amulet_test1 PROPERTIES
        INTERFACE_INCLUDE_DIRECTORIES "${amulet_test1_INCLUDE_DIR}"
        IMPORTED_IMPLIB "${amulet_test1_LIBRARY}"
    )
endif()
