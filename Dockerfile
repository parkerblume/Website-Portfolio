FROM python:3.9.12-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
    apt-get install -y \
    make \
    bash \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY setup.cfg ./setup.cfg
COPY Blume_Website ./Blume_Website
COPY Makefile ./Makefile

EXPOSE 8000

COPY requirements/dev.txt ./requirements/dev.txt
RUN pip install -r ./requirements/dev.txt

COPY . .

CMD ["make", "start-server"]