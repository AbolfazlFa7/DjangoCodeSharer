# DjangoProjectExporter

A simple tool for Django developers to extract project files into a single text file, ideal for sharing with AI for development assistance.
i think it is very useful for who are just started to learn django, and want help from Ai, but they have no time , for copy paste all text in each file for Ai !

A better way to use this tool is, put it in a folder, and create an alias from it in your system, to access it easly
```bash
alias Export 'python ~/Downloads/DjangoCodeSharer.py'
```

## Example
<img src="img.jpg">

<br>

## Features
- Extracts project files to `file.txt`.
- Supports multiple file formats (`python`, `html`, `css`, `js`, `text`) with `-f` flag.
- Allows specifying a project folder path.
- Colorful CLI interface using `colorama`.

## Installation
Install the required module:
```bash
pip install colorama
```

## Usage
```bash
python django_project_exporter.py [path] [-f]
```

- `[path]`: Project folder path (optional). Defaults to current directory (`.`).  
  Example: `python django_project_exporter.py ./my_django_project`
- `-f`: Enables file format selection. Choose formats by entering numbers:  
  - `1`: `.py` (Python)  
  - `2`: `.html` or `.htm` (HTML)  
  - `3`: `.txt` (Text)  
  - `4`: `.css` (CSS)  
  - `5`: `.js` (JavaScript)  
  - `6`: All formats above  
  Example: Enter `123` to select Python, HTML, and Text.

### With `-f` Flag:
```bash
python django_project_exporter.py ./my_project -f
```
- Prompts for format selection (e.g., `123`).  
- Only selected file types (e.g., `.py`, `.html`, `.txt`) are processed.

### Without `-f` Flag:
If `-f` is not used, only the following files are processed by default:  
- `.py` (Python)  
- `.html` and `.htm` (HTML)

### Example Without `-f`:
```bash
python django_project_exporter.py ./my_project
```
- Only `.py` and `.html` files are extracted.

## Output
- Selected files and their contents are saved to `DjangoCodeSharer.txt`in the folder that this code is.  
- File details (size and status) are displayed in the console.

## Requirements
- Python 3.6 or higher
- `colorama` module
