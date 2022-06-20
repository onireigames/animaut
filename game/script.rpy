# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define host = Character("Dannie")
define guest = Character("Karina")
define friend = Character("Darcy")
define unknown = Character("<Unknown>")

# The game starts here.

label start:
    "For how long will I keep failing...?"

    "Why am I even doing this to myself...?"

    scene bg guestroom

    show guest sitting_frustrated at left with hpunch
    guest "...Ugh! Not again!"

    "This stupid ledge again! I swear, they should perform tests for sadistic tendencies on every level designer. Or maybe they do, and that's exactly how they hire them."

    show guest sitting_normal
    "I think I'll just go to sleep. Wait... oh no... the exam, I completely forgot about it! Well, it's too late to prevent that! I might as well actually beat this level, at least."
    "And I feel like I'm forgetting something else, too..... oh! That shelter volunteer work [friend] invited me to."

    guest "Alright, I got this!"

    "Just one more try and I'll go to sleep and reply to her tomorrow. I'd reply to her now but I'd rather she didn't see a rogue message from me this late at night."
    "It's been, what... a few days already? And what was that shelter called, again? FPS... FPS...something... hmm, ironic acronym, isn't-"

    show guest sitting_frustrated with hpunch
    show guest sitting_frustrated
    guest "AAAAA!"

    show guest sitting_normal
    "Okay, this time I was just distracted. I think I deserve one more try."

    "..."

    show host sitting_unknown at right
    unknown "{b}<PING>{/b}"

    show guest sitting_normal
    "Oh, no, [friend]'s on to me, isn't-"

    show guest sitting_frustrated with hpunch
    hide host
    guest "AAAAA!"

    "Not again! Alright, I give up."

    show host sitting_unknown at right
    unknown "> {i}Hi [guest]{/i}\n> {i}Sorry, you're probably asleep...{/i}"

    show host sitting
    "Whew, it's just [host]. It's been a while..."

    guest "> {i}sup{/i}\n> {i}and dw, when was the last time i was even asleep at this time? it's only 1am{/i}"

    "{b}<The conversation progresses until Host mentions something that's troubling her and Guest presses on it>{/b}"

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

    hide guest
    show host pickedup
    guest "oof..."

    host "..."

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

    guest "Oh, by the way, there's something you might be interested in..."

    jump act5


label act5:
    # TODO: Actually should be the FPS (Fox Peak Sanctuary)
    scene bg guestlandscape
    with Dissolve(.5)
    pause .5

    show friend at center
    friend "Oh, you both made it! (Even you, [guest]!) Welcome to Fox Peak Sanctuary!"

    show guest at left
    show host at right

    guest "Oh, shut up!"

    host "A."

    return
