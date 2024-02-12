FROM pypy:latest

WORKDIR /code

COPY . .

ENTRYPOINT ["python", "main.py"]