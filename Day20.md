- Contents
    - [PIP version](#pip-version)
    - [Web browser module](#web-browser-module)
    - [Uninstalling packages](#uninstalling-packages)
    - [List of packages](#list-of-packages)
    - [Package information](#package-information)
        - [Detailed package information](#for-even-more-detailed-information)
    - [PIP freeze](#pip-freeze)    



## Python PIP - Python Package Manager

### PIP version

```sh
pip --version
```

```sh
pip 22.2
```

### Web browser module

```py
import webbrowser # Web browser module to open websites

url = 'https://ca.linkedin.com/in/adityadanturthi'
webbrowser.open_new_tab(url)
```

### Uninstalling packages

```sh
pip uninstall packagename
```
### List of packages

```sh
pip list
```
#### Package information

```sh
pip show packagename
```

### For even more detailed information

```sh
pip show --verbose packagename
```

### PIP freeze
#### List of all packages installed along with their version to use in requirements.txt

```sh
matplotlib==3.5.2
numpy==1.22.2
scikit-learn==1.0.2
```

