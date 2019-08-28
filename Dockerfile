FROM 10.114.15.89:8900/cis-analysis:base
LABEL maintainer="max_lin1@dell.com"

ENV APP_ROOT /data/code
WORKDIR ${APP_ROOT}

COPY . .

CMD cd src && gunicorn -c ./config.py main:app

