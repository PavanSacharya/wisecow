# Dockerfile
FROM debian:bookworm-slim

# Install cowsay, fortune-mod, socat, and netcat-openbsd (supports -N)
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay socat netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Add /usr/games to PATH (where cowsay/fortune are installed)
ENV PATH="/usr/games:${PATH}"

WORKDIR /app
COPY wisecow.sh .
RUN chmod +x wisecow.sh

EXPOSE 4499
CMD ["./wisecow.sh"]
