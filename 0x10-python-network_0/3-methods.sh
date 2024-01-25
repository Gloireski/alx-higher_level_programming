#!/bin/bash
#  takes in a URL and displays all HTTP methods the server will accept.
<<<<<<< HEAD
curl -sI $1 | grep -i "Allow:" | cut -d" " -f2,3,4
=======
curl -sI $1 | grep -i "Allow:" | cut -f2- -d" "
>>>>>>> 60e93dd4074038580dfe0b923fec8b69cec90958
