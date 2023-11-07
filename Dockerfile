# SERVER IMAGE
# Get the base image
FROM python:3.7 AS package-maker

# Install packages
RUN pip install build

# Set working directory
WORKDIR /work

# TEST IMAGE
# Get the base image
FROM python:3.7 AS test-image

# Copy package files
COPY dist .

# Install packages
RUN pip install *.whl

# Set working directory
WORKDIR /work