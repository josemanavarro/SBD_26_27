FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "import duckdb; duckdb.sql('INSTALL httpfs;')"

CMD ["sleep","infinity"]
