#!/bin/bash

script=$(basename $0)
DATE=$(date +%Y-%m-%d)
HOURS=$(date +%H:%M:%S)
LOG="/tmp/$script-log"

PY_SCRIPT="chronometer.py"
PATH_PY_SCRIPT="./src"

echo "Started $script [ $DATE $HOURS ]." > $LOG

if [[ $PATH_PY_SCRIPT != $PWD ]]; then
	cd $PATH_PY_SCRIPT
fi

echo "Run $PY_SCRIPT [ $DATE $HOURS ]." >> $LOG

echo "Run $PY_SCRIPT $@ ..."
#python3 $PY_SCRIPT $@
~/.venv/bin/python3 $PY_SCRIPT $@

echo "Finished $script [ $DATE $HOURS ]." >> $LOG
exit 0