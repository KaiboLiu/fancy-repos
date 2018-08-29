n=11
echo "top "$n" in terms of price"
cat -n $1 | sort -rnt$',' -k9|head -$n| lolcat
echo "top "$n" in terms of unit-price"
cat -n $1 | sort -rnt$',' -k11|head -$n| lolcat
