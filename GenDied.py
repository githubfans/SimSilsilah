from Functions import SetDied
# from time import gmtime, strftime
import os


try:
    while True:
        SetDied()
        os.system('clear')
except KeyboardInterrupt:
    pass
