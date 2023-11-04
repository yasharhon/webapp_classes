# SERVER IMAGE
# Get the base image
FROM python:3.7 AS package-maker

# Install packages
RUN pip install build

# Set working directory
WORKDIR /work