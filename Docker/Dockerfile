# Use an appropriate base image
FROM python:3.9

# Set environment variables
ENV MUSIC_BASEPATH="./music/"

# Set the working directory in the container
WORKDIR /StratagemHell

# Copy the game files into the container
COPY . /StratagemHell

# Install dependencies
RUN pip install pygame python-dotenv
RUN apt-get update && apt-get install -y pulseaudio

# Set the script as executable
RUN chmod +x /StratagemHell/Docker/start_pulseaudio.sh

# Command to run the game
CMD ["/StratagemHell/Docker/start_pulseaudio.sh"]
