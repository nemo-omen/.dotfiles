#!/bin/sh

swayidle -w \ 
    timeout 300 'swaylock' \ 
    timeout 330 'hyprctl dispatch dpms off' \
    # timeout 600 'systemctl suspend' \
    resume 'hyprctl dispatch dpms on' \
    before-sleep 'player-ctl pause; swaylock' lock swaylock