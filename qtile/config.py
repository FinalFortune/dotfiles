from libqtile.config import Key, Screen, Group, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget
from libqtile import hook
import subprocess
import re

mod = "mod4"

@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog'
        or window.window.get_wm_transient_for()):
        window.floating = True

@hook.subscribe.client_new
def idle_dialogues(window):
    if((window.window.get_name() == 'Search Dialog') or
       (window.window.get_name() == 'Module') or
       (window.window.get_name() == 'Goto') or
       (window.window.get_name() == 'IDLE Preferences')):
        window.floating = True

@hook.subscribe.client_new
def libreoffice_dialogues(window):
    if((window.window.get_wm_class() == ('VCLSalFrame', 'libreoffice-calc')) or
    (window.window.get_wm_class() == ('VCLSalFrame', 'LibreOffice 3.4'))):
        window.floating = True

keys = [
    # Audio Control
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c 0 -q set Master 2dB+")),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -c 0 -q set Master 2dB-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -c 0 -q set Master toggle")),

    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),
    # switch between groups
    # Key([mod], "h", lazy.screen.prevgroup(skip_managed=True)),
    # Key([mod], "l", lazy.screen.nextgroup(skip_managed=True)),

    # switch between screens,
    Key([mod], "h", lazy.to_screen(0)),  # left
    Key([mod], "l", lazy.to_screen(1)),  # right
    # Move windows up or down in current stack
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_up()
    ),
    # quit the window manager
    Key(
        [mod, "shift"], "q", lazy.shutdown()
    ),
    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "space",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),
    # toggle fullscreen
    Key(
        [mod], "f", lazy.window.toggle_fullscreen()
    ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "Return", lazy.spawn("urxvt")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",    lazy.nextlayout()),
    Key([mod], "w",      lazy.window.kill()),

    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod], "r", lazy.spawncmd()),
]


# My App Groups
webApps = ["google-chrome-stable"]
mailApps = ["thunderbird"]
chatApps = ["pidgin"]

groups = [
    Group("coding"),
    Group("doc"),
    Group("www", matches=[Match(wm_class=["Firefox"])]),
    Group("chat", matches=[Match(wm_class=["pidgin"])]),
    Group("mail", matches=[Match(wm_class=["Thunderbird"])]),
    Group("music", matches=[Match(wm_class=["ncmpcpp"])])
]

for i, g in enumerate(groups):
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], str(i + 1), lazy.group[g.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], str(i + 1), lazy.window.togroup(g.name))
    )

dgroups_key_binder = None
dgroups_app_rules = []

border_args = dict(
    border_width=1,
)

layouts = [
    layout.Max(),
    layout.MonadTall(),

    # a layout just for gimp
    layout.Slice('left', 192, name='gimp', role='gimp-toolbox',
         fallback=layout.Slice('right', 256, role='gimp-dock',
         fallback=layout.Stack(stacks=1, **border_args))),

    # a layout for pidgin
    layout.Slice('right', 256, name='pidgin', role='buddy_list',
                 fallback=layout.Stack(stacks=1, **border_args))

]

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox("default config", name="default"),
                widget.Systray(),
                widget.Volume(),
                widget.Clock('%Y-%m-%d %a %I:%M %p'),
            ],
            30,
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox("default config", name="default"),
                widget.Systray(),
                widget.Volume(),
                widget.Clock('%Y-%m-%d %a %I:%M %p'),
            ],
            30,
        ),
    )
]

main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
mouse = ()
auto_fullscreen = True
widget_defaults = {}


def is_running(process):
    s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x):
            return True
    return False


def execute_once(process):
    if not is_running(process):
        return subprocess.Popen(process.split())


# start programs after Qtile
@hook.subscribe.startup
def startup():
    # background wallpaper
    execute_once("feh --bg-scale "
                 "/home/finalfortune/Downloads/Pictures/Wallpapers/me.jpg")
    execute_once("firefox")
    execute_once("thunderbird")
    execute_once("urxvt -e ncmpcpp")
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])
