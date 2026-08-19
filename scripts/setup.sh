#!/usr/bin/env bash

if [ $# -ne 0 ]; then
    echo "usage: $0"
    exit
fi

shopt -s globstar

echo "pulling the newest version of the tabs repository"
git -C .. pull

declare -A CATEGORIES=(
    [czech]="../songs/czech"
    [english]="../songs/english"
    [melodies]="../melodies"
)

cp -r template/* tabs-web/

echo "converting tabs to html"
for category in "${!CATEGORIES[@]}"; do
    src="${CATEGORIES[$category]}"
    mkdir -p "tabs-web/$category"
    for i in "$src"/*.tab; do
        [ -e "$i" ] || continue
        echo -n "processing $i : "
        result="tabs-web/$category/$(basename -s .tab "$i").html"
        ./code/convert.py < "$i" > "$result"
        echo $?
    done
done

substitute(){
    FILE="$1"
    MARKER="$2"
    TEXT="$3"
    sed -i "s|$MARKER|$TEXT\n$MARKER|" "$FILE"
}

echo "adding all songs to the 'all.html' page"
for category in "${!CATEGORIES[@]}"; do
    src="${CATEGORIES[$category]}"
    for i in "$src"/*.tab; do
        [ -e "$i" ] || continue
        NAME="$(basename -s .tab "$i")"
        substitute "tabs-web/all.html" '<!--MARK-->' "<li><a href=\"$category/$NAME.html\">$NAME</a></li>"
    done
done

for category in "${!CATEGORIES[@]}"; do
    PAGE="tabs-web/$category/index.html"

    INDEX_PAGE="tabs-web/index.html"
    echo "adding '$PAGE' page to the landing page"
    substitute "$INDEX_PAGE" '<!--CATEGORIES-->' "<li><a href=\"$category/index.html\">$category</a></li>"

    echo "adding all songs to the '$PAGE' page"
    cp "tabs-web/category.html" "$PAGE"
    substitute "$PAGE" '<!--CATEGORY-->' "$category"
    for i in "tabs-web/$category"/*.html; do
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
