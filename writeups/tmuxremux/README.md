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

# Task 4 - Manage tmux windows
* windows are like a terminal tab
* create new window: ctrl+b+c
* change window name: ctrl+b+,
* detach pane into its own window: ctrl+b+shift!
* cycle to next window: ctrl+b+n
* cycle to previous window: ctrl+b+p
* list windows to cycle to: ctrl+b+w
* kill window: ctrl+b+shift+&+y
* join windows/panes: ctrl+b+shift+:
  * join-pane -s [source_window_name]
  * join-pane -t [destination_window_name]
  * add an -v to fuse veritcally
  * add an -h to fuse horizontally

# Task 5 - Copy mode
* Can be used to scroll up and down the page
* start copy mode: ctrl+b+[
* exit copy mode: q
* search up: ctrl+r
* continue search: hold ctrl, press r
* resume scrolling: press enter
* search down: ctrl+s
* to copy and paste:
  * ctrl+b+[
  * scroll to start of block of text
  * ctrl+spacebar to enable highlighting, then highlight
  * copy highlighted text with alt+w
  * paste: ctrl+b+]
* check what is in clipboard: ctrl+b+shift+#

# Task 6 - tmux and beyond
* show tmux config defaults: tmux show -g
* save config in /home/username directory
* save config with name .tmux.conf
* config file options
  * status bar color: set -g status-style bg='#443311',fg='223344'
  * selected window color: set -g window-status-current-style fg=black,bg=white
  * set a different prefix: set -g prefix C-a
  * use script on right: set -g status-right " #[fg="red,bold"]#(~/script.sh) "
  * variables
    * #H : hostname
    * %H:%M : hour and minutes on the clock
    * %d-%b-%y : day, month, year
  * change copy mode hotkeys to vim: set -g mode-keys vi
  * load plugin: set -g @plugin 'dir/plugin-name'
* reload config file: ctrl+b+shift+:
  * source-file /home/username/.tmux.conf
  * source-file ~/.tmux.conf
* reset config: tmux kill-server
* run plugin after loading it: run-shell


Resources
* tmux plugins: https://github.com/tmux-plugins/
* usable config: https://www.hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/
* config examples: https://www.golinuxcloud.com/tmux-config/
* config examples: https://arcolinux.com/everything-you-need-to-know-about-tmux-plugins-manager/
* config examples: https://www.barbarianmeetscoding.com/blog/jaimes-guide-to-tmux-the-most-awesome-tool-you-didnt-know-you-needed

# Task 7 - Conclusion
Conclusion