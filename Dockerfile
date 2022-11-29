# Deriving the base image (~45MB)
FROM python:3.8-slim-bullseye

WORKDIR /usr/src/app

RUN python3 -m venv /envgcs

# Installing dependencies
COPY requirements.txt .
RUN . /envgcs/bin/activate && pip install --no-cache-dir -r requirements.txt

# Copy the rest of files
COPY . .

# Execute the script
CMD ["/envgcs/bin/activate"]
ENTRYPOINT ["python", "uploader_gcs.py"]