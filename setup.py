from setuptools import setup
import os.path

setupdir = os.path.dirname(__file__)

setup(
    name="OpacityContests",
    version="2.0.6",
    author="Opacity.dev",
    description="A plugin for opacity contests who are in love with thonny",
    long_description="""A plugin for opacity contests who are in love with thonny""",
    url="https://github.com/opacityDev/opacity-contest-thonny-plugin",
#    keywords="IDE education programming tests in documentation",
    classifiers=[
        "Topic :: Problem :: Solving :: Contests",
        "Programming Language :: Python :: 3",
        "License :: Creative Commons Legal Code",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education"
        ],
    platforms=["Windows", "macOS", "Linux"],
    python_requires=">=3.7",
    package_data={
        "thonnycontrib.oc": ["*.py"], 
        "thonnycontrib.oc.pages":["*.py","*/*.*"],
        "thonnycontrib.oc.lib":["*.py"],
    },
    install_requires=["thonny>=3.2.1"],

    packages=["thonnycontrib.oc", "thonnycontrib.oc.pages", "thonnycontrib.oc.lib" ],
)
