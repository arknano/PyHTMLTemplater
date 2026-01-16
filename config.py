import os

# Base directory 
BASE_DIR = os.path.dirname(__file__)

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
EXPORT_DIR = os.path.join(BASE_DIR, 'export')
SOURCE_DIR = BASE_DIR  # Directory containing source HTML files

# Directories to copy to export
STATIC_DIRS = ['images']  

# File patterns
HTML_PATTERN = '*.html'
TEMPLATE_PATTERN = r'%(\w+)%'  # Regular expression for template markers

# files/directories to skip
EXCLUDE_DIRS = ['templates', 'export']