#    ______                        _           __     ______    
#   / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
#  / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
# / /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
# \____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
#                           /___/                               

# Daily coding problem (Algorithm, DB and etc)

# Date: 2024-JUN-22

# app: leetcode
# problem: https://leetcode.com/problems/tenth-line/description/

filename="file.txt"

count=0

while IFS= read -r line; do
    ((count++))
    if [ $count -eq 10 ]; then
        echo "$line"
    fi
done < "$filename"