"""
This is a docker "shell" that I created when I was having issues getting a docker container running.
"""

import os

container_name = "hadoop"

while(True):
    try:
        command: str = input("> ")
        if command == "\x04" or command == "q":
            exit()
        command = f"docker exec -it ${container_name} " + command
        os.system(command)
    except KeyboardInterrupt:
        print()
        continue