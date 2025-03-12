# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy Python script into the container
COPY hello.py .

# Install Flask
RUN pip install flask

# Expose port 80
EXPOSE 80

# Run the Python script
CMD ["python", "hello.py"]