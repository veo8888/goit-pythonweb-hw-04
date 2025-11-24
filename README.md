# goit-pythonweb-hw-04

## 🎉 Async File Sorter — Asynchronous File Sorter

🗂️ Instantly sorts thousands of files by extension

⚡ Works asynchronously (asyncio + aiofiles)

🧪 Fully test-ready thanks to the random file generator

## 🚀 Features

✔ Asynchronous file copying

✔ Recursive directory traversal

✔ Automatic creation of extension-based subfolders

✔ Error logging

✔ Limiting the number of concurrent tasks (Semaphore)

✔ Supports running via Poetry or standard pip

✔ Includes a script for generating a random file structure

## 🧰 Installation and Launch

## 🔧 Option 1: Installing via pip (classic method)

1. Create a virtual environment

```bash
python -m venv .venv
```

2. Activate the virtual environment

Windows:

```bash
.\.venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🍀 Option 2: Installation via Poetry

1. Install dependencies

```bash
poetry install --no-root
```

2. Activate the virtual environment

Windows:

```bash
.\.venv\Scripts\activate
```

## 🧪 Generating a Test Structure

`random_file_generator.py` is an auxiliary script and not required for the main program.

- To generate a test structure:

```bash
python random_file_generator.py
```

- It will create a directory:

`random_structure/`

containing nested folders and files of various types — perfect for testing the sorter!

## 📦 Sorting files

(Make sure the virtual environment is activated!)

- Start the sorter:

```bash
python sorter.py "source_path" "output_path"
```

- Example:

```bash
python sorter.py "random_structure" "sorted_structure"
```

## 📝 Logs and errors

If a file cannot be read or copied, the error will be logged:

```yaml
2025-01-01 12:00:00 - ERROR - Copy error somefile.pdf: [error]
```

## 🧹 Removing the Virtual Environment

### pip:

```bash
deactivate
```

```bash
rm -r .venv
```

### Poetry:

- If the environment folder was created inside the project:

```bash
rm -r .venv
```

- If the virtual environment is located in the system:

```bash
poetry env remove python
```
