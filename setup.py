from setuptools import setup
import os.path

setupdir = os.path.dirname(__file__)

setup(
    name="OpacityShare",
    version="0.0.1",
    author="Opacity.dev",
    description="A Plugin for students and teachers who are in love with thonny to share in real time their work and code together with a very little data usage",
    long_description="""A Plugin for students and teachers who are in love with thonny to share in real time their work and code together with a very little data usage""",
    url="https://github.com/opacityDev/opacity-share",
#    keywords="IDE education programming tests in documentation",
    classifiers=[
        "Topic :: Problem :: Solving :: Contests",
        "Programming Language :: Python :: 3",
        "License :: GNU Lesser General Public License v3.0",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Education"
        ],
    platforms=["Windows", "macOS", "Linux"],
    python_requires=">=3.7",
    package_data={
        "thonnycontrib" : ["*.py"],
        "thonnycontrib.oc": ["*.py"], 
        "thonnycontrib.oc.pages":["*.py","*/*.*"],
        "thonnycontrib.oc.lib":["*.py"],
    },
    install_requires=["thonny>=3.2.1","pygubu"],

    packages=["thonnycontrib","thonnycontrib.oc", "thonnycontrib.oc.pages", "thonnycontrib.oc.lib" ],
)
