# Use the cdrx/pyinstaller-windows:python3 image as the base
FROM cdrx/pyinstaller-windows:python3

# Set the working directory
WORKDIR /src

# Copy application files
COPY App/ .

# Install dependencies and build the executable
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt && \
    pyinstaller --onefile --name=app-windows main.spec

# Specify the entry point for the final image
CMD ["cmd"]
