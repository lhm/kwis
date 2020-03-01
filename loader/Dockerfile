FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY catalog.yml ./
COPY *.py ./

CMD ["python", "./loader.py", "--help"]
