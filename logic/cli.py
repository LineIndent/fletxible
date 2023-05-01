import click
import os
from utilities import set_up_yaml_file


@click.command()
def init():
    # First, create the flet_config.yml file
    with open("flet_config.yml", "w") as f:
        string = set_up_yaml_file()
        f.write(string)

    # Create templates directory if it doesn't exist
    if not os.path.exists("logic"):
        os.makedirs("logic")

    # Define the list of files to be generated
    file_list = ["__init__.py", "main.py", "script.py", "utilities.py"]

    # Generate each file in the templates directory
    for file_name in file_list:
        file_path = os.path.join("logic", file_name)
        open(file_path, "a").close()

        # If it's the __init__.py file, write the import statements
        if file_name == "__init__.py":
            with open("./logic/main.py", "r") as j:
                init_thread = j.read()

            with open(file_path, "w") as f:
                f.write(init_thread)

        # If it's the main.py file, write the main statements
        if file_name == "main.py":
            with open("./logic/main.py", "r") as j:
                main_thread = j.read()

            with open(file_path, "w") as f:
                f.write(main_thread)

        # If it's the script.py file, write the main statements
        if file_name == "script.py":
            with open("./logic/script.py", "r") as j:
                script_thread = j.read()

            with open(file_path, "w") as f:
                f.write(script_thread)

        # If it's the utilities.py file, write the main statements
        if file_name == "utilities.py":
            with open("./logic/utilities.py", "r") as j:
                utilities_thread = j.read()

            with open(file_path, "w") as f:
                f.write(utilities_thread)

    click.echo(f"Generated {len(file_list)} files in the 'templates' directory.")
    click.echo(f"Get started by changing the fletDocs.yml file!")


@click.group()
def flet_template():
    pass


flet_template.add_command(init)

if __name__ == "__main__":
    flet_template()
