    #!/usr/bin/env bash

    ## “clean up” a typical macOS zip file
    set -exuo pipefail
        
    VERBOSE=false
    while getopts "v" arg; do
    case $arg in
        v) VERBOSE=true;;
    esac
    done
    shift $((OPTIND-1))


    zipfile=$1
    if [ ! -f "$zipfile" ] || [ ! "${zipfile##*.}" = "zip" ] ; then
        echo "$0: .zip file expected" >&2
        exit 1
    fi

    zip -d "${zipfile}" "__MACOSX*" ".DS_Store" "*/.DS_Store" "Thumbs.db" "*/Thumbs.db"

    if [ $VERBOSE = true ]; then
        unzip -l "${zipfile}" | sort -k 5
    fi
