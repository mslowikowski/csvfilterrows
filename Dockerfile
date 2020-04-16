FROM python:3-alpine AS base

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

FROM base AS app

WORKDIR /app

COPY . .

WORKDIR /app/csvfilterrows

ENTRYPOINT [ "python3", "csvfilterrows.py" ]

CMD [ "--help" ]