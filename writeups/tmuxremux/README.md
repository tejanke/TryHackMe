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