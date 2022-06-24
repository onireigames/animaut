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
    "That's what you get for not replying to her for at least a few days, especially about an invitation to such a wholesome place. Idiot..."

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
    "I wish. Even if she were, she plays only slow-paced games like Meow Meadow. I don't get what she sees in them."

    host " > {i}No{/i}"
    "This isn't like her at all. At least she didn't notice my slip-up about being a delinquent. Or she's just used to it by now..."
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
    "{b}<The background is an oasis - a park, surrounded by a desert>{/b}"

    show guest armor at left
    show host armor at right
    host "...I breathe slowly, and imagine I'm in a nice place with trees. I'd play some ambient sounds too if I could do that quickly enough."

    "{b}<The oasis dissolves a little>{/b}"
    host "But it wasn't enough this time... so I wanted to talk to you."
    guest "Why me? Not that I mind."
    host "You were the only one who was awake at this time."
    "I can't argue with that..."
    guest "Alright, alright. So, what are you up to now? Going to sleep?"
    host "I started playing to help get my mind off some things."
    "{b}<There might be a transition into [guest]-o-vision - she's feeling around, sensing only a little part of this oasis>{/b}"
    "I don't even need to ask what she's playing. I can't relate, but if Meow Meadow is helping her calm down, maybe it's not so pointless after all."

    "{b}<The oasis dissolves completely, revealing a barren landscape>{/b}"
    host "But I shouldn't. I should go back to sleep."
    guest "Want to share those things you've been trying to stop thinking about first?"
    "{i}As if.{/i} Considering how little we've talked lately, I might as well be a stranger to her."
    host "Just some things from my past."
    guest "Oh, you've never talked to me about any of it before. It's funny how we've known each other for years and I still don't even know where you're from... and neither do you know much about me, actually."

    host "Well, my childhood wasn't anything special."
    "{b}<They go to a somewhat lively, but more dusty, town, with all faces being collages of facial parts, like {a=https://static.wikia.nocookie.net/grim-fandango/images/3/36/Land_of_the_Living_exterior.png/revision/latest?cb=20150216003752}here{/a}>{/b}"
    host "I grew up in {image=jumbletext.png}{alt}some village{/alt} until I started going to school and had to move."
    guest "Huh? I've never heard of {image=jumbletext.png}{alt}that village{/alt}, sorry."
    host "Yeah, it's just a remote village, sorry for not clarifying."
    guest "It wasn't anything special?! Maybe I'm just a naïve city kid, but I've love to live in a village."
    host "I guess so... there weren't many people, but that didn't bother me. The adults terrified me and I was too afraid to even hang out with the ones my age."
    host "There was one whom I clicked with, but she was from a city and had to go back soon afterwards."
    guest "Didn't you keep in touch with her?"

    host "I really wanted to. I could have written a letter to her..."
    "{b}<Maybe [host] takes her mask off while saying this>{/b}"
    host "I was too shy to ask my parents for help with that..."
    guest "That sucks..."
    "{b}<More [guest]-o-vision?>{/b}"
    "I knew she was the shy type, but that's something else... I don't know what to say to comfort her, though."

    host "And I definitely couldn't have asked my older sister."
    guest "Why not? Wait, you have a sister?! You've never told me about her."
    host "Sorry if I was secretive about that. I don't want to think about her. I don't trust her, honestly..."
    "{b}<They climb a spiral staircase, with some stuff in the background that represents her sister>{/b}"
    guest "What did she do?"
    "Maybe I'm asking her too much-"
    host "She never cared about others. Even worse..."
    host "When I was still a stupid little kid, I invited her to my secret hideout."
    "I don't like where this is going. Quick, change the topic! Just don't say anything..."
    guest "Oh, like an abandoned construction site? I loved hanging out at those. Well, maybe there aren't many of those in villages, I guess."
    "...stupid. Damn it."
    host "No, it was just a little shack next to a river. There was a cat - Mitzi - that I would play with and bring some food to."
    guest "Cute!"
    host "..."
    host "I was playing with my sister when suddenly, she decided to throw a rock straight at Mitzi while she was sleeping."
    guest "Oh... Was it an accident?"
    host "I used to hope for that too. But no, it was on purpose. She survived, but never fully recovered from this."
    pause 1
    host "Sorry, I'm talking too much."
    guest "No, it's fine. I want to know more, actually."
    "Well, that was selfish."
    host "There's nothing more to this. Thanks for listening... I think I feel better now."
    "Maybe my memory just sucks, but this has to be the first time I've heard her say \"thanks\" instead of \"sorry\"."
    guest "Just for the record - I'm not a licensed professional, you know."
    host "I've already been to therapy. It helped, and their prescription helped too."

    "{b}<They walk along upside-down stairs; The Forger of Smiles corpse is visible behind them>{/b}"
    host "At least for a while."
    "I feel a monolithic but dead presence."
    guest "There are all kinds of therapists. Some are better than others, or so I've heard at least. So, you might want to explore more."
    host "Maybe. But I thought I would get better over time, not worse."

    scene bg black
    with Dissolve(.5)
    pause .5

    "{b}<More [guest]-o-vision?>{/b}"
    "{i}You did your best, Forger of Smiles. But your best wasn't enough, was it?{/i}"
    guest "Have you forgiven your child self? There's nothing you could have done to prevent any of that. If anything, you probably handled everything better than present me would."

    jump act3


