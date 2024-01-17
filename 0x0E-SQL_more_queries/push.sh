#!/bin/bash

while true
do
    git add .
    git commit -m "$1"
    git push

    sleep 25
done