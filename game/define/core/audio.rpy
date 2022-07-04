define config.fade_music = 1.0

init:
    init python:
        renpy.music.register_channel("ambience", "sfx")
        renpy.music.register_channel("extra_ambience", "sfx")
