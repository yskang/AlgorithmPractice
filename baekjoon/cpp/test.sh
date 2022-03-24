#!/bin/bash

A=$1
B=$2
X=$3
Y=$4
result_check=$5
gcc  -DDEBUG b.c  -o a.out 
#gcc c.c -DDEBUG -DNOT_FAST -o b.out 
while   true ;
do
    a=$((RANDOM%A+1))
    b=$((RANDOM%B+1))
    x=$((RANDOM%X+1))
    y=$((RANDOM%Y+1))
    echo "$a $b $x $y" > r_in.txt
    cat r_in.txt
    # time ./a.out < r_in.txt
    #R=`time ./a.out < r_in.txt`
    R=`time python3 inje_did_you_catch_a_mushmom_17221.py < r_in.txt`
    r=($R)
    [[ "$result_check" == "" ]] && continue
    #IFS=$'\n'
    
    R_F=`time ./a.out < r_in.txt`
    r_f=($R_F)
    [[ ${r[0]} == ${r_f[0]} ]] && continue

    echo -e "Mismatch " $R " <<>> " $R_F  " || "  ${r[0]}  " || " ${r_f[0]}
    break
done

