Create a .desktop file in preferred location. 
This is typically: ```/usr/share/applications/``` or ```/home/usr/.local/share/applications/```
Example .desktop file:
```
[Desktop Entry]
Type=Application
Version=0.0.1
Name=dice_rolling
Comment=Python based CLI for rolling dice
Exec=/home/usr/code/dice_rolling/dice_rolling.sh
Terminal=true
Categories=Utilites;Games
TerminalOptions=\s--noclose
```
Make sure the .desktop and .sh files are executable.