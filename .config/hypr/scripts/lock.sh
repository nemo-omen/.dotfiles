#!/bin/sh

# Idle timeout to lock screen
swayidle -w \ 
    timeout 300 'swaylock' \ 
    timeout 360 'hyprctl dispatch dpms off' \
    resume 'hyprctl dispatch dpms on' \
    before-sleep 'player-ctl pause; swaylock' lock swaylock

gtklock
# kill %%