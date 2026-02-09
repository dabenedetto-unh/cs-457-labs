## Getting started

* Create a folder called CS_457
* Open this folder in VSCode:
    * ```File -> Open Folder```

## Directory structure

Directory structure:

```
* CS_457/                   <-- root directory
    * labs/
        * lab02_python/
            * lab02.py
            * test_lab02.py
            * __init__.py
        * __init__.py       <-- empty file for test discovery
```

## Setting up testing in IDE

Open a python file in VS Code.

Click the lab flask icon in the left panel.
* Select "unittest"
* Select root directory "."
* Select "test_*"

This will create a file 

* CS_457/.vscode/settings.json

## Settings.json

Open the file and add a few lines, so it looks like this:

```
{
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        ".",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.unittestEnabled": true,
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}"
    },
    "python-envs.defaultEnvManager": "ms-python.python:system",
    "python-envs.pythonProjects": []
}
```

## Importing code in a test

In test_lab02_python.py, add this:

```
from labs.lab02_python.lab02 import *
```

Now try:

* with the test file open, run the test by clicking the play button (upper-right)
* with the testing panel open, run the test by clicking the play button.

