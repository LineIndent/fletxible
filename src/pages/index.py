import flet as ft
from core.base import FxBaseView
import fx_material as fx

intro = """
Fletxible is a Python web boilerplate project designed to provide a solid foundation for building web applications with Python and Flet. The project comes pre-configured with a range of tools and features to make it easy for developers to get started building their applications, without the need to spend time setting up infrastructure or configuring tools.
"""

pip = """
Fletxible is published as a Python package and can be installed with pip, ideally by using a virtual environment. Open up a terminal and install Fletxible using the following command:
"""

pip_command = """```python
pip3 install Fletxible
```
"""

pip_outro = """
This will automatically install compatible versions of all dependencies including Flet.
"""

app_intro = """
After installing Fletxible, you can test if it's working properly by running the following command:
"""

app_command = """
```python
fletxible-init
```
"""

app_outro = """
If the package was installed correctly, you should see the following directories:
    - core              
    - components
    - utilities 

As well as the following files:
    - main.py
    - script.py
    - base.py
    - fx_tempalte.py
    - fx_config.yml
"""

script = """
First, open up your fx_config.yml file and make sure the following are present:
"""

config = """```yaml
site-name: "fletxible."
repo-url: "https://github.com/LineIndent/fletxible"

theme:
  - bgcolor: "teal"

navigation:
  - Home: "index.py"
  - About: "about.py
```
"""

change_config = """
You can replace the default configuration with your own data. The navigation header will generate files with names correpsonding to the python file. 
"""

script_two = """
When you're set with your config file (fx_config.yml), navigate to your terminal and run the following command to generate your files inside a directory called web:
"""

script_cmd = """```python
python3 script.py
```
"""

conclusion = """
That's it! You now have your pages set up along with the necessary routing and layout. 
You can open the web directory and start creating your pages immediately!
"""


class FxView(FxBaseView):
    def __init__(
        self,
        page: ft.Page,
        docs: dict,
        route="/index",
    ):
        self.components = self.fx_controls()
        self.nav_rail = self.fx_rail()

        super().__init__(
            page=page,
            docs=docs,
            components=self.components,
            nav_rail=self.nav_rail,
            route=route,
        )

    def fx_rail(self) -> list[list]:
        return [
            [1, "Installation"],
            [2, "Application Setup"],
            [3, "Configuration"],
        ]

    def fx_controls(self) -> list:
        return [
            ft.Divider(height=35, color="transparent"),
            ft.Divider(height=25, color="transparent"),
            # start your layout design here ...
            fx.heading("Getting Started - INDEX PAGE"),
            fx.paragraph(intro),
            fx.subtitle("Installation"),
            ft.Divider(height=5, color="transparent"),
            fx.subtitle("with PIP", key=1),
            fx.paragraph(pip),
            fx.CodeBlock(pip_command),
            fx.paragraph(pip_outro),
            fx.subtitle("Application Setup", key=2),
            fx.paragraph(app_intro),
            fx.CodeBlock(app_command),
            fx.paragraph(app_outro),
            fx.subtitle("Configure YAML File", key=3),
            fx.paragraph(script),
            fx.CodeBlock(config),
            fx.paragraph(change_config),
            fx.paragraph(script_two),
            fx.CodeBlock(script_cmd),
            fx.paragraph(conclusion),
            # end your layout design here ...
            ft.Divider(height=15, color="transparent"),
        ]
