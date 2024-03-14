# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the Python source code into the container
COPY . /app

# Install Flask and any other dependencies
RUN pip3 install Flask

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the Flask application
ENTRYPOINT ["python", "main.py"]