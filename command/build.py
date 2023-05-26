import click
import os
from pathlib import Path


@click.command()
def build():
    # Create 'web' directory if it doesn't exist
    Path("web").mkdir(exist_ok=True)
    click.echo("Creating web directory...")

    # Define the list of files to be generated
    file_list = ["main.py", "styles.py", "controls.py", "route.py"]
    click.echo()

    click.echo("Generating files inside web directory...")
    # Generate each file in the templates directory
    for file_name in file_list:
        file_path = Path("web") / file_name
        file_path.touch()

        # Read the contents of the source file
        source_path = Path(__file__).parent / file_name
        with open(source_path, "r") as source_file:
            source_contents = source_file.read()

        # Write the contents to the new file
        with open(file_path, "w") as new_file:
            new_file.write(source_contents)

    page_list = []

    # Get the user created files from 'pages' dir
    for page in os.listdir("pages"):
        if os.path.isfile(f"pages/{page}"):
            page_list.append(page)

    # Generate each file in the templates directory
    for file_name in page_list:
        file_path = Path("web") / file_name
        file_path.touch()

        source_path = Path(os.getcwd()) / "pages" / file_name
        # Read the contents of the source file
        with open(source_path, "r") as source_file:
            source_contents = source_file.read()

        # Write the contents to the new file
        with open(file_path, "w") as new_file:
            new_file.write(source_contents)

    click.echo()
    click.echo(
        f"Generated {len(file_list) + len(page_list)} files in the 'web' directory:"
    )
    for files in file_list:
        click.echo(f"● {files}")
    for files in page_list:
        click.echo(f"● {files}")

    click.echo("Status: OK")
    click.echo()

    # click.echo("Configuring main.py ...")
    # init_main_method()
    # subprocess.run(["python3", "logic/main.py"], capture_output=True, text=True)
    # click.echo("Status: OK")


@click.group()
def flet_template():
    pass


flet_template.add_command(build)

if __name__ == "__main__":
    flet_template()
