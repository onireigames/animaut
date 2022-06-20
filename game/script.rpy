# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define host = Character("Host")
define guest = Character("Guest")

# The game starts here.

label start:

    scene bg guestroom

    show guest chatting at left

    "Chatting..."

    guest "sup"

    show host unknown at right

    host "nm"

    guest "lies"

    host "ok fine i'll explain"

    jump act2

label act2:
    scene bg entrance
    with Dissolve(.5)
    pause .5

    show guest armor at left

    show host armor at right

    guest "Cool place..."

    host "Blah blah... (talking about the place)"

    guest "Blah blah blah... (commenting on it)"

    "Hmmmmm... (guest's unsaid thoughts about the place)"

    "Etc. etc."

    jump act3


label act3:
    scene bg beach
    with Dissolve(.5)
    pause .5

    show guest armor at left

    show host armor at right

    host "..."

    show host almostnaked

    host "aaaaAAAAAA *takes some armor off*"

    show host naked

    host "AAAAAAAAAAAAAAAA *takes the rest of the armor off*"

    guest "L-lewd!"

    host "It's ok, this is marked as an NSFW game, I think."

    show host molten

    host "Anyway, where was I... AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa *melts*"

    guest "oof..."

    host "..."

    hide guest
    show host pickedup

    scene black
    with Pixellate(.5, 5)
    pause .5

    "It's only fair if I do the same..."

    jump act4


label act4:
    scene bg guestlandscape
    with Pixellate(.5, 5)
    pause .5

    show guest holdhost at center

    host "A."

    guest "A."

    return
