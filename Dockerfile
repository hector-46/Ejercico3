FROM public.ecr.aws/docker/library/python:3.10-slim

WORKDIR /app

COPY . .

CMD ["python", "app.py"]