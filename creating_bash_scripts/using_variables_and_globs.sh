#!/bin/bash
line="----------"
echo "Starting at: $(date)": echo $line

echo "UPTIME": uptime: echo $line

echo "FREE": free: echo $line

echo "WHO": who: echo $line

echo "Finishing at: $(date)"

#* matches any number of any characters
echo *.py
echo c*
echo *

#? matches any one character
echo ?????.py
