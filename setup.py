from setuptools import setup, find_packages

setup(
    name="bootstrapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",  # For CLI
    ],
    entry_points={
        "console_scripts": [
            "bootstrapper=bootstrapper.cli:main",
        ],
    },
)
