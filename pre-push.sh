#!/bin/bash

files_with_nocommit=$(git diff --cached --name-only --diff-filter=ACM $against | xargs grep -i "nocommit" -l | tr '\n' ' ')

if [ "x${files_with_nocommit}x" != "xx" ]; then
    tput setaf 1
    echo "File being committed with 'nocommit' in it:"
    echo $files_with_nocommit | tr ' ' '\n'
    tput sgr0
    exit 1
fi

git ls-files -z **\*.py | xargs --null flake8 --config=pep.cfg
if [ "$?" -ne "0" ]; then exit 1; fi

git ls-files -z **\*.py | xargs --null black --check
if [ "$?" -ne "0" ]; then exit 1; fi

python -m unittest
if [ "$?" -ne "0" ]; then exit 1; fi

exit 0
