# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Specify the command to run the application
CMD ["uvicorn", "controller.CrudController:app", "--host", "0.0.0.0", "--port", "8000"]
