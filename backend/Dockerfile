FROM python:3.10-alpine
WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./api /src/api
CMD ["uvicorn", "api.janusservice:api", "--host", "0.0.0.0", "--port", "8008"]
 
