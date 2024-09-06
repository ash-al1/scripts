#!/bin/bash
#
if [ -z "$1" ]; then
    echo "Usage: $0 <file-to-watch>"
    exit 1
fi

# Constants
FILE="$1"
COMMAND="python $FILE"
LAST_MOD_TIME=$(stat -c %Y "$FILE")

# Run pytho file every time fingerprint change
while true; do
	CURRENT_MOD_TIME=$(stat -c %Y "$FILE")
    if [[ $CURRENT_MOD_TIME != $LAST_MOD_TIME ]]; then
        clear
        echo "==============START=============="
        $COMMAND
        LAST_MOD_TIME=$CURRENT_MOD_TIME
        echo "===============FIN==============="
    fi
    sleep 1
done
