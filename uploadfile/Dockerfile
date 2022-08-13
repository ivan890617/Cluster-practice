FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

COPY ./app.py /app

RUN pip install python-multipart

RUN pip install fastapi uvicorn

RUN pip install pandas

RUN pip install joblib

RUN pip install numpy

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app:app", "--reload","--host", "127.0.0.1", "--port", "8000"]