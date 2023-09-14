#!/bin/bash

if [ "$1" = 'dec' ]
then
  delta='-'
else
  delta='+'
fi

notify-send "$(brightnessctl s 5%${delta} | awk '{if (NR ==3) print $0}' | sed 's/^[ \t]*//')"
