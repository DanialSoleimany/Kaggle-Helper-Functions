Kaggle Helper Functions
A lightweight, dependency-free Python module with simple and safe utilities for file/folder management in Kaggle Notebooks.
Perfect for organizing outputs, renaming folders, cleaning up, and — most importantly — easily downloading trained PyTorch models (like YOLO best.pt or last.pt).

Quick Start
1. Download the helper module
Run this cell once in your Kaggle notebook:
Pythonimport urllib.request
url = "https://raw.githubusercontent.com/DanialSoleimany/Kaggle-Helper-Functions/main/helper.py"
urllib.request.urlretrieve(url, "helper.py")
2. Import it
Pythonimport helper
That's it — no extra packages needed!

Available Functions
create_folder(path)
Safely creates a folder. Can be called multiple times without errors.
Pythonhelper.create_folder("/kaggle/working/my_outputs")
remove(path)
Deletes a file or an entire folder (recursively).
Python# Delete a folder and everything inside
helper.remove("/kaggle/working/old_experiment")

# Delete a single file
helper.remove("/kaggle/working/temp.yaml")
⚠️ Caution: Folder deletion is permanent and recursive.
rename(old_path, new_path)
Renames or moves a file/folder. Fails if the destination already exists.
Pythonhelper.rename("/kaggle/working/run1", "/kaggle/working/best_run")
pytorch_model_downloader(source_path, dest_filename="best.pt")
The most useful function for Kaggle users!
Kaggle only allows downloads from /kaggle/working/. This function:

Copies your trained .pt model from any deep path to /kaggle/working/
Generates a clickable download link right in the notebook
Makes the file visible in the Output tab for manual download

Usage
Python# Default name (best.pt)
helper.pytorch_model_downloader("/kaggle/working/yolo/runs/train/exp/weights/best.pt")

# Custom name
helper.pytorch_model_downloader(
    "/kaggle/working/yolo/runs/train/exp/weights/best.pt",
    dest_filename="my_yolo_v8_best.pt"
)
After running, you'll see a blue clickable link — just click to download!
Recommended Cleanup (Save disk space)
Once downloaded, remove the copied file:
Pythonhelper.remove("/kaggle/working/my_yolo_v8_best.pt")

Full Example Workflow (YOLO / PyTorch Training)
Pythonimport helper

# 1. Create output folder
helper.create_folder("/kaggle/working/models")

# 2. (After training finishes) Download the best model
helper.pytorch_model_downloader(
    "/kaggle/working/yolo/runs/train/exp/weights/best.pt",
    "yolo_v8_final_best.pt"
)

# 3. (Optional) Also download last.pt
helper.pytorch_model_downloader(
    "/kaggle/working/yolo/runs/train/exp/weights/last.pt",
    "yolo_v8_final_last.pt"
)

# 4. Clean up copied files after download
helper.remove("/kaggle/working/yolo_v8_final_best.pt")
helper.remove("/kaggle/working/yolo_v8_final_last.pt")

Important Kaggle Tips

Only files in /kaggle/working/ are persistent and downloadable
Session outputs are cleared when the notebook is closed or restarted
Always enable Internet in notebook settings to download helper.py
No external dependencies — uses only os and shutil


License
Free to use and modify for Kaggle competitions, research, personal projects, or any other purpose. No attribution required.
