#!/bin/bash

export PYTHONPATH=./proppyworker

until python3 followUsers.py -l eng; do
        echo "followUsers script crashed! with exit code $?. Respawning.." >&2
        sleep 1
done &

until python3 followUsers.py -l ara; do
        echo "followUsers script crashed! with exit code $?. Respawning.." >&2
        sleep 1
done &

