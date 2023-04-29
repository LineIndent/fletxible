from setuptools import setup

setup(
    name="flet-web-template",
    version="0.1.0",
    author="S. Ahmad P. Hakimi",
    author_email="pourhakimi@pm.me",
    description="Web Boilerplate for Flet Library",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/LineIndent/flet_boilerplate",
    packages=["flet_template", "command"],
    install_requires=["click==8.1.3", "flet==0.5.2"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "flet_material_init=flet_material.command.new_project:init_code"
        ],
    },
    keywords=["python web templates", "web application", "development"],
)
