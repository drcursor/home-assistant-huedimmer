# home-assistant-huedimmer

home-assistant-huedimmer python helper script that polls a philips hue bridge and makes a call to home assistant's API whenever a button press is detected.

## How to use
- Script must be run permanently, use something like supervisord to make sure it stays alive
- Add your settings to the CONFIG area of the script
- Define the actions inside the while script (there are 4 examples there)
