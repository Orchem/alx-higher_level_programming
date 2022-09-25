#!/bin/bash
# script that displays status code of webpage
curl -so /dev/null -w "%{http_code}" "$1"
