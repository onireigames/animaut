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
    "Now I remember. It wasn't deja-vu after all. It's probably [friend]. No, it's {b}definitely{/b} [friend]!"
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
    guest " > {i}sup{/i}\n > {i}it's been a while{/i}\n > {i}and dw, it's only 2am{/i}"

    host " > {i}Oh, sorry, I forgot about your sleep schedule{/i}\n > {i}Or lack thereof?{/i}"

    guest " > {i}at least i follow my nonexistent sleep schedule{/i}\n > {i}arent {b}you{/b} supposed to be asleep?{/i}"
    host " > {i}Yeah{/i}"

    guest " > {i}need help with something?{/i}"
    host " > {i}No{/i}"
    guest " > {i}dont tell me you forgot to study too{/i}"
    "Who am I kidding?! If there's anyone crazy enough to prepare weeks in advance, it's her."

    guest " > {i}bored?{/i}"
    show guest sitting
    "I wish. Even if she were, she only plays slow-paced games like Meow Meadow. I don't get what she sees in them."

    host " > {i}No{/i}"
    "This isn't like her at all. At least she didn't notice my slip-up about being a delinquent who doesn't study. Or she's just used to it by now..."
    show guest sitting nervous
    host " > {i}Sorry for distracting you, forget about this.{/i}\n > {i}Goodnight!{/i}"

    guest " > {i}...{/i}"
    show guest sitting frustrated
    guest " > {i}goodnight my ass{/i}\n > {i}youre not going to sleep till youve told me whats up{/i}"

    show guest sitting nervous
    host " > {i}I just felt like I was dying. I wasn't thinking straight because I had just woken up.{/i}"
    guest " > {i}and you messaged me instead of calling an ambulance?{/i}"

    host " > {i}I wasn't actually dying! I only had to calm down.{/i}"
    show guest sitting
    "I'm glad..."
    guest " > {i}i was your go-to option for calming down?{/i}"
    show guest sitting smirk
    guest " > {i}why dont you just marry me then?{/i}"
    show guest sitting nervous
    guest " > {i}jk jk{/i}"
    "What am I doing?! This isn't the time to joke around."

    show guest sitting
    host " > {i}Sorry if it's like I was using you or something{/i}\n > {i}I tried everything else before that{/i}"

    scene bg black
    with Dissolve(.5)
    pause 1
    guest " > {i}everything else?{/i}"

    jump act2

label act2:
    host "Everything else - I close my eyes..."

    scene bg entrance
    with Dissolve(.5)
    pause .5

    show guest armor at left

    show host armor at right

    "{b}<The background is an oasis - a park, surrounded by a desert>{/b}"
    host "...I breathe slowly, and imagine I'm in a nice place with trees. I'd play some ambient sounds too if I could do that quickly enough."

    "{b}<The oasis dissolves, revealing a barren landscape>{/b}"
    host "But it wasn't enough this time... so I wanted to talk to you."
    guest "Why me?"
    host "You were the only one who was awake at this time."
    "I can't argue with that..."
    guest "Alright, makes sense."

    guest "{b}<Asks [host] a question about what she's doing right now>{/b}"
    host "{b}<Talks about something she's doing in order to cope - actually probably only talking to [guest]>{/b}"
    "{b}<[guest] reflects on this place>{/b}"

    "{b}<A transition from the present to [host]'s past>{/b}"

    "{b}<They go to a somewhat lively, but more dusty, town, with all faces being collages of facial parts, like {a=https://static.wikia.nocookie.net/grim-fandango/images/3/36/Land_of_the_Living_exterior.png/revision/latest?cb=20150216003752}here{/a}>{/b}"
    guest "{b}<Asks [host] a question about something from her past that's related>{/b}"
    host "{b}<Answers, and they talk back and forth a little, perhaps>{/b}"
    "{b}<[guest] reflects on this place, too>{/b}"

    "{b}<A transition from the past to how [host] feels about it>{/b}"

    "{b}<They walk along upside-down stairs; The Forger of Smiles corpse is visible behind them>{/b}"
    host "{b}<Talks about how she has kept a secret about her severe mood swings and her vain attempts to quell them>{/b}"
    "{b}<[guest] reflects on this place, too>{/b}"

    scene bg black
    with Dissolve(.5)
    pause .5

    "{b}<Image of [guest]'s hand reaching in near-darkness, with only some outlines being visible>{/b}"
    "{b}<[host] has a sister who was cruel to animals, especially cats, and never got punished for it>{/b}"
    "{b}<The two discuss how cute cats are and how animals are treated unjustly by people who should know better{/b}"
    "{b}<While feeling around, [guest] feels a cat, which slowly becomes visible in her view>{/b}"

    jump act3


