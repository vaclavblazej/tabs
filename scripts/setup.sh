#!/usr/bin/env bash

if [ $# -ne 0 ]; then
    echo "usage: $0"
    exit
fi

shopt -s globstar

echo "pulling the newest version of the tabs repository"
cd tabs || exit
git pull
cd ..

cp -r template/* tabs-web/

echo "converting tabs to html"
for i in **/*.tab; do
    echo -n "processing $i : "
    source="$i"
    result="$(dirname "${i/tabs\//tabs-web\/}")/$(basename -s .tab "$i").html"
    mkdir -p "$(dirname "$result")"
    ./code/convert.py < "$source" > "$result"
    echo $?
done

substitute(){
    FILE="$1"
    MARKER="$2"
    TEXT="$3"
    sed -i "s|$MARKER|$TEXT\n$MARKER|" "$FILE"
}

echo "adding all songs to the 'all.html' page"
for i in **/*.tab; do
    result="$(dirname "${i/tabs\//tabs-web\/}")/$(basename -s .tab "$i").html"
    NAME="$(basename -s .html "$result")"
    substitute "tabs-web/all.html" '<!--MARK-->' "<li><a href=\"${result/tabs-web\//}\">$NAME</a></li>"
done

for d in tabs/*/; do
    PAGE="${d/tabs\//tabs-web\/}index.html"
    PAGE_DIR="$(dirname "$PAGE")"

    INDEX_PAGE="tabs-web/index.html"
    echo "adding '$PAGE' page to the landing page"
    NAME="$(basename -s .html "$d")"
    echo "$PAGE"
    substitute "$INDEX_PAGE" '<!--CATEGORIES-->' "<li><a href=\"${PAGE/tabs-web\//}\">$NAME</a></li>"

    echo "adding all songs to the '$PAGE' page"
    cp "tabs-web/category.html" "$PAGE"
    substitute "$PAGE" '<!--CATEGORY-->' "$(basename "$d")"
    for i in "$PAGE_DIR"/*.html; do
        LINK="$(basename "$i")"
        NAME="$(basename -s .html "$i")"
        if [ "$NAME" == "index" ]; then
            continue
        fi
        substitute "$PAGE" '<!--MARK-->' "<li><a href=\"$LINK\">$NAME</a></li>"
    done
done

# echo "committing and pushing the website"
# cd tabs-web
# git add .
# git commit -m "$(date +"%F")"
# git push
# cd ..
