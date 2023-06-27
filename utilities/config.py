"""
Method: Returns a string to create the fx_config.yml file
"""


def create_yaml_file():
    string = """
  site-name: "fletxible."
  
  repo-url: "https://github.com/LineIndent/fletxible"
  repo-name: "LineIndent/fletxible"
  
  theme:
    - bgcolor: "teal700"
    - primary: "teal700"
    
  navigation:
    - Home: "index.py"
    - About: "about.py"
  """

    return string
