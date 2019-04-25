# ping-logging

## Requirements
- you have to install the Python module "pyping" before running the code using (sudo) pip install pyping

## How to use the code
For automatic ping logging, you have to add the script to the crontab (when working on Linux) typing "crontab -e" into the terminal and adding the line "*/1 * * * * python [path_to_script]" at the bottom.
In my case, this is "*/1 * * * * python ~/pingcheck.py" which executes the script every minute. This writes the current ping into a logfile every minute.
