#!/bin/bash

until ./run_followUsers.sh; do
	echo "followUsers script crashed! with exit code $?. Respawning.." >&2
	sleep 1

done


