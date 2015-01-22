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

plugins=(cp pip lol git git-extras archlinux tmux tmuxinator common-aliases \ 
         catimg systemd fasd vi-mode)

source $ZSH/oh-my-zsh.sh

# vi-mode binds { 
    bindkey '\e[A' history-beginning-search-backward
    bindkey '\e[B' history-beginning-search-forward
    bindkey '^p' history-beginning-search-backward
    bindkey '^n' history-beginning-search-forward

    bindkey '^?' backward-delete-char
    bindkey '^h' backward-delete-char
    bindkey '^w' backward-kill-word
    bindkey '^r' history-incremental-search-backward
# }

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
    export TERM='screen-256color'
    export PAGER=/usr/bin/vimpager

    # append third-party program binaries to PATH
    
    # get latest gem folder
    gembindirs=(/home/finalfortune/.gem/ruby/*/bin)
    export PATH=$PATH:/home/finalfortune/bin:$gembindirs[-1]

    # Aliases {
        alias pgrep="pgrep -a"
        alias grep="grep -i"
        alias man="man --pager=_man2vim"
        alias less=$PAGER
        alias zless=$PAGER
    # }

# }

# USER PROGRAM START-UPS { 
    . /usr/share/zsh/site-contrib/powerline.zsh

    # welcome message
    archey
# }
