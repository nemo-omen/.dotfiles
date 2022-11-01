#!/bin/sh

# A basic script that installs all of the apps I currently
# use on a newly installed Arch-based system. I've been
# distro-hopping a lot recently and I'd like to cut down the 
# time it takes to "move in," so to speak.

# Here are the apps I think I'll need:
# Qtile
# khal
# rofi
# alacritty
# vim
# neovim (or maybe Emacs)
# Doom-nvim (or mayme Doom Emacs)
# nvm (and the latest Node)
# Deno (and Denon)
# VS Code
# Android Studio (at least this semester)
# GNU Stow (run command `stow .` from within `~/.dotfiles` after the repo is cloned)
# Powerline fonts
# rNote
# Xournal++ (just in case)

# Digimend kernel drivers!
# https://github.com/DIGImend/digimend-kernel-drivers

# We'll need to set up git/github credentials before proceeding with
# private repo cloning

# Repos to clone:
# git clone https://github.com/nemo-omen/.dotfiles.git ~/.dotfiles
# git clone https://github.com/nemo-omen/school.git ~/school (School may also be copied on storage drive)

# mkdir ~/dev ~/dev/projects ~/dev/learning (The whole ~/dev folder may also be copied on the storage drive)

#########################################
# ADD CHAOTIC AUR MIRRORLIST TO PACMAN #

# must be su
# pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com
# pacman-key --lsign-key FBA220DFC880C036
# pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'

# Append (adding to the end of the file) to /etc/pacman.conf:
# [chaotic-aur]
# Include = /etc/pacman.d/chaotic-mirrorlist 

# sudo pacman -Sy
#########################################
# Misc
# Turn on firefox autoscroll & in `about:config` set `services.sync.prefs.sync.general.autoScroll` to `false`
