import click
import os
from utilities.config import create_yaml_file
from pathlib import Path
import subprocess


@click.command()
def init():
    main: list = []

    code = create_yaml_file()
    with open("fx_config.yml", "w") as f:
        f.write(code)

    root: list = ["main.py", "script.py", "base.py", "fx_template.py"]

    index = 0
    for file_name in root:
        file_path = Path(".") / file_name
        file_path.touch()

        source_path = Path(".") / root[index]
        with open(source_path, "r") as source_file:
            source_contents = source_file.read()

        with open(file_path, "w") as new_file:
            new_file.write(source_contents)

        main.append(file_name)
        index += 1

    paths: list = ["components", "core", "utilities"]
    for path in paths:
        Path(path).mkdir(exist_ok=True)

    dirs: list = ["components", "core", "utilities"]

    index = 0
    for dir in dirs:
        file_names: list = []
        for file in os.listdir(dir):
            if file.endswith(".py"):
                main.append(file)
                file_names.append(file)

        for file_name in file_names:
            file_path = Path(paths[index]) / file_name
            file_path.touch()

            source_path = Path(dirs[index]) / file_name
            with open(source_path, "r") as source_file:
                source_contents = source_file.read()

            with open(file_path, "w") as new_file:
                new_file.write(source_contents)

        index += 1

    click.echo()
    click.echo(f"Generated {len(root) + 1} files in the 'logic' directory:")
    for files in main:
        click.echo(f"● {files}")
    click.echo("Status: OK")
    click.echo()
    click.echo("Running script file ...")
    subprocess.run("python3", "script.py", capture_output=True, text=True)
    click.echo("Status: OK")


@click.group()
def flet_template():
    pass


flet_template.add_command(init)

if __name__ == "__main__":
    flet_template()
