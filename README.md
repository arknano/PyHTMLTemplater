# PyHTMLTemplater

PyHTMLTemplater is a simple Python script for generating HTML files using templates.

## Prerequisites

### Python Installation

This project requires Python 3.7 or later.

**Check if Python is installed:**
```bash
python --version
```

**Install Python:**
- **Windows**: Download from [python.org](https://www.python.org/downloads/) and run the installer
  - ⚠️ **Important**: Check "Add Python to PATH" during installation
- **macOS**: `brew install python3`
- **Linux**: `sudo apt-get install python3`

## Usage

### Running the Build

You can run the build process in several ways:

#### Option 1: VS Code Build Task (Recommended)
Press `Ctrl+Shift+B` (Windows/Linux) or `Cmd+Shift+B` (macOS) to run the default build task.

**Or manually:**
1. Open the Command Palette: `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
2. Type "Run Build Task"
3. Select "Build Site"

#### Option 2: Terminal - From Project Root
Open a terminal and run:
```bash
python build.py
```

### How It Works

1. **Template Processing**: The script scans all HTML files in the project and replaces template markers with template file contents.
   - Template markers use the format: `%template_name%`
   - Template files are located in the `templates/` directory with `.html` extension
   - Example: `%header%` will be replaced with the contents of `templates/header.html`

2. **Static Assets**: Copies static directories (images, music, etc.) to the export folder.

3. **Output**: Generates processed HTML files in the `export/` directory.

### Configuration

Edit `config.py` to customize:
- `STATIC_DIRS`: List of directories to copy to export (default: `['images']`)
- `TEMPLATE_PATTERN`: Regex pattern for template markers (default: `r'%(\w+)%'`)
- `EXCLUDE_DIRS`: Directories to skip during processing (default: `['templates', 'export']`)

### Example Template Usage

**index.html:**
```html
<!DOCTYPE html>
<html>
<head>
  %style%
</head>
<body>
  %header%
  <p>Page content goes here</p>
</body>
</html>
```

**templates/header.html:**
```html
<header>
  <h1>My Website</h1>
</header>
```

After running the build, `export/index.html` will contain the merged content.