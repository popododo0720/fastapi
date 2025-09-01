from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir
import pybind11
from setuptools import setup, Extension

ext_modules = [
    Pybind11Extension(
        "hello_cpp",
        [
            "hello.cc",
        ],
        cxx_std=20,
    ),
]

setup(
    name="hello_cpp",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
)