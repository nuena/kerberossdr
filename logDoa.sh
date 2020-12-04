#!/bin/sh
logfile="DOA_values/$(date +"%Y.%m.%d_%H-%M-%S")"

while true; do
wget -qO - 127.0.0.1:8081/DOA_value.html 2>&1 | tr '\n' ' ' | ts "%Y.%m.%d_%H:%M:%.S" | tee -a $logfile
echo | tee -a $logfile # newline
done

