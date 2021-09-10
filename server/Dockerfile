FROM ubuntu:18.04

RUN apt-get update -y \
    && apt-get install nginx nano curl -y \
    && apt-get install software-properties-common -y \
    && add-apt-repository ppa:certbot/certbot -y \
    && apt-get update -y \
    && apt-get install python-certbot-nginx -y \
    && apt-get clean

EXPOSE 80

STOPSIGNAL SIGTERM

WORKDIR /oriapp

COPY ./sites-enabled/ /etc/nginx/sites-enabled

CMD ["nginx", "-g", "daemon off;"]