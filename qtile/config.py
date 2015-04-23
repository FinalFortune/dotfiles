# from powerline.bindings.qtile.widget import Powerline
from libqtile.config import Key, Screen, Group, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget
from libqtile import hook
import subprocess
import re

mod = "mod4"

# @hook.subscribe.client_new
# def dialogs(window):
#     if(window.window.get_wm_type() == 'dialog'
#             or window.window.get_wm_transient_for()):
#         window.floating = True
#
#
# @hook.subscribe.client_new
# def idle_dialogues(window):
#     if((window.window.get_name() == 'Search Dialog') or
#        (window.window.get_name() == 'Module') or
#        (window.window.get_name() == 'Goto') or
#        (window.window.get_name() == 'IDLE Preferences')):
#         window.floating = True
#
#
# @hook.subscribe.client_new
# def libreoffice_dialogues(window):
#     if ((window.window.get_wm_class() == ('VCLSalFrame', 'libreoffice-calc'))
#         or (window.window.get_wm_class() == ('VCLSalFrame', 'LibreOffice 3.4'))):
#         window.floating = True
#
# #from libqtile.config import Click, Drag
from libqtile.manager import Click, Drag
mouse = [
    # Drag windows around with mouse.
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.disable_floating())
]
# Get this kind of window data from xprop
# These wm_types are always floated
floating_types = set(['dialog'])
# These are programs where names may be matched to float
floating_classes = set(["Steam"])
# names to float, if class is in floating_classes
floating_names = set(["Steam - Self Updater", "Video Driver Check"])
@hook.subscribe.client_state_changed
def whatever(window):
    import logging
    logging.error("csc %r", window)

@hook.subscribe.client_new
def floating_dialogs(window):
    wm_type = window.window.get_wm_type()
    wm_transient = window.window.get_wm_transient_for()
    wm_classes = window.window.get_wm_class()
    wm_name = window.info().get('name')
    wm_classes = set(wm_classes) if wm_classes else set([])
    wm_normal_hints = window.window.get_wm_normal_hints()
    # e.g.
    # {'base_height': 0,
    # 'base_width': 0,
    # 'flags': set(['PBaseSize', 'PPosition', 'PResizeInc', 'PWinGravity']),
    # 'height_inc': 22,
    # 'max_aspect': 0,
    # 'max_height': 0,
    # 'max_width': 0,
    # 'min_aspect': 0,
    # 'min_height': 0,
    # 'min_width': 0,
    # 'width_inc': 10,
    # 'win_gravity': 0}
    if wm_normal_hints:
        min_width = wm_normal_hints.get('min_width')
        min_height = wm_normal_hints.get('min_height')
        max_width = wm_normal_hints.get('max_width')
        max_height = wm_normal_hints.get('max_height')
    else:
        min_width, min_height, max_width, max_height = [None] * 4
        wants_to_be_big = (max_height > 540.0 if max_height is not None else True)
        import logging
        logging.error(
            ("wprg name: {wm_name} "
             "wants to be big: {wants_to_be_big} "
             "type: {wm_type} "
             "classes: {wm_classes} "
             "normal_hints: {wm_normal_hints}").format(
                 wm_name=wm_name,
                 wants_to_be_big=wants_to_be_big,
                 wm_type=wm_type,
                 wm_classes=wm_classes,
                 wm_normal_hints=wm_normal_hints,
             ))
        if wm_transient or wm_type in floating_types or (
            (wm_classes & floating_classes) and
            ((not wants_to_be_big) or (wm_name in floating_names))):
            window.floating = True

keys = [
    # Audio Control
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c 0 -q set Master 2dB+")),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -c 0 -q set Master 2dB-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -c 0 -q set Master toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
    Key([], "XF86Forward", lazy.spawn("mpc next")),
    Key([], "XF86Back", lazy.spawn("mpc prev")),

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
    Key([mod], "Return", lazy.spawn("urxvtc -e tmux")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",    lazy.nextlayout()),
    Key([mod], "w",      lazy.window.kill()),

    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod], "r", lazy.spawncmd()),
]


# My App Groups
webApps = ["google-chrome-stable","Firefox"]
mailApps = ["thunderbird"]
chatApps = ["pidgin"]

groups = [
    Group("coding"),
    Group("doc"),
    Group("www", matches=[Match(wm_class=["Firefox"])]),
    Group("chat", matches=[Match(wm_class=["pidgin"])]),
    Group("mail", matches=[Match(wm_class=["Thunderbird"])]),
    Group("music", matches=[Match(title="ncmpcpp")]),
    Group("win7", matches=[Match(wm_class=["virtualbox"])]),
    Group("steam", matches=[Match(wm_class=["Steam"])])
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
                                       fallback=layout.Stack(stacks=1,
                                                             **border_args))),

    # a layout for pidgin
    layout.Slice('right', 256, name='pidgin', role='buddy_list',
                 fallback=layout.Stack(stacks=1, **border_args)),

    # a layout for steam
    layout.Slice('right', 256, name='steam', role='Friends',
                 fallback=layout.MonadTall(stacks=1, **border_args))
    ]

# orange text on grey background
default_data = dict(fontsize=12,
                    foreground="FF6600",
                    background="1D1D1D",
                    font="ttf-droid")

date_conf = dict(fontsize=12,
                    foreground="FFFFFF",
                    background="1D1D1D",
                    font="ttf-droid")
screens = [
    Screen(
        # top=bar.Bar(
        #     [
        #         # Powerline(timeout=2)
        #     ],
        #     30
        # ),
        bottom=bar.Bar(
            [
                widget.GroupBox(**default_data),
                widget.WindowName(**default_data),
                widget.TextBox(**default_data),
                widget.Systray(**default_data),
                widget.Volume(**default_data),
            ],
            30,
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(**default_data),
                widget.WindowName(**default_data),
                widget.TextBox(**default_data),
                widget.Systray(**default_data),
                widget.Volume(**default_data),
            ],
            30,
        ),
    )
]

main = None
follow_mouse_focus = True
cursor_warp = False
floating_layout = layout.Floating()

# Mouse

# mouse = (
#     # Drag([mod], 'Button1', lazy.window.set_position_floating(),
#     #     start=lazy.window.get_position()),
#     # Drag([mod], 'Button3', lazy.window.set_size_floating(),
#     #     start=lazy.window.get_size())
# )

bring_front_click = True
auto_fullscreen = True
widget_defaults = {}


def is_running(process):
    # s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
    s = subprocess.Popen(["pgrep", process], stdout=subprocess.PIPE)
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
    execute_once("steam")
    execute_once(["urxvtc", "-e", "ncmpcpp"])
    execute_once(['xsetroot', '-cursor_name', 'left_ptr'])
