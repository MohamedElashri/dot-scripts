#!/bin/sh

# $X can be many things, such as 1 2 3 4 5, $(seq 1 5), `seq 1 5` or "Mo"
for i in $X
do
  echo "Looping $i"
done

