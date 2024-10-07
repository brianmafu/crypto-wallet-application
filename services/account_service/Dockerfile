FROM python:3.9-slim

# Install netcat
RUN apt-get update && apt-get install -y netcat-openbsd

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the wait-for-it script into the container
COPY ./wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Copy your application code
COPY . /app
RUN pip install pylint
RUN pylint --rcfile=.pylintrc .
# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Set the entry point to wait for the database and run migrations
ENTRYPOINT ["./wait-for-it.sh", "db:5432", "--"]
