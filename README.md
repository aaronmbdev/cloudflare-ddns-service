# Cloudflare DDNS Service

This is an Debian installable service that will serve as a DDNS client that updates the DNS records of a Cloudflare hosted domain. 
The functionality is limited to only keep one domain updated using an A record. 

## Usage

### Recommended - Setup a virtual environment to get started
This project was build using 3.10

```
python -m venv venv
```

### Install dependencies

```
pip install .
```


### Setup Cloudflare account and domain to keep updated

```
ddns setup --cloudflare-token XXXXX --domain abc.com --subdomain xxx
```

### Start DDNS Service
Once the service is configured, we can start the ddns service

```
ddns start
```


## Usage from Docker image - No install required

### First we need to create a config file
We will add this content to config.json
```
{
    "cloudflare_token": "XXXXX",
    "domain": "google.com",
    "subdomain": "storage"
}
```

With this file we will be setting the configuration for storage.google.com

### Use docker-compose to launch the service from the latest avaiable version
Contents of the docker-compose.yaml

```
version: '3.8'

services:
  ddns-run:
    image: ghcr.io/aaronmbdev/cloudflare-ddns-service:latest
    command: start
    volumes:
      - ./config.json:/usr/src/app/config/config.json
    restart: always

```

Then we only need to use docker-compose up to start the service. Use -d to start it in the background and leave it enabled.
