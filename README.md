# Inro
This is a simple microservice for mailing, currently for google only

# Install

## Pre install

To turn on Application password
----
Google account settings -> Security -> Login to Google -> Two factor authentication -> checked

To create an Application password
----
Google account settings -> Security -> Login to Google -> Application password -> other

create an .env from .env.sample
fillout your gmail and password
```txt
GOOGLE_MAIL=xxxxxxxxx@gmail.com
GOOGLE_SMTP_PASS=xxxxxxx
```

## Build the project

simply run `make build` for installing

# Run

simple run `make test` for running current project