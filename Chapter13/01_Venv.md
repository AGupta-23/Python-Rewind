## Virtual Environment in Python

A **Virtual Environment** is an isolated Python environment used to keep project dependencies separate from other projects and the system Python installation.

It helps:

* Avoid package version conflicts
* Keep projects independent
* Install libraries only for a specific project
* Make projects easier to share and deploy

Example:
One project may use:

* NumPy 1.24

Another project may use:

* NumPy 2.0

Virtual environments allow both to work separately without conflicts.

---

## Creating a Virtual Environment

Command:

```bash
python -m venv myenv
```

Explanation:

* `python -m venv` → uses Python’s built-in virtual environment module
* `myenv` → name of the virtual environment folder

This creates a separate environment inside the `myenv` folder.

---

## Activating Virtual Environment

### Windows

```bash
myenv\Scripts\activate
```

### Mac/Linux

```bash
source myenv/bin/activate
```

After activation:

* The environment name appears in the terminal
* Packages installed using `pip` are installed only inside that environment

---

## Deactivating Virtual Environment

Command:

```bash
deactivate
```

This exits the virtual environment and returns to the system Python environment.

---

## pip freeze

`pip freeze` is used to display all installed Python packages and their versions in the current environment.

Command:

```bash
pip freeze
```

Example Output:

```bash
numpy==2.0.1
pandas==2.2.2
matplotlib==3.9.0
```

Uses:

* Check installed packages
* Save dependencies for sharing projects
* Recreate the same environment later

---

## requirements.txt

A `requirements.txt` file stores all project dependencies and package versions.

It helps other users install the exact same libraries needed for the project.

### Create requirements.txt

```bash
pip freeze > requirements.txt
```

This saves all installed packages into the file.

---

### Install from requirements.txt

```bash
pip install -r requirements.txt
```

Explanation:

* `-r` means read from file
* Installs all packages listed in `requirements.txt`

Used in:

* Team projects
* Deployment
* Sharing projects on GitHub
* Recreating environments on another computer
