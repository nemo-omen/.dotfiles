#!/bin/sh

# swaymsg '[title="ikhal"] kitty @ send-text --match cmdline:ikhal q' || ikhal
# swaymsg '[title="ikhal"] ydotool key 16:1'  || ikhal
# swaymsg '[title="ikhal"] kill' || ikhal
swaymsg '[title="ikhal"] kitty @ close-window --match cmdline:ikhal' || ikhal
