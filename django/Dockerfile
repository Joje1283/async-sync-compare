FROM python:3.11.7

WORKDIR /djangoproject
ADD . /djangoproject
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 80
CMD ["gunicorn", "mysqltestdjango.asgi:application", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker"]