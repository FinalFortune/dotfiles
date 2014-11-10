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

plugins=(git archlinux tmux tmuxinator common-aliases vundle systemd fasd vi-mode)

source $ZSH/oh-my-zsh.sh

bindkey '^P' up-history
bindkey '^N' down-history
bindkey '^?' backward-delete-char
bindkey '^h' backward-delete-char
bindkey '^w' backward-kill-word
bindkey '^r' history-incremental-search-backward

function zle-line-init zle-keymap-select {
    VIM_PROMPT="%{$fg_bold[yellow]%} [% NORMAL]%  %{$reset_color%}"
    zle reset-prompt
}

zle -N zle-line-init
zle -N zle-keymap-select
export KEYTIMEOUT=1
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
    export TERM='xterm-256color'

    # append third-party program binaries to PATH
    export PATH=$(pwd)/../bin:/home/finalfortune/.gem/ruby/2.1.0/bin:$PATH

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
