#!/bin/bash

wait_for () {
    for _ in `seq 0 100`; do
        (echo > /dev/tcp/$1/$2) >/dev/null 2>&1
        if [[ $? -eq 0 ]]; then
            echo "$1:$2 accepts connections"
            break
        fi
        sleep 1
    done
}

case "$PROCESS" in
"DEV_DJANGO")
    wait_for "${POSTGRES_HOST}" "${POSTGRES_PORT}"
    python manage.py collectstatic --noinput &&
    python manage.py makemigrations &&
    python manage.py migrate &&
    gunicorn --config gunicorn.conf.py config.wsgi:application --reload --capture-output --log-level info --access-logfile -
    ;;
"TEST")
    pytest -v --cov . --cov-report term-missing --cov-fail-under=90 --color=yes
    ;;
"DJANGO")
    wait_for "${POSTGRES_HOST}" "${POSTGRES_PORT}"
    python manage.py collectstatic --noinput &&
    python manage.py makemigrations &&
    python manage.py migrate &&
    gunicorn --config gunicorn.conf.py config.wsgi:application --reload --capture-output --log-level info --access-logfile -
    ;;
esac
