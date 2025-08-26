from players import Players
from gtts import gTTS

import playsound


def sound(message, lang='cs', filepath='/tmp/voice.mp3'):
    tts = gTTS(text=message, lang=lang)
    tts.save(filepath)
    playsound.playsound(filepath)


players = Players()
players.process([print])

while True:
    command = input('\n[+](Add Sound Effect...)\n[E]xit [O]rder [V]ersus [F]ree4All [G]roups→<count>: ').lower()

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
