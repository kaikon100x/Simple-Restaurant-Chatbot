
---

### 🐳 **Dockerfile**

```dockerfile
# Use the official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install required packages
RUN pip install flask

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
