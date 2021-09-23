FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install -r requirements.txt
COPY . /code/

CMD [ "gunicorn", "e_learning.wsgi" ]


