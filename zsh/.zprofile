# MODELINE {
# vim: set foldmarker={,} foldlevel=0 foldmethod=marker:
# }

# MPD daemon start (if no other user instance exists)

if [[ -z $DISPLAY && $XDG_VTNR -eq 1 ]]
then
    [ ! -n "$(pgrep mpd)" ] && mpd ~/.config/mpd/mpd.conf
    # startx prompt {
        echo "starting X, press ESC to cancel or any other key to continue..."

        read -t 10 -n 1 key

        # if not escape pressed
        if [[ $key != $'\e' ]]
        then
            # xinit -nolisten tcp "$@"
            startx
        fi
    # }
fi
