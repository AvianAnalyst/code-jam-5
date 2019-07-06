import pygame as pg

from project.constants import BG_MUSIC, SOUNDS_BUTTONS as SND
from project.utils.user_data import UserData


user_data = UserData()


class Sound:
    """Represents all sounds and settings for the UI."""

    pg.mixer.pre_init(44100, -16, 2, 2048)
    pg.mixer.init()
    pg.mixer.music.set_volume(0)
    pg.mixer.music.load(str(BG_MUSIC))
    pg.mixer.music.play(-1)

    click = pg.mixer.Sound(str(SND["click3"]))
    check = pg.mixer.Sound(str(SND["switch1"]))
    task_completed = pg.mixer.Sound(str(SND["twoTone2"]))
    task_failed = pg.mixer.Sound(str(SND["phaserUp1"]))

    @staticmethod
    def update():
        """Updates the volume of the sounds and music."""
        # edit the volume to be in 0.0 - 1.0 range
        vol = user_data.volume / 100

        Sound.click.set_volume(vol)
        Sound.check.set_volume(vol)
        Sound.task_completed.set_volume(vol)
        Sound.task_failed.set_volume(vol)
        pg.mixer.music.set_volume(vol / 6)
