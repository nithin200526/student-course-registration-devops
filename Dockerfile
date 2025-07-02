# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Fix network-related pip issues (force pip to use main PyPI URL)
RUN pip config set global.index-url https://pypi.org/simple

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask app port
EXPOSE 5000

# Run the app
CMD ["python", "app/main.py"]
