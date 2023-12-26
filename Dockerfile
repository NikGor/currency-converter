# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install poetry
RUN pip install poetry

# Use poetry to install dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Make ports available to the world outside this container
EXPOSE 5000 8000

# Start both applications using a shell script
COPY start.sh /app
CMD ["/bin/bash", "/app/start.sh"]
