# AWS
- yetta_chen
- 25Vg-J7|
- https://661990540174.signin.aws.amazon.com/console

# kubectl
- kubectl port-forward service/milvus 19530:19530



FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir poetry
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN poetry install --no-root --no-cache
COPY . /app/
EXPOSE 8501
ENTRYPOINT ["poetry", "run", "streamlit", "run"]
CMD ["main.py"]