label act3:
    host "Maybe I've forgiven myself for that. But there's something I haven't said."

    scene bg beach
    with Dissolve(.5)
    pause .5

    show guest armor cat at left

    host "I'm a murderer..."
    "This has to be a joke."
    "But unlike me, she doesn't make such badly timed jokes."

    guest "How so? And I hope it's not too late to say this, but our conversation isn't encrypted."
    "What have I dragged myself into?!"
    host "It doesn't matter."
    guest "Look, I don't want you to say anything you'll regret in the morning. Let's just go to sleep."
    "As if I can sleep after this..."
    host "It was an accident. I was helping my grandparents out, digging into a compost pile."
    "Is she even listening? Also, compost pile?!"
    host "I heard some strange squeaking coming out of it. I didn't know what it was and didn't think too much of it. I was so stupid..."

    "{b}<Dark clouds gather in the background>{/b}"
    host "I kept digging despite it."
    "{b}<The clouds cover almost the whole sky>{/b}"
    host "I didn't know there were mice hidden there."
    "Mice?! In there?!"
    "{b}<It starts raining blood>{/b}"
    host "I still vividly remember how it looked. I don't want to remind myself of that moment, sorry. But, only one of them was left alive..."
    host "It was a pup that still couldn't even see."
    "{b}<She smiles a little, her armor is slowly falling apart, and there is a ray of light in the distance, and it isn't raining as much>{/b}"
    host "I took Beep inside, protected him from my cat, gave him special milk..."
    host "I even had to make sure he was warm because it was winter. Once, I panicked that he had frozen to death. I was sure he was a goner. He was alright, fortunately."
    host "After some time, he grew up and could finally see."
    "{b}<The ray of light starts disappearing and the rain increases in intensity again>{/b}"
    host "But then, he jumped out of his box and fell onto the floor."
    host "My first thought was that my cat would get to him, so I stepped back without looking..."
    "{b}<She melts with her armour gone, and the tide rises to her>{/b}"
    "I was prepared for the worst, but I don't know what to say even about this..."
    "I feel like I can only stare."
    "Come on, do something..."

    guest "Well, it was the mice's fault for living in a compost pile of all places!"
    "That sounded much better in my head."

    scene black
    with Pixellate(.5, 5)
    pause .5
    host " > {i}Sorry, I didn't want to bother you with this...{/i}\n > {i}It's so late, sorry for keeping you up{/i}"

    "Why is she sorry?! {b}I{/b} should be sorry for failing to comfort her."

    "Idiot! You're leaving her hanging like this?!"

    "I still don't know what to say..."

    pause 1
    guest " > {i}wait{/i}"

    pause 3
    "She's gone, isn't she?"

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
    "{i}I don't know how much time we spent talking, but she fell asleep a little after the sun had risen{/i}"

    scene bg guestlandscape
    with Dissolve(.5)
    pause .5
    "{b}<The background is now them sitting on the rock, which now is surrounded by land (the water level has lowered), and [guest] is being [host]'s lap pillow and petting her hair>{/b}"
    guest "Sleep well - or at least as well as you possibly can after pulling an all-nighter like this."
    guest "And, by the way..."

    scene black
    with Dissolve(.5)
    pause .5
    guest " > {i}when you wake up -- theres something you might be interested in if youre free in a few days{/i}"

    jump act5


label act5:
    scene bg guestlandscape
    with Dissolve(.5)
    pause .5

    "{b}<The background is Fox Peak Sanctuary - a nonprofit which rescues foxes>{/b}"
    show friend at right
    friend "Oh, you both made it! Welcome to Fox Peak Sanctuary."

    show guest at center
    guest "Hello."

    show host at left
    host "Hi! Nice to meet you!"

    friend "Thanks so much for your donations. I was so excited to invite you that I forgot to clarify something - you can play with the animals and all, but this is also an opportunity for you to learn about how to care for them."
    host "No, it's ok! Actually, can I work here?"

    show guest smug
    guest "Getting ahead of ourselves here, aren't we? You haven't even started learning about any of this."

    show guest
    friend "Come on, don't berate her like that."

    show host proud
    host "That's right. Also, I may already know a thing or two."

    scene bg black
    with Dissolve(.5)
    pause 1

    "{b}<The background is something abstract or just black>{/b}"
    "...She did know a thing or two. Actually, probably three or four."

    scene bg guestlandscape
    with Dissolve(.5)
    pause .5

    "{b}<The background is a close-up of [host] and [guest] h*ndholding - I mean such a close-up that their hands cover half of the foreground>{/b}"
    host "Thanks so much for inviting me here! I hope we can come back sometime."
    guest "Glad to help! I had fun too, actually."
    guest "By the way..."

    scene bg black
    with Dissolve(.5)
    pause 2
    guest "Does Meow Meadow have multiplayer support?"

    return
