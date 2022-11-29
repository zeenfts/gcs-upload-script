# Deriving the base image (~45MB)
FROM python:3.8-slim-bullseye

WORKDIR /my-uploader

# RUN python3 -m venv /envgcs

# Installing dependencies
COPY requirements.txt .
# RUN . /envgcs/bin/activate && pip install --upgrade pip 
# RUN . /envgcs/bin/activate && pip install -r requirements.txt

# If not using virtual environment
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Copy the rest of files
COPY uploader_gcs.py .
COPY *.json .

# Execute the script
# CMD ["/envgcs/bin/activate"]
ENTRYPOINT ["python", "uploader_gcs.py"]
# CMD ["python", "uploader_gcs.py", "(PROJECT_GCP)", "(BUCKET_GCP)", "-i", "(IMAGE_URL)", "-n", "IMAGE_NAME"]