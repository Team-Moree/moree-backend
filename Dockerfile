FROM python:3.12-slim

ENV PROJECT_DIR_PATH=/project

WORKDIR ${PROJECT_DIR_PATH}

COPY requirements.txt .

RUN apt update && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    nginx \
    goaccess \
    supervisor \
    vim \
    htop \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove gcc libc-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN ln -s $(realpath django/django.nginx.conf) /etc/nginx/conf.d/
RUN ln -sf $(realpath nginx.conf) /etc/nginx/nginx.conf
RUN mkdir -p django/logs/nginx

RUN ln -s $(realpath django/supervisor.conf) /etc/supervisor/conf.d/
RUN ln -sf $(realpath supervisord.conf) /etc/supervisor/

RUN python django/manage.py collectstatic --noinput

RUN ./django/reset_local_db.bash

EXPOSE 8080

CMD ["./start.bash"]
