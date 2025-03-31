#!/usr/bin/env bash
# Install Tesseract OCR without sudo
echo "Installing Tesseract OCR..."
apt-get update && apt-get install -y tesseract-ocr

# Install Python dependencies
pip install -r requirements.txt
