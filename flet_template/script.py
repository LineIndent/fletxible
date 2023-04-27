import os
import yaml


def run_temlate_script():
    # Load the YAML file
    with open("fletDocs.yml", "r") as file:
        fletDocs = yaml.safe_load(file)

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

    # Loop over the nav list and create/update files
    for page in fletDocs["nav"]:
        for key in page:
            filename = f"{page[key]}"
            filepath = os.path.join("pages", filename)

            if not os.path.exists(filepath):
                with open(filepath, "w") as f:
                    f.write(f"This is the {page} page")


run_temlate_script()
