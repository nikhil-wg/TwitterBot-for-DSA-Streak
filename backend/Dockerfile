# Use an official Python image that supports Tesseract
FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
