"""
Method: Returns a string to create the fx_config.yml file
"""


def create_yaml_file():
    string = """
  navigation:
    - Home: "index.py"
    - About: "about.py"
  """

    return string
