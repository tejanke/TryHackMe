# Room
https://tryhackme.com/room/tmuxremux

# Task 1 - Deploy VM
Deploy

# Task 2 - Starting sessions
* tmux
* rename session : ctrl+b+shift+$
* rename session in session : ctrl+b+ctrl+b+shift+s
* start named session : tmux new -s thm
* start session in session: tmux new -s thm -d
* swap sessions : ctrl+b+s
* list all active sessions : tmux ls
* detatch from session : ctrl+b+d
* attach to session : tmux attach -t thm
* kill session : tmux kill-session -t thm
* kill all but specific session: tmux kill-session -t notme -a
* change default new session dir: ctrl+b+shift+:
  * attach -c /new/dir

# Task 3 - Manage tmux panes
* split pane in two horizontally: ctrl+b+shift+"
* split pane in two vertically: ctrl+b+shift+%
* close selected pane: exit
* move to another pane: ctrl+b+arrow key
  * or: ctrl+b+o
* swap between most used panes: ctrl+b+;
* force kill current pane: ctrl+b+x+y
* move through panes clockwise: ctrl+b+shift+}
* move through panes counter-clockwise: ctrl+b+shift+{
* predefined layouts: ctrl+b+esc+1-5
* cycle through predefined layouts: ctrl+b+spacebar
* check pane numbers: ctrl+b+q
* move panes to other locations: ctrl+b+shift+:
  * swap-pane -s [destination_number] -t [source_number]
  * pane numbers start at 0 and are numbered clockwise
  * you can also reverse this, -t [source_number] -s [destination_number]