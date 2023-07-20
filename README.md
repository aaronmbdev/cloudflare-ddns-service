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
