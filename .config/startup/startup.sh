#!/bin/sh
xrandr --output HDMI-A-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DisplayPort-0 --mode 1920x1080 --pos 1920x0 --rotate normal --output DisplayPort-1 --mode 1920x1080 --pos 3840x0 --rotate normal --output DisplayPort-2 --off

sleep 2s

xsetwacom --set "10" MapToOutput DisplayPort-1
xsetwacom --set "11" MapToOutput DisplayPort-1

picom --experimental-backends -b