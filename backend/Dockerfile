FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential make \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN make install

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["make", "start"]
