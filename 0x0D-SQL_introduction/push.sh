#!/bin/bash

read commit
while true
do
    git add .
    git commit -m "$commit"
    git push

    sleep 15
done