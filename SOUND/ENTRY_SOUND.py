import time
import winsound


def entry_sound():
    freq = 1000
    dur = 2000
    winsound.Beep(freq, dur)
    time.sleep(1)
    winsound.Beep(freq, dur)
