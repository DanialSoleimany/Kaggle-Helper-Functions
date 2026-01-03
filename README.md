# Kaggle Helper Functions

A **lightweight, dependency-free Python utility module** designed specifically for **Kaggle Notebooks**.
It provides safe and convenient helpers for file and folder management, with a strong focus on **making trained PyTorch models easily downloadable**.

Ideal for:

* Organizing experiment outputs
* Renaming and versioning folders
* Cleaning up temporary files
* Downloading trained PyTorch models such as `best.pt` or `last.pt` (YOLO, etc.)

---

## Quick Start

### 1. Download the helper module

Run this cell **once** in your Kaggle notebook:

```python
import urllib.request

url = "https://raw.githubusercontent.com/DanialSoleimany/Kaggle-Helper-Functions/main/helper.py"
urllib.request.urlretrieve(url, "helper.py")
```

---

### 2. Import the module

```python
import helper
```

That’s it — no additional packages or installations required.

---

## Available Functions

### `create_folder(path)`

Safely creates a folder at the given path.

```python
helper.create_folder("/kaggle/working/my_outputs")
```

**Features:**

* Can be called multiple times
* No error if the folder already exists
* Ideal for preparing output directories before training or inference

---

### `remove(path)`

Deletes **either a file or a folder**, depending on the provided path.

```python
# Delete a folder and everything inside it
helper.remove("/kaggle/working/old_experiment")

# Delete a single file
helper.remove("/kaggle/working/temp.yaml")
```

**Behavior:**

* Files are deleted normally
* Folders are deleted recursively (including all contents)

⚠️ **Warning:** Folder deletion is permanent.

---

### `rename(old_path, new_path)`

Renames or moves a file or folder.

```python
helper.rename(
    "/kaggle/working/run1",
    "/kaggle/working/best_run"
)
```

**Rules:**

* `old_path` must exist
* `new_path` must not already exist

Useful for experiment versioning and result organization.

---

### `pytorch_model_downloader(source_path, dest_filename="best.pt")`

Kaggle only allows file downloads from the `/kaggle/working/` directory.
This function solves that limitation by:

* Copying a trained PyTorch `.pt` model from any deep internal path
* Placing it directly inside `/kaggle/working/`
* Generating a **clickable download link** inside the notebook
* Making the file visible in the **Output** tab for manual download

---

#### Usage

```python
# Default output name (best.pt)
helper.pytorch_model_downloader(
    "/kaggle/working/yolo/runs/train/exp/weights/best.pt"
)
```

With a custom filename:

```python
helper.pytorch_model_downloader(
    "/kaggle/working/yolo/runs/train/exp/weights/best.pt",
    dest_filename="my_yolo_v8_best.pt"
)
```

After execution, a blue clickable link will appear — simply click it to download the model.

---

### Recommended Cleanup (Save Disk Space)

Once the model has been downloaded, you can safely remove the copied file:

```python
helper.remove("/kaggle/working/my_yolo_v8_best.pt")
```

---

## Full Example Workflow (YOLO / PyTorch Training)

```python
import helper

# 1. Create an output folder
helper.create_folder("/kaggle/working/models")

# 2. Download the best model after training
helper.pytorch_model_downloader(
    "/kaggle/working/yolo/runs/train/exp/weights/best.pt",
    "yolo_v8_final_best.pt"
)

# 3. (Optional) Download last.pt as well
helper.pytorch_model_downloader(
    "/kaggle/working/yolo/runs/train/exp/weights/last.pt",
    "yolo_v8_final_last.pt"
)

# 4. Clean up copied files after download
helper.remove("/kaggle/working/yolo_v8_final_best.pt")
helper.remove("/kaggle/working/yolo_v8_final_last.pt")
```

---

## Important Kaggle Notes

* Only files inside `/kaggle/working/` are downloadable
* Session files are cleared when the notebook is restarted or closed
* Internet access must be enabled to download `helper.py`
* Uses only Python standard library modules (`os`, `shutil`)

---

## License

Free to use and modify for:

* Kaggle competitions
* Research
* Personal and commercial projects

No attribution required.

* Split this into **Quick Start / Advanced Usage**
* Provide a minimal version for Kaggle notebooks only
