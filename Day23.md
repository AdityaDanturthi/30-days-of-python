## Virtual Environments

### Setting up a virtual environment
```sh
pip install virtualenv
```

### For windows
```sh
python -m venv venv
```

### Checking if venv was created
```sh
ls
```

### Activation of the virtual environment in windows
```sh
venv\Scripts\activate
```

### After activation the name of the virtual environment will appear before the folder path:
```sh
(venv) folder path
```

### install the package in the 
```sh
(venv) folder path> pip install flask
```

### PIP freeze to check the packages installed
```sh
(venv) folder path> pip freeze
Click==7.0
Flask==1.1.1
Werkzeug==0.16.0
```

### After completing working in the virtual environment, we should deactivate
```sh
(venv) folder path> deactivate
```