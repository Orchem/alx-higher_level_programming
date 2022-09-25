#!/bin/bash
# script that displays all allowed methods
curl -Is "$1" | grep Allow | cut -d " " -f2-
