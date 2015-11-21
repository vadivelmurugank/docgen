#!/bin/bash
# sed -i 
file=${1}
echo "processing $1"
sed -i '/^$/d' $file
sed -i '/*[" "]*$/d' $file
sed -i 's/[" "]*$//' $file
sed -i 's/\t/    /' $file
