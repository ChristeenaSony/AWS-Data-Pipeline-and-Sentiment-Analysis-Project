# # Start with an official Python image
# FROM python:3.9-slim

# # Install PostgreSQL development headers
# RUN apt-get update && apt-get install -y libpq-dev

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements.txt into the container
# COPY requirements.txt .

# # Install dependencies from requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of your application code into the container
# COPY . .

# # Expose the port the app will run on
# EXPOSE 8051

# # Define the command to run the app
# CMD ["streamlit", "run", "app.py"]

# Start with an official Python image
FROM python:3.9-slim

# Install build dependencies for psycopg2 and other packages that require compilation
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port the app will run on
EXPOSE 8051

# Define the command to run the app
CMD ["streamlit", "run", "app.py"]

