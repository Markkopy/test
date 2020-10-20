##################################################################################################################################################################################################################
###################################################### CHAPTER 2 CLOSE AT HAND ################################################################################################
##################################################################################################################################################################################################################

label chapter_two:
    $ lena_active = False
    $ ian_active = True
    $ save_name = "Ian: Chapter Two"
    
    show active_ian
    with long
    pause 1.0
    scene blackbg
    with long
    pause 0.5 
    call screen calendar
    
## LIFE DRAWING ###########################################################################################################################################################################################
    
    scene gallery2
    show v1_draw2
    if v1_fight:
        show v1_draw2_hurt
    with long
    
    "It was her, no possible doubt about it."
    if v1_name:
        "What the hell was Lena doing there?"
    else:
        "What the hell was the waitress doing there?"
    play music "music/fancy.mp3" loop
    scene gallery2
    show v1_drawpose3 # averting eyes
    with short
    "I was pretty sure she had seen me, too."
    "Her eyes crossed mine for a second, and now she was avoiding my gaze, seemingly on purpose."
    "Was she as stunned as I was?"
    scene gallery2
    $ fian = "insecure"
    $ fperry = "flirt"
    show ian at lef
    with short
    "I also averted my eyes. For some reason it felt kinda wrong looking at her like that...!"
    "Perry hit me with his shoulder to catch my attention."
    show perry at rig
    with short
    p "What did I tell you? What a b--{w=0.5}beauty, huh!?"
    if ian_tell_lenaperry:
        "Of course, Perry had no idea she was the girl I had told him about..."
    else:
        "Of course, Perry had no idea I knew who that girl was..."
    "Was he there to drool over her or to practice his drawing skills?"
    "While I was immersed in my thoughts, the guy conducting the session asked her to take a new pose."
    scene gallery2
    show v2_lenadraw1
    with short
    if v1_name:
        "I turned my attention back to Lena."
    else:
        "I turned my attention back to the waitress."
    "I almost couldn't believe she was the same girl I had been talking to just the other day."
    "I shouldn't be so surprised, though. It was normal that a girl as beautiful as her was offered jobs like that..."
    "And oh boy, was she beautiful..."
    "She was covering her eyes now, so I felt more at ease taking my time to look at her body..."
    menu:
        "Concentrate on your drawing":
            $ renpy.block_rollback()
            "I shook my head and tried to focus."
            "I was there to draw, not to stare at the model like a creep."
            "Though I couldn't avoid feeling somewhat creepy..."
            if v1_name:
                "I wondered if Lena was feeling anxious about the situation. I knew I would."
            else:
                "I wondered if she was feeling anxious about the situation. I knew I would."
            "Then again, I would never even think about posing naked in front of random people. So maybe it was no big deal for her."
            "I should concentrate and do what I came there to do."
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            
        "Stare at her body":
            $ renpy.block_rollback()
            "I took my time to stare at her beautiful figure."
            "Her long and silky legs, her toned and sinuous waist, her perfect, bountiful breasts..."
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            "I already knew she was a very attractive girl, but stripped of that apron she looked like a goddess!"
            "And I was having the privilege of admiring her naked beauty, just a few steps away from me..."
            "I was not looking at a picture. She was right there, in front of me, so real I could stand up, reach out and touch her..."
            "Again, the guy who was conducting the session asked her for a new pose."
            "I shook my head. I hadn't drawn a single line yet!"
            
    scene gallery2
    show v2_lenadraw2
    with long
    "As she changed to a new pose, I put pencil to paper and tried to draw."
    "Perry had kept drawing during these years, but I had focused on writing. It had been so long since I had practiced..."
    "I used to be pretty decent at it, though."
    i "Let's see..."
    show v2_lenadraw2 at lef3
    with move
    show v2_iandraw_base
    with short
    "I started sketching some lines, trying to get the proportions right."
    i "This goes here... And then the legs..."
    play sound "sfx/drawing.mp3"
    i "Hmmm..."
    if ian_wits > 1:
        show v2_iandraw1
        with long
        i "There... That looks quite like it."
        "It was nothing wonderful, but it wasn't half bad, either."
        "I had retained most of my ability."
        if v1_name:
            "I didn't have too much time to work on it either, since Lena changed to a new pose."
        else:
            "I didn't have too much time to work on it either, since she changed to a new pose."
    else:
        show v2_iandraw1b
        with long
        i "..."
        i "Oh, boy."
        "I had no idea what I was doing. I couldn't get the proportions or the anatomy right..."
        "And that face..."
        i "This barely looks human."
        "Had I forgotten how to draw properly in just a few years?"
        "I was finding it hard to get my hand-eye coordination going, that was for sure..."
        i "Let me erase this part and try again..."
        if v1_name:
            "Before I could do much, Lena was asked to change position again."
        else:
            "Before I could do much, she was asked to change position again."
        i "Damn!"
    scene gallery2
    show v2_lenadraw3
    with long
    "She sat down and arched her back, looking sideways into my direction."
    "Was she trying to see how I reacted?"
    "I tried to focus my eyes on the paper. I didn't want to come off as a creep... But it was hard not to stare at her!"
    "Those sensual and elegant curves on her body, her beautiful black hair..."
    show v2_lenadraw3 at lef3
    with move
    show v2_iandraw_base
    with short
    if ian_wits > 1:
        i "Focus, Ian. Don't be a perv."
        "After whispering to myself I took a deep breath and started drawing again."
        "My hand felt looser now, after having warmed up with the previous drawings..."
        play sound "sfx/drawing.mp3"
        i "Hmmm..."
        show v2_iandraw2
        with long
        "The image began taking shape as I analyzed her anatomy and translated it to the paper."
        i "Not bad... I'm not quite catching her face, but the rest is pretty good, I'd say..."
        "I worked a bit more on it until the time for this pose expired."
    else:
        "I pulled up the paper, and tried to draw..."
        "Damn, she was too distracting. I was worried her eyes would cross with mine and she'd catch me ogling her body."
        "But that was what we both were there for, right? Everybody else was doing it!"
        "Was I the only one feeling like a perv?"
        i "Shit, I should draw before the time for this pose expires...!"
        play sound "sfx/drawing.mp3"
        i "Quick!"
        show v2_iandraw2b
        with long
        i "..."
        i "What the hell is this...?"
        i "I can't draw with so much pressure!"
        "I had no time to carefully plan the drawing, and before I could do much more the pose changed again."
    
    scene gallery2
    with long
    if v1_name:
        "The session ended and Lena left the podium, going backstage to change."
    else:
        "The session ended and the model left the podium, going backstage to change."
    "The participants stood up and began chatting and checking out each others' drawings."
    $ fian = "sad"
    $ fperry = "happy"
    show ian at lef3
    show perry at rig3
    with short
    p "T--{w=0.5}that was fun! It had been such a long time since I practiced drawing from life."
    p "I should do this more often..."
    p "And that girl was... Oh mamma!"
    p "When have you seen a girl that hot? Aside from maybe Cindy."
    i "Dude, I know her."
    p "What do you mean you k--{w=0.5}know her?"
    if ian_tell_lenaperry:
        i "I know her! She's the waitress I told you about!"
        $ fperry = "surprise"
        if v1_name:
            i "Lena!"
        p "The waitress? No way!"
        i "I swear!"
    else:
        i "I haven't told you, but there's this waitress at that cafe where I usually go..."
        i "And well, we talked a bit the other day, and also on Thursday..."
        $ fperry = "surprise"
        p "That girl's t--{w=0.5}the waitress?"
        i "Yeah!"
        p "No way."
        i "I swear!"
        if v1_name:
            i "I even know her name. Lena!"
            p "Is that so?"
        else:
            p "And what's her name?"
            i "I, uh... I haven't gotten around asking her yet..."
            $ fperry = "meh"
            p "Really? And you said you've talked a couple of times already?"
            i "The opportunity just didn't present itself, alright?"
    $ fperry = "n"
    p "And what's she doing here?"
    i "How am I supposed to know?"
    p "I don't know, it's you who t--{w=0.5}talked to her!"
    $ fian = "serious"
    i "Yeah, and she she told me: \"when I'm not working as a waitress I pose naked in life-drawing sessions\"!"
    p "No, she did not."
    $ fian = "worried"
    i "Of course she didn't. I'm really surprised to find her here..."
    p "It's a small world..."
    p "So, are you gonna talk to her?"
    if v1_name:
        i "What? I... I don't know if I should."
        p "Well, you k--{w=0.5}know her name already. It would be weird not to talk to her."
        i "I think the situation is plenty weird as it is..."
    else:
        i "What? Talk to her?"
        p "You can ask her name n--{w=0.5}now."
        i "Are you sure this is the best scenario, dude?"
        p "Well, it would be weird to leave without at least saying hi..."
    $ flena = "n"
    show lena 
    with short
    $ fian = "surprise"
    if v1_name:
        l "Hey, hello Ian."
        l "This is such a... funny place to meet you."
        $ fian = "blush"
        i "It sure is... I was shocked when I saw you were the model."
        if v1_fight:
            $ flena = "surprise"
            l "What happened to your eye!?"
            $ fian = "worried"
            i "Oh, this... Well, I got into an... altercation."
            l "Someone punched you?"
            i "He was just some drunk guy who started up a fight with my friend Perry..."
            p "He stepped in to help me."
            $ flena = "worried"
            l "That's very noble on your part... Too bad you ended up hurt!"
            i "It's nothing... It'll go away soon enough."
            $ flena = "n"
            l "Do you get into fights often?"
            $ fian = "blush"
            i "Me? No, no, it was my first time to be honest!"
            i "You see, me, I'd rather spend a quiet afternoon here drawing than getting into trouble, ha ha..."        
        l "I didn't know you were so artistically inclined."
        i "I'm more of a writer, but I used to draw, too... It was Perry who brought me here today."
        p "Hey."
        l "Oh, nice to meet you. I'm Lena."
        p "I know."
        l "You do?"
        "Lena looked at me. That fucking Perry."
        i "I just told him I knew you."
        $ flena = "shy"
        l "Of course."
        $ flena = "n"
    else:
        wai "Hey, hello again."
        wai "This is such a... funny place to meet you."
        $ fian = "blush"
        i "It sure is... I was shocked when I saw you were the model."
        if v1_fight:
            $ flena = "surprise"
            wai "What happened to your eye!?"
            $ fian = "worried"
            i "Oh, this... Well, I got into an... altercation."
            wai "Someone punched you?"
            i "He was just some drunk guy who started up a fight with my friend Perry..."
            p "He stepped in to help me."
            $ flena = "worried"
            wai "That's very noble on your part... Too bad you ended up hurt!"
            i "It's nothing... It'll go away soon enough."
            $ flena = "n"
            wai "Do you get into fights often?"
            $ fian = "blush"
            i "Me? No, no, it was my first time to be honest!"
            i "You see, me, I'd rather spend a quiet afternoon here drawing than getting into trouble, ha ha..."       
        wai "I didn't know you were so artistically inclined."
        i "I'm more of a writer, but I used to draw, too... It was Perry who brought me here today."
        p "Hey."
        wai "Oh, nice to meet you. I'm Lena."
        "So that was her name!"
        i "I'm Ian, by the way."
        l "Oh, right! We hadn't properly introduced yet."
        l "Nice to meet you too, Ian."
        i "Same..."
    $ ian_lena_agenda = True
    $ lena_ian_agenda = True
    $ lena_perry_agenda = True
    l "Can I see your drawings?"
    i "Ehh..."
    menu:
        "Sure, take a look":
            $ renpy.block_rollback()
            i "Sure, take a look..."
            show v2_iandraw_base
            if ian_wits > 1:
                show v2_iandraw1
            else:
                show v2_iandraw1b
            with short
            i "I did this one..."
            if ian_wits > 1:
                p "Hey, not bad."
                l "It's pretty good!"
                i "It came out better than expected, yeah."
            else:
                $ fian = "worried"
                p "Dude, what the fuck?"
                i "It's not very good, I know that, OK?"
                l "Sometimes it take a while to warm up, doesn't it?"
                i "Right..."
            if ian_wits > 1:
                hide v2_iandraw1
                show v2_iandraw2
            else:
                hide v2_iandraw1b
                show v2_iandraw2b
            with short
            i "And also this one here."
            if ian_wits > 1:
                $ v2_photo_draw = True
                l "This one's beautiful! You're pretty good at it, aren't you?"
                $ ian_lena += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                p "I thought you'd d--{w=0.5}do worse."
                i "Me, too, but it seems I haven't completely forgotten how to draw."
                hide v2_iandraw_base
                hide v2_iandraw2
                with short
                p "Are you sure you want to write books? Maybe you could try finding work as an artist..."
                i "That's even harder."
                l "Well, I'm glad I inspired such beautiful drawings!" 
                l "Can I take a picture of them?"
                $ fian = "shy"
                i "Oh, sure... Go ahead."
                play sound "sfx/camera.mp3"
                with flash
            else:
                $ flena = "shy"
                l "..."
                p "..."
                i "..."
                hide v2_iandraw_base
                hide v2_iandraw2b
                with short
                p "Dude, seriously?"
                i "Hey, I tried my best! It's been ages since I last drew anything..."
                $ flena = "smile"
                l "You have an interesting style, very avant-garde. Seems like you're influenced by Picasso!"
                i "Uh, yeah, I... love Picasso."
            
        "Better not":
            $ renpy.block_rollback()
            $ fian = "insecure"
            i "I think better not."
            $ flena = "happy"
            l "Oh, come on! Why not?"
            i "They're not very good. I'm ashamed."
            $ flena = "n"
            l "Really? You shouldn't be."
            $ fian = "smile"
            i "I have reasons to be, believe me... Ha ha."
            l "Can I see yours, Perry?"
            p "Sure, g--{w=0.5}go ahead."
            $ flena = "smile"
            l "Oh, wow, these are pretty good!"
            $ fperry = "happy"
            p "You think so?"
            l "Yeah, you have good technique!"
            $ lena_perry += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            p "T--{w=0.5}thanks!"
    $ fperry = "n"
    $ flena = "n"
    $ fian = "smile"
    i "So, how did you end up here, doing this?"
    l "Oh, well, I've done a bit of artistic modeling..."
    l "And the gallery found my Peoplegram profile and offered me work. It was quite random."
    l "It's only my second time doing this."
    i "I see..."
    menu:
        "{image=icon_charisma.png}We should add each other on Peoplegram!" if ian_charisma > 0:
            $ renpy.block_rollback()
            $ v2_addlena = True
            i "Hey, we should add each other on Peoplegram!"
            i "We've been running into each other too often to keep being strangers, ha ha."
            $ flena = "smile"
            l "That's right. A lot of coincidences, right?"
            l "It's \"bluenightsky\", without spaces."
            i "Cool, I'll add you."
            "She didn't seem bothered by me asking for her Peoplegram profile. She even smiled at me..."
            i "Looks like some people are waiting to speak to you."
            l "Oh, yeah, the organizers... Well, I guess I'll be seeing you around!"
            i "Yeah."
            l "I'll follow you back when you add me. Gotta go!"
            i "Bye."
            hide lena
            with short
            i "Awesome."
            p "Well played, man. You've got some balls."
            i "She's awesome, I couldn't pass up on this chance... I'd like to get to know her more."
            p "You're aiming really high, you know that, don't you?"
            i "A man can try, right?"
            p "Of course. Just don't get your hopes up too much."
            $ fian = "serious"
            i "You always know how to cheer me up."
            p "I'm just concerned about you, as your friend!"
            i "Whatever. Let's go home."                
            
        "I hope it wasn't uncomfortable for you":
            $ renpy.block_rollback()
            $ fian = "worried"
            i "Um, I hope it wasn't too uncomfortable for you..."
            l "What?"
            i "Us being here and seeing you..."
            $ flena = "blush"
            l "Oh."
            l "No, don't worry about it... It's just work, after all..."
            p "It's not a very usual job, t--{w=0.5}though."
            l "I guess not..."
            $ flena = "n"
            l "I must admit it was a bit shocking finding you here, and it's a bit different posing in front of someone you know."
            l "But we live in the twenty-first century, it's not something I should feel ashamed about!"
            $ fian = "smile"
            i "Of course, you shouldn't..."
            i "Oh, looks like some people are waiting to speak to you."
            l "Yeah, the organizers... Well, I guess I'll be seeing you at the café."
            i "Yeah."
            p "How can one find you on Peoplegram?"
            $ fian = "worried"
            l "Oh." 
            l "It's \"bluenightsky\", without spaces."
            p "Cool!"
            l "Well, gotta go."
            i "Bye!"
            hide lena
            with short
            i "Dude, why did you ask for her Peoplegram?"
            $ fperry = "meh"
            p "Huh? Why shouldn't I?"
            i "It was kinda inappropriate."
            p "H--{w=0.5}how's that inappropriate?"
            i "It sounded like you just wanted to see naked pictures of her."
            p "I've just done you a favor, man! It's clear you l--{w=0.5}like her, but you don't have the balls to ask for it yourself."
            p "I don't care, so I did. You should be t--{w=0.5}thanking me!"
            "He had a point..."
            i "Whatever. Let's go home."            
            
        "We should get going":
            $ renpy.block_rollback()
            i "Well, um, I guess we should get going."
            i "Looks like some people are waiting to speak to you."
            l "Oh, yeah, the organizers... Well, I guess I'll be seeing you at the café."
            i "Yeah."
            p "How can one find you on Peoplegram?"
            $ fian = "worried"
            l "Oh." 
            l "It's \"bluenightsky\", without spaces."
            p "Cool!"
            l "Well, gotta go."
            i "Bye!"
            hide lena
            with short
            i "Dude, why did you ask for her Peoplegram?"
            $ fperry = "meh"
            p "Huh? Why shouldn't I?"
            i "It was kinda inappropriate."
            p "H--{w=0.5}how's that inappropriate?"
            i "It sounded like you just wanted to see naked pictures of her."
            p "I've just done you a favor, man! It's clear you l--{w=0.5}like her, but you don't have the balls to ask for it yourself."
            p "I don't care, so I did. You should be t--{w=0.5}thanking me!"
            "He had a point..."
            i "Whatever. Let's go home."   
    stop music fadeout 2.0
    $ gallery_scene3 = True

## PERRY HOME

    $ fian = "n"
    $ fperry = "n"
    play sound "sfx/door_home.mp3"
    scene ianhomenight
    show ian at lef
    show perry2 at rig
    with long
    "When we arrived at home we were still talking about Lena."
    p "So are you gonna ask her out an a date?"
    i "Don't be ridiculous."
    p "Why not? It's how you're sup--{w=0.5}supposed to go about it if you like her."
    i "First of all... Of course I like her. But I barely know her."
    if v1_name == False:
        i "I didn't even knew her name until today!"
    p "Well, that's a good way of getting to know her, isn't it?"
    i "Didn't you just tell me she's out of my league?"
    p "I told you you were aiming very high. I'm not saying it's imp--{w=0.5}impossible, but dude, she's friggin' beautiful."
    i "She is..."
    $ fperry = "happy"
    p "Let's check out her Peoplegram!"
    show ian at left
    show perry2 at right
    with move
    show v1_peoplegram
    if v1_rss_quote == 1:
        show v1_peoplegram_a
    elif v1_rss_quote == 2:
        show v1_peoplegram_b
    elif v1_rss_quote == 3:
        show v1_peoplegram_c
    with short
    "We pulled up our phones and looked at her profile."
    if v2_addlena:
        "I had added her right after leaving the gallery."
    else:
        "I had complained at Perry, but I wouldn't have her contact if it weren't for him..."
    $ fperry = "n"
    if v1_rss_quote == 1:
        $ fperry = "meh"
        p "\"Life is not a p--{w=0.5}problem to be solved, but a reality to be experienced\"."
        if ian_wits > 0:
            if ian_wits > 1 or ian_wits_xp > 1:
                p "This sounds like a caption you'd put on one of your posts."
                $ fian = "smile"
                i "Seems like she likes to use her brain. That's awesome."
            else:
                p "She sounds a bit smarty-pants."
                i "She looks like a clever girl alright."
        else:
            p "She sounds a bit smarty-pants."
            i "She looks like a clever girl alright."
        p "I doubt people follow her because of what she writes in these posts... Damn, look at that ass."
    elif v1_rss_quote == 2:
        $ fperry = "serious"
        p "\"Open your eyes, live and lie down with the s--{w=0.5}satisfaction of having done it all\"."
        if ian_charisma > 0:
            p "Ugh, that sounds like the typical, cheap inspirational quote every other girl posts with her photos."
            if ian_charisma > 1 or ian_charisma_xp > 1:
                $ fian = "smile"
                i "I think it's cool, she likes to promote a good vibe! It's typical, but what you gonna do?"
                i "She's smart, she's giving the public what they want."
                p "Oh yeah she is."
                p "I doubt the public is here for her inspirational quotes... Damn, look at that ass."    
            else:
                i "Yeah, sounds pretty generic and superficial... Well, I guess she has to give the public what they want."
                p "I doubt the public is here for her inspirational quotes... Damn, look at that ass."            
        else:
            i "Yeah, sounds pretty generic and superficial... Well, I guess she has to give the public what they want."
            p "I doubt the public is here for her inspirational quotes... Damn, look at that ass."            
    elif v1_rss_quote == 3:
        $ fperry = "flirt"
        p "\"If you want to p--{w=0.5}play with fire I can teach you\"."
        p "Would you look at that. Seems she's naughtier than we thought..."
        i "It's a pretty flirty caption, that's true..."
        if ian_lust > 0:
            if ian_lust_xp > 0:
                $ fian = "smile"
                i "Not necessarily a bad thing, though!"
        i "Maybe she needs to do that to engage her audience?"
        p "I'd say her pictures are engaging enough! Damn, look at that ass..."
    $ fperry = "n"
    $ fian = "n"
    "She hadn't posted too many pictures, but all of them were artistic, beautiful and sexy."
    i "You can't see much about her personal life in here. Seems she really sees this as some kind of job."
    p "She's keeping it professional, yeah. Though I would be more c--{w=0.5}concerned about posting pictures like this than to post about my personal life."
    i "To each their own, I guess... But it's true we're not used to interacting with people like her..."
    p "I wouldn't mind knowing more girls like her!"
    i "I'm sure you wouldn't..."
    $ fian = "n"
    play sound "sfx/sms.mp3"
    scene ianhomenight
    show ian at left
    show perry2 at right
    with short
    i "Wait, I just got a text..."
    show ian at lef
    show perry2 at rig
    with move
    i "It's Jeremy's."
    p "What does he want?"
    "I read what it said"
    j "{i}Hey dude, I just remembered tomorrow's that big MMA fight! Wanna watch it together?{/i}"
    "I wrote back."
    i "{i}Sure dude, sounds like a plan.{/i}"
    j "{i}Cool. I'll drop by your place around eight.{/i}"
    p "Is he c--{w=0.5}coming over?"
    i "Yeah."
    i "{i}Bring some beers.{/i}"
    "He replied one last time."
    j "{i}Sure, we don't wanna anger Perry \;\) See you tomorrow{/i}."
    i "We're gonna watch the fight tomorrow."
    $ fperry = "meh"
    p "Here?"
    i "Yeah."
    p "Hmm..."
    i "What? Since when do you complain when I invite our friends over?"
    p "I'm not c--{w=0.5}complaining! But Jeremy's your friend, not really mine."
    i "Since when is he not your friend? You've known him almost as long as I have, back in high school."
    p "Yeah, yeah, we used to be buddies. But things changed since then."
    p "He changed." 
    p "We don't have so much in common anymore. You know I'm not as much into martial arts and all that s--{w=0.5}stuff as you guys are."
    i "Well, in any case tomorrow he's coming over. You're welcome to watch the fights with us."
    p "Cool, cool..."
    i "Anyway, I'm going to my room."
    p "So soon? Don't you wanna have a few beers with your buddy?"
    i "Nah, I'll have them tomorrow while watching the fights."
    p "But it's S--{w=0.5}Saturday night! We should be doing something!"
    i "I want to do something productive tomorrow morning. Goodnight."
    scene ianroomnight
    with long
    "I went to my room and not too long after I went to sleep."
    
    
## SUNDAY ###########################################################################################################################################################################################################################################
    $ day = "Sunday"
    scene blackbg
    with long
    call screen calendar
    scene ianroom
    with long
    "I woke up fresh in the morning and decided to get myself going."
    play music "music/normal_day.mp3" loop
    $ ian_look = 2
    $ fian = "n"
    show ian
    with short
    "I had the whole morning and most of the afternoon to myself."
    "I could finally sit down and concentrate on writing."
    "I had been postponing it for a long time, but I had to seriously take care of it at some point."
    "If I wanted to have a shot at achieving my dream goal, that is."
    scene ianroom
    show v2_ianwrite
    with long
    "I powered up the computer and sat in front of it."
    i "Let's see..."
    "I had been toying with this idea for a book for quite a while."
    "I had only written down some notes and a few random paragraphs or scenes."
    i "This is no way to get a book written. I need to get my ideas straight."
    i "Start from the ground up and build things one step at a time."
    i "First of all, I need to know what kind of book I am writing."
    i "Which is its genre?"
    call screen book_screen_1
    if book_scifi:
        $ renpy.block_rollback()
        i "That's it, a {color=#3FB305}Science Fiction{/color} book!"
        play sound "sfx/keyboard.mp3"
        "I began to write the outlines of the plot, defining and chaining together some of the ideas I previously had."
        i "Science Fiction is an awesome genre. Deep and complex and super rich in subtext!"
        i "I can talk about society, politics, metaphysics... And add a few spaceships and lightsabers for good measure!"
        "I could do much with that, and use elements like aliens, AI, cyborgs..."
        i "This is the age of science fiction, after all."
    if book_fantasy:
        $ renpy.block_rollback()
        i "Of course, a {color=#B30505}Fantasy{/color} book!"
        play sound "sfx/keyboard.mp3"
        "I began to write the outlines of the plot, defining and chaining together some of the ideas I previously had."
        i "Fantasy is an awesome genre. Epic and dark and full of adventure!"
        i "I can let my imagination run rampant, take inspiration from so many mythologies, and create any world that I want!"
        "Fantasy was very fun to write, and I could use elements like magic, monsters and gods..." 
        i "Fantasy is really popular nowadays, after all."        
    if book_historical:
        $ renpy.block_rollback()
        i "I should write a {color=#D1B402}Historical{/color} novel!"
        play sound "sfx/keyboard.mp3"
        "I began to write the outlines of the plot, defining and chaining together some of the ideas I previously had."
        i "Human History is full of super interesting characters and stories, and all of those talk about who we are and who we used to be."
        i "I can dig deep into it and come up with a real, amazing plot based in one of those periods."
        "I had so much to choose from. I could write an adventure in medieval times or explore the great battles of the twentieth century."
        i "Historical novels are quite prestigious, after all."
    "For the first time in several months I felt excited again about writing my book."
    "I spent the whole morning immersed in this, writing down my notes and typing on the computer."
    "Ideas seemed to be flowing together nicely, as if they had been blocked until this moment."
    "I wondered if what had been happening lately had something to do with it..."
    "Meeting Lena and finding her in that life-drawing session..."
    if v1_alisonlunch:
        "Having lunch with Alison after so much time..."
    else:
        "Having lunch with Holly for the first time..."
    "Going out with the guys, Perry getting into trouble..."
    if v1_fight or v1_fight_kick or v1_fight_grappling:
        "And me getting into my first real street fight..."
    play sound "sfx/keyboard.mp3"
    scene ianroomnight
    show v2_ianwrite
    with long
    "I kept working on my book until late in the afternoon."
    i "Enough for today... Jeremy must be about to arrive."
    
##JEREMY ############################################################################
    $ jeremy_look = 1
    $ fjeremy = "smile"
    $ fperry = "n"
    play sound "sfx/door.mp3"
    scene ianhomenight
    show ian
    with long
    stop music fadeout 2.0
    "I decided to call it a day and relax."
    "I was happy. It had been quite a productive Sunday."
    play sound "sfx/doorbell.mp3"
    i "Oh, Jeremy's here."
    show ian at lef3
    with move
    play sound "sfx/door.mp3"
    play music "music/perrys_theme.mp3"
    show jeremy1b
    show jeremysmile
    with short
    "I opened the door for him."
    j "Hey! Whats up, dude?"
    if v1_fight:
        hide jeremysmile
        show jeremysurprise 
        j "Dude, what happened to your eye?"
        i "I got into a fight."
        j "Really? Tell me what happened!"
        i "Give me a minute and I'll tell you the story. Come on in."
        hide jeremysurprise
        show jeremysmile
    else:
        i "Not much, taking a break from work. Come on in."
        j "Working on a Sunday? Not even I do that!"
        i "I've been working on my book, you know."
        j "Oh, good, good."
    show perry2 at rig3
    with short
    p "Hey there."
    j "Hey, Perry!"
    hide jeremysmile
    show jeremyhappy
    "Jeremy smiled and held up a six-pack."
    j "I've brought beers."
    hide perry2
    show perry at rig3
    with short
    p "Oh, c--{w=0.5}cool."
    $ fjeremy = "smile"
    $ fian = "smile"
    hide jeremyhappy
    hide jeremy1b
    show jeremy
    hide perry
    show perry at rig3
    with short
    "Jeremy took off his jacket and we took a seat on the couch as we cracked some beers open."
    play sound "sfx/beer.mp3"
    j "Cheers!"
    j "The fights are starting, put them on!"
    "We began watching the first fight while drinking and chatting."
    if v1_fight:
        j "So, are you gonna tell me about your black eye?"
        $ fian = "n"
        i "Oh, yeah. So, Friday, after everyone decided to go home, Perry bumped into this drunk guy..."
        $ fperry = "mad"
        p "It was him who bumped into me!"
        j "So they bump into each other, then what?"
        i "Well, he got really aggressive and pushed Perry to the floor, so I decided to intervene. And things escalated."
        $ fperry = "meh"
        $ fjeremy = "happy"
        j "So you got into a street fight? And who won?"
        $ fian = "sad"
        i "I don't think anybody won... We just began punching each other like crazy. I'm not even sure what happened."
        $ fperry = "n"
        p "B--{w=0.5}both of you started flailing your arms like Rock 'Em Sock 'Em Robots."
        i "Yah, basically... We just punched each other until some bystanders separated us."
        j "I hope you gave him a black eye, too."
        $ fian = "smile"
        i "I cracked him with a good one... He was bleeding out of his nose."
        j "That's a cool story, bro. I wish I had been there!"
        i "You would've helped me, I hope!"
        j "Only if I saw you were having trouble, ha ha."
        j "Aside from that, how was the night with the gang?"
    else:
        j "How was last Friday with the gang?"
    i "Pretty cool."
    p "It had been a while since we all got together like that."
    j "It sucks I had to miss it, but my weekends are complicated with my new job!"
    if v1_fight_kick or v1_fight_grappling:
        p "You missed Ian's f--{w=0.5}fight."
        $ fjeremy = "surprise"
        j "You got into a fight?"
        i "Yeah."
        $ fjeremy = "happy"
        j "A real one? What happened?"
        i "So, after everyone decided to go home, Perry bumped into this drunk guy..."
        $ fperry = "mad"
        p "It was him who bumped into me!"
        j "So they bump into each other, then what?"
        i "Well, he got really aggressive and pushed Perry to the floor, so I decided to intervene. And things escalated."
        $ fperry = "meh"
        j "And who won?"
        if v1_fight_kick:
            $ fperry = "happy"
            p "Ian kicked his ass."
            i "He didn't even manage to lay a hand on me. I blasted him with some of those low kicks we had been practicing and he quit."
            j "Duuude, that's so badass! I wish I had seen it!"            
            $ fperry = "n"
            j "Seems like your training is starting to pay off!"
            i "It is."
            j "You're still a long ways from beating me, though!"
        if v1_fight_grappling:
            $ fian = "sad"
            $ fperry = "n"
            i "Well, I wouldn't say anyone won..."
            j "What happened?"
            i "When he tried to punch me I used that technique Wen showed me, I closed the distance and grappled with him."
            j "So you just hugged him."
            i "Well, I guess you could call it that... But he wasn't able to land a single punch."
            j "Well, neither were you. That shit's gay, I already told you. Don't listen to Wen."
            $ fjeremy = "smile"
            j "Next time punch his face in!"
            p "Let's hope there w--{w=0.5}won't be a next time..."
            j "You never know."
        j "So, what else is there to tell?"
    $ fjeremy = "smile"
    "Perry and I talked about the night and updated Jeremy on the other guys' status."
    play sound "sfx/sms.mp3"
    "While we were chatting and watching the fights I received a message."
    "It was Alison's."
    a "{i}Hey, how's it going?{/i}"
    i "{i}Chilling. I'm with Jeremy and Perry watching the fights.{/i}"
    a "{i}Oh, you're with Jeremy? Say hi to him on my behalf!{/i}"
    i "Guys, Alison says hi."
    p "She texted you?"
    i "Yeah, just now."
    if v1_alisonlunch:
        j "That's true! You did met Alison for lunch the other day, right?"
        i "Yeah."
    else:
        i "Oh, by the way, Alison asked about you the other night."
        j "About me?"
        i "Yeah."
        j "It's been so long since I last saw her... But we texted a few times."
    play sound "sfx/sms.mp3"
    if v1_alisonlunch:
        a "{i}It was nice having lunch with you the other day! We should do that more often.{/i}"
        $ fian = "smile"
        i "{i}Agree.{/i}"
        a "{i}And I'd like to see Jeremy and the others, too.{/i}"
        if v1_encourage_alison:
            a "{i}By the way, those things you told me, did you really mean them?{/i}"
            i "{i}What did I tell you, exactly?{/i}"
            a "{i}That I'm the smartest person you know, fun, and very attractive.{/i}"
            i "{i}Of course. Why would I lie to you?{/i}"
            a "{i}I don't know. So you think I'm very attractive?{/i}"
            play sound "sfx/sms.mp3"
            show ian at left
            show jeremy at rig3
            show perry at right
            with move
            show v2_alison_selfie1
            with short
            
            $ ian_alison_gallery = True
            $ ian_alison_pics.append("v2_alison_selfie1.png")
            
            $ fian = "surprise"
            i "...!"
            "Alison sent me an unexpected selfie. She was lying on her bed, smiling at me."
            "Jeremy noticed my reaction."
            j "Huh? What's that?"
            $ fian = "worried"
            i "Alison just sent me a selfie."
            $ fjeremy = "happy"
            j "Show us!"
            "I let Jeremy and Perry see it."
            j "Damn son, look at those jugs!"
            p "Why did she s--{w=0.5}send you that?"
            if v1_encourage_alison:
                i "I don't know. She asked me if I think she were attractive..."
            else:
                i "I don't know. She asked me if I think she were cute..."
            j "She's flirting hard!"
            p "Are you sure?"
            j "Dude, could it be more obvious?"
            i "What should I tell her?"
            p "P--{w=0.5}play it cool..."
            j "Bullshit, guns blazing man, show her you can play that game too."
            menu:
                "{image=icon_lust.png}You're so damn hot" if ian_lust > 0:
                    $ renpy.block_rollback()
                    $ v2_alisonflirt += 3
                    $ fian = "n"
                    "I decided to do as Jeremy was telling me."
                    i "{i}You're so damn hot, Alison.{/i}"
                    "She wrote back."
                    a "{i}So damn hot? I wasn't expecting that from you!{/i}"
                    i "{i}I'm just saying it how it is.{/i}"
                    $ ian_alison += 1
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    a "{i}I'm glad to know.{/i}"
                    $ fian = "happy"
                    hide v2_alison_selfie1  
                    with short
                    show jeremy at truecenter
                    with move
                    i "I told her she's really hot and it seems like she liked it!"
                    j "Of course she liked it, man! That's what she's after!"
                    
                "You're very beautiful":
                    $ renpy.block_rollback()
                    $ v2_alisonflirt += 2
                    $ fian = "n"
                    "I decided to find a middle ground between their two pieces of advice."
                    i "{i}You're very beautiful, Alison.{/i}"
                    a "{i}So you think I'm beautiful? You're adorable.{/i}"
                    a "{i}Thank you.{/i}"
                    $ fian = "smile"
                    hide v2_alison_selfie1  
                    with short
                    show jeremy at truecenter
                    with move
                    i "I told her she's beautiful and she said I'm adorable."
                    $ fjeremy = "n"
                    j "Ugh, adorable doesn't sound too good."
                    i "Why not? She seemed happy I called her beautiful."
                    j "You could've been more direct."
                    
                "You look good":
                    $ renpy.block_rollback()
                    $ v2_alisonflirt += 1
                    $ fian = "n"
                    "I decided to do as Perry advised."
                    i "{i}You look good.{/i}"
                    a "{i}Good to know I don't look horrible.{/i}"
                    hide v2_alison_selfie1  
                    with short
                    show jeremy at truecenter
                    with move
                    i "I told her she looks good, but I'm not sure she liked that."
                    j "You're thick as a brick, dude! She was letting you know what she wanted from you."
                    p "I d--{w=0.5}don't see how."
                    j "That's because you're even dumber than Ian."
                    
                "No comment":
                    $ renpy.block_rollback()
                    $ fian = "n"
                    i "I think it's better to not write anything back..."
                    i "I don't want Alison to get the wrong idea."
                    j "What wrong idea, dude? She knows what she wants. It's clear to me."
                    hide v2_alison_selfie1  
                    with short
                    show jeremy at truecenter
                    with move
    else:
        a "{i}Was nice seeing you guys the other day. Too bad he couldn't come.{/i}"
        if v1_alisonoften:
            a "{i}By the way, when you told me you wanted to see me more often, did you really mean it?{/i}"
            i "{i}Of course. Why do you doubt it?{/i}"
            a "{i}Oh, so you miss me?{/i}"
            i "{i}Like the desert misses the rain, ha ha.{/i}"
            a "{i}So cute. Do you think I'm cute?{/i}"
            $ fian = "worried"
            "Why was she asking me that all of a sudden?"
            p "What's up?"
            i "It's Alison. She just asked me if I think she's cute."
            p "What? W--{w=0.5}why?"
            j "Dude, you seem new to this. She's flirting."
            p "Are you sure?"
            j "Trust me, I know this shit."
            i "What should I tell her?"
            p "P--{w=0.5}play it cool..."
            j "Bullshit, she's testing the waters, seeing if you want to play the game, too."
            menu:
                "You're very beautiful":
                    $ renpy.block_rollback()
                    $ v2_alisonflirt += 2
                    $ fian = "n"
                    "I decided to do as Jeremy was saying. I told her what she was probably wanting to hear..."
                    i "{i}You're very beautiful, Alison.{/i}"
                    a "{i}So you think I'm beautiful? You're adorable.{/i}"
                    a "{i}Thank you.{/i}"
                    $ fian = "smile"
                    i "I told her she's beautiful and she said I'm adorable."
                    $ fjeremy = "n"
                    j "Ugh, adorable doesn't sound too good."
                    i "Why not? She seemed happy I called her beautiful."
                    j "You're being way too nice, dude. Add some more spice."
                    $ fjeremy = "smile"
                    
                "You look good":
                    $ renpy.block_rollback()
                    $ v2_alisonflirt += 1
                    $ fian = "n"
                    "I decided to do as Perry advised."
                    i "{i}You look good.{/i}"
                    a "{i}Good to know I don't look horrible.{/i}"
                    i "I told her she looks good, but I'm not sure she liked that."
                    j "You're thick as a brick, dude! That's not what she wanted to hear."
                    p "I d--{w=0.5}don't see how you can be so sure about what she wants."
                    j "That's because you're even dumber than Ian."
                    
                "No comment":
                    $ renpy.block_rollback()
                    $ fian = "n"
                    i "I think it's better to not write anything back..."
                    i "I don't want Alison to get the wrong idea."
                    j "What wrong idea, dude? She knows what she wants. It's clear to me."
    
    if v1_alisonlunch or v1_alisonoften:
        j "It seems she's been quite horny since she broke up with that loser boyfriend she had!"
        p "How do you know that?"
        $ fjeremy = "evil"
        j "She flirted with me, too."
        $ fian = "worried"
        $ fperry = "surprise"
        p "Really? W--{w=0.5}when? You said you haven't seen each other in a long time..."
        j "I also said we texted a few times. Wait a second..."
        "Jeremy searched on his phone."
        show jeremy at rig3
        show perry at right
        with move
        show v2_alison_selfie2
        with short
        $ ian_alison_gallery = True
        $ ian_alison_pics.append("v2_alison_selfie2.png")
        $ fjeremy = "smile"
        j "Here. She sent me this."
        p "Oh, wow."
        j "Wow indeed."
        $ fperry = "flirt"
        if v1_encourage_alison:
            p "The selfie she just sent you wasn't showing that much c--{w=0.5}cleavage, right Ian?"
            i "I don't think there's much difference..."
            p "Are you sure? Look at t--{w=0.5}that unbuttoned shirt!"
            "Her pose and attitude appeared more flirty than in the selfie she sent me..."
            "And for a minute there I thought I was special..."
        else:
            p "Holy smokes! Look at t--{w=0.5}that unbuttoned shirt!"
            "Her pose and attitude appeared quite flirty indeed... And she was showing a good bit of cleavage."
        i "What were you talking about for her to send you this?"
        j "I don't know, nothing special. She told me about her breakup and asked me about my relationships."
        hide v2_alison_selfie2
        with short
        play sound "sfx/sms.mp3"
        i "Wait, she texted me again."
        show ian at lef3
        show perry at rig3
        show jeremy at truecenter
        with move            
    
    $ fian = "n" 
    $ fperry = "n"
    a "{i}So, this Friday is a holiday. Me and a friend from work wanted to go out and have some drinks Thursday night, since we don't need to get up early the next day.{/i}"
    a "{i}Are you guys up for it?{/i}"
    "I read Alison's message aloud for the guys."    
    p "I'm always down for some beers."
    j "Count me in, too! I don't have to work Thursday nights."
    i "OK, I'm telling her we're in."
    a "{i}Awesome! See you guys on Thursday!{/i}"
    j "I wonder who this friend from work is. Hopefully a hot girl!"
    $ fian = "smile"
    i "You're incorrigible."
    $ fjeremy = "evil"
    j "Alison's pretty hot, too."
    if v1_encourage_alison and v1_alisonoften:
        j "And she seems to be flirting with you..."
        $ fian = "sad"
        i "And with you, too."
    j "What do you think about her?"
    menu:
        "She's just a friend":
            $ renpy.block_rollback()
            $ ian_alison_interest += 1
            $ fian = "smile"
            i "She's just a friend."
            if v2_alisonflirt > 1 and v1_alisonlunch:
                j "You're saying that now, but two minutes ago you were flirting with her over a selfie she sent you!"
                i "That was... I didn't ask for it, and she wanted to know what I thought about it!"
                j "And you let her know how much you liked it... Next thing you should do is give her some dicking!"
            else:
                j "I'm not saying she's not. But being friends doesn't mean you can't give her some dicking."
                j "It makes it even easier, in fact!"
            i "That's a good way of losing a friend."
            j "Only if you're bad in bed, ha ha."
            
        "She's very hot":
            $ renpy.block_rollback()
            $ ian_alison_interest += 2
            $ fian = "blush"
            $ fjeremy = "happy"
            i "Truth be told, she's very hot."
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            p "That's undeniable, even though she's not my type."
            j "How come she's not your type? Have you taken a good look at her tits?"
            p "Yeah, yeah. But she's too t--{w=0.5}tall, to begin with."
            i "You only say that because you're short as fuck."
            $ fperry = "mad"
            p "She's taller than you, too, d--{w=0.5}dumbass."
            $ fian = "worried"
            i "Just by a few centimeters..."
            
        "She's not my type":
            $ renpy.block_rollback()
            $ fian = "n"
            i "She's not my type, to be honest."
            if v2_alisonflirt > 1:
                j "Then what were you flirting with her for a moment ago?"
                i "That was... She sent me a selfie I didn't ask for and asked me what I thought about it!"
                j "And you let her know how much you liked it..."
                i "I just wanted to be polite."
                j "That sounded more than polite. Are you sure you don't want to get a taste of those tits?"
            else:
                j "Really? Are you sure about that?"
            i "Yeah. Besides, we've been friends since forever."
            i "It would be weird trying anything else with her."
            p "He's got a point. And she's too tall."
            j "You only say that because you're short as fuck."
            $ fperry = "mad"
            p "She's taller than Ian, too."
            $ fian = "worried"
            i "Just by a few centimeters..."  
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_jeremy += 1  
            j "In any case, fine by me. No competition!"
    
    if v1_encourage_alison or v1_alisonoften:
        p "So you're gonna try s--{w=0.5}something with her?"
        if ian_alison_interest == 2:
            j "Well, she seemed interested in Ian..."
            p "She was flirty with you, too."
            j "We'll have to see how she acts on Thursday, then!"
        elif ian_alison_interest == 1:
            j "Well, seems she showed some interest in Ian, but since you only see her as a friend, I might as well try!"
            i "Yeah... Just don't make things weird for the rest of us, please."
        elif ian_alison_interest == 0:
            j "Hey, you both said she's not your type, so I might as well try!"
            i "Just don't make things weird for the rest of us, please."
    else:
        j "It seems she's been quite horny since she broke up with that loser boyfriend she had!"
        p "How do you know that?"
        $ fjeremy = "evil"
        j "I think she showed me enough to let me know."
        $ fian = "worried"
        i "What do you mean?"
        p "You said you haven't seen her in a long time..."
        j "That's true, but we texted a few times. Wait a second..."
        "Jeremy searched on his phone."
        show ian at left
        show perry at right
        show jeremy at rig
        with move
        show v2_alison_selfie2
        with short
        $ ian_alison_gallery = True
        $ ian_alison_pics.append("v2_alison_selfie2.png")
        $ fperry = "surprise"
        $ fjeremy = "smile"
        j "Here. She sent me this."
        p "Oh, wow."
        j "Wow indeed."
        $ fperry = "flirt"
        p "That open button is really suggestive..."
        j "And the way she's biting her finger? A total tease."
        "Her pose and attitude were clearly flirty..."
        i "What were you talking about for her to send you this?"
        j "I don't know, nothing special. She told me about her breakup and asked me about my relationships."
        hide v2_alison_selfie2
        with short
        show ian at lef3
        show perry at rig3
        show jeremy at truecenter
        with move
        $ fperry = "n"
        $ fian = "n"
        p "So you're gonna try s--{w=0.5}something with her?"
        if ian_alison_interest == 2:
            j "Why not? Ian understands me! We're open to it, right bro?"
            i "Could be..."
        elif ian_alison_interest == 1:
            j "I know she's your friend, but since none of you is gonna do it, I might as well try!"
            i "Just don't make things weird for the rest of us, please."
        elif ian_alison_interest == 0:
            j "You both said she's not your type, so I might as well try!"
            i "Just don't make things weird for the rest of us, please."
    $ fian = "n"
    $ fperry = "n"
    $ fjeremy = "smile"
    i "In any case, you said you have plenty of girls already. Do you really need Alison to be one of those?"
    j "There's no reason to ever say no to a new pair of boobs, dude!"
    j "But yeah, I'm far from desperate. As I told you, working at that club is bonkers."
    $ fjeremy = "happy"
    $ fperry = "meh"
    j "And there's this girl I've been dating for a while, too... You could say I have my hands full, {p=0}ha ha."
    hide perry
    show perry2 at rig3
    with short
    i "And what about that girl, the one from the selfie you showed me?"
    j "The go go dancer? Nothing yet, but it looks very promising..."
    p "A go go d--{w=0.5}dancer?"
    j "Yeah. Wanna see?"
    $ fperry = "surprise"
    show ian at left
    show jeremy at rig3
    show perry2 at right
    with move
    show v1_selfiejeremy
    with short
    "Jeremy showed him the picture."
    p "Holy fuck."
    j "Right, baby!"
    p "She's very fit. And has the most amazing ass I've ever s--{w=0.5}seen..."
    p "I thought Lena was perfect, but this girl is something else...!"
    hide v1_selfiejeremy
    with short
    show ian at lef3
    show jeremy at truecenter
    show perry2 at rig3
    with move
    $ fperry = "n"
    $ fjeremy = "smile"
    j "Lena? Who's that?"
    i "Remember the girl I told you about, the waitress?"
    if v1_name_wits or v1_name_charisma:
        j "Oh, yeah, Lena! That was her name, right?"
    else:
        j "Oh, yeah, the waitress! You didn't know her name yet, right?"
        i "No, but I do now..."
    if ian_tell_lenaperry == False:
        $ fperry = "meh"
        p "Wait, you told him and not me?"
        j "Don't be a jealous girlfriend, Perry, ha ha."
        play sound "sfx/frienddown.mp3"
        show friend_down
        $ ian_perry -= 1
        p "I'm not."
    $ fian = "smile"
    i "Well, turns out we saw her yesterday..."
    "I told Jeremy what had happened at the art gallery."
    $ fperry = "n"
    $ fjeremy = "surprise"
    j "No way, she was the girl posing nude? Dude, that's so hot!"
    $ fjeremy = "flirt"
    j "You said she gave you her Peoplegram? Show me!"
    menu:
        "Show him Lena's profile":
            $ renpy.block_rollback()
            $ v2_showlena_jeremy = True
            i "Sure, look..."
            show ian at left
            show jeremy at rig3
            show perry2 at right
            with move
            show v1_peoplegram
            if v1_rss_quote == 1:
                show v1_peoplegram_a
            elif v1_rss_quote == 2:
                show v1_peoplegram_b
            elif v1_rss_quote == 3:
                show v1_peoplegram_c
            with short
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_jeremy += 1   
            j "Daaamn, boy! What a beauty!"
            i "She's stunning."
            j "She's super pretty, and what a nice ass... And those legs are killers."
            j "I'm happy for you, but don't let her get away. Don't fail me, man, you need to hit that!"
            p "You think he has a chance?"
            j "That doesn't matter. Warrior mentality, bro: do it or die trying."
            hide v1_peoplegram
            hide v1_peoplegram_a
            hide v1_peoplegram_b
            hide v1_peoplegram_c
            with short
            show ian at lef3
            show perry2 at rig3
            show jeremy at truecenter
            with move
            
        "Don't show it to Jeremy":
            $ renpy.block_rollback()
            $ fian = "sad"
            i "Never mind, man."
            $ fjeremy = "serious"
            j "What do you mean, never mind?"
            i "I don't want to show her off like an object."
            j "Don't get all white-knighty on me, man. Come on, don't be silly."
            i "Just forget about it, OK?"
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_jeremy -= 1
            j "Seriously... Sometimes you're a real jackass, dude."
            
    $ fjeremy = "smile"
    $ fian = "n"
    "We continued to hang out until the fights and the beers were done."
    "Finally, Jeremy stood up and got ready to leave."
    hide jeremy
    show jeremy1b
    show jeremysmile
    with short
    j "It's been fun, guys. See you on Thursday!"
    j "And see you at the gym on Tuesday, bro!"
    i "Bye, Jeremy."
    stop music fadeout 2.0

## MONDAY ###########################################################################################################################################################################################################################################
    $ week = 2
    $ day = "Monday"
    scene blackbg
    with long
    call screen calendar
    scene magazine
    with long
    $ fholly = "n"
    $ fminerva = "n"
    $ fian = "n"
    $ ian_look = 1
    "Another Monday at the office."
    show ian 
    with short
    "Today Minerva was gonna announce the next book review to take care of."
    "One of my favorite authors had just published his new book, and I was hoping I could review that one."
    "It was about time I could work with something I liked..."
    show ian at lef3
    with move
    show minerva
    with short
    mi "Alright, come here everybody. I'm going to designate this week's book reviews."
    show holly2 at rig3
    with short
    "The boss began assigning books to the interns. Then it was my turn."
    mi "Ian. Here, this one's for you."
    "I took the book she was handing me and looked at the cover."
    scene magazine
    show v2_book1
    with short
    i "What the...?"
    "Not again. Not another shitty, pre-pubescent book to review."
    i "\"Poker Love\"? What the hell is this?"
    "I had never even heard of this book or its author. And just looking at the cover made me cringe so hard...!"
    mi "It's the newest bet from Hierofant Publishing. They hope to kick-start a best-selling franchise with this new author."
    $ fian = "sad"
    $ fminerva = "mad"
    $ fholly = "sad"
    scene magazine
    show ian at lef3
    show minerva
    show holly2 at rig3
    with short
    mi "Make sure to keep that in mind."
    "That meant \"make sure to write an ass-licking review\", and she wasn't asking nicely."
    menu:
        "{image=icon_mad.png}This book is crap!" if ian_minerva < 4:
            $ renpy.block_rollback()
            $ fian = "serious"
            i "This book looks like crap! I can't review this!"
            mi "Excuse me?"
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            i "You've heard me. I won't review this."
            play sound "sfx/frienddown.mp3"
            show friend_down
            if ian_minerva > 1:
                $ ian_minerva -= 2
            else:
                $ ian_minerva -= 1
            "Minerva glared at me like she wanted to strike me dead."
            mi "You will, if you want to keep working here."
            i "Why do I keep getting assigned these awful reads?"
            mi "First of all, you haven't even read it, and you're assuming it's bad. How in the hell can I expect an honest review from you?"
            "She got on my nerves so fucking much!"
            $ fian = "mad"
            i "That's precisely what you won't let me do! Assign me a decent book and I'll write an honest review praising it!"
            $ fian = "n"
            i "\"The Fall of Delbaeth\" for example, by Victor White. It just came out this week!"
            mi "Ha! How do you expect me to assign such a complex and prestigious book to you, considering how poorly you've been doing?"
            $ fian = "mad"
            mi "You can't even write a competent review about a young-adult romance novel!"
            $ fian = "mad"
            i "I re-did it as you asked!"
            mi "Still not good enough. Far from it."
            if v1_alisonlunch == False:
                "That bitch! That was a blatant lie! Holly had helped me re-write it, I was sure we did a job she'd be pleased about."
            i "That's...!"
            mi "Enough! You have one choice, either resign and leave or shut up and review this book, making sure you do a good job this time."
            "I clenched my fists and gritted my teeth. I needed this job, but oh how I hated it."
            "How I hated her."
            $ fian = "serious"
            
        "Give me another book to review":
            $ renpy.block_rollback()
            i "Can't you give me a different book to review?"
            mi "What?"
            i "This book looks... Like another bland teenager romance novel. I'm sure there's someone else more suited to review this one."
            mi "You haven't even read it and you're already judging it? Have you ever heard the saying \"don't judge a book by its cover\"?"
            mi "How can I expect an honest review from you with that attitude?"
            i "That's all I'm trying to give you! But you just won't let me!"            
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_minerva -= 1
            mi "Excuse me?"
            i "Let me review another book, one I can honestly praise."
            i "\"The Fall of Delbaeth\" for example, by Victor White. It just came out this week!"
            mi "Ha! How do you expect me to assign such a complex and prestigious book to you, considering how poorly you've been doing?"
            mi "You can't even write a competent review about a young-adult romance novel!"
            $ fian = "serious"
            i "I re-did it as you asked!"
            mi "Still not good enough. Far from it."
            if v1_alisonlunch == False:
                "That bitch! That was a blatant lie! Holly had helped me re-write it, I was sure we did a job she'd be pleased about."
            i "That's...!"
            mi "Enough, Ian. If you want to get assigned more complex books, you need to prove your worth with these simpler ones first. That's it."
            "I clenched my fists and gritted my teeth. How much would I like to scream what I really thought to her face..."
           
        "Stay silent":
            $ renpy.block_rollback()
            i "..."
            "I wanted to complain, but I knew it wouldn't be wise to do so."
            "The face I was making gave me away, though."
            mi "You want to say something, Ian?"
            i "Uh... Not really but... I was hoping I could get books from a different genre to review from time to time."
            mi "Like what?"
            i "Well, \"The Fall of Delbaeth\" by Victor White, for example. It just came out this week and he's one of my favorite authors."
            mi "Ian, come on, you can't expect me to entrust you with such a complex and prestigious book after how poorly you've been doing with easier reads."
            i "What? I... I re-did the last one as you asked."
            mi "Still not good enough. Far from it."
            $ fian = "serious"
            if v1_alisonlunch == False:
                "That bitch! That was a blatant lie! Holly had helped me re-write it, I was sure we did a job she'd be pleased about."
            i "That's...!"
            mi "Enough, Ian. If you want to get assigned more complex books, you need to prove your worth with these simpler ones first. That's it."
            "I clenched my fists and gritted my teeth. How much would I like to scream what I really thought to her face..."
    hide friend_down        
    $ fminerva = "n"
    mi "Now, \"The Fall of Delbaeth\"... A book this prestigious needs someone able to rise to its level."
    $ fminerva ="smile"
    mi "Holly, dear, I trust you with this one."
    $ fholly = "blush"
    hide holly2
    show holly3 at rig3
    with short
    h "Oh... Thank you..."
    mi "I know it's a dense and thick book, but I'm counting on you to put in the extra work."
    $ fminerva = "n"
    mi "Well, that's it. The reviews are due on Monday, and since Friday's a holiday I won't be able to take a look at them until then."
    mi "Make sure to be thorough and proofread it yourselves."
    $ fminerva = "mad"
    mi "You've heard, Ian?"
    i "Sure."
    if v1_fight:
        mi "Oh, and by the way. Try not to show up to work with a black eye."
        if ian_minerva > 0:
            $ ian_minerva -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
        mi "It doesn't exactly reflect well on you, if you hadn't noticed."
        i "..."
    $ fholly = "sad"
    hide minerva
    with short
    "She turned around and went back to her office."
    "I dropped the book on my desk with disdain."
    i "\"Poker Love\"... What a joke."
    show holly3 at rig
    with move
    h "Um..."
    h "Sorry about that."
    $ fian = "n"
    show ian at lef
    with move
    i "Hey... What are you apologizing for?"
    h "What Minerva said to you... It wasn't nice."
    i "No, it wasn't."
    if v1_alisonlunch == False:
        $ fian = "serious"
        i "Can you believe what she said? That my last review was far from good."
        i "That's complete BS. You helped me write it in a way she'd like it."
        i "She adores your reviews. There's no reason why she shouldn't like mine."
        h "Yes, that was weird..."
    i "I swear, she's got something personal against me..."
    h "And I'm sorry I got assigned the book you wanted to read..."
    $ fian = "sad"
    i "It's OK..."
    if v1_fight:
        "She pointed at my black eye."
        h "Can I ask what happened...?"
        i "That's... I got into a fight defending a friend, just that."
        h "Oh. I see."
        "She noticed I wasn't too eager to talk about the matter again and didn't inquire anymore."
    menu decide_review:
        "I'll try to please her this time":
            $ renpy.block_rollback()
            $ ian_minerva_review = True
            i "I'll try to please her this time and write the review she wants."
            if v1_alisonlunch == False:
                i "Can I ask for your help again?"
                h "Of course..."
                $ fian = "smile"
                i "Thanks, Holly. I'll send you the review when I have it so you can take a look at it and advise me."
                $ fholly = "smile"
                h "I'd be glad to help."
            else:
                i "I'm sorry I had to cancel our lunch last time..."
                i "I feel bad asking you for help now, but if you could take a look at my review once I've written it..."
                $ fholly = "n"
                h "I'll be glad to help."
                $ fian = "smile"
                i "Thanks, Holly. I'll send it to you over the weekend."                
            i "I won't give Minerva any reason to complain this time. We'll see how she reacts..."
        "I'm going to write an actual honest review!":
            $ renpy.block_rollback()
            $ ian_honest_review = True
            $ fian = "serious"
            i "Well, I'm fed up. I'm going to write an actual honest review this time."
            i "If this book is any good, Minerva will be happy, but I doubt that will be the case..."
            h "Are you sure that's wise?"
            i "Who cares? No matter what I do, Minerva always shits on me."
            i "Might as well give her some real reasons to be mad!"
            h "I just hope you know what you're doing..."
            i "At least I'll get some fun out of reading this sorry excuse of a book."            
        "Would you exchange your book with mine?" if decide_review_holly == False:
            $ renpy.block_rollback()
            i "Hey, I just thought about something..."
            i "Feel free to say no, but..."
            i "Would you exchange your book with mine?"
            h "You want us to write each other's review?"
            i "Yes. I'll make a honest review of \"The Fall of Delbaeth\" and pass it as yours, while you'll write about \"Poker Love\" and submit it under my name."
            i "That way we'll see what Minerva really thinks about our analysis and writing skills."
            if ian_holly > 5:
                $ ian_switch_review = True
                h "Hm, I see what you're going after... It would really show if Minerva has something against you."
                i "I know I'm asking a lot of you... As I said, feel free to say no."
                h "No, I want to see what happens, too. I want to know if she really likes my work or just praises me no matter what I do."
                $ fian = "smile"
                i "Thanks, Holly! You're the best."
                "I pointed at the book laying on my desk."
                i "I'm sorry you'll have to read that pile of crap instead of \"The Fall of Delbaeth\"."
                h "Don't worry, I'm planning on reading it anyways!"
                i "Cool. I owe you one!"            
            else:
                $ decide_review_holly = True
                $ fholly = "blush"
                h "Uh... I'm sorry Ian, it's not that I don't want to help you..."
                $ fian = "sad"
                h "But I don't want to get in trouble with Minerva, and well..."
                h "I was hoping I could read \"The Fall of Delbaeth\" too."
                i "I understand... I was asking too much of you. Sorry, Holly."
                i "I'll need to think about something else..."
                jump decide_review
   
    hide holly3
    with short
    $ fian = "n"
    "With that decision in mind, I continued to work until it was time to get back home."
   
   
## IAN HOME #########################
    
    $ v2_talkperry_wade = False
    $ v2_talkperry_jeremy = False
    $ v2_talkperry_emma = False
    play sound "sfx/door_home.mp3"
    scene ianhomenight
    show ian at lef
    with long
    $ fperry = "n"
    i "I'm home."
    play music "music/perrys_theme.mp3" loop
    show perry at rig
    with short
    p "Hey."
    "I found Perry sitting on the couch, playing video games and drinking beer."
    i "Have you done anything today aside from that?"
    p "I w--{w=0.5}watched a couple of movies."
    i "Porn doesn't count as movies."
    p "Shut up."
    "I sat next to him and sighed."
    i "Pass me a beer."
    p "Drinking on a Monday? What's up with you?"
    i "Tough day at the office."
    p "And you ask me why I don't wanna get a job... Look at you. And W--{w=0.5}Wade's the same."
    i "Well, you'll need to earn your own money at some point. You can't live off me and your parents your whole life."
    p "You're one to talk. Your parents are giving you m--{w=0.5}money each month, too."
    i "I wish I didn't need it, believe me. My mother was right... I should've studied Law or Medicine or something like that."
    p "You would've never graduated."
    i "I know."
    play sound "sfx/beer.mp3"
    menu v2_talkperry:
        "Talk about Wade" if v2_talkperry_wade == False:
            $ renpy.block_rollback()
            $ v2_talkperry_wade = True
            i "You must miss when Wade was also unemployed and you two spent all day playing video games."
            p "Oh, I'm p--{w=0.5}playing with him right now."
            i "Online?"
            p "Yeah, we play almost every day."
            i "Really...? I thought he would be busier with his job and living with his girlfriend."
            p "Nah, he just got lazier. He's already got everything a man can hope for, so what's left for him to do?"
            i "I guess you could say his life is already fulfilled..."
            p "With a girlfriend like Cindy I would feel completely f--{w=0.5}fulfilled, no doubt about that."
            i "You could never have a girlfriend like Cindy."
            p "I know, she looks like a super model."
            i "I meant that you would be at each other's throat all day. You wouldn't last a week together."
            p "Yeah, that's also probably true. But s--{w=0.5}still, I do envy Wade. I mean, I'm happy for him, but he has always had it so easy with girls..."
            $ ian = "sad"
            i "Yeah, he almost made me feel bad seeing what a hard time I had in comparison."
            p "Don't complain, you scored Gillian."
            i "Yeah, and look where that got me..."
            p "Women are just trouble."
            $ fian = "n"
            jump v2_talkperry
            
        "Talk about Jeremy" if v2_talkperry_jeremy == False:
            $ renpy.block_rollback()
            $ v2_talkperry_jeremy = True
            i "You were cool with Jeremy last night."
            p "Of course. Why shouldn't I?"
            i "You told me you didn't really like him."
            p "I just s--{w=0.5}said I don't consider him a close friend. The guy's OK, I don't have anything against him."
            p "It's just he's not my cup of tea."
            i "Why?"
            $ fperry = "meh"
            hide perry
            show perry2 at rig
            with short
            p "Well, for starters, he's always b--{w=0.5}bragging about how many chicks he has, which girl he met, which one he fucked..."
            i "It's not like he's lying. He seems to be crushing it."
            p "Sure, but there's more to life than that, you know? And I'm not interested in hearing about all his conquests."
            i "That's because it makes you feel bad about yourself."
            p "Yeah, it does. So fucking what? I'm just n--{w=0.5}not interested in hearing about it, and that's it."
            $ fperry = "n"
            hide perry2
            show perry at rig
            with short
            jump v2_talkperry
            
        "Talk about Emma" if v2_talkperry_emma == False:
            $ renpy.block_rollback()
            $ v2_talkperry_emma = True
            i "Have you told Emma about Thursday?"
            p "Yeah. She can't come."
            i "Too bad."
            $ fian = "smile"
            i "When are you going to ask her on a date?"
            $ fperry = "meh"
            hide perry
            show perry2 at rig
            with short
            p "Don't start with that again."
            if v2_alisonflirt > 1 or ian_alison_interest < 1:
                p "I'm not like you or J--{w=0.5}Jeremy with that Alison thing. My friends are just that, friends."
            else:
                p "I'm not like J--{w=0.5}Jeremy with that Alison thing. My friends are just that, friends."
            $ fian = "evil"
            i "Oh, so you don't mind if some other guy asks her out?"
            p "She's free to do whatever she likes. It's not like she needs my p--{w=0.5}permission, or ever asked for it."
            i "So if I hook up with her you won't get mad?"
            $ fperry = "mad"
            p "What the hell are you t--{w=0.5}talking about?"
            i "You know, since you don't care, I could maybe ask her if she would like to have some fun..."
            p "Stop, you're embarrassing yourself, dude. She would n--{w=0.5}never agree to that. And you don't have the balls to ask her."
            $ fian = "smile"
            i "Calm down, I was just joking. Of course I won't do it."
            i "I just wanted to prove a point. And I think I clearly did."
            p "You just proved you're a jackass sometimes."
            hide perry2
            show perry at rig
            with short
            $ fperry = "n"
            $ fian = "n"
            jump v2_talkperry
            
        "Finish the beer and go to your room":
            $ renpy.block_rollback()
            "I finished drinking my beer and got up."
            i "Anyways, I'm going to my room."
            p "Alright."
            
    p "Oh, by the w--{w=0.5}way. Have you decided what to do about Lena?"
    i "What's there to do about her?"
    p "Well, you added her on Peoplegram... Have you texted her yet?"
    i "No, I haven't..."
    p "I thought you'd invite her on a d--{w=0.5}date or something."
    if ian_charisma > 0:
        i "I guess I should do that at some point, huh?"
    else:
        i "No way, dude..."
    p "I'm no expert on girls, but I imagine that's what she's expecting..."
    p "You've seen her nude, after all."
    i "What has that to do with anything?"
    p "I d--{w=0.5}don't know. But are you only going to meet her while she's working?"
    i "You've got a point..."
    i "I don't know, I need to think about it."
    stop music fadeout 2.0
    play sound "sfx/door.mp3"
    scene ianroomnight
    show ian 
    with long
    "I went to my room, sat down on the bed and picked up the book I had to review."
    "But I couldn't start reading just yet. What Perry had told me was still lingering in my mind."
    "Was Lena expecting me to contact her? Should I ask her out?"
    menu:
        "Text Lena":
            $ renpy.block_rollback()
            $ v2_ian_date = True
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            i "I don't know why I'm giving this so much thought. I should just write to her and see how it goes."
            "I picked up my phone and sent Lena a message through Peoplegram."
            i "{i}Hey Lena, it's Ian! How are you doing?{/i}" 
            i "{i}It was such a surprise seeing you on Saturday, and even meeting you in the first place. It would be cool if we could meet without it being an unexpected coincidence!{/i}"
            i "{i}If you're not very busy, we could hang out one of these days.{/i}"
            play sound "sfx/sms.mp3"
            i "There... sent."
            "I hope I didn't come across as too needy or try-hard..."
            i "I'm just overthinking things. If she's interested she'll say yes."
            "Now all I had to do was wait for her answer..."
            
        "Don't do it":
            $ renpy.block_rollback()
            i "I don't know what to say... And I have the feeling she's not interested..."
            i "I guess she was just trying to be polite..."
            "There was no real way to know unless I tried, though. But I felt it was too early."
            "I needed more time, more information..."
    
    i "Well, time to read this."
    if ian_switch_review:
        "I had to thank Holly. I could finally read something I would enjoy."
        "I was eager to write the best review I was capable of and show Minerva how full of shit she was..."
    elif ian_minerva_review:
        scene ianroomnight
        show v2_book2
        with short
        i "I can tell how ridiculously bad and absurd this book is just by looking at its cover."
        i "But I need to try my best and write a review that Minerva will like and praise."
        i "I'm gonna suffer through this..."        
    elif ian_honest_review:
        scene ianroomnight
        show v2_book2
        with short
        i "I can tell how ridiculously bad and absurd this book is just by looking at its cover."
        i "I will write a review Minerva won't be able to ignore. I'm fed up with her bullshit."
        i "I can't wait to see the look on her face when she reads it...!"
        
##############################################################################################################################################################################################################################
## LENA ##############################################################################################################################################################################################################################
##############################################################################################################################################################################################################################

    $ ian_active = False
    $ lena_active = True
    $ save_name = "Lena: Chapter Two"
    
    $ lena_look = 1
    $ flena = "n"
    $ day = "Monday"
    scene blackbg
    with long
    show active_lena
    with long
    pause 1.0  
    scene blackbg
    with long
    call screen calendar
    scene street
    with long
    play music "music/normal_day.mp3" loop
    show lena
    with short
    "I was on my way to the cafe."
    "I used my whole Sunday to relax at home, reading and listening to music."
    "Last week had been an intense one."
    $ flena = "blush"
    "The photo-shoot with Danny, Axel showing up at the restaurant and punching Robert, and then finding Ian at the life-drawing session..."
    "That had been really unexpected, and a bit uncomfortable."
    "Being found out was a risk I thought I had accepted, but it still felt weird. I hoped we wouldn't feel awkward next time he'd come to the cafe."
    "It was nothing I felt ashamed of, after all... But I would be lying if I said other people's perception didn't worry me."
    "I knew there were a lot of people who would frown upon knowing I was posing nude. But it was artistic, not a sexual thing."
    "At least not to me..."
    
    $ flena = "n"
    scene cafe
    show lena
    with long
    l "Good morning!"
    show ed at lef3
    with short
    ed "Good morning, Lena."
    show molly at rig3
    with short
    mo "Hello darling!"
    $ flena = "smile"
    l "Oh Ms. Van Dyke! You're back!"
    mo "Come on, I told you to call me Molly!"
    l "That's true. Sorry, Molly. Are you feeling alright?"
    mo "Yes, I'm OK now."
    ed "I told her to take a few more days off, but she wouldn't listen."
    mo "I'm not at ease knowing you're here all alone, Ed."
    $ fed = "smile"
    ed "Well, that's why I have Lena with me!"
    if v1_ed_truth:
        $ fed = "n"
        mo "But Lena's not here all the time. Oh, that reminds me..."
        mo "Did that photo-shoot go well?"
        $ flena = "blush"
        l "Oh, that..."
        "It seems like Ed had told his wife."
        l "Yeah, thanks... I'm sorry I had to leave early, but my friend organized it and it was a mess..."
        l "I'll make up for it by staying longer when you need it."
        mo "Oh, don't worry about it. I know we can't pay much, so I completely understand if you need to do some extra work!"
        ed "As long as it doesn't happen too often..."
        l "It won't, it was just a one time thing."
        mo "I hope you don't mind me asking, but I'm a bit concerned... You're OK with that kind of job?"
        l "What? Yeah, I am..."
        mo "OK, I just wanted to know! Please, don't think I'm judging or anything!"
        mo "But I know some young girls can do some things they end up regretting because they need money."
        l "It's nothing like that. It's just artistic modeling."
        mo "Good, good. I was just worried."
        "That conversation was taking longer than I wanted, and it was being too awkward."
        $ flena = "n"
        l "Thanks for your concern. Well, let's get to work."
    elif v1_ed_flirt:
        mo "She's really helpful, isn't she?"
        ed "Yeah, a lot... I don't know what I would've done without her these days!"
        $ flena = "shy"
        l "It's not such a big deal..."
        "It seems Molly didn't know anything about me leaving early the other day. Her husband hadn't told her..."
        "I felt a bit bad for having manipulated him, asking him for a favor while in my underwear."
        "It had been an awkward situation we were better off not speaking of."
        $ flena = "n"
        l "Well, let's get to work."
    else:
        mo "But Lena's not here all the time. Oh, that reminds me..."
        $ fmolly = "sad"
        $ fed = "n"
        mo "How's your dad feeling, Lena? Ed told me you had to take him to the hospital..."
        $ flena = "sad"
        l "Oh, that..."
        "I had come up with that excuse to be able to get off work early, and it seems Ed had told her..."
        "I felt bad lying about my father's health and making her worry. She seemed genuinely concerned..."
        menu:
            "Tell the truth":
                $ renpy.block_rollback()
                $ v1_ed_truth = True
                "I couldn't keep up the lie. Such a kind woman deserved the truth."
                l "Actually... I don't know how to say this, but I... I lied."
                $ fed = "sad"
                ed "What?"
                l "It's true that my father had cancer, and his health is delicate, but I didn't have to take him to the hospital."
                l "The truth is a friend of mine got me a photo-shoot and it was very important for me to go, but she messed up and organized it at a bad time frame."
                l "I needed to get off work early and I came up with that excuse. I'm really sorry..."
                ed "Why didn't you tell me up front?"
                l "I figured out you wouldn't agree to let me skip work, since Molly was ill... And I also felt kind of ashamed to tell you I was doing nude modeling."
                ed "Oh, wow, nude modeling?"
                mo "Darling, you can be honest with us. I know we can't pay much, so I completely understand if you need to do some extra work..."
                $ fmolly ="n"
                mo "And Ed can manage the business on his own for a few hours."
                $ fed = "sad"
                ed "As long as it doesn't happen too often..."
                l "It won't, it was just a one time thing."
                mo "I don't want you to feel like you have to lie to us. We don't want to be that kind of bosses!"
                play sound "sfx/xp.mp3"
                show charisma_up
                $ lena_charisma_xp += 1
                call screen skillsup
                l "You're too kind..."
                mo "I hope you don't mind me asking, but I'm a bit concerned... You're OK with that kind of job?"
                l "What? Yeah, I am..."
                mo "OK, I just wanted to know! Please, don't think I'm judging or anything!"
                mo "But I know some young girls can do some things they end up regretting because they need money."
                l "It's nothing like that. It's just artistic modeling."
                mo "Good, good. I was just worried."
                "That conversation was taking longer than I wanted, and it was being too awkward."
                $ flena = "n"
                l "Thanks for your concern. Well, let's get to work."
                
            "Keep lying":
                $ renpy.block_rollback()
                $ flena = "n"
                "I couldn't blow my cover now, though. And it was no lie his health was delicate, after all."
                l "Yeah, he's much better. It was just a check-up, but I had to take him... I'm sorry I had to leave early."
                $ fmolly = "n"
                mo "I'm glad to hear. Having cancer can get really tough..."
                mo "If you ever need to take care of him don't hesitate to tell us, you hear me?"
                mo "You don't need to prioritize work over your dad's health, or feel bad about leaving early if you need to."
                "She was so good-hearted... It felt wrong lying to her."
                l "Thank you so much... Well, let's get to work."

    $ fed = "n"
    $ flena = "n"
    scene cafe
    show lenawork
    with long
    "It was a slow day at the cafe. Not many customers..."
    "I hoped we would get busier days, or else the Van Dykes might see no need to employ me anymore..."
    "Time went by and my shift ended."
    stop music fadeout 2.0
    scene street
    show lena
    with long
    "I took my bag and headed to the gym."
    "Normally I had the night off at the restaurant on Mondays and Wednesdays. And I had promised Ivy I would attend her class."
    scene polegym
    with long
    $ lena_look = 2
    $ ivy_look = 2
    $ fivy = "smile"
    show lena at rig
    with short
    "I changed and got into the classroom."
    show ivy at lef
    with short
    v "Hey, you came!"
    l "I said I would, didn't I?"
    if v1_talk_ivy:
        $ fivy = "sad"
        v "How are you feeling? Any news about Axel?"
        $ flena = "sad"
        l "No, everything's been calm during the weekend..."
        l "Well, some stuff happened. But I'll tell you after class."
        $ fivy = "n"
    else:
        v "How have you been doing these past few days?"
        $ flena = "sad"
        l "A lot happened actually..."
        $ fivy = "n"
        v "A lot?"
        l "I'll tell you after the class."
    v "Alright."    
    $ flena = "n"
    show ivy at left
    show lena at right
    with move
    play music "music/jeremys_theme.mp3"
    v "OK, girls, let's get moving!"
    v "Let's pick it up from last week's figure..."
    scene polegym
    show v1_pole1
    with long
    "Ivy played the music and we began following her movements and instructions."
    "I gripped the pole and jumped, holding tight with hands and legs."
    "As the pole spun around, I tried going through the different figures Ivy taught us."
    scene polegym
    show v2_pole1
    with long
    "Ivy introduced a new move, and I followed her instructions."
    "I held myself up with just one arm and my thighs, gripping the pole between them."
    "I tensed my core muscles and tried to hold a plank position with my other arm stretched out."
    v "Good job, Lena!"
    play sound "sfx/xp.mp3"
    $ lena_athletics_xp +=1
    show athletics_up
    call screen skillsup
    l "This is tough...!"
    "Pole dancing was more physically demanding than it seemed! My body trembled as I tried to hold that pose."
    v "Use your core and your glutes!"
    l "I'm already doing it!"
    "I felt my strength falter and had to drop down."
    scene polegym
    show v2_pole2
    with long
    "Ivy didn't have that problem at all."
    "She spun around the pole holding herself up effortlessly, or so she made it seem."
    "Her face didn't even show a grimace, far from it."
    "She smiled confidently as she blew her hair away, displaying the feats her perfectly toned body was capable of."
    "It was a thing of beauty, no doubt about it... Feminine, athletic, and very sexy."
    "She must've put in a lot of effort to achieve that level."
    menu:
        "Try again":
            $ renpy.block_rollback()
            scene polegym
            show v2_pole1
            with long
            "I tried again. The difference in our level was obvious ..."
            "I felt clumsy compared to her, but still I found enjoyment in it."
            "I was far from perfect, but I found beauty in it nonetheless."
            "If only it weren't so tiring!"
            play sound "sfx/xp.mp3"
            $ lena_athletics_xp +=1
            show athletics_up
            call screen skillsup
            "After practicing for a few more minutes, the class came to an end."        
            
        "Rest":
            $ renpy.block_rollback()
            "I felt tired enough for today. I used the last few minutes of the class to stretch and rest."
    stop music fadeout 2.0
    scene polegym
    show ivy at left
    show lena at right
    with long
    v "Good job, girls. That's it for today."
    show ivy at lef
    show lena at rig
    with move
    l "Whew... I'm beat."
    if lena_athletics > 1:
        v "You're getting better! You did well today, if you keep up training you'll improve in no time."
        l "Thanks, Ivy."
    else:
        v "You should take it more seriously and train more."
        l "I do plenty already, considering how much I'm working the rest of the day..."
    $ minerva_look = 2
    $ fminerva = "smile"
    show lena at rig3
    show ivy at lef3
    with move
    show minerva
    with short
    $ lena_minerva_agenda = True
    mi "Thanks for the class, Ivy! It was great."
    v "I'm glad you liked it, Minerva. Will you be coming more often?"
    mi "I'd love to, but it's hard for me to find time since I'm already doing yoga..."
    mi "I really liked the class, but you have to be in such good shape! I'm not that strong..."
    v "It's all about practicing and getting in shape bit by bit."
    mi "I'll try and come again. Will you join us in yoga class?"
    v "I don't know about that, it's a bit too... calm for my taste."
    l "I didn't know they did yoga classes in here, too."
    mi "Yes, and the teacher's great. You should come!"
    mi "Anyways, I'll go take a shower... I'm beat!"
    v "Bye Minerva, thanks for coming."
    hide minerva
    with short
    $ fivy = "flirt"
    v "Did you see her during class? She looked like a sausage dangling from the pole, ha ha ha!"
    v "She's too old for pole dancing, she should stick with her yoga classes for grannies."
    menu:
        "Yeah, she's trying too hard":
            $ renpy.block_rollback()
            $ flena = "evil"
            $ v2_berate_minerva = True
            l "Yeah, it's kinda pitiful how hard she's trying..."
            v "Right? It's embarrassing."
            l "Some women have a hard time accepting they're not young anymore... And when they try to act all hot and sexy they just look ridiculous."
            v "Especially when compared with two beautiful hotties like us, right?"
            $ flena = "happy"
            $ lena_ivy += 1
            show friend_up
            play sound "sfx/friendup.mp3"
            l "Hee hee!"
            l "Oh God, I can be so mean when I'm with you sometimes!"
            v "Mean girls for the win!" 
            $ fivy = "n"
            $ flena = "n"
            
        "I'm not judging":
            $ renpy.block_rollback()
            l "I'm not judging her. She's just trying to stay active and healthy."
            v "People need to recognize when they're trying too hard. She's not young and sexy anymore, she should stop pretending to be."
            $ fivy = "serious"
            l "I don't really care about what other people do with their lives."
            v "Bah, you're no fun."
            $ fivy = "n"
            
        "Don't be mean":
            $ renpy.block_rollback()
            l "Oh, come on, don't be mean."
            l "She just wants to stay healthy and attractive. I wouldn't mind having her age and looking like she does."
            v "I shiver just thinking about becoming old and decrepit like her..."
            l "You're exaggerating too much!"
            v "Bah, you're no fun! I just wanted to have a laugh at the old lady."
            l "I think what she's doing is very cool. She's not letting her age defeat her. You'll be just like her in the future!"
            play sound "sfx/xp.mp3"
            show charisma_up
            $ lena_charisma_xp += 1
            call screen skillsup
            $ fivy ="sad"
            v "Oh God, I just hope I look much younger and hotter than she does..."
            $ fivy ="n"

    if v1_talk_ivy:
        v "So, no news about Axel. He hasn't tried to contact you again or showed up at the hotel?"
        l "Thankfully not..."
        v "So then, what other thing happened?"
        $ fivy = "flirt"
        v "Wait, don't tell me. You followed my advice and fucked that guy from work... What's he called, Robert, right?"
        l "No, that didn't happen."
        $ fivy = "n"
        v "Oh, and here I was hoping. You don't have any other candidates?"
        l "Not really... Well, in fact, I met someone last week..."
        
    else:
        v "So, what it is you had to tell me?"
        $ flena = "n"
        l "Yeah, about that..."
        "I told Ivy what had happened with Axel. How he showed up demanding to speak to me and how he had flipped out and punched Robert."
        $ fivy = "surprise"
        v "No way!"
        v "Why didn't you tell me that before?"
        $ fivy = "sad"
        v "You should've called!"
        l "I was such a mess... And I wanted to speak to you face to face. It's easier for me."
        v "That's no excuse... You know you can lean on me, right?"
        $ flena = "n"
        l "Yes... Thanks, Ivy."
        $ fivy = "n"
        v "So, what are you gonna do about that situation?"
        $ flena = "sad"
        l "I don't know... For now I'm content with him not showing up at my workplace again..."
        v "The staff threatened to call the police on him. He's a smart guy, I doubt he'll take that risk again."
        l "I don't know. Considering how he was acting, it wouldn't surprise me if he did..."
        v "So far he hasn't, right?"
        l "No, thankfully not."
        v "And if he does, maybe you should just talk to him."
        l "You want me to give him what he wants?"
        v "It's not such a big deal. He wants to talk, so talk to him."
        v "Tell him you don't want anything to do with him and that he should move on."
        $ flena = "serious"
        l "That's what I already told him! He just wants me to get back with him, and won't stop until I agree."
        v "Maybe he's not giving up because you're giving him reasons not to."
        l "How the hell am I giving him reasons for that?"
        v "You get so emotional and hot-headed when he's involved. If I were him, I'd think you haven't moved on yet and that you still have feelings for me."
        $ flena = "sad"
        l "I guess you have a point there..."
        v "That's why if you just talk to him calmly, without getting all riled up, and you tell him you're done with him, he'll have no other choice but to accept it."
        l "I'll think about it."
        v "And you show him you've really moved on."
        l "How?"
        v "You know my idea. You should fuck some other guy already!"
        v "What about Robert? That poor guy got punched because of you and he has been after you for quite some time!"
        l "I'm not feeling it..."
        v "Well, is there someone else then?"
        $ flena = "n"
        l "Not really... Well..."
        l "In fact, I met someone last week..."

    $ fivy ="flirt"
    v "Is that so? Tell me about it!"
    $ flena = "n"
    l "I just talked to this guy who comes sometimes to the café..."
    "I spoke to Ivy about Ian and about our surprising meeting at the art gallery."
    v "That's a coincidence!"
    v "Well, if he's seen you naked I'm sure he's dying to get you into his bed! That's an easy one for you."
    $ flena = "blush"
    l "I don't know if it's like that..."
    v "Oh, come on. You know how guys are. And you're very hot, it's just natural."
    l "I think we actually connected on other levels. Like we have similar interests and such..."
    v "So? That just makes it even better for you. And you said he's pretty cute, isn't he?"
    v "You should go for it and fuck him."
    l "We'll see how things play out. It's way too early to tell."
    $ fivy = "n"
    v "Sometimes you just overthink too much! You should learn to go with the flow."
    $ flena = "n"
    l "Sadly I'm not as easy-going as you are!"
    v "Speaking of which, how was the photo-shoot with Danny?"
    l "It was pretty nice. He's a good photographer."
    v "See? I told you you'd like working with him. Better than that life-drawing crap."
    v "So the last picture you posted on Peoplegram was from him?"
    l "Yeah. It's getting a lot of likes compared to the other ones."
    $ fivy = "smile"
    v "That's good. You should focus on making your follower count grow... It's good business!"
    v "Let me show you this!"
    "Ivy pulled up her phone and opened up an app I was unfamiliar with."
    show ivy at left
    show lena at right
    with move
    show v2_stalkfap1
    with long
    $ flena = "worried"
    l "Stalkfap? What's this?"
    $ fivy = "smile"
    v "It's a new social media platform for girls like us..."
    l "Looks similar to Peoplegram..."
    v "The basic gist is the same, but here people subscribe for a monthly fee if they want to have access to your content."
    v "And what you give them is, of course..."
    hide v2_stalkfap1
    show v2_stalkfap2
    with short
    "Ivy swiped down."
    v "Sexy stuff."
    $ flena = "surprise"
    l "So you're uploading your uncensored photo-shoots?"
    v "Yeah. Peoplegram doesn't allow explicit content, so if I did that they would delete my account..."
    v "But that's what people really wanna see. And they'll pay good money for that!"
    $ flena = "worried"
    v "I've been using it only for a week, but I'm already making some money..."
    l "So they just want to see your uncensored modeling pictures?"
    $ fivy = "flirt"
    v "Well, you have to give them some other stuff, too."
    hide v2_stalkfap2
    show v2_stalkfap3
    with short
    "She swiped down again, and this time a video appeared on screen."
    $ flena = "blush"
    "It was a crappy home-made recording of Ivy twerking on top of her bed."
    "Or I should rather say, a close up of her ass bouncing up and down."
    v "People want some hot stuff, things you won't upload to Peoplegram."
    l "It has nothing to do with your modeling shots... The difference in quality is rather big."
    v "People don't care about that! They want real, intimate stuff, which is great!"
    v "You don't even need a photographer! You just take a selfie or record yourself with your phone and they'll pay up!"
    l "I see..."
    v "I know some girls who are making bank like you wouldn't believe! As I said, I just got started and it looks very promising so far..."
    v "You should try it!"
    menu:
        "I'll check it out.":
            $ renpy.block_rollback()
            $ flena = "smile"
            l "Hmm... I guess I can check it out."
            v "You'd be dumb not to!"
            l "So I only have to post pictures from the photo-shoots and some selfies?"
            v "Yeah, it takes you literally five minutes a day and you can end up earning way more than with your actual two jobs!"
            l "That sounds too good to be true..."
            v "And just by showing some skin! The world is wonderful!"            
            play sound "sfx/xp.mp3"
            show lust_up
            $ lena_lust_xp += 1
            call screen skillsup
            l "Ha ha! OK, maybe I'll give it a try."

        "I'm not sure that's my style":
            $ renpy.block_rollback()
            $ flena = "n"
            l "I don't know, I'm not sure that's my style."
            v "What do you mean, your style?"
            play sound "sfx/xp.mp3"
            show charisma_up
            $ lena_charisma_xp += 1
            call screen skillsup
            l "You know, I like artistic photography, but posting videos twerking in my room... Not my thing."
            $ ivy = "n"
            v "Well, then do what you're comfortable with!"
            v "Posting the uncensored pictures from your photo-shoots could be enough, who knows. Just give it a try."
            l "I'll think on it."
            
        "It's quite tasteless":
            $ renpy.block_rollback()
            $ flena = "serious"
            l "You know I don't like these kind of things. It seems a bit... tasteless."
            play sound "sfx/xp.mp3"
            show wits_up
            $ lena_wits_xp += 1
            call screen skillsup
            $ fivy = "serious"
            v "What do you mean \"tasteless\"?"
            l "You know, selling my body like that..."
            $ lena_ivy -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            v "Oh, so you think I'm selling my body?"
            $ flena = "sad"
            l "No, I didn't mean it like that..."
            v "Just so you know, you're doing the same thing as me. In case you never noticed it."
            l "I know, I'm sorry, I didn't want to sound bitchy."
            l "It's just there are some limits I'm not comfortable with passing."
            v "Whatever. I just said it because I wanted to help you, but if you're not interested that's on you."
            $ fivy ="n"
            
    v "Anyways, it's getting late. Let's hit the showers."
    stop music fadeout 2.0
    scene streetnight
    with long
    $ louise_look = 2
    $ flouise = "cry"
    $ lena_look = 1
    $ flena = "n"
    $ look_ivy= 1
    $ fivy = "n"
    "After that I said goodbye to Ivy and went back home."
    "She had me given a lot to think about..."
    $ gallery_scene4 = True
    
## LENA HOME NIGHT

    scene lenahomenight
    with long
    play sound "sfx/door_home.mp3"
    show lena at rig
    with short
    l "Ah, I love my free nights... I'm home!"
    show louisebra at lef
    with short
    lo "Hi..."
    $ flena = "surprise"
    l "Louise! Are you OK?"
    "She was sitting on the sofa, eating ice cream and watching some random movie on the TV."
    lo "Yeah..."
    $ flena = "sad"
    "I sat next to her."
    l "That's obviously not true. Tell me, what happened?"
    lo "It's... I just feel so dumb."
    l "Why?"
    lo "Do you remember the guy I told you about?"
    l "Yes. Did he do something to you?"
    lo "Well, I wanted to see him so badly yesterday... It was Sunday after all. Couples do things together on Sundays."
    lo "But he told me he couldn't meet me because he had to see his guy friends!"
    l "So he promised you he would meet you and then turned back on his word?"
    $ flouise = "sad"
    show louise_smear at lef
    lo "Well no, we hadn't agreed on anything, but I expected him to want to see me when I called!"
    $ flouise = "mad"
    lo "But it seems he prefers his friends over me!"
    if v1_lena_louisecarriedaway:
        lo "You told me I shouldn't get so carried away, and you were right..."
        lo "I'm such a fool!"
    l "Wait, wait..."
    $ flouise = "serious"
    menu:
        "{image=icon_charisma.png}Maybe it's not like that" if lena_charisma > 1:
            $ renpy.block_rollback()
            l "Try seeing it from his perspective. Maybe it's not like that."
            lo "It's pretty clear to me how it is."
            l "I'm sure his friends are important to him, and he wants to see them, too. If he had agreed to hang out with them he would be a bad friend if he canceled at the last moment."
            lo "But he should want to see his girlfriend, too..."
            l "Yes, but it's important to find time for everything. Having personal space is important, too, in a relationship."
            l "And hey, you've only been seeing each other for two months. It's normal for these things to take some time."
            $ lena_louise += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            lo "I guess you have a point... I shouldn't freak out so much."
            l "Yeah, you're not making it any easier for yourself! Try to take it easier."
            $ flouise = "smile"
            lo "Thanks, Lena. I'm lucky to have you as a friend."
            
        "You're overreacting":
            $ renpy.block_rollback()
            l "Calm down, you're overreacting."
            lo "How am I overreacting? It's normal for a girlfriend to want her boyfriend's attention!"
            l "Yes, but you're making a big deal out of it and it doesn't have to be."
            l "He wants to see his friends, that's normal, too. And you've just known each other for two months!"
            $ lena_louise -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ flouise = "mad"
            lo "So you're taking his side?"
            $ flena = "worried"
            l "No, not at all! I'm just trying to say these things take time."
            $ flouise = "sad"
            l "Relationships usually develop slowly. Just give him some time until your relationship has solidified."
            lo "I don't know..."
            
        "Try to take it easy":
            $ renpy.block_rollback()
            l "I'm sorry about that, Louise... But try to take it easy."
            l "How long have you being dating this guy? Not long, right?"
            lo "It's been around two months since we met..."
            l "That's not very long. Some people take longer to feel comfortable in a new relationship..."
            $ flouise = "serious"
            lo "So you think he doesn't feel comfortable with me?"
            $ flena = "worried"
            l "No, I didn't say that...! I'm just trying to say maybe you just need to give it more time."
            l "See how things evolve..."
            lo "I don't know..."
    
    l "You'll see, I'm sure it's nothing to worry about. Try to think positive."
    hide louise_smear 
    with short
    "Louise took a tissue and wiped her eyes and cheeks."
    $ flouise = "n"
    $ flena = "n"
    lo "You're right. It will be OK."
    if v2_ian_date:
        play sound "sfx/sms.mp3"
        l "Oops, that's my phone."
        lo "Don't worry."
        "Someone had texted me."
        $ flena = "shy"
        l "Oh."
        "It was Ian."
        $ flouise = "smile"
        lo "What do you mean, \"oh\"? And what's with that face? There's something you're not telling me."
        l "Wait..."
        "I read aloud what he had texted me."
        l "{i}Hey Lena, it's Ian! How are you doing?{/i}" 
        l "{i}It was such a surprise seeing you on Saturday, and even meeting you in the first place. It would be cool if we could meet without it being an unexpected coincidence!{/i}"
        l "{i}If you're not very busy, we could hang out one of these days.{/i}"
        lo "Who's the guy? Come on, tell me!"
        l "It's this guy I met last week..."
    else:
        lo "I'm sorry to bother you with my problems."
        l "It's no bother, Louise! You're my friend."
        lo "Friends also listen!"
        lo "So, you have anything new to tell me?"
        if v1_talk_louise:
            lo "Aside from that unpleasant business with Axel..."
            lo "He hasn't bothered you again, right?"
            l "No, he hasn't, thankfully."
            lo "So, any other news?"
        else:
            "I could tell her about Axel, but I was in no mood for drama that night..."
            "I tried to think about something else to tell."
        l "Mhhh... Well, let's see... There's this guy I met last week..."        

    "I told Louise about Ian, same as I told Ivy."
    $ flouise = "blush"
    lo "Oh my God! So he saw you completely naked at the life drawing session?"
    $ flena = "blush"
    l "Yeah."
    lo "And then you went and talked with him?"
    l "Yes."
    lo "How do you do it? Didn't you feel, like, really uncomfortable?"
    l "I'd say I'm used to it, so normally it's not a big deal..."
    l "But I must admit this time it did feel quite awkward."
    $ flouise = "happy"
    lo "Uhh, so you feeling something like that means something..."
    $ flena = "shy"
    l "I guess not many people can make me feel awkward like that. I'm not sure that's a good thing, though."
    lo "It's something, that's for sure."
    $ flouise = "smile"
    if v2_ian_date:
        lo "So he wants to hang out someday?"
        $ flena = "n"
        l "So it seems."
        lo "That's another way of asking you out on a date."
        l "Louise...!"
        lo "Just saying. So, are you gonna meet him?"
        l "I guess... I see no reason not to..."
        lo "You don't look too convinced."
        l "He seems like a nice guy. And I guess it could be fun."
        l "I would feel less pressure if someone hadn't called it a date!"
        lo "Hee hee, sorry! But I think it's a good idea for you to meet him."
        lo "Just see what's the vibe like."
        l "Alright... I'm gonna text him."
        l "{i}Hi Ian! Sounds good to me, though I'm pretty busy during this week{/i}."
        l "{i}Wednesdays I have some extra time during morning before I get to the café. We can do something during those couple of hours if it's OK with you!{/i}"
        lo "Wednesday, huh? You won't have much time."
        l "No, but if things are uncomfortable the date won't drag out too long. That's my exit strategy."
        $ flouise = "happy"
        lo "You called it a date."
        $ flena = "shy"
        l "That's... It's your fault!"
        $ flouise = "sad"
        lo "I'm happy for you..."
        "Louise expression changed and she almost looked like she was gonna start crying again." 
        $ flena = "sad"
        l "You don't look too happy."
        lo "I'm sorry, it's just... Hearing you talk about this guy made me think about my boyfriend and..."
        
    else:
        lo "So he hasn't written you yet?"
        if v2_addlena:
            l "No, and I thought he would... It was him who asked to exchange Peoplegrams."
            lo "Maybe he's shy..."
            l "People tend to be shy face to face, not through social media... And he didn't look that shy."
            lo "Well, maybe he's not interested?"
        else:
            lo "You said he looked shy, right?"
            l "I got that impression... We exchanged Peoplegrams because his friend said it, so maybe he just wasn't interested..."
            lo "Could be. Or maybe he's just very insecure."        
        l "Who knows... I swear, sometimes guys just don't make no sense."
        $ flouise = "sad"
        lo "You're telling me..."
        $ flena = "sad"
        "Louise looked like she was gonna start crying again, remembering her problems with her new boyfriend."
        
    l "Hey, don't get like that again... We already talked about it."
    lo "I know, it's just..."
    if lena_louise > 5:
        "She looked at me."
        lo "Can I sleep with you tonight? I don't want to feel alone."
        menu:
            "{image=icon_friend.png}Sure, let's sleep together":
                $ renpy.block_rollback()
                $ v2_sleep_louise = True
                $ flena = "n"
                l "Sure. I'll keep you company tonight."                
                $ flouise = "happy"
                $ lena_louise += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                lo "Thank you, Lena! You really are my best friend!"
                scene lenaroomnight
                with long
                "We went to my room and got into bed."
                scene v2_lena_sleep1
                with long
                "I wasn't expecting Louise to get all over me and hug me like a koala hugs an eucalyptus tree right away."
                lo "You don't mind if I hug you a bit, right?"
                "She was still emotional because of that thing with her boyfriend..."
                "She was one of those girls who needed cuddles to feel better... But don't we all?"
                l "Sure, no problem..."
                "Louise fell asleep almost immediately, at least that was the impression I got."
                "She closed her eyes and the weight of her relaxed body pressed into mine. I heard her deep and slow breathing."
                l "I should try and sleep, too..."
                scene v2_lena_sleep2
                with long
                "I closed my eyes and Louise's sweet smell filled my nostrils when I took a deep breath, trying to relax."
                "I felt the warmth of her body, the skin of her thigh brushing against my own..."
                "I was a nice sensation."
                "I gradually fell asleep, embraced by my friend."
                jump v2lena_stan_photo
                
            "Sorry, but no":
                $ renpy.block_rollback()
                l "Sorry Louise, but I don't think it's a good idea."
                lo "Why not?"
                l "My bed's small, and I need to get a good night's sleep."
                l "Tomorrow will be a hard day..."
                $ lena_louise = 5
                play sound "sfx/frienddown.mp3"
                show friend_down
                lo "Alright, I get it... Good night."
            
    else:
        lo "Never mind. Good night, Lena."
        a "Good night..."   
    
    scene lenaroomnight
    with long
    $ flena = "n"
    play sound "sfx/door.mp3"  
    show lena
    with short
    "We each went to our room after chatting a bit more."
    play sound "sfx/meow.mp3"
    show lola at lef3
    with short
    l "Oh, here you are."
    play sound "sfx/meow.mp3"
    l "Yes, yes, I'm coming to bed. Don't be impatient."
    if v2_ian_date:
        "So I would see Ian soon, not as a waitress or a model, but just as a regular girl..."
        "Why was I kind of anxious about it?"
    else:
        "As I went to sleep I wondered why Ian hadn't texted me yet."
        "And why was I hoping for him to do it? I was just being silly..."
        
    jump v2lena_stan_photo

## LENA STAN PHOTOSHOOT #############################################################################################################################

label v2lena_stan_photo:
    $ day = "Tuesday"
    scene blackbg
    with long
    call screen calendar
    play music "music/normal_day.mp3" loop
    scene lenaroom
    with long
    show lenabra 
    with short
    $ stan_camera = True
    $ fstan = "sad"
    "I got up with the new day."
    if v2_sleep_louise:
        "Louise had already left. She always got up early to work on her master's degree."
        "I hadn't slept as comfortably having her glued to me all night, but not too bad either..."
        "Anyways, today was going to be a long day."
    else:
        l "Ahh... I didn't sleep too bad tonight but not too great either..."
        l "And today will be a long day."
    play sound "sfx/sms.mp3"
    l "A message this early in the morning? Who could this be...?"
    "Turns out it was Danny who had texted me."
    dan "{i}Hi Lena! Remember about that exposition I told you about?{/i}"
    dan "{i}It's going to be this Friday! It's a holiday, so a lot of people will be coming. Important ones, too!{/i}"
    dan "{i}I'm so excited to showcase my work, and you're the star of it! You can't miss it! I'm attaching the address below.{/i}"
    dan "{i}See you on Friday!{/i}"
    l "That's true, he told me he would expose his work in this important opening..."
    l "And I guess I already told him I'd go, right?"
    l "In any case, it's probably a good idea to do so. I should check it out at least."
    l "Who knows, it might be the right place at the right time to be."
    "As I was about to go get some breakfast I heard the the shutter of a camera."
    play sound "sfx/camera.mp3"
    "It came from the living room."
    scene lenahome
    show lola_b 
    show stan at lef3
    with long
    st "Not like this..."
    "I found Stan taking pictures of Lola."
    play sound "sfx/camera.mp3"
    st "Damn, I can't get it right..."
    show lenabra at rig3
    with short
    l "What are you doing?"
    $ fstan = "surprise"
    with vpunch
    st "Uh--! Oh, I'm..."
    st "I was just trying to take some pictures of Lola with my new camera, but I can't get it to focus properly..."
    menu:        
        "I can help you out":
            $ renpy.block_rollback()
            $ flena = "smile"
            l "I can help you out if you want. I've picked up several things after working with photographers."
            $ fstan = "shy"
            st "Really? That would be awesome."
            l "Here, let me see... Oh, this is a really good camera!"
            l "I didn't know you had one like this."
            st "I just bought it recently..."
            l "So are you trying to get into photography?"
            st "Yes... I always found it interesting and I decided it was time to give it a try..."
            st "I wanted to pick a new hobby, but I'm more clueless than I thought..."
            l "Getting the hang of it is half the fun. Look, you should use this ISO setting and focus like this..."
            st "Oh, I see..."
            play sound "sfx/camera.mp3"
            with flash
            "He tried my setup and took another photo of Lola."
            $ fstan = "smile"
            st "Oh, this is much better! It almost looks like a professional picture!"
            play sound "sfx/friendup.mp3"
            show friend_up
            $ lena_stan += 1
            l "Glad to help! It's not easy taking good pictures of a black cat."
            st "Thank you so much..."
            hide friend_up
            
        "That's a very nice camera":
            $ renpy.block_rollback()
            l "That's a very nice camera! Looks expensive, too. I didn't know you had one like this..."
            $ fstan = "blush"
            st "I just bought it recently..."
            l "So are you trying to get into photography?"
            st "Yes... I always found it interesting and I decided it was time to give it a try..."
            st "I wanted to pick a new hobby, but I'm more clueless than I thought..."
            l "Getting the hang of it is half the fun."
            
        "{image=icon_mad.png}Don't take photos of my cat" if lena_stan < 5:
            $ renpy.block_rollback()
            $ flena = "serious"
            l "Please, don't take pictures of my cat without my permission. It's rude."
            $ fstan = "sad"
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ lena_stan -= 2
            st "Oh... I'm sorry... I didn't think it would bother you..."
            l "Since when are you into photography, by the way?"
            st "Uh, I just picked up the hobby recently... I have no idea of what I'm doing yet..."
            l "You didn't need such a good camera to get started. That one looks really expensive."
            st "I wanted to have quality equipment..."
            $ flena = "n"
            l "A newbie doesn't need that. You'd be doing better with a simpler camera."
            st "OK... Thanks for the advice."
            hide friend_down


    if lena_stan > 2:
        $ fstan= "blush"
        st "Um, I..."
        st "I was wondering... Since you're a model and you know about photography..."
        st "Could you help me out?"
        l "Sure, what do you need?"
        st "I meant if you could... Or you would..."
        st "Would you pose for me?"
        $ flena = "surprise"
        l "You want to use me as a model?"
        st "W-{w=0.3}well, yeah. Since you're a pro and you know about the technical aspects..."
        menu:
            "{image=icon_money.png}I can do it, for a price":
                $ renpy.block_rollback()
                $ lena_stan_model_cash = True
                $ v2_lena_stan_model_shirt = True
                $ flena = "n"
                l "Hmm... Well, if you want to work with me I can tell you my rates."
                st "Oh, sure..."
                "I saw the opportunity of turning this into some extra work. That was always welcome..."
                "Even though I wasn't especially thrilled about working with Stan, but I told myself I had to be professional."
                l "What are you looking for, exactly?"
                st "Nothing special... Just taking a few pictures here in the living room to get some practice..."
                l "So you want me to pose as I am now?"
                $ fstan = "shy"
                st "Yeah, that would be nice."
                l "Alright, so that'll be the lingerie rate."
                st "Sounds good to me."
                l "So, tell me, how do you want me?"
                $ fstan = "blush"
                jump v2_stanmodelscene
                
            "{image=icon_friend.png}I'll be your model" if lena_stan > 4:
                $ renpy.block_rollback()   
                $ lena_stan_model_free = True
                $ flena = "worried"
                l "I guess I can help you out..."
                st "You'd do that? For real?"
                $ flena = "n"
                l "Sure, why not. Everyone starts somewhere..."
                l "If I can help a friend..."
                $ fstan = "shy"
                st "You're wonderful Lena, for real!"
                l "So tell me, what do you need?"
                jump v2_stanmodelscene
                
            "I don't think it's a good idea":
                $ renpy.block_rollback()  
                $ flena = "worried"
                l "I don't think it's a good idea, Stan."
                st "Oh."
                l "I try to work only with professionals. And we're flatmates, after all."
                l "I don't want to mix my personal life with my work."
                "I didn't want things to get weird..."
                st "Of course, I understand... Sorry for asking."
                l "It's OK. I'm gonna prepare some breakfast, do you want some?"
                st "No, thanks, I already ate."
                l "OK. You can keep practicing your camera skills with Lola. She's a good model, she doesn't move much."
                st "Sure..."
                "I prepared some breakfast, took a shower and went to work."
                jump v2_cafehollyscene
                
    else:
        "I prepared some breakfast, took a shower and went to work."
        jump v2_cafehollyscene

label v2_stanmodelscene:
    stop music fadeout 2.0
    st "Uh... You're the professional here. I'll trust your experience, so do whatever you want..."
    l "Mhh, OK. Let's see..."
    play music "music/sensual.mp3"
    scene lenahome
    show v2_stan1
    with long
    "I got in front of the kitchen counter and leaned on it, facing Stan."
    l "I think the light is good from this angle."
    st "Alright..."
    "I straightened my back and held my head up, adopting a modeling pose."
    play sound "sfx/camera.mp3"
    with flash
    "Stan took several pictures."
    l "Are they turning out OK?"
    st "I'd say so... Let me take a few more..."
    if lena_stan_model_cash:
        st "Um... By the way..."
        st "You charged me the lingerie rate, right?"
        l "Yes."
        st "Could you... remove your shirt, please?"
        l "Sure..."
        scene lenahome
        show v2_stan1b
        with long
        "As soon as I began pulling up my shirt, Stan took a picture."
        play sound "sfx/camera.mp3"
        with flash  
        l "Do you like this pose?"
        st "Y-{w=0.3}yeah."
        l "OK."
        "I held it for him to take a few more pictures."
        "I couldn't really see Stan's face, since it was hidden behind the camera at all times, but his hands were slightly trembling..."
        "Did I make him so nervous?"
        "I didn't know if it was funny or if I should feel bad. Probably a mix of both."        
    else:
        play sound "sfx/camera.mp3"
        with flash  
    st "OK, I'm getting the gist of it, I think."
    st "Could we try with another pose?"
    l "Sure."
    scene lenahome
    if lena_stan_model_cash:
        show v2_stan2b
    else:
        show v2_stan2
    with long
    if lena_stan_model_cash:
        "I finished removing my shirt and I turned around, resting my hands on the kitchen counter and leaning forward slightly."
    else:
        "I turned around and rested my hands on the kitchen counter, leaning forward slightly."
    l "I think you'll get a nice silhouette if you move to the left. There's a lot of light coming through the window this morning."
    st "OK..."
    "I arched my back a bit more, trying to give him an interesting shape to photograph."
    st "C-{w=0.3}could you... look to the camera over your shoulder?"
    l "Sure."
    "I did as he asked. It was clear he was having trouble making requests..."
    "Working with someone so insecure was a bit weird... His awkward vibe was rubbing onto me."
    if lena_stan_model_cash:
        "Thankfully, professional photographers were nothing like this, or photo-shoots would be a lot less comfortable..."
        "Though I couldn't really blame Stan for being awkward. He was clearly not used to it and was making great effort to get out of his comfort zone."
    else:
        "Though this wasn't really work. I was just helping out a friend..."
        "And I couldn't really blame Stan for being awkward. It was clear he was out of his comfort zone."
    play sound "sfx/camera.mp3"
    with flash  
    "He took several pictures, and took his time tinkering with the camera after each one."
    "He was a total newbie, that much was clear... And the shoot was beginning to drag out."
    l "Are you getting some good pictures?"
    if lena_stan_model_cash:
        st "I think so... Let's maybe try something else now?"
        l "Sure."        
    else:
        st "I think so... But I'm having trouble with the shirt."
        st "It casts a very weird shadow... Like way too dark and sharp."
        if lena_lust > 1:
            menu:
                "{image=icon_lust.png}Take your shirt off":
                    $ renpy.block_rollback()
                    $ v2_lena_stan_model_shirt = True
                    l "I can take it off if you want."
                    st "Really? If you don't mind..."
                    scene lenahome
                    show v2_stan2b
                    with long
                    "I took it off and resumed the pose."
                    l "Better now?"
                    st "Y-{w=0.3}yeah... Much better..."
                    play sound "sfx/camera.mp3"
                    with flash 
                    "He took a few more pictures. This time he wasn't stalling so much between each shot..."
                    st "OK... Let's maybe try something else now?"
                    l "Sure."  
                "Take it easy":
                    $ renpy.block_rollback()
                    l "Take it easy. Step by step."
                    l "You can't expect to get super good pictures on your first day."
                    jump v2_stanmodelsceneend
        else:
            l "Step by step. You can't expect to get super good pictures on your first day."
            jump v2_stanmodelsceneend
            
    scene lenahome
    show v2_stan3
    with long
    "I changed it up a bit and got on my knees this time."
    l "Get in front of the window. You don't want your light source behind your model, or you'll get a dark picture."
    st "That's basic, yeah..."
    "He stood behind his camera, pointing it at me, but didn't take any picture."
    "Maybe he was having trouble focusing the lens... But no, he was not moving at all."
    l "Is there a problem?"
    st "What? No, no, no. I just got a bit... distracted. Sorry."
    l "Is this pose OK?"
    st "It's perfect..."
    play sound "sfx/camera.mp3"
    with flash 
    "He finally began taking some pictures."
    st "It looks way too bright..."
    l "Change your ISO settings."
    st "Wait..."
    "That's why I usually didn't like to work with amateurs..."
    if lena_stan_model_free:
        "I had to remind myself I was just doing Stan a favor."
    play sound "sfx/camera.mp3"
    with flash
    st "OK, now it looks better."
    l "I'm running out of time..."
    if lena_stan_model_cash:
        scene lenahome
        show v2_stan4
        with long
        l "Let's do a final quick one."
        "Stan was paying me after all, so I decided to give him something more before calling it quits."
        st "Great... Thank you so much, Lena..."
        st "Oh, I love this pose... Hold it..."
        play sound "sfx/camera.mp3"
        with flash 
        "He got on his knees and continued to take pictures."
        play sound "sfx/camera.mp3"
        with flash 
        st "Oh, yeah..."
        "He wasn't checking the pictures or the camera settings between shots now, like there was no doubt in him anymore."
        "He just took picture after picture, varying his angles slightly."
        "At one point I felt like his focal point was right between my legs..."
        play sound "sfx/camera.mp3"
        with flash 
        "Maybe he was getting too carried away, now..."
        l "OK, that's enough."
        
label v2_stanmodelsceneend: 
    $ flena = "n"
    $ fstan = "shy"
    stop music fadeout 2.0
    scene lenahome
    if lena_stan_model_cash or v2_lena_stan_model_shirt:
        $ lena_look = 2
        show lenabra2 at rig
        if lena_stan_model_cash:
            $ fstan = "perv"
    else:
        show lenabra2 at rig
    show stan at lef
    with long
    l "It's getting late and I need to get ready for work."
    st "Of course..."
    if lena_stan_model_cash:
        st "Here's your payment..."
        $ lena_money += 1
        play sound "sfx/moneyup.mp3"
        show money_up
        l "Thanks!"
        "That was some easy money, that photo-shoot had barely lasted thirty minutes!"
    else:
        st "Thanks you so much for your help, Lena."
    st "I'm sorry I'm such a noob right now. I hope I'll get better."
    l "Keep practicing and at some point maybe you'll be able to take really good pictures!"
    st "Will do."
    l "Stan, could you prepare some breakfast for me? I still need to take a shower and get dressed and I'm in a bit of a hurry..."
    l "Just a couple of toasts and coffee, doesn't have to be anything fancy!"
    $ fstan = "smile"
    st "Sure, don't worry. I'll do it gladly."
    l "Thanks!"
    $ gallery_scene5 = True
    play music "music/normal_day.mp3" loop

###### CAFE HOLLY ##################

label v2_cafehollyscene:
    
    scene cafe
    with long
    $ lena_look = 1
    $ flena = "n"
    "I arrived on time at the café."
    show lena
    with short
    l "Good morning!"
    show molly at lef3
    with short
    mo "Good morning, Lena!"
    l "You look cheerful today, Molly. Are you feeling better?"
    mo "Yes, much better."
    l "Ed's out shopping?"
    mo "Yes. I asked him to get some raspberries for a new cake I want to make... You'll see, it'll be delicious!"
    l "Can't wait to try it. I'm gonna get changed!"
    mo "Sure!"
    hide molly
    with short
    "I went into the back room and stripped down."
    hide lena
    show lenaunder
    with short
    $ lena_look = 2
    "I was about to get changed when I got a text message."
    play sound "sfx/sms.mp3"
    if v2_ian_date:
        "It was Ian's."
        $ flena = "smile"
        i "{i}Wednesday sounds good! Is there something specific you wanted to do?{/i}"
        "I hadn't thought about anything..."
        l "{i}I don't know, do you have any suggestions?{/i}"
        i "{i}Not really... But we can just take a stroll and do whatever in the spur of the moment.{/i}"
        l "{i}Going with the flow, I like that. See you tomorrow then!{/i}"
        "So it was a done deal. I was going to meet Ian tomorrow morning..."
    else:
        "It was Robert's."
        r "{i}Hey Lena, how are you doing? I heard that asshole didn't show up again at the hotel during the weekend.{/i}"
        "I texted him back."
        l "{i}No, everything's been calm since Friday.{/i}"
        r "{i}Good to hear. See you tonight, right?{/i}"
        l "{i}Yeah. Gotta get to work, see you at night. Bye.{/i}"
    
    play sound "sfx/door.mp3"
    $ flena = "surprise"
    $ fed = "surprise"
    $ lena_look = 2
    hide lenaunder
    show lenabra2
    show ed at left
    with short
    with vpunch
    "Suddenly Ed opened the door. He was carrying groceries in each hand."
    if v1_ed_truth:
        $ fed = "n"
        $ flena = "blush"
        ed "Oh, good morning, Lena."
        "Ed came in despite me being in my underwear and proceeded to put the groceries on the shelves."
        l "Uh... Good morning?"
        menu:
            "Call him out":
                $ renpy.block_rollback()
                $ ed_callout = True
                l "Excuse me... I'm getting changed over here."
                $ fed = "sad"
                ed "Uh?"
                "He turned around and looked at me again, like he wasn't getting my point."
                l "I would like some privacy, if you don't mind..." 
                ed "Oh. Oh my!"
                ed "I'm so sorry! Since you told me you were doing that modeling stuff I didn't think you'd be bothered by it..."
                "I knew it. Letting him know about my other line of work hadn't been a good idea..."
                l "It bothers me in this context. I feel it's kinda inappropriate."
                $ lena_ed -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                ed "Of course, my bad. Sorry about that."
                hide ed
                with short
                $ fed = "n"
                "He finally got the message and left."
                $ flena = "sad"
                hide lenabra2
                show lenaunder
                with short
                $ lena_look = 1
                "That had been uncomfortable... I hope I had made things clear for him."
                "I really liked this job, and I would hate it if other aspects of my life messed it up..."
                hide lenaunder
                show lenawork
                with short
                "I finished getting changed and prepared to get work started."

            "Say nothing":
                $ renpy.block_rollback()
                l "..."
                "I decided it was best to not say anything and try to act normal."
                "I didn't want to make the situation even more awkward..."
                "He had learned I was doing nude modeling and he now thought he could walk around while I was in my underwear like it was no big deal."
                "I feared this could happen, that's why I was reluctant to tell him in the first place..."
                hide lenabra2
                show lenaunder
                with short
                $ lena_look = 1
                "He finished organizing his groceries while I finished getting changed."
                hide lenaunder
                show lenawork
                with short
                $ fed = "smile"
                ed "You look in a good mood today! Ready for work?"
                l "Yeah..."
                $ lena_ed += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                ed "Good, good! Let's get started, then!"
                $ flena = "n"
                l "Alright."
                "I guessed it wasn't such a big deal, after all. If Ed wasn't concerned about this situation, why should I be?"
                "Maybe I was just making a big deal of something that really wasn't. That was so unlike me..."
        
    elif v1_ed_flirt:
        $ fed = "smile"
        $ flena = "blush"
        ed "Oh, good morning, Lena. How are you feeling today?"
        l "Um... I'm fine, thanks..."
        ed "Good, good."
        "He looked at me and smiled before proceeding to put the groceries on the shelves."
        "He not only didn't seem to mind me being in my underwear, but he also was looking at me quite unapologetically."
        menu:
            "Call him out":
                $ renpy.block_rollback()
                $ ed_callout = True
                $ flena = "serious"
                l "Excuse me... I'm getting changed over here."
                $ fed = "sad"
                ed "Uh?"
                "He turned around and looked at me again, like he wasn't getting my point."
                $ flena = "serious"
                l "I would like some privacy, if you don't mind. This is kinda inappropriate."
                ed "How come? You didn't seem bothered by it the other day..."
                ed "And now it's inappropriate all of a sudden?"
                "I knew it. He had gotten some weird ideas after what happened last time..."
                l "I didn't say it was appropriate last time. And you're making me feel uncomfortable, so please get out while I'm not done changing!"
                $ lena_ed -= 2
                play sound "sfx/frienddown.mp3"
                show friend_down
                $ fed = "mad"
                ed "Alright, alright! Don't make a fuss over it!"
                hide ed
                with short
                $ fed = "n"
                "He finally left."
                $ flena = "sad"
                hide lenaunder
                show lenabra2
                with short
                $ lena_look = 1
                "That had been really uncomfortable... I shouldn't have let things get this far in the first place..."
                "I really liked this job, and I didn't want to mess it up. And maybe I had done just that..."
                hide lenabra2
                show lenawork
                with short
                "I finished getting changed and prepared to get work started."
                
            "Say nothing":
                $ renpy.block_rollback()
                l "..."
                "I decided it was best to not say anything and try to act normal."
                "I didn't want to make the situation even more awkward..."
                "And it had been me who had kinda led him on last time. No wonder he now thought he could walk around while I was in my underwear like it was no big deal."
                hide lenabra2
                show lenaunder
                with short
                $ lena_look = 1
                "He finished organizing his groceries while I finished getting changed."
                hide lenaunder
                show lenawork
                with short
                $ fed = "smile"
                ed "You look in a good mood today! Ready for work?"
                l "Yeah..."
                $ lena_ed += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                ed "Good, good! Let's get started, then!"
                $ flena = "n"
                l "Alright."
                "I guessed it wasn't such a big deal, after all. If Ed wasn't concerned about this situation, why should I be?"
                "Maybe I was just making a big deal of something that really wasn't. That was so unlike me..."
        
    else:
        ed "Oh, sorry!"
        $ flena = "blush"
        hide ed
        with short
        $ fed = "sad"
        "He quickly turned around and left the room."
        hide lenabra2
        show lenaunder
        with short
        $ lena_look = 1
        hide lenaunder
        show lenawork
        with short
        "I got dressed quickly and got out."
        show ed at lef3
        ed "I'm sorry Lena, I can't believe it happened again."
        l "It's OK..."
        ed "I'll be sure to knock from now on!"
        $ flena = "n"
        l "That's a good idea. Let's get to work."
        $ fed = "n"
        ed "Let's."
         
    hide ed
    with short
    $ fed = "n"
    $ fholly = "n"
    $ flena = "n"
    "The morning went by as usual."
    "There weren't many customers today, either..."
    if v1_alisonlunch:
        "After some long minutes of inactivity a new customer finally came in."
        show lenawork at rig
        with move
        show holly2 at lef
        with short
        l "Welcome, take a seat, please. What would you like to order?"
        h "I'd like a chai latte, please."
        l "Right away."
        "As I prepared the tea I looked at her. She looked familiar, for some reason."
        "Where had I seen her face before...?"
        l "Here you go."
        h "Thank you..."
        "She had a couple of notebooks on the table, and it looked like she was writing notes for some kind of book or story..."
        l "Wait a minute..."
        $ flena = "surprise"
        l "You're Holly Watson?"
        l "The author of \"The Ice Flower\"?"
        h "Y--{w=0.5}Yes."
        $ flena = "happy"
        $ lena_holly_agenda = True
        "That's why her face looked familiar! I had just read her book a few weeks ago, and her picture was on the back cover."
        l "Wow, I can't believe it! I've enjoyed reading your books a lot!"
        $ fholly = "shy"
        h "Oh, really? Thank you..."
        l "It's true! Oh God, sorry for acting like a fan girl just now. I wasn't expecting to meet you like this."
        h "It's OK... What's your name?"
        $ flena = "smile"
        l "Oh, I haven't told you, sorry. I'm Lena."
        $ fholly = "smile"
        h "Nice to meet you, Lena. You've been working here for a month or so, right?"
        l "More or less, yeah. I knew we lived in the same city, but I can't believe you have been coming to this cafe all along. What a surprise."
        $ holly = "shy"
        h "It's a surprise for me, too, you know. I'm not used to people recognizing me, or praising my book. It doesn't happen often."
        l "I hope you just meant the part about being recognized. Your books are becoming quite popular."
        $ fholly = "smile"
        h "Yes, it seems they are. I'm not used to that yet, either!"
        "I pointed at her open notebook."        
    else:
        "Then I saw a familiar face come in."
        show lenawork at rig
        with move
        show holly2 at lef
        with short
        l "Oh, hi Holly!"
        h "Good afternoon."
        "It seemed she was coming alone today."
        l "What's it gonna be today?"
        h "I'd like a chai latte, please."
        l "Right away."
        "When I brought her the drink I found her going through a notebook full of notes and little drawings."
    l "Is that where you write down your ideas for your books?"
    h "Yeah... And not just the idea, most of the time I end up writing almost the whole book like this."
    $ flena = "smile"
    l "You must have tons of notebooks then!"
    $ fholly = "smile"
    h "You have no idea... There's barely any room left for me in my own bedroom!"
    h "Some people say I'm too young to be this old-school, and nowadays everyone writes on their computers, but what can I say..."
    h "I just like it better putting pen to paper and writing. It feels more... personal."
    l "I know! It's the same with me! Seems like we're a dying breed, ha ha."
    h "You write, too?"
    $ flena = "shy"
    l "Well, not exactly... I mean, I don't write books, but I like writing poetry and songs as a hobby."
    $ fholly = "happy"
    h "Really? That's so cool! I love poetry, but I'm not very good at it."
    $ flena = "smile"
    l "That's not true. There was this poem in your book that I really loved... It was so good!"
    $ fholly = "shy"
    h "Thank you... I just like to sneak one in from time to time."
    $ fholly = "smile"
    h "I've never written a song, though. Would you share one of yours with me?"
    $ flena = "shy"
    l "One of mine? Oh, wow, I don't know..."
    h "You don't have to, of course."
    l "No, it's not that, I'd love to... But I'm a bit nervous showing something like that to a writer I admire!"
    l "You're a true professional, after all."
    $ fholly = "n"
    h "I've just started my professional career, so I'm not so different from any other novice author..."
    h "And I know how hard it can be showing your work to others... The doubts you have about yourself, the fear of what people might say..."
    h "Some critics can be very harsh..."
    h "But you'll always find people who like what you do! Some might even love it."
    menu:
        "I'll share a song with you":
            $ renpy.block_rollback()
            $ v2_holly_song = True
            $ flena = "smile"
            l "Sure, I'll share one of my songs with you." 
            $ fholly = "happy"
            h "Thank you."
            l "No, thank you! I can't believe I'm gonna get the opinion of a writer I admire."
            $ flena = "sad"
            l "But it's been a long time since I wrote anything... And I guess my old songs aren't that good."
            h "You haven't been writing lately?"
            l "No... Life just got in the way, I guess. I should find more time for it..."
            h "It's important to keep your passion alive. And with writing, it's something only you can do..."
            $ lena_holly += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            $ flena = "smile"
            h "In any case, thank you for your willingness to share that with me. It's always nice meeting someone you can share these kinds of things with..."
            $ fholly = "n"
            h "And I don't have many friends like that, to be honest..."
            $ flena = "happy"
            "I smiled at her."
            l "We can find a solution to that."
            $ fholly = "happy"
            h "You are so nice!"
            $ flena = "smile"
            l "Thanks, ha ha. So, shall we exchange numbers and meet one of these days? I should be working right now..."
            $ fholly = "smile"
            h "Sure, don't let me keep you."
            
        "I'd rather not":
            $ renpy.block_rollback()
            $ flena = "worried"
            l "I think I rather not..."
            l "I haven't written anything for the longest time, and I'm sure it won't be up to your standards..."
            "I wasn't ready to share what I wrote with her. She was a professional writer, I was sure she'd find my stuff laughable."
            "I felt more comfortable sharing with people who were not that exceptional..."
            $ fholly = "sad"
            h "Oh, I'm sure that's not the case... But I respect you wanting to keep it to yourself."
            $ fholly = "n"
            h "I was like that for a long time, too. To be honest, I haven't gotten used to people reading my books yet..."
            $ flena = "n"
            l "Well, they're very good. Most people think so, me amongst them."
            h "Thank you for your kind words."
            if v1_alisonlunch:
                l "It's been so cool meeting you, Holly!"
            else:
                l "It's been so cool having the chance of talking to you, Holly!"
                h "Anytime!"
            l "I'd like to keep chatting with you about your books and stuff, but I have to get back to work now..."
            h "We can meet some day if you want..."
            $ flena =  "happy"
            l "Really? That would be so cool. Let's exchange numbers!"
            $ fholly = "smile"
            h "Sure."
            
    "We got each other's numbers and I went back to work."
    hide holly
    hide holly2
    with short
    "How cool to have the opportunity to hang out with Holly Watson! I loved her books, and she looked like such a nice girl!"
    if v1_alisonlunch == False:
        "Maybe Ian, her and me could hang out together."
    else:
        "It had been such an unexpected and pleasant surprise."
    "Just this had made the day worth it."            
            
##RESTAURANT #########################################################
    
    stop music fadeout 2.0
    $ robert_hurt =1
    $ v2_rbt_now = False
    $ frobert = "n"
    $ robert_look = 2
    scene restaurant
    with long
    "After I was done at the café my shift at the restaurant began."
    $ flena = "n"
    $ lena_look = 2
    play music "music/fancy.mp3"
    show lenawork
    with short
    "Monday and Wednesday were my days off, sometimes Saturday too."
    "It was Tuesday, so I felt fresh and ready to take on the night. And there was no sign of Axel, which was a good thing, too..."
    show lenawork at rig with move
    show robert at lef with short
    r "There you are."
    $ flena = "worried"
    l "Hey, Robert. How are you?"
    "Robert rarely worked during weekends, so I hadn't seen him since Friday's incident."
    r "My face's still a bit swollen, but all in all I'm alright."
    $ flena = "sad"
    l "I'm so sorry about what happened... God, I'm so ashamed."
    r "Hey, it wasn't your fault... You used to date a psycho, that's all."
    l "I had never seen him lose his mind like that. I'm so sorry you got hurt because of him."
    r "Don't worry. I just can't stand assholes like him. I couldn't let him treat you like that."
    menu:
        "{image=icon_friend.png}I owe you a drink!":
            $ renpy.block_rollback()
            $ v2_robert_invite = True
            $ v2_robert_date = True
            $ v2_robert_spoiler = False
            $ flena = "happy"
            l "Hey, let me show you my gratitude by buying you a drink! We've had that pending for quite a while now, right?"
            $ lena_robert += 2
            play sound "sfx/friendup.mp3"
            show friend_up
            $ frobert = "smile"
            r "Oh, yeah! I would love to get a few drinks with you tonight. But you don't have to pay for them, don't worry!"
            l "I didn't say tonight, but... Why not, let's go after the shift's over."
            hide robert
            with short
            $ flena = "n"
            show lenawork at truecenter 
            with move
            l "I could really use a distraction tonight."
            if v2_ian_date:
                "I shouldn't take too long though, since I had to get up early to meet Ian next morning."
        
        "Thank you, Robert":
            $ renpy.block_rollback()
            $ flena = "smile"
            l "Thanks, Robert."
            $ frobert = "smile"
            r "You know how you could show me your gratitude?"
            l "No, tell me."
            r "By getting some drinks with me tonight after we're done here."
            r "We've had that pending for quite a while, haven't we?" 
            hide friend_up
            menu:
                "Alright, let's do that":
                    $ renpy.block_rollback()
                    $ v2_robert_date = True
                    $ v2_robert_spoiler = False
                    l "Alright, let's do that..."
                    $ frobert = "smile"
                    $ lena_robert += 1
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    r "Cool! I know just the place, let's go after the shift's over."
                    l "OK."
                    hide robert
                    with short
                    $ flena = "n"
                    show lenawork at truecenter 
                    with move
                    l "So I guess I'll be going out for drinks after my shift..."
                    if v2_ian_date:
                        "I shouldn't take too long, since I had to get up early to meet Ian next morning."
                    
                "No, thanks":
                    $ renpy.block_rollback()
                    $ v2_robert_spoiler = True
                    $ flena = "n"
                    l "Thanks for the offer, but no... I'm not feeling it tonight, Robert..."
                    $ frobert = "n"
                    r "Come on, it'll do you good. Besides, I have something important to tell you."
                    $ flena = "worried"
                    l "Something important?"
                    r "Yes, something I've heard being discussed, and it involves you."
                    l "What is it?"
                    r "This is not the best place for me to talk about that..."
                    $ frobert = "smile"
                    r "Let's go get that drink after work and we can talk calmly."
                    jump v2robertoffer
            
        "I didn't need your help":
            $ renpy.block_rollback()
            $ flena = "serious"
            $ v2_robert_spoiler = True
            l "Robert, just so we're clear, I didn't need your help."
            $ lena_robert -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ frobert = "serious"
            r "Where's that coming from? I got punched in the face because of it, you know?"
            l "I thought you said just a moment ago that it wasn't my fault."
            $ frobert = "sad"
            r "And it's not, that's not what I meant...!"
            r "I'm just saying I could get a \"thank you\" in return. Or we could go get some drinks together tonight after we're done here."
            $ frobert = "n"
            r "We've had that pending for quite a while, haven't we?"   
            hide friend_down
            l "I don't know, I'm not feeling it tonight, Robert..."
            r "Come on, it'll do you good. Besides, I have something important to tell you."
            $ flena = "worried"
            l "Something important?"
            r "Yes, something I've heard being discussed, and it involves you."
            l "What is it?"
            r "This is not the best place for me to talk about that..."
            $ frobert = "smile"
            r "Let's go get that drink after work and we can talk calmly."
            menu v2robertoffer:
                "Alright, let's do that":
                    $ renpy.block_rollback()
                    $ v2_robert_date = True
                    if v2_rbt_now or lena_robert < 4:
                        $ flena = "n"
                    else:
                        $ flena = "smile"
                    l "Alright, let's do that."
                    $ frobert = "smile"
                    $ lena_robert += 1
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    r "Cool!"
                    l "But promise you will tell me, whatever it is!"
                    r "Of course! I would never keep you in the dark with something like this."
                    r "Well, let's take care of work. The sooner we're done here the sooner we'll be able to leave."
                    $ frobert = "n"
                    r "Set up tables one to ten, and don't forget to make sure the cutlery is clean!"
                    l "Yes, sir."
                    hide robert
                    with short
                    $ flena = "n"
                    show lenawork at truecenter 
                    with move
                    l "So I guess I'll be going out for drinks after my shift..."
                    if v2_ian_date:
                        "I shouldn't take too long, since I had to get up early to meet Ian next morning."
                    l "I wonder what's so important he has to tell me..."            
                    
                "Tell me now" if v2_rbt_now == False:
                    $ renpy.block_rollback()
                    $ v2_rbt_now = True
                    $ flena = "serious"
                    l "Why can't you tell me now?"
                    $ frobert = "n"
                    r "I don't want to discuss work related things here... I've already said too much."
                    l "But I want to know now."
                    r "You'll know in a few hours if you come with me to grab a drink!"
                    jump v2robertoffer
                    
                "I'll pass":
                    $ renpy.block_rollback()
                    $ flena = "sad"
                    $ v2_robert_reject = True
                    l "Sorry, Robert, but I'll pass."
                    $ frobert = "sad"
                    r "Why?"
                    l "For the same reason I've passed all the other times you proposed the same thing."
                    if v2_ian_date:
                        l "Besides, I'm meeting someone tomorrow morning, and I have to get up early."
                        l "I don't want to stay up until late tonight."
                        $ frobert = "mad"
                        r "Oh, I see. So that's how it is."
                    else:
                        l "My life is pretty busy right now and I can't afford to go out so late at night."
                        l "I need to get some rest, you know?"
                        $ frobert = "serious"
                        r "You could try to come up with a better excuse."
                    $ flena = "serious"
                    $ lena_robert = 2
                    play sound "sfx/frienddown.mp3"
                    show friend_down
                    r "You're not gonna find many guys who would take a punch to the face for you, you know?"
                    l "Maybe that's not what I'm after."
                    r "OK, OK. Suit yourself."
                    hide robert
                    with short
                    "He turned around and went to take care of his work."
                    $ flena = "sad"
                    show lenawork at truecenter 
                    with move
                    "It was clear Robert wasn't pleased with my answer. But I didn't like his antics."
                    "He had tried to bait me into going out with him by withholding some kind of important information..."
                    "Of course, he hadn't told me. I wondered what it could be..."
                    l "It's probably nothing important and he was just looking for an excuse to persuade me..."
            
    "The night was intense, as always. Working in this high-class restaurant could get really stressful."
    "There were a lot of tables to serve and not many employees to take care of it. And the service had to be exquisite."
    $ flena = "worried"
    "After taking all the customers' orders, carrying around many plates and pouring countless glasses of wine my shift ended."
    stop music fadeout 2.0
    if v2_robert_date:
        show lenawork at rig 
        with move
        $ frobert = "smile"
        l "Whew, I'm beat..."
        show robert at lef
        with short
        r "We're finally done! Let's get changed and go get those drinks. I know just the place."
        $ flena = "n"
        l "OK."
        jump v2_robertdatescene
    else:
        "Was it my imagination or had Robert been avoiding me the whole night?"
        "Not that I really cared..."
        "I got changed and went back home to get a good night's sleep, or at least try."
        jump v2_predate

##ROBERT DATE ##########################################################################################################################################################################################################

label v2_robertdatescene:
    
    $ v2_rbt_wait = False
    $ v2_rbt_wait2 = False
    
    scene streetnight
    with long
    $ lena_look = 1
    $ flena = "n"
    $ robert_look = 1
    show lena at rig
    show robert at lef3
    with short
    r "Ready?"
    l "Yeah. Where are we going?"
    r "It's a very nice cocktail bar called Shine. It's nearby. You'll like it."
    if v2_ian_date:
        l "Alright. I shouldn't stay too long, though. It's late and tomorrow morning I have something to do..."
    else:
        l "Alright. I shouldn't stay too long, though. It's late and tomorrow I have work at the café."
    r "Sure, don't worry. Let's go."
    
    play music "music/flirty.mp3"
    scene cocktailbar
    with long
    "I followed Robert to the bar he had spoken about."
    "It was a nice place indeed, one of those fancy businesses that had been opening recently in the downtown area."
    show lena at rig
    show robert at lef3
    with short
    r "Let's take a seat over there. Do you like the place?"
    menu:
        "It's really nice!":
            $ renpy.block_rollback()
            $ lena_posh += 1
            $ flena = "smile"
            l "Yes, I like it! It's really nice, and it has style."
            r "I knew a girl like you would like this bar."
            
        "It's OK":
            $ renpy.block_rollback()
            l "Yes, it's OK."
            r "I really like it, it has style!"
            
        "Not my style":
            $ renpy.block_rollback()
            $ lena_posh -= 1
            l "It's not my style, to be honest. Too pretentious and fancy."
            r "Why's this pretentious? It's just a place with style."
            r "I thought you'd like it."
            l "I guess I prefer quieter places that feel more... cozy."
            
    r "Let me get you a drink. They make good mojitos here. Want one?"
    l "Alright."
    $ flena = "n"
    "Robert went to the bar and returned shortly after with the drinks. He sat down in front of me and leaned forward on his arm."
    show robert at lef
    with move
    $ frobert = "smile"
    r "So... We should've done this a long time ago, don't you think?"
    if v2_robert_invite:
       l "Yeah, I guess you're right." 
    else:
        l "Eh... I guess?"
    r "We've been working together for several months, but this is the first time we're meeting outside of the restaurant!"
    r "I have so many questions about you..."
    if v2_robert_spoiler:
        menu rbtbarone:
            "Tell me that important thing" if v2_rbt_wait == False:
                $ renpy.block_rollback()
                $ v2_rbt_wait = True
                l "Could you please tell me that important thing you spoke about?"
                $ frobert = "n"
                r "You don't need to be so impatient... Why don't we talk a bit first?"
                r "I've been wanting to talk with you for so long..."
                l "You said it was important."
                $ frobert = "smile"
                r "Not as important as us getting to know each other!"
                jump rbtbarone
                
            "Make conversation with Robert":
                $ renpy.block_rollback()
                if v2_rbt_wait:
                    l "Alright... What do you want to ask about me?"
                    r "I don't know, many things..."
                else:
                    l "Is that so? Ask away, then."
                    r "Where to start...?"
                r "I've always wondered if you were single."
                r "I guess you are, considering that psycho of an ex-boyfriend you have."
                l "Yes, I've been single for about half a year."
                r "That's rare!"
                l "Why?"
                r "You're such a pretty girl... I imagine you'd have a ton of guys after you... Especially considering you're a model!"
                $ flena = "surprise"
                l "You know about that?"
                $ frobert = "n"
                r "Yes... Let's say I searched for you on social media and well, I saw your profile."
                $ flena = "n"
                l "I see... "
                "I guess I shouldn't be surprised about him knowing. It was pretty easy finding people's profiles on the Internet if you tried."
                menu:
                    "What did you think about it?":
                        $ renpy.block_rollback()
                        $ flena = "shy"
                        l "So... What did you think about it?"
                        r "About what?"
                        l "My photos."
                        $ frobert = "smile"
                        $ lena_robert += 1
                        play sound "sfx/friendup.mp3"
                        show friend_up
                        r "Do you really need to ask? I absolutely loved them!"
                        $ flena = "smile"
                        l "Really?"
                        r "Of course, who wouldn't? You're super pretty and hot!"
                        r "I already liked you, but after seeing those, I like you even more."
                        l "Oh... Thank you, Robert."
                        play sound "sfx/xp.mp3"
                        show lust_up
                        $ lena_lust_xp += 1
                        call screen skillsup
                        r "Just being honest, babe."
                        hide friend_up
                        hide lust_up
                        
                    "You never told me you knew":
                        $ renpy.block_rollback()
                        l "You never told me you knew about my modeling job."
                        r "I never found the right moment to do it, until now."
                        r "I didn't want to bother you at work, since you never mentioned it yourself..."
                        $ flena = "smile"
                        l "That's nice of you."
                        $ frobert = "smile"
                        
                    "That's a bit creepy":
                        $ renpy.block_rollback()
                        $ flena = "worried"
                        l "That's a bit creepy..."
                        $ frobert = "sad"
                        $ lena_robert -= 1
                        play sound "sfx/frienddown.mp3"
                        show friend_down
                        r "Creepy? Why?"
                        l "People looking you up on the Internet without you knowing..."
                        r "Well, I only saw what you uploaded. If you don't want people to see, why upload it at all?"
                        $ frobert = "n"
                        r "I mean, it's only normal for people to see your social media, isn't it?"
                        l "I guess so..."            
                        hide friend_down
                        
                r "So how come you're a model and a waitress?"
                $ flena = "n"
                l "I wouldn't really say I'm a model... I mean, I do professional modeling from time to time, but it's not really my profession, I guess..."
                "I told Robert a bit about my modeling gigs, how I got started and how I felt about it."
                r "I see, I see..."
                
            "I want you to tell me right now" if v2_rbt_wait:
                $ renpy.block_rollback()
                $ flena = "serious"
                l "Robert, I want to hear it right now. That's the reason I've come here tonight!"
                $ frobert = "sad"
                r "So that's the only reason?"
                if lena_robert > 4:
                    r "And here I thought we were having fun..."
                    l "That's not the point..."
                else:
                    r "That's not nice..."
                l "Look, it was you who told me you had something really important to say, and couldn't tell me at the restaurant."
                play sound "sfx/xp.mp3"
                show wits_up
                $ lena_wits_xp += 1
                call screen skillsup
                l "Here we are, so cut to the chase and tell me already."
                $ frobert = "serious"
                if lena_robert > 4:
                    $ lena_robert -= 2
                else:
                    $ lena_robert -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                r "I didn't know you could be so unpleasant, Lena."
                l "Are you gonna tell me or not?"
                r "Alright, alright..."
                $ frobert = "n"
                hide friend_down
                jump v2_robertdatescene2
    else:
        l "Is that so? Ask away, then."
        r "Where to start...?"
        r "I've always wondered if you were single."
        $ frobert = "n"
        r "I guess you are, considering that psycho of an ex-boyfriend you have..."
        l "Yes, I've been single for about half a year."
        $ frobert = "smile"
        r "That's rare!"
        l "Why?"
        r "You're such a pretty girl... I imagine you'd have a ton of guys after you... Especially considering you're a model!"
        $ flena = "surprise"
        l "You know about that?"
        $ frobert = "n"
        r "Yes... Let's say I searched for you on social media and well, I saw your profile."
        $ flena = "n"
        l "I see... "
        "I guess I shouldn't be surprised about him knowing. It was pretty easy finding people's profiles on the Internet if you tried."
        menu:
            "What did you think about it?":
                $ renpy.block_rollback()
                $ flena = "shy"
                l "So... What did you think about it?"
                r "About what?"
                l "My photos."
                $ frobert = "smile"
                $ lena_robert += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                r "Do you really need to ask? I absolutely loved them!"
                $ flena = "smile"
                l "Really?"
                r "Of course, who wouldn't? You're super pretty and hot!"
                r "I already liked you, but after seeing those, I like you even more."
                l "Oh... Thank you, Robert."
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
                r "Just being honest, babe."
                hide friend_up
                hide lust_up
                
            "You never told me you knew":
                $ renpy.block_rollback()
                l "You never told me you knew about my modeling job."
                r "I never found the right moment to do it, until now."
                r "I didn't want to bother you at work, since you never mentioned it yourself..."
                $ flena = "smile"
                l "I see. That's nice of you."
                $ frobert = "smile"
                
            "That's a bit creepy":
                $ renpy.block_rollback()
                $ flena = "worried"
                l "That's a bit creepy..."
                $ frobert = "sad"
                $ lena_robert -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                r "Creepy? Why?"
                l "People looking you up on the Internet without you knowing..."
                r "Well, I only saw what you uploaded. If you don't want people to see, why upload it at all?"
                $ frobert = "n"
                r "I mean, it's only normal for people to see your social media, isn't it?"
                l "I guess so..."            
                hide friend_down
                
        r "So how come you're a model and a waitress?"
        $ flena = "n"
        l "I wouldn't really say I'm a model... I mean, I do professional modeling from time to time, but it's not really my profession, I guess..."
        "I told Robert a bit about my modeling gigs, how I got started and how I felt about it."
        r "I see, I see..."
        
    $ frobert = "smile"
    r "Look, we're almost done with our drinks. Why don't we get another one?" 
    if v2_robert_spoiler:
        menu rbtbar2:
            "Tell me that important thing" if v2_rbt_wait2 == False:
                $ renpy.block_rollback()
                $ v2_rbt_wait2 = True
                l "So, about that important thing you had to tell me..."
                l "What's it about?"
                $ frobert = "n"
                r "Uh? Oh that. I'm gonna tell you, but I'm having such a great time chatting with you."
                $ frobert = "smile"
                r "You're not in a hurry, right? Let's get another mojito."
                jump rbtbar2
                
            "Get another drink":
                $ renpy.block_rollback()
                if v2_rbt_wait2:
                    l "Alright... Just one more, OK?"
                    r "Sure."
                else:
                    l "OK, we can have another one."
                    r "Cool!"
                hide robert
                with short
                "Robert got up and ordered another round of drinks."
                if lena_robert > 4:
                    "I was having a surprisingly good time that night. I wasn't expecting it..."
                elif lena_robert > 3:
                    "I wasn't having a bad time, but I just wished he'd cut to the chase and tell me that important thing."
                else:
                    "He was persistent... I decided to indulge him a bit more, hoping he would tell me that important thing already."  
                show robert at lef
                with short
                r "Here you go."
                r "You know, I might've gotten punched in the face, but working at the restaurant has gotten a lot more interesting since you showed up."
                l "Is that so?"
                r "Yeah, I've been working there for three years now, being head waiter for one..."
                r "It's not a small achievement, especially in such a prestigious restaurant as Yunalesca, but it can get kinda dull, to be honest!"
                l "It's not the most exciting job, yeah."
                r "Not as exciting as being a model, that's for sure, ha ha! But not everybody can do that..."
                r "I would've loved to be a football player, or maybe a fireman... I don't know which one is cooler."
                l "I'd say the fireman, ha ha."
                l "So, how come you ended up as a professional waiter?"
                r "Nah, I don't know. I guess school bored me too much to stick with higher education and I went for something practical. Something that could get me some money easily, you know?"
                r "I didn't like depending on my parents for money. I wanted to live my own life, have my own money and be able to do what I wanted."
                l "I'd say we're pretty similar on that regard."
                r "It seems that way!"
                r "Tell me... What do you think about me, Lena?"
                menu:
                    "{image=icon_friend.png}I like you" if lena_robert > 4:
                        $ renpy.block_rollback()
                        l "I like you."
                        $ lena_robert += 1
                        play sound "sfx/friendup.mp3"
                        show friend_up
                        r "You do?"
                        $ flena = "blush"
                        "The drink was making me lose a bit of control on how I expressed things." 
                        l "I mean, you seem like a cool guy."
                        $ frobert = "flirt"
                        r "How am I a cool guy?"
                        $ flena = "shy"
                        l "I mean, how do you say this?"
                        "Was he making me nervous? How?"
                        $ flena = "smile"
                        l "You're hardworking, you seem to have your priorities straight and you're not ashamed of yourself."
                        l "And you're not hard on the eyes either, ha ha!"
                        play sound "sfx/xp.mp3"
                        show charisma_up
                        $ lena_charisma_xp += 1
                        call screen skillsup
                        r "I'll take that as compliment!"
                        $ flena = "happy"
                        l "It was."
                        $ frobert = "smile"
                        r "See? Coming to have drinks with me wasn't that bad, huh?"
                        l "No, it was not. I'm having fun."
                        l "It's been a while since I did this, you know?"
                        r "Did what?"
                        l "This, having drinks at a bar with a guy..."
                        r "We can do it as often as you want."
                        $ flena = "flirtshy"
                        l "Ha ha..."
                        $ flena = "n"
                        l "Oh, I almost forgot."
                        l "What's that important thing you had to tell me?"
                        $ frobert = "n"
                        l "Oh, that..."
                        hide friend_up
                        hide charisma_up
                        jump v2_robertdatescene2
                        
                    "You're OK":
                        $ renpy.block_rollback()
                        l "You're OK, I guess."
                        $ frobert = "sad"
                        r "What's that supposed to mean?"
                        l "It's not bad!"
                        r "I hope so!"
                        if lena_robert > 3:
                            l "If I thought poorly about you I guess I wouldn't be here right now."
                            r "I thought as much, but you never know..."
                            r "So you're having a good time with me?"
                            l "Yeah."
                        l "I just don't know you enough yet to really get an idea of who you are exactly."
                        $ frobert = "smile"
                        r "Well, that's why we're here, so we get to know each other better. Right?"
                        l "I guess... But if I recall correctly you had something important to tell me, too."
                        $ frobert = "n"
                        r "Oh, yeah, that..."
                        jump v2_robertdatescene2
                    
                    "{image=icon_mad.png}I barely know you" if lena_robert < 5:
                        $ renpy.block_rollback()
                        $ lena = "sad"
                        l "Honestly, I barely know you Robert... So I can't really say."                    
                        $ lena_robert -= 1
                        play sound "sfx/frienddown.mp3"
                        show friend_down
                        $ frobert = "sad"
                        r "Really? You've known me for quite a while... You don't have any opinion about me?"
                        l "I just don't have enough information to judge yet."
                        r "That sounds cold... I'm sure there's something you can tell me."
                        l "Look, I don't know what to tell you. I just don't know you enough yet, so I don't have an opinion!"
                        $ frobert = "n"
                        r "But that's why we're here, so we get to know each other better."
                        $ flena = "n"
                        l "I thought we were here because you had something important to tell me."
                        r "Oh, right, about that..."
                        l "Can I finally know what it's about?"
                        r "Sure..."
                        hide friend_down
                        jump v2_robertdatescene2
                
            "I want you to tell me right now" if v2_rbt_wait2:
                $ renpy.block_rollback()
                $ flena = "serious"
                l "Look, I've indulged you long enough."
                l "Tell me the damn thing already!"
                if lena_robert > 4:
                    $ lena_robert -= 2
                else:
                    $ lena_robert -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                if lena_robert > 5:
                    $ frobert = "sad"
                    r "And here I thought we were having fun..."
                    l "I'm not having a bad time, but you've been waving that mystery in front of me like some kind of prize or something."
                else:
                    $ frobert = "serious"
                    r "OK, OK, calm down!"
                    l "You've been waving that mystery in front of me like some kind of prize or something, and I don't like that."
                play sound "sfx/xp.mp3"
                show wits_up
                $ lena_wits_xp += 1
                call screen skillsup
                l "I don't know if you're trying to make me work for it or what, but it's about time you tell me."
                r "Sheesh, OK..."
                r "I didn't know you could be so unpleasant, Lena."
                l "Are you gonna tell me or not?"
                r "Alright, alright."
                $ frobert = "n"
                hide friend_down
                jump v2_robertdatescene2
    else:
        if v2_robert_invite and lena_robert > 3:
            $ flena = "happy"
            l "OK, but this round's on me!"
            r "It's not neccessary..."
            l "I insist!"
            r "OK, then."
            if lena_robert > 5:
                "I was having a surprisingly good time that night. I wasn't expecting that..."
            elif lena_robert > 3:
                "I was having a good time with Robert, so I decided to stay a bit longer."
            "I went to the bar and got two more drinks."
            $ flena = "smile"
            l "Here you go."
            r "Thank you, beautiful!"
        else:
            menu:
                "Alright":
                    $ renpy.block_rollback()
                    l "OK, we can have another one."
                    r "Cool!"
                    hide robert
                    with short
                    "Robert got up and ordered another round of drinks."
                    if lena_robert > 4:
                        "I was having a surprisingly good time that night. I wasn't expecting that..."
                    elif lena_robert > 3:
                        "I was having a good time at the bar, so I decided to stay a bit longer."
                    else:
                        $ flena = "n"
                        "I decided to stay a bit longer, even though I was starting to consider calling it a night."  
                    show robert at lef
                    with short
                    r "Here you go."
                    l "Thanks."
                    
                "I should get going":
                    $ renpy.block_rollback()
                    $ flena = "n"
                    l "I should get going. It's getting late and I'm pretty tired..."
                    $ frobert = "sad"
                    r "Oh, come on, just another one! It took us too long to go out together!"
                    l "I'm sorry. Maybe another night."
                    $ lena_robert -= 1
                    play sound "sfx/frienddown.mp3"
                    show friend_down
                    $ frobert = "n"
                    r "Too bad... There was something important I had to tell you..."
                    l "Something important? What is it?"
                    r "Well... I'd like you to stay a bit longer..."
                    l "Now you've spilled the beans, so go ahead and tell me."
                    r "Alright... It has to do with work."
                    l "What's up with that?"
                    r "Well... I didn't want to ruin the mood, but I think you deserve to know..."
                    r "It seems Samantha overheard the chef and the staff chief talking the other day."
                    hide friend_down
                    jump v2_robertdatescene2
        
        r "You know, I might've gotten punched in the face, but working at the restaurant has gotten a lot more interesting since you showed up."
        l "Is that so?"
        r "Yeah, I've been working there for three years now, being head waiter for one..."
        r "It's not a small achievement, especially in such a prestigious restaurant as Yunalesca, but it can get kinda dull, to be honest!"
        l "It's not the most exciting job, yeah."
        r "Not as exciting as being a model, that's for sure, ha ha! But not everybody can do that..."
        r "I would've loved to be a football player, or maybe a fireman... I don't know which one is cooler."
        l "I'd say the fireman, ha ha."
        l "So, how come you ended up as a professional waiter?"
        r "Nah, I don't know. I guess school bored me too much to stick with higher education and I went for something practical. Something that could get me some money easily, you know?"
        r "I didn't like depending on my parents for money. I wanted to live my own life, have my own money and be able to do what I wanted."
        l "I'd say we're pretty similar on that regard."
        r "It seems that way!"
        r "Tell me... What do you think about me, Lena?"
        menu:
            "{image=icon_friend.png}I like you" if lena_robert > 4:
                $ renpy.block_rollback()
                l "I like you."
                $ lena_robert += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                r "You do?"
                $ flena = "blush"
                "The drink was making me lose a bit of control on how I expressed things." 
                l "I mean, you seem like a cool guy."
                $ frobert = "flirt"
                r "How am I a cool guy?"
                $ flena = "shy"
                l "I mean, how do you say this?"
                "Was he making me nervous? How?"
                $ flena = "smile"
                l "You're hardworking, you seem to have your priorities straight and you're not ashamed of yourself."
                l "And you're not hard on the eyes either, ha ha!"
                play sound "sfx/xp.mp3"
                show charisma_up
                $ lena_charisma_xp += 1
                call screen skillsup
                r "I'll take that as compliment!"
                $ flena = "happy"
                l "It was."
                $ frobert = "smile"
                if v2_robert_invite:
                    r "I'm surprised you invited me out for drinks."
                    l "Surprised?"
                    r "Pleasantly surprised."
                else:
                    r "See? Coming to have drinks with me wasn't that bad, huh?"
                    l "No, it was not. I'm having fun."
                l "It's been a while since I did this, you know?"
                r "Did what?"
                l "This, having drinks at a bar with a guy..."
                r "We can do it as often as you want."
                $ flena = "flirtshy"
                l "Ha ha..."
                $ flena = "smile"
                hide friend_up
                hide charisma_up
                
            "You're OK":
                $ renpy.block_rollback()
                l "You're OK, I guess."
                $ frobert = "sad"
                r "What's that supposed to mean?"
                l "It's not bad!"
                r "I hope so!"
                if lena_robert > 3:
                    l "If I thought poorly about you I guess I wouldn't be here right now."
                    r "I thought as much, but you never know..."
                    r "So you're having a good time with me?"
                    l "Yeah."
                l "I just don't know you enough yet to really get an idea of who you are exactly."
                $ frobert = "smile"
                r "Well, that's why we're here, so we get to know each other better. Right?"
                l "Sure..."
            
            "{image=icon_mad.png}I barely know you" if lena_robert < 5:
                $ renpy.block_rollback()
                $ lena = "sad"
                l "Honestly, I barely know you Robert... So I can't really say."                    
                $ lena_robert -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                $ frobert = "sad"
                r "Really? You've known me for quite a while... You don't have any opinion about me?"
                l "I just don't have enough information to judge yet."
                r "That sounds cold... I'm sure there's something you can tell me."
                l "Look, I don't know what to tell you. I just don't know you enough yet, so I don't have an opinion!"
                $ frobert = "n"
                r "But that's why we're here, so we get to know each other better."
                $ flena = "n"
                l "I guess..."
                hide friend_down
    "We kept chatting as we finished our second drink."
    r "I'm having a blast tonight, Lena! Thank you for this."
    if lena_robert > 5:
        $ flena = "happy"
        l "I'm having a great time, too."
    elif lena_robert > 4:
        $ flena = "smile"
        l "I'm glad."
    else:
        $ flena = "n"
        l "Yeah, sure."
    $ frobert = "n"
    r "I hate to ruin the mood, but... there's something I really need to tell you."
    $ flena = "worried"
    l "Uh-oh, that sounds like trouble..."
    r "Could be... But you deserve to know."
    r "It seems Samantha overheard the chef and the staff chief talking the other day."

label v2_robertdatescene2:
    if v2_robert_spoiler:
        l "You said it had to do with work..."
        r "Yeah, it seems Samantha overheard the chef and the staff chief talking the other day."
    l "About what?"
    r "About you."
    $ flena = "worried"
    l "About me? Why?"
    r "Well, Friday's incident made quite a ruckus. People are talking about it..."
    l "Oh God..."
    r "And the chief wasn't too thrilled about what happened on Thursday's service, when they had to send you home early."
    l "But that wasn't my fault! None of it was..."
    r "Of course not, but I guess they're not too pleased with your personal life interfering with work..."
    "I felt awful. Like I was one of those crazy people who just can't live a healthy life and end up bringing trouble to everybody around them."
    l "I'm so ashamed... So are they going to kick me out or something?"
    r "That's the thing. You've only been here for a few months, and you know it's normal for people to come and go in this business."
    $ flena = "drama"
    l "So you think they won't renew my contract? It expires very soon!"
    r "I don't know, but I guess that's a possibility... Or maybe they will cut some hours off your schedule."
    l "But I need the money right now...! Not just for me, but my parents expect me to help them financially, too..."
    "I looked at Robert."
    l "You're the head waiter! You have a say in the matter, don't you?"
    if lena_robert > 5:
        $ frobert ="smile"
        r "Yes, I do."
        $ flena = "sad"
        r "I will put in a good word for you. I won't let them get rid of the best waiter in my whole staff!"
        l "You'll do that?"
        r "Yes, don't worry. I just thought I should tell you, since some other staff are talking about it, but it's not something you need to worry about."
        r "I'll make sure they keep you around."
        $ flena = "n"
        l "Thanks, Robert... I would be so grateful."
        r "As I said, it's a done deal. I just thought you deserved to know, since it concerned you."
        r "Now you can just forget about it. Everything will be OK, I promise."
        "I felt a great relief... For a moment I thought I would need to find another job once again."
    else:
        r "I suppose they'll value my opinion on the staff members, yeah."
        l "You know I'm very hardworking. No one has ever complained about me. What happened with Axel was not my fault..."
        r "I know, I know. Relax."
        $ flena = "sad"
        r "I guess they'll hear me out. I will put in a good word for you."
        r "If that guy doesn't come around again, I'm sure they won't have any reason to cut you."
        l "Let's hope so..."
        r "Try not to worry about it too much. I just told you because it concerns you, and I thought you deserved to know."
        $ frobert = "smile"
        r "But as I said, I got you. I won't let them fire the best member of my staff!"
        $ flena = "n"
        l "Thanks, Robert..."
        "Knowing Robert would speak on my behalf made me feel a bit more at ease, but I was still worried."
        "Just thinking about having to find another job yet again..."
    "And it was so hard finding a job I could combine with my schedule at the café."  
    l "It's getting really late... We should get going."
    $ frobert = "n"
    r "OK..."
    "We got up and went to pay at the counter." 
    r "It's my treat."
    if v2_robert_invite:
        l "I said I was inviting you..."
    else:
        l "It's not necessary..."
    r "I insist."
    if lena_robert > 5:
        $ v2_robert_kiss = True
        r "It just doesn't feel right ending the night on such a sour note, after the great time we were having..."
        l "It was fun, yeah. But thanks for telling me, I'm glad you did..."
        scene cocktailbar
        show v2_robert2
        with vpunch
        "Suddenly, Robert wrapped his arms around me and kissed me."
        "I found my lips and my chest pressed against his."
        "A shiver ran down my spine when I felt his hands sliding up my nape, caressing my hair."
        menu:
            "Kiss him back":
                $ renpy.block_rollback()
                "This surely was a better way to end the night..."
                "I could say it was also unexpected, but it really wasn't."
                "I he hadn't taken the first step I would've probably done it. I felt like kissing him, too."
                jump v2_roberthouse               
                
            "Stop him":
                $ renpy.block_rollback()
                $ v2_robert_reject = True
                scene cocktailbar
                show v2_robert1
                with short
                "I pushed him away slightly."
                l "Robert, stop..."
                r "Why? What's the problem?"
                l "I'm just... I'm not in the mood for this..."
                r "I thought we were having fun... Come on, Lena..."
                l "Please, I said stop."
                $ flena = "blush"
                $ frobert ="sad"
                scene cocktailbar
                show lena at rig
                show robert at lef
                with long
                $ lena_robert = 4
                play sound "sfx/frienddown.mp3"
                show friend_down
                "He let me go reluctantly."
                r "I thought we..."
                l "Sorry, Robert. But I just don't feel like that about you..."
                r "Not a single bit?"
                l "I mean... You're nice and all that...  But maybe it's too soon, I don't know."
                l "I'm just not feeling it tonight."
                r "..."
                $ frobert = "n"
                r "Alright. Sorry about that."
                l "We should go."
                r "Let me at least walk you home."
                l "Thanks Robert, but no. I'd like to be alone right now."
                r "If that's what you want... At least text me to let me know you made it home safely."
                l "I will. Good night, Robert."
                jump v2_robertnohouse
        
    elif lena_robert > 4:
        r "I'm sorry I had to give you bad news. We were having a good time! Not a good way to end the night..."
        l "Don't worry about it. I'm glad you told me..."
    else:
        r "You look concerned. I told you you shouldn't worry."
        l "Easier said than done..."
        "I was tired and the bad news had me worried. I hoped nothing bad would come out of them, but still..."
        r "That's not how I wanted to end the night."
    scene cocktailbar
    show v2_robert1
    with short
    "Suddenly, Robert wrapped his arms around my hips and pulled me towards him."
    "My chest met his as he held me close to him, his face searching for mine."
    l "Robert..."
    r "What's up? I've been wanting to do this for so long..."   
    menu: 
        "{image=icon_friend.png}Kiss him" if lena_robert > 4:
            $ renpy.block_rollback()
            $ v2_robert_kiss = True
            "Robert had been pretty nice with me tonight. Maybe it was a bit too soon for me but... Why not just give it a try?"
            "I was tired of feeling anxious and restless... I didn't want to keep resisting the situation."
            scene cocktailbar
            show v2_robert2
            with long
            "I gave in. I let his face find mine, and our lips met."
            $ lena_robert += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            jump v2_roberthouse      
            
        "Push him away":
            $ renpy.block_rollback()
            $ v2_robert_reject = True
            "I pushed him away slightly."
            l "Robert, stop..."
            r "Why? What's the problem? Come on, Lena..."
            l "I said stop."
            "I pushed him away harder."
            $ flena = "blush"
            $ frobert ="sad"
            scene cocktailbar
            show lena at rig
            show robert at lef
            with short
            "He let me go reluctantly."
            r "I thought we..."
            if lena_robert > 4:
                $ flena = "worried"
                $ lena_robert = 2
                play sound "sfx/frienddown.mp3"
                show friend_down
                l "No, Robert. I'm sorry if I gave you that impression, but I'm not interested."
                r "That's... There's no way for me to change your mind?"
                l "Sorry, but no."
                $ frobert = "n"
                r "Alright..."
            else:
                $ flena = "serious"
                $ lena_robert = 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                l "What did I do to give you that impression?"
                r "I don't know, but..."
                l "I think I've made it clear I'm not interested..."
                $ frobert = "serious"
                r "Alright."
            r "I guess I'll see you at work. Good night."
            hide robert
            with short
            $ flena = "sad"
            if v2_robert_invite:
                "Going to get some drinks with Robert had seemed like a good idea, but things didn't go as well as I had hoped..."
            else:
                "I should've guessed the night would end like this..."            
            jump v2_robertnohouse

label v2_roberthouse:
    
    "I closed my eyes and accepted his kisses, responding with my own."
    "He didn't wait to sneak his tongue into my mouth, searching for mine, and he found it."
    "The smell of his cologne filled my nostrils. It was nice..."
    "It had been quite some time since I kissed someone... Too long, probably."
    "Maybe that was the reason I wasn't being able to completely let go..."
    "We made out for a couple of minutes before taking a break and acknowledging the situation."
    $ flena = "flirtshy"
    $ frobert = "smile"
    scene cocktailbar
    show lena at rig
    show robert at lef
    with long
    l "Um..."
    r "Finally. It was about time that happened, don't you think?"
    l "Maybe..."
    r "You're too cute, Lena. I like you so much."
    "I wasn't sure how to respond to him. I wasn't sure about anything, to be honest..."
    "I chuckled a bit."
    $ flena = "shy"
    l "Sorry, I'm being really awkward right now."
    $ frobert = "flirt"
    r "It's OK. Your kisses say much more than your words..."
    r "Let me walk you home tonight."
    l "You don't need to..."
    r "It wouldn't be chivalrous of me to let you go back to your place all alone, so late at night. Allow me."
    $ flena = "smile"
    l "Alright. Let's go."
    stop music fadeout 2.0
    $ frobert = "smile"
    scene street2night
    show robert at lef
    show lena at rig
    with long
    "Robert accompanied me home. He had a big and happy grin on his face and he was resting his hand on my waist as we walked."
    "That made me smile, too..."
    "We arrived at my destination after a few minutes."
    l "Here it is."
    r "Cool."
    l "Thanks for walking me home. So..."
    scene street2night
    show v2_robert2
    with long
    "He grabbed me by the hips with both hands and kissed me goodnight."
    "Or so I thought, but he didn't seem to have any intention to let me go, since his kisses didn't stop."
    "We began making out again in front of the building's entrance. Thankfully it was very late we were practically alone in the street."
    "Our kisses began turning more passionate, Robert's hands running down my hips, getting closer to my butt..."
    r "Baby... Aren't you gonna invite me up?"
    menu:
        "{image=icon_will.png}{color=#DAC10D}OK, let's go up{/color}":
            $ renpy.block_rollback()
            $ v2_robert_home = True
            $ lena_will -=1
            show will_down
            play sound "sfx/willdown.mp3"
            "Then again... Why not?"
            "Why should I feel so insecure? What was I afraid of?"
            "As Robert's kisses continued, I thought about Ivy's words."
            "I had been sulking over Axel for half a year. Maybe it was time to try getting someone else into my bed..."
            "Yes, it was time."
            $ flena = "flirtshy"
            $ frobert = "flirt"
            scene street2night
            show robert at lef
            show lena at rig
            with short
            l "Alright. Let's go."
            r "Nice!"           
            jump v2_robertsexscene
            
        "Maybe another night":
            $ renpy.block_rollback()
            $ flena = "blush"
            $ frobert = "sad"
            scene street2night
            show robert at lef
            show lena at rig
            with short
            "I pushed him away gently."
            l "Maybe another night..."
            r "Why not today?"
            l "This is going a bit too fast... Tonight was nice, Robert, I had fun with you..."
            l "But I like to take things a bit slower. I'm not ready yet, you understand, right?"
            r "Sure... OK, if that's what you want."
            $ frobert = "smile"
            r "Well, then, I'll see you at the restaurant..."
            r "Good night, Lena."
            $ flena = "smile"
            l "Thanks, Robert. Good night."  
            scene fade
            with long
            jump v2_predate
            
        "No way":
            $ renpy.block_rollback()
            $ flena = "worried"
            $ frobert = "sad"
            scene street2night
            show robert at lef
            show lena at rig
            with short
            "I pushed him away gently."
            l "No way, Robert..."
            r "What? Why not? It's clear you like me..."
            l "I don't want you to get the wrong idea. Tonight was nice, and I had fun, but you're going way too fast."
            l "Let's take things one step at a time, OK? Don't take this for what it's not."
            $ lena_robert -= 2
            play sound "sfx/frienddown.mp3"
            show friend_down
            r "You're making me a bit confused, Lena."
            l "Well, it's simple: we had fun and made out a bit tonight. That's about it."
            l "Let's see where things go from here, calmly."
            r "Alright, if that's what you want..."
            r "Well, then, I'll see you at the restaurant..."
            r "Good night, Lena."
            $ flena = "n"
            l "Good night."    
            scene fade
            with long
            jump v2_predate

label v2_robertnohouse:
    
    stop music fadeout 2.0
    scene lenaroomnight
    with long
    $ flena = "n"
    play sound "sfx/door.mp3"
    show lena at rig
    with short
    "I finally got home. It was very late and I was tired..."
    play sound "sfx/meow.mp3"
    show lola at lef
    with short
    "Lola climbed on the bed to welcome me. I petted her."
    l "Hey, baby girl... I've had such a crazy night."
    if v2_robert_invite:
        l "I'm not sure what I was expecting when I invited Robert to get some drinks, but..."
        l "I mean, I suspected he was into me..."
    else:
        "It was clear Robert was into me. Of course he was going to try something, I should've seen that coming..."
    if lena_robert > 5:
        "I had more fun with him than I expected, but still..."
        "I felt we just didn't click together that well. He wasn't awful, but..."
        "He just didn't make me feel that spark I had felt in the past."
        if v2_robert_kiss:
            $ flena = "blush"
            "He had kissed me, though. It was brief, but..."
    elif lena_robert > 3:
        $ flena = "worried"
        "It wasn't like I thought badly of him, but I felt we were just not hitting it off."
        "I guess he wasn't my type... I wasn't really sure if I liked him as a person or not." 
        "But I knew I was not interested in him like he was in me."
    else:
        $ flena = "serious"
        "The interest wasn't mutual, of course."
        "Robert had something about him that kinda repelled me."
        "I couldn't put my finger on it exactly, but I just knew he wasn't the kind of guy I could be interested in."
    l "I hope things won't be too uncomfortable at work from now on..."
    "Also, there was that thing Robert had told me about..."
    "Was my position at the restaurant in jeopardy?"
    "I didn't want to think about it. I just wanted to get some sleep."
    if v2_ian_date:
        "I had to meet Ian first thing in the morning..."
    scene fade
    with long
    jump v2_predate


label v2_robertsexscene:
    
    scene lenaroomnight
    with long
    play sound "sfx/door.mp3"
    show lena at rig3
    show robert at lef3
    with short
    r "So this is your room... How nice."
    l "Yeah..."
    l "You know, you're the first guy that steps into it."
    r "You haven't brought anyone else in?"
    l "Nope. Not since I moved..."
    play sound "sfx/meow.mp3"
    show lola 
    with short
    "Lola climbed on the bed to welcome me."
    $ frobert = "smile"
    r "Oh, you have a cat! Here, kitty kitty."
    hide lola
    play sound "sfx/cat_angry.mp3"
    $ frobert = "sad"
    $ flena = "worried"
    show lolamad
    with vpunch
    r "Whoa!"
    "Robert tried to pet Lola, but she hissed at him."
    hide lolamad
    with short
    $ lena_lola -= 1
    play sound "sfx/frienddown.mp3"
    show friend_down
    "She jumped off the bed and ran away. I closed the door behind her."
    l "Sorry about that. She can be a bit special with guys..."
    $ frobert = "n"
    r "Never mind. Come here."
    play music "music/sensual.mp3" loop
    scene lenaroomnight
    show v2_robert2b
    with long
    "Robert kissed me again, and I kissed him back."
    "We embraced, our hands beginning to caress and explore each other's bodies..."
    scene lenaroomnight
    show v2_robert3
    with long
    "It wasn't before long that clothes began coming off."
    "Robert started to unbutton his own shirt, and asked me to help him with a gesture."
    "As his shirt came off, revealing his lean torso, he began pulling my top off."
    "My breathing became heavier as my heart pounded increasingly. Robert removed my bra, baring my breasts..."
    "I felt my heart racing. It was the first time I was with somebody like this since Axel..."
    "Robert kissed me on the neck while his hands caressed them, making me shiver."
    play sound "sfx/mh1.mp3"
    l "Nhh..."
    r "Oh, baby... Mhhh..."
    "I had been wanting someone to touch me and kiss me like that... I couldn't even remember the last time..."
    "Robert's hands slid down my abdomen, reaching down to my jeans."
    "He unbuttoned them, and I heard him unzip his own pants..."
    scene lenaroomnight
    show v2_robert4
    with long
    play sound "sfx/xp.mp3"
    show lust_up
    $ lena_lust_xp += 1
    call screen skillsup
    "I turned slightly to face him and kissed Robert on the lips."
    "We were mostly naked now..."
    r "Mhh, you're so hot, baby..."
    "I felt his bulging dick rubbing against my crotch. He was already completely hard."
    r "Touch it..."
    "I reached down with my hand and wrapped it around the shaft."
    "I was really touching his cock..."
    "I began stroking it slowly as our lips and tongues played together."
    r "Mhh, yes baby..."
    "It was really happening... I was doing it..."
    "I couldn't tell if I felt excited, anxious or nervous. A mix of everything, to be honest."
    "Why was I feeling like an inexperienced girl during her first time?"
    "It was, in a way... My first time since Axel..."
    "I hadn't planned for it, yet it was happening."
    "Robert's saliva was in my mouth, his cock in my hand, his hands massaging my breasts, clenching my butt cheeks..."
    "But I was having trouble going with the flow. I felt I couldn't really get into it, even if I wanted to..."
    "Thoughts couldn't stop spilling in my head. If I could only make my own mind shut up for a few minutes!"
    r "Let's do it... I want to fuck you, Lena."
    $ flena = "blush"
    $ frobert = "flirt"
    scene lenaroomnight
    show lenatopless2 at rig
    show robertnude at lef
    with short
    "There it was. The moment of truth."
    "Why was I overthinking it so much? I had already made my choice when I decided to bring Robert to my room."
    l "Alright... Let's do it."
    l "Do you have a rubber?"
    $ frobert = "sad"
    r "Huh? I..."
    r "I'm not sure... Don't you have one?"
    l "No."
    "Sex had been the last thing on my mind after breaking up with Axel. I hadn't thought about buying some condoms."
    r "Wait..."
    "Robert picked up his pants and searched for his wallet."
    r "Let's see... I should have one here..."
    r "..."
    r "Shit. I thought I had one... Can't one of your flatmates lend us one?"
    l "Maybe Louise... But it's three in the morning, I'm not gonna wake her up!"
    r "Shit... OK... So what do we do?"
    l "I'm not going to do it without a rubber..."
    r "Of course... Well, we can do other things, right?"
    l "Yeah... I guess so."
    $ frobert = "flirt"
    r "Come here."
    scene lenaroomnight
    show v2_robert4
    with long
    "Robert went back to kissing and caressing me."
    "I had some trouble getting into it before, and after this I felt the mood was even weirder..."
    "We were not going to fuck. At least that much was clear."
    "I tried to relax and go with the flow..."
    scene lenaroomnight
    show v2_robert5_animation
    with long
    "We ended up on my bed. Robert lay down and pushed me down gently, showing me what he wanted. Of course."
    "I grabbed his erect manhood as he pulled my panties off, leaving me completely naked."
    "I didn't give it much thought. I was weary of the doubts. I wanted this to happen."
    "I opened my mouth and wrapped my lips around Robert's cock."
    play sound "sfx/bj1.mp3"
    r "Mhhh, baby...!"
    "As I began sucking him off, I felt Robert's hand slide between my thighs."
    "He gently rubbed his thumb across my slit while I pleasured him."
    "I really had his cock in my mouth... The shape, the taste, the texture... I was experiencing them sharply."
    "It felt new and familiar at the same time. It felt exciting..."
    "He tried to sneak his finger into my sex, but I could tell he was having trouble..."
    "Despite me beginning to get into it, my pussy was barely moist..."
    "I continued to suck him, sliding my hand up and down the shaft while I used my lips on the tip."
    "He squirmed and moaned a bit. Was I doing it right? Was he enjoying it?"
    play sound "sfx/mh1.mp3"
    l "Ngh..."
    "He made a back-and-forth motion with his thumb, trying to penetrate me deeper."
    "However, I wasn't getting any wetter down there..."
    "Why? Why was I having a hard time getting into it?"
    "Even though I found Robert attractive, even though I was turned on by the situation..."
    "Something in the back of my mind wasn't letting me fully enjoy this."
    stop music fadeout 2.0
    $ flena = "sad"
    $ frobert = "sad"
    scene lenaroomnight
    show lenanude2 at rig
    show robertnude at lef
    with short
    l "Robert... Let's just stop."
    r "What? Why?"
    l "I'm... I'm not really feeling it."
    r "Fuck, am I doing something wrong?"
    l "No, no, it's... It's me. It's been a long time since I last, you know..."
    l "And I guess I need a bit more time to feel comfortable in this situation."
    l "Besides, it's been a long day, I'm very tired..."
    l "And I guess the situation at the restaurant has me worried or something."
    "How many excuses was I gonna give him?"
    r "I shouldn't have told you..."
    l "No, I'm glad you did."
    l "It's just I'm in my head and I can't seem to get out of it."
    r "So... What do we do?"
    l "I think we should leave it like this for tonight..."
    r "Alright, I understand... I'm sorry..."
    l "It's not your fault, really. You can stay the night, if you want..."
    r "Uh, sure... It's pretty late after all..."
    $ frobert = "n"
    l "Cool. Come, lie here with me."
    scene lenaroomnight
    with long
    "We lay close together on my bed, which wasn't very big."
    "We kept quiet, but I couldn't sleep... I felt like an idiot."
    "I had messed it up, hadn't I?"
    scene fade
    with short
    $ gallery_scene6 = True

## LENA WEDNESDAY ##########################################################################################################################################################################################################

label v2_predate:
    $ day = "Wednesday"
    
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    "I opened my eyes with the first lights of day."
    if v2_robert_home:
        $ flena = "worried"
        show lenanude at rig
        with short
        "I had barely gotten any sleep, and my body felt sore. That night I hadn't managed to be comfortable on my own bed..."
        "I would've felt bad sending Robert off after last night, though..."
        "I felt sorry for how awkward things had turned out..."
        show robertnude at lef
        with short
        r "Mhhh... Good morning, babe."
        l "Oh, you're awake?"
        r "Yeah... I didn't get much sleep."
        l "Yeah, me neither..."
        l "I'm gonna get up. You want some breakfast or..."
        "Robert slid his hand down my neck and across my boobs."
        $ frobert = "flirt"
        r "I have what I want right here."
        $ flena = "shy"
        l "Someone got up in a rounchy mood..."
        "He pointed down. The shape of his erect cock stuck out under the sheets."
        r "I think it's been like this since last night!"
        $ flena = "blush"
        l "Oh..."
        r "Do you think we could give it another chance...?"
        if v2_ian_date:
            "I looked at the clock. I still had some time before my date with Ian..."
        else:
            "We still didn't have a condom, but maybe I could do something for Robert..."
        menu:
            "Suck him off":
                $ renpy.block_rollback()
                $ v2_robert_bj = True
                play music "music/sensual.mp3" loop
                "I owed him one after making it so awkward last night. He deserved something..."
                scene lenaroom
                show v2_robert6_animation
                with long
                "I pulled the sheets away and found a comfortable position between his legs."                
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
                "He was hard as a rock already, not much for me to do but get to work..."
                play sound "sfx/bj1.mp3"
                "I began stroking his dick slowly while sliding my tongue around the shaft."
                "Robert arched his back and groaned. I didn't know if he was stretching his limbs or feeling great pleasure."
                r "Mhhh, yeah baby..."
                "It seems he was liking it alright. I continued to use my tongue, caressing his glans with it."
                "I licked and jerked him off at the same time for several minutes. For some reason I felt more at ease than last night..."
                if lena_lust > 1:
                    "In fact, I was getting kinda horny..."
                r "Suck it baby, take it deep..."
                scene v2_robert7_animation1
                with long
                play sound "sfx/bj2.mp3"
                l "Mhh..."
                "I granted his request."
                "I slid his cock into my mouth and began moving my head up and down."
                "My hand followed my head's movement, stroking his cock in sync."
                "The wet caresses of my lips and tongue made Robert's sex throb and his body shake slightly."
                r "Mhhh... Oh... Yes, just like that..."
                "The morning silence was filled by Robert's moans and the slurping sounds of the blowjob I was giving him."
                if lena_lust > 1:
                    scene v2_robert7_animation2
                    with long
                    play sound "sfx/bj3.mp3"
                    "I looked at Robert, watching his ecstasy painted on his face... It was so hot..."
                    "And I was getting really horny... I felt my pussy becoming wet."
                    "Why couldn't I manage to feel like this last night? I knew Robert turned me on..."
                "I clearly saw how much I excited him. And I noticed he wouldn't take much longer..."
                r "Oh baby! I'm gonna cum!"
                r "Take it all!"
                "That was even sooner than I expected! Seems like I hadn't lost my skills after all..."
                menu:
                    "{image=icon_lust.png}Swallow his cum" if lena_lust > 1:
                        $ renpy.block_rollback()
                        $ v2_robert_swallow = True
                        "I had gotten so into it I felt the need to do as he was saying."
                        play sound "sfx/dp1.mp3"
                        "I tightened my lips and my grip, jerking him off to the finish."
                        scene v2_robert7
                        show v2_robert7_cum
                        with flash
                        with vpunch
                        pause (0.7)
                        with vpunch
                        r "Ohhhh!"
                        "After his convulsion I could taste his jizz shooting inside my mouth, collecting around my tongue."
                        "His bitter and strangely sweet taste filled my mouth as I kept stroking and sucking, until his orgasm died down."
                        "Then I held my breath, prepared myself and swallowed."
                        l "*{i}Gulp{/i}*"
                        "It was tougher than I thought, but I felt like doing it..."
                        $ flena = "slutshy"
                    "Let him cum":
                        $ renpy.block_rollback()
                        scene lenaroom
                        show v2_robert6_animation2
                        with short    
                        "I went back to using my tongue while I jerked him off quickly, to the finish."
                        r "Ohhhh!"
                        play sound "sfx/bj4.mp3"
                        with vpunch
                        scene v2_robert6
                        show v2_robert6_cum
                        with flash
                        "He convulsed and a rope of jizz shot from his dick, and then another one."
                        "Some of it splashed my lips, and most of it ended up on my hand."
                        "The bitter and strangely sweet smell of cum filled my room as Robert's orgasm died down."
                        $ flena = "shy"
               
                $ frobert = "smile"
                stop music fadeout 2.0
                scene lenaroom
                show lenanude2 at rig
                show robertnude at lef
                with long
                if v2_robert_swallow:
                    r "Holy shit, you swallowed!"
                    l "You asked me to..."
                    r "I guess I did, huh?"
                    r "That was incredible, baby... Just incredible."
                    l "I'm glad you liked it... Come on, let's get up."                      
                else:
                    r "Mhhh, that was great... Such an incredible blowjob, baby..."
                    l "I'm glad you liked it... Come on, let's get up."   
                    "I cleaned my hand and chin with a tissue and got dressed."
                $ gallery_scene7 = True
                
            "Get up":
                $ renpy.block_rollback()
                $ flena = "n"
                l "I'm sorry, Robert. We should get up. I have things to take care of."
                if v2_ian_date:
                    "I didn't want to be late for my meeting with Ian."
                    "And most importantly... I just didn't feel like it."
                $ frobert = "sad"
                r "Come on, babe..."
                "I ignored his request, got up and put on some clothes."
                hide lenanude
                show lenabra at rig
                with short
                $ lena_robert -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                r "Sheesh..."
                $ frobert = "n"
                hide robertnude
                show robert at lef
                with short
                l "Sorry. Next time, OK?"
                r "Alright... I'll wait."
                "Robert followed suit and got dressed."
        $ louise_look = 1
        play sound "sfx/door.mp3"
        scene lenahome
        show lenabra at rig
        show robert at lef
        with short
        r "Guess I'll get going, then."
        l "OK. I'll go take a shower..."
        show robert at truecenter
        show lenabra at rig3
        with move
        $ flena = "surprise"
        $ flouise = "surprise"
        $ frobert = "n"
        show louise at lef3
        with short
        lo "Oh."
        $ flouise = "happy"
        lo "Good morning."
        $ flena = "blush"
        l "Good morning, Louise..."
        r "Hey there."
        lo "Who's this?"
        l "His name's Robert, and he was just leaving..."
        $ frobert = "smile"
        r "Nice to meet you. Maybe next time we can make better introductions, ha ha."
        lo "Sure."
        "Robert gave me a quick kiss on the lips and left."
        hide robert
        with short
        show lenabra at rig
        show louise at lef
        with move
        l "..."
        $ flouise = "flirt"
        lo "Sooo... Are you gonna tell me about this or what?"
        l "You don't need to be so excited about it..."
        lo "I don't? It's the first guy I see you bring home! He stayed the night? And you didn't even tell me!"
        l "This was... kinda unexpected, OK?"
        if v2_ian_date:
            if v2_robert_bj:
                $ flena = "surprise"
                l "Oh no, look at the hour!"
                l "I'm gonna be late...!"                
            else:
                l "Anyways, I'm going to take a shower. I don't wanna be late."
            $ flouise = "sad"
            lo "Oh, that's right, this morning you were meeting that other guy you told me about..."
            lo "And you just slept with that one?"
            $ flouise = "flirt"
            lo "Lena, you're out of control!"
            $ flena = "blush"
            l "It's not like that...!"
            lo "Are you sure? Anyways, I gotta go. But you must tell me everything!"
            l "Sure..."
            lo "Everything, you hear me?"
            hide louise
            with short
            l "Oh boy..."
            "I took a shower and got ready to meet Ian."
            jump v2_firstdate
            
        else:
            lo "I need to go now, but you must tell me everything!"
            l "Sure..."
            lo "Everything, you hear me?"
            hide louise
            with short
            l "Oh boy..."
            l "Well... I have a few hours until I have to be at the café..."
            l "I should do something productive."
            jump v2_lena_alone

    else:
        show lenabra 
        with short
        if v2_robert_date:
            $ flena = "n"
            "I woke up a bit tired..."
            if v2_ian_date:
                "I wished I could get some more hours of sleep, but I had to meet Ian..."
                l "Maybe I shouldn't have gone out for drinks with Robert..."
                "But it was important for me to learn about what he told me... Even if it made me more stressed."
                "I hoped he could really help me."
                l "Oof... Let's go..."
                jump v2_firstdate
            else:
                "I stayed in bed, lazing around for a while."
                l "Ahh... I can't fall back to sleep."
                "I had a few hours to myself that morning, so I decided to get up and do something with them."
                jump v2_lena_alone
        else:
            l "That was a good night's sleep."
            if v2_ian_date:
                "I got up and took a shower, getting ready to meet Ian."
                jump v2_firstdate
            else:
                "I felt rested and motivated to do something with these few hours I got before going to work at the café."
                jump v2_lena_alone
    

## WEDNESDAY LENA AND IAN DATE ####################################################################################################################################################################################################

label v2_firstdate:
    if v1_fight:
        $ ian_hurt = 2
    scene street2
    with long
    $ lena_look = 1
    if v2_robert_bj:
        $ fian = "sad"
        $ flena = "sad"
        show ian at lef
        with long
        i "..."
        show lena at rig
        with short
        l "Hey! Sorry for making you wait..."
        i "Hey. Don't worry, it's OK..."
        l "Have you been waiting for long?"
        i "Hmm... I don't know. Around twenty minutes?"
        if ian_lena > 2:
            $ ian_lena -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
        l "I'm so sorry! I had some... something to take care of this morning."
        $ fian = "smile"
        i "I said it's OK."
        $ flena = "n"
        play music "music/date.mp3" loop
        
    else:
        $ flena = "n"
        $ fian = "smile"
        "I arrived at our meeting point just in time."
        show lena at rig
        with short
        "Ian was already waiting for me."
        show ian at lef
        with short
        play music "music/date.mp3" loop
        i "Hey there."
        l "Good morning, Ian. You're very punctual!"
        i "Only for important occasions, ha ha."
        l "Oh, I should be honored then!"
        $ fian = "blush"
        i "Not at all..."
        
    $ fian = "smile"
    i "So... Have you thought about what you want to do?"
    l "Oh, that's right... We agreed to meet, but we didn't have a plan..."
    menu:
        "I was hoping you had something in mind, Ian":
            $ renpy.block_rollback()
            l "I was hoping you had something in mind, Ian, since you proposed this..."
            i "Of course... I had something in mind, in case you hadn't come up with something yourself."
            l "Let's hear it."
            i "We can go check out this neighborhood's record store. Have you ever been there?"
            $ flena = "smile"
            $ ian_lena += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            l "Not yet, but I wanted to!"
            l "I've heard it's pretty big and they even have a bar."
            i "Yes. We can take a look and get a coffee or something there."
            l "Sounds great. Let's go."  
            hide friend_up
            
        "There's something I want to do":
            $ renpy.block_rollback()
            l "There's something I want to do, in fact."
            l "I've heard the record store in this neighborhood is really big, but I haven't been there yet."
            l "Let's go check it out."
            $ lena_charisma_xp += 1
            show charisma_up
            play sound "sfx/xp.mp3"
            call screen skillsup
            $ fian = "smile"
            i "Sure, I've been there several times and it's pretty cool."
            i "They even have a bar. We can take a look and get a coffee or something there."
            l "Let's go then." 
            hide charisma_up
            
        "I can't think about anything...":
            $ renpy.block_rollback()
            $ flena = "sad"
            l "Um... I can't think about anything right now..."
            i "You don't have any suggestions? Anything you feel like doing?"
            l "It shouldn't be this hard, but nothing comes to mind right now... Sorry."
            i "Oh...In that case..."
            i "Maybe we can go check out this neighborhood's record store. Have you ever been there?"
            $ flena = "n"
            l "Not yet, but I've heard it's pretty big."
            i "Yes, and they even have a bar. We can take a look and get a coffee or something there."
            l "Let's go then." 
            
    if v1_fight:
        l "By the way, I see your eye is much better now!"
        $ fian = "shy"
        i "Yeah, the hematoma is fading away, thankfully..."
        i "You have no idea how bothersome it is having to give explanations to everyone..."
        l "It should be gone in a few more days!"
        i "I hope so."
    $ fian = "smile"
    "We walked to the record store."
    $ flena = "n"
    "When was the last time I met someone like this?"
    if v2_robert_date:
        $ flena = "sad"
        "I guess last night with Robert counted."
        "Although I had known him for several months, that had been the first time we hanged out outside of work."
        if v2_robert_home:
            "The first time, yet he ended up spending the night at my place..."
            "Maybe I was going too fast, rushing things in my confusion..."
        "And now here I was, with Ian. Sometimes I felt I had no clue of what I was doing since I broke up with Axel."
    else:
        $ flena = "sad"
        "Not since Axel... I hadn't met anyone really interesting and I had turned down any invitations."
        "I also avoided dating apps and such things... I still believed in meeting people the old fashioned way."
        "I was about to find out if that method still worked..."
    "I shouldn't be this nervous. This wasn't a date, after all..."
    $ flena = "n"
    "Just two people hanging out and getting to know each other."
    
    scene recordstore
    with long
    "The record store was even better than I had imagined."
    "It was indeed very big, with a ton of albums and memorabilia."
    "The decoration was really cozy too, and they even had a small scenario with some instruments, so it seemed they played some live music from time to time!"
    show lena at rig
    show ian at lef
    with short
    l "Wow, this place is cool!"
    i "I thought you'd like it."
    l "Do you come here often?"
    i "I wouldn't say often... But it's a great place to buy vinyl records."
    l "You have a vinyl player? You must really be into music, then!"
    i "I like it quite a lot, yeah... But just as a hobby."
    "We talked while browsing through some records and checking out the store."
    i "I used to play the bass when I was in high school, but that's about as far as my music career got."
    $ flena = "smile"
    l "That's cool. I know how to play guitar, and also the piano, but I'm not great. And also a bit of violin."
    i "That's impressive. Do you sing, too?"
    $ flena = "shy"
    l "Yeah..."
    $ fian = "happy"
    i "You're the complete package. Have you thought about making a career out of it?"
    l "Sure. One can dream, right?"
    $ fian = "smile"
    i "I dreamed about it too, but it's really hard to get into the industry... I chose writing instead, but I'm afraid it's equally hard, ha ha."
    $ flena = "smile"
    l "You know, I also love writing. What I enjoy most about music is the lyrics. Not only listening to them, but also writing them."
    $ flena = "shy"
    l "Expressing my feelings in them... They are the truest form of poetry, in my opinion."
    $ fian = "happy"
    i "So you're also a writer, in that sense... That's awesome."
    menu:            
        "I guess I am":
            $ renpy.block_rollback()
            $ flena = "smile"
            l "I guess I am, yeah. But I can only write songs and poetry."
            $ fian = "smile"
            l "I could never write a book or something like that."
            i "That's exactly what I'm trying to write. A novel."
            l "Really?"
            
        "I wouldn't consider myself a writer":
            $ renpy.block_rollback()
            $ flena = "n"
            l "Nah, I wouldn't consider myself a writer..."
            $ fian = "sad"
            i "Why not? You write, don't you?"
            l "But just songs or bad poetry... I'm just a newbie."
            $ fian = "n"
            i "Well, every pro starts as a newbie. I'm still unpublished, but I would like to become a professional writer myself."
            l "Really? You write books?"
            i "I try to."            
    
        "It's my passion":
            $ renpy.block_rollback()
            $ flena = "happy"
            l "Yeah. It's my passion, similarly to yours."
            $ fian = "happy"
            $ ian_lena += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            i "No way. That's amazing."
            l "Amazing? Why?"
            i "Uh, I meant that's... really cool. I like creative people!"
            i "And I love music. I think writing a good song, a really good one, is as difficult and as valuable as writing a novel." 
            i "I could never write a song, though. I tried back in high school, when I used to play the bass."
            l "Oh, so you play too!"
            i "Used to."
            hide friend_up
            
    $ fian = "smile"
    $ flena = "n"        
    l "So what kind of things do you write?"
    if book_scifi:
        i "Right now I'm working on a sci fi novel."
        l "Oh, that sounds cool. What's it about?"
    elif book_historical:
        i "Right now I'm working on a historical novel."
        l "That sounds really interesting, and hard! What period is it based on?"
    elif book_fantasy:
        i "Right now I'm working on a fantasy novel."
        l "Really? I love fantasy books! What's it about?"
    $ fian = "insecure"
    i "Uh, well... It's still in the early stages..."
    i "I have a lot of work to do and stuff to figure out."
    l "Does it have a title?"
    i "Not yet... Coming up with a title is one of the hardest things, often times the last one to be done."
    l "I could help you come up with one when you're done with it!"
    $ fian = "smile"
    "As we were talking, I saw something that grabbed my attention."
    $ flena = "surprise"
    l "Oh, look at that!"
    "A beautiful acoustic guitar was on display."
    $ flena = "n"
    l "It's not too expensive..."
    i "Do you wanna buy it?"
    l "I've been thinking about getting a guitar, yeah. The one I used to have... Well, I lost it."
    l "And I've been feeling the urge to write songs again recently."
    i "Then go ahead!"
    "Should I? Money was tight, but... I really wanted to."
    "And I had some extra cash thanks to the photo-shoot Ivy had gotten me."
    $ flena = "happy"
    l "Alright, I'll do it!"
    "I picked it up, excited."
    l "Let me buy this and then we can get a coffee."
    show ian at lef3
    show lena at rig3
    with move
    "We went to the counter so I could pay for my new guitar."
    show emma
    with short
    l "Excuse me, I'll take this guitar."
    e "Sure."
    $ fian = "surprise"
    $ femma = "surprise"
    i "Emma?"
    e "Oh! Ian!"
    $ fian = "smile"
    $ femma = "smile"
    $ flena = "worried"
    i "What are you doing here?"
    e "I finally got a job!"
    $ flena = "n"
    l "You know each other?"
    i "Yes, we used to play in the band I told you about earlier, during high school."
    l "Oh, I see."
    e "Name's Emma, nice to meet you!"
    $ lena_emma_agenda = True
    l "I'm Lena."
    "She looked like a girl one could easily get along with, nice and easy-going."
    $ femma = "n"
    e "Let me take care of this guitar for you..."
    "She stored it in a case and charged me."
    play sound "sfx/moneydown.mp3"
    show money_down
    $ lena_money -= 1
    e "I hope you enjoy your purchase!"
    i "We're gonna get a couple of coffees, too."
    e "Right away!"
    $ fian = "worried"
    i "Hey, Emma... I just noticed, but you just got a tattoo, right?"
    e "Oh, yeah! Just the other day... I made a bet with a friend that I would get one if I got a job!"
    e "And they just hired me, so..."
    menu:
        "That's funny":
            $ renpy.block_rollback()
            $ flena = "happy"
            l "That's a really funny reason to get a tattoo done!"
            $ femma = "smile"
            $ lena_emma += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            e "Right?"
            i "I would've picked a more significant reason to get one..."
            e "Why? It's not a big deal. It's just skin."
            e "Besides, I had been thinking if I should get one. This was as good an excuse as any other."
            $ fian = "smile"
            i "As long as you're happy with it."
            $ flena = "n"
            l "It looks good on you."
            e "Thanks!"
            hide friend_up
            
        "That's crazy":
            $ renpy.block_rollback()
            $ flena = "surprise"
            l "That's a crazy reason to get a tattoo!"
            e "You think so?"
            i "I would've also picked a more significant reason to get one..."
            e "Why? It's not a big deal. It's just skin."
            e "Besides, I had been thinking if I should get one. This was as good an excuse as any other."
            $ flena = "n"
            $ fian = "smile"
            i "As long as you're happy with it."
            l "It looks good on you."
            e "Thanks!"
            
        "That's stupid":
            $ renpy.block_rollback()
            $ flena = "worried"
            l "That's a pretty stupid reason to get a tattoo, if you ask me..."
            $ lena_emma -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            e "Why? There are no stupid reasons if it's what you really wanna do."
            i "I would've also picked a more significant reason to get one..."
            e "Nah, it's not a big deal. It's just skin."
            e "Besides, I had been thinking if I should get one. This was as good an excuse as any other."
            $ flena = "n"
            $ fian = "smile"
            i "As long as you're happy with it."
            hide friend_down
    
    hide emma
    with short
    show ian at lef
    show lena at rig
    with move
    "The record store had a couple of small tables and a handful of stools. We took a seat and Emma brought us our coffee."
    i "It's a small world."
    l "It is.... So, what else can you tell me about yourself, Ian?"    
    "We talked about life, learning some basic things about each other."
    "Ian told me he was an only child and he had recently started living with his friend Perry."
    "I also told him a bit about who I was living with, my jobs and why I had to drop my Philology studies due to my family's situation."
    $ ian = "worried"
    i "Damn, that's... tough. I hope your father is doing fine..."
    l "Yes, he's better now."
    $ fian = "n"
    i "So you work two jobs aside from your modeling gigs..."
    i "You're incredibly hardworking. I doubt I could ever do that."
    l "When you have pressing needs you have no choice but to adapt."
    i "I guess..."
    i "Can I ask you a question?"
    l "Sure."
    i "That day at the café... What made you talk to me?"
    menu:
        "I was bored":
            $ renpy.block_rollback()
            l "I don't know, I guess I was bored. Not many people at the café that day..."
            $ fian = "sad"
            i "Oh, I see."  
            if ian_lena > 2:
                $ ian_lena -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
            i "I thought that might be the reason."
            l "Hey, but I was pleasantly surprised."
            $ fian = "n"
            i "Well, that's something I suppose."
            
        "I like chatting people up":
            $ renpy.block_rollback()
            l "I guess I like chatting people up."
            i "It seems you're quite extroverted."
            l "It depends... I don't mind talking to people, getting to know them a bit, engaging in some interesting conversation..."
            l "But there are parts of me I don't usually show to anybody."
            i "Mysterious..."
             
        "I found you interesting":
            $ renpy.block_rollback()
            l "I had seen you a couple times before... Always writing or with a book in hand, focused but also distressed, like you were struggling or something."
            $ fian = "happy"
            i "That sounds pretty much like me, yeah."
            l "I guess I found you interesting, and I wanted to know more about you."
            i "Oh."
            $ flena = "happy"
            l "And teasing you about that teenage vampire book you were reading was way too tempting to pass on!"
            $ fian = "happy"
            i "That's the only good thing that book brought to my life."
            $ fian = "smile"
            $ ian_lena += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            i "But I guess I should be really thankful."
            "The way he said it, it sounded so sincere... Not like he was trying to sweet-talk me or anything."
            if v2_robert_date:
                "Somehow he sounded different from Robert..."       
    l "Can I ask you a question, too?"
    i "Of course."
    l "What did you think when you saw me at the life-drawing session?"
    $ fian = "blush"
    i "Oh, well..."
    i "I must admit I was surprised... But I guess it's just because I never knew anybody who had a job like that."
    i "I didn't think ill of you if that's what you're asking... I mean, not that there's any reason anyone should, but I guess some people have a hard time with that."
    l "They do... But I try surrounding myself with people who are open minded and who don't get their morals from the Middle Ages!"
    $ fian = "n"
    i "You've had trouble because of it?"
    l "Sometimes, but it has been rare, thankfully."
    i "Is your family OK with it?"
    $ flena = "sad"
    l "My dad doesn't know. I don't think he'd understand it. I've told my mom, but she doesn't see any of my work."
    l "Other than that, I'm not ashamed of what I do, even if it can be trouble for some people."
    $ fian = "sad"
    l "Some think I'm a slut or a whore, others are interested in me not because who I am, but because I'm a model and they wanna stroke their ego."
    i "Everything related to sexuality is quite taboo, even if the times are slowly changing..."
    l "It is, but I don't know why we're so ashamed of it. There's art and beauty to be found in sexuality."
    $ flena = "n"
    l "Not even in sexuality, but in sensuality."
    l "In our body, the essential thing we can't exist without. All that we can express and experience through it..."
    l "That's why I'm not ashamed about baring my body in front of the camera."
    l "Because I trust what we're creating is Art. And I truly believe in Art."
    $ fian = "surprise"
    "He looked at me stunned, with an absent-minded expression that lasted a few seconds."
    $ flena = "blush"
    "I felt the urge to talk to snap him out of it."
    l "Did I say something weird?"
    i "Uh?"
    $ fian = "worried"
    i "Oh no, no... I was just, eh..."
    $ flena = "shy"
    "It was kinda cute how awkward he was. He looked so honest."
    $ fian = "smile"
    i "What you just said, it just struck me for some reason. I thought it was..."
    i "Really beautiful."
    $ flena = "happy"
    "I smiled wider than I intended to and I hoped I didn't blush."
    "Honest, and able to be so warm."
    "He deserved me to tease him for it!"
    $ flena = "flirt"
    l "So, you thought it was beautiful but you don't know the reason?"
    i "Well, I do... but I can't pinpoint it exactly..."
    i "I guess it's because I'm very passionate about art myself. It's all I want to do, really."
    i "If I could live off of writing my stories I wouldn't ask anything else from this life."
    $ flena = "smile"
    l "Not even someone to share it with? It would be so lonely otherwise."
    $ fian = "insecure"
    i "Uh, well..."
    $ flena = "sad"
    "His face and tone suddenly changed."
    "I don't know why I chose that question to tease him with, but it seemed to have struck a chord."
    i "I haven't thought about that yet."
    $ flena = "n"
    "Better change the subject... I took a look at the clock and saw our time was almost up."
    l "It's getting late... I should get going to the café."
    $ fian = "n"
    i "Yeah... I'm late for work, too. But I don't really care."
    show lena at rig
    show ian at lef
    with move
    "We got up and paid at the counter."
    "I had one last question I wanted to ask him before parting, though."
    if v1_alisonlunch:
        l "So that girl you came to the cafe with the other day is not your girlfriend?"
        $ fian = "surprise"
        i "Who? Alison?"
        i "No, not at all! She's just a friend...!"
        l "Oh. My mistake!"
        i "If I had a girlfriend I wouldn't have invited you out like this!"
        menu:
            "{image=icon_lust.png}You have bad intentions?" if lena_lust >1:
                $ renpy.block_rollback()
                $ v2_ian_like = True
                "Oh, there was something I could work with."
                $ flena = "flirt"
                l "Oh, so your hypothetical girlfriend would be mad because of this date?"
                l "Is it because you have bad intentions?"
                "He reacted way more scared than I had anticipated."
                i "No, no no!"
                i "I mean, it's not like that. Not that I don't find you a beautiful girl, of course!"
                i "But it's not because I'm just trying to..."
                $ fian = "worried"
                i "I guess the reason would be because I like you."
                $ flena ="surprise"
                "The humble honesty of that answer probably left me as dazed as Ian himself had been a few moments ago."
                $ fian = "surprise"
                "Then he looked like he was about to freak out."
                i "Oh shit, I said something weird."
                $ flena = "blush"
                l "No, no, sorry, that's... That's OK!"
                $ fian = "blush"
                i "I'm sorry, I..."
                l "Who am I kidding, I knew that was the case... That's why I'm here, I guess."
                $ flena ="shy"
                l "Because I like you, too."
                l "And I thought the way you said it was just beautiful."
                "He looked at me with his mouth open for a while, like he was waiting for words to form in his mouth."
                "Finally he shook his head and smiled. Gone was all that clumsy awkwardness."
                $ fian = "smile"
                i "Never mind. I can't find a good answer to that."
                $ ian_lena += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                i "Thanks for the sentiment."
                $ flena = "smile"
                "How could he act so clumsy and so charming at the same time?"
                l "And to you for the honesty."
                jump v2datekiss
                
            "{image=icon_wits.png}/{image=icon_charisma.png}We aren't doing anything wrong" if lena_wits > 1 or lena_charisma > 1:
                $ renpy.block_rollback()
                "Why was it charming how nervous he got?"
                l "Don't worry, we're not doing anything wrong."
                $ fian = "worried"
                i "Of course we're not..."
                i "Why would it be wrong?"
                l "It's not. That's what I just said."
                i "Sure, I was... just wondering about reasons why it might be."
                l "Did you find any?"
                i "Huh..."
                "He shook his head and smiled. Gone was all that clumsy awkwardness."
                $ fian = "smile"
                $ ian_lena += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                i "No. Can't think of a single one..."
                jump v2datekiss
                
            "Good to know":
                $ renpy.block_rollback()
                l "Good to know you're that kind of guy."
                $ fian = "n"
                i "Of course..."
                $ fian = "smile"
                i "So... I guess this was a date, after all."
                $ flena = "shy"
                l "Oh. Uh, I guess..."
                "A slightly awkward silence followed. He could be so blunt and clumsy...!"
                "And yet, so sweet."
                $ flena = "n"
                l "Anyways..."
                jump v2datened
        
    else:
        l "So there's nothing between you and Holly then."
        $ fian = "surprise"
        i "What, with Holly?"
        $ fian = "worried"
        i "No, no, she's just a co-worker... I mean, that was the first time we did anything together outside the office."
        i "And it had to do with work, to be honest..."
        l "Really? She's a very successful writer..."
        l "You wanting to write a book and become a pro, I would think you'd be pretty interested in someone like her."
        $ fian = "n"
        i "Well, she's really interesting, of course, but she's always so quiet..."
        l "She looked really shy, the poor thing. Not fair, considering how amazing her books are!"
        $ fian = "smile"
        i "That's what I told her. She should be so proud of herself."
        l "It seems like you know some interesting people, Ian... I like that. I got to meet a writer I admire thanks to it!"
        i "So that's the only reason you accepted to meet me today? Ha ha."
        menu:
            
            "{image=icon_lust.png}What's your reason?" if lena_lust > 1:
                $ renpy.block_rollback()
                $ v2_ian_like = True
                $ flena = "flirt"
                "I decided to tease him a bit more."
                l "And what's your reason?"
                $ fian = "blush"
                i "Uh... Mine?"
                l "I'm just a random waitress you met. Oh, and you saw me at the life-drawing session..."
                l "Is that the reason you invited me on a date?"
                $ fian = "surprise"
                "He reacted way more scared than I had anticipated."
                i "No, no no!"
                i "I mean, it's not like that. Not that I don't find you a beautiful girl, of course!"
                i "But it's not because I'm just trying to..."
                $ fian = "worried"
                i "I guess the reason would be because I like you."
                $ flena ="surprise"
                "The humble honesty of that answer probably left me as dazed as Ian himself had been a few moments ago."
                $ fian = "surprise"
                "Then he looked like he was about to freak out."
                i "Oh shit, I said something weird."
                $ flena = "blush"
                l "No, no, sorry, that's... That's OK!"
                $ fian = "blush"
                i "I'm sorry, I..."
                l "Who am I kidding, I knew that was the case... That's why I'm here, I guess."
                $ flena ="shy"
                l "Because I like you, too."
                l "And I thought the way you said it was just beautiful."
                "He looked at me with his mouth open for a while, like he was waiting for words to form in his mouth."
                "Finally he shook his head and smiled. Gone was all that clumsy awkwardness."
                $ fian = "smile"
                i "Never mind. I can't find a good answer to that."
                $ ian_lena += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                i "Thanks for the sentiment."
                $ flena = "smile"
                "How could he act so clumsy and so charming at the same time?"
                l "And to you for the honesty."
                jump v2datekiss
            
            "{image=icon_wits.png}/{image=icon_charisma.png}Tease him" if lena_wits > 1 or lena_charisma > 1:
                $ renpy.block_rollback()
                "I decided to play the game and tease him."
                $ flena = "smile"
                l "Of course, that's the only reason... ha ha."
                i "I thought as much..."
                i "What could a boring failure of a writer bring to the table? Ha ha."
                l "You're not boring. Maybe just a bit of a failure... But that can be fixed."
                i "If you know how, please let me know!"
                l "Hey, I'm optimistic, but not a miracle worker!"
                i "You don't have a magic solution for me? I'm afraid I will stay as I am, then..."
                $ ian_lena += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                i "A not so boring failure. Well, I guess I can work with that."
                l "So can I..."
                jump v2datekiss
                
            "It's not like that":
                $ renpy.block_rollback()
                $ flena = "worried"
                l "No, don't be silly!"
                l "I wouldn't accept a date for a reason like that."
                $ fian = "n"
                i "I know, or I hope so... I was just joking."
                $ flena = "n"
                l "Oh. That flew right over my head, sorry."
                $ fian = "smile"
                i "So... I guess this was a date, after all."
                $ flena = "shy"
                l "Oh. Uh, I guess..."
                "A slightly awkward silence followed. He could be so blunt and clumsy...!"
                "And yet, so sweet."
                $ flena = "n"
                l "Anyways..."
                jump v2datened
                           
label v2datekiss:   
    stop music fadeout 2.0
    scene recordstore
    show v2_ian_kiss1
    with long
    "It was then that I noticed something."
    "We were face to face, and somehow we had been getting closer to each other as we spoke..."
    "Was it me who moved, or him? Or maybe both, propelled by a mysterious force?"
    "I looked briefly into his amber eyes and our gazes locked. Was what I felt at that moment... a shiver?"
    menu:
        "{image=icon_friend.png}Kiss him" if v2_robert_bj == False and ian_lena > 3:
            $ renpy.block_rollback()
            $ v2_kiss = True
            $ v2_lena_kiss = True
            play music "music/main_menu.mp3"
            "I don't know what made me do it. Not exactly."
            "But I just felt compelled to."
            scene recordstore
            show v2_ian_kiss3
            with long
            "I leaned forward, closed my eyes and kissed him."
            "He received my kiss gently and kissed me back the same way."
            "It was just one kiss, but a long one."
            "I don't know how long the moment lasted, but for the duration of it I kind of lost sight of everything else in my surroundings."
            "Finally, the brief moment passed and we backed away slowly."
            $ fian = "shy"
            $ flena = "shy"
            scene recordstore
            show ian at lef
            show lena at rig
            with short
            $ ian_lena += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            "We looked at each other and nervous smiles appeared on our faces."
            "Like a couple of awkward idiots who didn't know what to say...!"
            l "Um..."
            i "I guess I'll be seeing you around, then?"
            l "Yes, you will."
            i "Cool."
            l "Well, gotta go. Bye, Ian."
            $ flena = "smile"
            l "And thanks for the date."
            jump v2wedlena
            
        "Stay still":
            $ renpy.block_rollback()
            "I didn't know what to do..."
            "I couldn't move, neither forward nor backwards."
            "Maybe I was waiting for something to happen...?"
            if v2_robert_bj:
                "A part of me felt like I had no right to kiss him. Maybe because of Robert...?"
            "I could see doubt in Ian's eyes..."
            if ian_charisma > 0 and ian_lena > 4:
                $ v2_kiss = True
                $ v2_ian_kiss = True
                play music "music/main_menu.mp3"
                scene recordstore
                show v2_ian_kiss2
                with long
                "But then he closed them and kissed me."
                "It was just one kiss, but a long one. A gentle, heartfelt one."
                "I don't know how long the moment lasted, but for the duration of it I kind of lost sight of everything else in my surroundings."
                "Finally, the brief moment passed and we backed away slowly."
                $ fian = "shy"
                $ flena = "shy"
                scene recordstore
                show ian at lef
                show lena at rig
                with short
                $ ian_lena += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                "We looked at each other and nervous smiles appeared on our faces."
                "Like a couple of awkward idiots who didn't know what to say...!"
                i "Um, that was... I..."
                $ flena = "shy"
                l "That's OK..."
                l "I guess I'll be seeing you around, then?"
                $ fian = "shy"
                i "For sure."
                l "Cool. Well, gotta go... Bye, Ian."
                $ flena = "smile"
                l "And thanks for the date."
                jump v2wedlena
            else:
                $ v2_almost_kiss = True
                $ fian = "blush"
                $ flena = "blush"
                scene recordstore
                show ian at lef
                show lena at rig
                with short
                stop music fadeout 2.0
                "He then backed away."
                i "Um... So I'll be seeing you around?"
                l "Sure... This was fun, we can hang out some other day."
                $ fian = "smile"
                i "That would be cool."
                $ flena = "smile"
                l "Yeah. Well, gotta go. Bye, Ian."
                jump v2wedlena
            
        "Back away":
            $ renpy.block_rollback()
            stop music fadeout 2.0
            $ v2_almost_kiss = True
            $ flena ="blush"
            $ ian = "blush"
            scene recordstore
            show ian at lef
            show lena at rig
            with short
            "I felt the need to back away."
            "The situation, Ian's proximity, made me feel tense... Kind of anxious..."
            l "So, uh..."
            i "I'll be seeing you around?"
            l "Sure... This was fun, we can hang out some other day."
            $ fian = "smile"
            i "That would be cool."
            $ flena = "smile"
            l "Yeah. Well, gotta go. Bye, Ian."
            jump v2wedlena


label v2datened:
    
    l "I gotta go."
    i "Yeah, me, too. This was nice. I hope we can do it again sometime..."
    l "Me, too. See you soon, Ian!"  
    stop music fadeout 2.0
    jump v2wedlena

## WEDNESDAY LENA ALONE ####################################################################################################################################################################################################

label v2_lena_alone:
    
    "I had been staying at home too often lately, and having trouble finding time for myself."
    "There was this record store I had been hearing about and that I wanted to check out..."
    play music "music/normal_day.mp3" loop
    scene street2
    with long
    $ lena_look = 1
    $ flena = "n"
    "I got out and took a walk. The record store was near the downtown area, but a bit hidden."
    scene recordstore
    with long
    "It was even better than I had imagined."
    "It was indeed very big, with a ton of albums and memorabilia."
    "The decoration was really cozy too, and they even had a bar where they served coffee and beer."
    "There also was a small scenario with some instruments, so it seemed they played some live music from time to time!"
    show lena
    with short
    l "Wow, this place is cool!"
    "I spent some time browsing records and other stuff."
    "If I only had a vinyl player in my room... I missed a lot of things."
    "I didn't even have a computer! I could only listen to music on my phone..."
    $ flena = "surprise"
    "And then I saw it."
    "A beautiful acoustic guitar was on display."
    $ flena = "n"
    l "It's not too expensive..."
    "Just the other day I had been thinking about getting a guitar..."
    "And I had been feeling the urge to write songs again recently."
    l "Should I buy it? Money's tight, but... I really want to!"
    "I had some extra cash thanks to the photo-shoot Ivy had gotten me. I could afford to."
    $ flena = "happy"
    l "Alright, I'll do it!"
    "I picked it up, excited, and went to pay at the counter."
    $ flena = "smile"
    $ femma = "n"
    show lena at rig
    with move
    show emma at lef
    with short
    l "Excuse me, I'll take this guitar."
    girl "Sure. Let me take care of this for you..."
    "She stored it in a case and charged me."
    play sound "sfx/moneydown.mp3"
    show money_down
    $ lena_money -= 1
    girl "Here you go. I hope you enjoy your purchase!"
    l "Thanks!"
    "She was really nice. It only made me happier with my purchase."
    "After that, it was time for me to go to work."
    
    scene cafe
    with long
    $ flena = "n"
    $ fian = "smile"
    show lenawork
    with short
    "It was another slow day at the café, without too many customers."
    "I had to wait until the afternoon for it to get a bit more interesting."
    show lenawork at rig
    with move
    show ian at lef
    with short
    i "Hey there."
    l "Hello, Ian. How are you doing?"
    i "Can't complain... Well, I can, to be honest, but I won't."
    i "I have to read through this book and write a review before Monday."
    l "Another lovely vampire romance story?"
    if ian_minerva_review:
        $ fian = "sad"
        i "Yeah... Even worse, this time."
        i "But I have to find a way to write a review that presents this in a good light."
    elif ian_honest_review:
        $ fian = "evil"
        i "Even worse this time. But I've decided to have fun writing the review."
        i "I'm going to write exactly what I think."
    elif ian_switch_review:
        i "Not this time, thankfully. I managed to get my hands on a book I really wanted to read."
        i "It's excellent, so far, but the review will be complex."
    $ fian = "smile"
    i "I'd like a latte to help we with the task."
    l "Right away."
    hide ian
    with short
    show lenawork at truecenter
    with move
    "I served Ian his coffee and let him work."
    "He was as friendly as ever. I wondered why he hadn't texted me yet..."
    "Or even if I wanted him to."
    "I came back to pick up his empty cup after a while."
    $ fian = "n"
    show lenawork at rig
    with move
    show ian at lef
    with short
    l "How's the work coming along? Finished yet?"
    i "It's getting there."
    if ian_switch_review:
        i "I get to read and analyze a good book for a change. This will help me with my own novel."
    else:
        i "I wished I wouldn't have to waste time with this, though. I could be spending this time with writing my own book."
    l "Oh, so you're writing a book?"
    i "Yes... That's my passion. And my dream, so to speak."
    i "To become a professional writer."
    l "That's cool! So what kind of books do you write?"
    if book_scifi:
        i "Right now I'm working on a sci fi novel."
        l "Oh, that sounds cool. What's it about?"
    elif book_historical:
        i "Right now I'm working on a historical novel."
        l "That sounds really interesting, and hard! What period is it based on?"
    elif book_fantasy:
        i "Right now I'm working on a fantasy novel."
        l "Really? I love fantasy books! What's it about?"
    $ fian = "insecure"
    i "Uh, well... It's still in the early stages..."
    i "I have a lot of work to do and stuff to figure out."
    $ fian = "n"
    l "Does it have a title?"
    i "Not yet... That's one of the hardest things, sometimes the last one to be done."
    l "I know. Sometimes I can change the title of a song twenty times and still not be convinced about it."
    $ fian = "smile"
    i "Oh, do you write songs?"
    l "As a hobby, yeah... I also know how to play a little."
    i "That's so cool! So you're a writer, too."
    menu:            
        "I guess I am":
            $ renpy.block_rollback()
            $ flena = "smile"
            l "I guess I am, yeah. But I can only write songs and poetry."
            l "I could never write a book or something like that."
            i "Everyone has their talents. I could never write a song."
            i "I love music, though. I used to play the bass back in high school."
            l "Really? I just bought myself a guitar this morning!"
            
        "I wouldn't consider myself a writer":
            $ renpy.block_rollback()
            $ flena = "n"
            l "Nah, I wouldn't consider myself a writer..."
            $ fian = "sad"
            i "Why not? You write, don't you?"
            l "But just songs or bad poetry... I'm just a newbie."
            $ fian = "n"
            i "Well, every pro starts as a newbie. I'm still unpublished, but I would like to become a professional writer myself."
            i "And writing a good song, a really good one, is as difficult and as valuable as writing a novel."
            i "I love music, but I could never write a song. I tried back in high school, when I used to play the bass."
            l "Really? I just bought myself a guitar this morning!"
    
        "It's my passion":
            $ renpy.block_rollback()
            $ flena = "happy"
            l "Yeah. It's my passion, similarly to yours."
            $ fian = "happy"
            $ ian_lena += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            i "No way. That's amazing."
            l "Amazing? Why?"
            i "Uh, I meant that's... really cool. I like creative people!"
            i "And I love music. I think writing a good song, a really good one, is as difficult and as valuable as writing a novel." 
            i "I could never write a song, though. I tried back in high school, when I used to play the bass."
            l "Really? I just bought myself a guitar this morning!"
            hide friend_up
    
    "I felt strangely comfortable talking with him. And I felt he really liked it, too..."
    "But I couldn't tell if he was into me or if he was just being friendly. What was he about?"
    "I wasn't able to really figure Ian out... And that bothered me."
    "I wanted some answers."
    menu:
        "Be direct":
            $ renpy.block_rollback()
            l "Hey, can I ask you a question?"
            i "Sure."
            l "How come you didn't write to me after we exchanged Peoplegrams?"
            play sound "sfx/xp.mp3"
            show charisma_up
            $ lena_charisma_xp += 1
            call screen skillsup
            $ fian = "surprise"
            i "Oh, that's..."
            $ fian = "worried"
            i "I just didn't want to bother you."
            if v2_addlena:
                l "But you expressly asked for it. You were thinking about contacting me or were you just curious to see what I uploaded to my profile?"
                i "No, no, I didn't ask for it just to stalk you...!"
                i "I was thinking about writing to you. I just didn't know if the timing was right."
                $ fian = "smile"
                i "But in the end I just like talking face to face, like this, rather than through the phone."
                l "That's true. It's the same for me."
            else:
                i "After all, I only got your Peoplegram because Perry asked for it. And he's... not too socially savvy, so to speak."
                i "I thought you might've felt obligated to share that with us, but maybe you didn't really want to."
                l "If I hadn't wanted to I wouldn't have shared it with you. I'm not too meek when it comes to that."
                l "So don't worry, it's no bother."
                $ fian = "smile"
                i "I see... Good to know."
            
        "Inquire indirectly":
            $ renpy.block_rollback()
            l "So, did you find my Peoplegram profile interesting?"
            $ fian = "worried"
            i "Oh, that's... Yeah, very interesting."
            play sound "sfx/xp.mp3"
            show wits_up
            $ lena_wits_xp += 1
            call screen skillsup
            l "So you're one of those who likes to silently stalk people on social media?"
            $ fian = "surprise"
            i "What? No!"
            i "I thought of it as a way to keep in touch, but..."
            if v2_addlena:
                i "I was thinking about writing to you. I just didn't know if the timing was right."
                $ fian = "smile"
                i "But in the end I just like talking face to face, like this, rather than through the phone."
                l "That's true. It's the same for me."
            else:
                i "I only got your Peoplegram because Perry asked for it, after all. And he's... not too socially savvy, so to speak."
                i "I thought you might've felt obligated to share that with us, but maybe you didn't really want to."
                l "If I hadn't wanted to I wouldn't have shared it with you. I'm not too meek when it comes to that."
                l "So don't worry, it's no bother."
                $ fian = "smile"
                i "I see... Good to know."
                
    $ fian = "n"       
    i "I just didn't want to come off as a creep, you know... I can imagine you have to deal with a few, with the nude modeling and all..."
    $ flena = "n"
    l "Sometimes, yeah... But I try surrounding myself with people who are open minded and who don't get their morals from the Middle Ages!"
    l "And I'm not ashamed of what I do, even if it can be trouble for some people."
    $ fian = "sad"
    l "Some think I'm a slut or a whore, others are interested in me not because of who I am, but because I'm a model and they wanna stroke their ego."
    i "Everything related to sexuality is quite taboo, even if the times are slowly changing..."
    l "It is, but I don't know why we're so ashamed of it. There's art and beauty to be found in sexuality."
    $ flena = "n"
    l "Not even in sexuality, but in sensuality."
    l "In our body, the essential thing we can't exist without. All that we can express and experience through it..."
    l "That's why I'm not ashamed about baring my body in front of the camera."
    l "Because I trust what we're creating is Art. And I truly believe in Art."
    $ fian = "surprise"
    "He looked at me stunned, with an absent-minded expression that lasted a few seconds."
    $ flena = "blush"
    "I felt the urge to talk to snap him out of it."
    l "Did I say something weird?"
    i "Uh?"
    $ fian = "worried"
    i "Oh no, no, no. I was just, eh..."
    "Oh God, could he make it more obvious how really absent-minded he was?"
    $ flena = "shy"
    "But at the same time... It was kinda cute how awkward he was. He looked so sincere."
    $ fian = "smile"
    i "What you just said, it just struck me for some reason. I thought it was..."
    i "Really beautiful."
    $ flena = "happy"
    "I smiled wider than I intended to and I hoped I didn't blush."
    "Sincere, and able to be so warm."
    "He deserved me to tease him for it!"
    $ flena = "flirt"
    l "So, you thought it was beautiful but you don't know the reason?"
    i "Well, I do but I can't pinpoint it exactly..."
    i "I guess it's because I'm very passionate about art myself. It's all I want to do, really."
    i "If I could live off of writing my stories I wouldn't ask anything else from this life."
    $ flena = "smile"
    l "Not even someone to share it with? It would be so lonely otherwise."
    $ fian = "insecure"
    i "Uh, well..."
    $ flena = "sad"
    "His face and tone suddenly changed."
    "I don't know why I chose that question to tease him with, but it seemed to have struck a chord."
    i "I haven't thought about that yet."
    $ flena = "n"
    if v1_alisonlunch:
        l "So that girl you came to the cafe with the other day is not your girlfriend?"
        $ fian = "surprise"
        i "Who? Alison?"
        i "No, not at all! She's just a friend...!"
        l "Oh. My mistake!"
        $ fian = "worried"
    else:
        l "So there's nothing between you and Holly then."
        $ fian = "surprise"
        i "What, with Holly?"
        $ fian = "worried"
        i "No, no, she's just a co-worker... I mean, that was the first time we did anything together outside the office."
        i "And it had to do with work, to be honest..."
        l "Really? She's a very successful writer..."
        l "You wanting to write a book and become a pro, I would think you'd be pretty interested in someone like her."
        $ fian = "n"
        i "Well, she's really interesting, of course, but she's always so quiet..."
        l "She looked really shy, the poor thing. Not fair, considering how amazing her books are!"
        $ fian = "smile"
        i "That's what I told her. She should be so proud of herself."
            
    l "It's nice chatting with you, but I should get back to work..."
    i "Sure. I've been keeping you busy for too long!"
    l "Talk to you soon."
    hide ian
    with short
    show lenawork at truecenter
    with move
    "What a curious guy, this Ian..."
    stop music fadeout 2.0
    jump wedlenaend


## WEDNESDAY LENA END ####################################################################################################################################################################################################

label v2wedlena:
    stop music fadeout 2.0
    scene cafe
    with long
    $ flena = "n"
    show lenawork
    with short
    "It had been another slow day at the café, without too many customers."
    if v2_ian_date:
        "Good thing, because I had my head in another place."
        "The date I just had with Ian..."
        if v2_kiss:
            $ flena = "blush"
            if v2_lena_kiss:
                "Had I really kissed him?"
                "What had gotten into me?"
            elif v2_ian_kiss:
                "He had really kissed me..."
                "I hadn't been expecting it, to be honest. But it had happened."
            "Weren't things going a bit too fast?"
            "It was just a kiss, though. And it had happened very... naturally."
        if v2_robert_home:
            "What made it really awkward was that it had happened the morning after I had brought another guy to my place."
            "We didn't end up having sex, but that had been the intention at some point..."
            if v2_robert_bj:
                "And I had given Robert a blowjob just this morning."
                if v2_robert_swallow:
                    "I had swallowed his cum, even!"
            "I had been on a dry spell for months and all of a sudden things piled up..."
            "I had no idea where I was at that moment in life, or even what I was doing for that matter..."    
        elif v2_robert_kiss:
            "It was kinda awkward I had kissed Robert just the night before."
            if v2_robert_reject:
                "Well, that was incorrect. He had kissed me, and I had backed away."
                "I wasn't that I didn't like him, but... I wasn't sure I was comfortable with him."                    
            else:
                "We had just made out for a bit, nothing else..."
                "Even though it was clear he was expecting more of me."
            "I had been on a dry spell for months and all of a sudden things piled up..."
            "I had no idea where I was at that moment in life, or even what I was doing for that matter..."
        elif v2_robert_date:
            "I had been on another date with Robert just the night before."
            "But the way I felt about Ian was quite different, wasn't it?"
            "I had been on a dry spell for months and all of a sudden things piled up..."
            "I had no idea where I was at that moment in life, or even what I was doing for that matter..."  
        if v2_kiss == False:
            "Not that anything had happened with Ian, of course."
            "Not yet, at least..."
        
    elif v2_robert_date:
        "Good thing, because I had my head in another place."
        "What had happened with Robert recently..."
        if v2_robert_home:
            "I had brought another guy to my place for the first time in forever."
            "We didn't end up having sex, but that had been the intention at some point..."
            if v2_robert_bj:
                "And I had given Robert a blowjob just this morning."
                if v2_robert_swallow:
                    "I had swallowed his cum, even!"
            "I had been on a dry spell for months and it was finally breaking."
            "That was supposed to be a good thing..."
        elif v2_robert_kiss:
            "I had kissed Robert just the night before..."
            if v2_robert_reject:
                "Well, that was incorrect. He had kissed me, and I had backed away."
                "It wasn't that I didn't like him, but... I wasn't sure I was comfortable with him."                    
            else:
                "We had just made out for a bit, nothing else..."
                "Even though it was clear he was expecting more of me."
            "I had been on a dry spell for months and it was finally breaking."
            "That was supposed to be a good thing..."
        else:
            "My date with Robert hadn't gone too well, and I was worried about what he told me..."
    scene cafe
    with long
    $ flena = "n"
    "I finished my working hours, picked up my new guitar and left."
    stop music fadeout 2.0

label wedlenaend:
    
    scene streetnight
    show lena
    with long
    "It was Wednesday, so I didn't have to go to the hotel tonight." 
    l "I should go to the gym, but I also wanted to get home and play my new guitar..."
    "What should I do?"
    
    menu:
        "Go to the gym":
            $ renpy.block_rollback()
            $ v2_lena_gogym = True
            "I decided to go to the gym and take Ivy's class."
            jump v2lenagymscene
            
        "Go home":
            $ renpy.block_rollback()
            $ v2_lena_gohome = True
            "I decided to go home and relax."
            jump v2lenahomescene

label v2lenagymscene:
    
    play music "music/jeremys_theme.mp3"
    scene polegym
    with long
    $ flena = "n"
    $ lena_look = 2
    show lena at rig
    show ivy at lef
    with short
    v "Hey, you showed up twice in a week! Impressive."
    l "I told you I would try to come more often."
    v "Good girl! Let's get this started!"
    scene polegym
    show v2_pole1
    with short
    "We picked up where we left last time, practicing the figures of the routine Ivy was teaching us."
    play sound "sfx/xp.mp3"
    $ lena_athletics_xp +=1
    show athletics_up
    call screen skillsup
    "Bit by bit I was getting the hang of it, but I was still miles away from Ivy's level."
    "After thirty minutes or so, Ivy turned off the music and stopped the class."
    scene polegym
    show lena at rig3
    show ivy at lef3
    with short
    v "OK, girls! Enough pole for today."
    v "Let's do some power training now. Grab one of those kettlebells."
    $ flena = "worried"
    l "We're gonna lift weights, now?"
    v "Yeah, it's important to build up some muscle! Otherwise how are you gonna get the strength you need?"
    l "I don't like lifting weights... It's boring and painful."
    v "No pain no gain, darling!"
    menu:
        "Do the exercise":
            $ renpy.block_rollback()
            l "Alright, I'll do it..."
            scene polegym
            show v2_gym
            with long
            "I grabbed a kettlebell and took position next to the other girls."
            "Ivy instructed us which sets we had to do and gave us the rest of the hour to do them."
            "We worked our legs, arms and core..."
            "As I squatted, holding the kettlebell, my legs trembled and ached."
            "Sweat ran down my forehead as pain spread through my thighs, like a thousand needles being buried in them."
            "How I hated this!"
            "But as Ivy had said, no pain no gain..."           
            play sound "sfx/xp.mp3"
            $ lena_athletics_xp +=1
            show athletics_up
            call screen skillsup
            "Finally I finished the workout and the class ended."
            $ flena = "drama"
            $ fivy = "smile"
            scene polegym
            show lena at rig3
            show ivy at lef3
            with short
            l "Oh, God... I'm dying..."
            v "Ha ha, you look quite pitiful right now!"
            v "But you did a good job, Lena."
            l "I'm... just... trying to catch my breath..."
            l "Oof..."
            "It took me a couple of minutes to feel like I could breathe again."
            $ flena = "worried"
            l "Alright..."
            show lena at rig
            show ivy at lef
            with move
            l "That was hellish."
            v "Come on, it was normal."
            
        "Skip it and chat with Ivy":
            $ renpy.block_rollback()
            l "I honestly don't feel like doing it."
            l "Can I stay chatting with you while they do the sets?"
            v "You're so lazy! OK, have it your way."
            $ flena = "n"
            show lena at rig
            show ivy at lef
            with move
            "We stood aside as the other girls began their workout."
    
    $ fivy = "n"
    $ flena = "n"
    v "So, how is it going? Anything new to tell me?"
    if v2_robert_date:
        l "Well, in fact..."
        "I told Ivy about my date with Robert."
        if v2_robert_home:
            $ fivy = "flirt"
            v "And you took him home? That's my girl!"
            l "Yeah, but nothing happened... I mean, it did, but we didn't fuck. We had no condoms."
            v "You're kidding me! Well, next time then."
            v "That's good, you finally followed my advice."
            l "We'll see what happens..."
        elif v2_robert_kiss and v2_robert_reject == False:
            v "So he kissed you and you rejected him? Way to go..."
            l "I just didn't feel comfortable with him."
            v "Well, if that's the case... I think you're being too picky, but there are a ton of guys out there."
            v "At least something's happening in your life, and it was about time!"
        else:
            v "So he tried to kiss you and you rejected him?"
            if v2_robert_kiss:
                l "He did kiss me... But I don't know, I didn't feel really comfortable with the situation."
                v "You're being too neurotic. Just stop fretting and go for it."
                l "I don't know. We'll see what happens..."
            else:
                l "Yeah. I didn't feel all that comfortable with him."
                v "I see... I think you're being too neurotic about it, but oh well, there are a ton of guys out there."
                v "At least something's happening in your life, and it was about time!"
        if v2_ian_date:
            l "That's not all of it though... Remember that other guy I told you about? I met him this morning..."
            "I also told her about my date with Ian."
            $ fivy = "smile"
            if v2_lena_kiss:
                v "So you kissed him? Way to go!"
                v "Two in a row, that's my girl!"
                l "Well, it was just a simple kiss... We'll see how things evolve."
            elif v2_ian_kiss:
                v "So he kissed you? You are driving them crazy, ha ha!"
                v "Two in a row, that's my girl!"
                l "Well, it was just a simple kiss... We'll see how things evolve."
            else:
                v "But nothing happened?"
                if ian_lena > 3:
                    l "Not really... But he's really nice."
                    v "Sounds boring..."
                else:
                    l "Not really..."
                    l "I don't know, on one hand he's really nice, and I ought to like him..."
                    l "But on the other hand we're not really clicking with each other. Not yet at least..."
                    v "He's probably too boring for you."
        v "Well, I'm glad things are starting to get in motion for you."
        v "Now, for the love of God, stop fussing about things and just fuck somebody already. You've been needing it badly!"
        
    elif v2_ian_date:
        l "Well, in fact..."
        l "Remember that other guy I told you about? I met him this morning..."
        "I told her about my date with Ian."
        $ fivy = "smile"
        if v2_lena_kiss:
            v "So you kissed him? Way to go!"
            v "You're being too cute though. We're not kids anymore!"
            l "Maybe, but I felt comfortable with it... It was just a simple kiss, that's true... But we'll see how things evolve."
        elif v2_ian_kiss:
            v "So he kissed you? You are driving him crazy, as I told you!"
            v "You're being too cute though. We're not kids anymore!"
            l "Maybe, but I felt comfortable with it... It was just a simple kiss, that's true... But we'll see how things evolve."
        else:
            v "But nothing happened?"
            if ian_lena > 3:
                l "Not really... But he's really nice."
                v "Sounds boring..."
            else:
                l "Not really..."
                l "I don't know, on one hand he's really nice, and I ought to like him..."
                l "But on the other hand we're not really clicking with each other. Not yet at least..."
                v "He's probably too boring for you."
        v "Well, I'm glad you're starting to see someone, at least. Even if he sounds a bit bland..."
        v "Let's see if you both can stop fussing about things and just fuck already. You've been needing it badly!"
    else:
        "Nothing too interesting going on right now, I guess."
        "We chatted a bit about how the week was going and other trivial things."
    $ flena = "n"
    l "What about you, Ivy? You're still seeing several guys, or have you finally decided to settle for just one?"
    v "I have no intention of settling at all!"
    l "But you said you wouldn't mind if the right guy showed up..."
    v "I doubt he shows up until I'm at least thirty, ha ha! I just love my freedom."
    $ fivy = "flirt"
    v "There's this tall, black guy who works at the club... He's been pushing hard to get my attention, lately."
    v "I have been just teasing him so far, but I guess I'm gonna go for it."
    v "I've never been with a black guy... I'm curious."
    $ lena_ivy += 1
    play sound "sfx/friendup.mp3"
    show friend_up
    $ fivy = "n"
    v "By the way, have you looked into that Stalkfap thing I told you about?"
    l "No, not yet."
    v "I'll grant you free access to mine so you can see how I'm managing it. You have to create an account first, though!"
    l "I'll do it at some point..."
    v "What about your Peoplegram? You should be posting more often!"
    v "That way you won't get new followers..."
    l "I guess I could post another pic from Danny's photo-shoot. Last one did pretty well."
    v "Really? Let me see what people commented!"
    show lena at right
    show ivy at left
    with move
    show v1_peoplegram
    if v1_rss_quote == 1:
        show v1_peoplegram_a
    elif v1_rss_quote == 2:
        show v1_peoplegram_b
    elif v1_rss_quote == 3:
        show v1_peoplegram_c
    with short 
    "I opened Peoplegram and read the comments on my pic."
    "{i}\"You look marvelous.\"{/i}"
    "{i}\"Amazing pic! Simple, yet elegant! Love your curves! Looking forward to what else you can offer {image=emoji_smile.png}\"{/i}"
    "{i}\"I love your expression in this pic and I can't imagine ever being not amazed by your eyes. It simply makes my day whenever you upload something {image=emoji_love.png}\"{/i}"
    l "I love my followers. They are always so nice."
    v "Don't fool yourself. They might be well mannered, but the sentiment behind their words is always the same."
    l "I don't believe so."
    "{i}\"Great pose! Simple, yet powerful. Innocent. You’ve inspired my next piece. Keep it up!\"{/i}"
    l "See? I'm even inspiring artists."
    $ fivy = "flirt"
    $ flena = "shy"
    "Ivy made the gesture of jerking off."
    v "His next piece is probably a completely white and sticky Pollock, ha ha!"
    l "Ivy!"
    "I read a few more."
    $ fivy = "n"
    $ flena = "n"
    "{i}\"Body goals!! {image=emoji_ass.png}\"{/i}"
    l "Oh, this one's from a girl. How encouraging."
    "{i}\"My angel, my muse, my seductress! How you walk the earth among mortal men is a mystery {image=emoji_heart.png}\"{/i}"
    l "How passionate."
    v "How cringy."
    if v1_ed_truth:
        "I kept scrolling down and reached the last comment."
        l "{i}\"I can't believe your beauty, you're such a wonderful young lady, Lena {image=emoji_love.png} {image=emoji_kiss.png} {image=emoji_cum.png}\"{/i}"
        $ flena = "worried"
        l "Wait, he knows my real name? Who's this?"
        "It had to be someone who knew me in real life... And I only had to read his user name to discover who he was."
        $ flena = "surprise"
        l "It's Ed!"
        v "Who?"
        l "One of my bosses at the café!"
        v "That old man? Does he even have a Peoplegram account?"
        $ flena = "blush"
        l "So it seems... I told them I worked as a model sometimes and he must have looked me up..."
        if ed_callout:
            "Even though I told him what he did at the café was inappropriate..."
        l "Oh God, this is so uncomfortable... Look at those emojis."
        l "What's that last one supposed to mean?"
        $ fivy = "flirt"
        v "It means he's a horny old man, ha ha!"
        l "It's not funny, Ivy... I don't like it when this stuff gets mixed with my professional life..."
        v "That's why you should quit those shitty waitressing jobs already! Do yourself a favor and look into that Stalkfap thing already."
    else:
        v "Anyways, keep posting stuff and building some followers."
        v "They're money!"
    scene polegym
    with short
    "After hearing Ivy's advice, we hit the showers and I went back home." 
    stop music fadeout 2.0
    jump v2lenathursday
     
label v2lenahomescene:
    
    $ louise_look = 1
    $ flouise = "smile"
    play music "music/normal_day.mp3" loop
    scene lenahomenight
    with long
    play sound "sfx/door_home.mp3"
    show lena at rig
    with short
    l "Ah, home, sweet home..."
    show louise at lef
    with short
    lo "Hey Lena. What's that? You bought a guitar?"
    l "Yeah, this morning! I'm dying to give it a try."
    lo "Why don't you play something for me?"
    l "It's been a long time... I'll probably mess it up!"
    lo "Oh, come on! I wanna hear you."
    l "Alright..."
    stop music fadeout 2.0
    scene lenahomenight
    show lena_guitar1
    with long
    "I sat down on the couch and took my new guitar out of the bag."
    "The familiar feeling of holding the instrument between my arms came back as if it had never left me."
    play sound "sfx/guitar.mp3"
    "When I strummed the strings and its sound filled the room I couldn't avoid smiling."
    "I tuned the pegs as I played some chords until I was happy with the sound, and began playing some old melodies I had learned long ago."
    play sound "sfx/guitar_long.mp3"
    "Louise listened and suggested some songs I should play. We spent the afternoon together like that until dinner time."
    "I almost forgot how much fun I had with this."
    play sound "sfx/xp.mp3"
    show wits_up
    $ lena_wits_xp += 1
    call screen skillsup
    play music "music/normal_day.mp3" loop
    $ flouise = "happy"
    $ lena = "smile"
    scene lenahomenight
    show lena at rig
    show louise2 at lef
    with short
    lo "See? That was pretty good!"
    l "I'm not as rusty as I thought."
    lo "Thanks for playing for me."
    l "No, thank you for wanting to listen."
    $ lena_louise += 1
    play sound "sfx/friendup.mp3"
    show friend_up
    $ flena = "n"
    $ flouise = "smile"
    l "Anyways, I'll keep practicing some other time."
    l "By the way, you look quite happy, Louise. You smoothed things over with your boyfriend?"
    lo "Yes, we talked and he said he's sorry. He promised to spend time with me tomorrow and during the weekend."
    l "I'm glad things are working out for you."
    if v2_robert_home or v2_robert_kiss and v2_robert_reject == False:
        if v2_robert_home:
            $ flouise = "flirt"
            lo "So... Are you gonna tell me about the guy that was in our flat this morning?"
            $ flena = "blush"
            l "Robert... He's a co-worker..."
            "I told her about last night and how he ended spending the night at our place."
            $ flouise = "smile"
            lo "I see! I'm glad for you! It was about time you found somebody."
            l "It's not like that... We're not dating or anything... It's too soon to put a label on it."
            if v2_ian_date:
                l "Besides..."
        elif v2_robert_kiss and v2_robert_reject == False:
            lo "What about you? How's your love life going? Any news?"
            $ flena = "blush"
            l "Well, something happened last night..."
            "I told Louise about my date with Robert."
            $ flouise = "happy"
            lo "So you made out with him? Congratulations! It was about time you found somebody."
            l "It's not like that... We're not dating or anything... We just kissed, that's all."
            lo "Well, it's a start."
            if v2_ian_date:
                l "The thing is..."
        if v2_ian_date:
            "I also told her about my date with Ian this morning."
            if v2_lena_kiss:
                $ flouise = "surprise"
                lo "You kissed him, too?"
                $ flouise = "sad"
                lo "Wow Lena, that's quite a mess... Getting involved with two guys at the same time... One right after the other..."
                $ flena = "worried"
                l "I knew it, I shouldn't have kissed him, right?"
                lo "I don't know... But it just seems you're a bit confused..."
                lo "Maybe you just need to take things a bit slower."
                l "Maybe you're right..."
            elif v2_ian_kiss:
                $ flouise = "surprise"
                lo "You kissed him, too?"
                l "Not me, it was him who kissed me..."
                $ flouise = "sad"
                lo "Still... That's quite a mess... Getting involved with two guys at the same time... One right after the other..."
                $ flena = "worried"
                l "I knew it, I'm doing something wrong, right?"
                lo "I don't know... But it just seems you're a bit confused..."
                lo "Maybe you just need to take things a bit slower."
                l "Maybe you're right..."            
            else:
                $ flouise = "sad"
                lo "I see... Seems like you're a bit undecided... Confused, maybe?"
                l "Am I? I honestly don't know."
                lo "Well, nothing happened with Ian, so... But it shouldn't, if you're with Robert."
                lo "Even though I know you said you two are dating, but..."
                l "I don't know. This all happened too suddenly."   
        lo "Well, I guess it's not surprising these things happen to you..."
        l "What do you mean?"
        lo "I'm sure you're super popular."
    elif v2_ian_date:
        $ flouise = "flirt"
        lo "By the way, aren't you gonna tell me about your date with Ian?"
        lo "You were meeting him today, right?"
        $ flena = "shy"
        l "Oh, yes..."
        "I told Louise about our date at the record store."
        if v2_lena_kiss:
            $ flouise = "happy"
            lo "So you kissed him?"
            l "Yeah..."
            lo "So cute! I'm glad for you! It was about time you found somebody."
            l "It's not like that... We're not dating or anything... We just kissed, that's all."
        elif v2_ian_kiss:
            $ flouise = "happy"
            lo "So he kissed you?"
            l "Yeah..."
            lo "And you liked it?"
            l "It was... nice, yeah."
            lo "So cute! I'm glad for you! It was about time you found somebody."
            l "It's not like that... We're not dating or anything... We just kissed, that's all."
        else:
            $ flouise = "smile"
            $ flena = "smile"
            if ian_lena > 3:
                lo "So it seems it went well!"
                l "Yes, I had fun, and he's very nice..."
                lo "I'm glad! It was about time you found somebody."
                l "Hold your horses! It's nothing like that. We're just getting to know each other."
            else:
                lo "So you're not really hitting it off?"
                l "I don't know, on one hand he's really nice, and I ought to like him..."
                l "But on the other hand we're not really clicking with each other. Not yet at least..."
        $ flouise = "n"
        lo "Well, it's a start. I guess you can't rush thing, being in your situation."
        $ flena = "worried"
        l "My situation?"
        lo "You being a model and all that... I guess you can never be sure about the real reason why guys are into you."
    else:
        lo "What about you? Nothing new yet?"
    lo "You must get a lot of DMs on Peoplegram from guys who want to date you, considering the photos you upload."
    $ flouise = "sad"
    lo "Well, who want to date you or... sleep with you."
    $ flena = "n"
    l "Not at all. People are quite polite."
    $ flouise = "n"
    lo "Really? What kind of comments do they leave in your pics?"
    l "Let me check the last one I uploaded..."
    show louise2 at left
    show lena at right
    with move
    show v1_peoplegram
    if v1_rss_quote == 1:
        show v1_peoplegram_a
    elif v1_rss_quote == 2:
        show v1_peoplegram_b
    elif v1_rss_quote == 3:
        show v1_peoplegram_c
    with short 
    "I opened Peoplegram and read the comments on my pic."
    "{i}\"You look marvelous.\"{/i}"
    "{i}\"Amazing pic! Simple, yet elegant! Love your curves! Looking forward to what else you can offer {image=emoji_smile.png}\"{/i}"
    "{i}\"I love your expression in this pic and I can't imagine ever being not amazed by your eyes. It simply makes my day whenever you upload something {image=emoji_love.png}\"{/i}"
    l "I love my followers. They are always so nice."
    lo "They're more polite and insightful than I had hoped, yeah..."
    "{i}\"Great pose! Simple, yet powerful. Innocent. You’ve inspired my next piece. Keep it up!\"{/i}"
    l "See? I'm even inspiring artists."
    lo "That's cool, I guess."
    "I read a few more."
    $ fivy = "n"
    $ flena = "n"
    "{i}\"Body goals!! {image=emoji_ass.png}\"{/i}"
    l "Oh, this one's from a girl. How encouraging."
    "{i}\"My angel, my muse, my seductress! How you walk the earth among mortal men is a mystery {image=emoji_heart.png}\"{/i}"
    l "How passionate."
    lo "That sounds really cringy, actually..."
    lo "I don't know... I'm not sure if I would feel comfortable with some of those comments if they wrote them in one of my pictures."
    l "Why not? They're not being gross or anything..."
    if v1_ed_truth:
        "I kept scrolling down and reached the last comment."
        l "{i}\"I can't believe your beauty, you're such a wonderful young lady, Lena {image=emoji_love.png} {image=emoji_kiss.png} {image=emoji_cum.png}\"{/i}"
        $ flena = "worried"
        l "Wait, he knows my real name? Who's this?"
        "It had to be someone who knew me in real life... And I only had to read his user name to discover who he was."
        $ flena = "surprise"
        l "It's Ed!"
        $ flouise = "sad"
        lo "Who?"
        l "One of my bosses at the café!"
        lo "No way! He found you on Peoplegram?"
        $ flena = "blush"
        l "So it seems... I told them I worked as a model sometimes and he must have looked me up..."
        if ed_callout:
            "Even though I told him what he did at the café was inappropriate..."
        l "I didn't even think a man his age would be on Peoplegram..."
       
        l "Oh God, this is so uncomfortable... Look at those emojis."
        l "What's that last one supposed to mean?"
        $ flouise = "mad"
        lo "Ugh, that's gross!"
        lo "You should talk to him about this, Lena."
        if ed_callout:
            l "I will..."
        else:
            l "I don't know... I don't want things to get weird..."
            lo "Weirder than this?"
        "Why did these things happen to me? Why couldn't I just have a calm life?"
        l "*{i}Sigh...{/i}*"
        
    else:
        lo "I guess you're right... Maybe I'm just a bit more shy than you are."
    scene lenahomenight
    with long
    "We had dinner after that and I went to sleep."
    stop music fadeout 2.0


##THURSDAY #######################################################################################################################################################################################################################

label v2lenathursday:
    $ day = "Thursday"
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    $ stan_camera = False
    $ flena = "n"
    if v2_lena_stan_model_shirt:
        $ lena_look = 2 
    else:
        $ lena_look = 1
    show lenabra
    with short
    "I woke up the next morning, ready to get on with my Thursday routine."
    if lena_stan > 3:
        l "First some breakfast..."
        play sound "sfx/door.mp3"
        scene lenahome
        show lenabra2 at rig
        show stan at lef
        with short
        l "Good morning."
        if v2_lena_stan_model_shirt:
            $ fstan = "blush"
        st "Oh, good morning Lena..."
        if v2_lena_stan_model_shirt:
            "I just realized I had forgotten to put on my t-shirt..."
            "Well, never mind. Stan had taken some pictures of me in my underwear the other day, after all."
            "He wasn't seeing anything he hadn't seen before."
        "I began preparing myself some breakfast next to Stan."
        st "..."
        if v2_lena_gohome:
            st "Um... I heard you playing guitar yesterday. You're really good."
            l "Oh, you heard it? I hope I didn't bother you..."
            st "No, not at all...! I liked listening to it."
            l "Really? You could've come join us, then!"
            $ fstan = "sad"
            st "I don't know... I didn't want to be a nuisance."
            l "A nuisance? Why?"
            st "You were with Louise... I felt I would get in the way."
            st "Besides, I don't think she likes me very much..."
        else:        
            l "It's weird, I only see you during breakfast Stan."
            st "Oh... We seem to have... similar morning schedules."
            l "How come you never have dinner with me and Louise? You never join us when we watch a movie or stuff like that."
            st "I just don't want to be a nuisance..."
            l "A nuisance? Why?"
            st "I don't know, I don't want to get in the way when you're talking about your stuff. Besides, I don't think she likes me very much..."
        $ flena = "n"
        "Louise had told me her opinion about Stan, yeah."
        l "She just needs to spend some more time with you. Get to know you better."
        $ flena = "smile"
        l "Next time you should join us. We're living here together, the three of us, after all."
        l "We should do some stuff together, watch a movie or something..."
        st "I guess we could..."
        $ fstan = "smile"
        st "Thanks Lena, you're so... nice to me."
        l "Don't mention it."
        play sound "sfx/ring.mp3"
        "I heard my phone ringing in my room."
        l "Gotta get that. Have a good day, Stan!"
        if v2_lena_stan_model_shirt:
            $ fstan = "perv"
        st "You too, Lena."
        play sound "sfx/door.mp3"
        scene lenaroom
        show lenabra
        with short
        play sound "sfx/ring.mp3"
        $ flena = "n"
        l "I'm coming, I'm coming..."
    else:
        play sound "sfx/ring.mp3"
        "As I got out of bed, my phone rang."
    hide lenabra
    show lenabra_phone
    with short
    l "Yes?"
    show phone_mom_smile at lef3
    with short
    lm "Hello, honey!"
    l "Oh, hi Mom."
    lm "How are you doing? It's been a whole week since we last spoke!"
    hide phone_mom_smile 
    show phone_mom at lef3
    lm "And you haven't called..."
    "There was her little jab."
    l "You know, I've been keeping myself busy... A lot of work and all that stuff."
    l "Not much to tell, to be honest."
    lm "Are you eating well? Is your health OK?"
    l "Yes, everything's fine. Don't worry so much, Mom."
    l "You know what they say, no news is good news."
    lm "Oh, speaking of news!"
    lm "Can you guess who came by yesterday? We hadn't seem him in a long time!"
    l "Um..."
    menu:
        "My brother?":
            $ renpy.block_rollback()
            $ flena = "sad"
            l "Don't tell me Spike showed up again..."
            hide phone_mom
            show phone_mom_sad at lef3
            lm "No... You know we haven't seen him for almost two years now..."
            lm "And last I talked to him over the phone was during Christmas."
            lm "I'm so worried about him..."
            lm "And you won't call us either, I feel abandoned by my own children..."
            $ lena_lenamom -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ flena = "serious"
            l "Alright, Mom, enough."
            "I shouldn't have brought up my brother. She always got like that..."
            l "Just tell me who came by."
            hide phone_mom_sad
            show phone_mom at lef3
            lm "Oh, yeah."
            
        "My aunt?":
            $ renpy.block_rollback()
            l "I don't know... Auntie?"
            lm "No, you know her, she's a busy woman."
            lm "She could show up more often, I always tell her that..."
            l "Just tell me who came by, Mom."
            
        "The Mayor?":
            $ renpy.block_rollback()
            l "I don't know. The Mayor?"
            lm "Don't be silly! Why would he come to our home?"
            lm "We don't even know him personally."
            l "I have no idea who came by, Mom. Just tell me."
            
        "I have no idea":
            $ renpy.block_rollback()
            l "I have no idea. Who?"
    hide phone_mom 
    show phone_mom_smile at lef3        
    lm "Axel! We invited him to have lunch with us."
    $ flena = "surprise"
    "My heart skipped a beat."
    $ flena = "mad"
    l "What did you say?"
    hide phone_mom_smile
    show phone_mom_sad at lef3  
    lm "He came to visit, asking about your dad's health..."
    l "And you invited him to have lunch!?"
    lm "It's the least we could do! He's such a nice lad, even brought us chocolates..."
    lm "What would you expect us to do?"
    l "Kick him out! He's no longer part of my life, and has no business sticking his nose into it!"
    lm "He's very worried about you, you know?"
    lm "He told us you won't even talk to him..."
    l "I can't believe this. Haven't I told you time and time again what he did to me?"
    l "He cheated on me! He lied to my face, not once, but a ton of times!"
    l "He toyed with me, treated me like a fool!"
    lm "People make mistakes. If you could only forgive him... He really cares about you!"
    "My blood was boiling. This again."
    l "Mom, get this into your head: I don't want to get back with Axel, I don't want him in my life, and I don't want you inviting him to lunch!"
    l "I don't want you to tell him anything about me!"
    hide phone_mom_sad
    show phone_mom_serious at lef3  
    lm "What do you want us to tell him? You barely tell us anything!"
    lm "You think it's normal to keep your parents in the dark like this? I just realized we don't even know the address where you're living now!"
    l "Let me guess: you realized that only when Axel asked you, right?"
    hide phone_mom_serious
    show phone_mom_sad at lef3 
    lm "Um, yeah..."
    l "And if you knew, you would've told him, and I'd have him knocking on my door right now!"
    l "I did well not telling you shit!"
    hide phone_mom_sad
    show phone_mom_serious at lef3 
    lm "That's no way to speak to your mother!"
    l "Start acting like one, then! And stop messing up my life!"
    hide phone_mom_serious
    hide lenabra_phone
    show lenabra
    with vpunch
    "I hung up without giving her time to reply."
    "My breathing was shaky and my hands were almost trembling with indignation."
    "How could she do this to me?"
    "Mom had never understood me, but this... Was it so hard, was I asking so much, hoping for her to get in my shoes just for a second?"
    "She did whatever the fuck she pleased. No matter what I said or wanted, only her view on things was right."
    $ flena = "sad"
    "And her specialty was ruining my day just after I got up..."
    
    scene cafe
    with long
    $ lena_look = 1
    "Needless to say, I wasn't too jazzy when I came to work."
    show lena at rig
    with short
    l "Good morning..."
    show ed at lef
    with short
    ed "Good morning Lena."
    l "Where's Molly?"
    ed "She wasn't feeling too well today either, so I told her to stay home."
    ed "She wanted to come, of course... But she needs to take things easy. She's not young anymore!"
    l "I hope she's alright..."
    ed "It's just the ailments of age... Tomorrow's a holiday, so she will have plenty of time to rest."    
    
    if ed_callout:
        if v1_ed_truth:
            "This was as good a time as any to talk to Ed about his comment on my Peoplegram, since his wife was not around."
            $ flena = "serious"
            l "Listen, Ed..."
            l "The other day I told you your behavior had been inappropriate, yet I saw your comment on my Peoplegram..."
            $ fed = "sad"
            ed "Yes... So what?"
            l "It made me feel uncomfortable, especially after the talk we had."
            $ fed = "mad"
            ed "Uncomfortable? How? I was just trying to be nice to smooth things out!"
            l "If that's your idea of smoothing things out I'm afraid to tell you it's quite wrong."
            $ lena_ed -= 2
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ fed = "mad"
            ed "I don't get why you're getting offended about it. Besides, it's you who posted that picture on the internet."
            ed "Everybody can see and comment, I don't see why I specifically shouldn't."
            l "Because you're my boss, and because I'm specifically telling you not to."
            l "Did I make myself clear?"
            ed "Yeah, sure... It won't happen again, don't you worry about it."
            l "Good. Thanks."
            $ fed = "sad"
            ed "Let's just get to work..."
            hide ed
            with short
            $ flena = "sad"
            l "Oh, God..."
            "That had been even worse than the first time. But at least now my message was clear."
            "I just hoped I wasn't messing things up even more..."
            
        else:
            "Ed was acting pretty naturally despite the clash we had the other day. I hoped he kept it that way."
            ed "Sorry to ask you to take care of her work, too. I'll help you best as I can."
            l "Don't worry about it. Let's get to work."
            hide ed
            with short
        
    elif v1_ed_truth:
        "If I wanted to talk to Ed about his comment in my Peoplegram, this was the moment. His wife was not around and I could tell him openly."
        "But I didn't want to make things uncomfortable... He was acting like nothing weird was going on."
        "Should I risk making things awkward at work by calling him out?"
        menu:
            "Call out Ed":
                $ renpy.block_rollback()
                $ ed_callout = True
                $ flena = "sad"
                l "Listen Ed..."
                l "I saw the comment you posted on my Peoplegram. It made me feel uncomfortable."
                $ fed = "sad"
                ed "What? Why?"
                l "I just... don't think it to be appropriate. I don't want to mix my personal life with work."
                ed "I thought you said modeling was just work, too."
                l "Uh, maybe, but I still feel the same..."
                ed "I'm sorry, Lena, that wasn't my intention. I didn't think I was doing anything wrong, I just wanted to comment something positive."
                ed "I don't get why you're getting offended about it. Besides, it's you who posted that picture on the internet."
                ed "Everybody can see and comment, I don't see why I specifically shouldn't."
                $ flena ="serious"
                l "Because you're my boss, and because I'm specifically telling you not to."
                $ lena_ed -= 2
                play sound "sfx/frienddown.mp3"
                show friend_down
                $ fed = "mad"
                ed "Alright, my bad.... Sorry about that."
                $ fed = "sad"
                ed "Let's get to work."
                hide ed
                with short
                $ flena = "sad"
                "That had been uncomfortable... But I think I got my message across."
                "I just hoped I wasn't messing things up even more..."
                
            "Don't mention it":
                $ renpy.block_rollback()
                "I decided it was best not to say anything, much like what had happened in the back room the other day."
                "It was harmless and it didn't seem to be affecting the mood at work."
                "If I called Ed out on it it would probably only serve to make things uncomfortable and create unnecessary conflict."
                "It was not such a big deal after all..."
                ed "Let's get to work, Lena!"
                l "Yes."
                hide ed
                with short
    else:
        ed "Sorry to ask you to take care of her work, too. I'll help you best as I can."
        l "Don't worry about it. Let's get to work."
        hide ed
        with short
    $ flena = "n"
    show lena at truecenter
    with move
    hide lena
    show lenawork
    with short
    "With Molly being absent I had to take care of a lot more things, but it was manageable."
    "Thankfully the number of clients wasn't overwhelming, but today was the day we had the most customers during this week."
    "When my shift ended I was quite tired, but I still had to clock in at the restaurant..."
    stop music fadeout 2.0
    
    $ robert_look = 2
    scene restaurant
    with long
    $ lena_look = 2
    show lenawork at rig
    with short
    play music "music/fancy.mp3" loop
    "Once there, I got ready for a long night."
    if v2_robert_home or v2_robert_kiss:
        $ frobert = "smile"
        "I hadn't talked to Robert since last night..."
        show robert at lef
        with short
        r "Hello, baby!"
        if v2_robert_home:
            $ v3_robert_date = True
            "He kissed me briefly on the lips."
            $ flena = "blush"
            l "Robert...! We're at work..."
            r "Sorry, I couldn't restrain myself. We had so much fun last night, huh?"
            l "Yeah..."
            if v2_robert_bj:
                "He leaned in and talked to my ear."
                $ frobert = "flirt"
                r "Not to speak about the morning after..."
                r "That was the best blowjob I've ever gotten..."
                if v2_robert_swallow:
                    r "And I loved that you swallowed..."
                $ flena = "shy"
                l "Robert!"
                r "Sorry, sorry. I just got so excited, ha ha."
                $ flena = "shy"
                l "I'm glad you liked it..."
            else:
                "He leaned in and talked to my ear."
                $ frobert = "flirt"
            r "I've already bought some condoms so we can finish what we started..."
            $ flena = "shy"
            l "Oh... I see..."
            $ frobert = "n"
            r "I can't tonight, though. I'm going out with the guys. Unless you wanna join..."
            l "No, thanks... I'm pretty tired already, I'll be dead after the shift."
            r "How about tomorrow?"
            $ flena = "n"
            l "I have to attend a photography exhibition. Maybe during the weekend..."
            l "We'll talk about it."
            $ frobert = "smile"
            r "Alright. I can't wait!"
            hide robert
            with short
            
        elif v2_robert_kiss and v2_robert_reject == False:
            $ v3_robert_date = True
            "He kissed me briefly on the lips."
            $ flena = "blush"
            l "Robert...! We're at work..."
            r "Sorry, I couldn't restrain myself."
            r "I thought about what you said, that we should take it a bit slower... And you're right."
            $ flena = "n"
            l "Yeah."
            r "We need to see each other more, taking it step by step."
            r "I can't wait to go on a date with you again. When do you want us to meet?"
            l "Well..."
            $ frobert = "n"
            r "I can't tonight, though. I'm going out with the guys. Unless you wanna join..."
            l "No, thanks... I'm pretty tired already, I'll be dead after the shift."
            $ frobert = "smile"
            r "How about tomorrow?"
            l "I have to attend a photography exhibition. Maybe during the weekend..."
            l "We'll talk about it."
            r "Alright. I can't wait!"
            hide robert
            with short
            
        elif v2_robert_reject:
            $ flena = "sad"
            l "Hey, Robert..."
            $ frobert = "sad"
            r "Look, about the other night..."
            r "I'm sorry I kissed you like that, but we connected so well...!"
            r "I felt it and I know you also did."
            $ flena = "blush"
            l "Do we have to speak about that now? We're at work..."
            r "Just give me another chance. I know you and I have something special."
            menu:
                "Sorry, but no":
                    $ renpy.block_rollback()
                    $ v3_robert_date = False
                    $ flena = "worried"
                    l "Sorry Robert, but I'm just not interested."
                    $ frobert = "serious"
                    if v2_robert_invite:
                        r "I don't know what the problem is. It was even you who invited me out in the first place!"
                    else:
                        r "I don't know what the problem is."
                    $ flena = "serious"
                    l "Look, there's no problem. I'm not feeling it, that's it."
                    l "I have other things in my life to worry about right now, so it's not a good time."
                    l "Are those reasons enough for you?"
                    $ lena_robert = 2
                    play sound "sfx/frienddown.mp3"
                    show friend_down
                    r "I see I'm wasting my time."
                    r "The glasses weren't cleaned properly last night. Please take care of it now."
                    $ flena = "worried"
                    r "After you're done, be quick and set up the tables."
                    hide robert
                    with short
                    l "Sure..."
                    "He was butthurt... But it wasn't my fault."
                    "I hoped he would get over it quickly."
                    
                "OK, we can meet again...":
                    $ renpy.block_rollback()
                    $ v2_robert_chance = True
                    $ v3_robert_date = True
                    "The date hadn't been terrible. Robert could be kind of fun..."
                    $ lena = "n"
                    l "Alright, we can meet again..."
                    $ frobert = "smile"
                    $ lena_robert += 1
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    r "You won't regret it!"
                    r "When, though? I can't tonight. I'm going out with the guys. Unless you wanna join..."
                    l "No, thanks... I'm pretty tired already, I'll be dead after the shift."
                    r "How about tomorrow?"
                    l "I have to attend a photography exhibition. Maybe during the weekend..."
                    l "We'll talk about it."
                    r "Alright. I can't wait!"
                    hide robert
                    with short
                    "No harm in going out with him again, right...?"
            
    elif v2_robert_reject:
        $ frobert = "n"
        "I had to face Robert, too..."
        show robert at lef
        with short
        l "Hey, Robert..."
        r "Hey."
        r "The glasses weren't cleaned properly last night. Please take care of it now."
        $ flena = "worried"
        l "Sure..."
        r "After you're done, be quick and set up the tables."
        hide robert
        with short
        l "That was cold."
        if v2_robert_date:
            l "He didn't even mention anything about last night..."
            "No wonder, since I had rejected him... He was probably feeling ashamed or humiliated."
        else:
            "No wonder, since I had rejected him last night... He was probably feeling ashamed or humiliated."
        "Not my fault, though..."
        l "He'll get over it."
    else:
        $ frobert = "n"
        show robert at lef
        with short
        l "Hey, Robert."
        r "Hey."
        r "The glasses weren't cleaned properly last night. Please take care of it now."
        $ flena = "worried"
        l "Sure..."
        r "After you're done, be quick and set up the tables."
        hide robert
        with short
        "He was acting so cold..."
        "I guess he wasn't too happy about me not wanting to go and have some drinks with him."
        $ flena = "n"
        l "Well, whatever. I'm here to make money, not friends."
        "I applied myself to the task at hand and decided not to worry about him."
    
    show lenawork at truecenter
    with move
    "That night was especially busy. A lot of people were having dinner, since tomorrow was a holiday."
    "At least I'd get to rest a bit myself..."
    $ flena = "worried"
    "After struggling to serve two big noisy groups and cleaning up when the diners were gone, I finally got to leave."
    "I was dead tired..."
    stop music fadeout 2.0
    

##FRIDAY ######################################################################################################################################################################################################################
    $ day = "Friday"
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    $ lena_look = 1
    $ flena = "worried"
    show lenabra
    with short
    "Once again, I had trouble sleeping last night..."
    "Working in such an stressful ambience until so late at night made it really hard for me to fall asleep."
    "Thankfully I could get up late this Friday. I had time for myself until the afternoon."
    l "I need to take a shower to clear my head."
    hide lenabra
    with short
    "After a hot shower and some breakfast I felt lively again."
    $ flena = "n"
    show lena
    with short
    "This week had been a really intense one, too..."
    if v2_robert_date:
        "My date with Robert on Tuesday night, and the concerning news he'd told me..."
    if v2_ian_date:
        "Meeting Ian on Wednesday..."
    if ed_callout:
        "Calling out Ed on his behavior..."
    $ flena = "sad"
    "And to top it all off, yesterday's phone call with Mom... Learning that Axel hadn't given up and was still acting like a maniac..."
    l "Oh God. Is it too much to ask for a little peace?"
    $ flena = "sad"
    "I began reminiscing about my relationship with Axel, all that was great and all that I lost."
    "The pain, the betrayal... The sadness."
    "I had so many feelings bottled up inside, and they needed to come out."
    "That's what I bought my guitar for..."    
    if v2_holly_song:
        "And none other than Holly Watson had told me she wanted to hear one of my songs."
    "It was time to finish one of the songs that had been buzzing in my head."
    scene lenaroom
    show lena_guitar1
    with long
    "I picked up pen and paper and my new guitar, and sat down on the bed."
    play music "music/lenas_theme.mp3"
    "I began playing a sad melody. Music that portrayed all the sorrow I had been carrying with me."
    "All that I had lost, all that I was trying to let go. A dream that vanished..."
    l "That's how I'm gonna call this song: {i}{color=#C12509}\"Broken Dreams\"{/color}{/i}."
    play sound "sfx/drawing.mp3"
    show song_1a
    with long
    "I began writing down the lyrics, letting my words flow with the melody I had just played."
    l "{i}\"So vast and dark, this cosmic field of dreams we live in...\"{/i}"
    l "{i}\"With our child-like hands, reaching out, trying to grasp something...\"{/i}"
    l "Something..."
    l "What is the most appropriate word for this verse?"
    call screen write_song1a
    if song_1a == "real":
        show song_1a_real
        with short
        l "\"Real\". That's definitely the word I was looking for."
    if song_1a == "precise":
        show song_1a_precise
        with short
        l "\"Precise\"... It could work, yeah."
    if song_1a == "cool":
        show song_1a_cool
        with short
        l "\"Cool\". I guess that's OK."
    "I kept playing, and writing."
    "Now I had to take care of the chorus, the most important part of the song."
    "It had to really reflect what the song was about."
    play sound "sfx/drawing.mp3"
    show song_1b
    with long
    l "{i}\"Like two moons on a collision course, this is our gravity...\"{/i}"
    l "{i}\"Like a star that burns out too quick, this is our...\"{/i}"
    call screen write_song1b
    if song_1b == "tragedy":
        show song_1b_tragedy
        with short
        l "\"Tragedy\". Yes, that's it."
    if song_1b == "story":
        show song_1b_story
        with short
        l "\"Story\"... It sounds very fitting."
    if song_1b == "stuff":
        show song_1b_stuff
        with short
        l "\"Stuff\". This will do."
    l "Now to finish the song..."
    play sound "sfx/drawing.mp3"
    show song_1c
    with long
    l "{i}\"So bright and terrifying, this cosmic field of dreams where I exist...\"{/i}"
    l "{i}\"Down the rabbit hole, holding your hand. Spiraling into our...\"{/i}"
    call screen write_song1c
    if song_1c == "abyss":
        show song_1c_abyss
        with short
        l "\"Abyss\". It's dark, and deep... Like this song."
    if song_1c == "kingdom":
        show song_1c_kingdom
        with short
        l "\"Kingdom\"... Our kingdom, yeah."
    if song_1c == "cave":
        show song_1c_cave
        with short
        l "\"Cave\". What else could it be?"
    play sound "sfx/drawing.mp3"
    show song_1d
    with long
    l "Now the chorus again, and to finish it off..."
    l "{i}\"Ours, until we burned out.\"{/i}"
    l "{i}\"Ours, until we ceased to be...\"{/i}"
    stop music fadeout 2.0
    l "..."
    scene lenaroom
    show lena
    with long
    "I put down my guitar and looked at the song scribbled on the paper."
    if song_1a == "real" and song_1b == "tragedy" and song_1c == "abyss":
        $ flena = "cry"
        "I couldn't help but shed some tears. My emotions had overflowed into that song..."
        "I felt sad and cleansed at the same time."
    if song_1a == "cool" and song_1b == "stuff" and song_1c == "cave":
        "I had a weird feeling about it."
        "It made me sad, but I also felt kind of rusty..."        
    else:
        "It was a good song... I had translated my emotions into it."
        "And that meant I had gotten in touch with my sadness. It weighed on me and at the same time I felt lighter..."
    "Such a weird feeling."
    l "That's art, I guess..."
    
    scene lenaroom
    with long
    "I spent the rest of the day touching up the song, writing down chords, rhythms and melodies..."
    "I hadn't been so immersed into something since forever."
    "I almost decided to stay home instead of going to Danny's expo, but I had already made a commitment..."
    
    play music "music/fancy.mp3"
    scene gallery
    with long
    $ flena = "n"
    show lena2 at rig
    with short
    "When I arrived at the art gallery the place was buzzing with people."
    "Danny had told me several people where exhibiting, but I didn't imagine there would be so many guests..."
    "I made my way through them, trying to find a familiar face. I didn't know anybody..."
    $ fdanny = "smile"
    show danny2 at lef
    with short
    dan "Lena! There you are!"
    "Finally."
    l "Hey, Danny. The exhibition is being a great success, I see!"
    dan "Yeah, a lot of people... I'm even nervous! I'm not used to so many people seeing my work..."
    dan "Not in this context, at least!"
    l "Where are your photos?"
    $ fdanny = "n"
    dan "Here, follow me."
    "Danny led me to the area of the exhibition where his work was being displayed."
    "Several pictures of different models hung on the walls, and in the center of those..."
    if v1_choosepic == 1:
        show danny2 at left
        show lena2 at right
        with move
        show v2_frame1
        with short
    if v1_choosepic == 2:
        show danny2 at left
        show lena2 at right
        with move
        show v2_frame2
        with short
    if v1_choosepic == 3:
        show lena2 at right
        show danny2 at left
        with move
        show v2_frame3 behind lena2, danny2
        with short
    if v1_choosepic == 4:
        show lena2 at right
        show danny2 at left
        with move
        show v2_frame4 behind lena2, danny2
        with short
    "My image, the one I helped Danny pic."
    "It had been printed in a huge format and framed. I had never seen my own image like that..."
    dan "Do you like it?"
    l "It's a beautiful photo, Danny. The lighting and framing are really crisp and balanced..."
    if v1_choosepic == 1:
        dan "You think so?"
        dan "The critics I received have been mixed."
        $ flena = "sad"
        l "Mixed? How?"
        dan "They said the technical aspects are OK, but the picture lacks some dynamic..."
        l "Oh... Maybe I should've tried another pose that would have looked more interesting..."
        dan "No, no, it's on me!"
        l "But if I..."
        show seymour
        with short
        man "He's right. An artist should always be responsible for his work, if he truly considers himself its creator."        
    if v1_choosepic == 2:
        $ fdanny = "smile"
        dan "That's what the critics said! Your picture has been highly appreciated!"
        $ flena = "smile"
        l "Really? I'm glad!"
        dan "You're not only wonderful to work with, but you also have trustworthy criteria!"
        play sound "sfx/xp.mp3"
        show wits_up
        $ lena_wits_xp += 1
        call screen skillsup
        l "I really liked this picture, but the merit is yours, Danny."
        show seymour
        with short
        man "The picture is beautiful indeed, and so is the model."
    if v1_choosepic == 3:
        $ fdanny = "smile"
        dan "You know, people loved it! And also the critics..."
        dan "It seems it has great potential to receive the award of best photo of the exhibition!"
        $ flena = "happy"
        l "No way! I'm so glad for you!"
        dan "It's thanks to you, Lena."
        dan "You're not only wonderful to work with, but you also have a very good eye for art!"
        play sound "sfx/xp.mp3"
        show wits_up
        if lena_wits_xp == 2:
            $ lena_wits_xp += 1
            call screen skillsup
            $ lena_wits_xp += 1
        else:
            $ lena_wits_xp += 2
            call screen skillsup
        l "It's you who took this amazing picture."
        show seymour
        with short
        man "It's a very beautiful piece indeed, as outstanding as the model who breathes life into it."
    if v1_choosepic == 4:
        $ fdanny = "sad"
        dan "I don't know, the opinions I received aren't that great..."
        $ flena = "sad"
        l "They're not?"
        dan "They said the piece is technically correct, but the framing of the pose is nothing special."
        dan "I know we took some really great pictures that day. Maybe I should've chosen a different one..."
        show seymour
        with short
        man "Most of the time men fail to capture the true beauty of what they see in front of them. That's the real struggle of an artist." 
    $ flena = "n"
    $ fdanny = "n"
    "A man approached us from the crowd."
    "He was very well dressed and had a distinguished demeanor. The way he carried his head high and the confidence in his eyes made him stand out."
    "And he looked familiar for some reason..."
    hide v2_frame1
    hide v2_frame2
    hide v2_frame3
    hide v2_frame4
    with short
    if v1_choosepic == 1 or v1_choosepic == 4:
        dan "You're absolutely right, Mr. Ward."
    if v1_choosepic == 2 or v1_choosepic == 3:
        dan "Thank you so much, Mr. Ward."
    dan "Please, let me introduce you to the model. "
    dan "Lena, this is Mr. Seymour Ward. He's the owner of Hierofant publishing and a well known philantropist."
    dan "Have you ever heard of him?"
    $ fseymour = "smile"
    hide seymour
    show seymour2
    with short
    mr "Nice to meet you, Lena."
    "He extended his hand and I shook it."
    "His cold blue eyes pierced mine and I felt like he was able to see behind them, to know what kind of person I was just by looking at me..."
    l "Nice to meet you, too. And no, I'm sorry to say I'm not familiar with the name..."
    l "But I know of Hierofant publishing."
    mr "I'm not a particularly public figure. Though I enjoy the lights and warmth of social events of this nature."
    "His voice was deep and his words cultured. It was clear he had something to do with the world of art and culture."
    "And the way he spoke, well, you couldn't avoid feeling he was someone of importance. I felt obliged to make some polite conversation."
    l "So you enjoy the art of photography?"
    mr "I enjoy art in many of its numerous expressions... But I have other reasons to be here today."
    mr "I've been meaning to pick a new hobby, you see. And model photography sounds like something I'd like to try my hand with."
    menu:
        "Art should be more than a hobby":
            $ renpy.block_rollback()
            l "Art should be more than a hobby, don't you think?"
            $ fseymour = "n"
            mr "You think so? I think quite the opposite."
            mr "Art should only be a hobby."
            $ flena = "worried"
            l "I doubt artists would like that point of view, right, Danny?"
            $ fdanny = "surprise"
            dan "Oh, well...! Mr. Ward is an artist himself, even if it's in a different field..."
            l "There are too many people who don't take art seriously. They call themselves photographers but they only undermine the art."
            play sound "sfx/xp.mp3"
            show wits_up
            $ lena_wits_xp += 1
            call screen skillsup
            $ fdanny = "sad"
            $ fseymour = "smile"
            mr "You're not entirely wrong,  and I can see where that noble sentiment of yours comes from, Lena. But it's just clouded by arrogance."
            "Was he calling me arrogant? I'd say that adjective described him far better than it did me..."
            l "How so?"
            mr "What is art, if not passion? What is art, if not beauty? And what are those things for, if not to enjoy them?"
            $ flena = "sad"
            mr "Art's nature is to be enjoyed. And we call what we enjoy a hobby. If not, it becomes a chore, and art can never be a chore."
            mr "There's no soul to be found there."
            "I couldn't argue against that... His logic was sound and his speech vehement."
            
        "What makes you want to try it?":
            $ renpy.block_rollback()
            l "What makes you want to try model photography, specifically? The world of photography is so vast."
            mr "I see you're an inquisitive young lady. You've piqued my curiosity now. "
            mr "Why do you think have I chosen this particular field?"
            l "I don't know, there are a lot of possible reasons..."
            l "But I don't see such a well dressed man as yourself climbing a mountain at five in the morning to take a picture of a sunrise over a lake."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ lena_charisma_xp += 1
            call screen skillsup
            mr "Ha ha, inquisitive indeed. You're right, but that's not the reason behind my choice."
            mr "What would you say is the goal of an artist?"
            $ flena = "sad"
            l "Huh... That's a difficult question. I guess there's as many reasons as there are artists."
            mr "See, there's where you're wrong."
            mr "Every artist is in search of the same thing: beauty, which is just another way to say \"art itself\"."
            mr "Ancient artists were well aware of this passionate desire, and gave it a body: the Muse."
            mr "And well, aren't models like you the worldly incarnation of the Muse itself?"
            "I had no response to that... I felt anything I said would make me sound dull after his eloquent speech."            
         
        "It's because of the naked girls?":
            $ renpy.block_rollback()
            l "A lot of people want to get into this kind of photography... And they all do it because of the naked girls."
            $ fdanny = "surprise"
            dan "Lena...!"
            $ fseymour = "happy"
            mr "That's some refreshing impertinence, ha ha!"
            $ fdanny = "sad"
            $ fseymour = "smile"
            mr "But I understand where it comes from, and it's legitimate."
            l "I'm just saying a lot of men call themselves \"photographers\", but their only intention is getting the chance to take pictures of naked girls."
            play sound "sfx/xp.mp3"
            show lust_up
            $ lena_lust_xp += 1
            call screen skillsup
            mr "And is that so wrong? It's not like they're taking something from the models they themselves are not offering."
            l "There's a difference. We offer our body to be turned into a work of art, not to be drooled over by someone who doesn't even know how to get a shot on focus."
            mr "And as I said, your concern is completely legitimate. There are a lot of those who would use that excuse you just mentioned."
            mr "It's not for me to judge if I'm one of them. But I feel some sympathy for their point of view."
            $ flena = "serious"
            "How unapologetic he was."
            l "How so?"
            mr "You talk about lending your body to be turned into a work of art. But you fail to see the obvious."
            l "Oh, yeah? What is that?"
            mr "The body of a beautiful woman, your body, Lena, is already a work of art. The most beautiful piece Mother Nature has been able to create."
            mr "Can you judge those men for wanting to admire it? To feel close to its sundering allure, even if it's from behind the lens of a camera?"
            $ flena = "sad"
            mr "After all, it's that same desire that attract those with artistic merits and those without to you, modern day muses."
            "I didn't know what to reply to that... He hadn't argued against my point, but somehow had imposed his."
            "And very vehemently at that."
            
    $ fdanny = "n"
    $ flena = "n"
    hide seymour2
    show seymour
    with short
    mr "So, that's the reason I've decided to get into this hobby. Although I must admit I'm also interested in the business aspect of it..."
    mr "But I won't bore you with such talk."
    dan "Mr. Ward, if you're looking for someone to teach you a bit about photography, I'd love to be of service..."
    $ fseymour = "n"
    if v1_choosepic == 3:
        mr "I will seriously consider your offer. Your artistic merit has been made very obvious in this exhibit."
        $ fdanny = "smile"
        play sound "sfx/friendup.mp3"
        show friend_up
        $ lena_danny += 2
        dan "I'd be honored!"
    if v1_choosepic == 2:
        mr "I will consider your offer, since your artistic merit has been clearly displayed in this exhibit."
        $ fdanny = "smile"
        play sound "sfx/friendup.mp3"
        show friend_up
        $ lena_danny += 1
        dan "I'd be honored!"
    if v1_choosepic == 1:
        mr "I have been looking for someone to show me the ropes, so I'll think about it."
        dan "Please, let me know if you decide favorably about it. I'd be honored."
    if v1_choosepic == 4:
        mr "I have already been talking with some other people. They got me covered for now."
        $ fdanny = "sad"
        play sound "sfx/frienddown.mp3"
        show friend_down
        $ lena_danny -= 1
        dan "Oh... OK. Let me know if you change your mind. I'd be honored."
    "He then looked at me."
    mr "I'm also looking for models to work with, Lena."
    mr "I've liked what I've seen of you... And also what I heard."
    mr "Here's my card. Let me know if you're interested in my offer."
    "I took it."
    l "Thanks, I will."
    $ fseymour = "smile"
    mr "Well, I won't bother you anymore. Thanks for your time."
    $ fdanny = "n"
    dan "No, thank you for taking the time to speak to us!"
    mr "It's been a pleasure, Lena."
    $ lena_seymour_agenda = True
    hide seymour
    with short
    "He turned around and went back to socialize with other people in the room."
    show lena2 at rig
    show danny2 at lef
    with move
    dan "Oh boy!"
    l "Is he that important? You were sucking up to him the whole time..."
    dan "He's one of the most important men in this city! He not only has influence in culture, but also in businesses..."
    dan "Getting in his good graces is a golden ticket for anybody."
    dan "And he invited you to work with him directly! He even gave you his card... I'm jealous!"
    $ flena = "worried"
    stop music fadeout 2.0
    l "I see..."
    "So he really was someone important..."
    "He looked the part, that was for sure. Elegant, confident and highly intelligent. That was obvious to see."
    "But there was something else about him... Something that was not so clear to the eye."
    "I didn't know what it was... And I wasn't sure if it intrigued me... or disturbed me."
    jump chapter2_b

## V2 IAN GYM ####################################################################################################################################################################################################################

label chapter2_b:
    
    $ save_name = "Ian: Chapter Two"
    $ lena_active = False
    $ ian_active = True
    $ day = "Thursday"
    scene blackbg
    with long
    show active_ian
    with long
    pause 1.0  
    scene blackbg
    with long
    call screen calendar
    show street
    with long
    $ ian_look = 1
    $ fian = "n"
    show ian
    with short
    
    "My mind was playing back yesterday's events as I made my way to the gym."
    if v2_ian_date:
        if v2_lena_kiss:
            $ fian = "blush"
            i "She kissed me..."
            "I still couldn't believe it..."
            "I wasn't expecting that to happen when I asked Lena out. Of course I was hoping it could happen, but I thought it was probably just wishful thinking..."
            "I wasn't expecting it to happen so soon, that was for sure. Yet it did..."
            $ fian = "shy"
            "I felt so comfortable around Lena and had such a fun date... I really liked her."
            "But I didn't want to get my hopes up too much."
            i "Hold your horses, Ian. It was just a kiss."
            i "Let's see how things play out... And don't mess it up!"            
        elif v2_ian_kiss:
            $ fian = "blush"
            i "I really kissed her..."
            "I wasn't planning on doing that at all, but it happened."
            "I felt so comfortable around Lena and had such a fun date that I couldn't restrain myself."
            "I just felt the need to do it... And she didn't seem to mind."
            $ fian = "shy"
            i "I'd say she even liked it..."
            "I couldn't yet believe my luck. But I didn't want to get my hopes up too much."
            i "Hold your horses, Ian. It was just a kiss."
            i "Let's see how things play out... And don't mess it up!" 
        else:
            "My date with Lena had been very enjoyable."
            "I felt so comfortable around her and had a lot of fun... I felt like she did, too."
            "I liked where this was going, but it was too early to jump to conclusions, though."
            i "Let's see how things play out... I just hope I don't mess it up!" 
        "It was the first time I felt this for a girl since Gillian..."
        "Suddenly life didn't feel as dull."
    else:
        "I had seen Lena at the café again, and this time we had a longer, deeper conversation."
        "She was quite an amazing girl... She had a lot of things to like about her."
        $ fian = "sad"
        i "I should've texted her..."
        "I had decided against it because of my insecurities, but it seemed clear I should have. She even questioned me about it."
        i "I'd say she was expecting me to text her and invite her out or something..."
        "It was too early to jump to conclusions, though. One could never be sure about these things."
        "But I felt we had a genuine connection..."
        i "I should definitely invite her to hang out."
    
    play music "music/jeremys_theme.mp3"
    scene gym
    with long
    $ fian = "n"
    $ fjeremy = "smile"
    $ jeremy_look = 2
    $ ian_look = 7
    "I arrived at the gym and got ready for my training session."
    show ian at lef
    show jeremy at rig
    with short
    "Jeremy was already on the mat, warming up."
    j "Here you are."
    if v1_fight:
        j "That eye is looking much better!"
        i "Yeah, but it's still visible. I was hoping it would've faded away by now..."
        i "I don't want Alison and her friend asking me why I have a black eye."
        j "It's a cool story to tell, bro!"
        j "Get ready and we'll do some sparring! Let's make sure you know how to defend yourself next time!"
    else:
        j "Get ready and we'll do some sparring!"
        i "I want to go easy today. We have to meet Alison and her friend later."
        j "Those are pussy excuses! What if you get into another fight?"
    if ian_wen_agenda:
        show ian at lef3
        show jeremy at rig3
        with move
        show wen
        with short
        wen "So you got into a fight?" 
        if v1_fight or v1_fight_kick:
            if v1_fight:
                wen "I hope you gave the guy something for that black eye!"
                i "A bloody nose."
                wen "It's something!"
                i "Not really... It was pretty pathetic. All technique went out of the window as soon as we began punching each other."
                if v1_fight_grappling:
                    wen "Even though I taught you how to close the distance and avoid punches..."
                elif v1_fight_kick:
                    wen "Even though I taught you how to throw a proper leg kick... That would've helped."
                i "Easier said than done."
                wen "That just means you need more practice. You should learn some Jiu Jitsu."        
            elif v1_fight_kick:
                j "Yeah, he smashed the guy with leg kicks."
                $ fian = "smile"
                i "They proved to be quite useful."
                wen "Good to know that technique worked for you. But if you had used Jiu Jitsu..."
            if ian_grappling == False:
                j "Come on man, we already told you we're not interested in that shit!"
                wen "I'm just saying Ian doesn't have your physical gifts. He'd be a better grappler than striker."
                if v1_fight_kick:
                    i "I'm doing this just as a hobby, and striking is more fun. Besides, those kicks really did the trick."
                    i "I think I can get good at this."
                else:
                    i "I'm doing this just as a hobby, but it's clear I still suck at striking..."
                    j "That's because you need to practice more!"
            else:
                j "Come on man, stop trying to get new clients!"
                hide wen
                show wensmile
                wen "Some extra cash never hurts, ha ha!"
                hide wensmile
                show wen
                wen "I'm just saying Ian doesn't have your physical gifts. He'd be a better grappler than striker."
                i "I don't know about that. Those kicks worked really well. I think I can get good at this."
                j "Tell him like it is, Ian."
                
        elif v1_fight_grappling:
            i "Yeah. I used that technique you taught me in fact..."
            wen "Was it useful?"
            $ fian = "sad"   
            i "Well..."
            j "He got made fun of for hugging the guy like he was his girlfriend, ha ha!"
            i "It worked, but let's just say it was... underwhelming."
            wen "That's because that was an incomplete technique."
            j "You should've taught him the complete technique, ha ha!"
            wen "Jiu Jitsu needs some time to be learned properly. It's not so straightforward as throwing punches."
            j "Simplicity for the win."
            wen "Sometimes that's the case, but everybody can throw a punch. Not everybody knows how to grapple."
            j "You're such a fanboy."
            $ fian = "n"
            i "At least I avoided him punching me in the face. So the defensive aspect of it worked."
            hide wen
            show wensmile
            wen "You should try some Jiu Jitsu. I think it'd be good for you."
            j "Don't listen to him, Ian. We're doing manly stuff here."
            
        else:
            i "No, it didn't come to that..."
            j "Because you lacked the confidence! That's why you need to spar more!"
            wen "I taught you some techniques, but you need to practice them, that's true."
            wen "You should do it in a smarter way, though. Sparring is fun, but you need to get the basics down first, be it in striking or in grappling."
            i "That makes sense."
            j "Yeah, but that's the boring stuff..."
            wen "I think you should give Jiu Jitsu a try. Or you can continue focusing on kick boxing."
            wen "Either way, learn some proper technique!"
            
        j "Well now, if you excuse us... We were gonna do some sparring..."
        wen "Not so fast. Today I'll be in charge of the class."
        $ fjeremy = "n"
        j "How come?"
        wen "Since Yuri is still absent, he asked me to take care of his students."
        i "That's true. I haven't seen the kickboxing coach in a long time."
        j "He's in a training camp in Thailand... He told me I could take care of the class while he was gone, since we're very few people at this hours."
        wen "I know, but I think you need some structure. At least Ian does."
        i "I guess I do."
        hide wen
        show wensmile
        wen "So, today we'll work on conditioning!"
        $ fjeremy = "smile"
        j "Sure, why not? Let's break a sweat."
        scene v4_gym_ian
        with long
        "Wen instructed us on which exercises to do."
        "Sit ups, lunges, crunches, push-ups..."
        "My body ached and I was soon covered in sweat as I forced myself to keep pushing."
        wen "Come on, don't stop now! One more!"
        wen "It's way too early to give up!"
        "Jeremy worked out next to me, and though he was also strained I could see he could keep up the pace much better than me."
        "I still had a lot to improve..."
        play sound "sfx/xp.mp3"
        show athletics_up
        $ ian_athletics_xp += 1
        call screen skillsup
        "After one of the longest hours of my life, the workout finally ended."
        $ fian = "worried"
        $ fjeremy = "smile"
        scene gym
        show ian at lef3
        show wensmile
        show jeremy at rig3
        with long
        "I laid on the floor, panting and dizzy."
        i "I'm about to die..."
        j "It was an intense workout, I'll give you that!"
        wen "You did a good job. Technique is important, but you need to be in shape to be able to execute them properly."
        jump v2endtraining
            
    else:
        show headgear at lef
        with short
        j "Come on, let's go."
        i "Easy, OK?"
        scene gym
        show v1_kickboxing1
        with short
        "After a short warm-up we got into our fighting stance one in front of the other."
        "We began circling each other, feinting, throwing some light techniques..."
        play sound "sfx/punchgym.mp3"
        scene gym
        show v1_kickboxing2
        with vpunch
        i "Oof!"
        "Jeremy nailed me with a good punch right away."
        if v1_fight:
            i "Careful! I don't want to get another black eye!"
        else:
            i "Hey, I don't want to go to the bar with a concussion!"
        j "That's what the headgear is for!"
        "We sparred for a bit, but I felt like Jeremy was using me like a moving punching bag."
        "As always, there was nothing I could do to reach him."
        $ fian = "worried"
        $ fjeremy = "happy"
        scene gym
        show ian at lef
        show headgear at lef
        show jeremy at rig
        with short
        i "OK, that's enough... This is frustrating."
        j "Oh, come on dude! We're having fun!"
        jump wen_training
        
        
label v2endtraining:  
    
    if ian_grappling:
        wen "The kickboxing coach won't be back until next week, so we can do some Jiu Jitsu next time. I think you'll like it."
        j "I'd rather stick to what we're already doing."
        menu:
            "I'll stick to kickboxing, too":
                $ renpy.block_rollback()
                $ fian = "smile"
                i "I'll stick to kickboxing, too. I want to get good at it, and it's more fun."
                wen "Then focus on learning good technique!"
                j "We know, we know! Come on, Ian, let's hit the showers. We have to meet some girls!"
                
            "I'll give it a try":
                $ renpy.block_rollback()
                $ jiujitsu = 1
                $ fian = "smile"
                i "Sounds good. I'll give it a try."
                $ fjeremy = "n"
                j "You will fall behind on the striking department if you start doing that."
                i "I want at least to give it a try. I think it's cool."
                wen "Exactly. You can decide later. Get yourself a {i}gi{/i} and a belt for the next day."
                i "Will do. Thanks for the offer."
                $ fjeremy = "smile"
                j "Come on, Ian, let's hit the showers. We have to meet some girls!"
                
    $ fivy = "flirt"
    $ ivy_look = 1
    stop music fadeout 2.0
    scene streetnight
    with long
    $ fian = "smile"
    $ fjeremy = "smile"
    $ ian_look = 1
    $ jeremy_look = 3
    show ian at lef
    show jeremy at rig
    with short
    "We took a shower and left the gym."
    i "Damn, my legs feel wobbly..."
    j "You'll be sore as hell tomorrow, ha ha."
    j "So where are we meeting Alison tonight?"
    i "She said she wanted to go to a bar downtown, around eleven."
    j "Cool, so we won't be going to that dump you and Perry like so much."
    i "Hey, maybe it's a bit of a dump, but it has its charm. But no, we're checking out a new place tonight."
    show ian at lef3
    show jeremy at rig3
    with move
    show ivy
    with short
    v "Hey, Jeremy."
    $ fjeremy = "surprise"
    $ fian = "surprise"
    j "Ivy! What are you doing here?"
    v "Me? I teach pole dancing in this gym on the third floor."
    $ fjeremy = "happy"
    $ fian = "worried"
    j "No way! I train in this gym, too."
    v "So we work together and we go to the same gym? That's some coincidence..."
    menu:
        
        "{image=icon_charisma.png}Make a joke" if ian_charisma > 1:
            $ renpy.block_rollback()
            $ fian = "happy"
            i "He's not a stalker, I can vouch for him. But I can understand if you have your doubts."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_ivy += 1
            v "Ha ha ha! Yeah, I do."
            $ fjeremy = "smile"
            j "Oh, this is my friend Ian."
            i "Nice to meet you. Ivy, was it?"
            $ fivy = "smile"
            v "Yeah. Nice to meet you, too, Ian."
            
        "Introduce yourself":
            $ renpy.block_rollback()
            $ fian = "n"
            i "Hi... I'm Ian, Jeremy's friend."
            $ fjeremy = "n"
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_jeremy -= 1
            j "Yeah, I was about to introduce you, dude. Chill."
            v "I guess he prefers to introduce himself, right?"
            v "I'm Ivy. Nice to meet you."
            $ fjeremy = "smile"
            
        "Stay quiet":
            $ renpy.block_rollback()
            $ fjeremy = "flirt"
            j "There are no coincidences in this life. Everything happens for a reason..."
            "Ivy let her eyelids droop and smiled."
            v "Oh, yeah? And what reason might that be?"
            j "I guess we'll have to find out together."
            v "I guess."
            v "And who's this guy over there?"
            j "Oh, he. He's Ian, a friend of mine."
            i "Hey."
            
    $ ian_ivy_agenda = True
    v "So you train together?"
    j "Yep. Kickboxing!"
    v "Oh, I see! I know who I will call if I need protection one of these days, ha ha!"
    v "Well, see you tomorrow at the club, Jeremy."
    v "Bye, Ian."
    i "Bye..."
    hide ivy
    with short
    if ian_lust > 0:
        "I looked at her while she walked down the street. Damn, was she hot!"
    i "So she's the girl you told me about..."
    $ fjeremy = "flirt"
    j "Yeah! What do you think, dude? Isn't she the hottest girl you've ever seen?"
    i "She's quite spectacular, yeah... How's it going with her? Have you yet...?"
    j "Not yet, but it's almost a done deal. Did you feel our sexual tension? It's palpable!"
    $ fian = "smile"
    i "If you say so!"
    $ fjeremy = "smile"
    j "So, what were we talking about... Oh, yeah, tonight's plan. You said at eleven?"
    i "Yeah."
    j "Cool. I'll be a bit late, though."
    i "How come?"
    j "I have to meet this girl first..."
    $ fian = "worried"
    i "Dude, seriously? Can't it wait another day?"
    j "Hey, not my fault. She's been giving me shit lately, saying I don't pay enough attention to her..."
    j "So I need to go have dinner with her and smooth things out. And hopefully get a quick fuck!"
    i "Seriously? You're gonna join us right after having sex?"
    $ fjeremy = "happy"
    j "A man's gotta do what a man's gotta do!"
    j "Well, I'll see you guys later. Don't get too drunk before I get there!"
    hide jeremy
    with short
    "He was truly incorrigible..."

## V2 IAN BAR SCENE ####################################################################################################################################################################################################################

    scene streetnight
    with long
    $ jeremy_look = 1
    $ fperry = "meh"
    $ fian = "n"
    "I went back home, had dinner with Perry and left to meet Alison at this bar."
    play music "music/nice_place.mp3" loop
    if v2_robert_date:
        scene cocktailbar
        show ian at lef
        show perry2 at rig
        with long
    else:
        scene cocktailbar
        with long
        "We went inside. It was a classy-looking cocktail bar."
        "One of those fancy businesses that had been opening recently in the downtown area."
        show ian at lef
        show perry2 at rig
        with short
    i "Wow... If I had known it was this kind of place I'd dressed more appropriately..."
    "Perry didn't seem too thrilled."
    p "I don't know why we couldn't go to our usual place. That bar is p--{w=0.5}perfectly fine."
    i "It was Alison who chose this place."
    p "I don't like this kind of posh bars... I don't want a margarita, I just want a good beer!"
    menu:
        "Let's try something new":
            $ renpy.block_rollback()
            i "It can't hurt to try something new."
            p "Yes, it can. It can hurt my w--{w=0.5}wallet!"
            i "Stop complaining and let's find Alison."
            
        "I think it's cool":
            $ renpy.block_rollback()
            $ ian_chad += 1
            $ fian = "smile"
            i "I like the place, it's pretty cool."
            p "It's w--{w=0.5}way too posh."
            i "Stop complaining and let's find Alison."
            
        "I don't like it either":
            $ renpy.block_rollback()
            $ ian_chad -= 1
            i "I know, I don't like this place either. But what's important is the company..."
            i "Let's find Alison and try to have fun."
            
    "She hadn't arrived yet, so we found a free table and secured a spot. The place was getting full of people..."
    hide perry2
    with short
    "I gave Perry a few bucks and he went to grab a couple of beers."
    $ fperry = "mad"
    show perry at rig
    with short
    p "Unbelievable! Five bucks for just a beer! Five b--{w=0.5}bucks!"
    p "And it's not even a p--{w=0.5}pint! This place sucks!"
    if ian_chad > 1:
        $ fian = "n"
        i "Dude, stop complaining, you're bumming me out."
    else:
        i "Damn, that sucks... But a night's a night."
    $ fperry = "meh"
    "We had drunk down half our beer when Alison finally showed up."
    $ alison_look = 2
    $ falison = "smile"
    show ian at centerlef
    show perry at right5
    with move
    $ fian = "surprise"
    $ fperry = "surprise"
    show alison at rig
    with long
    a "There you are! Hi, guys!"
    menu:
        "You look amazing" if v2_alisonflirt > 1:
            $ renpy.block_rollback()
            $ v2_alison_clothes = True
            $ fian = "happy"
            $ fperry = "n"
            i "Wow, Alison, you look amazing!"
            $ falison = "flirt"
            a "Oh, you think so?"
            i "Absolutely."
            $ falison = "smile"
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_alison += 1
            a "Thank you, Ian!"
            hide friend_up
        "Hello, Alison":
            $ renpy.block_rollback()
            $ fian = "smile"
            $ fperry = "n"
            i "Hello, Alison. You finally show up!"
            a "Sorry, we're a bit late."
        "You dressed up for the occasion":
            $ renpy.block_rollback()
            $ v2_alison_clothes = True
            $ fian = "smile"
            $ fperry = "n"
            i "I see you dressed up for the occasion!"
            a "You think so? I don't know..."
            i "I have never seen you looking like this!"
            a "Do you think it suits me?"
            i "Yeah."
            a "Good to know!"
        "What's with those clothes?":
            $ renpy.block_rollback()
            $ fian = "worried"
            $ fperry = "n"
            i "What's with those clothes?"
            $ falison = "serious"
            a "What's wrong with them?"
            i "Nothing wrong, I guess..."
            i "It's just I'm not used to seeing you looking like this!"
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_alison -= 1
            a "Maybe you should try grooming yourself a bit more sometime, too!"
            $ falison = "n"
            hide friend_down
    a "Let me introduce you to my friend Cherry."
    show cherry at left
    with long  
    $ fian = "blush"
    $ fperry = "surprise"
    ch "Hi guys, nice to meet you."
    "A stunning dark-skinned beauty showed up from behind Alison. She was slender and striking in style and demeanor." 
    i "Hey... I'm Ian, and this here is my friend Perry."
    $ fperry = "meh"
    p "H--{w=0.5}h--{w=0.5}h--{w=0.5}hey."
    a "What are you drinking?"
    $ fian = "n"
    i "Just beer."
    a "Let's go get something for ourselves. What do you want, Cherry?"
    ch "I've been dying for a good Tequila Sunrise."
    a "We'll be right back."
    $ ian_cherry_agenda = True
    hide alison
    hide cherry
    with short
    $ fperry = "sad"
    $ fian = "worried"
    show ian at lef
    show perry at rig
    with move
    i "Holy shit."
    p "D--{w=0.5}dude, have you seen that?"
    i "Of course I have. Alison looks stunning."
    p "Not Alison, her friend Cherry! She looks like she has popped up from a fashion magazine or something like that!"
    p "Who s--{w=0.5}stutters so much just to say a simple \"hey\"? I'm sure she thinks I'm an i--{w=0.5}idiot."
    i "Calm down. You're way too concerned about that..."
    p "Easy for y--{w=0.5}you to say. You n--{w=0.5}never had my problem."
    p "You don't know what it's like to only b--{w=0.5}be able to speak half of what's on your mind. It's so frustrating."
    p "And when you talk to s--{w=0.5}somebody the first thing they always think is \"oh look, a fucking stutterer\"!"
    p "They find it annoying to s--{w=0.5}speak to me no matter what."
    "He was right. I had no idea what that feeling was like..."
    i "Chill, dude, you're freaking out. Try not to worry so much about what they think about you."
    i "Just think that you're having a couple of beers with your friends, as we always do."
    p "That would be easier if we w--{w=0.5}were at our usual place! Oh, here they come!"
    p "Please, stick with me and d--{w=0.5}don't you leave me alone with the girls."
    $ fian = "n"
    $ fperry = "meh"
    $ falison = "n"
    show ian at centerlef
    show perry at right5
    with move
    show alison at rig  
    show cherry at left
    with short     
    "They came back with their cocktails and sat with us."
    a "Where's Jeremy, by the way?"
    i "He said he'll come later. He had... something to take care of."
    a "Really? What's so important that he has to take care of it at this hour?"
    menu:
        "You should ask him yourself":
            $ renpy.block_rollback()
            i "You should ask him yourself when he shows up."
            a "So mysterious. Alright, I will."
            
        "He's with a girl":
            $ renpy.block_rollback()
            $ v2_tell_jeremy_girl = True
            i "Oh, he's with a girl."
            $ falison = "surprise"
            a "He went on a date?"
            i "Yeah. He said he'd come as soon as he's finished with that."
            $ falison = "serious"
            a "I see... So we're only second best to him."
            i "Everyone has his priorities..."
            
        "I don't know":
            $ renpy.block_rollback()
            i "I... I don't know. He didn't tell."
            a "Really? How weird. It must be something shady."  
     
    $ falison = "smile"
    a "So, do you like this bar?"
    if ian_chad == 2:
        $ fian = "smile"
        i "Yeah, I like it pretty much! It has a nice ambience."
        "Cherry pointed at my beer."
        ch "You haven't tried the cocktails, though. It's this bar's specialty."
        i "I was waiting for you, girls. I'm gonna get one when I'm done with this."
        i "Any recommendations?"
        $ fcherry = "smile"
        ch "My favorite is the Tequila Sunrise, but to each his own..."
        i "Noted. You want to try it too, Perry?"
        p "No, t--{w=0.5}thanks... I'll stick to beer."
    elif ian_chad == 1:
        $ fian = "smile"
        i "It's not bad. Quite different from the place we usually go to, but it's good to change scenery from time to time."
        ch "Where do you guys usually go?"
        p "To the Fortress. It's a rock bar in another p--{w=0.5}part of the town. They have good beer and pool tables."
        $ fcherry = "smile"
        ch "Sounds cool. I haven't been to one of those since I was in my teens."
        a "It's quite different from this place."
        i "Yeah, not so classy."
        ch "A place doesn't have to be classy to be cool, though."
        $ fperry = "n"
        p "Exactly my thoughts."
    else:
        $ fian = "sad"
        i "It's not my cup of tea, really. I'd prefer it if we went to our usual spot."
        a "That rock bar? I don't know, I think I like it better here."
        a "In any case, I had never been here. It was Cherry who suggested it."
        i "Oh..."
        ch "It's a nice place. I thought you guys would like it, but I had to guess, since I don't know you."
        i "No, it's OK..."
        a "I like it!"
    i "So you two are colleagues?"
    $ falison = "n"
    a "We met at work, yeah. But we work in different departments."
    $ fcherry = "smile"
    ch "Yeah, she takes care of the difficult, numerical stuff. I just send e-mails and talk to people over the phone, ha ha."
    a "It's not our dream job for any of us, that much is clear!"
    $ fian = "smile"
    i "Who's working in their dream job? I'm starting to think that's just fairy tales, ha ha."
    ch "The economy is fucked, but we get by, don't we?"
    p "You c--{w=0.5}changed jobs recently, right Alison?"
    a "Yes."
    p "So you haven't known C--{w=0.5}Cherry for long..."
    a "Nope. In fact, this is our first time going out together!"
    ch "And it was about time!"
    a "Yeah... I wish I wasn't so busy! They can't stop piling up work on my desk, all because the guy whose position I'm filling in now was totally incompetent."
    ch "They fired him for a reason."
    ch "What about you, guys?"
    "We told Cherry we had known each other since high school, that Perry and I were living together and so on."
    "Perry and I finished our beers, and the girls were making quick work of their cocktails."
    i "I'm gonna get some more drinks. Want something?"
    a "Yes, bring one for us too!"
    p "I'm coming with you."
    hide cherry
    hide alison
    with short
    show ian at lef
    show perry at rig
    with move
    $ fian = "n"
    $ fperry = "n"
    "We got up and went to the bar. There were a lot of people, and we had to wait a few minutes for the bartender to attend to us."
    guy "What will it be?"
    p "B--{w=0.5}beer for me."
    i "For me and the girls, three..."
    menu:
        "Bloody Marys":
            $ renpy.block_rollback()
            $ v2_cocktail = 1
            i "Three Bloody Marys!"
            guy "Right away."
        "Margaritas":
            $ renpy.block_rollback()
            $ v2_cocktail = 2
            i "Three Margaritas!"
            guy "Right away."
        "Tequila Sunrises":
            $ renpy.block_rollback()
            $ v2_cocktail = 3
            i "Three Tequila Sunrises!"
            guy "Right away."
    "The bartender began preparing the cocktails."
    i "Well, so far, so good, no?"
    p "Yeah. Cherry seems like a nice gal..."
    p "I wonder if she has a b--{w=0.5}boyfriend..."
    i "Probably. She's very attractive."
    p "But if she had one, wouldn't he be here with her?"
    i "Who knows... Let's get them their drinks."
    $ fian = "smile"
    show ian at centerlef
    show perry at right5
    with move
    show alison at rig  
    show cherry at left
    with short     
    i "Here you go, girls."
    if v2_cocktail == 3:
        if ian_chad == 2:
            ch "Nice! I see you decided to follow my recommendation."
            i "Of course!"
        else:
            ch "You got a Tequila Sunrise for yourself, too?"
            i "Yeah. I saw yours and got jealous. Looks pretty good!"
            ch "It is!"
        play sound "sfx/friendup.mp3"
        show friend_up
        $ ian_cherry += 1      
    elif v2_cocktail == 2:
        $ cherry = "n"
        ch "Oh, a Margarita? I thought I asked for a Tequila Sunrise..."
        $ fian = "worried"
        i "You did? Oh, sorry, I might've gotten it wrong..."
        $ fcherry = "smile"
        ch "Don't worry, I like Margaritas a lot, too."
    else:
        $ cherry = "sad"
        ch "Oh, a Bloody Mary? I thought I asked for a Tequila Sunrise..."
        $ fian = "worried"
        i "You did? Oh, sorry, I might've gotten it wrong..."
        play sound "sfx/frienddown.mp3"
        show friend_down
        $ ian_cherry -= 1 
        ch "I don't really like Bloody Marys..."
        i "I'm sorry. I'll ask the barman if he can change it..."
        $ fcherry = "n"
        ch "It's OK, don't bother. I'll make due with this."
    $ fian = "smile"
    $ fperry = "happy"
    a "Cheers!"
    play sound "sfx/toast.mp3"
    "We toasted, drank and made some small talk, getting to know Cherry a bit more."
    "It wasn't long before Alison turned the focus of the conversation to herself."
    $ falison = "serious"
    a "Oh, you know what happened to me the other day? My ex-boyfriend called me asking me to give back some household stuff, duvet covers and whatnot."
    $ fian = "sad"
    $ fperry = "meh"
    a "Stuff I bought for us with {i}my{/i} money, and for some reason he thinks he's entitled to them."
    $ fcherry = "mad"
    ch "Cheap bastard."
    a "But that's not the worst of it. He asked me if I had slept with somebody else since we broke up."
    i "And what did you tell him?"
    a "I told him it was none of his business. And then he said he was expecting me to refrain from it for at least three or four months, as a sign of mourning for our relationship!"
    $ fcherry = "sad"
    ch "Tell me you're joking."
    a "That's exactly what I told him! He expects me to act like a nun and reject my sexuality out of grievance for him?"
    p "I hope he intends on doing the same, at l--{w=0.5}least."
    a "He says he does, but not because he's mourning. It's because he knows no one's gonna be stupid enough to sleep with him!"
    a "He feels bad about himself and wants to drag me down in his misery. I can't believe I dated someone like him."
    a "He's such a loser."
    ch "Guys can surely be unbelievable. I also have some stories I could tell..."
    a "Who doesn't? I swear, guys are crazy."
    $ fperry = "n"
    menu:
        "Women are crazy, too":
            $ renpy.block_rollback()
            $ fian = "serious"
            i "Don't bash guys so nonchalantly. Women are crazy, too!"
            a "That's because you make us crazy!"
            i "Nobody buys that excuse!"
            $ fian = "smile"
            i "Maybe in your case that's true, however, ha ha."
            a "What's that supposed to mean?"
            $ fcherry = "flirt"
            ch "You're one of those women who lose their mind over guys, Alison?"
            a "I'm not! If anything, I'm very rational..."
            $ fian = "confident"
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup  
            i "Maybe guys are your kryptonite, if you know what I mean..."
            $ falison = "smile"
            a "Ha ha, don't be ridiculous..."
            ch "I don't know, Ian has a point... You don't seem as rational as you claim to be, ha ha!"
            $ falison = "surprise"
            $ fian = "happy"
            a "Hey!"
            
        "Relationships are only trouble":
            $ renpy.block_rollback()
            $ fian = "n"
            i "Relationships are only trouble... For both men and women."
            $ falison = "n"
            a "You're absolutely right."
            $ fcherry = "sad"
            ch "They sure are... But they're worth the trouble, ain't they?"
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup   
            i "That's what you think until everything comes crashing down. Then you're left with only trouble and no relationship."
            ch "That's such a pessimistic way to look at it..."
            $ fian = "smile"
            i "Let's just call it realistic... I haven't lost hope yet!"
            $ fcherry = "smile"
            ch "Good to know. Hope is the last thing to lose, right?"
            a "You're a bunch of romantics!"
            
        "There must be someone good out there":
            $ renpy.block_rollback()
            i "There must be someone good out there... Someone who's not a crazy asshole."
            a "You'll have better luck searching for a unicorn!"
            i "Don't be so bitter!"
            i "Believe me, I have more reason than you to think like that and be bitter towards relationships... And I guess I am."
            $ fian = "smile"
            i "But having that outlook in life is so cynical and shitty. For sure, there will always be trouble in a relationship, and maybe nothing lasts forever..."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup   
            i "But what's the point of it all if we don't try to enjoy the ride?"
            $ fcherry = "happy"
            ch "That's a very nice way to put it!"
            a "Well yeah, let me know how that works for you."
            
        "Don't say anything":
            $ renpy.block_rollback()
            $ fian = "n"
            i "..."
            "They were complaining about guys. I didn't want to say anything in case they attacked me, too..."
            
    $ falison = "n"
    a "I have one thing clear in my mind: the last thing I want right now is a serious relationship."
    a "The last thing!"
    $ fcherry = "smile"
    $ fian = "smile"
    ch "It's understandable, after what happened with your ex. You need some freedom right now."
    a "Exactly. To be honest, dumping him, painful as it was, felt like dropping a weight off my shoulders."
    a "I have no intention of loading myself with another one!"
    ch "Well said! Let's toast to that!"
    a "Hey, you guys want some shots? They're on me!"
    $ fperry = "happy"
    p "Oh, s--{w=0.5}shots! It's been a long time since I had one. I'm i--{w=0.5}in!"
    i "Alright, me too."
    ch "I'll go with you."
    a "Don't worry, I've got this. Stay with them, I'll be right back."
    if v2_alisonflirt > 2:
        "Before leaving, Alison turned back and looked at me."
        a "Maybe I could use some help... Ian."
    menu:
        "Go with Alison" if ian_alison_interest > 0:
            $ renpy.block_rollback()
            $ v2_bar_alison = True
            "I got up."
            i "Sure, I'll come with you."
            $ fperry = "sad"
            "Perry looked at me with a silent plea, but I wasn't there to babysit him."
            i "Be right back."
            jump v2_alisonbar
            
        "Stay with Cherry and Perry":
            $ renpy.block_rollback()
            if v2_alisonflirt > 2:
                i "I don't want to leave poor Cherry alone with Perry, ha ha."
                a "Oh, OK."
            else:
                "I let Alison go fetch those shots."
            hide alison
            with short
            jump v2_cherrybar
            
## CHERRY #############################################################################################################################################
    
label v2_cherrybar:
    
    show perry at rig3
    show ian at truecenter
    show cherry at lef3
    with move
    $ fian = "n"
    $ fcherry = "n"
    $ fperry = "n"
    "Perry and I were left alone with Cherry and we found ourselves in an awkward silence for a second."
    menu:
        "{image=icon_charisma.png}Break the ice" if ian_charisma > 1:
            $ renpy.block_rollback()
            $ v2_cherry_interest += 1
            i "I hope you're not too mad with Alison, Cherry."
            ch "Mad? Why should I be mad?"
            i "I don't know how she convinced you to come here tonight, but I'm sure she had to lie to you."
            $ fian = "happy"
            i "And now she's left you stuck with a couple of weirdos. What a friend she is!"
            $ fperry = "meh"
            p "Hey, t--{w=0.5}talk for yourself."
            $ fcherry = "happy"            
            ch "Ha ha ha! Oh, come on, don't say that."
            i "In our defense I will say we didn't know we were coming to such a fancy place. I'm surprised they even let us in, the way we're dressed."
            ch "Well, look at it from the bright side... This way you stand out!"
            i "Yes, we do, but I'm gonna tell you the real reason: people must be thinking \"how the hell are those two nerds hanging out with such beautiful girls?\"" 
            p "Dude, s--{w=0.5}stop including me." 
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_cherry += 1   
            ch "Ha ha ha! Stop it, now you're just messing with me."
            $ fian = "n"
            $ fperry = "n"
            i "Maybe. Just trying to make you feel comfortable."
            ch "I am. And honestly, you guys are OK. Who's not a bit weird, after all? Normal people are just boring."
            i "I'm glad you think that way, because Alison's probably the weirdest of us all. Don't let her trick you."
            ch "She's a funny girl, yeah, ha ha! But I like her."
            i "I hope you like us, too."
            $ fcherry = "smile"
            ch "I do."
            "Gone was that momentary awkwardness. I felt comfortable talking to Cherry, and she seemed comfortable with me too..."
            hide friend_up
            
        "So you come here often?":
            $ renpy.block_rollback()
            $ perry_cherry += 1
            "I tried to make a bit of conversation with her."
            i "So Cherry, you come here often?"
            ch "Here? Not really... I've only come a couple of times before."
            ch "The place is nice and I thought it would be a safe bet, but I see I was mistaken!"
            if ian_chad == 2:
                i "I like it!"
                ch "But not Perry, it seems. You haven't even tried the cocktails!"
                p "I'm not into t--{w=0.5}those. Too fancy for me... What I enjoy is a g--{w=0.5}good beer!"
                $ fcherry = "smile"
                ch "Is that so? Where do you guys usually go, then?"
                $ fperry = "smile"
                p "To the Fortress. It's a rock bar in another p--{w=0.5}part of the town. They have good beer and pool tables."
                p "And the music is way better. The ambience is just much more authentic."
                $ fcherry = "happy"
                ch "Sounds cool! I haven't been to one of those since I was in my teens, but I'm kind of missing it now."
            elif ian_chad == 1:
                i "It's not bad..."
                p "Be honest, dude. It's not our thing."
                $ fcherry = "smile"
                ch "That rock bar you talked about sounds nice."
                $ fperry = "smile"
                p "It's the b--{w=0.5}best. They have a ton of beers, cheap ones, and special brews too."
                p "And the music is way better. The ambience is just m--{w=0.5}much more authentic."
                $ fcherry = "happy"
                ch "You're selling it well! I'm kinda beginning to miss going to a place like that..."
            else:
                i "Well, it's... not so bad..."
                p "Be honest, dude. It's not our thing."
                $ fcherry = "smile"
                ch "Alison talked about a rock bar. Is that where you guys usually go?"
                $ fperry = "smile"
                p "Yeah! It's called the Fortress. They have good b--{w=0.5}beer, and cheap! And also pool tables."
                p "And the music is way better. The ambience is j--{w=0.5}just much more authentic."
                $ fcherry = "happy"
                ch "Sounds cool! I haven't been to one of those since I was in my teens, but I'm kind of missing it now."
            ch "Maybe you can show it to me one of these days."
            p "Hell yeah!"
            ch "Does Alison like those kind of places, though?"
            i "She never complained."
            ch "She rarely does..."
       
        "Keep quiet":
            $ renpy.block_rollback()
            "Suddenly I didn't know what to say. With Alison gone, I felt there was a block between me and Cherry."
            i "..."
            "Perry wasn't being helpful, either."
            $ fperry = "sad"
            p "..."
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_cherry -= 1  
            ch "..."
            ch "So, guys... You said you've known Alison since high school?"
            i "Yeah..."
            ch "And did you know her ex-boyfriend?"
            p "I think I saw him once, but n--{w=0.5}never really talked to him."
            i "I didn't get to know him much more, either. Maybe saw him a couple of times."
            hide friend_down
     
    $ fcherry = "sad"
    ch "I'm sorry about her situation, honestly."
    $ fian = "n"
    $ fperry = "n"
    i "Yeah..."
    p "Life s--{w=0.5}sucks."
    $ fcherry = "smile"
    ch "She's so tough, though! I think I would be pretty bummed out in her situation, but she keeps moving forward with a lot of positive attitude."
    $ fian = "smile"
    i "I guess we all can learn from her. But not everybody has her vitality and energy."
    ch "I know. But that's why I like having her around. It's kind of contagious."
    i "So you're in need of that positive attitude, too?"
    $ fcherry = "n"
    ch "A bit, yeah. I went through hard times recently, too."
    $ fian = "worried"
    p "Damn, seems like everybody's having relationship p--{w=0.5}problems these days..."
    ch "Not you, Perry?"
    p "No. I mean..."
    p "I guess n--{w=0.5}not. I just don't have anything. And I d--{w=0.5}don't miss it, honestly."
    $ fcherry = "smile"
    ch "That's one sure way to steer clear of problems."
    $ fian = "n"
    p "Where are our shots, by the w--{w=0.5}way? Alison's taking forever!"
    $ fcherry = "n"
    ch "Seems that the bar is getting crowded."
    menu:
        "Keep chatting with Cherry":
            $ renpy.block_rollback()
            if v2_cherry_interest == 1:
                "I was enjoying talking to Cherry. I didn't want to cut it short."
            i "She won't take long now."
            i "So, Cherry..."
    
        "Go find Alison":
            $ renpy.block_rollback()
            $ v2_find_alison = True
            jump v2_findalison
             
    menu:
        "{image=icon_wits.png}You don't look like an office worker" if ian_wits > 1:
            $ renpy.block_rollback()
            $ v2_cherry_interest += 1
            $ fian = "smile"
            i "You really work at the same company as Alison?"
            i "I'm not calling you a liar, but you don't look like an office worker, honestly."
            $ fcherry = "happy"
            ch "I don't? What gave me away?"
            i "I can't exactly tell... Maybe the way you're dressed, or the way you walk... Just the vibe you give."
            i "I feel like there's something more to you."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_cherry += 1   
            ch "You have a good eye! Indeed, I'm not an office worker because that's my passion."
            ch "I studied fine arts and I'd love to be a painter, but you know how this goes. I have to pay the bills, so painting is just a hobby."
            $ fperry = "smile"
            $ fian = "happy"
            i "No way! Perry studied art, too. And I'm a writer. Well, an aspiring one."
            ch "Really? That's so interesting! Tell me more about it."
            "We began talking about art and our experiences with it, and how hard it was making a living out of it."
            if v2_cherry_interest == 2:
                "I felt things were really flowing between me and Cherry..."
            else:
                "Cherry and I had more things in common than I thought. She was an interesting girl..."
            hide friend_up
            
        "Tell us about your job":
            $ renpy.block_rollback()
            $ perry_cherry += 1
            "I tried to think about something I could ask her."
            i "So, tell us about your job?"
            $ fcherry = "n"
            ch "There's nothing to tell... It's pretty boring."
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_cherry -= 1  
            ch "And to be honest, the last thing I want to discuss when I'm out drinking is work."
            $ fian = "sad"
            i "Oh... Sorry."
            p "What do you like to d--{w=0.5}discuss?"
            ch "I don't know... Let's talk hobbies. What is your passion?"
            p "I like to draw and that kind of s--{w=0.5}stuff."
            $ fcherry = "happy"
            ch "Really? I studied fine arts and I love to paint!"
            $ fperry = "happy"
            p "No way! Such a c--{w=0.5}coincidence. How come you're working in an office?"
            ch "I'd love to be a painter, but you know how this goes. I have to pay the bills, so painting is just a hobby."
            p "Yeah, I'm having a lot of t--{w=0.5}trouble finding work too..."
            "Cherry and Perry began talking about art and their own experience with it."
            hide friend_down
            
        "What are your hobbies?":
            $ renpy.block_rollback()
            $ perry_cherry += 1
            $ v2_cherry_interest += 1
            i "Aside of working with Alison, what can you tell us about yourself? What are your hobbies?"
            ch "Well, they have nothing to do with my office work, that's for sure."
            ch "What I really like is to paint. I studied fine arts."
            $ fperry = "happy"
            p "No way! I s--{w=0.5}studied art, too. I love to draw and stuff."
            $ fcherry = "happy"
            ch "Is that so? Do you work as an artist?"
            $ fperry = "sad"
            p "No, I c--{w=0.5}can't seem to find a job... It's too d--{w=0.5}difficult!"
            ch "I know, right? I would love to be a painter, but I have to pay the bills... So I'm stuck with a desk job."
            $ fperry = "happy"
            "Cherry and Perry began talking about art and their own experience with it."
    jump v2_barfollowup

label v2_findalison:     
    i "I'll go help her. I'll be right back."
    hide perry
    hide cherry 
    with short
    "I got up and went looking for Alison. The bar was really full of people, it seemed that it was quite popular..."
    scene cocktailbar
    show v2_alison1b
    with short
    "Then I saw her. She was next to the bar, and Jeremy was with her."
    "They were very close together. Way too close."
    "Jeremy was holding her against his chest, talking to her ear, and Alison was smiling and chuckling."
    "I hesitated for a moment, but decided to approach them."
    $ fian = "worried"
    $ falison = "smile"
    $ fjeremy = "flirt"
    scene cocktailbar
    show ian at rig3
    show alison
    show jeremy at lef3
    with short
    i "Hey... I see you're already here, Jeremy."
    j "Hey, Ian! Yeah, me and Alison are waiting for our drinks..."
    i "You were taking too long, so I came searching for you."
    a "Oh, you were worried about me?"
    $ fian = "n"
    i "Yes, but I see you're in very good company."
    j "Indeed, she is!"
    a "Hee hee! Nights like this make me remember the old times. Like when we were in high school. We used to hang out more back then."
    $ falison = "n"  
    j "Yep, but adult life got in the way!"
    a "Sometimes I miss those times, everything seemed simpler. I remember that concert you did with Perry and Wade, Ian... What was the name of your band?"
    $ fjeremy = "happy"
    j "They were called {i}Fucking Chicken Nuggets{/i}!"   
    $ falison = "smile"
    a "Oh, that's true! It was such a stupid name."
    i "Perry came up with it."
    a "Why?"
    i "We were rehearsing one night, got really high on weed and ordered out super hungry..."
    i "We ordered a ton of chicken nuggets to stop the munchies. And Perry kept saying \"I love these fucking chicken nuggets\" while stuffing his mouth with it."
    i "And it just stuck... But yeah, it's a very stupid name."
    $ fjeremy = "smile"
    j "I thought it was a very funny name."
    i "We were just some stupid kids back then."
    $ falison = "n"
    a "That might be true, but I thought you were really cool when I saw you playing on stage that night."   
    menu:
        "{image=icon_charisma.png}I liked you too" if ian_charisma > 0 and ian_alison_interest > 0:
            $ renpy.block_rollback()
            $ v2_alisonflirt += 1 
            i "I thought you were cool, too."
            $ falison = "flirt"
            a "Me? How so?"
            i "I always had a blast around you. I liked your personality and I thought you were attractive."
            a "You thought I was attractive? Really?"
            i "Yeah."
            j "You've always been pretty hot!"
            $ falison = "n"
            a "Ha ha, that's funny... We were teenagers back then... I guess a lot has changed."
            i "Some things have. I haven't played the bass for years now."
            i "But I still think the same about you."
            $ falison = "blush"
            a "Is that so...?"
            $ falison = "n"
            j "We all think that about you! You're cool, Alison."
            a "Well, thank you!"
       
        "I wasn't cool at all":
            $ renpy.block_rollback()
            $ v2_alisonflirt -= 1 
            $ fian = "sad"
            i "Nah, I wasn't cool at all. Just a dumb teenager trying to fit in."
            a "We were all dumb teenagers trying to fit in. Be we did some things right, too."
            $ falison = "sad"
            a "Or so I like to think... Sometimes I wonder what would our teenage selves think if they saw us right now."
            a "Would they be hopeful, or feel let down?"
            $ fian = "n"
            j "That's not something you should think about! Tonight we're having fun!"
            $ falison = "n"
            j "The good times are now!"
            a "You're right!"
            
        "You thought I was cool?":
            $ renpy.block_rollback()
            i "Oh, you thought I was cool? You never told me!"
            a "Yes, I did."
            i "I don't remember that being the case..."
            a "Well, I'm telling you now."
            i "A bit late for that, isn't it? Ha ha. It's been years since I stopped playing the bass."
            a "You still do cool things, like writing and all that."
            j "Ian's a cool dude, in his own way!"
     
    j "Oh, here are our drinks!"
    a "Let's get back to the others."
    jump v2_barfollowup
     
## ALISON ############################################################################################################################################################################

label v2_alisonbar:     
    $ jeremy_look = 1
    hide perry
    hide cherry
    with short
    show ian at rig
    show alison at lef
    with move
    $ fian = "smile"
    $ falison = "n"
    "I followed Alison to the bar, but it was crowded with people. We had to wait in line before ordering our drinks."    
    if ian_alison_interest == 2:
        "Not that it bothered me. That way I could spend some time alone with Alison."
    elif ian_alison_interest == 1:
        "It didn't bother me too much. I could talk with Alison in the meantime."
    i "I'm glad that we're doing this tonight. Suddenly it seems I get to see you more often."
    a "I know I've been hard to meet these past few months. Losing my job, breaking up with my boyfriend, finding work..."
    a "It's been quite hectic. But I'm alright now. And I'm happy to spend more time with you, too!"
    if v2_alison_clothes:
        a "By the way, the comment you made about my clothes... Do you think they suit me?"
        menu:
            "They do":
                $ renpy.block_rollback()
                $ alison_sexy = True
                i "Absolutely. This look really suits you."
                $ falison = "smile"
                a "I'm glad you think that way. I wasn't sure about it..."
                a "I can't remember the last time I dressed like this."
                i "You should do it more often."
                
            "You look different":
                $ renpy.block_rollback()
                i "It's not that it doesn't suit you, but you look... different."
                a "I thought so. Anyways, it's something I can wear from time to time, I guess."
                
    if v2_alisonflirt == 3:
        $ falison = "flirt"
        a "Also... You never told me I was \"hot\" before."
        i "You never asked what I thought."
        a "So I need to ask?"
        i "If you want my opinion, yes."
        a "I see. I'll remember that. Though it's also appreciated if you just want to let me know your thoughts."
        i "I'll also remember that."
        $ falison = "n"
    elif v2_alisonflirt == 2:
        $ falison = "smile"
        a "Also... You never told me I was \"beautiful\" before."
        i "You never asked what I thought."
        "She chuckled."
        a "So you think I'm beautiful?"
        i "Who doesn't? It's obvious to see."
        a "You're so nice."
    $ falison = "n"    
    a "Nights like this make me remember the old times. Like when we were in high school. We used to hang out more back then."
    a "I remember that concert you did with Perry and Wade... What was the name of your band?"
    i "{i}Fucking Chicken Nuggets{/i}."   
    $ falison = "smile"
    a "Oh, that's true! It was such a stupid name."
    i "Perry came up with it."
    a "Why?"
    i "We were rehearsing one night, got really high on weed and ordered out super hungry..."
    i "We ordered a ton of chicken nuggets to stop the munchies. And Perry kept saying \"I love these fucking chicken nuggets\" while stuffing his mouth with it."
    i "And it just stuck... But yeah, it's a very stupid name. We were just some stupid kids."
    $ falison = "n"
    a "I thought you were really cool when I saw you playing that night."   
    menu:
        "{image=icon_charisma.png}I liked you too" if ian_charisma > 0:
            $ renpy.block_rollback()
            $ v2_alisonflirt += 1 
            i "I thought you were cool, too."
            $ falison = "flirt"
            a "Me? How so?"
            i "I always had a blast around you. I liked your personality and I thought you were attractive."
            a "You thought I was attractive? Really?"
            i "Yeah."
            $ falison = "n"
            a "Ha ha, that's funny... We were teenagers back then... I guess a lot has changed."
            i "Some things have. I haven't played the bass for years now."
            i "But I still think the same about you."
            $ falison = "blush"
            a "Is that so...?"
            $ falison = "n"
       
        "I wasn't cool at all":
            $ renpy.block_rollback()
            $ v2_alisonflirt -= 1 
            $ fian = "sad"
            i "Nah, I wasn't cool at all. Just a dumb teenager trying to fit in."
            a "We were all dumb teenagers trying to fit in. Be we did some things right, too."
            $ falison = "sad"
            a "Or so I like to think... Sometimes I wonder what would our teenage selves think if they saw us right now."
            a "Would they be hopeful, or feel let down?"
            $ fian = "n"
            i "Better not to think about that..."
            $ falison = "n"
            
        "You thought I was cool?":
            $ renpy.block_rollback()
            i "Oh, you thought I was cool? You never told me!"
            a "Yes, I did."
            i "I don't remember that being the case..."
            a "Well, I'm telling you now."
            i "A bit late for that, isn't it? Ha ha. It's been years since I stopped playing the bass."
            a "You still do cool things, like writing and all that."  
            
    a "Look, there's some space at the bar! Let's go."
    "We pushed through to get a spot at the bar and ask for the shots."
    if v2_alisonflirt > 1:
        scene cocktailbar
        show v2_alison1
        with short
        "The crowd squeezed us together, and I found Alison's back resting against my chest."
        "Far from feeling uncomfortable in this position, she leaned back on me, making even more contact between our bodies."
        "I rested my hand on her hip, her hair practically brushing against my nose. Her smell was so sweet..."
        a "Six tequila shots for us, please!"
        i "Why six? We're only four people."
        a "Let's have an extra one, just you and me."
        "The barman poured the shots and Alison and I toasted and drank one."
        a "To us!"
        "We gulped it down and I felt the alcohol burning in my throat and chest."
        i "Oof, that was strong."
        "Alison turned sideways and looked at me."
        a "Say, Ian..."
        a "How come nothing ever happened between us?"
        "Her question was so direct it left me perplexed for a second."
        menu:    
            "{image=icon_lust.png}Kiss her" if ian_lust > 0 and v2_alisonflirt > 2:
                $ renpy.block_rollback()
                $ v2_alisonflirt += 1 
                $ v2_alison_home = True
                "I tried to think how to respond to that, but the best answer was so obvious."
                scene cocktailbar
                show v2_alison2b
                with long
                "I turned her around and kissed her."
                "It was an impulse I couldn't contain. I just had to do it."
                "And she responded in the best way possible."
                "She wrapped her arms around my shoulders and kissed me back, pulling me even closer."
                "Our tongues met right away in a deep, long kiss."                
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_alison += 1   
                "It was really happening... After all this time, Alison and I were making out..."
                "And it felt as good as I had always thought it would."
                $ fian = "smile"
                $ falison = "flirt"
                scene cocktailbar
                show ian at rig
                show alison at lef
                with long
                i "How's that for an answer?"
                "She smiled at me."
                a "Better late than never, I guess..."
                show alison at truecenter
                show ian at rig3
                with move
                show jeremy at lef3
                with short
                $ falison = "n"
                j "Yo, guys! What's up?"
                i "Hey, dude. Here you are at last."
                j "Am I interrupting something?"
                a "Kind of..."
                j "Ha ha, I'm sorry."
                i "We were just getting some tequila shots and bringing them to Perry and Cherry."
        
            "We were too young and naive":
                $ renpy.block_rollback()
                $ v2_alisonflirt += 1 
                i "I guess we were just too young and naive..."
                a "Do you think that's the reason?"
                i "Probably."
                a "So if we hadn't been young and naive, something would've happened?"
                i "Who knows? It's hard to tell..."
                i "Though we're not young nor naive anymore."
                a "No, we're not..."
                scene cocktailbar
                show alison at truecenter
                show ian at rig3
                show jeremy at lef3
                with short
                $ falison = "n"
                j "Yo, guys! What's up?"
                i "Oh, hey, dude. Here you are at last."
                j "Am I interrupting something?"
                a "What? No... We were just getting some tequila shots and bringing them to Perry and Cherry!"
                
            "I never thought about it":
                $ renpy.block_rollback()
                i "I never thought about it honestly... Did you?"
                a "I'm wondering about it now. We used to be such good friends, weren't we?"
                i "Yes. I guess that's why, we were just good friends."
                a "Sometimes friendship turns into something more, especially when you're that young. But it didn't in our case."
                a "Maybe we were already really mature back then?"
                i "Who knows... As I said, I never thought about it..."
                scene cocktailbar
                show alison at truecenter
                show ian at rig3
                show jeremy at lef3
                with short
                $ falison = "n"
                j "Yo, guys! What's up?"
                i "Oh, hey, dude. Here you are at last."
                j "Am I interrupting something?"
                a "No, we were just getting some tequila shots and bringing them to Perry and Cherry!"
                
            "It would've been weird":
                $ renpy.block_rollback()
                $ v2_alisonflirt -= 1 
                i "It would've been weird, don't you think?"
                $ fian = "worried"
                $ falison = "sad"
                scene cocktailbar
                show ian at rig
                show alison at lef
                with short
                a "You think so?"
                i "We were good friends, and at that age hooking up always ends badly..."
                i "If something had happened back then, we probably wouldn't be friends right now."
                a "I guess you're right."
                show alison at truecenter
                show ian at rig3
                with move
                show jeremy at lef3
                with short
                $ falison = "n"
                j "Yo, guys! What's up?"
                i "Hey, dude. Here you are at last."
                j "Am I interrupting something?"
                a "Not at all. We were just getting some tequila shots and bringing them to Perry and Cherry!"
    else:
        show alison at truecenter
        show ian at rig3
        with move
        show jeremy at lef3
        with short
        j "Yo, guys! What's up?"
        $ falison = "smile"
        a "Jeremy! Here you are! I was beginning to think you wouldn't show up!"
        j "And miss seeing you? Not a chance."
        j "How's it going?"
        i "We were just getting some tequila shots and bringing them to Perry and Cherry."
    
    j "Nice! Let me get myself a drink and I'll go with you."
    jump v2_barfollowup
    
##BAR FOLLOWUP ####################################################################################################################
    
label v2_barfollowup:
    $ fjeremy = "smile"
    $ jeremy_look = 1
    if v2_bar_alison:
        $ fcherry = "n"
        $ fperry = "meh"
        "We came back with the shots."
        scene cocktailbar
        show jeremy at left5
        show alison at lef5
        show ian at truecenter
        show cherry at rig5
        show perry2 at right5
        with long
        "We found Perry and Cherry sitting next to each other, checking their phones instead of making conversation..."
        "Cherry looked kinda bored, and Perry frustrated."
        p "Here you are! You t--{w=0.5}took so damn long..."
        i "Sorry, the bar was so crowded..."
        p "Yeah, sure."
        j "Hey people."
        "He introduced himself to Cherry."
        j "Hi, I'm Jeremy. Nice to meet you. What's up, Perry?"
        "We sat down next to them."
    elif v2_find_alison:
        $ fcherry = "smile"
        $ fperry = "n"
        "I came back with Alison and Jeremy."
        scene cocktailbar
        show ian at truecenter
        show jeremy at left5
        show alison at lef5
        show cherry at rig5
        show perry at right5
        with long
        p "Here you are, f--{w=0.5}finally!"
        j "Hey people."
        a "The bar was so crowded!"
        j "And we might've had a couple of shots too, ha ha."
        "He introduced himself to Cherry."
        j "Hi, I'm Jeremy. Nice to meet you."
        "We sat down next to them."
    else:
        $ falison = "n"
        show cherry at truecenter
        show perry at right5
        show ian at rig5
        with move
        show jeremy at left5
        show alison at lef5
        with short
        "Finally, Alison came back. She was with Jeremy."
        j "Hey people."
        i "Hey. You took so long!"
        a "The bar was so crowded!"
        j "And we might've had a couple of shots too, ha ha."
        "He introduced himself to Cherry."
        j "Hi, I'm Jeremy. Nice to meet you."
        "They both sat down next to us."
    $ fcherry = "n"
    a "Cheers!"
    "We picked up the shots and gulped them down."
    $ fperry = "n"
    p "Woah, t--{w=0.5}that was strong! I'm not used to it a--{w=0.5}anymore..."
    j "Tonight you can get used to it again! Next round's on me!"
    p "Another one? S--{w=0.5}sure, if you're  paying."
    a "Wait, Jeremy. I haven't asked you yet: what took you so long?"
    j "I had something to take care of."
    if v2_tell_jeremy_girl:
        $ falison = "flirt"
        a "Don't try to act all mysterious! Ian told us you were with a girl."
        $ fjeremy = "n"
        play sound "sfx/frienddown.mp3"
        show friend_down
        $ ian_jeremy -= 1 
        j "Oh, he did, huh?"
        $ fian = "n"
        j "Well, yeah, I was with a girl."
        a "Who is she?"
        j "Just a girl I met through a dating app some time ago. We've been hooking up for a while now, but she's kinda too demanding."
        a "Too demanding? So she can't get enough of you?"
        $ fjeremy = "flirt"
        j "Well, yeah, I guess. That's what happens when you taste quality!"
        a "Oh, come on, you're such a show-off!"
        j "You don't think I'm that good?"
        a "I have serious doubts about it!"
        j "You can't judge the product if you haven't tried it, baby!"
        "Jeremy wasn't even trying to hide his flirting at this point..."
        if ian_alison_interest == 2:
            "Even though he knew I had showed interest in Alison..."
        hide friend_down
    else:
        a "What of? Come on, don't try to be mysterious!"
        $ fjeremy = "flirt"
        j "A man has his mysteries, Alison! If you want to know them, you'll need to dig a bit deeper."
        a "You're such a show-off! If I give you enough tequila you'll talk?"
        j "Only if you drink it with me. Though you'll pass out before my tongue loosens up..."
        $ fian = "worried"
        j "Or rather you'll pass out {i}if{/i} my tongue loosens up? Ha ha ha!"
        $ falison = "flirt"
        a "I don't know about your tongue, but you love running your mouth, ha ha!"
        "Jeremy wasn't even trying to hide his flirting at this point..."
        if ian_alison_interest == 2:
            "Even though he knew I had showed interest in Alison..."
        p "Knowing you, you were probably with a girl..."
        j "Who knows. Could be..."
    a "Stop bragging! You think you're some kind of playboy? Ha ha."
    $ fjeremy = "happy"
    j "The true playboy here is my man Ian! How's it going with the model?"
    $ falison = "surprise"
    $ fian = "blush"
    a "A model? What is he talking about, Ian?"
    j "A waitress Ian met in a café, and turns out she does nude modeling."
    if v1_alisonlunch:
        a "No way! {i}That{/i} girl we met at the café?"
    else:
        a "Really?"
    if v2_ian_date:
        i "You guys are making a big deal out of nothing!"
        $ falison = "flirt"
        if v2_kiss:
            p "It's not n--{w=0.5}nothing. You kissed her."
            j "Congrats, dude! You didn't tell me!"
            a "You didn't tell me either! You've been keeping it all to yourself, I see... Well, except for Perry."
            i "Because you guys just love to gossip!"
            i "We're not sixteen anymore. A kiss doesn't mean that much..."
            a "It doesn't, huh?"
        i "We just met at the record store, hung out and talked a bit. That's all there is to it so far."
        j "You said it: \"so far\"."
        if v2_kiss == False:
            a "So you went on a date and didn't say anything to us! How rude!"
            i "It's not like I'm obligated or something. You guys just love to gossip a bit too much!"
    else:
        $ falison = "flirt"
        i "We exchanged Peoplegrams, but that's about it. I talk to her when I go to the café she works at and nothing more."
        j "Dude, I thought you would've made some progress."
    $ fian = "n"
    i "Stop breaking my balls. If there's anything to tell about it I'll let you guys know."
    i "For now she's just a friend."
    $ fjeremy = "flirt"
    $ falison = "n"
    "I managed to make them change the subject. I wasn't enjoying being scrutinized."
    if perry_cherry > 1:
        "The conversation kept going. Alison and Jeremy were hitting it off and Perry and Cherry seemed to be having a very friendly conversation."  
    else:
        "The conversation kept going. Alison and Jeremy were hitting it off and Perry and Cherry made some small talk." 
    "Jeremy was getting pretty close to Alison, smiling and looking at her with flirty eyes..."
    menu:
        "{image=icon_lust.png}Maintain eye contact with Cherry" if v2_cherry_interest == 2 and ian_cherry > 4:
            $ renpy.block_rollback()
            $ v2_cherry_interest += 1
            "I tuned my attention to Cherry and made eye contact with her."
            "I didn't want to lose the mood we had been building."
            "Alison, Jeremy and Perry were busy talking about something, so I had Cherry to myself."
            hide jeremy
            hide perry
            hide perry2
            hide alison
            with short
            show ian at rig
            show cherry at lef
            with move
            $ fian = "confident"
            i "So... What were we talking about?"
            $ fcherry = "flirt"
            ch "About your conquests, I believe."
            i "They just love to gossip and give me shit. But I haven't conquered anything yet..."
            ch "Yet? So you're aiming to conquer something?"
            i "\"Conquering\" just doesn't sound right. Change the verb and maybe I'll tell you."
            ch "You should be the one to chose the right word. You're the writer, after all."
            $ fian = "happy"
            i "You got me there. Hmm... Let's change \"conquer\" with \"connect\"."
            $ fian = "confident"
            i "Yeah, I'm trying to connect with someone."
            "I didn't know if it was thanks to the tequila shots or what, but I felt confidence swelling in me."
            "I was enjoying this."
            ch "I see... Well, I don't know if it's with the person you're interested in, but you're connecting with someone tonight."
            "Holy shit. That was as direct as a girl could get in my experience. I could barely believe it, but she was letting me know she was attracted to me, wasn't she?"
            menu:
                "Keep flirting":
                    $ renpy.block_rollback()
                    $ v2_cherry_home = True
                    play sound "sfx/xp.mp3"
                    show lust_up
                    $ ian_lust_xp += 1
                    call screen skillsup   
                    i "You're not mistaken. That's exactly the person I was aiming for."
                    "Cherry looked at me and smiled before answering."
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    $ ian_cherry += 1  
                    ch "Good to know I'm not mistaken, then."
                    ch "Let's get another round of shots! Come with me."
                    $ fian = "smile"
                    i "Sure thing."
                    jump v2_cherryend
                    
                "Break it off":
                    $ renpy.block_rollback()
                    $ fian = "worried"
                    "And, for some reason, that felt wrong."
                    if v2_kiss:
                        "Was it because Lena and I had just kissed yesterday?"
                        "Probably, yeah."
                    elif v2_ian_date:
                        "Was it because I had just had a wonderful date with Lena and I was interested in her?"
                        "Probably, yeah."
                    else:
                        "Was it because I was interested in Lena? Or because Gillian's phantom was still in the back of my mind?"
                    "In any case, I felt uncomfortable keeping up with this game."
                    i "Um... I meant I'm looking to connect with my friends, and with you. It's always cool meeting new people."
                    $ fcherry = "sad"
                    play sound "sfx/frienddown.mp3"
                    show friend_down
                    $ ian_cherry -= 3  
                    ch "Oh. I see. OK."
                    "She looked kind of disappointed. And no wonder..."
                    "We turned our attention to the other guys and kept chatting with them."
                    jump v2_jeremyend

        "Talk to Alison and Jeremy":
            $ renpy.block_rollback()
            $ perry_cherry += 1
            if ian_alison_interest > 1:
                "I decided to get Alison's attention back. I didn't want to let it slip..."
            if v2_alisonflirt > 2 and v2_bar_alison:
                "I had been working to get it and Jeremy was trying to steal it!"
            a "Long time no see, Jeremy. What's going on with your life?"
            j "Oh, not much. Going to the gym, having fun..."
            a "Really? What about work? Are you still helping your father with his business?"
            j "No, fuck that! I hated it. I'm working at a club now!"
            a "Oh, that's right. I think Ian mentioned it."
            j "You should come one night! I'll get you in for free, and you won't have to spend a cent on drinks!"
            $ falison = "smile"
            a "That sounds like a plan!"
            j "It's settled then. Let me know when you want to come."
            j "You have to dress sexy, though, or they won't let you in!"
            if v2_alison_home:
                a "And who decides that?"
                j "I do, heh heh!"
                a "Then I'd rather pay at the entrance! I don't trust your criteria."
                "Alison turned to me, pinched my cheek and smiled."
                a "I'd rather ask your advice on what I should or shouldn't wear."
                $ fian = "confident"
                $ fjeremy = "sad"
                i "The \"shouldn't\" part sounds a lot more interesting..."
                $ falison = "flirt"
                a "Ian! Where does this naughty stroke come from?"
                i "You'll need to find out yourself, ha ha."
                j "Um, yeah guys...!"
                $ fjeremy = "smile"
                j "So, I bet you don't know what happened to me the other day!"
                "Jeremy tried to bring the attention back to him, but Alison kept looking at me from the corner of her eye, and no wonder why."
                jump v2_alisonend
                
            else:
                $ falison = "flirt"
                $ fian = "worried"
                a "They won't?"
                j "I'll tell them not to. Unless I like what you're wearing, ha ha."
                a "Oh yeah? And what should I wear?"
                j "Something similar to what you're wearing tonight... But maybe change the jeans for a mini-skirt!"
                "Jeremy kept attacking Alison with his flirting, and she didn't seem bothered by it..."
                if v2_alisonflirt > 3:
                    "Where did that leave me?"
                    menu:
                        "Flirt with Alison":
                            $ renpy.block_rollback()
                            "I knew there was sexual tension between Alison and me. She had let me know."
                            "It was my turn to show her I felt the same."
                            $ fian = "confident"
                            i "If somehow you decide to listen to this maniac please let me know, I wouldn't want to miss it."
                            a "Maybe I'll ask your advice on what I should wear."
                            "She turned all her attention to me. She was interested, after all..."
                            "I kept eye contact with her and smiled."
                            if ian_lust == 0:
                                play sound "sfx/xp.mp3"
                                show lust_up
                                $ ian_lust_xp += 1
                                call screen skillsup 
                            i "Anytime. As you know, I have really good taste."
                            $ fjeremy = "sad"
                            a "I don't know about that. You'll have to show me if that's really the case."
                            i "Sounds fair. When do you want me to do it?"
                            a "Tonight looks like a good moment..."
                            j "Um, yeah guys...!"
                            $ fjeremy = "smile"
                            j "So, I bet you don't know what happened to me the other day!"
                            "Jeremy tried to bring the attention back to him, but Alison kept looking at me from the corner of her eye."
                            jump v2_alisonend
                            
                        "Stay quiet":
                            $ renpy.block_rollback()
                            $ fian = "n"
                            "I had no intention of competing with Jeremy... And if Alison wanted to flirt back with him that badly, who was I to get in the way?"
                            "I didn't like her antics. Not my style."
                            "I let Jeremy have her, since he seemed so adamant about it."
                else:
                    "In fact, she seemed to be loving it."
                    "She laughed and touched his leg as she responded. It seemed like Jeremy was gonna get what he wanted, after all..."
                "I felt like a third wheel, so I ended up diverging my attention to Cherry and Perry and chatted with them, leaving Alison and Jeremy to their mutual flirting."
            jump v2_jeremyend
                
        "Talk to Cherry and Perry":
            $ renpy.block_rollback()
            "I turned to Cherry and Perry and made conversation with them."
            "We made some small talk, enjoyable, but nothing extremely interesting."
            if perry_cherry > 1:
                "In fact, I felt like a third wheel, kinda... Perry and Cherry seemed to be clicking so well together."
                ch "I'm gonna get another drink. Do you want to come with me, Perry?"
                p "Sure. We'll b--{w=0.5}be right back, dude."
                hide perry
                hide cherry
                with short
                show ian at rig5
                with move
                $ fian = "sad"
                "They got up and left, leaving me alone."
                $ falison = "flirt"
                $ fjeremy = "flirt"
                "Alison and Jeremy were immersed in a conversation of their own, flirting hard with each other."
                "There was no way I could jump into it."
                "I saw her laughing and touching Jeremy's leg. It seemed like he was gonna get what he wanted, after all..."
                "I felt out of place..."
            elif v2_alison_home:
                "Alison demanded my attention and I was dragged into her conversation with Jeremy."
                "I should pay attention to Alison. We had just kissed, after all..."
                a "Jeremy was telling me he can let us in for free at the club he's working at!"
                j "You won't spend a cent on drinks, either! But you have to dress sexy, though, or they won't let you in!"
                a "And who decides that?"
                $ fjeremy = "flirt"
                j "I do, heh heh!"
                a "Then I'd rather pay at the entrance! I don't trust your criteria."
                "Alison turned to me, pinched my cheek and smiled."
                a "I'd rather ask your advice on what I should or shouldn't wear."
                $ fian = "confident"
                $ fjeremy = "sad"
                i "The \"shouldn't\" part sounds a lot more interesting..."
                $ falison = "flirt"
                a "Ian! Where does this naughty stroke come from?"
                i "You'll need to find out yourself, ha ha."
                j "Um, yeah guys...!"
                $ fjeremy = "smile"
                j "So, I bet you don't know what happened to me the other day!"
                "Jeremy tried to bring the attention back to him, but Alison kept looking at me from the corner of her eye, and no wonder why."
                jump v2_alisonend
            else:
                $ falison = "flirt"
                $ fjeremy = "flirt"
                "Next to us, Alison and Jeremy were immersed in a conversation of their own, flirting hard with each other."
                "I saw her laughing and touching Jeremy's leg. It seemed like he was gonna get what he wanted, after all..."
                if v2_alisonflirt > 3:
                    "Maybe I should jump into their conversation..."
                    menu:
                        "Flirt with Alison":
                            $ renpy.block_rollback()
                            "I knew there was sexual tension between Alison and me. She had let me know."
                            "I didn't want to let that slip."
                            $ fian = "confident"
                            i "What are you guys talking about?"
                            a "Jeremy was telling me he can let us in for free at the club he's working at!"
                            j "You won't spend a cent on drinks, either! But you have to dress sexy, though, or they won't let you in!"
                            a "And who decides that?"
                            $ fjeremy = "flirt"
                            j "I do, heh heh!"
                            a "Then I'd rather pay at the entrance! I don't trust your criteria."
                            i "You shouldn't trust the advice of this depraved guy over there, ha ha!"
                            a "Maybe I'll ask your advice on what I should wear, Ian."
                            "She turned all her attention to me. She was interested, after all..."
                            "I kept eye contact with her and smiled."
                            if ian_lust == 0:
                                play sound "sfx/xp.mp3"
                                show lust_up
                                $ ian_lust_xp += 1
                                call screen skillsup 
                            i "Anytime. As you know, I have really good taste."
                            $ fjeremy = "sad"
                            a "I don't know about that. You'll have to show me if that's really the case."
                            i "Sounds fair. When do you want me to do it?"
                            a "Tonight looks like a good moment..."
                            j "Um, yeah guys...!"
                            $ fjeremy = "smile"
                            j "So, I bet you don't know what happened to me the other day!"
                            "Jeremy tried to bring the attention back to him, but Alison kept looking at me from the corner of her eye."
                            jump v2_alisonend
                            
                        "Stay quiet":
                            $ renpy.block_rollback()
                            $ fian = "n"
                            "I had no intention of competing with Jeremy... And if Alison wanted to flirt back with him that badly, who was I to get in the way?"
                            "I didn't like her antics. Not my style."
                            "I let Jeremy have her, since he seemed so adamant about it."
    
            jump v2_jeremyend

## BAR END JEREMY+ ALISON ##############################################################################################################################################################################################     

label v2_jeremyend:  
    
    "We had a few more drinks as the night kept going."
    scene cocktailbar
    show v2_alison1b
    with short
    "Jeremy and Alison also were clearly hitting it off. They weren't even trying to hide it."
    "Jeremy was all over her, and she seemed to be loving it."
    "At this point it was clear it was a done deal... Jeremy had succeeded again."
    "Finally, we decided to call it a night."
    $ falison = "flirt"
    $ fjeremy = "flirt"
    $ fian = "sad"
    if perry_cherry > 1:
        $ fperry = "happy"
    elif v2_bar_alison:
        $ fperry = "mad"
    else:
        $ fperry = "n"
    scene cocktailbar
    show cherry at truecenter
    show perry at right5
    show ian at rig5
    show jeremy at left5
    show alison at lef5
    with short
    ch "Guys, I'm gonna head home."
    i "Yeah, me and Perry too."
    a "We'll stay a bit longer."
    j "Yeah."
    i "Alright... Have fun."
    stop music fadeout 2.0
    scene street2night
    show ian at lef
    show perry at rig
    with long
    "After saying goodbye to Cherry, Perry and I walked back home."
    if perry_cherry > 1:
        p "T--{w=0.5}tonight was so fun! I really liked meeting Cherry. She's a great g--{w=0.5}gal."
        i "You two got along really well it seems."
        p "Yeah! She even gave me her n--{w=0.5}number. She said we should check out the Fortress sometime."
        i "Nice, good going man."
        play sound "sfx/friendup.mp3"
        show friend_up
        $ ian_perry += 1   
        "Perry looked really happy, and no wonder why. I was astounded seeing how well he and Cherry had hit it off..."
        "I wasn't expecting something like that, that was for sure..."
        "And Jeremy had managed to seduce Alison. It seems he was right about her: she was quite receptive after her breakup."
    elif v2_bar_alison:
        p "Dude, t--{w=0.5}tonight sucked. I told you not to leave me alone with Cherry!"
        i "I'm not your babysitter, dude. You're old enough to fend for yourself."
        p "You know it's n--{w=0.5}not so easy for me!"
        i "Get over it already."
        play sound "sfx/frienddown.mp3"
        show friend_down
        $ ian_perry -= 2  
        p "Such a friend you are."
        "I was not in a good mood. Seeing Alison and Jeremy flirting like that was bothering me."
        if ian_alison_interest == 2:
            "Even though I had told Jeremy I thought she was hot..."
        else:
            "I saw Alison just as a friend, or so I had said, but..."
        if v2_alisonflirt > 1:
            "I felt there was some kind of sexual tension between her and me."
            "But at the end of the day we were nothing more than friends... I shouldn't expect anything more from her. I didn't want to."
            "She could do whatever she wanted with whoever she wanted."
        else:
            "I shook my head. There was no logical reason for me to be bothered by it."
            "Alison and I were nothing more than friends. She could do whatever she wanted with whoever she wanted."
        "If she fancied Jeremy good for her... I shouldn't care."
        "It seems he was right about her: she was quite receptive after her breakup."
    else:
        p "It was a p--{w=0.5}pretty good night after all. I didn't like the place, but Cherry was pretty nice."
        i "Yeah, she was."
        p "Though Jeremy and Alison's behavior was b--{w=0.5}bothering me. They should've chilled down a bit."
        p "If they wanted to be all over each other like that they c--{w=0.5}could've left, or meet each other alone to b--{w=0.5}begin with."
        i "Yeah..."
        "Seeing Alison and Jeremy flirting like that had bothered me a bit, too."
        if ian_alison_interest == 2:
            "I had told Jeremy I thought she was hot, even though that didn't really mean anything..."
        elif ian_alison_interest == 1:
            "I saw Alison just as a friend, or so I had said, but..."
        else:
            "It's not like I had any interest in Alison, though."
        if v2_alisonflirt > 1:
            "I felt there was some kind of sexual tension between her and me."
            "But at the end of the day we were nothing more than friends... I shouldn't expect anything more from her. I didn't want to."
            "She could do whatever she wanted with whoever she wanted."
        else:
            "I shook my head. There was no logical reason for me to be bothered by it."
            "Alison and I were nothing more than friends. She could do whatever she wanted with whoever she wanted."
        "If she fancied Jeremy good for her... I shouldn't care."
        "It seems he was right about her: she was quite receptive after her breakup."
    "I wondered how the night would end for them... Though it wasn't hard to imagine."
    jump master_script
    

## CHERRY SEX SCENE ##############################################################################################################################################################################################     

label v2_cherryend:
     
    scene cocktailbar
    with long
    "We got another round of shots and kept drinking and chatting."
    "All in all, it was a very enjoyable night, and I had a blast with Cherry..."
    scene cocktailbar
    show v2_alison1b
    with short
    "Jeremy and Alison also seemed to be hitting it off. They weren't even trying to hide it."
    "Jeremy was all over her, and she seemed to be loving it."
    "At this point it was clear it was a done deal... Jeremy had succeeded again."
    "But I didn't want to concern myself with that. Cherry had had all my attention from the moment she stepped into this bar..."
    "After a while Perry had gotten extremely drunk. He was wobbly and somnolent."
    "It was time for him to go home, but he was in no condition to do it on his own."
    stop music fadeout 2.0
    $ fcherry = "sad"
    $ fperry = "sad"
    $ fian = "serious"
    scene streetnight
    show perry at rig3
    show ian
    show cherry at lef3
    with long
    "We decided to call it a night and left Alison and Jeremy at the bar. They wanted to continue the party on their own..."
    "Perry had to lean on me to walk straight as we left."
    p "Ugh..."
    i "For the love of God, if you're gonna puke at least give me the heads up first." 
    ch "Too many tequila shots..."
    i "He gulped them down like they were beer and there's a serious difference."
    ch "Well, a night's a night... Do you live nearby?"
    i "Yeah, close enough."
    $ fcherry = "smile"
    ch "Let me help you take him home."
    $ fian = "smile"
    i "Oh. OK."
    
    play sound "sfx/door_home.mp3"
    scene ianhomenight_dark
    with long
    "We arrived after a fifteen minute walk."
    $ fcherry = "n"
    $ fian = "n"
    show perry
    show ian at lef3
    show cherry at rig3
    with short
    i "Wait here, I'm gonna drop this doofus on his bed."
    ch "Sure."
    play sound "sfx/door.mp3"
    hide cherry
    with short
    "I helped Perry get into his room and and got a bottle of water for him."
    p "Uhhh..."
    i "Man, you're gonna be hangover as fuck tomorrow..."
    hide perry
    with short
    show ian at lef 
    with move
    "I left Perry laying in bed and went back to the living room."
    "I wasn't expecting it at all, but Cherry had ended up in my flat. I was unsure of what to do in this situation..."
    $ fian = "surprise"
    show v2_cherry1
    with long
    play music "music/sensual.mp3" loop
    ch "Hey."
    "Luckily, the choice was made for me."
    ch "So... Are you gonna take what you've been trying to get all night?"
    $ fian = "shy"
    "Holy shit."
    "I could barely believe what I saw before my eyes. Had I drunk too much, passed out and was now dreaming?"
    "No, this was the real deal."
    if ian_charisma > 1:
        "And I wasn't going to let it slip."
        $ fian = "confident"
        i "Of course I'm gonna take it."
        "I walked towards Cherry with confidence and pulled her to me."
    else:
        "I had no idea how I had managed this, but that was not the moment to think about it."
        i "Yeah, of course..."
        "I took a few steps towards Cherry and she closed the final distance that separated us."
    scene ianhomenight_dark
    show v2_cherry2
    with long
    "We embraced as our lips met."
    "She welcomed me with a deep kiss and our tongues immediately met."
    "I had never been kissed by lips like Cherry's. They felt so fleshy, enveloping mine with every kiss..."
    "The taste of her saliva and the faint smell of tequila mixed in my mouth as we continued to make out, exchanging kisses and caresses."
    "My hands ran down her naked back, feeling her warm skin under my fingers."
    "I could feel her hard and pointy nipples rubbing against my chest as her torso swaggered between my arms. "
    "She clearly communicated her passion..."
    "I raised my arms to get myself out of the hoodie, and Cherry took that chance and went for my pants."
    scene ianhomenight_dark
    show v2_cherry3
    with long
    play sound "sfx/bj1.mp3"
    "She got on her knees while unzipping them. Soon, my cock appeared in front of Cherry's face, completely erect."
    "As if it could be any other way. She had made me so fucking horny."
    "And she was fired up, too. Without any sign of hesitation, she slid her tongue up my shaft while looking at me with a smile."
    "She then wrapped her fleshy lips around the tip of my dick and began sucking gently."
    "I could've jizzed that very moment, both from the pleasure and the hype, but I managed to hold back."
    "I looked at Cherry with renewed disbelief. How the hell was I so lucky?"
    "I had just met a super attractive girl and all of a sudden I was having a one night-stand with her."
    "This was the last thing I imagined would happen tonight before leaving for the bar."
    play sound "sfx/bj1.mp3"
    i "Ohh...!"
    "Cherry quickly brought my attention back to the moment, sucking eagerly on my cock."
    "She slid her lips up and down the shaft, masturbating me with her mouth."
    "She continued to please me while I stood there, in the middle of the living room. If Perry just walked out of his room..."
    "Though I doubted he was able to."
    "Cherry continued with her blowjob for a bit longer as we gradually shed all our clothes."
    scene ianhomenight_dark
    $ fian = "shy"
    $ fcherry = "flirt"
    show cherrynude at rig
    show iannude at lef
    with long
    "When we were completely naked, she finally decided to stand up and grabbed my hand."
    ch "Show me to your room."
    i "Of course."
    play sound "sfx/door.mp3"
    scene ianroomnight
    show cherrynude at rig
    show iannude at lef
    with short
    "I watched Cherry get in after me and closed the door."
    "My eyes were glued to her slender and tight figure, and the way she moved..."
    "Even the way she walked had something sexy and arousing to it."
    ch "So... You wanna fuck me?"
    $ fian = "confident"
    i "Do I have to answer that?"
    "She chuckled."
    ch "No, I guess you don't. Do you have a condom?"
    $ fian = "worried"
    i "Oh, yeah. I should have a few around here..."
    "I quickly searched in the drawer where I always stored the rubbers."
    "They were there, but hidden under a pile of shirts. It had been long since I used one."
    "A whole year ago, with Gillian, before knowing she was cheating on me..."
    "{i}Fuck, why the hell do these thoughts come to mind now? It's not the moment!{/i}"
    "I opened one of the condoms and tried to put it on."
    "Would I even remember how to fuck properly after a whole year? Would I be able to satisfy Cherry?"
    "I felt my erection start to go away."
    i "Fuck..."
    $ fcherry = "n"
    ch "Is everything alright?"
    "Her asking that only made me feel more pressure!"
    "{i}Oh come on, don't be one of these guys, Ian, please!{/i}"
    menu:
        "{image=icon_lust.png}Look at Cherry" if ian_lust > 1:
            $ renpy.block_rollback()
            "I took a good look at Cherry."
            "Standing before me, completely naked, her amazing and tight body waiting for me to enjoy it..."
            "She was so hot, dammit. And I wanted to experience her. Her lips, her skin, her sex..."
            "I felt the blood rushing back to my cock."
            $ fian = "confident"
            i "Nice."
            ch "What?"
            i "Let's go to bed. I want you to make me even hornier."
            $ fcherry = "flirt"
            ch "Oh, I see. So that's what you want?"
            
        "{image=icon_wits.png}+{image=icon_charisma.png}Don't stress out" if ian_wits > 0 and ian_charisma > 1:
            $ renpy.block_rollback()
            "I took a deep breath and finished putting the rubber on."
            "Stressing about it would not solve the problem, but do exactly the opposite. I had to relax and take it easy."
            $ fian = "smile"
            i "It's nothing. The moment of putting the rubber on always kills the mood a bit, but I'll be fired up in no time."
            i "Let's go to bed."
            $ fcherry = "flirt"
            ch "I see. I can help you with that."
            
        "I can't":
            $ renpy.block_rollback()
            $ v2_ian_limp = True
            i "It's... I..."
            stop music fadeout 2.0
            hide iannude
            show iannude2 at lef
            with short
            $ fcherry = "sad"
            "Cherry saw what the problem was."
            ch "Oh."
            $ fian = "disgusted"
            i "Shit, I don't know why this is happening. It never happened to me before, I swear."
            i "I mean, not like this... Maybe it's... I've probably drunk too much tonight..."
            ch "It's alright... I know these things can happen sometimes..."
            i "Shit I'm sorry, I...!"
            $ fcherry = "n"
            ch "Don't worry about it. The pressure can get to you in these situations. It's all been quite sudden and unexpected."
            "Fuck! Why? Why me? Everything was going so smoothly... And I had to ruin it, as always!"
            $ fian = "depress"
            "I felt so fucking awkward and ashamed."
            i "Please, don't take it personally, it's not that I don't find you attractive or..."
            ch "I said I understand. You don't have to justify yourself to me. Don't worry about it."
            ch "I guess I'll... Just pick up my things and get going, is that alright?"
            i "Sure..."
            "I didn't know what else to say. All I could think about were excuses, and she didn't want to hear more of those."
            hide cherrynude
            hide iannude
            $ ian_look = 3
            show ianunder at lef
            with short
            "It was the most tense and awkward moment in recent memory."
            "When Cherry left I didn't know how to even look at her."
            "How the hell had I messed up something like that? I had to know, it was too good to be true."
            "I went to bed kicking myself in the teeth. The only thing I felt I was good at."
            jump master_script

    $ ian_cherry_sex = True
    scene ianroomnight
    show v2_cherry4_animation
    with long
    "Cherry made me lie down and climbed on top of me."
    call screen willup
    "To my surprise she turned around, lowered her hips and began swaying them sensually."
    "It was like she was giving me a lap dance..."
    "My dick was being rubbed by her perfect, tight little ass as I watched Cherry's body move in the dark."
    "Her eyes were the brightest thing in the room, shimmering as she looked back at me with a flirty smile."
    play sound "sfx/xp.mp3"
    show lust_up
    $ ian_lust_xp += 1
    call screen skillsup   
    "There was no way my dong wouldn't get hard as a rock with a sight like that. I was ready."
    show v2_cherry4c
    with short
    play sound "sfx/mh1.mp3"
    ch "Annhh..."
    "Cherry moaned lightly when she felt the tip of my dick pressing against her slit."
    "I used my hand to position it firmly, and Cherry began lowering her hips..."
    ch "Mhhh... You're so hard now..."
    i "How could I not be? You're so damn sexy."
    scene v2_cherry4b_animation
    show v2_cherry4c
    with short
    play sound "sfx/oh1.mp3"
    ch "Ohhhn...!"
    "My cock finally penetrated Cherry's sex. I felt the heat of her insides through the latex wall..."
    "I held her butt cheeks and guided her up and down movements, slowly and rhythmically."
    "It was the tightest ass I had ever had the pleasure to put my hands on..."
    ch "Oh yeah... Nice and slow..."
    play sound "sfx/ah1.mp3"
    ch "So good... Ahhh..."
    "We stayed in that position for a while, my cock going in and out of Cherry's hot pussy, her ass bouncing up and down, a bit faster and harder each time..."
    "This was really happening... I felt adrenaline rushing through my veins."
    i "Face me, Cherry. I want you!"
    scene ianroomnight
    show v2_cherry5_animation
    with short
    ch "Oh!"
    "I turned her around and I got on top this time. She was surprisingly light."
    "I spread her legs and dove right into them. I felt her tight pussy giving way to my cock as I pushed it in."
    ch "Ohh, Ian, yes...!"
    "She clasped her hands around my arms as I began moving my hips back and forth, penetrating her at a lively pace."
    "I kissed her on the mouth, on the neck, on her collarbone..."
    play sound "sfx/oh1.mp3"
    ch "Yes! Ohhhmm!"
    "I slid my lips and tongue across her skin, wanting to get high on her taste and smell."
    "I was so excited, and it felt so good... Yet, for some reason, I felt this wouldn't be enough for me to cum..."
    "But never mind that. I had to show Cherry a good time. I didn't want to look bad!"
    "Cherry moved her hips in synch with mine, but letting me know she wanted me to go harder and faster."
    show v2_cherry5_animation2
    with short
    "I followed the lead she was setting, increasing it more and more..."
    if ian_athletics > 1:
        "I gave it my all, taking my body to its cardiovascular limit. But she was loving it, so I had to keep going!"
        ch "Ah, yes, keep going! Yes, Ian, yes...!"
        "Was she going to cum!? I kept pumping into her, determined to make her achieve orgasm."
        ch "Yes, I'm almost..."
    else:
        "I was at my limit, but not because I was about to cum. I was about to collapse from exhaustion!"
        "I was at the brink of giving up, but I didn't want to. Cherry seemed to be loving it."
        ch "Ah, yes, keep going! Yes, Ian, yes...!"
        play sound "sfx/xp.mp3"
        show athletics_up
        $ ian_athletics_xp += 1
        call screen skillsup   
        "Was she going to cum? I couldn't stop now!"
        "{i}Cum, please cum already!{/i}"
        "Thankfully, my physical condition held on just enough."
    play sound "sfx/orgasm1.mp3"
    show v2_cherry5b
    with vpunch
    ch "Ahhhh!! Cumming!"
    "Cherry moaned as her grip on my body tightened. I felt her hips and legs trembling... What a wonderful feeling!"
    i "*{i}Gasp{/i}*..."
    "I collapsed next to Cherry, exhausted after having performed to the limit of my abilities, panting and sweating."
    stop music fadeout 2.0
    scene ianroomnight
    $ fcherry = "flirt"
    $ fian = "smile"
    show cherrynude at rig
    show iannude2 at lef
    with short
    ch "Wow... That was really good..."
    i "Yeah? You seemed to enjoy it."
    ch "Believe me, I did. I was in need of that..."
    $ fcherry = "n"
    ch "But what about you? You didn't cum..."
    i "Don't worry about it. Besides, I'm completely beat!"
    ch "Are you sure? I feel it's not fair."
    i "Don't worry, for real. I'm happy to know you enjoyed it so much."
    i "Let's get some sleep."
    $ fcherry = "smile"
    ch "I'm falling asleep already... Mhh..."
    $ fian = "worried"
    "It wasn't like I didn't want to cum, but I felt I couldn't even if I wanted to."
    "Maybe it was because I was tired, or because I had drunk a bit too much that night."
    "Or maybe it was for some other reason..."
    $ gallery_scene9 = True
    jump master_script

## ALISON SEX SCENE ##############################################################################################################################################################################################     

label v2_alisonend:
    
    ch "Hey guys, I'm gonna call it a night."
    p "Yeah, me too."
    a "Oh, really? I'm gonna stay a bit more, if that OK with you."
    ch "Of course! I see you're having fun."
    p "Are you staying, too, Ian?"
    i "Yeah, I'm gonna stay a bit longer."
    p "OK. See you tomorrow then."
    hide cherry
    hide perry
    hide perry2
    with short
    show ian at rig3
    show alison at truecenter
    show jeremy at lef3
    with move
    j "They're leaving early."
    i "You just came very late."
    "We had one final drink as we chatted and had a good time."
    "I felt Alison was more comfortable with me than with Jeremy..."
    if v2_alison_home:
        "And the reason was clear. That kiss we shared... I couldn't wait to kiss her again."
        "And by the way she leaned into my side I felt she wanted that, too."
    
    stop music fadeout 2.0
    scene streetnight
    with long
    "We finally decided to call it a night."
    $ fian = "smile"
    $ falison = "n"
    $ fjeremy = "n"
    $ jeremy_look = 3
    show ian at lef3
    show alison
    show jeremy at rig3
    with short
    a "Tonight was so fun. I needed this. Thanks for coming, guys."
    j "Thank you for inviting us. How are you going back home?"
    a "I think I'll walk."
    j "Do you want me to accompany you on your way home?"
    a "No, thanks. Besides, I'm going in the same direction as Ian. You have to go in the opposite direction, right?"
    j "Oh. Yeah..."
    i "See you at the gym, Jeremy!"
    $ fjeremy = "smile"
    j "Sure. It's been nice seeing you, Alison!"
    a "Good night."
    hide jeremy
    with short
    show alison at rig
    show ian at lef
    with move
    if v2_alison_home:
        $ falison = "flirt"
        a "Finally, alone again..."
        scene streetnight
        show v2_alison2b
        with long
        "As soon as Jeremy disappeared Alison kissed me again."
        "Should I feel weird about this happening? I had known Alison for the longest time, always treating her like a friend..."
        "But some kind of sexual tension had always been lurking in the shadows of our friendship."
        "Maybe it was because the alcohol in my system, but it just felt natural to let our desire finally free."
        "We both had been wanting this during the whole night. We might've been wanting it for much longer than that, actually..."
        $ fian = "shy"
        scene streetnight
        show alison at rig
        show ian at lef
        with short
        a "So... It's still kinda early. Are you gonna invite me to have one last drink at your place?"
        "It wasn't early. But we would be a lot more comfortable making out at my place instead than on the street."
        "More comfortable, and also..."
        i "Sure. Let's go."
    else:
        i "Are you sure you want to walk with me? You live quite a bit farther away than me."
        a "Yeah, it's OK. I don't mind."
        "If she really intended to go back to her place on foot she would be walking a long stretch tonight..."
        scene street2night
        with long
        "We stopped in front of my building after a fifteen minute walk."
        show alison at rig
        show ian at lef
        with short
        i "Here we are."
        a "So this is where you live with Perry? You know, I've never been to your place since you moved."
        i "That's true... Do you want to check it out?"
        $ falison = "flirt"
        a "Sure..."
        "I asked her without really thinking about it. Was this really the proper moment?"
        "Or maybe I was just trying not to think too much about what was about to happen."
        "What had been happening during the whole night, slowly leading to where we were now..."
    
    play sound "sfx/door_home.mp3"
    scene ianhomenight_dark
    with long
    $ fian = "smile"
    $ falison = "smile"
    show alison at rig
    show ian at lef
    with short
    i "Let's try to be quiet. Perry must be sleeping, let's not wake him up."
    a "Oh, so this is your new place... Not as bad as I was expecting."
    i "What were you expecting?"
    a "I don't know... A total mess? Ha ha."
    if v2_alison_home:
        i "I hope you have a better opinion about my room, ha ha."
        $ falison = "flirt"
        a "Let's check it out."
        play sound "sfx/door.mp3"
        scene ianroomnight
        show alison at rig
        show ian at lef
        with short
        a "It's similar to your old room. I see you're still a geek, ha ha."
        i "Some things never change. Others do, though..."
        play music "music/sensual.mp3"
        scene ianroomnight
        show v2_alison2
        with long
        "I grabbed Alison by the hips, turned her around and kissed her."
        "Her lips curved into a smile at the same time as she responded to my kiss with one of hers."
    else:
        $ v2_alison_home = True
        i "So, what do you want to drink?"
        a "At this point I'll have a glass of water. Keeping up with the alcohol wouldn't be wise!"
        i "Alright. Wait for me in my room, I'll bring it to you."
        hide alison 
        with short
        "I went to the kitchen and drank a glass of water myself. I wanted my head clear."
        "Alison was waiting in my room..."
        "I filled another glass with water and brought it to her."
        play sound "sfx/door.mp3"
        scene ianroomnight
        show alison at rig
        show ian at lef
        with short
        "I found Alison checking out the stuff on my shelves."
        a "I see you're still a geek... Some things never change!"
        menu:
            "Here's your water":
                $ renpy.block_rollback()
                i "Here's you water."
                a "Thanks."
                "I watched her empty the glass in one go. What should I do now?"
                "How had we ended up in my room at three in the morning?"
                a "So... tonight was fun, don't you think so?"
                i "Absolutely... We should do this again."
                $ falison = "flirt"
                a "Definitely. Though I was hoping something else happened tonight..."
                $ fian = "blush"
                i "Oh..."
                "I could feel it coming. There was no reason to keep playing the fool and denying it."
                "Alison and I, we..."
                play music "music/sensual.mp3"
                scene ianroomnight
                show v2_alison2
                with long
                "She got closer to me and kissed me."
                "I closed my eyes, rested my hand on her hips and kissed her back..."
                
            "You didn't come just for a glass of water":
                $ renpy.block_rollback()
                "I gave her the glass of water."
                $ fian = "confident"
                i "You didn't come here just for a glass of water, right?"
                $ falison = "blush"
                play sound "sfx/xp.mp3"
                show charisma_up
                $ ian_charisma_xp += 1
                call screen skillsup   
                "Alison almost choked while she was drinking."
                a "*{i}Cough{/i}*..."
                $ falison = "n"
                a "I guess not."
                "The cards were on the table. No reason to keep doubting myself."                
                play music "music/sensual.mp3"
                scene ianroomnight
                show v2_alison2
                with long
                "I grabbed Alison by the hips, pulled her towards me and kissed her."
                "Her lips curved into a smile at the same time as she responded to my kiss with one of hers."
                
            "Kiss her":
                $ renpy.block_rollback()
                "I gave her the glass of water, and while she finished drinking it I decided it was time for action."
                play music "music/sensual.mp3"
                scene ianroomnight
                show v2_alison2
                with long
                "I grabbed Alison by the hips, pulled her towards me and kissed her."
                play sound "sfx/xp.mp3"
                show lust_up
                $ ian_lust_xp += 1
                call screen skillsup   
                "Her lips curved into a smile at the same time as she responded to my kiss with one of hers."
                
        "There was no reason to keep dragging things out. We both had been wanting this during the whole night."
        "We might've been wanting it for much longer than that, actually..."
                
    "Alison's tongue searched for mine, sliding and rubbing against it in a wet, hot, yet tender caress."
    "As our lips fused, so tried our bodies as we embraced, our torsos pressing against each other."
    scene ianroomnight
    show v2_alison3
    with long
    "She was the first to sneak her hands under my clothes. They were a bit cold, and searched the heat of my torso."
    "I had heat to spare... My cock was already begging to be set free, hard as a rock and constrained by my pants."
    "Luckily it hadn't to wait long for that to happen. Alison and I stripped each other's clothes away as we continued to kiss."
    "I felt her soft and voluptuous bosom on my chest, her warmth, her accelerating heartbeat..."
    "My hands caressed her boobs, exploring them. I had always wondered how they would feel to the touch, and I was finally getting to know it."
    "Alison's breathing became heavier as our kisses deepened and my hands got more daring, caressing all of her body."
    "She responded in kind. Her hand reached down to my cock and her fingers wrapped around the shaft."
    "I shivered."
    i "Nhh..."
    a "Oh, you're so hard, Ian..."
    i "Guess whose fault it is..."
    a "I'll take responsibility... Do you have a condom?"
    "It was really going to happen. I was about to have sex with Alison."
    $ fian = "worried"
    $ falison = "flirt"
    scene ianroomnight
    show iannude at lef
    show alisonnude at rig
    with long
    i "I should have a few around here..."
    "I quickly searched in the drawer where I always stored the rubbers."
    "They were there, but hidden under a pile of shirts. It had been long since I used one."
    "A whole year ago, with Gillian, before knowing she was cheating on me..."
    "{i}Fuck, why the hell do these thoughts come to mind now? It's not the moment!{/i}"
    "I opened one of the condoms and tried to put it on."
    "Would I even remember how to fuck properly after a whole year? Would I be able to satisfy Alison?"
    "We had been friends for a long time. What would she think about me if I failed to perform? Things would get really werid..."
    "I felt my erection start to go away."
    i "Fuck..."
    $ falison = "sad"
    a "Is everything alright?"
    "Her asking that only made me feel more pressure!"
    "{i}Oh come on, don't be one of these guys Ian, please!{/i}"
    menu:
        "{image=icon_lust.png}Look at Alison" if ian_lust > 1:
            $ renpy.block_rollback()
            "I took a good look at Alison."
            "Standing before me, completely naked, her amazing and voluptuous body waiting for me to enjoy it..."
            "She was so hot, dammit. And I wanted to experience her. Her lips, her skin, her sex..."
            "I felt the blood rushing back to my cock."
            $ fian = "confident"
            i "Nice."
            a "What?"
            i "Let's go to bed. I want you."
            $ falison = "flirt"
            a "Oh, Ian..."
            
        "{image=icon_wits.png}+{image=icon_charisma.png}Don't stress out" if ian_wits > 0 and ian_charisma > 1:
            $ renpy.block_rollback()
            "I took a deep breath and finished putting the rubber on."
            "Stressing about it would not solve the problem, but do exactly the opposite. I had to relax and take it easy."
            $ fian = "smile"
            i "It's nothing. The moment of putting the rubber on always kills the mood a bit, but I know just how to get fired up again in no time."
            i "Let's go to bed."
            $ falison = "n"
            a "Alright."
            
        "I can't":
            $ renpy.block_rollback()
            $ v2_ian_limp = True
            i "It's... I..."
            stop music fadeout 2.0
            hide iannude
            show iannude2 at lef
            with short
            "Alison saw what the problem was."
            a "Oh."
            $ fian = "disgusted"
            i "Shit, I don't know why this is happening. It never happened to me before, I swear."
            i "I mean, not like this... Maybe it's... I've probably drunk too much tonight..."
            a "Don't worry... It's not like this is new to me..."
            i "What? No, no, don't take it personally...! It's not that I don't find you attractive or..."
            a "Then what's the reason?"
            "Fuck! Why? Why me? Everything was going so smoothly... And I had to ruin it, as always!"
            $ fian = "depress"
            i "It's me, OK? The pressure just got to me."
            a "The pressure? What pressure? It's just me, Alison."
            i "To me you're much more than \"just Alison\"."
            a "What's that supposed to mean?"
            i "Well, you're... You're an incredibly attractive woman, and I got so nervous."
            $ falison = "n"
            a "Oh, is that so?"
            i "Yeah... And it's been so long since... you know... I guess I'm freaking out a bit."
            a "I see... I guess these things can happen..."
            i "I'm sorry."
            "I felt so awkward and ashamed."
            a "Some other time, then?"
            i "Yeah... Some other time."
            a "OK... I guess I'll get going then..."    
            hide alisonnude
            hide iannude
            $ ian_look = 3
            show ianunder at lef
            with short
            "Alison picked up her clothes, got dressed and left."
            "That was one of the most tense and awkward moments in recent memory."
            "When Alison left I didn't know how to even look at her. Even though she acted less awkward than I expected..."
            "But how the hell had I messed up something like that?"
            "I should've let Jeremy take her... She wouldn't have gone home disappointed, at least."
            "I went to bed kicking myself in the teeth. The only thing I felt I was good at."
            jump master_script
    
    $ ian_alison_sex = True
    scene ianroomnight
    show v2_alison4
    with long
    "I made Alison sit down on my bed as I continued to make out with her."
    call screen willup
    "Slowly, I ran my hand down her chest and her abdomen, reaching down between her legs..."
    play sound "sfx/mh1.mp3"
    a "Mhh... Oh..."
    "I slid the tip of my fingers very lightly over Alison's sex, making her shiver a bit."
    "I did it again, this time more vehemently."
    "I began caressing her pussy, digging deeper into her labia with each stroke."
    "Soon my fingers were moist with Alison's juices... Feeling how wet and horny she was made me touch her with even more determination."
    "I found the outline of her clit and began rubbing it, making small circles. Her breathing became heavier and seething."
    play sound "sfx/ah1.mp3"
    "She looked at me with a smile that was horny and shy at the same time."
    a "Ahh... Ian..."
    a "I can't believe we're doing this..."
    i "You seem to be enjoying it."
    a "Mhhh, yeah..."
    "She took a look at my cock. It was hard as an iron rod again, and had been rubbing against Alison's leg for a while."
    a "Oh, look at you! Seems you're completely ready to go now... Come here."
    scene ianroomnight
    show v2_alison5_animation
    with long
    "This time she took the lead and pushed me aside, getting on top of me."
    "I was so horny at this point there was no room for insecure thoughts anymore. All I wanted was to be inside of Alison."
    "And she granted me that wish. She grabbed my cock, positioned it between her legs and lowered her hips."
    play sound "sfx/ah2.mp3"
    "I was inside her...!"
    "I felt the heat of her insides through the latex wall..."
    "Alison swayed her hips back and forth without haste, like she was delighting herself in the moment."
    "I for sure was..."
    a "Oh God, it's finally happening... We're having sex... Nhh..."
    "I held her hips with my hands and drove her body down at the same time as I pushed my pelvis up."
    play sound "sfx/oh1.mp3"
    "Alison moaned when my cock got even deeper, rubbing the inner walls of her sex."
    i "I'm so glad it's happening."
    a "Me, too... Fuck me, Ian!"
    "I couldn't resist her asking me like that."
    scene ianroomnight
    show v2_alison6_animation
    with long
    "I sat up, pushed Alison down and changed position."
    "She was much taller than Gillian, not so easy to maneuver around her body in bed, but I managed it."
    "I pulled her legs up and dove right between them. I felt her slippery pussy giving way to my cock as I pushed it in."
    play sound "sfx/ah1.mp3"
    a "Ian! Oh, yes...!"
    play sound "sfx/xp.mp3"
    show lust_up
    $ ian_lust_xp += 1
    call screen skillsup   
    "She held her own legs up as I began moving my hips back and forth, penetrating her at a lively pace."
    "I kissed her on the mouth, on the neck, on her collarbone..."
    a "Oh, this angle is nice... Keep doing it... Do me, Ian!"
    "I supported all my body weight with my arms as I focused on giving Alison what she was asking for."
    "It felt so good... Yet, for some reason, I felt this wouldn't be enough for me to cum..."
    "But never mind that. I had to show Alison a good time. I didn't want to look bad!"
    show v2_alison6_animation2
    with long
    "I tensed my body, penetrating her with my cock in that angle she seemed to like so much, increasing my speed more and more..."
    a "Ohhh, don't stop! Yes, Ian, yes...!"
    if ian_athletics > 1:
        "I gave it my all, taking my body to its cardiovascular limit. But she was loving it, so I had to keep going!"
        "Was she going to cum!? I kept pumping into her, determined to make her achieve orgasm."
        a "Yes, I'm almost..."
    else:
        "I was at my limit, but not because I was about to cum. I was about to collapse from exhaustion!"
        "I was at the brink of giving up, but I didn't want to. Alison seemed to be loving it."
        play sound "sfx/xp.mp3"
        show athletics_up
        $ ian_athletics_xp += 1
        call screen skillsup  
        a "Yes, I'm almost..."
        "Was she going to cum? I couldn't stop now!"
        "{i}Cum, please cum already!{/i}"
        "Thankfully, my physical condition held on just enough."
    play sound "sfx/orgasm1.mp3"
    show v2_alison6
    with vpunch
    a "Ohhhh, Ian! Yeees!!"
    "Alison moaned and I felt her hips and legs trembling... What a wonderful feeling!"
    i "*{i}Gasp{/i}*..."
    "I collapsed next to her, exhausted after having performed to the limit of my abilities, panting and sweating."
    stop music fadeout 2.0
    $ fian = "smile"
    $ falison = "slut"
    scene ianroomnight
    show iannude at lef
    show alisonnude at rig
    with long
    a "Mhhh... That was so nice... I was in desperate need of it!"
    i "*{i}Whew{/i}*... I'm glad you've enjoyed it."
    $ falison = "n"
    a "What about you? You didn't get to cum yet."
    i "Don't worry about it. Besides, I'm completely beat!"
    i "I couldn't keep going even if I wanted to..."
    a "Alright. I'm dead tired, too..."
    i "Let's get some sleep."
    $ falison = "smile"
    a "Sure."
    "Alison snuggled up next to me and we fell asleep, exhausted as we were."
    $ fian = "worried"
    "It wasn't like I didn't want to cum, but I felt I couldn't even if I wanted to."
    "Maybe it was because I was tired, or because I had drunk a bit too much that night."
    "Or maybe it was for some other reason..."
    "What a crazy night..."
    $ gallery_scene8 = True
    jump master_script
 
###### SCREENS ##################

screen book_screen_1:
    
    imagebutton idle "card1_scifi.png" hover "card1_scifi_hover.png" focus_mask True action SetVariable("book_scifi", True) , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "card1_fantasy.png" hover "card1_fantasy_hover.png" focus_mask True action SetVariable("book_fantasy", True)  , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "card1_historical.png" hover "card1_historical_hover.png" focus_mask True action SetVariable("book_historical",True) , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 

screen write_song1a:
    imagebutton idle "song_1a_button1.png" hover "song_1a_button1_hover.png" focus_mask True action SetVariable("song_1a", "precise") , [ Play ("ch_one", "sfx/paper_click.mp3") ]  , Return at fade_in_skill hovered [ Play ("ch_one", "sfx/paper_hover.mp3") ]
    imagebutton idle "song_1a_button2.png" hover "song_1a_button2_hover.png" focus_mask True action SetVariable("song_1a", "real")  , [ Play ("ch_one", "sfx/paper_click.mp3") ]  , Return at fade_in_skill hovered [ Play ("ch_one", "sfx/paper_hover.mp3") ]
    imagebutton idle "song_1a_button3.png" hover "song_1a_button3_hover.png" focus_mask True action SetVariable("song_1a", "cool") , [ Play ("ch_one", "sfx/paper_click.mp3") ]  , Return at fade_in_skill hovered [ Play ("ch_one", "sfx/paper_hover.mp3") ]
    
screen write_song1b:
    imagebutton idle "song_1b_button1.png" hover "song_1b_button1_hover.png" focus_mask True action SetVariable("song_1b", "tragedy") , [ Play ("ch_one", "sfx/paper_click.mp3") ]  , Return at fade_in_skill hovered [ Play ("ch_one", "sfx/paper_hover.mp3") ]
    imagebutton idle "song_1b_button2.png" hover "song_1b_button2_hover.png" focus_mask True action SetVariable("song_1b", "stuff")  , [ Play ("ch_one", "sfx/paper_click.mp3") ]  , Return at fade_in_skill hovered [ Play ("ch_one", "sfx/paper_hover.mp3") ]
    imagebutton idle "song_1b_button3.png" hover "song_1b_button3_hover.png" focus_mask True action SetVariable("song_1b", "story") , [ Play ("ch_one", "sfx/paper_click.mp3") ]  , Return at fade_in_skill hovered [ Play ("ch_one", "sfx/paper_hover.mp3") ]
    
screen write_song1c:
    imagebutton idle "song_1c_button1.png" hover "song_1c_button1_hover.png" focus_mask True action SetVariable("song_1c", "kingdom") , [ Play ("ch_one", "sfx/paper_click.mp3") ]  , Return at fade_in_skill hovered [ Play ("ch_one", "sfx/paper_hover.mp3") ]
    imagebutton idle "song_1c_button2.png" hover "song_1c_button2_hover.png" focus_mask True action SetVariable("song_1c", "cave")  , [ Play ("ch_one", "sfx/paper_click.mp3") ]  , Return at fade_in_skill hovered [ Play ("ch_one", "sfx/paper_hover.mp3") ]
    imagebutton idle "song_1c_button3.png" hover "song_1c_button3_hover.png" focus_mask True action SetVariable("song_1c", "abyss") , [ Play ("ch_one", "sfx/paper_click.mp3") ]  , Return at fade_in_skill hovered [ Play ("ch_one", "sfx/paper_hover.mp3") ]
    
            
    
    