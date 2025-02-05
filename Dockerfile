FROM python:3.12-slim-bookworm
ENV UV_COMPILE_BYTECODE=1
ENV PYTHONUNBUFFERED=1
# RUN apt-get update && apt-get install -y curl htop && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY . /app

WORKDIR /app


RUN uv sync --frozen --no-cache

CMD ["uv", "run", "main.py"]