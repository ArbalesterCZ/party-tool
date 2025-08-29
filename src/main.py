from players import Players
from gtts import gTTS
from termcolor import colored

import playsound
import re


def sound(message: str, lang='cs', filepath='/tmp/voice.mp3') -> None:
    tts = gTTS(text=re.sub(r'\x1b\[[0-9;]*m', '', message), lang=lang)
    tts.save(filepath)
    playsound.playsound(filepath)

players = Players()
players.show([print])

while True:
    print(f'\n{colored('+', 'green')} to add text to speech effect.')
    command = input(f'{colored('E', 'green')}xit {colored('V', 'green')}ersus {colored('F', 'green')}ree4All {colored('G', 'green')}roups[{colored('1', 'green')}]: ').lower()

    if command.startswith('+'):
        processes = [print, sound]
    else:
        processes = [print]

    if 'e' in command:
        exit()
    elif 'v' in command:
        players.versus()
    elif 'f' in command:
        players.free_for_all()
    elif 'g' in command:
        try:
            players.groups(int(command.split('g', 1)[1]))
        except Exception as e:
            players.groups(1)

    players.show(processes)
