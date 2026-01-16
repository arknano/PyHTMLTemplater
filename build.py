"""
PyHTMLTemplater - HTML template processor.

Processes HTML files with template markers (%template_name%) and generates
static output files with static assets.
"""

import os
import shutil
import re
from config import *


def ensure_export_dir() -> str:
    """
    Create export directory if it doesn't exist.
    
    Returns:
        str: Path to the export directory.
    """
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)
    return EXPORT_DIR


def process_templates(content: str) -> str:
    """
    Replace template markers in content with template file contents.
    
    Template markers use the format: %template_name%
    Looks for template files in TEMPLATE_DIR with .html extension.
    
    Args:
        content (str): HTML content containing template markers.
        
    Returns:
        str: Processed content with templates replaced.
    """
    template_pattern = re.compile(TEMPLATE_PATTERN)
    matches = template_pattern.finditer(content)
    
    processed_content = content
    for match in matches:
        template_name = match.group(1)
        template_file = os.path.join(TEMPLATE_DIR, f"{template_name}.html")
        
        if os.path.exists(template_file):
            with open(template_file, 'r') as f:
                template_content = f.read()
            processed_content = processed_content.replace(
                f"%{template_name}%", template_content
            )
        else:
            print(f"Warning: Template '{template_name}' not found at {template_file}")
    
    return processed_content


def should_process_file(filepath: str) -> bool:
    """
    Determine if a file should be processed based on exclusion rules.
    
    Args:
        filepath (str): Absolute path to the file.
        
    Returns:
        bool: True if file is not in excluded directories, False otherwise.
    """
    rel_path = os.path.relpath(filepath, BASE_DIR)
    return not any(rel_path.startswith(exclude) for exclude in EXCLUDE_DIRS)


def copy_static_dirs() -> None:
    """
    Copy static directories to export folder.
    
    Copies all directories specified in STATIC_DIRS from SOURCE_DIR to EXPORT_DIR.
    Removes existing target directories before copying.
    """
    for static_dir in STATIC_DIRS:
        source_path = os.path.join(SOURCE_DIR, static_dir)
        if os.path.exists(source_path):
            target_path = os.path.join(EXPORT_DIR, static_dir)
            
            if os.path.exists(target_path):
                shutil.rmtree(target_path)
            
            shutil.copytree(source_path, target_path)
            print(f"Successfully copied {static_dir} directory to export")
        else:
            print(f"Warning: Static directory '{static_dir}' not found at {source_path}")


def process_html_files() -> None:
    """
    Find and process all HTML files in the source directory.
    
    Processes template markers in HTML files and outputs them to EXPORT_DIR.
    Skips files in excluded directories.
    """
    ensure_export_dir()
    
    html_files = []
    for root, dirs, files in os.walk(SOURCE_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if should_process_file(filepath):
                    html_files.append(filepath)
    
    for filepath in html_files:
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            
            processed_content = process_templates(content)
            
            filename = os.path.basename(filepath)
            export_path = os.path.join(EXPORT_DIR, filename)
            
            with open(export_path, 'w') as f:
                f.write(processed_content)
            
            rel_path = os.path.relpath(filepath, SOURCE_DIR)
            print(f"Successfully processed {rel_path} to {filename}")
            
        except Exception as e:
            print(f"Error processing {filepath}: {str(e)}")


def main() -> None:
    process_html_files()
    copy_static_dirs()


if __name__ == '__main__':
    main()
