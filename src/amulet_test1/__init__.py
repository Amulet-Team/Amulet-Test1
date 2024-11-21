__version__ = '2.0.0'

def _init() -> None:
    import os
    import sys

    path = os.path.join(os.path.dirname(__file__), "bin")
    if sys.platform == "win32":
        os.add_dll_directory(path)
    elif sys.platform == "darwin":
        os.environ["DYLD_LIBRARY_PATH"] = (
                os.environ.get("DYLD_LIBRARY_PATH", "") + os.pathsep + path
        )
    else:
        os.environ["LD_LIBRARY_PATH"] = (
                os.environ.get("LD_LIBRARY_PATH", "") + os.pathsep + path
        )

    from ._amulet_test1 import init
    init(sys.modules[__name__])

_init()
