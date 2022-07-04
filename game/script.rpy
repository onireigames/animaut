# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define host = Character("Dannie", who_color="#C9A362")
define guest = Character("Karina", who_color="#A975AC")
define friend = Character("Darcy", who_color="#629A18")
define unknown = Character("<Unknown>", who_color="#E500FF")

# The game starts here.

label start:
    play music ocean
    scene bg intro
    "How long will I keep failing...?"
    "Why am I even doing this to myself...?"
    scene bg intro closeup with Dissolve(1)
    "I just need some time to reflect..."

    stop music
    scene bg guestroom with Dissolve(1)

    "Maybe I am a masochist after all."
    "At least this time it's going way better. I got this!"
    pause 1

    show guest sitting frustrated at left with hpunch
    guest "Ugh! Not again!"
    "...I don't got this."

    "This stupid ledge again! I swear, they should screen level designers for sadistic tendencies. Or maybe they do, and that's exactly how they hire them."

    show guest sitting smirk
    "{i}Or maybe you just got too full of yourself, dumbass.{/i}"

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
    show unknown sitting:
        yzoom 1.25
        xzoom 1.25
    "Oh no..."
    show guest sitting nervous
    show unknown sitting:
        yzoom 1.5
        xzoom 1.5
    "Oh no oh no oh no oh no oh no oh no oh no"
    show unknown sitting:
        yzoom 1.75
        xzoom 1.75
    "Now I remember. It wasn't deja-vu after all. It's probably [friend]. No, it's {b}definitely{/b} [friend]!"
    show guest sitting despairing
    show unknown sitting:
        yzoom 2
        xzoom 2
    "{i}That's what you get for not replying to her for at least a few days, especially about an invitation to such a wholesome place. Idiot...{/i}"

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
    show unknown menacing behind guest with vpunch
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
    guest " > {i}dont tell me you forgot to study for something too{/i}"
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

    scene bg black with Dissolve(.5)
    pause 1
    guest " > {i}everything else?{/i}"

    jump act2

