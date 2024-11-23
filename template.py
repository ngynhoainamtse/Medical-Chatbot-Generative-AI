import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# What need to change for your own project
list_of_files = [
    "src/__init__.py", # constructor file, OP concept
    "src/helper.py", # all functionalities
    "src/prompt.py", 
    ".env",
    "setup.py", # to install folder as local package
    "app.py",
    "research/trials.ipynb",
    "test.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
