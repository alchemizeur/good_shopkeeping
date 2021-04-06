import sys                                      # needed for loading bar
from select import select
import termios
from time import sleep                          # Allows for timing delays
import itertools                                # for supacute cycling loading animations

### CHAPTERS
CH1_INTRO = """
╔╦╗╔═╗╦═╗╦╔╗╔╔═╗╔═╗
║║║╠═╣╠╦╝║║║║╠═╣╚═╗
╩ ╩╩ ╩╩╚═╩╝╚╝╩ ╩╚═╝"""
CH2_INTRO = """
╦  ╔═╗╔╗╔╔╦╗╦═╗╦╔═╗╦  
║  ╠═╣║║║ ║║╠╦╝║║╣ ║  
╩═╝╩ ╩╝╚╝═╩╝╩╚═╩╚═╝╩═╝"""
CH3_INTRO = """
╦╔═╦╔═╗╦  ╔═╗╔╗╔  ╔╦╗╦╦═╗╔═╗
╠╩╗║╠═╝║  ╠═╣║║║  ║║║║╠╦╝║╣ 
╩ ╩╩╩  ╩═╝╩ ╩╝╚╝  ╩ ╩╩╩╚═╚═╝"""
CH4_INTRO = """
╦ ╦╔╗╔╔╦╗╦╔╗╔╔═╗
║ ║║║║ ║║║║║║║╣ 
╚═╝╝╚╝═╩╝╩╝╚╝╚═╝
"""
CH5_INTRO = """
╔═╗╦  ╔═╗╦╔═╗
║╣ ║  ║ ╦║╚═╗
╚═╝╩═╝╚═╝╩╚═╝"""
CH6_INTRO = """
╦  ╔═╗╔╗╔╔═╗╔═╗╦═╗  ╔═╗╦═╗╔═╗╔═╗
║  ║/║║║║║ ╦╠═╣╠╦╝  ║ ╦╠╦╝║╣ ║╣ 
╩═╝╚═╝╝╚╝╚═╝╩ ╩╩╚═  ╚═╝╩╚═╚═╝╚═╝"""

## turn this into a dictionary eventually
shopkeeper_1 = 'Marinas'
shopkeeper_1_short = 'Mari'
shopkeeper_2 = 'Landriel'
shopkeeper_2_short = 'Lando'
shopkeeper_3 = 'Kiplan Mire'
shopkeeper_3_short = 'Kip'
shopkeeper_4 = 'Undine'
shopkeeper_5 = 'Elgis'
shopkeeper_6 = 'Løgnar Gree'
shopkeeper_6_short = 'Løgnar'

### FORMATTING
def rgb( msg, r, g, b ):
    return f'\033[38;2;{r};{g};{b}m{msg}\033[0m'
#    color = Color()
#    color.("hello", 255, 0, 0)

def formatting(msg,format):
    if format == 'italics':
        format = "\033[3m"
    elif format == 'bold':
        format = '\033[1m'
    elif format == 'underline':
        format = '\033[4m'
    return f'{format}{msg}\033[0m'

formatting("blah",'italics')

### PROGRESS BAR

def progress_bar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write("%s╟%s%s╢ %i/%i\r" % (prefix, "█" * x, "░" * (size - x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()


def termset_noecho(func):
    def wrapped(*args, **kwargs):
        fd = sys.stdin.fileno()
        new_term = termios.tcgetattr(fd)
        old_term = termios.tcgetattr(fd)

        # New terminal setting unbuffered
        new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

        try:
            termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)
            func(*args, **kwargs)
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)
    return wrapped


@termset_noecho
def running_print(msg):
    for i, char in enumerate(msg):
        print(char, end='')
        sys.stdout.flush()
        dr, _dw, _de = select([sys.stdin], [], [], 0.07)
        if dr:
            break
    print(msg[i+1:], end='')
    sys.stdout.flush()


#for i in progressbar(range(15), "Loading: ", 40):
#    time.sleep(0.1)  # any calculation you need

shopkeeper_names = ['Landriel', 'Kiplan', 'Kip', 'Marinas', 'Undine', 'Elgis', 'Lojnar']
name_commentary = ['You must not be from around here.', 'That has a nice ring to it.', 'That\'s a fun name.', "I believe I had a cousin by that name. An odd one.", "That name reminds me of a story I heard once.", "The name of a real warrior.", "A splendid choice for a name.", "An interesting name. Filled with valor and mystery.","I could not think of a more fitting name for you.","Now that is a name worth being revered.","That is a name that will sound splendid in a bard's melody."]
