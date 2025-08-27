from players import Players
from gtts import gTTS
from termcolor import colored

import playsound
import re


def sound(message, lang='cs', filepath='/tmp/voice.mp3'):
    tts = gTTS(text=re.sub(r'\x1b\[[0-9;]*m', '', message), lang=lang)
    tts.save(filepath)
    playsound.playsound(filepath)


players = Players()
players.process([print])

while True:
    print(f'\n{colored('+', 'green')} to add sound effect.')
    command = input(f'{colored('E', 'green')}xit {colored('O', 'green')}rder {colored('V', 'green')}ersus {colored('F', 'green')}ree4All {colored('G', 'green')}roups→[count]: ').lower()

    if '+' in command:
        processes = [print, sound]
    else:
        processes = [print]

    if command.startswith('e'):
        exit()
    elif command.startswith('o'):
        players.order()
    elif command.startswith('v'):
        players.versus()
    elif command.startswith('f'):
        players.free_for_all()
    elif command.startswith('g'):
        try:
            players.groups(int(command.split("→", 1)[1]))
        except Exception as e:
            print(e)
            players.groups()

    players.process(processes)
