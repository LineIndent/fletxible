import subprocess
import click
import os
from utilities.config import create_yaml_file
from pathlib import Path


@click.command()
def init():
    main: list = []
    source = Path(__file__).parent.parent

    code = create_yaml_file()
    with open("fx_config.yml", "w") as f:
        f.write(code)

    root: list = ["main.py", "script.py", "base.py", "fx_template.py"]

    pos = 0
    for file_name in root:
        file_path = Path(".") / file_name
        file_path.touch()

        source_path = source / "fletxible" / root[pos]
        with open(source_path, "r") as source_file:
            source_contents = source_file.read()

        with open(file_path, "w") as new_file:
            new_file.write(source_contents)

        main.append(file_name)
        pos += 1

    paths: list = ["components", "core", "utilities"]
    for path in paths:
        Path(path).mkdir(exist_ok=True)

    dirs: list = ["components", "core", "utilities"]

    index = 0
    for dir in dirs:
        file_names: list = []
        path = os.path.join(source, dir)
        for file in os.listdir(path):
            if file.endswith(".py"):
                main.append(file)
                file_names.append(file)

        for file_name in file_names:
            file_path = Path(dir) / file_name
            file_path.touch()

            source_path = source / dir / file_name
            with open(source_path, "r") as source_file:
                source_contents = source_file.read()

            with open(file_path, "w") as new_file:
                new_file.write(source_contents)

        index += 1

    click.echo()
    click.echo(f"Generated {len(main) + 1} files in the 'root' directory:")
    click.echo("Status: OK")
    click.echo()

    click.echo("Running script file ...")
    subprocess.run(["python3", "script.py"], capture_output=True, text=True, bufsize=0)
    subprocess.run(["python3", "main.py"], capture_output=True, text=True, bufsize=0)
    click.echo("Status: OK")


@click.group()
def flet_template():
    pass


flet_template.add_command(init)

if __name__ == "__main__":
    flet_template()
