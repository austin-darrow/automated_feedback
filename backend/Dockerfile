FROM --platform=linux/amd64 python:3.12.5

WORKDIR /backend

RUN mkdir /var/log/backend

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]