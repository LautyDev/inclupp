from setuptools import setup

setup(
    name="inclupp",
    version="1.0.0",
    description="A CLI tool to preprocess and compile C++ files with remote #includes.",
    author="LautyDev",
    author_email="git@lauty.dev",
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
