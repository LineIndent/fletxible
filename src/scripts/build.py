import os
import shutil


def check_if_pages_directory_exists() -> None:
    pages_directory = None
    for root, dirs, __ in os.walk("."):
        if "pages" in dirs:
            pages_directory = os.path.join(root, "pages")
            break

        if not pages_directory:
            pages_directory = os.path.join(os.getcwd(), "pages")
            os.mkdir(pages_directory)


def get_list_of_pages_from_directory() -> list:
    pages_list = set()
    dirs_list: list = []

    def loop_over_sub_folders(path: str):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if item == "__pycache__":
                continue
            if os.path.isfile(item_path) and item_path.endswith(".py"):
                pages_list.add(item_path)
            elif os.path.isdir(item_path):
                dirs_list.append(item_path)
                loop_over_sub_folders(item_path)

    for root, folders, files in os.walk("pages"):
        for folder in folders:
            path = os.path.join(root, folder)
            dirs_list.append(path)
            loop_over_sub_folders(path)

        for file in files:
            item_path = os.path.join(root, file)
            if os.path.isfile(item_path) and item_path.endswith(".py"):
                pages_list.add(item_path)

    return dirs_list, pages_list


def get_list_of_pages_from_config_file(docs: dict, parent_path: str = "pages"):
    pages_list: list = []
    dirs_list: list = []

    def loop_over_nested_dict(docs: dict, current_path: str):
        if docs.get("navigation") is not None:
            docs = docs.get("navigation").items()
        else:
            docs = docs.items()

        for key, value in docs:
            new_path = os.path.join(current_path, key)
            if isinstance(value, dict):
                dirs_list.append(new_path)
                loop_over_nested_dict(value, new_path)
            else:
                file_path = new_path + ".py"
                pages_list.append(file_path)

    loop_over_nested_dict(docs, parent_path)

    return dirs_list, pages_list


def synchronize_directories(docs: dict):
    pages_dirs, pages_files = get_list_of_pages_from_directory()
    dict_dirs, dict_files = get_list_of_pages_from_config_file(docs)

    for pages_dir in pages_dirs:
        try:
            if pages_dir not in dict_dirs:
                shutil.rmtree(pages_dir)
        except:  # noqa: E722
            pass

    for dict_dir in dict_dirs:
        if not os.path.exists(dict_dir):
            os.makedirs(dict_dir)

    for file_path in pages_files:
        try:
            if file_path not in dict_files and file_path == "pages/_error":
                os.remove(file_path)
        except:  # noqa: E722
            pass

    with open("utilities/fx_template.py", "r") as file:
        view = file.read()

    with open("utilities/fx_sub_template.py", "r") as file:
        sub_view = file.read()

    for file in dict_files:
        if not os.path.exists(file):
            file_length = len(file.split("/"))
            with open(file, "w") as file:
                if file_length >= 3:
                    file.write(sub_view)
                else:
                    file.write(view)


def set_sub_directory_router_file():
    with open("utilities/fx_error.py", "r") as file:
        error = file.read()

    error_path = os.path.join("pages" + "/_error.py")
    if not os.path.exists(error_path):
        with open(error_path, "w") as file:
            file.write(error)

    with open("utilities/fx_sub_router.py", "r") as file:
        router = file.read()

    for root, dirs, __ in os.walk("pages"):
        for dir in dirs:
            router_path = os.path.join(root + "/" + dir + "/" + "router.py")
            if not os.path.exists(router_path):
                with open(router_path, "w") as file:
                    file.write(router)


# NOT USED #
def create_navigation_links_from_keys():
    nav_list: list = []

    __, list_of_pages = get_list_of_pages_from_directory()

    for file in list_of_pages:
        filename = file.split("pages", 1)[1].split(".")[0]
        title = file.split("/")[-1].split(".")[0]
        if filename == "/_error":
            continue
        nav_list.append(f"self.route('{title.capitalize()}', '{filename}'),")

    with open("core/navigation.py", "r") as file:
        data = file.read()

    start_index = data.index("# start #")
    stop_index = data.index("# end #")

    new_nav_list = "\n".join(nav_list)

    new_data = (
        data[:start_index] + "# start #\n" + new_nav_list + "\n" + data[stop_index:]
    )

    with open("core/navigation.py", "w") as file:
        file.write(new_data)


def build(docs: dict):
    check_if_pages_directory_exists()
    synchronize_directories(docs)
    set_sub_directory_router_file()


if __name__ == "__main__":
    import sys

    sys.path.append("../")
    from src.config import config

    build(config)