label act2:
    host "Everything else - I close my eyes..."

    scene bg host oasis with Dissolve(.5)
    pause .5

    show guest armor at left
    show host armor at right
    host "...I breathe slowly, and imagine I'm in a nice place with trees. I'd play some ambient sounds too if I could do that quickly enough."

    host "But it wasn't enough this time... so I wanted to talk to you."
    show guest armor talking
    guest "Why me?"
    show guest armor talking smile
    guest "Not that I mind."
    show guest armor
    host "You were the only one who was awake at this time."
    "I can't argue with that..."
    show guest armor talking
    guest "That was your only reason?"
    show guest armor
    host "Okay, you weren't the {i}only{/i} one who was awake, there are a few others. I just didn't want to bother them."
    host "Wait! I didn't mean it like that! It's not like I wanted to bother you."
    show guest armor talking smile
    guest "Relax, you aren't bothering me."
    show guest armor
    guest "If anything, she only interrupted my torture with that godawful level."
    show guest armor talking smile
    guest "You're actually doing it too rarely."
    show guest armor
    host "Doing what too rarely?"
    show guest armor talking
    guest "Talking to me."
    show guest armor
    host "I'm sorry!"
    show guest armor talking
    guest "Whatever. I'm guilty of the same."
    guest "Anyway, what are you up to now? Going to sleep?"
    show guest armor
    host "I started playing to help get my mind off some things."
    "I don't even need to ask what she's playing. I can't relate, but if Meow Meadow is helping her calm down, maybe it's not so pointless after all."

    show bg host desert with Dissolve(.5)
    pause .5
    host "But I shouldn't. I should go back to sleep."
    show guest armor talking
    guest "Want to share those things you've been trying to stop thinking about first?"
    show guest armor
    "{i}As if.{/i} Considering how little we've talked lately, I might as well be a stranger to her."
    host "Just some things from my past."
    show guest armor talking
    guest "Oh, you've never talked to me about any of it before. It's funny how we've known each other for years and I still don't even know where you're from... and neither do you know much about me, actually."

    show guest armor
    host "Well, my childhood wasn't anything special."
    scene bg host village with Dissolve(.5)
    pause 2
    show guest armor at left
    show host armor at right
    host "I grew up in {image=jumbletext.png}{alt}some village{/alt} until I started going to school and had to move."
    show guest armor talking
    guest "Huh? I've never heard of {image=jumbletext.png}{alt}that village{/alt}, sorry."
    show guest armor
    host "Yeah, it's just a remote village, sorry for not clarifying."
    show guest armor talking smile
    guest "It wasn't anything special?! Maybe I'm just a naïve city kid, but I've love to live in a village."
    show guest armor
    host "I guess so... there weren't many people, but that didn't bother me. The adults terrified me and I was too afraid to even hang out with the ones my age."
    host "There was one whom I clicked with, but she was from a city and had to go back soon afterwards."
    show guest armor talking
    guest "Didn't you keep in touch with her?"

    show guest armor
    show host armor takingmaskoff
    host "I really wanted to. I could have written a letter to her..."
    show host armor talking sad
    host "I was too shy to ask my parents for help with that..."
    show host armor sad
    show guest armor talking
    guest "That sucks..."
    show guest armor
    "I knew she was the shy type, but that's shyness on another level... I don't know what to say to comfort her, though."

    show host armor talking lookside
    host "And I definitely couldn't have asked my older sister."
    show host armor sad
    show guest armor talking
    guest "Why not? Wait, you have a sister?! You've never told me about her."
    show guest armor
    show host armor talking sad
    host "Sorry if I was secretive about that. I don't want to think about her. I don't trust her, honestly..."
    show host armor neutral
    show guest armor talking
    guest "What did she do?"
    show guest armor
    "Maybe I'm asking her too much-"
    show host armor talking sad
    host "She never cared about others. Even worse..."
    scene bg host staircase with Dissolve(1)
    pause 1
    show guest armor at left
    show host armor talking sad at right
    host "When I was still a little kid, I invited her to my secret hideout. I wish I hadn't..."
    show host armor neutral
    "I don't like where this is going. Quick, change the topic! Just don't say anything..."
    show guest armor talking smile
    guest "Oh, like an abandoned construction site? I loved hanging out at those."
    show guest armor
    "...stupid. Damn it! There aren't many construction sites in villages, obviously."
    show host armor talking gloomy
    host "No, it was just a little shack next to a river. There was a cat - Mitzi - that I would play with and bring some food to."
    show host armor gloomy
    show guest armor talking smile
    guest "Cute!"
    show guest armor
    host "..."
    show host armor talking lookside
    host "I was playing with my sister when suddenly, she decided to throw a rock straight at Mitzi while she was sleeping."
    show host armor gloomy
    show guest armor talking
    guest "Oh... Was it an accident?"
    show guest armor
    show host armor talking sad
    host "I used to hope for that too. But no, it was on purpose. She survived, but never fully recovered from this."
    show host armor gloomy
    pause 1
    show host armor talking lookside
    host "Sorry, I'm talking too much."
    show host armor gloomy
    show guest armor talking smile
    guest "No, it's fine. I want to know more, actually."
    show guest armor
    "Well, that sounded selfish."
    show host armor talking lookside
    host "There's nothing more to this. Thanks for listening... I think I feel better now."
    show host armor lookside
    "Maybe my memory just sucks, but this has to be the first time I've heard her say \"thanks\" instead of \"sorry\". Did she even mean it, though?"
    show guest armor talking
    guest "I'm glad to help, if I really did... But just for the record - I'm not a licensed professional, you know!"
    show guest armor
    show host armor talking
    host "I've already been to therapy. It helped, and their prescription helped too."

    scene bg host forger with Dissolve(1)
    pause 1
    show guest armor at left:
        yzoom -1.0
    show host armor talking sad at right:
        yzoom -1.0
    host "At least for a while."
    show host armor lookside
    show guest armor talking
    guest "There are all kinds of therapists. Some are better than others, or so I've heard at least. You might want to explore more."
    show guest armor
    show host armor talking sad
    host "Maybe. But I thought I would get better over time, not worse."

    scene bg black
    with Dissolve(.5)
    pause .5

    guest "Well, why didn't you go back when you started feeling worse again? Or did you keep going?"
    host "I stopped going and I didn't want to go again."
    host "Before you say anything - I know, it was stupid."
    guest "If you know it was a mistake, why are you talking to me instead of to someone who knows what they're doing?"
    host "It's not so simple! No matter how much I wanted it to work, I couldn't be honest with them."
    guest "Really? What you said wasn't so bad. You've probably heard this before, but there's nothing you could have done to prevent any of that."
    guest "If anything, you probably handled everything better than present me would."
    host "Yeah, I've heard this before, and I think I've already forgiven myself for that. Maybe I'd be okay with myself..."

    jump act3


label act3:
    scene bg beach first
    with Dissolve(.5)
    pause .5

    host "...if I weren't a murderer - just as bad as my sister."
    "...This has to be a joke."
    "But unlike me, she doesn't make such badly timed jokes."

    guest "What?! And I hope it's not too late to say this, but our conversation isn't encrypted."
    "What have I dragged myself into?!"
    host "It doesn't matter."
    guest "Look, I don't want you to say anything you'll regret later. Let's just go to sleep."
    host "It was an accident. I was helping my grandparents out, digging into a compost pile."
    "Is she even listening? Also, compost pile?!"
    host "I heard some weird squeaking coming out of it. I didn't know what it was and didn't think too much of it. I was so stupid..."

    scene bg beach second with Dissolve(.5)
    pause .5
    host "I kept digging despite the sounds."
    host "I didn't know there were mice hidden there."
    "Mice?! In there?!"
    scene bg beach third with Dissolve(.5)
    pause .5
    host "Even worse, it was a mother with her babies."
    host "I don't want to remind myself of that, sorry."
    host "One of the pups in there was still alive, at least..."
    scene bg beach fourth with Dissolve(.5)
    pause .5
    host "I named him Beep."
    host "I took him inside, protected him from my cat, gave him special milk..."
    host "I even had to make sure he was warm because it was winter. Once, I panicked that he had frozen to death. I was sure he was a goner. He was alright, fortunately."
    host "He was so cute."
    host "After some time, he grew up and could finally see."
    host "But then, he jumped out of his box and fell onto the floor."
    host "My first thought was that my cat would get to him, so I stepped back without looking..."
    host "Sorry..."
    scene bg beach fifth with Dissolve(.5)
    pause .5
    "I thought I was prepared for the worst, but I don't know what to say even about this..."
    "I feel like I can only stare."
    scene bg beach sixth with Dissolve(.5)
    pause .5
    "Come on, do something..."

    scene black with Pixellate(.5, 5)
    pause .5
    host " > {i}Sorry, I didn't want to bother you with this...{/i}\n > {i}It's so late, sorry for keeping you up{/i}"

    "Why is she sorry?! It was me who didn't do anything about this."

    "{i}Idiot! You're leaving her hanging like this?!{/i}"

    "I still don't know what to say..."

    pause 1
    guest " > {i}wait{/i}"

    pause 3
    "She's gone, isn't she?"

    jump act4


