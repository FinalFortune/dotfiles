# MODELINE {
# vim: set foldmarker={,} foldlevel=0 foldmethod=marker:
# }

# OH MY ZSH {

# Path to oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

ZSH_THEME="crunch"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

plugins=(git archlinux tmux tmuxinator common-aliases vundle systemd fasd)

source $ZSH/oh-my-zsh.sh

# }

# CUSTOM FUNCTIONS {

# list directory contents after changing directory
function cd()
{
    builtin cd "$*" && ls
}

# }

# ENVIRONMENT CONFIGURATION {

    export EDITOR='vim'

    # append third-party program binaries to PATH
    export PATH=/home/finalfortune/.gem/ruby/2.1.0/bin:$PATH

    # Aliases {
        alias pgrep="pgrep -a"
        alias grep="grep -i"
    # }

# }

# USER PROGRAM START-UPS {

# MPD daemon start (if no other user instance exists)
[ ! -s ~/.config/mpd/pid ] && mpd ~/.config/mpd/mpd.conf

# welcome message
archey

# }
