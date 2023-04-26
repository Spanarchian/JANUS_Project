FROM python:3.9-alpine
WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./api /src/api
CMD ["uvicorn", "messageservice:api", "--host", "0.0.0.0", "--port", "8008"]
 
