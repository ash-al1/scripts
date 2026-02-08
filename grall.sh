#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: grall <name> <file>"
    exit 1
fi

if [ ! -f "$2" ]; then
    echo "Error: File not found"
    exit 1
fi

awk -v term="$1" '
BEGIN { IGNORECASE = 1 }

function indent(s) {
    match(s, /^[[:space:]]*/)
    return RLENGTH
}

function flush() {
    if (n == 0) return
    while (n > 0 && lines[n] == "") n--
    for (i = 1; i <= n; i++) print lines[i]
    n = 0
}

/^[[:space:]]*(def|class)[[:space:]]/ && $0 ~ term {
    flush()
    printing = 1
    level = indent($0)
    lines[++n] = $0
    next
}

printing {
    curr_indent = indent($0)
    
    if (/^[[:space:]]*$/) {
        lines[++n] = $0
    } else if (curr_indent <= level) {
        flush()
        printing = 0
    } else {
        lines[++n] = $0
    }
}

END { flush() }
' "$2"
