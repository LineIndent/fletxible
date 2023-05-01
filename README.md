
<div align="center>

<span style="font-size:51px; font-family:League Spartan; font-weight:800; letter-spacing:0.025rem;">fletxible.</span>

<p align="center">

[![Build Status](https://github.com/LineIndent/fletxible/actions/workflows/build.yml/badge.svg)](https://github.com/LineIndent/fletxible/actions/workflows/build.yml)


[![Documentation](https://readthedocs.org/projects/fletxible/badge/?version=latest)](https://fletxible.readthedocs.io/en/latest/?badge=latest)


[![Python version](https://img.shields.io/pypi/pyversions/fletxible.svg)](https://pypi.org/project/fletxible/)


[![PyPI version](https://img.shields.io/pypi/v/Fletxible.svg)](https://pypi.org/project/Fletxible)

[![PyPI downloads](https://img.shields.io/pypi/dm/Fletxible.svg)](https://pypi.org/project/Fletxible/)

</p>

</div>


<p align="center">
Fletxible is a Python web boilerplate project designed to provide a solid foundation for building web applications with Python and Flet. The project comes pre-configured with a range of tools and features to make it easy for developers to get started building their applications, without the need to spend time setting up infrastructure or configuring tools.</p>



## 1. Installation

To use Flet Material, you need to have the following installed:

-   Latest version of Flet
-   Python 3.5+

If you don't have Flet installed, installing Flexible automatically installs it for you. You can install Flexible using the following command:
```
$ pip install Fletxible
```



## 2. Application Setup

After installing Fletxible, you can test if it's working properly by running the following command:

```
$ fletxible-init
```

If the package was installed correctly, a directory named ```logic``` along with a file called ```flet_config.yml``` will be generated inside the root directory.

The ```logic``` directory will contain four files:

1. ```__init__.py```
2. ```main.py```
3. ```script.py```
4. ```utilities.py```

<!-- ## 3. Code Breakdown

The script is similar to the basic Flet application setup, with some minor additions.

At the top of the main file, you need to import the Flet Material library and all its components:
```python
import flet_material as fm
```

Below the imported modules is the Theme instance from Flet Material. It sets up the entire application theme so that all colors, primary and accent, are uniform, giving the applications being built a consistent look and feel. For a list of supported theme colors, you can visit the library's documentation online.

For a list of supported theme colors, you can visit the library's documentation online.

```python
fm.Theme.set_theme(theme="teal")
```

Finally, within the main() method, you can use a new control called fm.Buttons(), which inherits its properties from several Flet classes and can be customized to your liking:

```python
button = fm.Buttons(
    width=220,
    height=55,
    title="Give this repo a star!",
)
```

That's it! You now have access to Flet Material library components! -->

## Contributing

Contributions are highly encouraged and welcomed. Check out the [contributon section](https://flet-material.vercel.app/contribute/) of the documentation for more details. 


## License

Flet Material Library is open-source and licensed under the [MIT License](LICENSE).




