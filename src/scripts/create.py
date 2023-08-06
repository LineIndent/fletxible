import os
from pathlib import Path
import subprocess
import click


file_structure = {
    "core": [
        "__init__.py",
        "base.py",
        "drawer.py",
        "header.py",
        "left_panel.py",
        "middle_panel.py",
        "mobile_drop_down.py",
        "mobile_navigation.py",
        "navigation.py",
        "repo_data.py",
        "right_panel.py",
    ],
    "fx_material": ["__init__.py", "annotation.py", "block.py", "typography.py"],
    "scripts": ["__init__.py", "create.py", "build.py"],
    "utilities": [
        "__init__.py",
        "fx_cli.py",
        "fx_config.py",
        "fx_error.py",
        "fx_scratch.py",
        "fx_sub_router.py",
        "fx_sub_template.py",
        "fx_template.py",
    ],
    "config.py": None,
    "main.py": None,
}


def create_src_directory():
    for __ in os.listdir("."):
        if not os.path.exists("./" + "src"):
            os.makedirs("src")
        else:
            continue


def create_src_file_structure():
    source = Path(__file__).parent.parent
    dublicate = Path("./src")
    fx_file_src = Path(source, "utilities")

    def create_dir_file_structure(dir_path: str, key: str, file: str):
        source_path = os.path.join(source, key, file)
        dublicate_path = os.path.join(dir_path, file)

        with open(source_path, "r") as src_file, open(dublicate_path, "w") as dst_file:
            dst_file.write(src_file.read())

    for key, value in file_structure.items():
        if value is not None:
            dir_path = os.path.join(dublicate, key)
            os.mkdir(dir_path)
            if isinstance(value, list):
                for file in value:
                    create_dir_file_structure(dir_path, key, file)
        else:
            source_path = os.path.join(fx_file_src, "fx_" + key)
            dublicate_path = os.path.join(dublicate, key)
            with open(source_path, "r") as src_file, open(
                dublicate_path, "w"
            ) as dst_file:
                dst_file.write(src_file.read())


@click.command()
def create():
    click.echo("Creating source directory...")
    create_src_directory()
    create_src_file_structure()
    click.echo("Source directory created successfully.")

    os.chdir("src")

    click.echo("Running build scripts...")
    if os.path.basename(os.getcwd()) == "src":
        # Run twine upload *
        subprocess.run(
            ["python3", "scripts/build.py"], capture_output=True, text=True, bufsize=0
        )
    click.echo("Build ran successfully.")


@click.group()
def flexible():
    pass


flexible.add_command(create)

if __name__ == "__main__":
    flexible()
