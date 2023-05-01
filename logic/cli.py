import click
import os
from logic.utilities import set_up_yaml_file
from pathlib import Path


@click.command()
def init():
    # First, create the flet_config.yml file
    with open("flet_config.yml", "w") as f:
        string = set_up_yaml_file()
        f.write(string)

    # Create 'logic' directory if it doesn't exist
    Path("logic").mkdir(exist_ok=True)

    # Define the list of files to be generated
    file_list = ["__init__.py", "main.py", "script.py", "utilities.py"]

    # Generate each file in the templates directory
    for file_name in file_list:
        file_path = Path("logic") / file_name
        file_path.touch()

        # Read the contents of the source file
        source_path = Path(__file__).parent / file_name
        with open(source_path, "r") as source_file:
            source_contents = source_file.read()

        # Write the contents to the new file
        with open(file_path, "w") as new_file:
            new_file.write(source_contents)

    click.echo()
    click.echo(f"Generated {len(file_list)} files in the 'logic' directory:")
    for files in file_list:
        click.echo(f"● {files}")
    click.echo()


@click.group()
def flet_template():
    pass


flet_template.add_command(init)

if __name__ == "__main__":
    flet_template()
