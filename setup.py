from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="inclupp",
    version="1.0.1",
    description="A CLI tool to preprocess and compile C++ files with remote #includes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="LautyDev",
    author_email="git@lauty.dev",
    url="https://github.com/LautyDev/inclupp",
    project_urls={
        "Bug Tracker": "https://github.com/LautyDev/inclupp/issues",
        "Source": "https://github.com/LautyDev/inclupp",
        "Documentation": "https://github.com/LautyDev/inclupp#readme",
    },
    packages=["inclupp"],
    install_requires=[
        "requests",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "inclupp=inclupp.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