label act3:
    scene bg beach
    with Dissolve(.5)
    pause .5

    show guest armor cat at left
    "{b}<The cat [guest] is holding is more grotesque than what she imaged>{/b}"

    show host armor at right

    "{b}<[guest] asks a question that leads her to find out about a great source of [host]'s torment - a shocking event which happened a long time ago>{/b}"
    "{b}<While digging in a compost pile at the countryside, [host] heard a squeak - there was a litter of mice inside, all of whom except one were eviscerated by her actions>{/b}"
    "{b}<Nursed the lone survivor, Beep - a blind and tiny mouse pup - back to life: gave it special milk with no lactose, kept it warm throughout the cold winter>{/b}"
    "{b}<However, one fateful day, the mousey jumped out of its box and [host], worried her cat would get to the mouse before her and eat it, accidentally stepped on the mousey>{/b}"
    "{b}<The mouse was barely alive, and had to be given a mercy killing>{/b}"
    "{b}<While [host] is talking about this, her armor falls apart and she melts>{/b}"

    scene black
    with Pixellate(.5, 5)
    pause .5
    guest "{b}<Stays quiet, afraid of saying something wrong; she looks away and reflects on what has just happened>{/b}"

    host " > {i}Sorry, I didn't want to bother you with this...{/i}\n > {i}It's so late, sorry for keeping you up{/i}"

    "Why is she sorry?! {b}I{/b} should be sorry for being so quiet."

    "Idiot! You're leaving her hanging like this?!"

    "I just don't know what to say..."

    pause 1
    guest " > {i}wait{/i}"

    pause 3
    "No reply..."

    jump act4


label act4:
    scene bg guestbed
    with Pixellate(.5, 5)
    pause .5

    "{b}<[guest] is in her bed, her face too dark to see, and a digital clock showing that it's now 5am, and a lit phone beside her>{/b}"
    "No matter how many times I check, it won't make her reappear."
    "Any rational person would just go to sleep, not spend 2 hours waiting for nothing like an idiot."

    scene bg guestlandscape
    with Dissolve(.5)
    pause .5

    "{b}<[guest] is seen lying on her rock with her blindfold in her hand, crying with her eyes open and a blank stare>{/b}"
    "{b}<[guest]'s pose matches the previous background perfectly>{/b}"
    "I can't sleep like this."

    scene bg guestlandscapereach
    with Dissolve(.5)
    pause .5
    "{b}<A close view of [guest]'s arm reaching into the murky water>{/b}"
    guest " > {i}are you still there?{/i}"
    guest " > {i}well, obviously not{/i}\n > {i}but i dont know what else to do{/i}"
    "I don't even know what I'm doing."
    guest " > {i}sorry im such an idiot{/i}"

    pause 1
    "Well, okay, I do know what I'm doing - one of those things you tend to regret in the morning when you can think clearly."

    pause 3
    "{b}<The background changes to [host]'s arm reaching out from under the water and grabbing [guest]'s forearm firmly>{/b}"
    host " > {i}Hi{/i}" with vpunch
    pause 1
    "{b}<The background changes yet again, to [host]'s other arm doing the same>{/b}"
    host " > {i}Can we talk?{/i}" with vpunch

    scene black
    with Dissolve(.5)
    pause .5

    guest " > {i}youre still up?!{/i}\n > {i}but yes, please, let's talk{/i}"

    "{b}<The background is something abstract, maybe a bunch of watery colours, and melting clocks (à la Salvador Dali)>{/b}"
    "{i}I don't even know how much time we spent talking, but she fell asleep a little after the sun had risen{/i}"

    "{b}<The background is now them sitting on the rock, which now is surrounded by land (the water level has lowered), and [guest] is being [host]'s lap pillow and petting her hair>{/b}"
    guest "Sleep well - or at least as well as you possibly can after pulling an all-nighter."
    guest "And, by the way..."
    guest " > {i}when you wake up - theres something you might be interested in... c;{/i}"

    jump act5


label act5:
    scene bg guestlandscape
    with Dissolve(.5)
    pause .5

    "{b}<The background is Fox Peak Sanctuary - a nonprofit which rescues foxes>{/b}"
    show friend at right
    friend "Oh, you both made it! Welcome to Fox Peak Sanctuary!"

    show guest at center
    guest "Hello."

    show host at left
    host "Hi!"

    "{b}<They discuss some stuff about what they're supposed to do there for the animals>{/b}"
    "{b}<Or perhaps they brought some money and got to see first-hand how professionals do their work and maybe were taught a few things about caring for animals there>{/b}"

    scene bg guestlandscape
    with Dissolve(.5)
    pause .5

    "{b}<The background is a close-up of [host] and [guest] h*ndholding - I mean such a close-up that their hands cover half of the foreground>{/b}"
    host ""
    guest "By the way..."

    scene bg black
    with Dissolve(.5)
    pause 2
    guest "Does Meow Meadow have multiplayer support?"

    return
