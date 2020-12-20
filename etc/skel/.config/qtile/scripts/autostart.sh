#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}


#Special python script for auto wallpaper and colorscheme change
~/.config/qtile/scripts/pywal-colors.py


#feh --bg-fill ~/.config/qtile/flower.jpg &
conky -c ~/.config/conky/conky.conf &


#starting utility applications at boot time
run nm-applet &
run pamac-tray &
numlockx on &
pasystray &
blueman-applet &
flameshot &
picom --config $HOME/.config/picom/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst &

#starting user applications at boot time
run volumeicon &
#run discord &
#nitrogen --random --set-zoom-fill &
#run caffeine -a &
#run vivaldi-stable &
#run firefox &
#run thunar &
#run dropbox &
#run insync start &
#run spotify &
#run atom &
#run telegram-desktop &
