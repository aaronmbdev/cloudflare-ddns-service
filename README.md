# Cloudflare DDNS Service

This is an Debian installable service that will serve as a DDNS client that updates the DNS records of a Cloudflare hosted domain. 
The functionality is limited to only keep one domain updated using an A record. 

## Usage


### Setup Cloudflare account and domain to keep updated

```
ddns setup --cloudflare-key XXXXX --domain abc.com
```

### Start DDNS Service
Once the service is configured, we can start the ddns service

```
ddns start
```
