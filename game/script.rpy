# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define host = Character("Dannie", who_color="#C9A362")
define guest = Character("Karina", who_color="#A975AC")
define friend = Character("Darcy", who_color="#629A18")
define unknown = Character("<Unknown>", who_color="#E500FF")

# The game starts here.

label start:
    "{b}<MUSIC: Vague ambient sounds that give a sense of emptiness>{/b}"

    "{b}<An image of [guest]'s inner landscape - her sitting or lying on a rock in the middle of the ocean, like the rocks around Scarborough shoal>{/b}"
    "How long will I keep failing...?"
    "Why am I even doing this to myself...?"
    "{b}<A close-up image of her>{/b}"
    "I just need some time to reflect..."

    scene bg guestroom
    with Dissolve(1)

    "{b}<MUSIC: Chill, either with a fast and light bass melody or something that emulates the same feel, think {a=https://youtu.be/ZZ-mtVyjBqI}this{/a} or perhaps the chill tracks from {a=https://youtu.be/5-K8R1hDG9E}here{/a}>{/b}"
    "Maybe I am a masochist after all."
    "At least this time it's going way better. I got this!"
    pause 1

    show guest sitting frustrated at left with hpunch
    guest "Ugh! Not again!"
    "...I don't got this."

    "This stupid ledge again! I swear, they should screen level designers for sadistic tendencies. Or maybe they do, and that's exactly how they hire them."

    show guest sitting smirk
    "Or maybe you just got too full of yourself, dumbass."

    show guest sitting
    "Anyway, I'm so done with this. I think I'll just go to sleep."

    pause 2
    show guest sitting nervous
    "Wait... oh no... how did I even forget there was an exam tomorrow?! I was supposed to be preparing for it."
    "Not to mention \"normal\" people get ready weeks in advance, not the day before."

    show guest sitting smirk
    "Well, it's too late for that! I might as well actually beat this level, at least."
    show guest sitting
    "And I feel like I'm forgetting something else, too. Maybe it's just a weird sense of deja-vu."

    show guest sitting determined
    guest "Alright, let's go! Last chance!"

    "It's muscle memory at this point, I can't possibly mess it up."
    show guest sitting
    pause 3
    show guest sitting frustrated
    show unknown sitting at right with vpunch
    unknown "{b}<PING>{/b}"

    show guest sitting
    "Oh no..."
    show guest sitting nervous
    "Oh no oh no oh no oh no oh no oh no oh no"
    "Now I remember. It's probably [friend]. No, it's {b}definitely{/b} [friend]!"
    show guest sitting despairing
    "That's what you get for not replying to her for at least a few days, especially about an invitation to such wholesome work. Idiot..."

    hide unknown
    show guest sitting frustrated
    "No, I can't just interrupt my flow right now. Focus!"

    pause 1
    show guest sitting
    "And what was that shelter called, again? FPS... FPS...something... hmm, ironic acronym, isn't it?"

    pause 2
    show guest sitting frustrated with hpunch
    guest "AAAAA!"

    "Not again! Okay, this time I was just distracted. I think I deserve one more try."

    show guest sitting nervous
    show unknown menacing with vpunch
    unknown "{b}<PING>{/b}"

    show guest sitting despairing
    "There's no escaping [friend] now, is there? I should just tell her I'd love to go but I'm too busy. I really do have so much work to do these days. I really hope she isn't mad at me for ignoring her, at least."

    show guest sitting nervous
    unknown "> {i}Hi, [guest]{/i}\n> {i}Sorry, you're probably asleep...{/i}"

    show guest sitting relieved
    show host sitting at right
    hide unknown
    "Phew, it's just [host]. I live to see another day!"

    show guest sitting smirk
    guest " > {i}sup{/i}\n > {i}it's been a while{/i}\n > {i}and dw, when was the last time i was even asleep at this time? it's only 1am{/i}"

    host " > {i}Oh, sorry I forgot about your sleep schedule{/i}\n > {i}Or lack thereof?{/i}"

    guest " > {i}{/i}"

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

    host "{b}<Is honest about something while smiling slightly and tearing up; *takes some armor off*>{/b}"

    show host naked

    host "{b}<Talks more, breaking down even more; *takes the rest of her armor off*>{/b}"

    guest "L-lewd!"

    host "It's ok, this is marked as an NSFW game, I think."

    show host molten

    host "Anyway, where was I... AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa *melts*"

    scene black
    with Pixellate(.5, 5)
    pause .5
    guest "{b}<Stays quiet, afraid of saying something wrong; she looks away and reflects on what has just happened>{/b}"

    host " > Sorry, I didn't want to bother you with this...\n > It's so late, sorry for keeping you up"

    "Why is she sorry?! {b}I{/b} am sorry."

    "Idiot! You're leaving her hanging like this?!"

    "I just don't know what to say..."

    guest " > wait\n > are you still there?"

    "{b}Not sure how to show this, but [host] sees [guest]'s messages and continues talking to her, giving her a chance to amend the situation... and something else - I forgot what{/b}"

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
