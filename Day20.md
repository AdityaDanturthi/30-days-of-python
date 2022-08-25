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

# Reading from a URL

```sh
pip install requests
```

#### Will use the following methods from the *requests* module:
- _get()_: to open a network and fetch data from url (returns a response object)
- _status_code_: After fetching the data, we can check the status of the operation (success or error)
- _headers_: To check the header types
- _text_: To extract text from the fetched response object
- _json_: To extract json data. Let's read the text file from  https://www.w3.org/TR/PNG/iso_8859-1.txt

