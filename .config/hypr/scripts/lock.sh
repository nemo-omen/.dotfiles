#!/bin/sh

# Idle timeout to lock screen
swayidle -w \ 
    timeout 300 'gtklock' \ 
    timeout 360 'hyprctl dispatch dpms off' \
    resume 'hyprctl dispatch dpms on' \
    before-sleep 'player-ctl pause; gtklock' lock gtklock

gtklock
# kill %%