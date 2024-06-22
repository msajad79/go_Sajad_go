#    ______                        _           __     ______    
#   / ____/___       _________ _  (_)___ _____/ /    / ____/___ 
#  / / __/ __ \     / ___/ __ `/ / / __ `/ __  /    / / __/ __ \ 
# / /_/ / /_/ /    (__  ) /_/ / / / /_/ / /_/ /    / /_/ / /_/ /
# \____/\____/    /____/\__,_/_/ /\__,_/\__,_/     \____/\____/ 
#                           /___/                               

# Daily coding problem (Algorithm, DB and etc)

# Date: 2024-JUN-23

# app: leetcode
# problem: https://leetcode.com/problems/transpose-file/


filename="file.txt"

awk '
{
    for (i=1; i<=NF; i++)  {
        a[NR,i] = $i
    }
}
NF>p { p = NF }
END {
    for(j=1; j<=p; j++) {
        str=a[1,j]
        for(i=2; i<=NR; i++){
            str=str" "a[i,j];
        }
        print str
    }
}' $filename