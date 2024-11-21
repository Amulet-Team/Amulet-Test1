import os
import subprocess
import sys
from pathlib import Path
import pybind11

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


# https://github.com/pybind/cmake_example/blob/master/setup.py
class CMakeExtension(Extension):
    def __init__(self, name: str, sourcedir: str = "") -> None:
        super().__init__(name, sources=[])
        self.sourcedir = os.fspath(Path(sourcedir).resolve())


class CMakeBuild(build_ext):
    def build_extension(self, ext):
        ext_fullpath = Path.cwd() / self.get_ext_fullpath("")
        src_dir = ext_fullpath.parent.resolve()

        subprocess.run([
            "cmake",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-Dpybind11_DIR={pybind11.get_cmake_dir().replace(os.sep, '/')}",
            f"-DCMAKE_INSTALL_PREFIX=install",
            f'-DSRC_INSTALL_DIR={src_dir}',
            '-B', 'build',
        ])
        subprocess.run(["cmake", "--build", "build", "--config", "Release"])
        subprocess.run(["cmake", "--install", "build", "--config", "Release"])


setup(
    cmdclass={"build_ext": CMakeBuild},
    ext_modules=[CMakeExtension("amulet_test1._amulet_test1")],
)
