# PyHTMLTemplater

PyHTMLTemplater is a simple Python script for generating HTML files using templates.

## Prerequisites

Python 3.7 or later

## Usage

### Running the Build

#### Option 1: VS Code Build Task (Recommended)
Open the folder in VSCode and press `Ctrl+Shift+B` (Windows/Linux) or `Cmd+Shift+B` (macOS) to run the default build task.

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
