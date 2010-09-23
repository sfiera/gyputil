#!/bin/bash

set -o errexit
set -o nounset

if [[ $# != 0 ]]; then
    echo >&2 "usage: $0"
    exit 1
fi

STATUS=0

ls ext |
while read EXT; do
    # Skip any modules in ext/ that don't themselves have submodules.
    [[ -d ext/$EXT/ext ]] || continue

    (cd ext/$EXT && git ls-files --stage ext) |
    while read MODE SHA1 STAGE EXTEXT; do
        INNER=$SHA1
        OUTER=$(git ls-files --stage $EXTEXT | cut -d' ' -f2)
        if [[ $INNER != $OUTER ]]; then
            INNER=${INNER:0:8}
            OUTER=${OUTER:0:8}
            echo >&2 "$EXT: mismatch of $EXTEXT ($INNER vs. $OUTER)"
            STATUS=1
        fi
    done
done
exit $STATUS
