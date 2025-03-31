FROM python:3.11

# Install Tesseract
RUN apt-get update && apt-get install -y tesseract-ocr

# Set up the working directory
WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Start the app
CMD ["python", "main.py"]
