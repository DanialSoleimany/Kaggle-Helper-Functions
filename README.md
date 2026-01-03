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

### 3.4 `pytorch_model_downloader(source_path, dest_filename="best.pt")`

This helper function is designed to **properly download PyTorch model files (e.g. `best.pt`) from Kaggle notebooks**.

In Kaggle, files are **only downloadable if they are located inside `/kaggle/working`**.
This function solves that limitation by **copying a trained PyTorch model from any internal path (such as training outputs) into `/kaggle/working`**, and then generating a direct download link.

---

#### Purpose

* Copies a trained PyTorch model (`.pt`) to `/kaggle/working`
* Ensures the file is downloadable from the Kaggle UI
* Generates a clickable download link
* Designed for YOLO and other PyTorch-based workflows

---

#### Usage Example

```python
pytorch_model_downloader(
    "/kaggle/working/results/models/weights/best.pt"
)
```

With a custom output name:

```python
pytorch_model_downloader(
    "/kaggle/working/results/models/weights/best.pt",
    "best.pt"
)
```

---

#### Important Kaggle Note

Kaggle **does not allow direct downloads** from arbitrary internal paths such as:

```
/kaggle/working/results/model_v42/weights/
```

To make a PyTorch model downloadable, it **must first be copied or moved to `/kaggle/working`**.
This function performs that copy automatically and exposes the file via a download link.

---

#### Cleanup After Download (Recommended)

After successfully downloading the model, you may want to remove it from the working directory to keep the environment clean.

This can be done using the `remove` helper function:

```python
remove("/kaggle/working/best.pt")
```

This will safely delete the copied model file **after** it has been downloaded.

---

#### Workflow

1. Train the PyTorch / YOLO model
2. Copy the model to `/kaggle/working` using `pytorch_model_downloader`
3. Download the model from Kaggle
4. Remove the file using `remove` to clean up

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
