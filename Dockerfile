FROM python:3.11.3-alpine3.18
LABEL manteiner="victoorsantos266@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY app /app
COPY scripts /scripts

WORKDIR /app
EXPOSE 8000

RUN pip install --upgrade pip && \
    pip install pipenv && \
    python -m pipenv install --system && \
    adduser --disabled-password --no-create-home palace && \
    apk add dos2unix && \
    dos2unix -n /scripts/commands.sh /scripts/commands.sh && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R palace:palace /data/web/static && \
    chown -R palace:palace /data/web/media && \
    chmod -R 775 /data/web/static && \
    chmod -R 775 /data/web/media && \  
    chmod -R 775 /scripts  && \
    chmod -R +x /scripts 

ENV PATH="/scripts:$PATH"
USER palace
CMD ["commands.sh"]