#!/bin/bash

set -o errexit
set -o nounset

exec >/dev/null  # Don't display anything on stdout.

if [[ $# != 0 ]]; then
    echo >&2 "usage: $0"
    exit 1
fi

STATUS=0

for EXT in ext/*; do
    pushd $EXT
    if [ -d ext ]; then
        for EXTEXT in ext/*; do
            INNER=$(git submodule status --cached $EXTEXT | egrep -o '[0-9a-f]{40}')
            popd
            OUTER=$(git submodule status --cached $EXTEXT | egrep -o '[0-9a-f]{40}')
            pushd $EXT
            if [[ $INNER != $OUTER ]]; then
                echo >&2 "${EXT#ext/}: mismatch of $EXTEXT ($INNER vs. $OUTER)"
                STATUS=1
            fi
        done
    fi
    popd
done
exit $STATUS
