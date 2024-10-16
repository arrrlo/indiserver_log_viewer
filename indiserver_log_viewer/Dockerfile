# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV LOG_FILE_PATH /app/logs/logfile.log

# Create directory for the app user
RUN mkdir -p /indiserver_log_viewer

# Set the working directory to /app
WORKDIR /indiserver_log_viewer

# Copy the current directory contents into the container at /app
COPY . /indiserver_log_viewer/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the app
EXPOSE 8080

# Create a directory for logs and set permissions
RUN mkdir -p /indiserver_log_viewer/logs
RUN chmod -R 755 /indiserver_log_viewer/logs

# Command to run when the container starts
CMD ["daphne", "-b", "0.0.0.0", "-p", "8080", "indiserver_log_viewer.asgi:application"]

