# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Need to reload config but you messed up the keybindings?
# qtile cmd-obj -o cmd -f reload_config

from tokenize import Number
from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, Screen, ScratchPad
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from libqtile.utils import guess_terminal
# os and subprocess needed for autostart
import os
import subprocess
import colors
import traverse
mod = "mod4"
# terminal = guess_terminal()
terminal = "alacritty"
HOME = "/home/trainingmontage/"

# CHECK THIS EXAMPLE
# https://github.com/qtile/qtile-examples/blob/master/mort65/config.py

# AUTOSTART #


@hook.subscribe.startup_once
def startup():
    startupscript = os.path.expanduser(
        '~/.config/startup/startup.sh')
    subprocess.Popen([startupscript])


@hook.subscribe.current_screen_change
def log_screen():
    logger.debug('Yep, screen changed')


# COLORS #
# See colors defined in ./colors.py
colors, backgroundColor, foregroundColor, workspaceColor, chordColor = colors.blackbird()
focuscolor = colors[5]
# colors = [
#     ["#011528", "#011528"],  # background (midnight) [0]
#     ["#8695ae", "#8695ae"],  # light gray (limbo) [1]
#     ["#ffffff", "#ffffff"],  # foreground (spirit) [2]
#     ["#05213b", "#05213b"],  # blue/grey (midnight-lighter) [3]
#     ["#79efc4", "#79efc4"],  # lightgreen (portal)[4]
#     ["#66d4ff", "#66d4ff"],  # cyan [5]
#     ["#00b8b4", "#00b8b4"],  # green (nevermore) [6]
#     ["#fac185", "#fac185"],  # orange [7]
#     ["#ff639d", "#ff639d"],  # pink (potion) [8]
#     ["#e863ff", "#e863ff"],  # purple [9]
#     ['#ff6363', '#ff6363'],  # red [10]
#     ["#f1fa8c", "#f1fa8c"]  # yellow (obliterate) [11]
# ]

# LAYOUT THEME & WIDGET DEFAULTS#

widget_defaults = dict(
    font="Fira Mono for Powerline Bold",
    fontsize=18,
    padding=5,
    background=backgroundColor,
    foreground=foregroundColor
)

extension_defaults = widget_defaults.copy()


def init_layout_theme():
    return {
        "margin": 10,
        "border-width": 4,
        "border_focus": focuscolor,
        "border_normal": backgroundColor
    }


layout_theme = init_layout_theme()


# def open_combi(qtile):
#     qtile.cmd(terminal + 'rofi -show combi -sidebar-mode -no-show-match')


