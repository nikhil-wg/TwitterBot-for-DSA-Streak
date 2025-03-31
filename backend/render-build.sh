#!/bin/bash

# Exit on error
set -o errexit

# Update package list and install Tesseract
sudo apt-get update && sudo apt-get install -y tesseract-ocr

# Install Python dependencies
pip install -r requirements.txt
 