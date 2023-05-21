import os, importlib.util
import yaml
import pickle
import flet as ft

from utilities import (
    route_string_method,
    set_app_route_method,
    set_app_default_pages,
    navigation_example_method,
)

#
route_keys: dict = {}


def open_yaml_script() -> dict:
    # Load the YAML file
    with open("flet_config.yml", "r") as file:
        docs = yaml.safe_load(file)

    return docs


def check_pages_directory_script():
    # Check if "pages" directory exists
    pages_dir = None
    for root, dirs, files in os.walk("."):
        if "pages" in dirs:
            pages_dir = os.path.join(root, "pages")
            break

    if not pages_dir:
        # Create "pages" directory in the root folder
        pages_dir = os.path.join(os.getcwd(), "pages")
        os.mkdir(pages_dir)


def update_pages_directory_script(docs: dict):
    # Loop over files in the pages directory and delete any files that are not listed in the nav
    for file in os.listdir("pages"):
        if file.endswith(".py"):
            found = False
            for page in docs["nav"]:
                if page.get(next(iter(page))) == file:
                    found = True
                    break
            if not found:
                os.remove(os.path.join("pages", file))


def handle_navigation_routing_script(docs: dict):
    # 1. Loop over the navigation tree items
    # 2. handle the file write method
    with open("./logic/temp_route.txt", "w") as f:
        for page in docs["nav"]:
            for key in page:
                route = os.path.splitext(page[key])[0]
                f.write(f"{route_string_method(route)}")


def set_application_routing_script(docs: dict):
    # Get the pre-defined content of the route.py file
    method = set_app_route_method()

    # 1. Read the contents from the generated 'temp_route.txt' file
    with open("./logic/temp_route.txt", "r") as r:
        string = r.read()

    # 2. Create/update the 'route.py' file
    with open("./logic/route.py", "w") as f:
        f.write(method % string)

    # 4. Remove the temp_route.txt file to avoid cluttering
    os.remove("./logic/temp_route.txt")


def set_default_methods_script(docs: dict):
    # Loop over the nav list and create/update files
    # 1. Temp. list to store the filepaths in + the modules dict
    file_list: list = []

    # 2. Loop through navigation tree and append the file_list with the filepaths
    for page in docs["nav"]:
        for key in page:
            filename = f"{page[key]}"
            filepath = os.path.join("pages", filename)
            file_list.append(filepath)

        filename = os.path.splitext(filename)[0]

        route_keys["/" + filename] = importlib.util.spec_from_file_location(
            filename, filepath
        )

    # 3. Loop through the file_list and create the corresponding pages
    for filepath in file_list:
        method = set_app_default_pages()
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write(f"{method}")

    # 4. Update/create the route.pickles file for modules setup
    for file in os.listdir("pages"):
        # Set the path of the file to loop over folders and only include files
        path = os.path.join("pages", file)

        # If the path is NOT a folder, continue ...
        if not os.path.isdir(path):
            # Get the list of routes from utilitites
            navigation = navigation_example_method()

            # Open the file and read it's content before seeking index points
            with open(f"./pages/{file}", "r") as f:
                code = f.read()

            # Find the start and end index of the `<start>` and `<end>` marks
            start_idx = code.index("# start #")
            end_idx = code.index("# end #")

            # Write your code to add between the `<start>` and `<end>` marks here
            code_to_add = "\n".join(navigation)

            # Modify the function string by inserting the new code between the start and end index
            modified_string = (
                code[:start_idx] + "# start #\n" + code_to_add + code[end_idx:]
            )

            with open(f"./pages/{file}", "w") as f:
                f.write(modified_string)

        else:
            pass

    # 5. The route.pickle file is a binary file!
    with open("./logic/route.pickle", "wb") as f:
        pickle.dump(route_keys, f)

    # 6. Finally, return the route_keys so we use itin the route.py logic
    return route_keys


def map_yaml(yaml_file_path, output_file_path):
    # 1. open the flet_config.yml file and safe load the data
    with open(yaml_file_path) as f:
        yaml_data = yaml.safe_load(f)

    # 2. Simply write the contents to a variable that will show up in the set location
    # with the set filename: mapped.py
    with open(output_file_path, "w") as f:
        f.write("mapped_data = ")
        f.write(str(yaml_data))


def script(page: ft.Page):
    # Get the YAML file
    try:
        docs = open_yaml_script()

    except FileNotFoundError as e:
        print(e)

    # Next, check if "pages" directory exists
    try:
        check_pages_directory_script()

    except Exception as e:
        print(e)

    # Next, loop over 'pages' for non-existant files/deleted files
    try:
        update_pages_directory_script(docs)

    except Exception as e:
        print(e)

    # Next, we either create new routes if not already created,
    # or update the routes to reflext the navigation tree in the .yml file
    try:
        handle_navigation_routing_script(docs)

    except Exception as e:
        print(e)

    # Next, we create/update the route.py file,
    # which contains the application routing logic
    try:
        # Make sure to create a function that returns a list of the modules for routing!!!
        set_application_routing_script(docs)

    except Exception as e:
        print(e)

    # Next, we have to handle the page logic, which requires
    # several step. First, adding the default method into each page
    try:
        route_keys: dict = set_default_methods_script(docs)

        for keys, __ in route_keys.items():
            page.views.append(route_keys[keys].loader.load_module().View())

        # Set's the index.py page as the first page.
        index = -1
        current = 1
        page.views[index], page.views[current] = page.views[current], page.views[index]
        page.update()

    except Exception as e:
        print(e)

    # Map out the .yml file into a python dict
    try:
        map_yaml("flet_config.yml", "./logic/mapped.py")

    except Exception as e:
        print(e)
