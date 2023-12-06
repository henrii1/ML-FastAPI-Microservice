FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /webapp/requirements.txt

WORKDIR /webapp

RUN pip install -r requirements.txt

COPY ./webapp/* /webapp

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]