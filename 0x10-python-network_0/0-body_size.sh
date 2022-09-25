#!/bin/bash
# script that displays the size of the body response
curl -so /dev/null -w "%{size_download}\n" "$1"
