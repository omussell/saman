FROM public.ecr.aws/docker/library/python:3.10

COPY . /app


ENV PATH="/opt/venv/bin:${PATH}"
ENV VIRTUALENV=/opt/venv
ENV PYTHONPATH=/app

#RUN apt install -y python3-venv python3-dev libcairo2-dev pkg-config

RUN python3.10 -m venv /opt/venv

RUN pip install -r /app/requirements/production.txt

WORKDIR /app/

CMD [ "uvicorn", "hortus.main:app" ]
