FROM python:3.10.4-slim-buster

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    COLUMNS=200


# Set timezone
RUN ln -fs /usr/share/zoneinfo/Asia/Almaty /etc/localtime \
    && echo "Asia/Almaty" > /etc/timezone

WORKDIR /src

COPY ./src/requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
    && pip install \
    --no-cache-dir -Ur /src/requirements.txt

COPY ./src /src
CMD ["/src/entrypoint.sh"]