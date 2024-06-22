#    ______                        _           __     ______    
#   / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
#  / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
# / /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
# \____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
#                           /___/                               

# Daily coding problem (Algorithm, DB and etc)

# Date: 2024-JUN-21

# app: leetcode
# problem: https://leetcode.com/problems/valid-phone-numbers/description/


# Define the input file
INFILE=file.txt

# Read the input file line by line
while read -r LINE
do
    if [[ "$LINE" =~ ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ ]]; then
        echo "$LINE"
    elif [[ "$LINE" =~ ^\([0-9]{3}\)\ [0-9]{3}-[0-9]{4}$ ]]; then
        echo "$LINE"
    fi
done < "$INFILE"
