from setuptools import setup

setup(
    name="Fletxible",
    version="0.5.3",
    author="S. Ahmad P. Hakimi",
    author_email="pourhakimi@pm.me",
    description="Web Boilerplate for Flet Library",
    long_description="Fletxible is a Python web boilerplate project designed to provide a solid foundation for building web applications with Python and Flet. The project comes pre-configured with a range of tools and features to make it easy for developers to get started building their applications, without the need to spend time setting up infrastructure or configuring tools.",
    long_description_content_type="text/markdown",
    url="https://github.com/LineIndent/fletxible",
    packages=["logic"],
    install_requires=["click>=8.1.3", "flet>=0.7.1", "PyYAML>=6.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "fletxible-init=logic.cli:init",
            "fletxible-build=logic.build:build",
        ],
    },
    keywords=["python web template", "web application", "development"],
)
