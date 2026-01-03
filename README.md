# Kaggle Helper Functions


# Usage Guide

This helper module provides simple and safe file and folder management utilities designed specifically for **Kaggle Notebooks**.

---

## 1. Download `helper.py` in Kaggle

Run the following cell in your Kaggle notebook to download the helper file directly from GitHub:

```python
import urllib.request

url = "https://raw.githubusercontent.com/DanialSoleimany/Kaggle-Helper-Functions/main/helper.py"
urllib.request.urlretrieve(url, "helper.py")
```

---

## 2. Import the Module

After downloading, import the helper module:

```python
import helper
```

---

## 3. Available Functions

### 3.1 `create_folder(path)`

Creates a directory at the given path if it does not already exist.

```python
helper.create_folder("/kaggle/working/test_folder")
```

* Safe to call multiple times
* No error if the folder already exists

---

### 3.2 `remove(path)`

Deletes **either a file or a folder**, depending on the given path.

* If `path` is a **folder**, the folder and **all its contents** are deleted recursively.
* If `path` is a **file**, only that file is deleted.

```python
# Remove a folder
helper.remove("/kaggle/working/test_folder")

# Remove a file
helper.remove("/kaggle/working/data.yaml")
```

⚠️ **Warning:** Folder deletion is recursive and permanent.

---

### 3.3 `rename(old_path, new_path)`

Renames a file or directory from `old_path` to `new_path`.

```python
helper.rename(
    "/kaggle/working/model_old",
    "/kaggle/working/model_new"
)
```

Conditions:

* `old_path` must exist
* `new_path` must not already exist

---

## 4. Typical Kaggle Workflow Example

```python
import helper

helper.create_folder("/kaggle/working/output")
helper.rename(
    "/kaggle/working/output",
    "/kaggle/working/output_v1"
)
helper.remove("/kaggle/working/output_v1")
```

---

## 5. Notes for Kaggle Users

* Use `/kaggle/working` for all writable files
* File changes persist only during the current session
* Restart the kernel if imports behave unexpectedly
* Internet access must be enabled to download from GitHub

---

## 6. Requirements

Uses only Python standard library modules:

* `os`
* `shutil`

No additional dependencies are required.

---

## 7. License

Free to use for Kaggle competitions, research, and personal projects.