def initWidgets(screens):
    return [
        widget.Image(
            filename="~/.config/Arch.png",
            mouse_callbacks={
                "Button1": lazy.group['scratchpad'].dropdown_toggle('start')}
        ),
        widget.Sep(
            foreground=colors[1],
            size_percent=40
        ),
        widget.GroupBox(
            highlight_method="block",
            highlight_color=[backgroundColor, focuscolor],
            active=focuscolor,
            inactive=colors[3],
            borderwidth=0,
            padding_x=10,
            visible_groups=list(screens)
        ),
        widget.Sep(
            foreground=colors[1],
            size_percent=40
        ),
        widget.Prompt(
            background=colors[3]
        ),
        widget.Chord(
            chords_colors={
                "launch": (colors[10], "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.WindowName(),

        # widget.TextBox("default config", name="default"),

        # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground = workspaceColor),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Clock(
            background=backgroundColor,
            format="%a %I:%M %p %m-%d",
            mouse_callbacks={
                "Button1": lazy.group['scratchpad'].dropdown_toggle('khal')}),
        widget.Sep(
            foreground=colors[1],
            size_percent=40
        ),
        widget.Memory(
            format='🐏 {MemPercent}%'
        ),
        widget.Sep(
            foreground=colors[1],
            size_percent=40
        ),
        widget.Volume(fmt='🔊 {}'),
        widget.Sep(
            foreground=colors[1],
            size_percent=40
        ),
        widget.CurrentLayoutIcon(
            foreground=colors[4],
            padding=-10,  # Wow, hackyo
            scale=0.4,
        ),
        widget.Sep(
            foreground=colors[1],
            size_percent=40
        ),
        widget.QuickExit(
            default_text="⏻",
        ),
        widget.Sep(
            foreground=backgroundColor,
            linewidth=5,
            size_percent=40
        ),
    ]


def initBar(groups, screen):
    return bar.Bar(
        initWidgets(groups),
        50,
        padding=5,
        margin=[10, 10, 0, 10],
        # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    )


def go_to_group(name):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            lazy.group[name].toscreen()
            return

        if name in '1234':
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
            # lazy.group[name].toscreen()
        elif name in "567":
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()
            # lazy.group[name].toscreen()
        else:
            qtile.focus_screen(2)
            qtile.groups_map[name].toscreen()
            # lazy.group[name].toscreen()

    return _inner


# KEYBINDINGS #
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Key([mod, "control"], "n", lazy.group['0'].dropdown_toggle('vimnote')),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Key([mod, "control"], "d", lazy.spawn("dmenu_run")),
    Key([mod, "control"], "f", lazy.spawn("firefox-developer-edition")),

    # Cycle through groups
    # Key([mod], "Page_Up", toggle_group),
    Key([mod], "Page_Up", lazy.screen.prev_group(skip_empty=False)),
    Key([mod], "Page_Down", lazy.screen.next_group(skip_empty=False)),

    # Traverse screens
    Key([mod, "control"], "Right", lazy.function(
        traverse.right), desc="Focus screen right"),

    Key([mod, "control"], "Left", lazy.function(
        traverse.left), desc="Focus screen left"),
    Key([mod, "control"], "e", lazy.spawn("rofi"), desc="Show Rofi window"),
    Key([mod, "control"], "o", lazy.spawn("rofi -show filebrowser"),
        desc="Open a file browser"),
    Key([mod, "control"], "w", lazy.spawn(
        "rofi -show window"), desc="Show open windows"),
    Key([mod], "r", lazy.spawn(
        "rofi -show run"), desc="Run a command"),
    Key([mod], "d", lazy.spawn(
        "rofi -show drun"), desc="Run a command with dmenu"),
    Key([mod, "control"], "k", lazy.spawn("rofi -show keys"), desc="Show keys"),
]

# GROUPS #
groups = [Group(f"{i+1}", label="") for i in range(9)]
# See: https://github.com/qtile/qtile/issues/1271#issuecomment-458107043

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                # lazy.function(go_to_group(i.name)),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# SCRATCHPADS #
groups.append(ScratchPad('scratchpad', [
    # Guake-like terminal
    DropDown('term', 'alacritty', width=0.6,
             height=0.4, x=0.2, y=0.006, opacity=1),
    # Calendar widget dropdown
    DropDown('khal', terminal + " -t ikhal -e ikhal",
             x=0.6785, y=0.006, width=0.32, height=0.997, opacity=1),
    DropDown(
        'start', 'rofi -show combi -modes combi -combi-modes "window,drun,run" -sidebar-mode -no-show-match', opacity=1),
]))

# Scratchpad keybindings
keys.extend([
    Key([mod], "F12", lazy.group['scratchpad'].dropdown_toggle(
        'term'), "Toggle 'guakelike' terminal")
])

layouts = [
    layout.Columns(**layout_theme, border_on_single=True),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2, **layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

screens = [
    Screen(
        top=initBar("1234", 0),
        wallpaper="~/Pictures/JupiterJunoMissionWallpaper.jpg",
        wallpaper_mode="fill"
    ),
    Screen(
        top=initBar("567", 1),
        wallpaper="~/Pictures/CosmicCliffsWallpaper.png",
        wallpaper_mode="fill"
    ),
    Screen(
        top=initBar("89", 2),
        wallpaper="~/Pictures/PillarsOfCreationWallpaper.png",
        wallpaper_mode="fill"
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=focuscolor,
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
