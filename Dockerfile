FROM python:3.9-slim
ENV ENV_DB_DATABASE="" \
    ENV_DB_HOSTNAME="" \
    ENV_DB_PORT="" \
    ENV_DB_USER="" \
    ENV_DB_PASSWORD=""
WORKDIR /
COPY . /
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]