from setuptools import find_packages, setup

setup(
    name="Fletxible",
    version="0.7.0",
    author="S. Ahmad P. Hakimi",
    author_email="pourhakimi@pm.me",
    description="Web Boilerplate for Flet Library",
    long_description="Fletxible is a Python web boilerplate project designed to provide a solid foundation for building web applications with Python and Flet. The project comes pre-configured with a range of tools and features to make it easy for developers to get started building their applications, without the need to spend time setting up infrastructure or configuring tools.",  # noqa: E501
    long_description_content_type="text/markdown",
    url="https://github.com/LineIndent/fletxible",
    packages=find_packages("fletxible"),
    package_dir={"": "fletxible"},
    install_requires=[
        "click>=8.1.3",
        "flet>=0.9.0",
        "beautifulsoup4>=4.12.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "fx-init=scripts.create:create",
        ],
    },
    keywords=["python web template", "web application", "theme"],
)
