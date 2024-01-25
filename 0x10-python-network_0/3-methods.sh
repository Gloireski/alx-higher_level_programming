#!/bin/bash
#  takes in a URL and displays all HTTP methods the server will accept.
curl -s -I -X OPTIONS $1 | grep -i Allow | cut -d" " -f2,3,4
