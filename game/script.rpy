# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define host = Character("Dannie", who_color="#C9A362")
define guest = Character("Karina", who_color="#A975AC")
define friend = Character("Darcy", who_color="#629A18")
define unknown = Character("<Unknown>", who_color="#E500FF")

# The game starts here.

label start:
    "How long will I keep failing...?"

    "Why am I even doing this to myself...?"

    scene bg guestroom

    show guest sitting frustrated at left with hpunch
    guest "...Ugh! Not again!"

    "This stupid ledge again! I swear, they should perform tests for sadistic tendencies on every level designer. Or maybe they do, and that's exactly how they hire them."

    show guest sitting
    "I think I'll just go to sleep. Wait... oh no... the exam, I completely forgot about it! Well, it's too late to prevent that! I might as well actually beat this level, at least."
    "And I feel like I'm forgetting something else, too..... oh! That shelter volunteer work [friend] invited me to."

    show guest sitting determined
    guest "Alright, I got this!"

    "Just one more try and I'll go to sleep and reply to her tomorrow."
    "It's been, how long... a few days already? And what was that shelter called, again? FPS... FPS...something... hmm, ironic acronym, isn't-"

    show guest sitting frustrated with hpunch
    show guest sitting frustrated
    guest "AAAAA!"

    show guest sitting
    "Okay, this time I was just distracted. I think I deserve one more try."

    "..."

    show unknown sitting at right with vpunch
    unknown "{b}<PING>{/b}"

    show guest sitting nervous
    "Oh, no, [friend]'s on to me, isn't she..."

    hide unknown
    "I can't just interrupt my flow right now, though..."

    "..."

    show guest sitting frustrated with hpunch
    guest "AAAAA!"

    "Not again! I guess I don't got this, after all. I give up."

    show unknown menacing with vpunch
    unknown "{b}<PING>{/b}"

    "Hmm. I should just tell [friend] I'd love to go but I'm too busy. I have so much work and studying to do these days. I really hope she isn't mad at me for ghosting her, at least."

    hide unknown
    show host sitting at right
    unknown "> {i}Hi [guest]{/i}\n> {i}Sorry, you're probably asleep...{/i}"

    show guest sitting
    "Phew, it's just [host]. It's been a while..."

    show guest sitting smirk
    guest "> {i}sup{/i}\n> {i}and dw, when was the last time i was even asleep at this time? it's only 1am{/i}"

    "{b}<The conversation progresses until [host] mentions something that's troubling her and Guest presses on it>{/b}"

    "{b}<Also, it may be unusual for [host] to be awake at 1am, in which case [guest] should take note of that and ask her why she's up so late>{/b}"

    jump act2

label act2:
    scene bg entrance
    with Dissolve(.5)
    pause .5

    show guest armor at left

    show host armor at right

    "{b}<The background is an oasis>{/b}"
    guest "{b}<Asks [host] a question about what she's doing right now>{/b}"
    host "{b}<Talks about something she's doing in order to cope>{/b}"
    "{b}<[guest] reflects on this place>{/b}"
    "{b}<The oasis is supposed to represent her temporary sense of relief, so there should be a way to show that...>{/b}"

    "{b}<A transition from the present to [host]'s past>{/b}"

    "{b}<They go to a somewhat lively, but more dusty, town, with all faces being collages of facial parts, like {a=https://static.wikia.nocookie.net/grim-fandango/images/3/36/Land_of_the_Living_exterior.png/revision/latest?cb=20150216003752}here{/a}>{/b}"
    guest "{b}<Asks [host] a question about something from her past that's related>{/b}"
    host "{b}<Answers, and they talk back and forth a little, perhaps>{/b}"
    "{b}<[guest] reflects on this place, too>{/b}"

    "{b}<A transition from the past to how [host] feels about it>{/b}"

    "{b}<They walk along upside-down stairs; The Forger of Smiles corpse is visible behind them>{/b}"
    host "{b}<Talks about how she has kept a secret about her severe mood swings and her vain attempts to quell them>{/b}"
    "{b}<[guest] reflects on this place, too>{/b}"

    "{b}<[guest] asks a question that lead her to find out about a major source of [host]'s torment - her regret and shock about her young self accidentally killing a cat she loved, and/or one that died recently, for the loss of which no drugs have been able to help>{/b}"
    "{b}<There can also be a bit about [host]'s sister/cousin being cruel to animals>{/b}"
    "{b}<If there is a cat, it can also appear as a twisted but cute character>{/b}"

    jump act3


label act3:
    scene bg beach
    with Dissolve(.5)
    pause .5

    show guest armor at left

    show host armor at right

    host "..."

    show host almostnaked

    host "{b}<Talks about something she agonizes about and cries; *takes some armor off*>{/b}"

    show host naked

    host "{b}<Talks about something she agonizes about and cries; *takes the rest of her armor off*>{/b}"

    guest "L-lewd!"

    host "It's ok, this is marked as an NSFW game, I think."

    show host molten

    host "Anyway, where was I... AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa *melts*"

    guest "{b}<Stays quiet, afraid of saying something wrong; she looks away and reflects on what has just happened>{/b}"

    host " > Sorry, I didn't want to bother you with this...\n > It's already 3am, sorry for keeping you up"

    scene black
    with Pixellate(.5, 5)
    pause .5

    "No, {b}I{/b} am sorry..."

    guest " > wait\n > are you still there?"

    "{b}Not sure how to show this, but [host] sees [guest]'s messages and continues talking to her, giving her a chance to prove that she did care about [host]'s wellbeing despite appearing not to care when she broke down.. and something else - I forgot what{/b}"

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
