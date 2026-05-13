FROM python:3.10

# Create user for running the app

RUN useradd -m appuser

USER appuser

# Setup uv

RUN wget -qO- https://astral.sh/uv/install.sh | sh

ENV PATH="$PATH:/home/appuser/.local/bin"

# Copy files

WORKDIR /app

COPY --chown=appuser:appuser backend/ /app/


RUN uv sync --locked 

ENTRYPOINT ["uv", "run", "main.py"]