label act4:
    scene bg guest bed with Pixellate(.5, 5)
    pause .5

    "No matter how many times I check, it won't make her reappear."
    "{i}Any rational person would just go to sleep, not spend 2 hours waiting for nothing like you.{/i}"
    "But this is also one of those moments where no matter how heavy my eyelids feel, I can't fall asleep anyway. If there's anything irrational here, it's the human body."

    scene bg guest lying with Dissolve(3)
    pause 1

    "{i}You shouldn't have asked her so much and you shouldn't have ignored her. She'll never forgive you for being so nosy and indifferent.{/i}"
    "Too nosy and too indifferent - what an oxymoron. It's true, though. How do I even manage to act like this?!"
    "And let me guess - if I told [friend] about this, she'd tell me I'm being too hard on myself. \"Treat yourself like you'd treat your best friend\" or something - {i}yeah, right{/i}."
    "{i}Maybe her little advice, would actually make sense if you didn't treat your friends even worse than yourself.{/i}"

    scene bg black
    pause 2
    "..."
    "Well, then..."
    "What would I like to see myself do if I were [host], anyway?"

    scene bg guest reach with Dissolve(1)
    pause .5
    guest " > {i}are you still there?{/i}"
    guest " > {i}well, obviously not{/i}\n > {i}but i dont know what else to do{/i}"
    "(Nevermind, I don't even know what I'm doing...)"
    guest " > {i}sorry im such an idiot{/i}"

    pause 1
    "Actually, I do know what I'm doing - one of those things you tend to regret in the morning, when you can finally think clearly."

    pause .5
    scene bg guest reach hand1 with Dissolve(2)
    pause .5
    scene bg guest reach arm1 with vpunch
    host " > {i}Hi{/i}"
    pause 1
    scene bg guest reach arm2 with vpunch
    host " > {i}Can we talk?{/i}"

    scene black with Dissolve(.5)
    pause .5

    guest " > {i}youre still up?!{/i}\n > {i}but yes, please, let's talk{/i}"

    scene bg clocks with Dissolve(3)
    pause .5
    "{i}I don't know how much time we spent talking, but she fell asleep a little after the sun had risen{/i}"

    scene bg lappillow with Dissolve(2)
    pause .5
    guest "Sleep well - or at least as well as you possibly can after pulling an all-nighter like this."
    guest "And, by the way..."

    scene black with Dissolve(.5)
    pause .5
    guest " > {i}when you wake up -- theres something you might be interested in if youre free in a few days{/i}"

    jump act5


label act5:
    scene bg fps
    with Dissolve(.5)
    pause .5

    show friend standing talking at right
    friend "Oh, you both made it! Welcome to Fox Peak Sanctuary."

    show friend standing
    show guest standing talking at center
    guest "Hello."

    show guest standing
    show host standing talking smiling at left
    host "Hi! Nice to meet you!"

    show host standing smiling
    show friend standing talking
    friend "Thanks so much for your donations. I was so excited to invite you that I forgot to clarify something - you can play with the animals and all, but this is also an opportunity for you to learn about how to care for them."
    show friend standing
    show host standing talking smiling
    host "No, it's ok! Actually, can I work here?"

    show host standing
    show guest standing talking smug:
        xzoom -1
    guest "Getting ahead of ourselves here, aren't we? You haven't even started learning about any of this."

    show host standing smiling
    show guest standing:
        xzoom 1
    friend "Come on, don't berate her like that."

    show host standing talking smiling eyesclosed
    host "Yeah. Also, I may already know a thing or two."

    scene bg black with Dissolve(.5)
    pause 1
    "...She did know a thing or two. Actually, probably three or four."

    scene bg handholding with Dissolve(.5)
    pause .5

    host "Thanks so much for inviting me here! I hope we can come back sometime."
    guest "Glad to help! I had fun too, actually."
    guest "By the way..."

    scene bg black with Dissolve(.5)
    pause 1
    guest "Does Meow Meadow have multiplayer support?"

    return
