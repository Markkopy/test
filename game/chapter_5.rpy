##################################################################################################################################################################################################################
########################################################### CHAPTER 5  PLAYING THE FIELD #################################################################################################################################################################################
##################################################################################################################################################################################################################

label chapter_five:
    
    image alison_voyeur_v5:
        "images/v5_voyeur1.png" with short
        pause 2
        "images/v5_voyeur2.png" with short
        pause 2
        "images/v5_voyeur3.png" with short
        pause 2
        "images/v5_voyeur4.png" with short
        pause 2
        repeat
    $ lena_active = False
    $ ian_active = True
    
    $ save_name = "Ian: Chapter Five"
    
    show blackbg
    with long
    call screen chapter_title  
    
## IAN THURSDAY ####################################################################################################################################################################

    $ day = "Thursday"
    show active_ian
    with long
    pause 1.0
    scene blackbg
    with long
    pause 0.5 
    call screen calendar
    scene street
    with long   
    $ fian = "n"
    $ ian_look = 1
    "I was on my way to the gym while reminiscing about the week."
    show ian with short
    if v4_ian_date:
        "In particular about yesterday and my date with Lena."
        if ian_lena_sex:
            $ fian = "happy"
            "I mean, how could I not?"
            i "I really slept with her..."
            "It was still hard to believe, but it had happened. And in the most unexpected way possible."
            "I thought the date was over, that she wanted to take it slow, and I was OK with that..."
            "But then she suddenly called, inviting me to her place. Of course I knew what that invitation really meant, but..."
            "It surprised me how eager and assertive Lena was. Sex with her had been great... Best I had in a while."
            if ian_cherry_sex:
                "I had enjoyed Cherry a lot, but this felt different..."
                if ian_alison_sex:
                    "Same with Alison. I had a lot of fun with her, but Lena..."
            elif ian_alison_sex:
                "I had enjoyed Alison a lot, but this felt different..."
            else:
                "I hadn't been having sex in a while anyways, but still..."
            "It had been amazing considering it was our first time. I felt we clicked together so well."
            "And it didn't feel awkward waking up next to her. We said goodbye with a smile on our faces, and the passion was still there."
            "It was clear it hadn't been a one-night thing, or at least that was the impression I got."
            i "I can't wait to see her again..."
        elif v4_ian_kiss:
            $ fian = "smile"
            "How could I not?"
            "We had so much fun together. We just clicked so well with each other."
            "And those kisses..."
            "There was some real passion behind them. I was pretty sure we would click so well in bed, too..."
            "But I had decided to let her set the pace. I wanted her to feel comfortable."
            "And judging by how things were playing out, it wouldn't take too long for us to sleep together..."
            i "Man, I can't wait to see her again."
        else:
            "I thought the date went well, and I felt Lena was comfortable around me."
            "But for some reason she acted weird when I tried to kiss her, like she was troubled by it."
            "That threw me off... So I decided to play it safe."
            i "Maybe I should've pushed a bit more... But I don't want to creep her out."
            i "I guess I'll need to try again next time..."

    if ian_honest_review or ian_switch_review:
        "I had the whole morning to myself, since I only worked three days a week now."
        "I felt full of energy and ready to take on the workout."
    else:
        "The morning at the magazine had been long and boring."
        "I hoped today's workout would help me unwind."
    
    scene gym
    with long
    $ fjeremy = "smile"
    $ jeremy_look = 2
    play music "music/jeremys_theme.mp3" loop
    if jiujitsu > 0:
        show ian at lef
        with short
        "I dropped my bag on the locker room and prepared for today's training session."
        if tournament:
            "I was considering entering that amateur MMA tournament Yuri and Wen had spoke about, but that meant I should get properly prepared."
        "I had been training Kick Boxing for a while now, but Wen was offering to teach me Jiu Jitsu."
        if jiujitsu > 1:
            "What I had seen so far seemed pretty cool..."
        else:
            "I wasn't sure if I liked better than punching and kicking, though..."
        "I had to decide what to focus on from now on."
        menu:
            "Stick with kickboxing":
                $ renpy.block_rollback()
                $ jiujitsu = 0
                $ fian = "smile"
                i "I'd rather stick with kick boxing. It's what I really like to train."
                i "It feels so good flowing with the strikes and being light on my feet!"
                scene gym with long
                $ ian_look = 7
                "I got changed and stepped onto the mat."
                
            "Focus on Jiu Jitsu":
                $ renpy.block_rollback()
                $ fian = "smile"
                i "I think learning Jiu Jitsu will be really interesting."
                i "I want to discover how many cool techniques there are!"
                scene gym with long
                $ ian_look = "gi"
                "I got changed and stepped onto the mat."
    else:
        $ ian_look = 7
        show ian
        with short
        "I got changed and stepped onto the mat."
        
##JIUJITSU
    if jiujitsu:
        show ian at lef
        show wen at rig
        with short
        if ian_lena_sex or v4_ian_kiss:
            wen "Hey, you look happy today."
            i "I guess I do, ha ha."
            wen "Good, let's put that energy to use."
        wen "I see you're ready for another lesson. I suppose you're going to focus your efforts in learning Jiu Jitsu?"
        i "Yeah, let's do it! What are we gonna learn today?"
        wen "You still need to practice your throws."
        $ fian = "n"
        i "Again? All we do is throw each other around..."
        wen "How are you gonna use Jiu Jitsu if you're not able to take your opponent to the ground?"
        i "I know, I know. But I would also like to know what to do once I have him on the ground!"
        wen "I guess I can teach you a basic technique..."
        wen "Let's take it from where we left it. Do you remember the sequence?"
        i "Of course..."
        scene gym
        with long
        show v3_jiu1
        with long
        i "You parry when I punch..."
        show v3_jiu2
        with short
        i "You make me lose my balance, and then..."
        show v3_jiu3
        with short
        show v3_jiu4
        with vpunch
        i "Oof!"
        wen "Alright, now that I have you where I want you..."
        wen "I make sure not to lose my hold on your arm, and..."
        show v3_jiu5
        with short
        "Wen fell on his back, my arm tightly tucked between his legs."
        i "...!"
        "I felt great pressure on my elbow, like it was about to pop!"
        "I quickly tapped to let him know my joint was in danger."
        wen "Are you feeling it?"
        i "Fuck yeah I am!"
        wen "This technique is called \"armbar\" and it's fairly easy to set up. You need good form to get away with it!"
        wen "The key is to force the joint upwards, pulling with your back and pushing up with your pelvis."
        i "OK, OK, I get it...! You can let go now!"
        scene gym
        show ian at lef
        show wensmile at rig
        with long
        "I got up and rubbed my arm."
        i "Damn, that was scary. I think I'd rather take a punch than have my arm broken like that."
        wen "That's the power of Jiu Jitsu, ha ha! Now, give it a try..."
        scene gym
        with long
        "We practiced the throw and the armbar from several positions for the next hour."
        "Wen was way stronger than he looked, and he had fun resisting my attempts to extend his arm."
        "It was quite frustrating and I burned out my arms trying to overcome his resistance."
        if ian_athletics > 2:
            $ jiujitsu += 1
            "But by the end of the training session I managed to get the basics down."
            $ fian = "smile"
        show ian at lef
        show wen at rig
        with short
        if ian_athletics > 2:
            wen "Good, you've got it!"
            i "You're not making it easy for me, though."
            wen "I'm resisting so you are forced to use technique, not just strength. But I see you learn quickly."
            i "I guess I've been training quite seriously lately."
            wen "That's the spirit. You'll get the basics in no time."
        else:
            i "It's too hard!"
            wen "It's not... You'll get it in no time if you keep training."
            wen "You need to devote yourself a bit more, though. If you take this as a simple hobby your progress will be slow."
            i "I guess I should train more, huh?"
            wen "That never hurts. One step at a time, though."
            $ ian_athletics_xp += 1
            play sound "sfx/xp.mp3"
            show athletics_up
            call screen skillsup
        show ian at lef3
        show wen at rig3
        with move
        show jeremy
        with short
        j "Hey there! How was the training today?"
        $ fian = "n"
        i "It was cool. Learning bit by bit."
        j "I'm sure you two had a lot of fun hugging each other, ha ha!"
        hide jeremy
        hide wen
        show wensmile at rig3
        show jeremy
        wen "Don't tell me you're feeling left out? I can hug you if you want, but I won't hold back with a big guy like you."
        $ fjeremy = "sad"
        j "Uh, no, thank you... I've seen you fight, you'd probably snap my neck or something."
        wen "Oh, so you don't like my tough love?"
        $ fjeremy = "n"
        j "I'll let Ian have all of it."
        j "Come on, let's go."
        jump v5trainingend
        
## KICKBOXING
    else:
        show yuri at lef3
        show jeremy at rig3
        with short
        $ kicklesson1_error = 0
        "We put on boxing gloves to hit the heavy bag and Yuri showed me some basic combinations."
        yuri "OK, pay attention."
        yuri "Let's start with the most basic combo: left jab, right cross, left hook."
        yuri "Got it?"
        i "Left jab, right cross, left hook."
        yuri "Yeah. Now do it on the heavy bag."        
        scene gym
        show v2_box
        with long
        $ timeout_label = "kicklessontime1"
        
        menu v5kick1a:
            "Left jab!":
                $ renpy.block_rollback()
                jump v5kick1b
                
            "Right jab!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "No! Left jab, right cross, left hook! Again!"
                jump v5kick1a
                
            "Right cross!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "No! Left jab, right cross, left hook! Again!"
                jump v5kick1a
        
        menu v5kick1b:
            "Left hook!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "No! Left jab, right cross, left hook! Again!"
                jump v5kick1a
            
            "Right cross!":
                $ renpy.block_rollback()
                jump v5kick1c
                
            "Left cross!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "No! Left jab, right cross, left hook! Again!"
                jump v5kick1a
                
        menu v5kick1c:
            "Right hook!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "No! Left jab, right cross, left hook! Again!"
                jump v5kick1a
                
            "Left cross!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "No! Left jab, right cross, left hook! Again!"
                jump v5kick1a
                
            "Left hook!":
                $ renpy.block_rollback()
                play sound "sfx/big_punch.mp3"
                i "Umpf!" with vpunch
        
        yuri "Good!"
        if kicklesson1_error == 0:
            play sound "sfx/xp.mp3"
            show athletics_up
            $ ian_athletics_xp += 1
            call screen skillsup
        yuri "Don't bend your wrist when you punch! Turn your foot inward and rotate the hip on the hook!"
        yuri "Let's practice this one for a while."
        play sound "sfx/punching_bag.mp3"
        "After several rounds Yuri showed me a different combo."
        $ fian = "n"
        scene gym
        show ian at lef 
        show yuri at rig
        with short
        yuri "OK now, look at this."
        yuri "Double jab to measure the distance and bring the opponet's guard up, then..."
        yuri "Right uppercut to the chin and left hook to finish him off!"
        yuri "Do it."
        scene gym
        show v2_box
        with long
        $ timeout_label = "kicklessontime2"
        
        menu v5kick1d:
            "Jab!":
                $ renpy.block_rollback()
                jump v5kick1e
                
            "Cross!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "No, no! Double jab, uppercut and right cross! Again!"
                jump v5kick1d
                
            "Uppercut!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "No, no! Double jab, uppercut and right cross! Again!"
                jump v5kick1d
        
        menu v5kick1e:
            "Cross!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "Come on, Ian! Are you even paying attention?"
                yuri "Start over!"
                jump v5kick1e
                
            "Jab!":
                $ renpy.block_rollback()
                jump v5kick1f
                
            "Uppercut!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "Come on, Ian! Are you even paying attention?"
                yuri "Start over!"
                jump v5kick1d
                
        menu v5kick1f:
            "Cross!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "Almost got it! Double jab, uppercut and right cross!"
                yuri "Start over!"
                jump v5kick1d
                
            "Jab!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "Almost got it! Double jab, uppercut and right cross!"
                yuri "Start over!"
                jump v5kick1d     
                
            "Uppercut!":
                $ renpy.block_rollback()
                yuri "Good! Now finish him off!"
                jump v5kick1g
                
        menu v5kick1g:
            "Left hook!":
                $ renpy.block_rollback()
                play sound "sfx/big_punch.mp3"
                i "Mhpf!!" with vpunch
                yuri "Excellent!"
                
            "Right hook!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                play sound "sfx/punch.mp3"
                i "Mhpf!!" with vpunch
                yuri "Good, but it's better if you end with a left hook, not a right one. See?"
                i "OK..."
                
            "Right cross!":
                $ renpy.block_rollback()
                $ kicklesson1_error += 1
                yuri "Nope! But close enough..."
        
        yuri "Come on, don't stop. Keep drilling the combo!"
        play sound "sfx/punching_bag.mp3"
        if kicklesson1_error < 2:
            play sound "sfx/xp.mp3"
            show athletics_up
            $ ian_athletics_xp += 1
            call screen skillsup        
        "I kept hitting the heavy bag until my arms felt heavy and sweat ran down my body."
        $ fian = "worried"
        $ fjeremy = "smile"
        scene gym
        show yuri at lef3
        show jeremy at rig3
        show ian 
        with long
        i "Man, I'm beat... This is tough!"
        yuri "It's a great way to build technique and endurance. I guess it's enough for today."
        j "Today was a cool session, but let's do some sparring next time! I have to get ready for the tournament."
        yuri "Don't worry, I'll get you ready."
        j "Come on, let's hit the showers."
        $ timeout_label = None
        jump v5trainingend

label kicklessontime1:
    yuri "Wake up, Ian! Jab, cross, hook!"
    jump v5kick1a
label kicklessontime2:
    yuri "Wake up, Ian!"
    jump v5kick1d
    
####END

label v5trainingend:
    stop music fadeout 2.0
    scene streetnight
    with long
    $ fian = "n"
    $ fjeremy = "smile"
    $ ian_look = 1
    $ jeremy_look = 3
    show ian at lef
    show jeremy at rig
    with short
    if jiujitsu > 0:
        j "So, how's the training with Wen going?"
        i "It's a bit repetitive, and quite methodical..."
        j "See? I told you, grappling's really boring."
        i "No, but I really feel I've learned something new. I can do something I had no idea of how to do before."
        i "And the training is tough, man. I've never felt so tired and banged up."
        j "Watch out or Wen will end up destroying you, he has no measure!"
        i "I'm surviving thus far."
    else:
        j "So, what did you think of Yuri?"
        i "It seems he really knows his stuff. And a really tough trainer, too."
        j "He's awesome. I've seen some of his fights when he was a pro... And yeah, he's a tough mofo."
        j "Now you see how I got so good so fast!"
        i "Let's hope that happens to me, too."
    if ian_lena_sex or v4_ian_kiss:
        $ fjeremy = "happy"
        j "So tell me, what were you so happy about before?"
        $ fian = "shy"
        if ian_lena_sex:
            i "Well, I might've... slept with Lena yesterday."
            $ fjeremy = "happy"
            j "No way, dude! For real?"
            i "Yeah."
            "I told him how the night had gone, and how it had ended."
            j "That's {i}aaawesome{/i} dude! So it was her who called you to invite you up. You're slaying it!"
            i "I wasn't expecting it, that's for sure."
            j "Seems like she's crazy about you, huh?"
            j "Either that, or she's a very horny chick!"
            $ fian = "worried"
            i "Um, well, maybe..."
            $ fjeremy = "smile"
            j "I'm happy for you, bro."
        else:
            i "I had a date with Lena last night..."
            $ fjeremy = "happy"
            j "Really? And you scored? Tell me you scored man, come on!"
            $ fian = "smile"
            i "No, not yet... But we made out."
            $ fjeremy = "sad"
            j "Just that? A few kisses?"
            i "Not just a few kisses... {i}Real{/i} kisses! There's passion there, there's no mistaking it."
            $ fjeremy = "smile"
            j "I'm happy for you, bro. If you feel she wants it, it's only a matter of time until it happens."
            j "Don't let up!"
    elif v4_ian_date:
        j "So, any new developments with the model?"
        i "With Lena?"
        j "Yeah!"
        i "We went on a date yesterday..."
        $ fjeremy = "happy"
        j "Really? And did you score with her?"
        i "No, not yet..."
        $ fjeremy = "smile"
        j "How come? Do you think she's not interested?"
        i "I'm not sure... I'd say she is, but I can't really read her. Women are complicated like that."
        j "You should go for it, man. Don't stress too much about it, just take action!"
        j "If she went on a date with you she has to have some sort of interest in you."
        i "Maybe you're right..."
    j "By the way, it's about time you guys came to see me at the club, don't you think so?"
    j "I've been working there for two months or so already!"
    i "I guess so..."
    j "When was the last time you went out partying? Not having some beers at a lame bar."
    j "Dancing, flirting, burning the night until the sun comes up..."
    $ fian = "insecure"
    i "I, uh..."
    "When was it, actually? I didn't recall going to a club after breaking up with Gillian yet..."
    $ fian = "n"
    i "Way too long."
    j "Way too long! See? Say what, you and the gang come see me this Saturday."
    j "I'll make sure to slip you some free drinks. And I'll even try to get you in for free."
    j "Surely you can't say no to that!"
    $ fian = "smile"
    i "No, I guess I can't. Have you told anyone else?"
    j "Not yet. Tell Perry and Emma, I'll take care of Wade, Cindy and Alison."
    i "You want me to tell Perry? There's no way he'll agree to come."
    $ fjeremy = "happy"
    j "I doubt it, unless you convince Emma to come, too, then..."
    $ fian = "happy"
    i "That's the only way he'd agree to come, that's for sure. And even if that were the case, I'd still have my doubts."
    $ fjeremy = "n"
    j "Whatever, just tell him so at least he can't say we leave him out of our get-togethers."
    $ fjeremy = "smile"
    $ fian = "smile"
    j "Well, see you on Saturday, then!"
    if ian_lena_sex:
        j "And congrats on scoring with the model!"
        i "Thanks."
    else:
        i "Sure."
    
    scene ianroomnight
    with long
    $ ian_look = 2
    $ fian = "n"
    play music "music/normal_day.mp3" loop
    show ian with short
    "Once home I ate some leftovers for dinner, then I lay down in bed."
    "I was tired, I didn't want to cook."
    if v4_ian_date:
        "I picked up my phone while lying down."
        i "I should text Lena..."
        if ian_lena_sex:
            "After the amazing night we had shared... The right amount of time had passed to not make her feel pressured and it was the moment to show her I cared about her."
            i "{i}Hey Lena, how was your day? {image=emoji_smile.png}{/i}"
            "She answered back almost immediately."
            play sound "sfx/sms.mp3"
            $ fian = "smile"
            l "{i}It was fine! What about yours?{/i}"
            i "{i}I'm trying to find the strength to get up from bed... Today's workout was killer.{/i}"
            i "{i}Not as killer as last night, though {image=emoji_crazy.png}{/i}"
            l "{image=emoji_shy.png} {image=emoji_shy.png} {image=emoji_shy.png}"
            l "{i}It was... I've been thinking about it all day.{/i}"
            $ fian = "shy"
            i "{i}Me, too... It was amazing. You were amazing.{/i}"
            l "{i}Are you trying to make me blush? Because you're accomplishing it {image=emoji_surprise.png} {image=emoji_tongue.png}{/i}"
            i "{i}You're so cute when you blush. I wouldn't mind seeing it again.{/i}"
            l "{i}And I wouldn't mind showing it to you again...{/i}"
            "A wide smile appeared on my face."
            i "Looks like she enjoyed the experience as much as I did..."
            i "{i}I can't wait to see it again. When is it OK for you?{/i}"
        elif v4_ian_kiss:
            "It had been almost twenty-four hours since our date. The right amount of time had passed to not make her feel pressured and it was the moment to show her I cared about her."
            i "{i}Hey Lena, how was your day? {image=emoji_smile.png}{/i}"
            "She answered back pretty fast."
            $ fian = "smile"
            play sound "sfx/sms.mp3"
            l "{i}It was fine! What about yours?{/i}"
            i "{i}I'm trying to find the strength to get up from bed... Today's workout was killer.{/i}"
            l "{i}Don't overdo it or you won't have any energy left to hang out with me!  {/i}"
            $ fian = "shy"
            "A wide smile appeared on my face."
            i "Looks like she's eager to see me again after last night..."
            i "{i}I will always find the energy to see you, believe me. I can't wait, in fact.{/i}"
            i "{i}When is it OK for you?{/i}"
        else:
            "It had been almost twenty-four hours since our date. The right amount of time had passed to not make her feel pressured and it was the moment to show her I was still interested."
            i "{i}Hey Lena, how was your day? {image=emoji_smile.png}{/i}"
            "She answered back after a couple of minutes."
            $ fian = "smile"
            play sound "sfx/sms.mp3"
            l "{i}It was fine! What about yours?{/i}"
            i "{i}I'm trying to find the strength to get up from bed... Today's workout was killer.{/i}"
            l "{i}Don't overdo it!{/i}"
            i "{i}It's OK. It's been the highlight of the week... Aside from last night at the bar, of course {image=emoji_wink.png}{/i}"
            l "{i}It was a lot of fun, yeah {image=emoji_smile.png} We should do that again.{/i}"
            "So, she wanted to go out with me again after all!"
            i "{i}I'd love to. When is it OK for you?{/i}"
        l "{i}I still have to organize my week. Things are pretty chaotic right now, with what's happening with my jobs and all that...{/i}"
        $ fian = "n"
        i "{i}Oh, yeah... If I can help with that don't hesitate to let me know.{/i}"
        l "{i}I'm taking care of it, don't worry!{/i}"
        i "{i}And what about this weekend? Tomorrow night, maybe?{/i}"
        l "{i}Oh, tomorrow I have plans with Ivy. I haven't been seeing her much lately. Are you free on Saturday?{/i}"
        i "{i}No, it's me who has plans with friends on Saturday...{/i}"
        l "{i}Oh, too bad! Well, I'm sure we'll find a moment to see each other soon!{/i}"
        "We texted for a bit, making some small talk, but a fun one at that. I felt a really good vibe between us."
        "We talked about our day-to-day life, and about what would be happening tomorrow at the magazine."
        "I put the phone away."
    $ ian_seymour_agenda = True
    if ian_switch_review or ian_honest_review:
        i "Tomorrow's the day... Seymour Ward is coming to the magazine."
        i "And Minerva won't let me attend."
        if v5_hand_proposal_lena:
            "Thankfully, Lena had agreed to hand my proposal to Mr. Ward for me."
            "Just imagining being published by Hierofant... I would be able to stop worrying about the literary contest."
            i "It would be much better if I could see him in person, but this way Minerva won't go crazy on me."
            i "Going against Minerva's express wishes would only cause me big trouble."
        elif v5_hand_proposal:
            $ fian = "worried"
            "I had been working on my book's synopsis and making sure the first chapters were perfect."
            "If I could hand this to Seymour Ward there was a chance for my book to be noticed by Hierofant publishing..."
            "Just imagining being published by them... I would be able to stop worrying about the literary contest."
            "I had said I would hand my proposal to Mr. Ward myself, but Minerva had forbidden me to show up at the office."
            "What should I do? Going against Minerva's express wishes would only cause me big trouble..."
            "Maybe I should try and find a better moment to hand it to Mr. Ward. But when? Lena said he knew him, though..."
        else:
            $ fian = "sad"
            "I had already accepted I wasn't gonna be able to hand him my book proposal."
            i "Not yet, at least..."
            "Going against Minerva's express wishes would only cause me big trouble."
            "Just imagining being published by Hierofant... I would be able to stop worrying about the literary contest."
            "Sadly, that wasn't going to happen. I still had to rely on my chance of winning that prize."
        play sound "sfx/sms.mp3"
        "As I was thinking about this, my phone buzzed with a text."
        "It was Holly's."
        h "{i}Hi, Ian. I was talking to my publisher and told her about Seymour Ward's visit at the magazine, tomorrow.{/i}"
        h "{i}Turns out she knows the reason: it looks like he's proposing co-working possibilities to certain magazines to get more control over them.{/i}"
        $ fian = "surprise"
        h "{i}That means he's offering jobs to interns. I know Minerva has forbidden you to go, but I thought you should know...{/i}"
        "These news changed everything. If I managed to get hired by Seymour Ward..."
        $ fian = "worried"
        "Not only that my job's security wouldn't be in Minerva's hands, but I would also get closer to him, increasing the possibilities of having my book noticed."
        "It was a very risky chance, but...!"
        i "{i}Thanks for letting me know, Holly. No wonder Minerva didn't want to disclose the real reason for his visit in front of me.{/i}"
        h "{i}I wasn't sure if I should tell you, because I'm worried you'll get yourself in trouble...{/i}"
        i "{i}You did the right thing, Holly. Thanks a lot, really.{/i}"
        i "{i}What happens from now on is only my responsibility.{/i}"
        h "{i}Please take care.{/i}"
        i "{i}I will.{/i}"
        $ fian = "n"
        "What to do with this information?"
        menu:
            "{image=icon_will.png}Show up at the office tomorrow" if ian_will > 0:
                $ renpy.block_rollback()
                $ v5_ian_showup = True
                $ fian = "serious"
                $ ian_will -= 1
                play sound "sfx/willdown.mp3"
                show will_down
                i "I have to show up. I can't afford to lose this opportunity."
                i "I have to get my book noticed by Hierofant publishing."
                "I knew Minerva would get completely furious with me, but I had to take this chance."
                if v5_hand_proposal == False and v5_hand_proposal_lena == False:
                    "And, since I was already risking it, why not hand Seymour my book proposal?"
                    i "I might as well try my luck with that, too. I'm already tempting fate as it is, so..."
                    $ v5_hand_proposal = True
                "I jumped from the bed and got in front of the computer."
                play sound "sfx/keyboard.mp3"
                scene ianroomnight
                show v2_ianwrite
                with long
                "I had to make sure everything was perfect before printing it and handing it to Mr. Ward."
                
            "It's better to stay home":
                $ renpy.block_rollback()
                $ fian = "sad"
                i "It's better if I stay home. I'm sure Minerva will fire me otherwise."
                i "And there's no guarantee Mr. Ward will hire me. I can't afford to lose my job at the magazine right now..."
                if v5_hand_proposal_lena:
                    i "At least I know Lena will hand him my proposal..."
                    i "The book's far from finished, though!"
                else:
                    $ v5_hand_proposal = False
                    i "I won't be able to hand him my proposal, either..."
                    i "But I'm hopeful other chances will appear. Besides, the book's far from finished!"
                "There was a lot of work to be done."
    else:
        $ v5_ian_showup = True
        if v5_hand_proposal:
            "There was work to be done."
            "I jumped from bed and got in front of the computer."
            scene ianroomnight
            show v2_ianwrite
            with long
            "I had been working on my book's synopsis and making sure the first chapters were perfect."
            "If I could hand this to Seymour Ward there was a chance for my book to be noticed by Hierofant publishing..."
            "I had said I would hand my proposal to Mr. Ward myself, but I knew Minerva wouldn't approve."
            "What should I do? She was already looking for any excuse to diminish me and that would surely cause trouble..."
            "Maybe I should try and find a better moment to hand it to Mr. Ward... But when? Lena said he knew him, though..."
            menu:
                "{image=icon_will.png}Hand him the book proposal" if ian_will > 0:
                    $ renpy.block_rollback()
                    $ fian = "serious"
                    $ ian_will -= 1
                    play sound "sfx/willdown.mp3"
                    show will_down
                    i "It has to be tomorrow."
                    i "I don't know when another chance like this will present itself."
                    i "If I make a good impression on him maybe I'll even increase the odds of being hired."
                    "I wasn't gonna lose this chance to get my book noticed by Hierofant publishing, no matter how much that could bother Minerva."
                    play sound "sfx/keyboard.mp3"
                    "I kept polishing my writing and making sure everything was perfect."
                    
                "Wait for another chance":
                    $ renpy.block_rollback()
                    $ v5_hand_proposal = False
                    $ fian = "sad"
                    scene ianroomnight
                    show ian
                    with long
                    i "I guess I should wait for another chance after all..."
                    "Going against Minerva's express wishes would only cause me big trouble."
                    $ fian = "n"
                    i "Things are already tough at the magazine as they are. Last I need is to make it harder for myself."
         
        elif v5_hand_proposal_lena:
            "Tomorrow was the day. Seymour Ward was coming to the magazine..."
            "Even though at first I thought this could be a good chance to hand him my book proposal, hoping to get noticed by Hierofant publishing, that would cause me trouble for sure."
            "I knew Minerva wouldn't approve of me pestering her guest. Thankfully, Lena had agreed to hand my proposal to him for me."
            i "It would be much better if I could give it to him myself, but this way Minerva wouldn't go crazy on me."
        else:
            $ fian = "sad"
            "I had already accepted I wasn't gonna be able to hand him my book proposal."
            i "Not yet, at least..."
            "Going against Minerva's express wishes would only cause me big trouble."
    
    if v5_cindy_shoot:
        play sound "sfx/ring.mp3"
        $ fian = "n"
        i "Uh? Who's calling at this hour?"
        scene ianroomnight
        show ian_phone
        with short
        show phone_cindy at lef3
        with short
        c "Hi, Ian."
        $ fian = "smile"
        i "Hey, Cindy. What's up, how come you're calling me at this hour?"
        c "It's not too late, is it?"
        i "No, don't worry. I just wasn't expecting you to call me just before bedtime, ha ha."
        c "It's about what we talked about at the gallery. The photo-shoot."
        "She was talking in a soft voice, like she didn't want to make too much noise."
        "Maybe like she didn't want to be heard, even..."
        c "I talked to Axel and he says to do it tomorrow afternoon."
        c "You said you would go with me, so... Are you free tomorrow?"
        i "Um, yeah, I think so... I have no plans I can recall."
        c "Cool! Tomorrow at six. I'll send you the address."
        c "Thanks, Ian."
        i "Don't mention it."
        hide phone_cindy
        hide ian_phone
        show ian
        with short
        i "It's my pleasure..."
        "So it was really happening, huh? Cindy decided to pose for Axel..."
        $ fian = "n"
        "And I would be there as her moral support."
        "I wondered if I was making a mistake encouraging her to do this."
        "I was pretty sure she hadn't told Wade, and I doubted he would be happy when he'd inevitably find out..."
        "Especially if he learned I had been involved in all of this."
        i "If I don't go with her she will find some other friend, though."
        $ fian = "serious"
        i "Better if it's me who goes, that way I can keep a close eye on things, make sure that Axel guy doesn't overstep his boundaries."
        "I didn't trust him. I had the feeling he wanted more from Cindy than just taking a few pictures."
        $ fian = "worried"
        "And I also had the feeling Cindy would have a hard time saying no to him..."
    
    stop music fadeout 2.0
    
## IAN FRIDAY ###########################################################################################################################################################################################
    
    $ day = "Friday"
    scene blackbg
    with long
    call screen calendar
    
    if v5_ian_showup:
        
        if ian_honest_review or ian_switch_review:
            scene street
            with long   
            $ fian = "serious"
            $ ian_look = 1 
            show ian with short
            "Next morning I got up early and had a hearty breakfast."
            "My stomach wasn't hungry for food, but I wouldn't let unease take control of me."
            "I was determined."            
            "I carried an envelope tucked tightly under my arm. Inside it there was a dossier with my book proposal."
            "I had to find the best moment to hand it to Mr. Ward."
            "And if what Holly had told me was true, I could even have a chance at getting hired by Hierofant publishing itself."
            scene magazine
            with long   
            "I arrived several minutes after the start of the working day, just to be sure, and I sneaked into the magazine."
            show ian at left with moveinleft
            "I hid behind one of the desks further to the back of the office, scouting the area."
            "It didn't take long to see what I was searching for."
            $ fian = "n"
        else:
            scene magazine
            with long   
            $ fian = "n"
            $ ian_look = 1
            show ian with short
            "I arrived at the office like any other day. But I knew today would be different."
            if v5_hand_proposal:
                "I carried an envelope tucked tightly under my arm. Inside it there was a dossier with my book proposal."
                "I had to find the best moment to hand it to Mr. Ward."
                "And if what Holly had told me was true, I could even have a chance at getting hired by Hierofant publishing itself."
            else:
                "If what Holly had told me was true, I could have a chance at getting hired by Hierofant publishing itself."
            "I sat at my desk and waited for the big man to show up. It didn't take too long."            
            show ian at lef3 with move
            
        play music "music/fancy.mp3" loop
        $ seymour_look = 1
        $ fseymour = "n"
        $ fminerva ="smile"
        show minerva at rig3
        show seymour
        with short
        mi "Listen everybody, gather round!"
        mi "Our guest needs no introduction, since he's such a well-known figure in the publishing world: Mr. Seymour Ward."
        mi "As you know, we've been collaborating with Hierofant publishing for quite some time now and Mr. Ward has expressed interest in our work."
        $ fseymour = "smile"
        mr "Thank you for welcoming me into your offices."
        "So this man was the famous Seymour Ward. He certainly looked the part of a cultured and successful businessman."
        if ian_honest_review or ian_switch_review:
            "All attention was focused on him and I had gone unnoticed so far."
        else:
            "He had the entire office's attention, mine included."
        mr "You might be wondering what brings me to visit your magazine. As Minerva said, we've been working together closely for quite some time."
        mr "The work that you do is paramount to give visibility to our published authors and spread the word to the readers. Much of our success depends on you."
        mr "One could say magazines such as yours are what connects us to the public. I thank you on behalf of Hierofant publishing."
        "What he was trying to say was that they used us as a publicity and marketing agency to increase their sells."
        mr "We're always expanding and interested in recruiting new talent. That's why I'm here, to extend an offer to the interns working at this magazine."
        "Gasps and whispering could be heard amongst my co-workers. So Holly was right."
        mr "In our attempt to tighten our collaboration with your magazine, we're offering a couple of co-working opportunities for you to work directly with our publishing firm."
        "Of course, that was a chance every intern would want to jump on. Me included."
        mr "Minerva here will take care of the applications of anyone who's interested and forward them to me. She'll let you know the details."
        mr "If you have any questions..."
        "I raised my hand."
        i "Yes, here."
        $ fminerva = "mad"
        if ian_honest_review or ian_switch_review:
            "Minerva's eyes widened with surprise when she saw me, and then narrowed with visible anger."
            "I noticed how she had to contain herself to keep quiet. She didn't want to cause a ruckus in front of Mr. Ward."
            "Maybe I had just signed my death sentence, but I had to act."
            "If Minerva was the one taking care of the applications, I could count myself out. If I wanted to have a chance, I had to jump on it now and grab it myself."
        else:
            "Minerva directed a sour look towards me, but didn't say anything."
            "If she was the one taking care of the applications, I could count myself out. If I wanted to have a chance, I had to jump on it now and grab it myself."
        mr "What's your name?"
        i "Ian. Ian Watts."
        mr "Nice to meet you, Ian. Go ahead."
        i "You haven't specified what the job will be about. I assume it has to do with selecting and reviewing submissions?"
        mr "Mostly, yes. We have a ton of authors who want to be published submitting their books to us, and we need more beta readers to take care of that."
        mr "But the job will also have you work on accepted proposals, editing, proofreading and things such like that, depending on your competence."
        mi "Now, if anybody else has a question..."
        "I wouldn't let Minerva cut me short."
        i "I still have another one, if I may."
        if ian_honest_review or ian_switch_review:
            $ fminerva = "furious"
            "If looks could kill I would've died right there at that moment. Thankfully, all Minerva could do was stare at me."
            $ fminerva = "mad"
        else:
            "Minerva gave me another look of disgust, but she couldn't do much more."
        mr "Sure, go ahead."
        menu:
            "I want that job":
                $ renpy.block_rollback()
                $ fian = "serious"
                i "I want to get that job, sir."
                "I looked at Minerva for a second, answering to her hateful stare."
                mr "That's not a question, isn't it?"
                i "No. It's a request."
                $ fian = "n"
                i "I'm really interested in this opportunity and I know I can do a good job."
                mr "I see. Ian Watts you said, right?"
                i "Yes, sir."
                mr "You have a good attitude, and I can see you're really serious and determined about this."
                mr "You can send your resume directly to our human resources team. Tell them Seymour Ward wants them to take a good look at it."
                mr "I hope it's as convincing as you're selling it to be."
                play sound "sfx/xp.mp3"
                show charisma_up
                $ ian_charisma_xp += 1
                call screen skillsup
                $ fian = "smile"
                i "Yes, sir."
                
            "What's the selection criteria?":
                $ renpy.block_rollback()
                i "I'm wondering about the selection criteria. What will you be looking at?"
                $ fseymour = "n"
                mr "Your analysis and writing ability, and your resume and work as an intern in this magazine."
                i "And is there any way we can provide added value? Proving to have technical experience not only reviewing, but also creating written works?"
                $ fseymour = "smile"
                mr "Interesting. Ian Watts you said, right?"
                i "Yes, sir."
                mr "I see you have a clever business mentality."
                play sound "sfx/xp.mp3"
                show wits_up
                $ ian_wits_xp += 1
                call screen skillsup
                $ fian = "smile"
                i "I'm just very interested in this chance and I'd like to get the job. I know I can meet your expectations."
                mr "That's an interesting attitude. Sure, feel free to submit what you think might provide that added value we're always looking for."
                
            "Who will be selecting the candidates?":
                $ renpy.block_rollback()
                i "So, who will be responsible for selecting the candidates? Our boss?"
                $ fseymour = "n"
                mr "No, she will review the applications and forward them to our human resources team."
                i "Can we directly forward our applications ourselves?"
                mr "As long as they comply with our requisites, I don't see why not... Why would you want to do that, though?"
                if ian_honest_review or ian_switch_review:
                    $ fian = "serious"
                    i "I want to make sure I'm able to present myself and my work honestly, without corporate interference..."
                    "I looked at Minerva for a second, answering to her hateful stare."
                    i "And I want to avoid any possible irregularities in the process."
                    mr "Irregularities, huh?"
                    $ fseymour = "smile"
                    mr "I see. You're really serious about your work, and proud."
                    $ fian = "n"
                    i "I try to be."
                    mr "That's a good attitude."
                else:
                    i "I'm just really interested in this opportunity and I want to make sure your department gets my resume."
                    mr "You don't trust Minerva to do it?"
                    i "It's something important to me, so I'd prefer to take care of things directly."
                    $ fseymour = "smile"
                    mr "I see. You're serious about your work and you want to take full personal responsibility for your goals."
                    i "Yes, sir."
                    mr "That's a good attitude."
                mr "Feel free to contact our human resources team directly, if that's how you want to go about it."
            
        mr "Wait a moment..."
        "He searched for something in the interior pocket of his jacket."
        mr "Here, take this card. It's the contact info of the head of the department. You can forward your application directly to him."
        $ fian = "smile"
        "I walked up to him and grabbed it."
        i "Thanks."
        hide minerva
        hide seymour
        with short
        show ian at truecenter with move
        "That went even better than expected!"
        "I had managed to bypass Minerva's interference and got the contact info of the head of the department."
        "That didn't guarantee me the job, but at least I was sure Minerva wouldn't meddle with my application."
        if ian_honest_review or ian_switch_review:
            "I saw how affronted she was by my defiance, but she left me no choice."
            "I wasn't gonna let her smother my dreams and goals."
            scene street with long
            show ian with short
            "Minerva took Seymour to her office and I left the magazine. I didn't want to overstay my welcome."
            if v5_hand_proposal:
                "I decided to wait for Mr. Ward at the door. I would approach him when he left."
                $ fian = "n"
                "I only had to wait around twenty minutes. I saw him exit the magazine... accompanied by Minerva."
                i "It's now or never."
                jump v5handproposal
            else:
                "I had gotten more than I had been hoping for from this visit. I could deal with not handing Mr. Ward my book proposal."
                if v5_hand_proposal_lena:
                    "Lena would do that for me, after all..."
                jump v5ianfriday2
            
        else:
            "I was sure she wasn't happy about me jumping the horse, but I wasn't gonna risk leaving that chance in her hands."
            "Her disposition to me had never been favorable."
            "After that, Minerva finished showing Seymour around and then took him to her office."
            "About twenty minutes later, I saw her walk him to the door. He was leaving."
            if v5_hand_proposal:
                $ fian = "n"
                "This was the moment. I had to approach him and hand him my proposal..."
                i "It's now or never..."
                jump v5handproposal
            else:
                "I had gotten more than I had been hoping for from this visit. I could deal with not handing Mr. Ward my book proposal."
                if v5_hand_proposal_lena:
                    "Lena would do that for me, after all..."
                jump v5ianfriday2
                
    else:
        scene ianhome
        with long   
        $ fian = "sad"
        $ ian_look = 1 
        if jiujitsu > 0:
            "I got up pretty late next morning. I was tired after Wen's training and I had no real reason to get up early."
        else:
            "I got up pretty late next morning. I was tired after Yuri's training and I had no real reason to get up early."
        "I wasn't welcome at the magazine, after all..."
        $ fian = "serious"
        i "Damned Minerva... Why does she have to make my life so hard?"
        $ fian = "sad"
        "I wondered what Seymour Ward would be telling my co-workers. I was sure it would've been an interesting experience."
        $ fian = "n"
        i "No point in brooding over it... It is what it is."
        i "I should get some writing done..."
        "I spent the morning trying to work on my book, but it wasn't one of my best days."
        "I managed to make some progress, at least."
        jump v5ianfriday2
        
label v5handproposal:        
    $ fminerva = "smile"
    $ fseymour = "n"
    show ian at lef3 with move
    show seymour2
    show minerva at rig3
    with short
    i "Excuse me, sir."
    $ fminerva = "mad"
    mr "Huh?"
    mi "Ian, don't bother Mr. Ward. He was just leaving."
    i "I know. It'll be just a second, Mr. Ward."
    mr "What is it? If you have any more questions I'm sure the head of department can help you."
    i "It's not about the job. I'm also an aspiring writer, and I wanted to take this chance to show you my work."
    "Minerva stepped between me and Mr. Ward, physically blocking my approach."
    mi "I'm sure Mr. Ward is a very busy man and doesn't have time to read the scribbles of an amateur."
    mr "We have an e-mail where you can send your proposal to for its evaluation. That's a competence of the same department you want to be hired on."
    i "I'd rather give it to you directly, if you don't mind."
    mi "It's obvious he does. Why should he accept to personally read the pitch of a no-name amateur writer?"
    i "Because I'm confident it's something worth reading and I believe in the quality of my work."
    i "All I'm asking is for you to read the synopsis. It won't take you more than ten minutes, and if you're unimpressed by it you can just throw it in the bin."
    i "I know I'm in no place to ask, but I'm sure you'll find it interesting."
    $ fseymour = "smile"
    mr "You're a passionate young man, aren't you? I can appreciate your will to succeed and the fire behind your words."
    mr "Alright, give it to me, I'll take a look at it when I have the time."
    $ ian_seymour += 1
    play sound "sfx/friendup.mp3"
    show friend_up
    $ fian = "happy"
    i "Thank you, sir. You won't be disappointed."
    mr "I hope not."
    "Minerva had to step aside for me to hand the envelope to Mr. Ward. She was clenching her teeth behind her mask of composure."
    i "I won't take any more of your time. Have a good day."
    hide minerva
    hide seymour2
    with short
    show ian at truecenter with move
    "I turned around and left them. I had managed to get him to accept my pitch!"
    "That was no guarantee of anything, but still..."
    "My proposal was in Seymour Ward's hands, and that alone was big."
    "It was to be seen if that seed would come to bear fruit... But at least I had planted it."
    stop music fadeout 2.0
        
label v5ianfriday2:        
    i "Now that I think about it, I haven't told Emma about tomorrow yet."
    i "I should give her a call."
    hide ian
    show ian_phone
    with short
    i "..."
    show phone_emma at lef3
    e "Hey, Ian! What's up!"
    $ fian = "smile"
    i "Hey! Jeremy wants the gang to go pay him a visit at that club he's working in this Saturday."
    i "Are you in?"
    e "A club, huh? It's been a while since I've been to one."
    e "But it's one of those clubs where you have to doll yourself up to get in and they only play dumb, mainstream music, right?"
    $ fian = "n"
    i "I'm afraid so..."
    e "Mhh... Those are not my favorite places."
    i "Come on, it will be fun... I hope."
    e "You know having fun is not a problem for me. I can adapt to almost everything!"
    $ fian = "smile"
    i "That's one of the many talents I envy you for."
    e "To be honest, the main reason I'm coming is because I'm curious to see you and Perry in that environment, ha ha!"
    i "I still have to try and convince Perry to come."
    e "He hasn't agreed yet?"
    i "I haven't told him yet... But I needed to get some leverage first if I'm to convince him!"
    e "Leverage?"
    i "Never mind... See you tomorrow!"
    e "I hope I can find something I can wear to that place! Bye!"
    hide phone_emma
    hide ian_phone
    show ian
    with short
    i "Alright, she's in. Now I have to pitch the idea to Perry..."
    if v5_cindy_shoot:
        i "But first I have something important to do."
        i "It's almost time..."
        jump v5cindyshooting
    else:
        jump v5ianfridayend

## CINDY SHOOT ##################################################################################################################################################################################

label v5cindyshooting:
    
    scene street
    with long
    $ fian = "n"
    $ axel_look = 1
    $ ian_look = 1
    $ faxel = "smile"
    show ian with short
    "I still wasn't sure I was doing the right thing as I walked to meet Cindy."
    "It probably should be Wade accompanying her to this photo-shoot, not me..."
    "But it was me she had chosen. At least she wouldn't be alone with Axel..."
    show ian at lef with move
    $ fcindy = "smile"
    show cindy at rig with short
    c "Hey, Ian! You made it."
    i "Yup. Are we waiting for Axel?"
    c "He's already in the studio."
    i "Does he know I'm coming along?"
    c "Yeah, I told him. Let's go!"
    play music "music/flirty.mp3"
    scene studio_pink
    with long
    "She rang the bell and Axel let us in. I looked around with curiosity: it was my first time in a photo studio."
    "These were the kind of places Lena used to work at?"
    show ian at lef3
    show axel 
    show cindy2 at rig3
    with short
    x "Hey there, thanks for coming. How are you doing?"
    c "I'm a bit nervous, to be honest!"
    x "Don't worry, we'll take it easy. The idea is to have fun."
    if ian_axel > 3:
        x "What's up, Ian?"
    else:
        i "Hey."
        x "Oh, hey. Ian, right?"
        i "Yeah."
    "Axel shook my hand. He had a very strong and confident grip."
    x "So you're here to protect Cindy, huh?"
    i "Me? I wouldn't say I'm here to \"protect\" her..."
    x "I know, I was just joking. It's normal for girls to ask a friend to tag along on their first photo-shoots."
    c "I hope it's no bother."
    x "Not at all, don't worry. You can sit over there, Ian."
    "He pointed to a couch in the back of the studio."
    i "Sure."
    "So that would be my part in this. Sitting down and watching quietly."
    i "Cindy, if you need anything..."
    c "I'm OK. Having you here is enough."
    i "Cool."
    x "Have you brought the clothes we talked about?"
    c "Yeah."
    x "You can change in the equipment room over there."
    c "Alright. I'll be done in a minute."
    hide cindy2
    with short
    "She left Axel and me alone."
    show ian at lef
    show axel at rig
    with move
    i "..."
    "I didn't know what to say, but he didn't let an awkward silence settle in."
    x "She must trust you a lot if she's asked you to be her emotional support. Have you been friends for a long time?"
    i "A couple of years."
    x "I hope it didn't bother you too much, me jumping in that night at the bar."
    "It did, but I wasn't gonna admit it in front of him."
    menu:
        "I would've done the same in your place":
            $ renpy.block_rollback()
            $ fian = "smile"
            i "Don't worry, I would've done the same in your place. She's a girl you want to talk to."
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            $ faxel = "happy"
            x "She is, isn't she? She has a very striking beauty, that's for sure."
            i "Indeed. I guess that's why you proposed this photo-shoot to her."
            $ faxel = "smile"
            x "Of course. I'm sure she will look good on camera. But I was also curious about her personality."
            
        "You pick up your models at bars?":
            $ renpy.block_rollback()
            $ fian = "smile"
            i "So that's where you go search for your models, at bars?"
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            $ faxel = "happy"
            x "Any place is good to find interesting models. And you can find a lot of different things at a bar."
            x "Isn't that why people go to them?"
            i "I thought they went to get drunk, basically."
            $ faxel = "smile"
            x "You don't need to get out of home to get drunk. What people like is social interaction."
            i "Social interaction with the opposite gender, you mean."
            x "There's no better social interaction than that, is there? Ha ha."
            x "And Cindy's a curious girl..."
            
        "That is what bars are for":
            $ renpy.block_rollback()
            $ fian = "smile"
            i "Don't worry, that's what bars are for, aren't they? To meet people."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            x "That's what I think, but not everybody shares that view."
            i "It seems Cindy and I do. Though I wasn't expecting to be invited to a photo-shoot when I went out that night!"
            i "I guess you don't like to shoot guys, and that's why you only offered it to Cindy."
            $ faxel = "happy"
            x "What can I say? I have my preferences, ha ha."
            x "She's a stunning girl, that's for sure. But I was also curious about her personality."
            $ faxel = "smile"
           
        "I didn't mind":
            $ renpy.block_rollback()
            i "No, I didn't mind..."
            x "Cool. I had no intention to chat people up that night, but Cindy really caught my eye."
            i "Is that so? Why?"
            x "She's a stunning girl, that's for sure. But I was also curious about her personality."
            
    x "It's obvious she's aware of how beautiful she is, but she still has a kind of naivety that I find interesting."
    x "I wanted to see how she would act in front of the camera... We photographers are curious like that."
    $ fian = "n"
    "I suspected from the start that Axel's interest in Cindy went further than using her as a model, and the way he was talking about her now only reinforced that feeling..."
    $ cindy_look = "comfy"
    $ fcindy = "shy"
    show ian at lef3
    show axel at rig3
    with move
    show cindybra with short
    c "I'm ready."
    $ fian = "blush"
    "Cindy came out wearing just a loose tank top and panties. It was not too revealing, but still..."
    "She made it look so sexy."
    c "Is this OK?"
    x "Perfect choice, yeah. Just like we talked about."
    x "OK, step in front of the canopy. Ian, you can go sit there."
    hide ian with short
    show cindybra at lef
    show axel at rig
    with move
    "I did as he asked while he picked up his camera and finished setting up the lighting."
    "Cindy looked a bit awkward while she waited for Axel to begin the shooting."
    "He finally got behind the camera, ready to start."
    x "How's that nervousness?"
    c "It's a bit hard shaking it off with the camera pointed at me, ha ha..."
    x "It's normal. Just try to forget about it. We chose these clothes so you'd feel at ease."
    x "Remember, we don't have to do anything you're not comfortable with. Just go along with what you feel."
    c "OK."
    x "Let's begin."
    scene v5_cindy1
    with long
    x "Think of yourself being at home, wearing those comfy clothes."
    x "You just got out of bed on a lazy Sunday..."
    "Cindy attempted to pose, but I could see she was a bit stiff."
    play sound "sfx/camera.mp3"
    with flash
    x "Forget about the set and the camera. Imagine you're by yourself."
    c "It's hard with a camera pointed at me... And with Ian looking!"
    menu:
        "That's what you brought me for!":
            $ renpy.block_rollback()
            i "Hey, that's what you brought me for, isn't it?"
            c "But you're making me shy..."
            x "Will you be more comfortable without him?"
            "Was he going to ask me to leave? No way."
            c "No, no..."
            "Cindy took a deep breath, focusing on the task at hand."
    
        "Sorry":
            $ renpy.block_rollback()
            i "Sorry about that."
            x "Isn't that what you brought him for? Ha ha."
            c "It's making me shy..."
            x "Will you be more comfortable without him?"
            "Was he going to ask me to leave? No way."
            c "No, no..."
            "Cindy took a deep breath, focusing on the task at hand."
        
        "...":
            $ renpy.block_rollback()
            "I stayed quiet, trying not to interfere."
            x "Forget about him. Concentrate on the here and now."
            "Cindy took a deep breath, doing as Axel was telling her."
    scene v5_cindy2
    with long
    "She threw her hair back, opening her posture."
    play sound "sfx/camera.mp3"
    with flash
    x "Good, expand your movements. Make the space around you yours."
    "It seemed like Cindy was easing herself into the right mood bit by bit."
    "Her eyes were not looking down anymore, as she found some confidence to look at the camera."
    "It seemed Axel's directions were helping her. He talked with a calm and reassuring tone and it showed he knew what he was doing."
    scene v5_cindy3
    with long
    "Cindy felt increasingly more comfortable."
    "She held her arms up and played with her long, golden hair, trying new poses."
    "She was visibly shedding her initial stiff awkwardness, much to Axel's satisfaction."
    play sound "sfx/camera.mp3"
    with flash
    x "Good, that's beautiful..."
    x "Imagine the warm light of the sun on your skin. It's a beautiful day, and you're enjoying it."
    x "You feel at ease, you feel alive and beautiful."
    "She was. Damn, she was beautiful."
    "I couldn't help but to admire her slender figure, that thin waist and those long, toned legs..."
    x "Now, turn around and look over your shoulder."
    scene v5_cindy4
    with long
    c "Like this?"
    x "Great, you're letting loose! Have fun, smile for me."
    play sound "sfx/camera.mp3"
    with flash
    "Not reacting to what I was seeing was quite hard."
    "Those panties barely covered half of Cindy's ass... A perfect, round, tight ass I couldn't avert my eyes from."
    "I couldn't tell if I was enjoying the view or if it was torture. I shouldn't lust after Cindy's body, and yet it was the only thing I could do."    
    "This was what Wade got to see every morning..."
    play sound "sfx/camera.mp3"
    with flash
    x "Keep playing, Cindy. Tease the camera, let your sensuality out."
    "Ten minutes into the photo-shoot, and she seemed to be finally enjoying herself."
    "Her poses looked more bold and confident, and so did her smile."
    x "Show me how beautiful you are."
    scene v5_cindy5
    with long
    "And she did."
    "Cindy began pulling up her top slowly, swaying her hips side to side."
    "She revealed her flat and toned belly, her white and smooth skin..."
    "But she kept pulling it up until her underboob became visible."
    "I gulped, witnessing what was in front of me, even if I was at the other end of the room."
    "I was seeing Cindy like I had only ever seen her in my imagination... And so was Axel."
    play sound "sfx/camera.mp3"
    with flash
    x "That's it, Cindy, perfect."
    x "These pictures are turning out incredible, much better than I had hoped."
    x "Keep going. Bare all your beauty."   
    "Cindy stood still for a second, like she was having doubts."
    scene v5_cindy5b
    with long
    "And then she looked at me."
    "Her eyes found mine and my heart skipped a beat."
    "I had the impression she was looking for something, a reaction, maybe an opinion."
    "Was she asking me what she should do?"
    menu:
        "{image=icon_lust.png}Encourage her" if ian_lust > 2 or ian_go_cindy > 2:
            $ renpy.block_rollback()
            $ v5_cindy_nude += 1
            if ian_go_cindy < 3:
                $ ian_go_cindy += 1
            $ cindy_look = "comfytopless"
            "I shrugged and nodded, letting her know Axel's request seemed reasonable."
            "Truth was, I just wanted to see what was hiding under that top."
            scene v5_cindy6
            with long
            "And she showed it to me."
            "She raised up her arms, taking off the top, and in doing so revealed her naked chest to me... and to Axel."
            "It was only for a moment, but that view got etched into my retinas."
            scene v5_cindy7
            with long
            "Immediately she covered her breasts with her forearms, looking at the camera with a less confident expression."
            "She felt exposed, no doubt. She was."
            play sound "sfx/camera.mp3"
            with flash
            "Axel snapped a few pictures. If I had had a camera, I would've, too."
            "At this point I couldn't tell what weighed heavier on me: excitement, astonishment, concern or guilt."
            "All I knew was that my heart was pounding in my chest and its blood flow was making my pants feel a bit tighter than they should..."
            "With her boob pressed together like that she looked even more erotic."
            x "That's beautiful, Cindy, so sexy... Put your arms up, show me your beauty."
            "Cindy directed a quick glance at me before doing what Axel asked."
            scene v5_cindy8b
            with long
            i "Damn..."
            "I probably shouldn't be seeing this, but I was."
            "Cindy's boobs in full view... And they were even more stunning than I had imagined."
            "For a girl so slender, her breasts were really full, and round and perky at the same time."
            "They could only be described with one word: perfect." 
            play sound "sfx/camera.mp3"
            with flash
            x "I'm loving this, Cindy. I've worked with many models, but you're a natural."
            x "I want you in front of my camera. All of you."
            x "You're a muse right now. Pose for me like one."
            x "Take off your panties."
            menu:
                "Let her go on":
                    $ renpy.block_rollback()
                    $ v5_cindy_nude += 1
                    "Axel wasn't pulling any punches. He wanted Cindy completely naked in front of him."
                    "I told myself the reason I was there was to make sure Axel didn't do anything inappropriate, and I was pretty sure this qualified as something that was."
                    "If I were Wade I would hate the idea of my girlfriend getting naked in front of another guy, especially if he was taking pictures of her..."
                    "But she was getting naked in front of me, too. And I wanted to see it."
                    "I wanted to see all of her."
                    play sound "sfx/xp.mp3"
                    show lust_up
                    $ ian_lust_xp += 1
                    call screen skillsup
                    scene v5_cindy9
                    with long
                    "Cindy hesitated for a moment. But just for a moment."
                    "She turned around and began taking off her panties slowly..."
                    "There was no denying it. I was hard as a rock."
                    "I shouldn't be, but to hell with it. Cindy was a girl to lose one's mind for."
                    "If only I could be closer to her... If only it were just the two of us in this room..."
                    "But that was only wishful thinking. Something that would never come to pass."
                    "The truth was the one Cindy was stripping for was Axel, not me..."
                    play sound "sfx/camera.mp3"
                    with flash
                    "And he was using this chance to take some spectacular pictures of Cindy, no doubt."
                    scene v5_cindy8
                    with long
                    "She finished removing her panties and turned around again."
                    x "Beautiful... You're leaving me breathless, Cindy."
                    "She had been quiet for a while now, but she was reacting to Axel's words just like he wanted."
                    "He was guiding her into his world and he had taken full control of the situation."
                    "There was no way I could have kept my cool like he was doing having Cindy completely naked in front of me."
                    "I was barely keeping it together as I was, sitting at the other end of the room like a mere spectator..."
                    "But how could I? What I had been dreaming of was in front of my eyes..."
                    play sound "sfx/camera.mp3"
                    with flash
                    x "Look at me, Cindy. Don't hide away your eyes."
                    x "Don't shy away from the camera."
                    scene v5_cindy10
                    with long
                    "Guided by Axel's words, Cindy faced the camera and held her arms up."
                    "She wasn't hiding anything."
                    "She stood in front of us, beautiful and proud, delicate and sensual."
                    "I couldn't even blink while looking at her."
                    play sound "sfx/camera.mp3"
                    with flash
                    play sound "sfx/camera.mp3"
                    with flash
                    x "Yes, incredible..."
                    "Axel kept taking pictures of her for five or so more minutes while all I could do was watch from a distance."
                    "And what a spectacle Cindy was to watch..."
                    "I didn't know if I was glad of witnessing it or if I'd rather never seen it."
                    "I knew I could never see Cindy the same way now."
                    "Until now I had been able to fend off my timid desire for her, but now..."
                    "I couldn't lie to myself anymore. I wanted her."
                    "And that was a desire that could never come true. It shouldn't come true..."
                    $ fian = "blush"
                    $ faxel = "happy"
                    $ fcindy = "shy"
                    scene studio_pink
                    show ian at lef3
                    show cindynude2
                    show axel at rig3
                    with long
                    x "OK, I think we're done. I've got some incredible pictures."
                    c "Really?"
                    x "Yeah. I'm amazed at how well you performed, Cindy. I can't believe this was your first time."
                    x "I've worked with a lot of models, amateurs and pros, and you posed like a true pro."
                    c "No way. I had no idea what I was doing..."
                    x "Sometimes it's not about the knowledge. It's about the feeling."
                    c "Can I see the pictures?"
                    x "Of course."
                    c "Wait a minute, I'll go get dressed..."
                    hide cindynude2
                    with short
                    
                "That's enough":
                    $ renpy.block_rollback()
                    "Axel wasn't pulling any punches. He wanted Cindy completely naked in front of him."
                    "I told myself the reason I was there was to make sure Axel didn't do anything inappropriate, and he was going too far..."
                    $ cindy_look = "comfytopless"
                    $ fian = "n"
                    $ faxel = "n"
                    $ fcindy = "blush"
                    scene studio_pink
                    show ian at lef3
                    show cindybra2
                    show axel at rig3
                    with long
                    i "Remember, don't feel forced to do something you're not comfortable with, Cindy."
                    c "Um, yeah... I think like this is enough."
                    $ faxel = "smile"
                    x "Sure."
                    x "We can call it done. I've got some incredible pictures already."
                    c "Really?"
                    x "Yeah. I'm amazed at how well you performed, Cindy. I can't believe this was your first time."
                    x "I've worked with a lot of models, amateurs and pros, and you posed like a true pro."
                    c "No way. I had no idea what I was doing..."
                    x "Sometimes it's not about the knowledge. It's about the feeling."
                    c "Can I see the pictures?"
                    x "Of course."
                    c "Wait a minute, I'll go get dressed..."
                    hide cindybra2
                    with short
            
        "Dissuade her":
            $ renpy.block_rollback()
            "I told myself the reason I was there was to make sure Axel didn't do anything inappropriate, and I was pretty sure this qualified as something that was."
            "And I could see Cindy had doubts about what Axel was asking of her."
            "I shook my head silently while looking at Cindy, dissuading her."
            "If I were Wade, I wouldn't like it one bit if my girlfriend showed her tits to some guy who wanted to take pictures of her."
            scene v5_cindy7b
            with long
            c "This is as far as I feel comfortable with..."
            x "Of course... No problem."
            x "Don't worry, I wasn't expecting more, just as we talked... Let's keep it playful just like you are now."
            play sound "sfx/camera.mp3"
            with flash
            "This was erotic enough already..."
            "It was near impossible not to see Cindy as the sexy and beautiful woman she really was."
            "I was sure Axel had been hoping to see more, but sadly for him I had been there to intervene."
            "He kept taking a few more pictures and after five more minutes or so decided to call it done."
            $ fian = "n"
            $ fcindy = "shy"
            scene studio_pink
            show ian at lef3
            show cindybra2
            show axel at rig3
            with long
            x "OK, I think that's enough. I've got some incredible pictures already."
            c "Really?"
            x "Yeah. I'm amazed at how well you performed, Cindy. I can't believe this was your first time."
            c "I felt a bit awkward to be honest..."
            x "It's normal. Being in front of a camera can be quite intimidating, I know that."
            x "Still, you did so good for a newbie. I've worked with pro models that have less talent than you do."
            c "No way. I had no idea what I was doing..."
            x "Sometimes it's not about the knowledge. It's about the feeling."
            c "Can I see the pictures?"
            x "Of course."
            c "Wait a minute, I'll go get dressed..."
            hide cindybra2
            with short
    $ fian = "n"
    $ cindy_look = 1
    $ fcindy = "smile"
    $ cindy_look = 1
    show ian at lef
    show axel at rig 
    with move
# new text
    x "So, Ian, what did you think about the photoshoot?"
    i "Me?"
    x "Yes. It was your first inside look on one, right?"
    i "Oh, yeah."
    menu:
        "It was pretty interesting":
            $ renpy.block_rollback()
            $ fian = "smile"
            i "It was pretty interesting, to be honest. I was curious about it."
            x "I'm sure you found it way less glamorous than you expected, ha ha."
            i "Not really. I liked seeing the artistry of it."
            x "Of course, you're a writer. You must have good artistic sensibility."
            $ ian_axel += 1
            show friend_up
            play sound "sfx/friendup.mp3"
            i "I have no clue about photography, though."
            x "Between you and me, it's not that hard. Once you nail down the technical aspect of it it's a walk in the park."
            if v5_cindy_nude > 1:
                x "The model does half the job, if she's a good one, that is... And Cindy really surprised me."
                x "All the girls feel a bit awkward the first time they pose in front of the camera, but she was willing to step out of her comfort zone."
                x "You can tell she wants to push her boundaries." 
            elif v5_cindy_nude > 0:
                x "The model does half the job, if she's a good one, that is... And Cindy looks really promising."
                i "She looked a bit uncomfortable, though."
                x "All the girls feel a bit awkward the first time they pose in front of the camera, even the cheeky ones. It's normal."
                x "You did well reassuring her and reminding she didn't need to do anything she was uncomfortable with."
            else:
                x "The model does half the job, if she's a good one, that is... And Cindy looks really promising."
                i "Are you sure? I'm not sure Cindy was too comfortable with this." 
                x "All the girls feel a bit awkward the first time they pose in front of the camera, even the cheeky ones. It's normal."
                x "But you saw I didn't try to push her or anything. We worked strictly within the boundaries she set."
                
        "It was just how I imagined it":
            $ renpy.block_rollback()
            i "It was just how I imagined it. No mystery there."
            x "I guess there isn't too much to it, right? Point the camera at the model and shoot, ha ha."
            i "Pretty much."
            x "All I can do is make sure the lightning is good and the picture is in focus. But most a great deal depends on the model."
            if v5_cindy_nude > 1:
                x "And Cindy really surprised me."
                i "I'm sure she did..."
                x "All the girls feel a bit awkward the first time they pose in front of the camera, but she was willing to step out of her comfort zone."
                x "You can tell she wants to push her boundaries." 
            elif v5_cindy_nude > 0:
                x "And Cindy looks really promising."
                i "She looked a bit uncomfortable to me."
                x "All the girls feel a bit awkward the first time they pose in front of the camera, even the cheeky ones. It's normal."
                x "You did well reassuring her and reminding she didn't need to do anything she was uncomfortable with."
            else:
                x "And Cindy looks really promising."
                i "Are you sure? I'm not sure Cindy was too comfortable with this." 
                x "All the girls feel a bit awkward the first time they pose in front of the camera, even the cheeky ones. It's normal."
                x "But you saw I didn't try to push her or anything. We worked strictly within the boundaries she set."
       
        "It found it rather uncomfortable":
            $ renpy.block_rollback()
            $ fian = "n"
            i "If I'm being honest, I found it rather uncomfortable."
            if ian_axel > 3:
                $ ian_axel -= 1
                show friend_down
                play sound "sfx/frienddown.mp3" 
            x "Uncomfortable? How come?"
            i "I mean... Don't you feel awkward having a girl you barely know get naked in front of you?"
            x "Oh, you mean that. You get used to being around beautiful, naked women all the time in this business."
            x "At first it can be a bit intimidating, so I get how you feel. But after a while you come to see it just as work."
            "That answer sounded like bullshit to me..."
            i "If you say so... But I'm not sure Cindy was too comfortable with this."            
            x "All the girls feel a bit awkward the first time they pose in front of the camera, even the cheeky ones. It's normal."
            if v5_cindy_nude > 1:
                x "Cindy surprised me, though. She's willing to step out of her comfort zone and you can tell she wants to push her boundaries." 
            elif v5_cindy_nude > 0:
                x "You did well reassuring her and reminding she didn't need to do anything she was uncomfortable with."
            else:
                x "But you saw I didn't try to push her or anything. We worked strictly within the boundaries she set."
                
    x "In any case, sorry for imposing myself the other night at the bar."
    x "No man likes some random guy hitting up his girl when they are on a date."
    $ fian = "n"
    i "She's not my girl."
    x "I know she said you were her friend, but come on, don't tell me there's nothing between you two..."
    menu:
        "{image=icon_friend.png}Does it look like there is?" if ian_axel > 3:
            $ renpy.block_rollback()
            i "Does it look like there is?"
            x "That's the impression I got."
            $ fian = "smile"
            i "and yet you hiy her up? Should I be mad?"
            $ faxel = "happy"
            x "Ha ha, don't be. I would've gone a lot harder if my intention was to score with her."
            i "You said you were feeling a bit off that night."
            $ faxel = "smile"
            x "Yeah... So don't worry, I wasn't trying to steal her from you or anything."
            i "As I said... She's not my girl. She already has a boyfriend, in fact."
            x "Of course she has."
            
        "She belongs to Wade":
            $ renpy.block_rollback()
            $ fian = "serious"
            "I decided to issue a clear warning to Axel: there was a line that shouldn't be crossed."
            i "She already has a boyfriend. A good friend of mine."
            x "So that's how it is, huh?"
            $ ian_axel = 3
            show friend_down
            play sound "sfx/frienddown.mp3"
            x "The question is: how come you're here with her instead of him?"
            x "And why were you with her at the bar, and not her boyfriend?"
            $ fian = "sad"
            i "You should ask her about that."
            x "No need. I already know the answer."
        
        "We're just friends":
            $ renpy.block_rollback()
            i "There isn't. We're just friends."
            x "I see. I'm sorry, man."
            i "Sorry for what?"
            x "It sucks to be in the friendzone."
            $ fian = "worried"
            i "It's not like that... She already has a boyfriend, a friend of mine."
            x "Oh, so that's how it is. But how come you're here with her instead of him?"
            i "You should ask her about that."
            x "No need. I already know the answer."
     
    if ian_axel > 2:
        x "In any case, I apologize if I was rude or bothered you. Thanks for being cool about it."
        $ fian = "smile"
        i "It's OK."
        x "You seem like a cool dude to hang around with, Ian. Feel free to come with Cindy to the next photoshoot."
        i "I'll take you up on that offer."
    else:
        $ fian = "n"
    show ian at lef3
    show axel at rig3
    with move
    show cindy with short
    c "I'm done! Can I see the pictures you took?"
    $ faxel = "happy"
    x "Sure, let me show them to you on the camera."
    "Cindy seemed pretty pleased with how the photos turned out."
    c "Oh my God, I can't believe that's me. I do really look like a model..."
    x "I told you, you're perfect for this. It would be such a shame if you never posed again."
    $ fcindy = "shy"
    c "You really think so?"
    $ faxel = "smile"
    x "And wait until I've edited these pictures a bit... You'll look like a total pro."
    c "I can't wait to see them!"
    x "I'll send them to you soon. Let's keep in touch."
    c "Yeah!"    
    x "I'll stay and tidy up a bit around here. You two can be on your way."
    c "Thanks a lot, Axel!"
    x "No, thank you."
    i "Bye."
    stop music fadeout 2.0
    
    scene street
    with long
    $ fcindy = "smile"
    show ian at lef
    show cindy2 at rig
    with short
    if v5_cindy_nude > 0:
        "We left the studio. There was a somewhat awkward silence between us..."
    else:
        "We left the studio. Cindy looked quite happy."
    c "So... Thanks for tagging along."
    i "Did it make you feel more comfortable?"
    if v5_cindy_nude > 0:
        $ fcindy = "blush"
        c "I... I guess so..."
        c "I wasn't expecting to end up... You know..."
        $ fian = "blush"
        i "Uh, yeah... I guess you got a bit carried away."
        c "You think I got carried away?"
        i "No, I mean... You really got into it."
        if v5_cindy_nude > 1:
            c "That's good, isn't it? It's just like your friend Lena does. She also gets naked in front of the camera."
        else:
            c "That's good, isn't it? It's just like your friend Lena does, only she gets fully naked."
        "She was right. But this whole situation felt somewhat different to me."
        $ fian = "n"
        i "Sure... So tell me, did you like the experience?"
        $ fcindy = "shy"
        c "Yeah, I'd say I did... And Axel said I was a natural."
    else:
        c "Yeah, definitely."
        $ fian = "smile"
        i "I'm glad. It seems you enjoyed the experience..."
        c "Yeah! But I felt a bit awkward, still... I guess I'm a bit shy!"
        c "I don't know how Lena does it, getting naked in front of the camera..."
        $ fian = "n"
        i "I guess she's gotten used to it..."
        c "I wonder if I could do that, too. I want to try posing again, that much I know."
    c "Maybe I've found something cool I can really enjoy doing..."
    i "Do you think so?"
    c "Well, I need to see the pictures when he sends them to me... But I was amazed with what I saw just now."
    c "He really made me look like a pro model."
    $ fian = "n"
    i "I think most of the merit is yours..."
    c "Ah, stop it. You're gonna make me blush..."
    c "It was hard to concentrate with you staring at me the whole time!"
    i "Who else was I supposed to look at?"
    if v5_cindy_nude > 0:
        c "I can't believe I let you see all that!"
        $ fian = "shy"
        i "Uh, well... You could've told me to wait outside."
        c "Maybe I should've..."
    $ fcindy = "n"
    c "Anyways... I don't need to say it, but not a word to Wade about this..."
    $ fian = "n"
    i "I know, I know. You want to tell him yourself."
    c "Yeah."
    i "Oh, by the way. Has Jeremy told you about tomorrow?"
    c "Yeah! You're going to the club! I would love to go, but I can't..."
    c "Tomorrow's my grandmother's birthday and the whole family is getting together for dinner."
    i "Oh, I see."
    c "Next time! Talk to you soon, Ian! Bye!"
    $ fian = "smile"
    i "Goodbye."
    hide cindy2 with short
    show ian at truecenter with move
    $ fian = "n"
    i "..."
    i "Oh, boy..."
    if v5_cindy_nude > 1:
        "I had just seen Cindy completely naked. And I had a desire to do more than just that..."
        "I shook my head."
        i "What are you doing, Ian?"
        "I was suspicious of Axel, but my intentions were even worse."
    elif v5_cindy_nude > 0:
        "I had just seen Cindy's boobs. And I had a desire to see even more than that..."
        "I shook my head."
        i "I'm acting like a damn perv."
        "Things could've escalated even more if I hadn't intervened, though. I did the right thing speaking up against Axel's demands."
        i "I don't know if I can tell myself I'm being the good guy here, though... Most probably not."
    else:
        "Good thing I had been there. Who knows how things would've ended if I had left Cindy alone with Axel..."
        i "I don't know if I can tell myself I'm being the good guy here, though..."
    i "Time to go back home..."
    
##FRIDAY END ##################################################################################################################################################################################

label v5ianfridayend:
    
    scene ianhomenight
    with long
    $ fian = "n"
    $ ian_look = 2
    $ fperry = "n"
    "When Perry got back home I went and talked to him."
    play music "music/normal_day2.mp3" loop
    show ian at lef
    show perry at rig
    with short
    i "Hey, dude. We have plans for tomorrow."
    p "I know, Jeremy wants us to go to his club. Wade t--{w=0.5}told me."
    i "Are you coming?"
    $ fperry = "meh"
    p "Do you really have to ask that? No, I'm not."
    i "Come on, man, it's been ages since we went out clubbing. It can be fun."
    p "No, it c--{w=0.5}can't. I hate those places and the kind of people who go to those p--{w=0.5}places."
    i "It will be fun if all the gang gets together."
    p "Well, that's not happening. Wade and I will be h--{w=0.5}hanging out tomorrow night, and Cindy has plans, too."
    i "Damn... So it will only be Jeremy, me, Alison and Emma..."
    p "E--{w=0.5}Emma is coming?"
    $ fian = "confident"
    i "Yeah, she told me she's in."
    hide perry
    show perry2 at rig
    with short
    p "Mhh, I see."
    i "Are you sure you don't wanna re-think it?"
    p "No, I don't want to. I already made p--{w=0.5}plans with Wade. I'll be spending the night at his place, since Cindy will be with her family..."
    i "I'm sure Emma will be sad if you don't come."
    p "S--{w=0.5}stop it with the bullshit. You trying to blackmail me with Emma is p--{w=0.5}pathetic."
    menu:
        "{image=icon_friend.png}Try to convince Perry" if ian_perry > 3:
            $ renpy.block_rollback()
            $ v5_perry_feelings = True
            i "I'm not blackmailing you, just giving you some incentive to go out partying."
            p "I don't care, just stop it..."
            $ fian = "n"
            i "Dude, come sit down. Let's get serious."
            i "Why are you so against it? You need to get out of your comfort zone sometimes."
            p "That s--{w=0.5}sounds like something Jeremy would say."
            i "Maybe, and he would be right. I know you don't like clubs, I'm no big fan either. But it's important to be able to adapt."
            i "Especially when it could be your best chance to get closer to Emma."
            $ fperry = "mad"
            p "Again with that? How many times do I have to tell you, Emma's just a f--{w=0.5}friend..."
            i "Drop that bullshit already. Everyone knows you like her. You've liked her for a very long time."
            $ fperry = "meh"
            p "I like her, as a friend..."
            i "Stop trying to fool yourself, because you're not fooling anybody else. It's plain to see you like her more than just that."
            $ fian = "smile"
            i "And do you know what gives it away the most?"
            i "You never stutter when you talk to her. I'm sure you've noticed it."
            $ fperry = "sad"
            p "Well, I..."
            hide perry2
            show perry at rig
            with short
            i "Why are you so afraid of admitting it?"
            p "I--{w=0.5}it's..."
            p "It's something that could never happen. I don't want to m--{w=0.5}mess up our friendship."
            i "I'm not sure I see things as you do. You and Emma have a really good vibe together."
            p "But there's no way she sees me as anything more than just a friend."
            i "You don't know. You haven't brought it up with her."
            p "She hasn't brought it up with me, either."
            i "She's Emma, dude. You know how carefree and naive she is most of the time. But if you told her how you feel..."
            p "S--{w=0.5}she will say no."
            i "First of all, you can't be sure of that. And even if she said no, I doubt she'd change the way she treats you. She's easy-going like that."
            p "Even if that's the c--{w=0.5}case, I would be too embarrassed to keep acting normally with her..."
            i "I don't get it, man. What are you so embarrassed about?"
            p "If Emma saw the real me, she... She would probably d--{w=0.5}despise me."
            $ fian = "worried"
            i "What are you talking about?"
            p "You know me, man. I'm a fucking p--{w=0.5}perv."
            p "If she saw my browser history, the kind of porn I look at sometimes..."
            i "We all have seen some freaky shit on the internet, man."
            p "It's not just that. The t--{w=0.5}things I imagine doing with her... If I dared express those feelings she would be a--{w=0.5}appalled."
            i "What the hell do you imagine doing to her?"
            p "Well, not doing to her, but with her... I mean, there's some pervy stuff I wouldn't d--{w=0.5}dare ask of her."
            i "Like what? Pissing in her mouth or something like that?"
            p "I didn't say that!"
            p "Though I must admit I've jerked off to that kind of porn videos..."
            i "Dude, relax... I think you've been watching too much porn. When was the last time you got laid?"
            p "I don't know, maybe like... T--{w=0.5}two years ago or something like that."
            i "That's the problem. You're mixing up porn with real life."
            p "Maybe, but still... I doubt Emma could a--{w=0.5}accept me."
            i "Precisely Emma looks like the most open-minded and non-judgmental girl I've ever met. And I'm pretty sure she likes kinky stuff, too."
            p "How can you know that?"
            i "You know her even better than I do. Don't tell me you don't get that impression, too."
            p "I don't know, man... I never asked her..."
            p "C--{w=0.5}could you talk to her for me? Ask her a few questions, discretely of course..."
            i "Why don't you do that yourself? Come tomorrow, I can't think of a better moment to ask her about that stuff."
            p "There's no way I could ask her that! C--{w=0.5}come on, man, just help me out with that."
            p "You're my best friend..."
            menu:
                "{image=icon_charisma.png} Come to the club, dude!" if ian_charisma > 2:
                    $ renpy.block_rollback()
                    $ v5_perry_club = True
                    $ fian = "smile"
                    i "And that's why I'm telling you to come tomorrow!"
                    i "Don't be a pussy, man, you need to stand up for yourself at some point."
                    i "Emma won't respect you if you don't do that, and that's what you're afraid of. So grow a pair and go for it."
                    p "I don't know, man..."
                    i "I'll have your back, don't worry. I'm your friend, am I not?"
                    $ fperry = "n"
                    "Perry took a deep breath."
                    p "OK... I'll go. B--{w=0.5}but no promises on making a move on Emma."
                    $ fian = "happy"
                    i "Don't worry about that, just come, have a couple of beers and let things flow!"
                    p "I hope I won't have to regret this..."
                    $ fian = "smile"
                    i "I'll tell Jeremy you're coming, too."
                    
                "I'll talk to her for you":
                    $ renpy.block_rollback()
                    $ v5_emma_talk = True
                    $ fian = "n"
                    i "Alright... I'll talk to her for you."
                    $ fperry = "smile"
                    p "R--{w=0.5}really, will you do that?"
                    i "Yeah, yeah..."
                    if ian_perry < 10:
                        $ ian_perry += 1
                        play sound "sfx/friendup.mp3"
                        show friend_up
                    p "Thanks, man. Try to be s--{w=0.5}subtle, though..."
                    i "I know, I know. Don't worry, I'll test the waters and tell you how she feels about things."
                    $ fperry = "n"
                    p "And don't mention my name!"
                    i "Stop worrying. I'll see what I can find out and report back to you."
                    p "Alright."
                    i "Anyways, I'll tell Jeremy you're not coming."
                    
                "It's not my job":
                    $ renpy.block_rollback()
                    $ fian = "serious"
                    i "Whatever, man, it's not my job."
                    i "I've told you all I could. The ball's in your field now, if you want something to happen you have to make a move."
                    $ fperry = "serious"
                    p "B--{w=0.5}but I've told you a hundred times already, I like things as they are now!"
                    p "It's you who's constantly pushing me to make a move, but I d--{w=0.5}don't want to!"
                    if ian_perry > 3:
                        play sound "sfx/frienddown.mp3"
                        show friend_down
                        $ ian_perry -= 1
                    i "OK, I got it. I won't insist again, have things your way."
                    
            scene ianroomnight
            with short
            play sound "sfx/door.mp3"
            show ian with short
            
        "Don't insist":
            $ renpy.block_rollback()
            $ fian = "serious"
            i "Whatever dude, I was just trying to include you."
            i "If you don't wanna come, don't come."
            p "That's exactly what I'm t--{w=0.5}telling you."
            i "Have fun with Wade."
            scene ianroomnight
            with short
            play sound "sfx/door.mp3"
            show ian with short
            "It was impossible to convince him, and his attitude didn't make me wanna keep trying."
            "If he didn't wanna come so be it, we didn't really need him anyway."
            
    if v5_perry_club:
        "I texted Jeremy to tell him both Emma and Perry were in. He was quite surprised."
    else:
        "I texted Jeremy to tell him Emma was in but Perry had refused. He wasn't surprised."
    "He informed me that Alison would be joining us, too, but Wade and Cindy were out."
    if v5_cindy_shoot:
        "I already knew she had to attend her grandma's birthday, and Wade wouldn't tag along with us without having Cindy to drag him out."
    else:
        "It seemed Cindy had to attend her grandma's birthday, and Wade wouldn't tag along with us without having Cindy to drag him out."
    i "Anyways, I should do something productive before going to sleep."
    if ian_switch_review:
        "I told Holly I would help her with the extra book review Minerva had tasked her with. This mess had been my fault, to begin with."
        "I picked up the book and began reading. \"Competition of Hearts\" promised to be one of the worst books I had read since I began working at the magazine."
        i "This sucks, man..."
        "As I read an old idea flashed through my mind. I had been tempted to write an honest review bashing my previous assignment, \"Poker Love\"."
        $ fian = "evil"
        "Maybe I could do it now... Since I had to read this piece of crap and take notes for Holly, I could blow off some steam writing a hilarious review."
        "Minerva would never let such a review out to the public, but I could post it online myself..."
        "It was a small act of defiance, but it was all I could do at the moment."
        "Minerva could censor me in the magazine, but not on the Internet."
        "I created a social media account and a blog where I would post my honest reviews bashing the crap publishers were selling."
        i "This will could be fun..."
    elif ian_honest_review:
        "I had promised Holly to help her with the extra review Minerva had tasked her with because of me."
        $ fian = "evil"
        "I would read the book and write some notes she could use, but I would also write my own cruel and sarcastic review of this piece of crap."
        "I had posted my first review on-line and a few people had already read it. They weren't many, but all the comments were very positive and hilarious."
        "\"Competition of Hearts\" promised to be as bad as \"Poker Love\", or even worse."
        i "I'm gonna have some fun destroying this book... And I'm sure people who'll read it will get a good laugh."
        "This was my small act of defiance, but it was all I could do at the moment."
    else:
        "I had to read the book Minerva had assigned me and write another stupid review."
        i "Well, I gotta earn a living somehow... Even if it's boring and loathsome."
    play sound "sfx/sms.mp3"
    $ fian = "n"
    "I had just started reading when Holly sent me a text."
    i "Oh. Let's see what she says..."
    h "{i}Good evening, Ian. How was today at the office? Could you give your proposal to Mr. Ward?{/i}"
    if v5_hand_proposal:
        $ fian = "smile"
        i "{i}Yes, I did.{/i}"
        h "{i}Really? And how did he react? And Minerva, did she say anything?{/i}"
    elif v5_hand_proposal_lena:
        if v5_ian_showup:
            if ian_honest_review or ian_switch_review:
                i "{i}No, Lena told me she would do it, remember? I showed up at the office, though.{/i}"
            else:
                i "{i}No, Lena told me she would do it, remember? I just heard what Mr. Ward had to say.{/i}"
            h "{i}Oh, that's true. And how did it go? Were the rumors I heard true?{/i}"
        else:
            i "{i}No, Lena told me she would do it, remember?{/i}"
            h "{i}So you didn't go to the office?{/i}"
            i "{i}No, I didn't want to get in trouble...{/i}"
            h "{i}That's probably for the best... So you couldn't confirm if the rumors I heard were true...{/i}"
            i "{i}Nope. I'll ask around the office on Monday...{/i}"
            h "{i}I can ask somebody and let you know...{/i}"
    else:
        if v5_ian_showup:
            i "{i}No, I didn't... But I showed up at the office.{/i}"
            h "{i}Oh, you did? And how did it go? Were the rumors I heard true?{/i}"
        else:
            i "{i}No, I couldn't... I didn't show up at the office in the end. I didn't want to get into trouble.{/i}"
            h "{i}That's probably for the best... So you couldn't confirm if the rumors I heard were true...{/i}"
            i "{i}Nope. I'll ask around the office on Monday...{/i}"
            h "{i}I can ask somebody and let you know...{/i}"   
    menu:
        "{image=icon_friend.png}Ask Holly for a date" if ian_holly > 5:
            $ renpy.block_rollback()
            $ v5_holly_date = True
            if ian_go_holly == 0:
                $ ian_go_holly += 1
            $ fian = "smile"
            if v5_ian_showup:
                i "{i}Why don't we meet this weekend and I tell you everything face to face? {image=emoji_wink.png} {/i}"
                h "{i}I'd love that {image=emoji_smile} {/i}"
            else:
                i "{i}Anyways, thanks for telling me about the rumor and stuff. Can I repay you?{/i}"
                h "{i}There's no need!{/i}"
                i "{i}I was thinking we could hang out this Sunday, go for a walk or something.{/i}"
                h "{i}Oh, I'd love that {image=emoji_smile} {/i}"
            h "{i}When are you free?{/i}"
            i "{i}Tomorrow I'm going out with my friends, but how about Sunday afternoon?{/i}"
            if ian_holly < 10:
                $ ian_holly +=1
                play sound "sfx/friendup.mp3"
                show friend_up
            h "{i}OK! I'll write it in my agenda.{/i}"
            i "{i}See you on Sunday, then!{/i}"
            h "{i}{image=emoji_tongue.png} {image=emoji_tongue.png}{/i}"
        "Continue texting":
            $ renpy.block_rollback()
            if v5_ian_showup:
                "I told Holly how the day had played out "                      
                h "{i}I see! That was a bold move on your part!{/i}"
                i "{i}Do you think it will increase my chances of getting hired?{/i}"
                h "{i}It's hard to say... But at least you managed to stand out. I'm sure Mr. Ward will remember you the next time you two meet.{/i}"
                i "{i}Yeah, I hope so... At least it's something!{/i}"
                h "{i}And how are you feeling right now? What are you doing?{/i}"
            else:
                i "{i}Sure! Text me if you learn something from someone in the office.{/i}" 
            if ian_minerva_review:
                i "{i}Right now I'm reading the book Minerva gave me. It's even worse than I expected it to be!{/i}"
                h "{i}Stay strong! I'll leave you to it. See you on Monday!{/i}"
            else:
                i "{i}Right now I'm reading the extra book Minerva tasked you with, see if I can help you a bit with some notes.{/i}"
                h "{i}Oh, thanks! I'll leave you to it, then. See you on Monday!{/i}" 
            i "{i}Goodnight, Holly.{/i}"
    stop music fadeout 2.0
    "I kept reading for a while before finally going to bed."
    "Tomorrow was surely going to be an interesting day..."
    
## IAN SATURDAY MORNING ####################################################################################################################################################################

    $ day = "Saturday"
    scene blackbg
    with long
    call screen calendar
    scene ianroom
    with long   
    $ fian = "n"
    $ ian_look = 2   
    "I took my time getting up the next day."
    play music "music/normal_day2.mp3" loop
    show ian with short
    "Still, I had most of the day to myself. I could do a few things."
    if jiujitsu > 0:
        i "Wen said I should take training more seriously... I could use this morning to go to the gym and work out a bit."
    else:
        i "Yuri said I should take training more seriously... I could use this morning to go to the gym and work out a bit."
    i "Or I could work on my book. I shouldn't take too long to finish it, and there's still a ton of work to do..."
    i "But today's night will be long, so I better save up something for that."
    i "Maybe I should just take it easy and rest."
    menu:
        "Work on your book":
            $ renpy.block_rollback()
            $ v5_ian_morning = "write"
            i "My goal is to write a great book and have it published. I should use any chance I get to work on my dream."
            play sound "sfx/keyboard.mp3"
            scene ianroom
            show v2_ianwrite
            with long
            "I got in front of the computer, opened up my documents and notebooks and got to working."
            "It was work, but it was a very enjoyable work."
            "I wished my work at the magazine was like this... I could do this all day and be happy about it."
            "Writing was not just a job. It was passion and pleasure."
            "That didn't mean it was easy... Far from it, in fact. I had to put my brain to work and sink in a ton of hours to create something that was good."
            $ ian_wits_xp += 1
            play sound "sfx/xp.mp3"
            show wits_up
            call screen skillsup
            "I spent most of the day writing and only decided to rest a few hours before dinner."
            
        "Go to the gym":
            $ renpy.block_rollback()
            $ v5_ian_morning = "gym"
            i "I want to get in shape and become more active. Going to the gym is hard work, but hard work pays off..."
            play music "music/jeremys_theme.mp3" loop
            scene gym
            with long
            $ ian_look = 7
            "I grabbed my bag and headed to the gym."
            show ian with short
            i "It's the first time I'm here on a Saturday..."
            "There were more people there than I was expecting to find."
            i "They seem to take this very seriously... So should I."
            play sound "sfx/punching_bag.mp3"
            scene gym
            show v2_box
            with long
            "I began working on some technique on the heavy bag."
            if jiujitsu > 0:
                "I had decided to focus on Jiu Jitsu, but I still enjoyed throwing some combos."
            else:
                "I tried to get the fundamentals straight and replicate some of the combos Yuri had been drilling with me the other day."
            "I did that for a few minutes, until sweat began running down my neck. I already knew how hard this exercise could be."            
            scene v4_gym_ian with long
            "But if I wanted to improve I had to push myself harder."
            "I took off the boxing gloves and continued with my workout: push-ups, sit-ups, jumping jacks, ab crunches..."
            $ ian_athletics_xp += 1
            play sound "sfx/xp.mp3"
            show athletics_up
            call screen skillsup
            "I worked out until my head felt dizzy and my lungs were about to collapse."
            $ fian = "disgusted"
            scene gym
            show ian
            with long
            i "Damn, I'm at my limit... I hope I didn't overdo it."
            "Working out was torture, but it had to be done. No pain, no gain."
            "After so much exercise I was hungry as a wolf."
            stop music fadeout 2.0
            "I went back home, had a copious lunch and rested during the afternoon."
            
        "Rest":
            $ renpy.block_rollback()
            $ fian = "smile"
            i "It's Saturday, and weekends exist to take it easy, relax and have fun."
            i "I guess I'll stay home and play some video games with Perry."
            $ fperry = "n"
            play sound "sfx/door.mp3"
            scene ianhome
            show ian at lef
            show perry at rig
            with long
            i "Hey, I'm bored. Let's play some games."
            $ fperry = "happy"
            p "It was about time you asked me, Mr. Busy!"
            p "I'm gonna make you eat dirt, though."
            i "Don't be so sure, I'm still pretty good at this, you'll see."
            if ian_perry < 10:
                $ ian_perry += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            "I spent the day playing video games with Perry and procrastinating on the internet."
            "It's good for one's health to relax and have some fun from time to time."
            
    scene ianroomnight
    with long
    "Finally, the time to get ready arrived."
    $ ian_look = 2
    $ fian = "n"
    show ian with short
    "I opened my closet and searched for some clothes."
    i "I know I can't wear my hoodie to that club..."
    hide ian with short
    $ fian = "smile"
    $ ian_look = 3
    i "Let's see..."
    show ian with short
    i "I think this combination is pretty cool. Laid back but not too casual..."    
    if ian_charisma > 3:
        $ fian = "n"
        i "Maybe I could try something else, though... Let me see."
        hide ian with short
        $ fian = "smile"
        $ ian_look = "cool"
        i "I haven't used these pants in a while... Oh, and this shirt!"
        show ian with short
        i "This looks good!"
        i "A bit too tight, though. Not as comfortable as the other clothes..."
        i "What should I wear?"
        menu:
            "Open blue shirt":
                $ renpy.block_rollback()
                i "I'll stick with my first choice."
                hide ian with short
                i "I feel stupid changing clothes so much..."
                $ ian_look = 3
                show ian with short
                i "There. I feel more comfortable in these."
                
            "{image=icon_charisma.png}Tight red shirt" if ian_charisma > 3:
                $ renpy.block_rollback()
                $ v5_ian_cool = True
                i "I should definitely wear these tonight."
                i "We're going out to a fancy club, after all... And I look pretty handsome, if I might say so myself!"
    else:
        i "Yeah, this'll do."
    if v5_perry_club:
        $ fperry = "meh"
        play sound "sfx/door.mp3"
        scene ianhomenight
        show ian at lef
        show perry2 at rig
        with long
        i "Are you ready?"
        p "I guess."
        i "Damn dude, cheer up a bit! We're going out to have fun."
        p "I already told you I don't like those kind of p--{w=0.5}places. I still don't know how I let you convince me..."
        i "I didn't, Emma did, indirectly. You're looking forward to dancing with her, aren't you?"
        p "I hope you'll sh--{w=0.5}shut your mouth and don't make any stupid comments like that in front of her."
        i "Don't worry man, you know I have your back... I won't bother you two."
        play sound "sfx/ring.mp3" 
        i "Oh, Alison's ringing. She must be waiting outside."
        i "Let's go!"        
    else:
        play sound "sfx/door.mp3"
        scene ianhomenight
        show ian 
        with long
        i "Perry has already left. He said he would be spending the night at Wade's place."
        if v5_perry_feelings:
            $ fian = "n"
            i "That idiot... He's head over heels for Emma and won't move a finger."
            if v5_emma_talk:
                i "And I'm supposed to probe her and see how she feels about Perry and stuff..."
                i "I hope I don't make things messy. I should be careful."
            else:
                i "He won't get far with that attitude..."
        else:
            i "There was no chance of me convincing him to come tonight..."        
        play sound "sfx/ring.mp3" 
        $ fian = "smile"
        i "Oh, Alison's ringing. She must be waiting outside."
        i "Coming!"
    stop music fadeout 2.0
    $ falison = "n"
    $ alison_look = 2
    scene street2night
    with long
    if v5_perry_club:
        show ian
        show perry at lef3
        show alison at rig3
        with short
        a "There you are."
        i "Hey, Alison."
        p "Hey."
        a "Oh, you're coming too, Perry?"
        p "Yeah."
        a "And you're expecting to get in dressed like that?"
        p "Y--{w=0.5}yes."
        if v5_ian_cool:
            a "You're being a bit too optimistic... Look at Ian, he knows what's up!"
            $ falison = "flirt"
            a "You look so handsome in that shirt! Why don't you wear something like that more often?"
            i "I think it's the only one of this kind I have."
            $ falison = "n"
        else:
            a "You're being a bit too optimistic... And you too, Ian."
            $ fian = "n"
            i "What's wrong with my clothes?"
            a "I mean, they're OK, but... At least you're not wearing that brown hoodie!"
            i "I love that hoodie."
        a "Oh God... Remind me to take you out shopping one of these days!"
        a "Come on, let's go."
        p "W--{w=0.5}where's Emma?"
        i "She'll be meeting us there. Don't worry, she'll show up."
        
    else:
        show ian at lef
        show alison at rig
        with short
        a "Oh, there you are. Perry's not coming?"
        i "Nope."
        if v5_ian_cool:
            a "Of course... By the way, I love that shirt!"
            $ falison = "flirt"
            a "You look so handsome in it. Why don't you wear something like that more often?"
            i "I think it's the only one of this kind I have."
            $ falison = "n"
        else:
            a "Of course... By the way, are those the best clothes you have?"
            $ fian = "n"
            i "What's wrong with them?"
            a "I mean, they're OK, but... At least you're not wearing that brown hoodie!"
            i "I love that hoodie."
        a "Oh God... Remind me to take you out shopping one of these days!"
        i "Come on, let's go. Emma will be waiting for us there."
        
    scene streetnight
    with long
    $ fperry = "meh"
    $ fian = "smile"
    "We took a bus that dropped us right in front of the club."
    "There was already quite a big line to get in, even though it was pretty early."
    $ emma_look = 2
    $ femma = "n"
    $ jeremy_look = 1
    $ fjeremy = "n"
    
##CLUB WITH PERRY ######################################################################################################################################################

    if v5_perry_club:
        jump v5clubwperry
    else:
        jump v5clubwoutperry
        
label v5clubwperry:
    show ian
    show perry at lef3
    show alison at rig3
    with short
    a "Wow, this place sure is popular."
    p "Ugh, it will be packed full of people inside. It'll be like being in a can of sardines..." 
    $ falison = "serious"
    a "Seriously, if you're gonna be complaining all the time you should go back home."
    hide perry
    show perry2 at lef3 
    with short
    p "Maybe I will."
    $ fian = "worried"
    i "Chill, guys. We're here to have fun..."
    a "That's what I'm saying. I don't want to have someone bringing down the mood all the time."
    p "What, can't I express my opinions now?"
    a "I'd prefer you'd keep them to yourself tonight."
    i "Let's get in the line, guys..."
    "I hoped Emma would show up soon..."
    "Thankfully, she didn't make us wait for long."        
    e "Hey, guys!"
    hide perry2
    show perry at lef3
    with short
    show perry at left
    show ian at centerlef
    show alison at right
    with move
    $ fperry = "surprise"
    $ falison = "smile"
    $ fian = "surprise"
    show emma at rig with short
    "It took me a second to realize the girl I was looking at was Emma. But she definitely was."
    "I had never seen her wearing something like that, and never expected to."
    "She was wearing a small laced bustier, shorts and thigh-high stockings."
    e "Why are you looking at me like that, guys"
    $ fian = "worried"
    $ fperry = "sad"
    "Shit, had we been that obvious? I looked at Perry, and he didn't seem to know how to react."
    "Thankfully, Alison took us out of that bind."
    a "Damn Emma, you look killer tonight! So hot!"
    e "Really? Don't tell me it's too much!"
    a "No, it isn't, but we're not used to seeing you in this guise, at least not me!"
    $ fian = "smile"
    i "Yeah, I was surprised, too."
    $ femma = "smile"
    e "Enough already, you're gonna make me blush, guys!"
    p "I n--{w=0.5}never thought you'd like these kind of clothes."
    $ femma = "n"
    e "I don't know, you're supposed to dress like this in clubs, right?"
    e "I thought the top was pretty cute and I bought it some time ago, but today's the first time I'm wearing it."
    "Emma and Alison made some small talk about clothing and style as we moved forward through the line."
    "Perry and I were behind them. I looked at my flatmate: he couldn't wipe his shocked expression from his face."
    i "What's up, dude? You look like you've seen a ghost or something."
    p "..."
    "He didn't answer me. I noticed his eyes were fixed on Emma's ass, glued to it."
    $ fian = "happy"
    i "Earth calling to Perry. Are you still there, my friend?"
    p "Huh... Uh, yeah, yeah."
    i "Are you OK?"
    "He whispered so only I could hear what he was saying. The girls were too distracted by their own conversation to notice."
    p "No, I'm not. Look at Emma...!"
    i "What's the problem?"
    p "What's the p--{w=0.5}problem? She's so fucking hot!"
    i "I must confess she looks pretty sexy in those clothes..."
    p "I always thought she was cute, but this... T--{w=0.5}this is too much!"
    p "She'll have every guy in this club trying to s--{w=0.5}score with her! She's a Goddess! How am I s--{w=0.5}supposed to compete with that?"
    i "Calm down, man... That's all in your head."
    i "She's just Emma, treat her as you always do..."
    p "I d--{w=0.5}don't think I can go through with this..."
    $ fian = "n"
    "He was being way too dramatic, but I could sympathize with his feelings."
    "Emma's look shocked me, too, and she was already attracting some looks from horny guys."
    "We finally arrived at the front of the line, where the bouncer stopped us."
    show alison at right5
    show emma at rig5b
    show ian at lef5
    show perry at left5
    with move
    show bouncer with short
    bo "How many are you?"
    a "Four. We're Jeremy's friends, we should be on a list or something like that."
    bo "Jeremy's friends? Wait..."
    bo "Yeah, here you are. Four people. Come on in..."
    "Alison and Emma crossed the entrance, but when Perry and I were going to do so the bouncer stopped us."
    bo "Wait. You can't get in dressed like that."
    $ fian = "worried"
    $ fperry = "sad"
    $ femma = "sad"
    $ falison = "sad"
    p "Who, me?"
    if v5_ian_cool:
        bo "Yes. You in the red shirt are OK."
        i "I can't let my friend remain outside on his own."
        bo "Then you'll have to stay outside with him."
        a "Damn, I told you, Perry!"
        menu v5bouncer:
            "{image=icon_wits.png}Use logic" if ian_wits > 3:
                $ renpy.block_rollback()
                $ v5_bouncer_in = True
                $ fian = "n"
                if v5_ian_cool:
                    i "Look, I know my friend is not exactly following the dress code, but the place is full of people. Nobody will notice."
                    i "Besides, if you don't let him in, the girls will leave with us, and I'm sure many of these dudes will be disappointed."
                else:
                    i "Look, I know we're not exactly following the dress code, but the place is full of people. Nobody will notice."
                    i "Besides, if you don't let us in, the girls will leave with us, and I'm sure many of these dudes will be disappointed."
                "I pointed at the guys in the queue, who were probably dying to get laid that night at the club."
                bo "Hm..."
                "The bouncer grunted. He seemed annoyed at my banter, but I had the feeling he could be convinced."
                i "We'll keep him hidden, don't worry."
                bo "OK, just go in."
                i "Thanks, man."
                hide bouncer with short
                $ fperry = "n"
                $ falison = "n"
                $ femma = "smile"
                e "Nice save! That was some good reasoning."
                p "Thank you, Ian."
                if ian_perry < 10:
                    $ ian_perry += 1
                    play sound "sfx/friendup.mp3"
                    show friend_up
                a "If we're done wasting time, let's go inside!"
                jump v5clubwperry2
            
            "{image=icon_charisma.png}Befriend the bouncer" if ian_charisma > 3:
                $ renpy.block_rollback()
                $ v5_bouncer_in = True
                $ fian = "smile"
                i "Hey, I know you don't make the rules and you probably don't mind how we're dressed. Just doing your job..."
                bo "Exactly."
                if v5_ian_cool:
                    i "It's my friend's mistake. But maybe if he takes off the sweater and we keep my him out of sight you could let us in."
                else:
                    i "It's our mistake. But maybe if I button my shirt and we keep my friend out of sight you could let us in."
                i "We really need to, and I don't want to bother Jeremy and have him try and convince you to let us in. He's working, same as you."
                i "I know I'm being a bother, but you'd be doing us a solid if you let us in just this one time. Next time we'll dress properly, that's for sure."
                bo "Alright, just get in. People are waiting in line."
                i "Thanks, man."
                hide bouncer with short
                $ fperry = "n"
                $ falison = "n"
                $ femma = "smile"
                e "Nice save! You are a great diplomat!"
                p "Thank you, Ian."
                if ian_perry < 10:
                    $ ian_perry += 1
                    play sound "sfx/friendup.mp3"
                    show friend_up
                a "If we're done wasting time, let's go inside!"
                jump v5clubwperry2
                
            "{image=icon_pay.png}Bribe the bouncer" if ian_money > 0:
                $ renpy.block_rollback()
                $ v5_bouncer_in = True
                $ fian = "sad"
                i "Look, maybe if I pay for the entrance..."
                bo "{i}Tch{/i}... Whatever, OK. Pay up."
                "That money would probably go directly to the bouncer's pocket, since we were supposed to go in for free..."
                "A good old bribe."
                $ ian_money -= 1
                play sound "sfx/moneydown.mp3"
                show money_down
                "And an expensive one at that."
                hide bouncer with short
                e "What an asshole..."
                i "Damn, I will miss that money..."
                p "Sorry, dude. Thanks for that."
                if ian_perry < 10:
                    $ ian_perry += 1
                    play sound "sfx/friendup.mp3"
                    show friend_up
                i "I hope you'll invite me to a drink inside at least."
                p "Only if it's a beer..."
                a "If we're done wasting time, let's go inside!"
                jump v5clubwperry2
                
            "Beg to get in":
                $ renpy.block_rollback()
                if v5_ian_cool:
                    i "Please, let him in. We're on that list..."
                    bo "But he's not properly dressed. I don't make the rules. Now step aside."
                else:
                    i "Please, let us in. We're on that list..."
                    bo "But you two aren't properly dressed. I don't make the rules. Now step aside."
                i "But..."
                bo "Are you deaf? There's people waiting in line. Move."
                e "Don't worry, we'll go fetch Jeremy so he can fix this."
                a "Stay put."
                i "OK..."
                jump v5clubwperry2
                
    else:
        "The bouncer pointed at me, too."
        bo "You both."
        i "What?"
        a "I told you, guys!"
        jump v5bouncer
        
label v5clubwperry2:

    if v5_bouncer_in == False:
        hide alison
        hide emma
        hide bouncer
        with short
        show ian at lef
        show perry at rig
        with move
        "We moved aside as the girls went in, and we waited."
        $ fperry = "mad"
        hide perry
        show perry2 at rig 
        with short
        p "Can you see now why I don't like this kind of p--{w=0.5}place?"
        if v5_ian_cool:
            $ fian = "serious"
            i "It's your fault, man. It's not so hard putting on a shirt and a pair of decent shoes."
            p "But I don't want to."
            i "As I said, it's not so hard. And it's just this once."
            p "W--{w=0.5}whatever. It's just not my style and I don't like being forced into it."
            i "I can see that, that's why we're here now."
            p "..."
        else:
            $ fian = "sad"
            i "We should've been more careful when choosing our attire... Especially you."
            p "Hey, the bouncer didn't let you in e--{w=0.5}either. We're the same."
            i "At least I put some effort into it. You're just wearing your everyday sweater..."
            p "Whatever, man. P--{w=0.5}places like this are full of assholes, that's why I hate them."
            i "..."
        $ fian = "n"
        show ian at lef3
        show perry2 at truecenter
        with move
        show jeremy at rig3 with short
        "Finally, Jeremy showed up."
        j "Hey guys."
        i "What's up, Jeremy?"
        j "Dude, how the hell did you let Perry come here dressed like that?"
        j "Of course they won't let you guys in!"
        p "Hey, don't talk like I'm not even here."
        "Jeremy completely ignored his comment."
        if v5_ian_cool == False:
            j "And dude, your attire isn't much better..."
            i "Is it that bad?"
        j "Dude... I trusted your criteria a bit more. Anyways, I've talked to the bouncer."
        j "He'll let you guys in, but this will be the only and last time."
        j "You made me burn that card to save your ass, guys."
        if ian_jeremy > 2:
            $ ian_jeremy -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
        i "Thanks, man..."
       
    play music "music/dumb.mp3" loop
    scene blazer
    "We finally got into the club."
    "The music was loud and the place dark, pierced by laser and flashing lights."
    "The room was long and the ceilings high. To the right I could see the VIP area, furnished with leather couches, and to the left stood the dancing podiums."
    "What struck me the most were the poles attached to them. Nobody was using them, though."
    "We advanced to the bar and through the crowd. The dance floor was already quite packed."
    if v5_bouncer_in:
        $ fjeremy = "happy"
        show perry at left
        show ian at centerlef
        show alison at right
        show emma at rig 
        with short
        a "Let's find Jeremy first of all!"
        p "He said he would give us free drinks, right?"
        i "Let's go."
        "We made it to the end of the room, where the bar was."
        show alison at right5
        show emma at rig5b
        show ian at lef5
        show perry at left5
        with move
        show jeremy with short
        j "Hey guys! You made it!"
        $ falison = "smile"
        $ fperry = "n"
        $ fian = "smile"
        $ femma = "n"
        a "Yeah! Thanks for letting us in for free!"
        j "I told you, didn't I? Though you didn't do as I asked, Alison..."
        
    else:
        show ian at lef3
        show jeremy
        show perry at rig3
        with short
        j "This way."
        "We followed Jeremy to the end of the room, where the bar and the girls were."
        $ falison = "smile"
        $ fperry = "n"
        $ fian = "smile"
        $ femma = "n"
        $ fjeremy = "happy"
        show ian at lef5
        show perry at left5
        with move
        show alison at right5
        show emma at rig5
        with short
        j "Here we are."
        a "You managed to get them in!"
        j "Of course. I told you guys I would let you in for free."
        j "Though you didn't do what I asked, Alison..."
    
    a "What was that?"
    $ fjeremy = "flirt"
    j "You didn't dress sexy enough!"
    $ falison = "flirt"
    a "What, isn't this sexy enough for you? I'd say the bouncer liked it!"
    j "He sure did, ha ha. But look at Emma! She got the point!"
    $ fperry = "mad"
    $ femma = "smile"
    $ falison = "n"
    e "Now I really know I overdid it! Ha ha!"
    j "No, really, I didn't know you had such good taste when it comes to clothes!"
    e "Everybody seems so surprised. I guess I should dress up more often so you guys don't think I'm some kind of tomboy!"
    $ fperry = "meh"
    $ fjeremy = "happy"
    j "Anyways guys, what do you wanna drink? It's on me."
    p "A beer for me."
    j "Of course."
    "Jeremy served us what we asked, free of charge."
    j "So, it was about time you guys came to visit! What do you think about the place?"
    a "It's pretty cool! I expected it to be a bit bigger, though."
    j "There's a second area upstairs, through that corridor over there."
    a "Oh, I see!"
    $ fjeremy = "smile"
    j "Sorry guys, the bar's getting crowded and I have a ton of work to do. I'll catch you later."
    j "Now go and have fun!"
    e "Thanks, Jeremy!"
    hide jeremy with short
    show perry at left
    show ian at centerlef
    show alison at rig
    show emma at right
    with move    
    "We moved to the dance floor while sipping our drinks."
    "The music was loud and its simple, raw beat pounded my ears. Perry didn't seem too happy with it."
    p "Man, this music sucks."
    a "I like it!"
    p "For real? It's the d--{w=0.5}dumbest kind music one can think of."
    e "It's not my cup of tea either, but it can be fun to dance to!"
    p "Really? What do you think, Ian?"
    menu:
        "This is terrible":
            $ renpy.block_rollback()
            $ fian = "worried"
            if ian_chad > 0:
                $ ian_chad -= 1
            i "I should've brought earplugs!"
            i "Tonight is gonna be fucking tough, man..."
            p "See?"
            a "Why tough?"
            i "Because I don't think there's any amount of alcohol I can drink to make this music minimally bearable."
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup    
            a "Don't be stupid! You're just too tense!"
            i "Is having a taste called being tense, now? This is garbage compared to what I like to listen to."
            $ falison = "serious"
            a "Oh, shut up and stop being a downer."
            if ian_alison > 3:
                $ ian_alison -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
            a "The problem with you is that you don't know how to let go and enjoy things! You're the same as Perry!"
            p "Hey, what's that s--{w=0.5}supposed to mean?"
            "Maybe she had a point... But that simple, repetitive music was unenjoyable, no matter how much I let myself go."
            "I took a deep breath and gulped down my drink, wishing for the alcohol to kick in as fast as possible."
        
        "This is gonna be tough":
            $ renpy.block_rollback()
            i "This is gonna be tough... I'll need a few drinks to even begin to get into this."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            p "Same."
            p "In fact I fear... No, I {i}KNOW{/i} there's no amount of b--{w=0.5}beer I can drink to make this m--{w=0.5}music minimally bearable." 
            i "It's not exactly the kind of music we like to listen to, that's for sure."
            a "You two are such drama-queens!"
            p "It's called having a t--{w=0.5}taste, Alison!"
            a "The problem with you two is that you don't know how to let go and enjoy things!"
            "Maybe she had a point... But I would really need to make an effort to enjoy this beat."
            "I took a deep breath and gulped down my drink, hoping the alcohol would make things easier for me."
            
        "It's not so bad":
            $ renpy.block_rollback()
            if ian_chad < 5:
                $ ian_chad += 1
            $ fian = "sad"
            i "It's not so bad..."
            p "How can you say that with a s--{w=0.5}straight face, dude?"
            p "Oh, you're not even making a straight face..."
            a "He knows how to have fun, unlike you!"
            p "Or he's just pretending."
            a "Oh, shut up."
            "Perry wasn't completely wrong, though. This wasn't my kind of music, but I could make an effort and try to enjoy this."
            $ fian = "shy"
            "After all, I wouldn't mind seeing the girls bringing out their sexiest dance moves..."
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            "And Alison looked pretty fired up."
            $ fian = "smile"
            "I gulped down my drink, eager to get in that same state of mind."
    
    "Then I noticed some movement to my left. The go-go dancers were climbing on the podiums to perform some kind of show."
    $ fian = "surprise"
    "And one of them looked very familiar."
    scene v5_ivy1
    with long
    "It was impossible not to admire her: flowing and shiny bleached hair, sultry moves and a totally spectacular body."
    "And the outfit she was wearing... Sexy and revealing, it only made Ivy appear even more striking."
    "She began a dance routine, walking around the podium, holding the pole, swaying her entire body in sensual undulation."
    "In a matter of seconds, almost every guy had his head turned to her, me and Perry included."
    "She also caught Alison's end Emma's eyes, and she focused all of our attentions."
    p "Hey, is that the girl Jeremy t--{w=0.5}told us about?"
    i "Yeah... Her name's Ivy."
    "Ivy had become the center of attention of the entire club and her confident and playful smile showed she was well aware of that."
    "She played with her hair as her flirtatious dance moves synced to the rhythm of the beat with natural and fascinating ease..."
    scene v5_ivy2
    with long
    "And those moves were getting progressively more erotic and enticing."
    "She turned her back to us and stuck her ass out, shaking it."
    "The thong she was wearing left little to the imagination."
    "Her perfectly round and tight butt cheeks bounced up and down and side to side as Ivy proudly exhibited herself." 
    "She held the pole, bending her knees, erotically rubbing herself against the pole, her naughty smile ever present."
    "You could tell she enjoyed it... And so did most of her audience."
    scene v5_ivy3
    with long
    "Suddenly, Ivy held the pole and jumped."
    "Holding herself up, she spun around while extending her legs side to side."
    i "Wow."
    "Her silvery hair followed her movement like a flowing wave and the lights outlined the shapes of her perfectly toned body."
    "Ivy maneuvered around the pole, shifting from figure to figure. She made it look effortless and easy, and very, very sexy."
    a "You know this girl?"
    i "I just met her a couple of times when leaving the gym..."
    a "And she has something to do with Jeremy?"
    i "Not exactly..."
    p "He was trying to hook up with her but things didn't t--{w=0.5}turn out the way he wanted."
    a "Really?"
    e "I can't say I'm surprised! Look at her!"
    "Ivy continued with her routine for a few more minutes, and then stepped down from the podium."    
    $ fian = "smile"
    $ fperry = "surprise"
    $ femma = "smile"
    $ falison = "n"
    scene blazer
    show perry at left
    show ian at centerlef
    show alison at rig
    show emma at right
    with long    
    p "That was p--{w=0.5}pretty amazing."
    "It had been, no doubt about it..."
    e "That girl is incredible! I wish I could do that!"
    $ fperry = "n"
    a "I doubt we ever could! But at least we don't have to earn a living dancing half-naked in a night club!"
    e "You never know! Life can take you to unexpected places!"
    a "I know that very well! In my case it took my boss to jail and me to a new, shitty office."
    p "I'm done with my beer... Let's go get another one and check the other floor."
    i "Sounds good. I'm almost done with mine, too."
    stop music fadeout 2.0
    scene blazer
    with long
    play music "music/edm.mp3" loop
    "We went to see Jeremy for another round of drinks and then moved to the upper floor."
    "The music there was different, and even if it still wasn't my cup of tea, it was more palatable than the coarse and raunchy beats playing downstairs."
    scene v5_dance_perry
    if v5_ian_cool:
        show v5_dance_perry1
    else:
        show v5_dance_perry2
    with long
    "We did what we had come to do: dance."
    "I was halfway through my second drink and that was surely helping me let loose. Perry wasn't feeling the music at all."
    "On the other hand, the girls didn't seem to have any problem with enjoying themselves, dancing and smiling."
    "I was convinced women had some kind of natural ease when it came to dancing that we guys rarely possessed..."
    "But their good vibe was contagious and I found myself dancing with them, letting the beat guide me."
    menu:
        "{image=icon_charisma.png}Dance!" if ian_charisma > 2:
            $ renpy.block_rollback()
            "It had been a long time since I went out partying like this, and I felt the urge to move and dance!"
            "Shoving any shame aside, I let the music guide my body and danced with the girls."
            "The three of us were smiling and having a good time, giving everything on the dance floor."
            play sound "sfx/xp.mp3"
            show athletics_up
            $ ian_athletics_xp += 1
            call screen skillsup
            "I knew I could let loose with them. They were my friends and made me feel comfortable."
            "I could tell they were really into it and were having a lot of fun."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_emma += 1
            if ian_alison < 10:
                $ ian_alison += 1
         
        "Focus on Perry":
            $ renpy.block_rollback()
            "I moved closer to Perry. He was standing still, barely moving his feet next to us."
            i "Come on man, cheer up a bit!"
            p "Don't p--{w=0.5}pester me. I need my time to get into the right mood."
            i "I'd say it's a matter of beers rather than a matter of time."
            if ian_charisma < 4:
                play sound "sfx/xp.mp3"
                show charisma_up
                $ ian_charisma_xp += 1
                call screen skillsup
            p "Yes, and I need t--{w=0.5}time to drink that number of beers."
            "He finished the one he was holding with a long sip."
            
        "Focus on Alison":
            $ renpy.block_rollback()
            $ v5_ogle = "alison"
            "I watched Alison move next to me."
            "She wasn't the smoothest dancer. In fact, I'd even say she lacked the natural grace I had seen from other girls."
            "But she didn't really need that to appear attractive. She was tall and beautiful, and had a lovely smile..."
            "And her generous bust bounced up and down as she danced. It was hard not to look at her cleavage..."
            if ian_lust < 5:
                play sound "sfx/xp.mp3"
                show lust_up
                $ ian_lust_xp += 1
                call screen skillsup
            if ian_alison_sex:
                "And all seemed to indicate that I could end the night with my face shoved between those boobs!"
                if alison_jeremy:
                    "Jeremy seemed to be pretty busy after all, and I was pretty sure Alison wanted a piece of me tonight."
                "She noticed my gaze and came closer, talking loudly into my ear so I could hear her."
                a "You're looking at me an awful lot, Ian."
                i "That's because I like what I see."
                if ian_alison < 10:
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    $ ian_alison += 1
                a "Good to know, hee hee!"
            elif alison_jeremy:
                "Jeremy would probably enjoy those at the end of the night..."
            else:
                "Too bad I had blown my chance with her..."
            
        "Focus on Emma":
            $ renpy.block_rollback()
            $ v5_ogle = "emma"
            "I watched Emma move next to me. She was a great girl to be around, always positive and full of joy."
            "She danced in a carefree way, not trying to look sleek or sexy or anything. She just had fun with it." 
            "Still, it was hard not to appreciate her sensuality... She was rather short and thick, but in the right places..."
            "And those tight shorts made her butt really stand out. It was plump and bubbly, and the way it bounced was quite hypnotic..."
            if ian_lust < 5:
                play sound "sfx/xp.mp3"
                show lust_up
                $ ian_lust_xp += 1
                call screen skillsup
            "I felt a bit weird. I had never looked at Emma this way, but now I couldn't avoid it. No wonder Perry was interested in her..."
            "Emma saw me looking at her and smiled at me. I smiled back, trying not to look too awkward."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_emma += 1
            "I doubted she suspected what I was really thinking at that moment..."
            
        "Focus on yourself":
            $ renpy.block_rollback()
            "I closed my eyes and focused on myself, on the music and on my movements."
            "I tried to forget about everything else, the people surrounding me, the thoughts that plagued my head..."
            if ian_wits < 4:
                play sound "sfx/xp.mp3"
                show wits_up
                $ ian_wits_xp += 1
                call screen skillsup
            "I just wanted to feel the vibe and enjoy myself while sipping my glass."
    
    scene blazer
    show perry at left
    show ian at centerlef
    show alison at rig
    show emma at right
    with long
    a "I need to go to the bathroom, guys!"
    p "And I need to go get another beer."
    e "OK, we'll be right here!"
    hide perry
    hide alison
    with short
    show ian at lef
    show emma at rig
    with move
    "They went in different directions, leaving me and Emma alone."
    e "Are you having fun?"
    i "It's not as bad as I was fearing it would be!"
    e "It's who you're with that matters, really. With friends everything can be fun!"
    menu v5aloneemma1:
        "Dance with Emma" if v5_dancing_emma == False:
            $ renpy.block_rollback()
            $ v5_dancing_emma = True
            i "Well, shall we dance while we wait?"
            $ femma = "smile"
            e "Of course! That's what we came here for, isn't it?"
            if v5_ian_cool:
                scene v5_dance1_solo
            else:
                scene v5_dance2_solo
            show v5_dance1_emma
            with long
            "I was having fun with Emma and I wanted to keep it that way."
            "We could still chat while dancing. I got closer and talked to her ear."
            i "So, Emma..."
            jump v5aloneemma1
            
        "{image=icon_lust.png}Grind on Emma" if v5_dancing_emma and ian_lust > 2 and v5_emma_convo3 == False and v5_emma_grind == False or v5_dancing_emma and v5_ogle == "emma" and v5_emma_convo3 == False and v5_emma_grind == False:
            $ renpy.block_rollback()
            $ v5_emma_grind = True
            "I watched Emma dancing next to me."
            if v5_ogle == "emma":
                "My eyes hadn't ceased to admire Emma's butt... Those tiny shorts were barely containing it..."
            else:
                "She danced in a carefree way, not trying to look sleek or sexy or anything. She just had fun with it." 
                "Still, it was hard not to appreciate her sensuality... She was rather short and thick, but in the right places..."
                "And those tight shorts made her butt really stand out. It was plump and bubbly, and the way it bounced was quite hypnotic..."
            if v5_ian_cool:
                scene v5_emma1
            else:
                scene v5_emma1b
            with long
            "As we danced, I got behind Emma, rested my hands on her hips and pulled her towards me slightly."
            "Her butt made contact with my crotch and I started grinding carefully, following the movements of her hips."
            "I had the feeling she was a bit surprised, but didn't say anything and went with it. She wasn't hating it."
            "Neither was I, that was for sure..."
            "I was determined to help Perry with Emma, but I could at least enjoy a little dance, right?"
            jump v5aloneemma1    
        
        "Comment about Emma's clothes" if v5_emma_convo1 == False:
            $ renpy.block_rollback()
            $ v5_emma_convo1 = True
            i "You really look like a different person with these clothes."
            e "You guys are really shocked! I'm beginning to get worried, ha ha!"
            i "You can't blame us! We're not used to seeing you rocking a sexy outfit like this one!"
            e "Can't a girl dress up for a special occasion?"
            if v5_emma_grind:
                "When she said that she pressed her ass against my crotch, accentuating her grinding."
                "Damn, she had one fine ass..."
            i "Oh, so this is a special occasion for you?"
            e "Of course! When was the last time we went partying like this?"
            if v5_emma_convo1 and v5_emma_convo2:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_emma += 1
            e "Too bad Wade and Cindy couldn't come... But at least Perry showed up!"
            jump v5aloneemma1
        
        "Ask about Emma's relationships" if v5_emma_convo2 == False:
            $ renpy.block_rollback()
            $ v5_emma_convo2 = True
            if v5_emma_grind:
                "I pulled her closer, her back against my chest, and talked to her ear."
            i "What about your love life? Are you seeing someone? You're a total mystery sometimes..."
            e "I guess I don't talk too much about that, huh?"
            e "Well, I don't because there's not much to talk about. I don't have anything serious."
            i "But you have something?"
            e "Just a couple of guy friends. Sometimes we get intimate, but we're buddies, first and foremost."
            e "In fact, I haven't been seeing one of them for quite some time. I have the feeling he wants something more from me, and I can't give that to him."
            e "So I thought it's better if I get some distance from him."
            i "You don't want him to get any ideas... So you don't want a serious relationship?"
            e "I don't know. I guess I would, if the right guy showed up. But it's not something I worry about."
            e "I'm fine with my life as it is right now!"            
            if v5_emma_convo1 and v5_emma_convo2:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_emma += 1
            jump v5aloneemma1
            
        "Try to help Perry" if v5_emma_convo3 == False and v5_emma_grind == False:
            $ renpy.block_rollback()
            $ v5_emma_convo3 = True
            $ perry_emma += 1
            i "About Perry..."
            e "What about him?"
            i "Don't you think he's a bit stiff tonight?"
            e "He's always been shy!"
            i "I know. That's why we should help him loosen up a bit... You should help him."
            e "Me? Why me?"
            i "Because you're the only one who can!"
            e "You think so?"
            i "Of course... You and him have a very special relationship."
            e "Special? In what sense?"
            i "Well, I don't know if you've ever noticed... But the only time when he doesn't stutter is when he's talking to you."
            $ femma = "surprise"
            e "Really? Now that you mention it..."
            i "So, will you do me this favor?"
            if ian_charisma < 5:
                play sound "sfx/xp.mp3"
                show charisma_up
                $ ian_charisma_xp += 1
                call screen skillsup
            $ femma = "smile"
            e "Sure. Let's wait until he comes back with his beer!"
            jump v5aloneemma1
            
        "Wait for the others to come back":
            $ renpy.block_rollback()
            if v5_emma_grind:
                "We kept grinding close together until Alison came back."
            elif v5_dancing_emma:
                "We kept dancing and chatting until Alison came back."
            else:
                "We kept chatting and drinking until Alison came back."
            "Perry followed shortly after."
    $ fian = "smile"
    $ femma = "n"
    $ falison = "n"
    $ fperry = "n"
    scene blazer
    show perry at left
    show ian at centerlef
    show alison at rig
    show emma at right
    with long        
    a "Everything alright over here?"
    i "Yeah."
    a "I want to go get another drink. Come with me, Ian!"
    i "Sure, I finished mine too."
    e "Bring one for me, too!"
    hide emma
    hide perry 
    with short
    show ian at lef
    show alison at rig
    with move
    "We left Emma and Perry on the dance floor and walked through the crowd to the bar."
    a "Damn, it's full of people..."
    i "Jeremy is barely coping with all these people asking for drinks..."
    a "I guess we'll have to wait."
    $ falison = "flirt"
    a "So, tell me about the model. How's it going with her?"
    $ fian = "n"
    i "With Lena?"
    a "Yeah, yeah, Lena."
    if ian_alison_sex:
        "Why was she always so interested in that subject?"
        "It felt weird talking to her about it, considering the relationship Alison and I had been having..."
        
label v5clubalisontalk:
    menu:
        "We slept together" if ian_lena_sex:
            $ renpy.block_rollback()
            $ v5_tell_alison = "sex"
            $ fian = "shy"
            i "Well, we... We slept together the other day."
            a "Really? Look at you..."
            if ian_alison_sex:
                a "Such a player. Fooling around with two girls at the same time."
                $ fian = "smile"
                if alison_jeremy:
                    i "Look who's talking. Shall I remind you what you're doing with me and Jeremy?"
                    $ falison = "smile"
                    a "Oh, shut up. But you're right. I guess you and I are even more alike than we already thought, huh?"
                    a "We've both been through tedious relationships. I guess it's just normal we want to have some fun..."
                    a "You hadn't been with anybody since you broke up with Gillian, right?"
                else:
                    i "Does it bother you?"
                    $ falison = "n"
                    a "You can do whatever you want, I guess. It's not like it's my business, is it?"
                    i "I feel weird telling you this, but since you asked... I'm not gonna lie to you."
                    a "I can appreciate that. And it's not your fault all the girls are throwing themselves at you, right?"
                    a "You need to have some fun after all this time."
                    i "All this time?"
                    a "You hadn't been with anybody since you broke up with Gillian, right?"
            else:
                a "I always knew you had potential to be a ladies' man, and you're finally showing it!"
                $ fian = "smile"
                i "Was I doing so badly in the past?"
                $ falison = "n"
                a "No, Gillian was a good catch, real pretty and smart... Too bad it ended that way."
                a "You hadn't been with anybody since you broke up with her, right?"
            $ fian = "n"
            i "No... It's been a long year."
            $ falison = "n"
            a "A year already, huh? And have you heard from her during this time?"
                
        "We hooked up" if v4_ian_kiss:
            $ renpy.block_rollback()
            $ v5_tell_alison = "kiss"
            $ fian = "shy"
            i "Well, we hooked up just the other day..."
            a "You hooked up? You mean you slept with her?"
            if ian_lena_sex:
                "The truth was Lena and I had already had sex, and things looked pretty promising..."
                "But I felt no need to give Alison too much information. I wanted to keep some of my private life to myself..."
                if ian_alison_sex:
                    "And I didn't feel all too comfortable telling her about me and Lena, considering I was sleeping with Alison too."
            i "No, no... We just made out. But by the look of things, it's very probable we will..."
            a "Really? Look at you..."
            if ian_alison_sex:
                a "Such a player. Fooling around with two girls at the same time."
                $ fian = "smile"
                if alison_jeremy:
                    i "Look who's talking. Shall I remind you what you're doing with me and Jeremy?"
                    $ falison = "smile"
                    i "I haven't even slept with her yet. You can't say the same about him..."
                    a "Oh, shut up. But you're right. I guess you and I are even more alike than we already thought, huh?"
                    a "We've both been through tedious relationships. I guess it's just normal we want to have some fun..."
                    a "You hadn't been with anybody since you broke up with Gillian, right?"
                else:
                    i "Does it bother you?"
                    $ falison = "n"
                    a "You can do whatever you want, I guess. It's not like it's my business, is it?"
                    i "I feel weird telling you this, but since you asked... I'm not gonna lie to you."
                    a "I can appreciate that. And it's not your fault all the girls are throwing themselves at you, right?"
                    a "You need to have some fun after all this time."
                    i "All this time?"
                    a "You hadn't been with anybody since you broke up with Gillian, right?"
            else:
                a "You just need to push a bit harder. She seems like a cool girl, don't let her slide!"
                a "I always knew you had potential to be a ladies' man, and you're finally showing it!"
                $ fian = "smile"
                i "Was I doing so badly in the past?"
                $ falison = "n"
                a "No, Gillian was a good catch, real pretty and smart... Too bad it ended that way."
                a "You hadn't been with anybody since you broke up with her, right?"
            $ fian = "n"
            i "No... It's been a long year."
            $ falison = "n"
            a "A year already, huh? And have you heard from her during this time?"
            
        "Same as always" if v4_ian_date:
            $ renpy.block_rollback()
            $ fian = "n"
            i "Oh, same as always."
            if ian_lena_sex:
                "The truth was Lena and I had already had sex, and things looked pretty promising..."
                "But I felt no need to give Alison too much information. I wanted to keep some of my private life to myself..."
                if ian_alison_sex:
                    "And I didn't feel all too comfortable telling her about me and Lena, considering I was sleeping with Alison too."
            elif v4_ian_kiss:
                "Lena and I had made out on our last date, and things looked pretty promising..."
                "But I felt no need to give Alison too much information. I wanted to keep some of my private life to myself..."
                if ian_alison_sex:
                    "And I didn't feel all too comfortable telling her about me and Lena, considering I was sleeping with Alison too."
            if v2_kiss:
                a "What do you mean, same as always? You two already kissed, right?"
                i "Yeah, but that's the extent of it. At least for now."
                $ falison = "n"
                a "Hmm, weird. People don't normally take that long to take the first step nowadays, especially at our age..."
                if ian_alison_sex:
                    $ falison = "smile"
                    a "Look at us, for example! Ha ha."                
            else:
                $ falison = "n"
                a "What do you mean, same as always? Nothing new has happened?"
                i "We've been hanging out a couple of times, but no, nothing happened."
                a "Mhh... Maybe she's not interested?"
                if ian_alison_sex:
                    i "Who knows."
                    $ falison = "smile"
                    a "Well, don't worry! You have me, ha ha!"
            if ian_alison_sex:
                $ falison = "flirt"
                a "Though it seems you don't have enough with me so you have to pursue other girls..."
                if alison_jeremy:
                    i "Does that... bother you? You're doing it with Jeremy too, so..."
                else:
                    i "Does that... bother you?"
                $ falison = "n"
                a "It was a joke... It's not like it's my business to tell you who to be with, right?"
                a "I understand you need to have some fun after all this time. I do too."
                i "All this time?"
                a "We've both been through tedious relationships. And you hadn't been with anybody since you broke up with Gillian, right?"
            else:
                i "It's hard to know, honestly. You girls are complicated like that."
                a "Not all of us! Look at me, I'm so easy. Too easy, maybe..."
                a "In any case, you just need to learn to read the signs and be a bit bold. Take the first step!"
                a "You haven't been with anyone else since Gillian, right?"
                if ian_cherry_sex:
                    a "Well, except for Cherry." 
            $ fian = "n"
            i "No... It's been a long year."
            $ falison = "n"
            a "A year already, huh? And have you heard from her during this time?"
            
        "There's nothing between us" if v4_ian_date == False:
            $ renpy.block_rollback()
            $ fian = "n"
            i "Nah, I don't think there's anything between us."
            $ falison = "n"
            a "No? How come?"
            i "It seems she's in a complicated period on her life, and she's very busy..."
            i "Or she just doesn't like me, simple as that."
            if v2_kiss:
                a "But you kissed her, right?"
                i "Yeah, but it was just that, a kiss. We never followed up."
            else:
                a "But it didn't seem that was the case, right?"
            i "I guess there wasn't enough chemistry between us, after all."
            if ian_alison_sex:
                $ falison = "flirt"
                a "Well, thankfully you and me have a lot of chemistry, right? Hee hee."
                $ fian = "smile"
                i "That I can't deny..."
                a "It took us long enough to test that. It's been what, a year since you broke up with Gillian?"
            else:
                a "Sometimes it's hard to find someone who you can let loose with..."
                a "You haven't been with anyone else since Gillian, right?"
                if ian_cherry_sex:
                    a "Well, except for Cherry." 
            $ fian = "n"
            i "No... It's been a long year."
            $ falison = "n"
            a "A year already, huh? And have you heard from her during this time?"
            
        "Let's change the subject":
            $ renpy.block_rollback()
            $ fian = "n"
            i "Let's talk about something else, shall we?"
            $ falison = "serious"
            a "Why? I'm interested."
            if ian_alison_sex:
                i "I don't feel comfortable talking about that, considering the relationship you and I have..."
                a "You don't want to talk about how you're fooling around with two girls at the same time?"
                if alison_jeremy:
                    a "Don't worry, I'm doing the same with Jeremy, and I'm open about it."
                i "It's just that... I feel my personal life's been under too much scrutiny lately."
                i "I'd like to save some privacy."
                a "What, are you worried I will get mad? If I'm asking it's because I won't get offended by the answer, believe me."
            else:
                i "It's just that... I feel my personal life's been under too much scrutiny lately."
                i "I'd like to save some privacy."
                a "Really? I thought we were friends..."
                i "We are."
                a "Well, one tells that kind of things to one's friends. I tell you everything."
            i "As I said, let's change the subject, OK?"
            a "OK, OK."
            if ian_alison > 3:
                $ ian_alison -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
            $ falison = "n"
            a "So, since you don't want to talk about that..."
            a "What about Gillian? Have you heard from her again?"
            hide friend_down
    
    i "No, not really. We texted back and forth a bit a couple of months after breaking up, but it wasn't nice..."
    i "And when I stopped texting her she stopped texting me. And that was that."
    a "She was out of town doing her master's degree, right?"
    i "Yeah, but not far. She rented a place in a small city in the vicinity..."
    i "But whatever, I don't want to talk about her. Especially not now."
    a "Oh, of course. I thought you didn't care anymore. A whole year has gone by, after all..."
    i "I don't care... I just don't want to talk about it."
    a "Sure, sure."
    if alison_jeremy:
        i "What about you and Jeremy, by the way?"
        $ alison = "n"
        a "What about it?"
        i "Like, are you still seeing each other?"
        if ian_alison_sex:
            a "Oh, I don't know... I haven't really thought about it."
            a "We hooked up a couple of times, that's all..."
            if alison_voyeur:
                "\"Hooking up\" was too mild a way to describe it. I couldn't think of it as \"mild\" after that picture Jeremy had sent me..."
                "His cock between Alison's big boobs... Damn, that picture... It was hard looking at Alison's cleavage and not imagining Jeremy's cock sticking out."
                "And I worried about her making comparisons..."
            i "So, you're not interested in sleeping with him any more?"
            a "I don't know, not particularly!" 
            a "I mean, we both were bored, wanted to have some fun, you know how it goes..."
            i "Same as with me, right?"
            a "Yeah... Same thing, more or less..."
            a "In any case, it's not like I'm looking forward to hooking up with him again. Not that I disliked it..."
            $ falison = "flirt"
            a "But tonight I was hoping it was you who I hooked up with."
            $ fian = "smile"
            i "Sure..."
        else:
            a "Yeah, from time to time. When we have nothing better to do, you know."
            i "So nothing really serious going on, just passing the time?"
            a "Yeah, nothing serious! He's like the last guy I'd try to have something serious with, come on!"
            if alison_voyeur:
                "She didn't want to have a serious relationship, yet she let Jeremy take a picture of her boobs around his cock..."
                "Damn, that picture... It was hard looking at Alison's cleavage and not imagining Jeremy's cock sticking out."
            i "But you intend to keep hooking up with him."
            a "For now, yes. I know it'll end sooner or later, but right now it suits both of us, so..."
            a "Unless something... or someone who was really worth it approached me... I guess there's no reason to cut it short."
            i "Someone who's really worth it?"
            a "You know, someone I'd really like to have something a bit more serious with..."
            i "I thought you weren't looking for a relationship."
            a "I'm not saying that, but if that person showed some interest in me, I'd consider seeing where things go..."
            a "But one step at a time, you know. I've learned rushing things isn't always the best approach..."
            i "Hmm..."
    show ian at lef3 
    show alison at rig3
    with move
    $ fivy = "n"
    $ falison = "n"
    $ fian = "smile"
    show ivy with short
# new text
    $ ivy_look = "gogo"
    $ v5ivychat = False
    v "Make way."
    i "Oh, excuse me... Hey, Ivy."
    "She was rushing through the crowd, but me calling her name made her stop and look at me. Only then did she recognize me."
    if ian_ivy > 3:
        v "Oh, hey there Ian! I wasn't expecting to find you here."
    else:
        v "Oh, hey... Liam, was it?"
        $ fian = "n"
        i "Ian."
        v "Oh, yeah, sorry. Ian. I'm terrible with names."
    v "What are you doing at Blazer?"
    menu:
        "I'm not really sure":
            $ renpy.block_rollback()
            if ian_chad > 0:
                $ ian_chad -= 1
            $ fian = "n"
            i "I'm not really sure."
            v "You're not?"
            i "I'm not a big fan of places like this, to be honest..."
            if ian_chad > 0:
                $ fian = "smile"
                i "Though it's not too bad."
                v "Not too bad? Come on, this is the place to be!"
            else:
                v "Really? Come on, this is the place to be!"
            v "By far the best club in town!"
        
        "Jeremy invited us":
            $ renpy.block_rollback()
            i "Jeremy invited us."
            v "Oh, of course he did. Being  friends with the bartender at the best club in town has it's perks, huh?"
            $ fian = "smile"
            i "I'm not complaining, ha ha."
            
        "Hey, it's a free country":
            $ renpy.block_rollback()
            $ v5ivychat = True
            $ fian = "happy"
            i "Hey, it's a free country. And they say this is the best club in town, so I came to check it out."
            $ ian_charisma_xp += 1
            show charisma_up
            play sound "sfx/xp.mp3"
            call screen skillsup
            $ fivy = "flirt"
            v "Ha ha ha, you're right about that."
            v "It's not like I was complaining, though! You're welcome here anytime."
            $ fian = "smile"
            i "Thanks."
    
    a "Hi, I'm Alison."
    $ fivy = "n"
    v "Oh, hi. Ivy."
    a "I already know."
    v "Is that so? Has Ian told you about me?"
    a "He called you by your name just a second ago. But yeah, he told us about you when we saw you dancing."
    $ fivy = "flirt"
    hide ivy
    show ivy2 
    with short
    v "Oh, so you saw my performance?"
    i "Yeah we did..."
    menu:
        "{image=icon_charisma.png}+{image=icon_lust.png}It was super hot" if ian_charisma > 2 and ian_lust > 2 or ian_charisma > 2 and v5ivychat or ian_lust > 2 and v5ivychat:
            $ renpy.block_rollback()
            $ fian = "confident"
            i "It was super hot. You really impressed me, Ivy."
            $ fivy = "smile"
            v "Oh, really?"
            i "I mean, I know you get that a lot, but honestly, it was the best poledancing I had ever seen. You have some amazing moves!"
            $ fivy = "slut"
            v "I'm pretty proud of my moves... I'm glad you appreciate them."
            i "It's hard not to."
            $ ian_ivy += 1
            show friend_up
            play sound "sfx/friendup.mp3"
            v "I'll trust your compliment is sincere, then, hee hee. Thanks."
            a "It's clear you devoted a lot of time to mastering those {i}moves{/i}."
            $ fivy = "smile"
            hide ivy2
            show ivy
            with short
            v "What can I say? I love poledancing and it's profitable! I'm sure you enjoy whatever it is you're doing with your time... and with your life."
            $ falison = "serious"
            v "Anyway, I told Lena I saw you! She came here last night, by the way!"
            
        "It was cool":
            $ renpy.block_rollback()
            $ fian = "smile"
            i "It was really cool. Some of those moves were really impressive, you're really fit."
            v "Practice makes perfect, or so they say, and I've been practicing for quite some time."
            a "It's clear you devoted a lot of time to it."
            $ fivy = "smile"
            v "What can I say? I love it and it's profitable! I'm sure you enjoy whatever it is you're doing with your time... and with your life."
            $ falison = "serious"
            v "Anyway, I told Lena I saw you! She came here last night, by the way!"
            
        "Aren't you ashamed?":
            $ renpy.block_rollback()
            $ fian = "n"
            i "But... Aren't you ashamed?"
            $ fivy = "serious"
            hide ivy2
            show ivy
            with short
            v "What?"
            $ fian = "surprise"
            i "No, I mean... How do you do it to not feel embarrassed while on stage?"
            v "You think I should feel embarrassed?"
            a "It's not far fetched to think so."
            $ ian_ivy -= 1
            show friend_down
            play sound "sfx/frienddown.mp3"
            $ fian = "worried"
            i "That's not what I meant...! I'm just wondering how you can handle your shyness..."
            $ fivy = "n"
            v "Well, I'm just not a shy person."
            $ fian = "n"
            a "We noticed."
            v "Whatever. I told Lena I saw you! She came here last night, by the way."
            
    if v4_ian_date:
        i "She told me she had plans with you, but she didn't mention she was going out clubbing."
        v "Next time you could come together!"
        i "Maybe."
    else:
        i "Oh, I didn't know. Say hi to her for me."
    show ian at left
    show ivy at centerlef
    show alison at right
    with move
    $ faxel = "smile"
    $ axel_look = 2
    show axel at rig with short
    $ falison = "blush"
    x "Hey Ivy, there you are."
    v "Axel! You came!"
    if v5_cindy_shoot or v3_cindy_date:
        if ian_axel > 4:
            $ faxel = "happy"
        x "I said I would... Oh, hey there Ian! Funny meeting you here."
        if v5_cindy_shoot:
            x "Cool shooting the other day, huh?"
            if ian_axel > 4:
                x "I'd buy you a drink, but I think Ivy has something she wants do dicuss with me."
                v "Yeah."
                $ faxel = "smile"
                x "How do you two know each other, by the way?"
            else:
                i "I guess. All I did was watch."
        else:
            $ fian = "n"
            i "Yeah, such a coincidence..."
            x "I met Cindy the other day. We took some really cool pictures, has she shown you?"
            i "No, she hasn't..."
            x "So you know Ivy, too? How?"
            "She answered for me."
        v "He's friends with Jeremy, one of the bartenders." 
        x "I see."
        if v3_cindy_shoot and ian_axel > 4:
            v "Come on, let's go somewhere quieter where we can talk."
        else:
            x "Anyways, you wanted to discuss something with me, right?"
            v "Yeah. Let's go somewhere quieter."
    else:
        $ fian = "n"
        x "I said I would. So, you wanted to discuss something with me, right?"   
        v "Yeah. Let's go somewhere quieter."
    v "Bye, guys!"
    i "See you."
    hide ivy
    hide ivy2
    hide axel
    with short
    show ian at lef
    show alison at rig
    with move
    a "Who's that guy?"
    if v3_cindy_date:
        i "Cindy and I met him a couple weeks ago at a bar. He's a photographer."
        $ falison = "n"
        a "I see... You need to tell me the bars where you go to, ha ha!"
        i "In fact it was at Shine, the one you brought me and Perry to..."
    else:
        i "I don't know."
        a "..."
        $ falison = "n"
    a "Anyways, that girl, Ivy, she sure is weird."
    if ian_ivy > 4:
        i "I think she's cool."
        a "Yeah, I've noticed."
        i "What's that supposed to mean?"
        a "Nothing. I didn't know you liked that kind of girl."
        i "What kind?"
        a "You know what I mean."        
    elif ian_ivy > 3:
        i "She's peculiar. But she's cool."
        a " You think so? I didn't know you liked that kind of girl."
        i "What kind?"
        a "Never mind."    
    else:
        i "She's very different to you, that's for sure."
        a "Yeah, thankfully!"

    if v5_perry_club:
        jump v5clubwperry3
    else:
        jump v5clubwoutperry3
        
label v5clubwperry3:
    
    "Finally the bar cleared a bit and we could move forward."
    $ fjeremy = "smile"
    show ian at lef3
    show alison at rig3
    show jeremy with short
    j "Hey guys, sorry for the wait! Tell me what you want."
    $ fian = "smile"
    $ falison = "n"
    "Alison and I asked for our drinks and he poured them."
    j "I didn't spare on the alcohol. Enjoy them!"
    a "You're being really generous!"
    j "I like to take care of my friends!"
    i "Work is crazy over here."
    j "Saturday nights are very busy, yeah! But it's fun and I have the energy!"
    j "I need to get back serving drinks, but I will take a break in a bit."
    if alison_jeremy and ian_alison_sex == False:
        $ fjeremy = "flirt"
        j "I'll search for you guys then! Keep Alison's sweet ass from other guys until I'm there!"
        a "Ha ha, idiot. See you in a bit!"
    else:
        j "I'll search for you guys then!"
        a "See you in a bit!"
    hide jeremy with short
    "We picked up our drinks and went back to find Perry and Emma."
    scene v5_emma_perry with long
    $ perry_emma += 1
    "And we found a pretty interesting scene."
    "They were dancing together and having what seemed to be a lot of fun."
    "Perry's initial reluctance had melted away and now he was giving his everything, dancing enthusiastically."
    "Emma followed his funny and purposefully corny dance moves with ones of her own. I could tell they were having a blast by their smiles."
    "And they weren't shying away from physical contact. At times Emma was grinding on him and Perry was visibly loving it."
    a "Look at those two... Seems like they have a party of their own going on!"
    i "Yeah... I think it's best if we leave them to it."
    scene blazer
    show ian at lef
    show alison at rig
    with long
    a "Alright... What should we do, then?"    
    if ian_alison_sex:
        a "Oh, I know. Let's try and find someplace to sit. My feet are starting to hurt!"
        i "There were sofas on the lower floor."
        a "Let's go then!"
    else:
        a "Oh, I know, why don't we go check the lower floor again?"
        i "Sure..."
    stop music fadeout 2.0
    play music "music/dumb.mp3" loop
    "We went downstairs once more to the main area of the club."
    if ian_chad > 2:
        "The same kind of music had been playing there during the whole night... I preferred the other one, but I could cope with this."
        "The drinks I had were helping, too."
    else:
        "The same kind of music had been playing there during the whole night... It was definitely terrible."
        "Thankfully the drinks were helping me tolerate it, even if it was just a bit."
    if ian_alison_sex:
        jump v5alisonsex
    else:
        jump v5clubend
        
        
##NO PERRY ######################################################################################################################################################

label v5clubwoutperry:
    show ian at lef
    show alison at rig
    with short
    a "Wow, this place sure is popular."
    i "Let's get in the line before it gets even longer."
    $ falison = "flirt"
    a "So... When was the time you and I went out clubbing like this?"
    i "Hmm... I can't really remember. Closest was that other night with you and Cherry..."  
    if ian_alison_sex:
        if alison_jeremy:
            a "Oh, yeah, the night you ignored me..."
            $ fian = "n"
            i "What? I didn't ignore you."
            if v2_cherry_home:
                a "You didn't? Then how come you brought Cherry to your place instead of me?"
                $ fian = "shy"
                i "Well, that was... I guess there was just some chemistry between her and me."
                $ fian = "n"
                i "Same as with you and Jeremy..."
                $ falison = "n"
                a "Of course, you have that to counter-attack with..."
                a "But there's also chemistry between you and me, right?"
                $ fian = "smile"
                i "Yeah, most definitely. We've tested that out already."
                a "Hee hee, yeah, we did."
            else:
                $ falison = "n"
                a "It sure did feel that way..."
                i "Hey, it's you who was all over Jeremy the entire night."
                a "Oh, come on, you know it's not like that..."
                a "I mean, sure, we have some chemistry, but so do you and me, right?"
                $ fian = "smile"
                i "Yeah, I guess we do."
        elif v2_alison_home:
            a "Oh, yeah, that night..."
            if v2_ian_limp:
                a "I ended up in your room... And without clothes."
                $ fian = "insecure"
                i "Um, yeah... I just wish it could've ended in a better way, though."
                a "Well, we took care of that the other day, didn't we?"
                $ fian = "smile"
                i "We sure did..."
            else:
                $ falison = "slut"
                a "It ended in the best way possible, didn't it?"
                $ fian = "confident"
                i "Yeah, I guess it did."
                "Alison got closer to me. I felt her hand sliding down my thigh, perilously close to my crotch."
                a "I wonder if tonight will end the same way..."
                i "We'll have to wait and see..."
                $ falison = "flirt"
                a "I guess I can be a bit patient..."
    else:
        if v2_alison_home and v2_ian_limp:
            $ fian = "blush"
            i "Can we forget about that and pretend it never happened?"
            $ falison = "n"
            a "Alright, alright. Sorry to bring that up."
            a "I won't mention it again."
            i "Cool..."
            "Remembering how I had failed to get hard and show Alison a good time was a memory that never failed to make me cringe."
            "I just wanted to forget about it."
        if alison_jeremy:
            a "Oh, yeah, the night you ignored me..."
            $ fian = "n"
            i "What? I didn't ignore you."
            if v2_cherry_home:
                a "Oh, come on, you were hounding my friend Cherry all night long."
                $ fian = "shy"
                i "That's not true. I was just trying to make her feel comfortable, chatting her up..."
                a "And taking her to your place! What a naughty boy you are!"
                $ fian = "smile"
                i "Hey, you ended up in Jeremy's bed, so don't go pointing fingers."
                $ falison = "n"
                a "Well, he showed a lot of interest so... I let him take care of me!"
                i "I guess tonight will end the same way, then..."
                a "Who knows."
            else:
                $ falison = "n"
                a "No? I got that impression..."
                i "I'd say you were too busy with Jeremy to be able to tell something like that."
                a "I wasn't busy with him. He just showed a lot of interest in me, for some reason."
                i "\"For some reason\"? Really?"
                a "Ha ha ha, well, for the reason you and I know."
                i "He's been keeping on showing interest, as far as I know, right?"
                a "Yes, he has..."            

    e "Hey, guys!"
    show ian at lef3
    show alison at rig3
    with move
    $ falison = "smile"
    $ fian = "surprise"
    show emma with short
    "It took me a second to realize the girl I was looking at was Emma. But she definitely was."
    "I had never seen her wearing something like that, and never expected to."
    "She was wearing a small laced bustier, shorts and thigh-high stockings."
    e "Why are you looking at me like that, Ian?"
    $ fian = "worried"
    "Shit, had I been that obvious?"
    $ fian = "smile"
    i "Sorry, I was just surprised about your outfit!"
    e "Why? Don't tell me it's too much!"
    i "No, no, it's OK. Really sexy."
    a "Super sexy!"
    $ femma = "smile"
    e "Really? You're gonna make me blush, guys!"
    a "I'm surprised too! I never thought you'd like these kind of clothes."
    $ femma = "n"
    e "I don't know, you're supposed to dress like this in clubs, right?"
    e "I thought the top was pretty cute and I bought it some time ago, but today's the first time I'm wearing it."
    "Emma and Alison made some small talk about clothing and style as we moved forward through the line."
    "When we arrived at the front, the bouncer stopped us."
    show ian at left
    show emma at centerlef
    show alison at right
    with move
    show bouncer at rig with short
    bo "How many are you?"
    a "Three. We're Jeremy's friends, we should be on a list or something like that."
    bo "Jeremy's friends? Wait..."
    bo "Yeah, here you are. Three people. Come on in..."
    if v5_ian_cool == False:
        "Alison and Emma crossed the entrance, but when I was going to do so the bouncer stopped me."
        bo "Wait. You can't get in dressed like that."
        $ fian = "worried"
        $ femma = "sad"
        $ falison = "sad"
        i "Who, me?"
        bo "Do you see anyone else standing next to you?"
        menu:
            "{image=icon_wits.png}Use logic" if ian_wits > 3:
                $ renpy.block_rollback()
                $ v5_bouncer_in = True
                $ fian = "n"
                i "Look, I know I'm not exactly following the dress code, but the place is full of people. Nobody will notice."
                i "Besides, if you don't let me in, the girls will leave with me, and I'm sure many of these dudes will be disappointed."
                "I pointed at the guys in the queue, who were probably dying to get laid that night at the club."
                bo "Hm..."
                "The bouncer grunted. He seemed annoyed at my banter, but I had the feeling he could be convinced."
                i "I'll button my shirt and put in inside my pants."
                bo "OK, just go in."
                i "Thanks, man."
                hide bouncer with short
                $ falison = "n"
                $ femma = "smile"
                e "Nice save! That was some good reasoning."
                i "That was close... Thankfully he wasn't a complete asshole."
                a "I'm telling you, I need to take you shopping... Come on, let's go inside!"
                jump v5clubwoutperry2
                
            "{image=icon_charisma.png}Befriend the bouncer" if ian_charisma > 3:
                $ renpy.block_rollback()
                $ v5_bouncer_in = True
                $ fian = "smile"
                i "Hey, I know you don't make the rules and you probably don't mind how we're dressed. Just doing your job..."
                bo "Exactly."
                i "It's my mistake. But maybe if I button my shirt and put it inside my pants you could let me in."
                i "I really need to, and I don't want to bother Jeremy and have him try and convince you to let me in. He's working, same as you."
                i "I know I'm being a bother, but you'd be doing us a solid if you let me in just this one time. Next time I'll dress properly, that's for sure."
                bo "Alright, just get in. People are waiting in line."
                i "Thanks, man."
                hide bouncer with short
                $ falison = "n"
                $ femma = "smile"
                e "Nice save! You are a great diplomat!"
                i "That was close... Thankfully he wasn't a complete asshole."
                a "I'm telling you, I need to take you shopping... Come on, let's go inside!"
                jump v5clubwoutperry2
                
            "{image=icon_pay.png}Bribe the bouncer" if ian_money > 0:
                $ renpy.block_rollback()
                $ v5_bouncer_in = True
                $ fian = "sad"
                i "Look, maybe if I pay for the entrance..."
                bo "{i}Tch{/i}... Whatever, OK. Pay up."
                "That money would probably go directly to the bouncer's pocket, since we were supposed to go in for free..."
                "A good old bribe."
                $ ian_money -= 1
                play sound "sfx/moneydown.mp3"
                show money_down
                "And an expensive one at that."
                hide bouncer with short
                e "What an asshole..."
                i "Damn, I will miss that money..."
                a "I told you! I need to take you shopping... Come on, let's go inside!"
                jump v5clubwoutperry2
                
            "Beg to get in":
                $ renpy.block_rollback()
                i "Please, let me in. I'm on that list..."
                bo "But you aren't properly dressed. I don't make the rules. Now step aside."
                i "But..."
                bo "Are you deaf? There's people waiting in line. Move."
                e "Don't worry, we'll go fetch Jeremy so he can fix this."
                a "Stay put."
                i "OK..."
                jump v5clubwoutperry2
        
    else:
        $ v5_bouncer_in = True
    
label v5clubwoutperry2:       
    
    if v5_bouncer_in == False:
        hide alison
        hide emma
        hide bouncer
        with short
        show ian
        with move
        "I moved aside as the girls went in, and I waited."
        $ fperry = "sad"
        i "I should've been more careful when choosing my attire... But I thought I was good."
        $ fian = "serious"
        i "That bouncer sure is an asshole, though."
        i "..."
        $ fian = "n"
        i "I hope Jeremy manages to get me in."
        show ian at lef with move
        show jeremy at rig with short
        "After a few long minutes he showed up."
        j "Hey dude."
        i "What's up, Jeremy?"
        j "Dude... What were you thinking when picking those clothes?"
        i "Is it that bad?"
        "He sighed."
        j "I trusted your criteria a bit more, dude. Anyways, I've talked to the bouncer."
        j "He'll let you in, but this will be the only and last time."
        j "You made me burn that card, so I won't be able to help you next time."
        if ian_jeremy > 2:
            $ ian_jeremy -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
        i "Thanks, man..."
       
    play music "music/dumb.mp3" loop
    scene blazer
    "We finally got into the club."
    "The music was loud and the place dark, pierced by laser and flashing lights."
    "The room was long and the ceilings high. To the right I could see the VIP area, furnished with leather couches, and to the left stood the dancing podiums."
    "What struck me the most were the poles attached to them. Nobody was using them, though."
    "We advanced to the bar and through the crowd. The dance floor was already quite packed."
    if v5_bouncer_in:
        $ fjeremy = "happy"
        show ian at lef3
        show emma
        show alison at rig3
        with short
        a "Let's find Jeremy first of all!"
        i "Let's go."
        "We made it to the end of the room, where the bar was."
        show ian at left
        show alison at right
        show emma at rig
        with move
        show jeremy at centerlef with short
        j "Hey guys! You made it!"
        $ falison = "smile"
        $ fian = "smile"
        $ femma = "n"
        a "Yeah! Thanks for letting us in for free!"
        j "I told you, didn't I? Though you didn't do as I asked, Alison..."
        
    else:
        show ian at lef
        show jeremy at rig
        with short
        j "This way."
        "I followed Jeremy to the end of the room, where the bar and the girls were."
        show ian at left
        show jeremy at centerlef
        with move
        show alison at right
        show emma at rig
        with short
        j "Here we are."
        a "You managed to get him in!"
        j "Of course. I told you guys I would let you in for free."
        j "Though you didn't do what I asked, Alison..."
    
    a "What was that?"
    $ fjeremy = "flirt"
    j "You didn't dress sexy enough!"
    $ falison = "flirt"
    a "What, isn't this sexy enough for you? I'd say the bouncer liked it!"
    j "He sure did, ha ha. But look at Emma! She got the point!"
    $ femma = "smile"
    $ falison = "n"
    e "Now I really know I overdid it! Ha ha!"
    j "No, really, I didn't know you had such good taste when it comes to clothes!"
    e "Everybody seems so surprised. I guess I should dress up more often so you guys don't think I'm some kind of tomboy!"
    $ fperry = "meh"
    $ fjeremy = "happy"
    j "Anyways guys, what do you wanna drink? It's on me."
    a "Gin and tonic for me."
    j "Of course."
    "Jeremy served us what we asked, free of charge."
    j "So, it was about time you guys came to visit! What do you think about the place?"
    a "It's pretty cool!I expected it to be a bit bigger, though."
    j "There's a second area upstairs, through that corridor over there."
    a "Oh, I see!"
    $ fjeremy = "smile"
    j "Sorry guys, the bar's getting crowded and I have a ton of work to do. I'll catch you later."
    j "Now go and have fun!"
    e "Thanks, Jeremy!"
    hide jeremy with short
    show ian at lef3
    show alison at rig3
    show emma at truecenter
    with move
    "We moved to the dance floor while sipping our drinks."
    "The music was loud and its simple, raw beat pounded my ears. Perry wouldn't have been happy with it."
    a "The music's not bad!"
    i "I never knew you liked this kind of music..."
    a "It's fun to dance to!"
    e "It's not something I would listen to at home, but for a night of partying, sure, why not?"
    e "Don't you like it, Ian?"
    menu:
        "This is terrible":
            $ renpy.block_rollback()
            $ fian = "worried"
            if ian_chad > 0:
                $ ian_chad -= 1
            i "I should've brought earplugs!"
            i "Tonight is gonna be fucking tough, man..."
            $ femma = "smile"
            e "Ha ha, don't be so dramatic!"
            a "Why's it gonna be so tough?"
            i "Because I don't think there's any amount of alcohol I can drink to make this music minimally bearable."
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup    
            a "Don't be stupid! You're just too tense!"
            i "Is having a taste called being tense, now? This is garbage compared to what I like to listen to."
            $ falison = "serious"
            a "Oh, shut up and stop being a downer."
            if ian_alison > 3:
                $ ian_alison -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
            a "The problem with you is that you don't know how to let go and enjoy things! You're the same as Perry!"
            "Maybe she had a point... But that simple, repetitive music was unenjoyable, no matter how much I let myself go."
            "I took a deep breath and gulped down my drink, wishing for the alcohol to kick in as fast as possible."
            $ femma = "n"
        
        "This is gonna be tough":
            $ renpy.block_rollback()
            i "This is gonna be tough... I'll need a few drinks to even begin to get into this."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            a "You are such a drama-queen!"
            i "I'd say it's called having good taste."
            a "The problem with you is that you don't know how to let go and enjoy things!"
            "Maybe she had a point... But I would really need to make an effort to enjoy this beat."
            "I took a deep breath and gulped down my drink, hoping the alcohol would make things easier for me."
            
        "It's not so bad":
            $ renpy.block_rollback()
            if ian_chad < 5:
                $ ian_chad += 1
            $ fian = "sad"
            i "It's not so bad..."
            a "That's what I wanted to hear!"
            "This wasn't my kind of music, but I could make an effort and try to enjoy this."
            $ fian = "shy"
            "After all, I wouldn't mind seeing the girls bringing out their sexiest dance moves..."
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            "Alison looked pretty fired up, ready to shake that body, and Emma was into it, too."
            $ fian = "smile"
            "I gulped down my drink, eager to get in that same state of mind."
    
    "Then I noticed some movement to my left. The go-go dancers were climbing on the podiums to perform some kind of show."
    $ fian = "surprise"
    "And one of them looked very familiar."
    scene v5_ivy1
    with long
    "It was impossible not to admire her: flowing and shiny bleached hair, sultry moves and a totally spectacular body."
    "And the outfit she was wearing... Sexy and revealing, it only made Ivy appear even more striking."
    "She began a dance routine, walking around the podium, holding the pole, swaying her entire body in sensual undulation."
    "In a matter of seconds, almost every guy had his head turned to her, me included."
    "She also caught Alison's end Emma's eyes, and she focused all of our attentions."
    a "Who's that girl? Don't tell me you know her."
    i "Yeah... Her name's Ivy."
    "Ivy had become the center of attention of the entire club and her confident and playful smile showed she was well aware of that."
    "She played with her hair as her flirtatious dance moves synced to the rhythm of the beat with natural and fascinating ease..."
    scene v5_ivy2
    with long
    "And those moves were getting progressively more erotic and enticing."
    "She turned her back to us and stuck her ass out, shaking it."
    "The thong she was wearing left little to the imagination."
    "Her perfectly round and tight butt cheeks bounced up and down and side to side as Ivy proudly exhibited herself." 
    "She held the pole, bending her knees, erotically rubbing herself against the pole, her naughty smile ever present."
    "You could tell she enjoyed it... And so did most of her audience."
    scene v5_ivy3
    with long
    "Suddenly, Ivy held the pole and jumped."
    "Holding herself up, she spun around while extending her legs side to side."
    i "Wow."
    "Her silvery hair followed her movement like a flowing wave and the lights outlined the shapes of her perfectly toned body."
    "Ivy maneuvered around the pole, shifting from figure to figure. She made it look effortless and easy, and very, very sexy."
    a "You really know this girl?"
    i "I just met her a couple of times when leaving the gym with Jeremy..."
    a "And she has something to do with Jeremy?"
    i "Not exactly..."
    e "If that's the case, he's missing out! Look at her!"
    "Ivy continued with her routine for a few more minutes, and then stepped down from the podium."    
    $ fian = "smile"
    $ femma = "smile"
    $ falison = "n"
    scene blazer
    show ian at lef3
    show alison at truecenter
    show emma at rig3
    with long    
    e "That girl is amazing. I wish I could do that!"
    a "I doubt we ever could. But at least we don't have to earn a living dancing half-naked in a night club!"
    e "You never know! Life can take you to unexpected places!"
    a "I know that very well! In my case it took my boss to jail and me to a new, shitty office."
    i "Hey, why don't we go check out the other area?"
    a "Sure, and we can get another drink on the way there. I'm almost finished with mine!"
    stop music fadeout 2.0
    scene blazer
    with long
    play music "music/edm.mp3" loop
    "We went to see Jeremy for another round of drinks and then moved to the upper floor."
    "The music there was different, and even if it still wasn't my cup of tea, it was more palatable than the coarse and raunchy beats playing downstairs."
    if v5_ian_cool:
        scene v5_dance1
    else:
        scene v5_dance2
    with long
    "We did what we had come to do: dance."
    "I was halfway through my second drink and that was surely helping me let loose."
    "The girls didn't seem to need any help though. They were freely enjoying themselves, dancing and smiling."
    "I was convinced women had some kind of natural ease when it came to dancing that we guys rarely possessed..."
    "But their good vibe was contagious and I found myself dancing with them, letting the beat guide me."
    menu:
        "{image=icon_charisma.png}Dance!" if ian_charisma > 3:
            $ renpy.block_rollback()
            "It had been a long time since I went out partying like this, and I felt the urge to move and dance!"
            "Shoving any shame aside, I let the music guide my body and danced with the girls."
            "The three of us were smiling and having a good time, giving everything on the dance floor."
            play sound "sfx/xp.mp3"
            show athletics_up
            $ ian_athletics_xp += 1
            call screen skillsup
            "I knew I could let loose with them. They were my friends and made me feel comfortable."
            "I could tell they were really into it and were having a lot of fun."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_emma += 1
            if ian_alison < 10:
                $ ian_alison += 1  
                
        "Focus on Alison":
            $ renpy.block_rollback()
            $ v5_ogle = "alison"
            "I watched Alison move next to me."
            "She wasn't the smoothest dancer. In fact, I'd even say she lacked the natural grace I had seen from other girls."
            "But she didn't really need that to appear attractive. She was tall and beautiful, and had a lovely smile..."
            "And her generous bust bounced up and down as she danced. It was hard not to look at her cleavage..."
            if ian_lust < 5:
                play sound "sfx/xp.mp3"
                show lust_up
                $ ian_lust_xp += 1
                call screen skillsup
            if ian_alison_sex:
                "And all seemed to indicate that I could end the night with my face shoved between those boobs!"
                if alison_jeremy:
                    "Jeremy seemed to be pretty busy after all, and I was pretty sure Alison wanted a piece of me tonight."
                "She noticed my gaze and came closer, talking loudly into my ear so I could hear her."
                a "You're looking at me an awful lot, Ian."
                i "That's because I like what I see."
                if ian_alison < 10:
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    $ ian_alison += 1
                a "Good to know, hee hee!"
            elif alison_jeremy:
                "Jeremy would probably enjoy those at the end of the night..."
            else:
                "Too bad I had blown my chance with her..."
            
        "Focus on Emma":
            $ renpy.block_rollback()
            $ v5_ogle = "emma"
            "I watched Emma move next to me. She was a great girl to be around, always positive and full of joy."
            "She danced in a carefree way, not trying to look sleek or sexy or anything. She just had fun with it." 
            "Still, it was hard not to appreciate her sensuality... She was rather short and thick, but in the right places..."
            "And those tight shorts made her butt really stand out. It was plump and bubbly, and the way it bounced was quite hypnotic..."
            if ian_lust < 5:
                play sound "sfx/xp.mp3"
                show lust_up
                $ ian_lust_xp += 1
                call screen skillsup
            "I felt a bit weird. I had never looked at Emma this way, but now I couldn't avoid it. No wonder Perry was interested in her..."
            "Emma saw me looking at her and smiled at me. I smiled back, trying not to look too awkward."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_emma += 1
            "I doubted she suspected what I was really thinking at that moment..."
            
        "Focus on yourself":
            $ renpy.block_rollback()
            "I closed my eyes and focused on myself, on the music and on my movements."
            "I tried to forget about everything else, the people surrounding me, the thoughts that plagued my head..."
            if ian_wits < 4:
                play sound "sfx/xp.mp3"
                show wits_up
                $ ian_wits_xp += 1
                call screen skillsup
            "I just wanted to feel the vibe and enjoy myself while sipping my glass."
    
    "After a while, Alison stopped and told us she had to go to the bathroom."
    scene blazer
    show ian at lef3
    show alison at truecenter
    show emma at rig3
    with long    
    a "Emma, keep Ian company for me, will you?"
    e "Sure!"
    hide alison with short
    show ian at lef
    show emma at rig
    with move
    e "So, are you having fun?"
    i "It's not as bad as I was fearing it would be!"
    e "It's who you're with that matters, really. With friends everything can be fun!"
    if v5_emma_talk:
        "I was alone with Emma... This could be the right moment to do what Perry had asked me to."
        "But what the hell should I ask her?"
    menu v5aloneemma2:
        "Dance with Emma" if v5_dancing_emma == False:
            $ renpy.block_rollback()
            $ v5_dancing_emma = True
            i "Well, shall we dance while we wait?"
            $ femma = "smile"
            e "Of course! That's what we came here for, isn't it?"
            if v5_ian_cool:
                scene v5_dance1_solo
            else:
                scene v5_dance2_solo
            show v5_dance1_emma
            with long
            "I was having fun with Emma and I wanted to keep it that way."
            "We could still chat while dancing. I got closer and talked to her ear."
            i "So, Emma..."
            jump v5aloneemma2
            
        "{image=icon_lust.png}Grind on Emma" if v5_dancing_emma and ian_lust > 2 and v5_emma_grind == False or v5_dancing_emma and v5_ogle == "emma" and v5_emma_grind == False:
            $ renpy.block_rollback()
            $ v5_emma_grind = True
            "I watched Emma dancing next to me."
            if v5_ogle == "emma":
                "My eyes hadn't ceased to admire Emma's butt... Those tiny shorts were barely containing it..."
            else:
                "She danced in a carefree way, not trying to look sleek or sexy or anything. She just had fun with it." 
                "Still, it was hard not to appreciate her sensuality... She was rather short and thick, but in the right places..."
                "And those tight shorts made her butt really stand out. It was plump and bubbly, and the way it bounced was quite hypnotic..."
            if v5_ian_cool:
                scene v5_emma1
            else:
                scene v5_emma1b
            with long
            "As we danced, I got behind Emma, rested my hands on her hips and pulled her towards me slightly."
            "Her butt made contact with my crotch and I started grinding carefully, following the movements of her hips."
            "I had the feeling she was a bit surprised, but didn't say anything and went with it. She wasn't hating it."
            "Neither was I, that's for sure..."
            if v5_emma_talk:
                "I was supposed to help Perry get with her, but I could at least enjoy a little dance, right?"
                "Besides, this was not the moment to talk to her about Perry and all that..."
            else:
                "Look at what that stupid Perry was missing..."
            jump v5aloneemma2
            
        "{image=icon_friend.png}Inquire on Perry's behalf" if v5_emma_convo3 == False and v5_emma_talk:
            $ renpy.block_rollback()
            $ v5_emma_convo3 = True
            $ fian = "n"
            "Perry wanted me to test the waters, see if Emma would accept him. But at the same time he didn't want me to make it obvious he was interested."
            "How should I do this?"
            i "So, Emma, uhm..."
            i "I have a silly question, but I'd like to know your opinion."
            e "Sure, go ahead!"            
            i "What do you think about guys that are... let's say, quite pervy?"
            $ femma = "smile"
            e "Why are you asking me that?"
            i "It's for a... friend."
            e "A friend, sure... Well, if you must know, I don't really mind. I'd say I'm quite pervy myself!"
            $ fian = "smile"
            i "You are?"
            e "Sure. Pervy stuff is fun, don't you think so?"
            i "What kind of pervy stuff are we talking about, exactly?"
            e "Ha ha, are you really asking me that?"
            $ femma = "n"
            e "Well, you know... Dirty stuff like anal, or getting a bit rough too..."
            if v5_emma_grind:
                "Was it my imagination or had the way she was grinding her hips against me changed?"
                "It felt different, more sensual, more intimate..."
            "I wasn't sure I wanted to know that much about Emma's intimacies... But..."
            i "That sounds... quite freaky, yeah. But those things aren't that weird, after all..."
            e "I don't mind weird things, either. We're all weird in our own way."
            e "As long as there's a good understanding between two people they're free to explore whatever. And I don't mind trying new things!"
            e "I kinda like it, in fact."
            "OK, that was enough information. Too much, even."
            $ femma = "smile"
            e "So, happy with my answer?"
            i "Yeah, pretty happy..."
            if v5_dancing_emma:
                e "Are you sure you're asking for a friend? Or do you maybe have some dirty curiosity yourself? Ha ha."
                i "It's for a friend, I swear..."
                e "I see."
            jump v5aloneemma2
            
        "Comment about Emma's clothes" if v5_emma_convo1 == False:
            $ renpy.block_rollback()
            $ v5_emma_convo1 = True
            i "You really look like a different person with these clothes."
            e "You guys are really shocked! I'm beginning to get worried, ha ha!"
            i "You can't blame us! We're not used to seeing you rocking a sexy outfit like this one!"
            e "Can't a girl dress up for a special occasion?"
            if v5_emma_grind:
                "When she said that she pressed her ass against my crotch, accentuating her grinding."
                "Damn, she had one fine ass..."
            i "Oh, so this is a special occasion for you?"
            e "Of course! When was the last time we went partying like this?"
            if v5_emma_convo1 and v5_emma_convo2:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_emma += 1
            e "Too bad Perry, Wade and Cindy couldn't come..."
            i "Apart from Cindy, they could've come tonight. They just didn't want to."
            if v5_emma_grind:
                "She continued grinding on me."
                e "Well, it's their loss."
            jump v5aloneemma2
        
        "Ask about Emma's relationships" if v5_emma_convo2 == False:
            $ renpy.block_rollback()
            $ v5_emma_convo2 = True
            if v5_emma_grind:
                "I pulled her closer, her back against my chest, and talked to her ear."
            i "What about your love life? Are you seeing someone? You're a total mystery sometimes..."
            e "I guess I don't talk too much about that, huh?"
            e "Well, I don't because there's not much to talk. I don't have anything serious."
            i "But you have something?"
            e "Just a couple of guy friends. Sometimes we get intimate, but we're buddies, first and foremost."
            e "In fact, I haven't been seeing one of them for quite some time. I have the feeling he wants something more from me, and I can't give that to him."
            e "So I thought it's better if I get some distance from him."
            i "You don't want him to get any ideas... So you don't want a serious relationship?"
            e "I don't know. I guess I would, if the right guy showed up. But it's not something I worry about."
            e "I'm fine with my life as it is right now!"            
            if v5_emma_convo1 and v5_emma_convo2:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_emma += 1
            jump v5aloneemma2
            
        "Wait for Alison":
            $ renpy.block_rollback()           
            
    if v5_emma_grind:
        menu:
            "Keep grinding":
                $ renpy.block_rollback()
                "We kept dancing, grinding on each other more and more comfortably."
                "Emma rubbed her butt against my crotch while I held her close by the hips..."
                play sound "sfx/xp.mp3"
                show lust_up
                $ ian_lust_xp += 1
                call screen skillsup
                "I had to admit it. That situation was getting me pretty horny..."
                "I had never thought of Emma as anything other than a good friend. Just another buddy of mine."
                "But feeling her thick ass grinding against my crotch, feeling her hips move swiftly side to side, was giving me a whole new perspective on things..."
                "I wondered if she could feel my dick bulging underneath my pants. It was fully erect at this point, she had to be feeling it..."
                "Yet she continued to move, pursuing as much physical contact as possible with me..."                
                menu:
                    "Kiss her":
                        $ renpy.block_rollback()
                        $ ian_emma_sex = True
                        jump v5emmasex
                        
                    "Stop":
                        $ renpy.block_rollback()
                        "But no... This just felt weird. Emma and I were just friends."
                        "Doing anything that went beyond that was... just not something I should do."
                        "Especially considering Perry was into her."
                        "I took some distance and told Emma I was feeling tired. Thankfully, Alison arrived just at that moment."
                
            "Stop dancing":
                $ renpy.block_rollback()
                "That was enough dancing, though."
                "I wanted to stop before things turned weird. Or I should say, weirder..."
                "I took some distance and told Emma I was feeling tired. Thankfully, Alison arrived just at that moment."
                
    elif v5_dancing_emma:
        "We kept dancing and chatting until Alison came back."
    else:
        "We kept chatting and drinking until Alison came back."
    $ fian = "smile"
    $ femma = "n"
    $ falison = "n"
    scene blazer
    show ian at lef
    show emma at rig
    with long
    show ian at lef3
    show emma at rig3
    with move
    show alison with short
    i "Hey, Alison"
    a "Here you go."
    "She handed me a brand new drink. She had one for herself, too."
    a "Sorry Emma, I wasn't brave enough to carry three glasses through all these people."    
    e "Don't worry! Now's time for me to go to the bathroom and get myself another drink!"
    a "We'll be waiting right here!"
    hide emma with short
    show ian at lef
    show alison at rig
    with move
    a "So, all good over here? Having fun?"
    i "Funny, Emma asked me the same. How do I look like?"
    $ falison = "smile"
    if v5_ian_cool:
        a "Handsome. That red shirt really suits you, hee hee."
    else:
        a "You're looking pretty fine to me, ha ha."
    i "Well, thank you..."
    $ falison = "flirt"
    a "So, tell me, Mr. Handsome. What about that model? How's it going with her?"
    $ fian = "n"
    i "With Lena?"
    a "Yeah, yeah, Lena."
    if ian_alison_sex:
        "Why was she always so interested in that subject?"
        "It felt weird talking to her about it, considering the relationship Alison and I had been having..."
    jump v5clubalisontalk
    
label v5clubwoutperry3:
    
    if ian_alison_sex:
        a "Where's Emma, by the way? She's taking a long time."
        i "Look, there she is."
        "Emma was talking to some people."
        "She wasn't far, talking with a group of two guys and a girl. I couldn't hear what they were saying, but all of them were laughing."
        a "She made some new friends already."
        i "Always happens with her. She's just friendly and easy-going like that."
        a "Sometimes I just don't get her. She's so different from me."
        a "Hey, since she's busy, let's try and find someplace to sit. My feet are starting to hurt!"
        i "There were sofas on the lower floor."
        a "Let's go then!"
        jump v5alisonsex    
    else:
        jump v5clubend
    
    
##CLUB END #############################################################################################################################################################################################

label v5clubend:
    
    $ v5_alison_jeremy = True
    
    if v5_perry_club:
        "Jeremy found us just at that moment."
        show ian at lef3
        show alison at rig3
        with move
        show jeremy with short
        j "Hey, guys!"
        a "Are you on your break?"
        j "Yeah, I have someone covering for me. Where are Emma and Perry?"
        i "They're upstairs, having fun on their own."
        $ fjeremy = "flirt"
        j "Oh, so he has finally decided to make a move?"
        i "Doesn't seem like it... Not yet at least. But I think he's getting closer."
        j "Let's see how the night ends for them!"
        a "I always thought they'd make a good couple. They're different from each other, but in a way that compliments them."
        $ fjeremy = "smile"
        j "I don't know about that. I just know Perry's had the hots for her for the longest time!"
        j "Oh, and speaking about having the hots... Do you know who was here last night?"
        $ fian = "n"
        i "Lena."
        j "Oh, so you know?"
        i "I stumbled upon Ivy before and she told me."
        j "So yeah, your friend Lena came by."
        a "Seems like this girl is everywhere."
        if alison_jeremy:
            j "Ivy invited her to come and she brought Lo--... She brought a friend of hers."
            "Jeremy refrained from talking about his so-called girlfriend in front of Alison."
            a "So, a busy night for you?"
            j "Not as busy as this one!"
        else:
            $ fjeremy = "sad"
            if louise_jeremy == False:
                j "She came with Louise... What a mess that was."
                i "What happened?"
                j "I'll tell you some other time..."
            else:
                j "She came with Louise.  The night didn't end as I hoped, though... She got really wasted."
            a "Louise? Who's this Louise?"
            i "A girl Jeremy was sweet on."
            a "Another one, huh?"
            $ fjeremy = "smile"
            j "Ha ha ha!"
        j "Guys, I'm tired! Let's find some place to sit down."
        a "Yes, please! My feet hurt."             
        if alison_jeremy:
            scene v5_alison1c with long
            "We found a small space on a couch and sat down."
            "There was only room for two of us, so Alison sat on Jeremy's lap."
            "As we made some small talk, I could see them openly flirting. They were barely paying any attention to me. I wasn't that talkative, to be honest."           
            "It was pretty late already, and as the effects of the alcohol began wearing away I started to feel a bit tired and sleepy."
            "And Alison and Jeremy clearly looked like they wanted to be alone... I had no interest in being a third wheel."
            "It was time for me to go home."
            $ fian = "n"
            $ falison = "flirt"
            scene blazer
            show ian at lef3
            show jeremy
            show alison at rig3
            with long
        else:
            "It was pretty late already, and as the effects of the alcohol began wearing away I started to feel a bit tired and sleepy."
            "We made some small talk, but Jeremy was monopolizing Alison's attention."
            "I felt a bit left out of the conversation, and honestly I wasn't too interested in taking part. It was time for me to go home."
            $ fian = "n"
        i "Hey guys, I'm leaving. I'm gonna try to find Emma and Perry, see if they are still around here."
        j "Sure, bro. I hope you had fun."
        $ fian = "smile"
        i "Yeah, man, thank you for inviting us. We didn't spend a penny tonight!"
        j "Next time I'll try and party with you guys!"
        stop music fadeout 2.0
        scene streetnight with long
        show ian with short
        "I left the club and texted Perry. Turned out they had just left a few minutes ago."
        i "Seems like it went well for him..."
        "I waited for the night bus and made the trip back home on my own."
        
    else:
        show ian at left
        show alison at right
        with move
        show emma at centerlef
        show jeremy at rig
        with short
        "Just then Emma showed up, and Jeremy was with her."
        e "Hey guys, look who's joining us!"
        a "Are you on your break?"
        j "Yeah, I have someone covering for me. Are you guys having fun?"
        a "Yes! And we haven't spent a penny!"
        j "As I said, I like to take care of my friends! You're welcome anytime!"
        j "Too bad Wade and Perry don't appreciate my hospitality, those bastards..."
        e "When we tell them how much fun this was they will re-think their position!"
        j "Oh, Ian... Do you know who was here last night?"
        $ fian = "n"
        i "Lena."
        j "Oh, so you know?"
        i "I stumbled upon Ivy before and she told me."
        j "So yeah, your friend Lena came by."
        if v2_ian_date:
            e "The girl I saw you with at the record store, right? She was so beautiful!"
        a "Seems like this girl is everywhere."
        if alison_jeremy:
            j "Ivy invited her to come and she brought Lo--... She brought a friend of hers."
            "Jeremy refrained from talking about his so-called girlfriend in front of Alison."
            if louise_jeremy == False:
                $ fjeremy = "sad"
                j "What a mess that was..."
                i "With Lena?"
                j "No, with her friend and... Well, I'll tell you some other time."
                $ fjeremy = "smile"
            a "So, a busy night for you?"
            j "Not as busy as this one!"
        else:
            $ fjeremy = "sad"
            if louise_jeremy == False:
                j "She came with Louise... What a mess that was."
                i "What happened?"
                j "I'll tell you some other time..."
                a "Louise? Who's this Louise?"
                j "It's, uh... you could call her my ex-girlfriend."
                $ fian = "worried"
                i "Ex-girlfriend? Since when?"
                j "Since yesterday. But I don't wanna talk about it now. I'll tell you some other time."
                $ fjeremy = "smile"
                a "Oh, now that it was getting interesting..."
            else:
                j "She came with Louise. Damn, and she got really wasted..."
                a "Louise? Who's this Louise?"
                i "A girl Jeremy is sweet on."
                a "Another one, huh?"
                $ fjeremy = "smile"
                j "Ha ha ha!"
        j "Guys, I'm tired! Let's find some place to sit down."
        a "Yes, please! My feet hurt."            
        if alison_jeremy:
            scene v5_alison1c with long
            "We found a small space on a couch and sat down."
            "There was only room for three, so Alison sat on Jeremy's lap."
            "They were too busy flirting with each other to pay too much attention to Emma and me. I talked to her a bit, but we were both pretty spent."           
            "It was late and as the effects of the alcohol began wearing away I started to feel a bit tired and sleepy."
            "And Alison and Jeremy clearly looked like they wanted to be alone... Emma and I were probably just a bother at this point."
            "It was time to call it a night."
        else:
            "It was pretty late already, and as the effects of the alcohol began wearing away I started to feel a bit tired and sleepy."
            "We made some small talk, but Jeremy was monopolizing Alison's attention, so I ended up speaking with Emma."
            "She was as spent as I was, so after a while we decided it was time to call it a night. "
        $ fian = "n"
        $ femma = "n"
        $ falison = "flirt"
        scene blazer
        show ian at left
        show alison at right
        show emma at centerlef
        show jeremy at rig
        with long
        i "Hey guys, Emma and I are gonna go home."
        $ falison = "n"
        a "Already?"
        e "It's pretty late and we've been dancing the whole night!"
        a "Oh, yes, it's late..."
        if alison_jeremy:
            a "Well then, until next time guys! I hope it's soon. Tonight was fun!"
            $ fjeremy = "flirt"
            j "Bye, guys."
        else:
            j "My shift won't take much longer. Wanna get one last drink, Alison?"
            a "Hmm, I don't know..."
            $ fjeremy = "flirt"
            j "Come on, when was the last time you stayed up until the club closed?"
            a "Well, OK. A day's a day."
            i "Are you staying?"
            a "Yeah."
            e "Well then, until next time!"
            a "Tonight was fun! We have to do this again!"
    
    stop music fadeout 2.0
    scene streetnight with long
    "Emma and I left the club, said goodbye to each other and went our separate ways."        
    jump v5iansunday 
    
##CLUB ALISON SEX  ###############################################################################################################################################   
       
label v5alisonsex:
    $ v5_alison_sex = True
    i "Look, we can sit there."
    if v5_ian_cool:
        scene v5_alison1
    else:
        scene v5_alison1b
    with long
    "I took a seat on a free couch I found in a corner, next to a pillar. Alison sat too, but on my lap."
    a "I'm not too heavy, am I?"
    i "No, not at all."
    "Being taller than me, Alison was a bit heavier than I was used to, but nothing I couldn't handle."
    "And it wasn't like feeling the weight of her ass on my crotch was something I didn't enjoy..."
    "I rested my hand on her hips and she leaned back, making herself comfortable. The smell of her hair and her perfume filled my nostrils."
    menu:            
        "Tease her a bit":
            $ renpy.block_rollback()
            "Having her on top of me like that was making me aroused and wanting to be a bit naughty."
            "I gripped her hips tighter and began moving mine very slightly, rubbing myself against Alison's ass."
            a "Oh, someone's feeling affectionate?"
            i "That's my line. It's you who sat on top of me."
            a "Well, let's just say I've been wanting to be on top of you for a while now..."
            "She matched the movement of her hips to mine, grinding on me. Needless to say, my cock was completely hard by this point."
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            if ian_lust > 3:
                "The desire to be even naughtier had been growing proportionally to my dick. I wanted to play with her..."
                menu:
                    "{image=icon_lust.png}Finger Alison" if ian_lust > 3:
                        $ renpy.block_rollback()
                        $ v5_alison_public = True
                        $ alison_satisfaction += 1
                        "Rather, I couldn't wait."
                        if v5_ian_cool:
                            scene v5_alison2
                        else:
                            scene v5_alison2b
                        show v5_alison2_face1
                        with long
                        "I slid one of my hands down Alison's belly and into her pants."
                        a "Ian, what are you doing...?"
                        "I brought my lips close to her ear and answered."
                        i "I want to check if you're as turned on as I am."
                        "My fingers snuck under her panties, ran down her pubis and found what I was looking for."
                        a "Ian...!"
                        "I felt her soft lower lips with the tip of my fingers. With subtle caresses I tried to reach even further."
                        "I made Alison open her legs to get easier access. We were facing one of the pillars, so our activities were a bit hidden... But not too much."
                        "Finally I managed to slide my finger into her slit, and I wasn't disappointed with what I found. Alison was already moist."
                        hide v5_alison2_face1
                        show v5_alison2_face2
                        with short
                        a "Mhhh, Ian, stop, what are you doing...?"
                        a "People might see..."
                        "I considered if I should indeed stop, but Alison's body wasn't telling me the same thing as her words did. She even spread her legs further apart so I could finger her more comfortably."
                        "I began rubbing her clit gently, feeling her moisture increase each time my fingers slid over her clit."
                        "I noticed Alison's breathing become heavier and I could almost hear her trembling sighs over the loud music."
                        "As I increased the speed of my caresses, so did Alison's whimpers. Her hips began shaking uncontrollably."
                        a "Fuck, Ian, oh God..."
                        "I kissed her on the lobe of her ear. Then on the neck. I brushed my lips across it."
                        a "Mhhh, Ian...! Mhh..."
                        hide v5_alison2_face2
                        show v5_alison2_face3 with vpunch
                        a "Mhhhh!!!"
                        "Alison held a loud moan as her body convulsed over me."
                        "She really was cumming!"
                        "I progressively slowed down the movement of my fingers until I felt Alison's pleasure die down."
                        hide v5_alison2_face3 
                        show v5_alison2_face1
                        with short
                        a "Ian, you're crazy..."
                        i "I'd rather say I just drove you crazy..."
                        a "That too... Oh God, I can't believe we did this... I hope nobody saw!"
                        "I took a look around. Nobody seemed to be looking in our direction."
                        i "I doubt it. We're in a dark corner... But maybe we should go to my place to do the other things I want to do to you."
                        a "I've been waiting the whole night to hear that..."
                        "Just as we stood up, ready to leave, Jeremy showed up."
                        
                    "Take her home":
                        $ renpy.block_rollback()
                        "But the best place to do so was at home. There we would be comfortable."
                        i "Hey... Why don't we call it a night and go to my place?"
                        a "I was waiting for you to propose it..."                        
                        "Just as we stood up, ready to leave, Jeremy showed up."
            else:
                "I wanted to do naughty things with Alison... But this wasn't the place."
                i "Hey... Why don't we call it a night and go to my place?"
                a "I was waiting for you to propose it..."                        
                "Just as we stood up, ready to leave, Jeremy showed up."
                
        "Keep it civil":
            $ renpy.block_rollback()
            "It was kinda nice being like that, feeling Alison close to me."
            a "I'm pretty tired... What about you?"
            i "Quite a bit, too. We've been dancing a lot... And drinking!"
            a "I was hoping you'd have some extra energy for me tonight, though..."
            i "Oh... Well, of course... I always have some extra energy for you."
            a "That's good to hear. So, why don't we call it a night and go to your place...?"
            "Just when I was going to agree and get up Jeremy showed up."
    
    if v5_alison_public:
        $ fian = "confident"
        $ falison = "blush"
    else:
        $ fian = "smile"
        $ falison = "n"
    scene blazer
    show ian at lef3
    show alison
    show jeremy at rig3
    with long
    j "Hey guys! I've been looking for you all over the place!"
    a "We were just resting a bit..."
    if v5_perry_club:
        j "Where are Emma and Perry, by the way?"
        i "They're upstairs, having fun on their own."
        $ fjeremy = "flirt"
        j "Oh, so he has finally decided to make a move?"
        $ fian = "smile"
        i "Doesn't seem like it... Not yet at least. But I think he's getting closer."
        j "Let's see how the night ends for them!"
        $ falison = "n"
        a "I always thought they'd make a good couple. They're different from each other, but in a way that compliments them."
        $ fjeremy = "smile"
        j "I don't know about that. I just know Perry's had the hots for her for the longest time!"
        j "Oh, and speaking about having the hots... Do you know who was here last night?"        
    else:
        j "Where's Emma, by the way?"
        $ fian = "smile"
        i "We left her upstairs..."
        $ falison = "n"
        a "She was talking with some random people..."
        j "I see she's having fun. Are you guys too?"
        a "Yes! And we haven't spent a penny!"
        j "As I said, I like to take care of my friends! You're welcome anytime!"
        j "Too bad Wade and Perry don't appreciate my hospitality, those bastards..."
        j "Oh, Ian, by the way... Do you know who was here last night?"
    $ fian = "n"
    i "Lena."
    j "Oh, so you know?"
    i "I stumbled upon Ivy before and she told me."
    j "So yeah, your friend Lena came by."
    a "Seems like this girl is everywhere."
    if alison_jeremy:
        j "Ivy invited her to come and she brought Lo--... She brought a friend of hers."
        "Jeremy refrained from talking about his so-called girlfriend in front of Alison."
        if louise_jeremy == False:
            $ fjeremy = "sad"
            j "What a mess that was..."
            i "With Lena?"
            j "No, with her friend and... Well, I'll tell you some other time."
            $ fjeremy = "smile"
        a "So, a busy night for you?"
        j "Not as busy as this one!"
    else:
        $ fjeremy = "sad"
        if louise_jeremy == False:
            $ fjeremy = "sad"
            j "She came with Louise... What a mess that was."
            i "What happened?"
            j "I'll tell you some other time..."
            a "Louise? Who's this Louise?"
            j "It's, uh... you could call her my ex-girlfriend."
            $ fian = "worried"
            i "Ex-girlfriend? Since when?"
            j "Since yesterday. But I don't wanna talk about it now. I'll tell you some other time."
            $ fjeremy = "smile"
            a "Oh, now that it was getting interesting..."
        else:
            j "She came with Louise. Damn, and she got really wasted..."
            a "Louise? Who's this Louise?"
            i "A girl Jeremy is sweet on."
            a "Another one, huh?"
            $ fjeremy = "smile"
            j "Ha ha ha!"
    $ fjeremy = "flirt"
    j "So, you wanna get wild on the dance floor? Maybe get another drink?"
    a "Actually, we were just thinking about leaving."
    $ fjeremy = "n"
    j "Oh, so early?"
    if v5_perry_club:
        a "It's not early at all! We've been here for like what, four hours? And I don't think I should drink anymore."
        j "Come on guys, when was the last time you stayed up until the club closed?"
        i "Maybe another day... The bed's calling, if you know what I mean."
        "I winked at Jeremy."
        $ fjeremy = "smile"
        j "Oh, sure. In that case I won't keep you any longer."
        i "Tell Perry and Emma we left if you see them."
        a "Thank you for everything, Jeremy. Tonight was so much fun."
        a "We have to do this again soon!"
        j "Whenever you guys want."
    else:
        $ femma = "n"
        show ian at left
        show alison at centerlef
        show jeremy at right
        with move
        show emma at rig with short
        e "I finally find you, guys!"
        i "Oh, Emma, here you are."
        e "Sorry, I got tangled up chatting with some random people... Crazy bunch, but nice guys!"
        i "Alison and I were about to leave."
        e "Sounds good to me. I'm tired, too!"
        $ fjeremy = "smile"
        j "Well, I see you've made up your mind already. I hope you had fun while I was working!"
        e "We did! Thank you for everything, Jeremy! We should do this again sometime, but when you don't have to work!"
        j "Whenever you guys want."
    stop music fadeout 2.0
    scene streetnight
    with long
    "We left the club and Alison and I took a night bus straight to my place."
    
    play sound "sfx/door_home.mp3"
    scene ianhomenight_dark with long
    $ fian = "smile"
    $ falison = "flirt"
    show ian at lef
    show alison at rig
    with short
    "When we crossed the door we were already in a playful mood."
    if v5_perry_club:
        a "We're alone, right? Perry hasn't arrived yet."
        i "No, he hasn't."
    else:
        a "We're alone, right?"
        i "Yes, Perry said he would spend the night at Wade's place."
    a "Well then, we should take advantage of that. First time we can go all out..."
    $ fian = "confident"
    i "That's true... I just need to go to the bathroom for a second before that."
    a "Don't take long..."
    hide alison with short
    show ian at truecenter with move
    "I went to the bathroom, took a leak and quickly washed my intimate parts."
    "I had been sweating a bit with all that dancing, but now I was gonna sweat a lot more..."    
    play sound "sfx/door.mp3"
    scene ianroomnight
    show ian 
    with long
    i "Perry's gone, so we're all alone..."
    $ fian = "surprise"
    "Those last words died in my mouth, wide open at what I was seeing."
    play music "music/sex.mp3" loop
    scene v5_alison3a with long
    a "Then come on, are you gonna make me wait?"
    "Alison had already undressed and was on top of my bed, inviting me to join her."
    "All that remained were her panties, and her hand was inside of them, slowly rubbing her sex."    
    a "Finally we can let it all out... We don't have to hold anything in..."
    "She bit her finger lusciously as she played with herself, teasing me."
    a "Come here, what are you waiting for?"
    if ian_lust > 2:
        menu:
            "{image=icon_lust.png}I'm enjoying the view" if ian_lust > 2:
                $ renpy.block_rollback()
                $ v5_alison_dirty_talk = True
                i "I'm just enjoying the view..."
                a "Oh, so you like what you're seeing?"
                i "Do you even have to ask?"
                a "I wanna know... What do you like so much?"
                i "I like your sexy body... Those beautiful boobs..."
                i "And how naughty you look touching yourself like that."
                a "So you like watching me touch myself?"
                i "Touching yourself for me."
                a "Mhh... I like how that sounds. But I'd like it even more if it was you touching me..."
                "I couldn't get any harder. It was time to give Alison what she was asking for."
                
            "Go get her":
                $ renpy.block_rollback()
                "I did the only reasonable thing to do: I walked to the bed and jumped on her." 
    else:
        "I did the only thing I could: I walked to the bed and jumped on her."
    if v5_ian_cool:
        scene v5_alison3
    else:
        scene v5_alison3b
    with long
    play sound "sfx/mh1.mp3"
    "I kissed her and ran my hands all over her body, pulling her panties off..." 
    "And then she pushed me down, getting on top of me. I could tell she was fired up!"
    if v5_alison_public:
        "And so was I... I had been hard as a rock since I had fingered her at the club."
        "Seems like I had left her wanting for more!"
    else:
        "And so was I... Looking at her dance at the club... Having her sitting on top of me..."
    "I did what I couldn't do at the club. I grabbed her boobs and began kissing, licking and sucking them."
    play sound "sfx/mh1.mp3"
    a "Mhhh... You must really like my boobs..."
    i "You know I do... Mffh..."
    if v5_alison_dirty_talk:
        a "Then play with them all you want..."
    "Alison was grinding her pussy against my crotch as I played with her breasts."
    "She moaned as pleasure built up. I helped her with that, softly biting her nipples, pushing my hips up, rubbing the bulge of my cock against her sex."
    a "Mhhh, you're so hard, Ian, aren't you? I can feel it even with your pants on..."
    if v5_alison_dirty_talk:
        i "Sucking on your tits makes me so fucking hard..."
        a "And the way you're doing it makes me so damn wet..."
    else:
        i "Guess whose fault it is?"
    "We kept grinding and making out like that for a few minutes, fanning the fire of our desire to the point it couldn't possibly get any hotter."
    "It was the moment to get rid of my clothes and take action."
    menu:
        "{image=icon_lust.png}Boob job" if ian_lust > 2 or v3_alison_boobjob:
            $ renpy.block_rollback()
            $ v5_alison_boobjob = True
            scene v5_alison4_animation with long
            "I took off my pants and rolled around, ending up on top of Alison."
            a "Oh, so this is what you want..."
            play sound "sfx/bj1.mp3"
            "She welcomed my erect manhood between her voluptuous and soft breasts."
            if v3_alison_boobjob:
                a "You liked this so much the other time..."
                i "You know I did. I gave you conclusive proof."
                a "I love it when you give me \"proof\"."
            else:
                a "Oh, so this is what you want?"
                i "You can't blame me."
                a "I'm not."
            "She pushed her tits together, trapping my cock between them, and stuck her tongue out."
            "I moved my hips back and forth, jerking myself off and feeling Alison's wet and warm tongue at the end of each thrust."
            "It felt so nice and soft... And the view was even better."
            "Alison was looking at me with a smirk as I fucked her tits slowly, twirling her tongue around the tip of my dick when it came close to her mouth."
            if alison_voyeur:
                "Seeing her like this made me remember the picture Jeremy had sent me. His cock had been buried between Alison's tits, too..."
                "And she seemed equally eager to please both of us."
                "For some reason I got even more turned on and I felt I could cum at any moment..."
            else:
                "It was enough to make me wanna cum."
            menu:
                "Fuck Alison":
                    $ renpy.block_rollback()
                    "But I didn't want to blow my wad just yet. I wanted to fuck her." 
                    
                "Cum all over Alison":
                    $ renpy.block_rollback()
                    $ v5_alison_boobjob_cum = True
                    "And why the hell not? I wanted to. I wanted to paint Alison's face with my cum."
                    "I sped up the movements of my hips and grunted. Alison read my body language right away."
                    a "What's up, are you gonna cum?"
                    i "I'm about to..."
                    if v5_alison_dirty_talk:
                        a "Do it, cum for me, Ian. Splash my face with your jizz."
                        "Hearing her say those naughty words was the final push I needed."
                    else:
                        a "Go ahead, you can do it. Feel free to cum."
                        "With her permission I had nothing else holding me back."
                    scene v5_alison4
                    show v5_alison4_cum 
                    with flash
                    with vpunch
                    i "Ohhh!!"
                    "Knowing we had privacy that night made me feel free to groan openly and loudly as pleasure overtook me."
                    play sound "sfx/bj2.mp3"
                    a "Mhh!"
                    "I closed my eyes, possessed by intense bliss, and shot my load all over Alison's face."
                    a "That was quite a lot, hee hee..."
                    i "Whew..."
                    "I took several deep breaths, recovering, still on top of Alison."
                    if v3_alison_boobjob:
                        "I had come on her face once again... And she seemed to love it."
                        a "Seems like fucking my tits really does it for you, you naughty boy..."
                        i "Not only fucking your tits..."
                    else:
                        i "You just turned me on so fucking much!"
                        a "I'm glad... But now the one who's super turned on is me!"
                        i "Let me return the favor, then!"
                    scene v5_alison5 
                    show v5_alison5_cum
                    with long
                    "I lay next to Alison, but not to rest. It was time for some active recovery."
                    "My hand ran down her abdomen until my fingers slid into her pussy. It was slippery and welcoming."
                    play sound "sfx/ah1.mp3"
                    if v5_alison_public:
                        a "Nhhh... Oh, Ian... Didn't you have enough with what we did at the club?"
                        i "I'm just greedy like that."
                        a "Mhhh, I'm not complaining!"
                        i "You're super wet again..."
                    else:
                        a "Nhhh... Do you find it to your liking?"
                        i "You're pretty wet, so yeah..."
                    a "Ready for you..."
                    i "Let me play with it a bit."
                    "I dug my fingers deeper, pressing up, massaging the most sensitive area of Alison's pussy."
                    "I could tell I was hitting the right spots by her moans and whimpers. I enjoyed hearing them so much..."
                    "I was glad Perry wasn't home."  
                    show v5_alison5_dick
                    with long
                    $ alison_satisfaction += 1
                    "Feeling her arousal and pleasure growing turned me on and got me ready for action again."
                    
        "Finger her":
            $ renpy.block_rollback()
            $ alison_satisfaction += 1
            scene v5_alison5
            show v5_alison5_dick
            with long
            "I lay next to Alison and my hand ran down her abdomen until my fingers slid into her pussy. It was slippery and welcoming."
            play sound "sfx/ah1.mp3"
            if v5_alison_public:
                a "Nhhh... Oh, Ian... Didn't you have enough with what we did at the club?"
                i "I'm just greedy like that."
                a "Mhhh, I'm not complaining!"
                i "You're super wet again..."
            else:
                a "Nhhh... Do you find it to your liking?"
                i "You're pretty wet, so yeah..."
            a "Ready for you..."
            i "Let me play with it a bit."
            "I dug my fingers deeper, pressing up, massaging the most sensitive area of Alison's pussy."
            "I could tell I was hitting the right spots by her moans and whimpers. I enjoyed hearing them so much..."
            "I was glad Perry wasn't home."                    
            a "Fuck me, Ian... I want you inside me..."
            "Her voice was full of need and desire. I needed no more motivation than that."
            
        "Fuck her":
            $ renpy.block_rollback()
            "I had been wanting to stick it inside Alison the whole night..."
            "There was no time for preliminaries or stuff like that. I had to satiate my desire!"
    
    "I reached for my drawer to pick up a condom."
    scene v5_alison6
    if v5_alison_boobjob_cum:
        show v5_alison6_cum
    with long
    "I made Alison lie down for me, got between her legs and pushed it in..."
    "I bit my lip while entering inside her. It felt so nice..."
    play sound "sfx/ah3.mp3"
    a "Oh, yes... I couldn't wait to enjoy this..."
    i "Then enjoy yourself to your heart's content."
    "I began giving it to her rather slowly, looking at her reactions."
    "Alison took my words to heart. She closed her eyes and focused on the sensations I was providing her with."
    a "So good..."
    a "Go faster... Yeah..."
    "She was a thing of beauty... I had always thought she was attractive, but seeing her like this had given me a whole new appreciation."
    "Moans escaping her open mouth, her lush breasts bouncing with each thrust, her long legs spread apart to each of my sides..."
    if v5_alison_boobjob_cum:
        "My cum was still dripping down Alison's face and chest, marking her."
    if ian_lust > 3:
        menu:
            "{image=icon_lust.png}Rub her clit" if ian_lust > 3:
                $ renpy.block_rollback()
                if alison_satisfaction < 5:
                    $ alison_satisfaction += 1
                show v5_alison6_hand with short
                "I wanted to make her look even more sexy. I wanted her to lose her mind!"
                "I began rubbing her clit with my thumb while I kept fucking her, driving my hips upward."
                a "Ian, what are you doing? Ian...!"
                show v5_alison6_face with long
                play sound "sfx/ah2.mp3"
                a "Ahhh, fuck...!"
                  
            "Go faster":
                $ renpy.block_rollback()
                "I sped up even more, penetrating Alison with the full length of my cock."
                play sound "sfx/ah2.mp3"
                a "Oh fuck, Ian!"
    else:
        "I sped up even more, penetrating Alison with the full length of my cock."
        play sound "sfx/ah2.mp3"
        a "Oh fuck, Ian!"
    "The always strong and rather blunt Alison was giving herself entirely to me, abandoning herself to my hands."
    "It made me feel so horny... It made me feel in control. I wanted to tease her."
    i "What's that? You're loving it, aren't you?"
    a "Yeah, I love it... I love having you inside me...!"
    a "I love you, Ian!"
    if alison_satisfaction > 3:
        a "I love you so much!"
        "I pounded her harder, rubbing my thumb with more pressure."
        "I could afford to be a bit rough. She was on the brink. I could feel it!"
    elif alison_satisfaction > 2:
        show v5_alison6_face with long
        a "Oh yes, oh yes!"
        "I pounded her harder, going for broke. She was on the brink. I could feel it!"
        play sound "sfx/ah4.mp3"
    else:
        "I pounded her harder, going for broke. She was on the brink. I could feel it!"
        play sound "sfx/oh1.mp3"
    a "Ahhhh!! Ian!! Yeees!!"
    with vpunch
    "She was serious when she said she wouldn't hold anything back."
    if alison_satisfaction > 2:
        "I had never heard Alison scream like that. I wondered if we had woken the neighbors up... Not that I cared."
        "I loved those sounds she was making!"
    else:
        "She let out a loud scream. Perry would've heard us for sure if he had been home."
    "I slowed down my thrusts as Alison's orgasm died down."
    stop music fadeout 2.0
    $ falison = "smile"
    $ fian = "smile"
    scene ianroomnight
    show iannude at lef
    show alisonnude at rig
    if v5_alison_boobjob_cum:
        show alison_cum1 at rig
    with long
    "Finally, I laid down next to her, catching back my breath."
    if alison_satisfaction > 3:
        a "Oh, wow... That thing you did at the end, it was... pretty nifty."
        i "I thought you'd like it."
    else:
        a "Oh, wow..."
    if v5_alison_boobjob:
        if v5_alison_boobjob_cum:
            a "I guess you're not cumming a second time, are you?"
            i "Once is more than enough... I don't know where did I get all that energy from, honestly."
            $ fian = "confident"
            i "Well, I do know, actually... You just make me so horny."
            a "Hee hee! I'm glad!"
        else:
            a "What about you? You haven't finished yet..."
            i "It's not gonna happen tonight... I'm completely spent."
            $ falison = "sad"
            a "Damn, and I thought you were so close to cumming when you were using my boobs..."
            i "I was, yeah."
            if v3_alison_boobjob:
                a "Next time do it. like you did the other time!"
            else:
                a "Mhh... I can't seem to get you to cum!"
            i "Don't worry, I had a lot of fun... It's just I'm so tired after the whole night out!"
            $ falison = "smile"
            a "Alright, but you owe me one... I don't like leaving things unfinished!"
    else:
        a "What about you? You haven't finished yet..."
        i "It's not gonna happen tonight... I'm completely spent."
        $ falison = "sad"
        a "Mhh... I can't seem to get you to cum!"
        if v3_alison_boobjob:
            i "You did last time, remember?"
            a "Yeah, but not this time!"
        i "Don't worry, I had a lot of fun... It's just I'm so tired after the whole night out!"
        $ falison = "smile"
        a "Alright, but you owe me one... I don't like leaving things unfinished!"
    a "But to be honest I'm dead tired too..."
    scene ianroomnight with long
    "Alison snuggled up to me and closed her eyes. I did the same."
    if v5_alison_boobjob_cum:
        if v3_alison_boobjob:
            "It seems I had found one sure way for Alison to make me cum!"
        else:
            "This time I got to cum while having sex with Alison!"
        "I felt I still had some trouble letting go completely when in bed with Alison, though."
        "Probably because I still felt a bit weird having this kind of relationship with her after so many years of friendship."
    else:
        "It seemed I still had some trouble letting go completely when in bed with Alison..."
        "Probably because I still felt a bit weird having this kind of relationship with her after so many years of friendship."
    "The sex was really enjoyable, so I knew the reason why I had a hard time cumming had to do with me, not with her."
    "But I felt a bit more comfortable each time... Tonight had been great."
    "There was something that irked me, though. Something she had said in the midst of passion."
    "She had said she loved me, right...?"
    jump v5iansunday        
        
##CLUB EMMA SEX    ###############################################################################################################################################   
    
label v5emmasex:    
    
    $ v5_alison_jeremy = True
    
    "I couldn't restrain myself any longer."
    if v5_ian_cool:
        scene v5_emma2
    else:
        scene v5_emma2b
    with long
    "My desire had been lit, and I had to express it."
    "I turned Emma around, pulled her towards me and kissed her."
    "And she kissed me back without hesitation."
    "I felt her tongue invading my mouth right away. And I welcomed it with mine."
    play sound "sfx/xp.mp3"
    show lust_up
    $ ian_lust_xp += 1
    call screen skillsup
    "We began kissing like we had pent up passion. Could it be that this dance had fired up both of us this much?"
    "In any case, we were devouring each other in the middle of the dance floor, Emma's body rubbing against mine, and my hands caressing her back and arms."
    "We were in the middle of the dance floor and some people looked at us. I felt observed and got pulled back from the moment."
    $ fian = "shy"
    $ femma = "flirt"
    scene blazer
    show ian at lef
    show emma at rig
    with long
    "When Emma and I left our embrace that inevitable awkward moment fell on us."
    "What the hell had just happened? Emma and me?"
    i "Wow, well, that was..."
    e "Unexpected?"
    i "Totally unexpected."
    e "Yeah, it was..."
    $ femma = "n"
    "Emma and me, yeah... And it had been so enjoyable..."
    "But now what? I felt the need to move things along, escape this awkward tension. Change the subject."
    i "Where's Alison, by the way? She's taking very long."
    e "Let's go find her."
    stop music fadeout 2.0
    play music "music/dumb.mp3"
    scene blazer with long
    "We went to the lower floor, looking for our lost friend."
    "It only took me a couple of minutes to spot her."
    scene v5_alison1c with long
    i "Look, there she is..."
    e "Oh."
    "She was sitting with Jeremy, or rather sitting on top of Jeremy."
    "He was running his hands down her thighs, and Alison seemed pretty pleased with it."
    if alison_jeremy:
        if ian_alison_sex:
            "I was not surprised. Even if Alison and I had slept together, she had done it with Jeremy first..."
            "He was clearly still interested in pursuing her, and she was open and willing to it."
        else:
            "I was not surprised. I knew her affair with Jeremy was still ongoing and that they would probably end the night together."        
    elif ian_alison_sex:
        "I was a bit shocked. I knew Jeremy was intent on pursuing Alison, but I thought she had chosen me..."
        "But I was in no position to complain. I had been giving my attentions to Emma and not to her..."
    e "You can feel the sexual tension between those two! They're going home together for sure."
    i "I bet they are..."    
    e "So..."
    if v5_ian_cool:
        scene v5_emma1
    else:
        scene v5_emma1b
    with long
    "Emma fell back to my chest again, her ass resting on my crotch once more..."
    "Fuck awkwardness. I was so down for that."
    if v5_ian_cool:
        scene v5_emma2
    else:
        scene v5_emma2b
    with long
    "I kissed her again, and I could sense she had been wanting it, expecting it."
    "We made out against one of the pillars, in a not-so-well-lit corner."
    "Each time our fire grew higher and higher. My hands grew bolder and I fondled Emma's ass as I kissed her."
    "I could feel her soft boobs pressed against my chest and my cock wanting to explode in my pants."
    "I thought about the comment Emma had made about Jeremy and Alison. That they would go home together tonight..."
    $ femma = "flirt"
    $ fian = "confident"
    scene blazer
    show ian at lef
    show emma at rig
    with long
    i "Hey, do you want to have one last drink? But not here. At my place..."
    e "I was hoping you'd suggest it."
    i "Then let's get the hell out of here."
    stop music fadeout 2.0
    scene ianhomenight_dark with long
    "We took the night bus straight to my place."
    play sound "sfx/door_home.mp3"
    show ian at lef
    show emma at rig
    with short
    i "Here we are..."
    e "Are we alone?"
    i "Yeah... Wait, let me check..."
    "I peeked into Perry's room. Indeed, he was out, spending the night at Wade's place."
    "Such luck... Otherwise I wouldn't have dared bringing Emma home."
    "What was about to happen was... It was kinda wrong, was it?"
    if v5_perry_feelings:
        "Perry had confessed his feelings for Emma to me. Not that he needed to for me to know."
        if v5_emma_talk:
            "He had even asked me to help him with the situation, see if there was a way Emma would be interested in him..."
            "But instead of that I was about to have sex with her."
        else:
            "And despite knowing that I was about to have sex with her..."
        "What was about to happen was wrong, yeah. But I wanted it so bad."
        "And I wasn't the only one."
    else:
        "I knew Perry liked Emma, even though he always denied it."
        "And he said he was happy with how things were between them, so..."
        "I should feel free to indulge in this with Emma. She wanted it as much as I did." 
    i "Yes, we're definitely alone."
    e "Cool. Your room was this way, right?"
    "Emma took my hand and pulled me to my bedroom."
    play sound "sfx/door.mp3"    
    if v5_ian_cool:
        scene v5_emma3
    else:
        scene v5_emma3b
    with long
    play music "music/sex.mp3"
    "As soon as we got into my room we resumed what we had begun on the dance floor."
    "Our bodies came together and so did our mouths, our tongues searching for each other's with base hunger."
    "I never knew kissing Emma would get me so hard... But I felt my cock full of blood and desire under my pants."
    "I grabbed her ass again, but her shorts were in the way."
    if v5_ian_cool:
        scene v5_emma4
    else:
        scene v5_emma4b
    with long
    "I turned Emma around, unbuttoned her booty shorts and slid both them and her panties down."
    i "Let's take these off..."
    "I marveled at Emma's bare ass. "
    "It was thick and hefty, but perfectly plump and bubbly."
    "I grabbed it with my hands and kneaded it. I couldn't resist sliding my tongue across it."
    e "That tickles... What are you doing back there, Ian?"
    menu:
        "{image=icon_charisma.png}+{image=icon_lust.png}Your ass drives me crazy" if ian_lust > 2 and ian_charisma > 2:
            $ renpy.block_rollback()
            $ emma_satisfaction += 1
            i "Your ass drives me crazy, Emma..."
            "I fondled her butt cheeks and kissed one of them."
            i "I couldn't take my eyes off it during the whole night..."
            i "The way it looked in those shorts... The way you shook it when you danced..."
            "I softly bit Emma's ass, and she let out a genuine whimper of excitement."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_emma += 1
            e "I'm glad you like it..."
            i "You're glad? Don't tell me you were wearing those booty shorts for me?"
            e "Maybe..."
            
        "Nothing":
            $ renpy.block_rollback()
            i "Oh, nothing..."
            "I took a last look at that majestic ass."
        
        "Just playing":
            $ renpy.block_rollback()
            $ emma_satisfaction += 1
            "I fondled her butt cheeks and kissed one of them."
            i "Just playing..."
            e "Playing with my ass?"
            i "Yup..."
            "I softly bit Emma's ass, and she let out a genuine whimper of excitement."
            e "Do you really like it that much?"          
            i "Can't you tell?"
        
        "...":
            $ renpy.block_rollback()
            i "..."
    
    scene v5_emma5
    with long
    "I stood up, still behind her, and pulled her towards me."
    "My erect cock got trapped between me and Emma's booty. The warm touch of her skin on my member made me shiver with excitement."
    if emma_satisfaction > 0:
        "I leaned forward and kissed her neck. My tongue rolled up until my lips touched her ear, and then I whispered."
        i "Are you telling me you wore those sexy shorts because you wanted me to notice your ass?"
        "While I kissed her and whispered my hips were moving up and down, my cock frazzling against her ass."
        "She answered with a trembling whisper."
        e "Uh... Not exactly... Well... Well yeah, but just a bit."
        "As she talked I pushed my hips further and my cock got buried between her ass cheeks. It was such a perfect fit..."
        e "I wasn't expecting the night to end like this at all, I swear..."
    else:
        "I pushed my hips further and my cock got buried between her ass cheeks. It was such a perfect fit..."
    "My hands fondled her breasts and caressed her tanned skin."
    "My lips and tongue were busy with her neck and ear"
    "And she began grinding herself against me, lifting her arms around my neck, pulling me closer."
    "I was jerking myself off using Emma's butt and she was eagerly helping me."
    "I could never have imagined that Emma could turn me on so much! I had always seen her as a plain friend, but being here now..."
    e "Oh fuck, you're so hard, Ian..."
    i "Can you feel it?"
    e "Yeah..."
    scene v5_emma6
    with long
    "She bent over, showing me a perfect view of her pussy and asshole."
    e "And you, can you feel how wet I am right now?"
    "I had no answer to that. I just stood there, amazed at what Emma was showing me."
    "It was true, her inner thighs were completely drenched."
    "I had never seen a pussy so wet. Even her asshole was completely shiny with lubrication."
    e "Since you like my ass so much... Do you wanna fuck it?"
    "I had to repeat it back to be sure if I was getting the situation right."
    i "You want me to fuck you in the ass."
    e "If you want..."
    "Her voice was not timid or shy. It was playful and inviting."
    "There was no way I could reject something like that."
    scene v5_emma7_animation
    with long
    play sound "sfx/ah2.mp3"
    e "Ohhh...!"
    "I pushed her to the bed and shoved my cock into her a bit rougher than I should've."
    "But her ass swallowed it without too much trouble. It was elastic and super well lubricated."
    i "Mphh..."
    "I drove my hip forward, sliding every inch of my cock in bit by bit. It only took about two seconds."
    "That first, single thrust, had slid in so easily... And it had felt amazing!"
    "Emma was panting, mouth wide open, enjoying the feeling of having me inside. A pleasure I was about to grant her aplenty."
    "I began moving my hips, sliding my cock in and out of her ass, not too fast, but not too slow, either."
    if emma_satisfaction > 0:
        "I decided to tease her a bit more."
        i "So you were not expecting tonight to end like this, huh?"
        "She spoke between sighs and whimpers."
        e "Fuck, no... But right now... I'm so glad that it did!"
        i "Then why did you want to make me horny with those slutty shorts?"
        i "That's what you said, right? That you wanted me to get horny looking at your ass..."
        e "Oh, Ian, fuck..."
        e "Yes...! I wore those slutty, slutty shorts because I wanted you to get horny from my booty!"
        e "I wanted you horny so you'd..."
        e "So you'd fuck me deep in the ass like you're doing right now...! Ohhh!"
    else:
        "Emma whimpered and moaned, showing me how intensely she was feeling it."
        "I was sure I could go a bit harder..."
    "I increased the rhythm of my thrusts. My cock went in and out of her ass like it was fucking a pussy."
    "But it felt tight. And Emma knew when to squeeze me."
    i "Fuck... This is so good..."
    e "Yes, so good...! I love how you're giving it to me, Ian."
    "Emma was always honest when she talked, but I had never heard a more honest sentence out of her mouth."
    menu:
        "{image=icon_lust.png}Tell Emma to touch herself" if ian_lust > 3 or ian_lust > 2 and emma_satisfaction > 0:
            $ renpy.block_rollback()
            $ v5_emma_finger = True
            i "I want you to touch yourself while I fuck you."
            i "Play with your pussy for me, Emma."
            scene v5_emma8_animation
            with long
            e "Mmmhh!!"
            "I didn't know if she moaned out of excitement or because I pulled her up on top of me."
            "From that position my cock was buried as deep as it could go in Emma's incredible butt."
            "She began bouncing up and down, impaling herself on my cock. And she gave the same treatment to her pussy."
            "I could tell she was shoving her fingers in, rubbing the insides of her pussy."
            "I could even feel the knuckles on my cock through the thin wall of flesh."
            play sound "sfx/ah6.mp3"
            e "Oh fuck, yeah...!"
            e "Fuck, Ian!"
            
        "Slow down":
            $ renpy.block_rollback()
            if emma_satisfaction > 0:
                $ emma_satisfaction -= 1
            scene v5_emma7_animation_slow
            "I slowed down a bit, trying to make Emma feel every inch as it went in and out."
            "Also, I didn't want to get too carried away and blow my load too early..."
            "Just at that moment I became aware: I was fucking Emma without a condom."
            "I had been so turned on it hadn't even crossed my mind. I was fucking Emma raw!"
            e "No... Don't slow down..."
            e"Keep that rhythm from before, it was sooo good..."
            i "Of course."
            scene v5_emma7_animation
            "I pumped my hips at the previous rate, going in and out like a well oiled piston."
            
        "Give it to her harder":
            $ renpy.block_rollback()
            scene v5_emma7_animation_fast
            play sound "sfx/ah6.mp3"
            e "Oh fuck...! Yes, Ian... Just like that...!"
            "Going at this pace I wouldn't take too long to cum..."
            "In fact, not long at all!"
            "Just at that moment I became aware: I was fucking Emma without a condom."
            "I had been so turned on it hadn't even crossed my mind. I was fucking Emma raw!"
            "And the feeling was amazing..."
    
    "The movement got faster and faster. And it was Emma who was setting the pace."
    i "Emma... I'm gonna cum...!"
    if v5_emma_finger:
        "She fingered herself faster, matching the rhythm of our hips."
    e "Yes, me too! Me too!"
    "She didn't tell me to stop, or to cum outside. I guessed since we were doing anal it was OK."
    "And even if she had told me to, I didn't know if I could've restrained myself..."
    "Luckily for me, I didn't have to."
    if v5_emma_finger:
        scene v5_emma8
        show v5_emma8cum
    else:
        scene v5_emma7
        show v5_emma7cum
    with flash
    with vpunch
    i "Ohhhh...!!"
    "As I came I felt the sudden contractions of Emma's muscles around my cock."
    "All her body tensed and she let out a loud moan."
    play sound "sfx/oh1.mp3"
    e "Ooooohh!!"
    with vpunch
    "I could feel her orgasming as my cum filled up her rectum."
    "After several long and tremulous seconds of bliss, we came back to our senses and broke our bodies' embrace."
    stop music fadeout 2.0
    scene ianroomnight
    with long
    pause (1)
    $ fian = "smile"
    $ femma = "flirt"
    show iannude at lef
    show emmanude at rig
    show emma_cum1 at rig
    with short
    if emma_satisfaction > 1:
        e "Oh my God, that was amazing! I didn't know you had it in you, Ian..."
        i "I'm glad to have surprised you, then."
        e "Mhhh yeah, you did..."
    else:
        e "Oh God, that was great, Ian...!"
        i "It definitely was... Damn..."
    e "Let me clean myself up a bit."
    hide emmanude
    hide emma_cum1
    with short
    "Emma went to the bathroom, leaving me lying on the bed, exhausted after such an intense night."
    if emma_satisfaction > 1:
        "The sex had been great, no doubt about it... I didn't know what got into me, but man, I had been so turned on!"
    else:
        "The sex had been great, no doubt about it..."
    $ fian = "n"
    "But now I had to let the consequences of what had happened sink in. I had fucked Emma, and if Perry ever found out..."
    if v5_perry_feelings:
        "I doubted he'd ever forgive me, especially after the talk we just had the day prior..."
    else:
        "He'd probably get so mad at me. Like really mad."
    play sound "sfx/door.mp3"
    $ femma = "n"
    show emmanude at rig with short
    e "Done."
    "Emma sat on the bed, next to me."
    e "I'm so tired..."
    i "Yeah, me too. I'd invite you to stay the night, but I don't know at which time Perry will be back, and..."
    i "I'd prefer if what happened tonight stayed just between us."
    $ femma = "sad"
    e "Uh, yeah... I hadn't considered that."
    e "I guess it'll be easier if we didn't tell the others about it, right?"
    if ian_alison_sex:
        i "Yes. I don't want them gossiping and all that. Things are already complicated as they are, with Alison and me... And also Jeremy."
    else:
        i "Yes. I don't want them gossiping and all that. Things are already complicated as they are, with Alison and Jeremy..."
    e "Yeah, I guess it could make things awkward when we all meet and stuff."
    $ femma = "n"
    e "Don't worry, I will keep the secret."
    $ fian = "smile"
    i "Cool. Now let me at least call you a taxi..."
    e "Don't worry, I'll take the bus. The sun's almost up!"
    e "Thanks for tonight, Ian. It was super fun."
    "Emma kissed me briefly before picking up her clothes and getting dressed."
    scene ianroomnight with long
    "She left and I went straight to bed. I was tired and satisfied, and the possible implications of what I had just done didn't get in the way of me falling asleep."
    jump v5iansunday    
    
############################################################################################################################################################################################################
##IAN SUNDAY ############################################################################################################################################################################################################
############################################################################################################################################################################################################
       
label v5iansunday:    
    
    $ day = "Sunday"
    scene blackbg
    with long
    call screen calendar
    scene ianroom
    with long   
    $ fperry = "n"
    $ ian_look = 3
    $ falison = "sad"
    if v5_alison_sex:
        $ fian = "smile"
        "I woke up pretty late next morning, with Alison still sleeping at my side." 
        "My body felt stiff and a bit sore. It had been an intense night, and my bed was a bit too small for two people."
        show iannude at lef
        show alisonnude at rig
        with short
        a "Mhh... Good morning... What time is it?"
        i "Half past twelve."
        a "So late... I guess I should get up."
        i "Yeah, me too. My mouth's dry, do you want some water?"
        $ falison = "n"
        a "Yes, please."
        "I put on my underwear and went to the kitchen."        
    elif ian_emma_sex:
        $ fian = "n"
        "I woke up pretty late next morning. I felt like I had run a marathon the day prior..."
        "And indeed it had been a very intense day. Especially during the night..."
        show ianunder with short
        "My mouth was dry, so I got up and went to the kitchen to get a glass of water."
        "My mind was busy reminiscing what had happened with Emma a few hours prior..."
    else:
        $ fian = "n"
        "I woke up pretty late next morning. I felt like I had run a marathon the day prior..."
        show ianunder with short
        i "Last night sure was tiresome..."
        "It had been fun, but nothing out of the ordinary. I didn't expect anything else, though."
        "My mouth was dry, so I got up and went to the kitchen to get a glass of water."
    
    play sound "sfx/door.mp3"
    play music "music/normal_day.mp3"
    scene ianhome 
    show ianunder 
    with long
    show ianunder at lef with move
    show perry at rig with short
    p "Hey. Good morning."
    "Perry was in the kitchen, preparing some coffee."
    if v5_perry_club:
        i "Oh, you're already up?"
        p "I just got up... I need some c--{w=0.5}coffee to clear this headache... Want some?"
        i "Sure."
        i "Drank too much again, huh? When did you get back home, by the way? You stayed with Emma after Alison and I left..."
        $ fian = "confident"
        i "Don't tell me you ended up at Emma's place?"
        p "No, d--{w=0.5}don't be ridiculous."
        $ fian = "smile"
        i "Oh, you didn't? That's too bad. You two were hitting it up pretty nicely last night..."
        $ fperry = "smile"
        p "You think so? I had that f--{w=0.5}feeling, but I wasn't sure..."
        i "So nothing happened?"
        $ fperry = "n"
        p "No... I didn't want to mess up or do something weird... And she didn't p--{w=0.5}push for it or anything either, so..."
        i "You'll have to take that step at some point, man. I'd say things look quite promising..."
        if perry_emma:
            i "In fact, I spoke to her about you a bit..."
            $ fperry = "surprise"
            p "You did? You didn't tell her anything e--{w=0.5}embarrassing, did you?"
            i "Calm down, I didn't. I just probed her a bit... and I think things are looking good, man, I promise."
            p "Are you sure?"
        else:
            p "You think so?"
        i "I can't be sure. Nobody can until you ask her out. But I think the odds are good."
        $ fperry = "n"
        p "Mhhh..."        
    else:
        i "Hey... You're already here. How was last night with Wade?"
        p "It was OK, we ordered p--{w=0.5}pizzas, drank beer and played video games."
        i "A perfect night..."
        p "Looks like yours was p--{w=0.5}pretty rough."
        if ian_emma_sex:
            $ fian = "worried"
            i "Um, well, it was... It was OK."
            "If he only knew..."
        else:
            i "It was quite intense, yeah, but in a good way."
        "I poured myself a cup of coffee."
        p "Was the music at the club any good?"
        i "No, not really. You would've hated it."
        p "See, I t--{w=0.5}told you. I'm glad I didn't go."
        if v5_emma_talk:
            $ fperry = "meh"
            p "By the way... Did you talk to Emma? Did she say anything?"
            if ian_emma_sex:
                i "Uh, ehhh..."
                "All I could think about was what had happened in my bedroom..."
            elif v5_emma_grind:
                $ fian = "worried"
                i "Uhh, let me think..."
                "All I remembered was that hot and steamy dance we had shared..."
            if v5_emma_convo3:
                i "I did actually ask her what you wanted."
                p "What I wanted? What d--{w=0.5}did you ask her?"
                i "I don't recall what I said exactly, but..."
                $ fian = "smile"
                i "Turns out she likes kinky stuff."
                $ fperry = "surprise"
                p "S--{w=0.5}she does? What kind of kinky stuff? What did she t--{w=0.5}tell you?"
                if ian_emma_sex:
                    "She did way more than just telling me. I got a very good taste... I wasn't going to tell Perry, of course."
                elif v5_emma_grind:
                    "I had the feeling she would've liked to do more than just telling me what she liked, but I hadn't wanted to cross that line."
                    "I wasn't gonna tell Perry that, of course."
                i "Well, she said she doesn't mind trying new things, even if they're weird, as long as she trusts the other person..."
                i "She seems like the kind of girl who's not judgmental and likes to explore her sexuality."
                p "She told you that?"
                i "Something like that, yeah..."
                $ fperry = "smile"
                p "So she won't think I'm a w--{w=0.5}weirdo?"
                i "Probably not..."
                if ian_emma_sex:
                    $ fian = "worried"
                    "I wasn't sure I should be encouraging him, but..."
                p "Cool, cool."
                    
            else:
                $ fian = "n"
                $ v5_emma_talk = False
                i "Not really, man. I didn't know how to really ask her."
                p "So you d--{w=0.5}didn't ask her anything?"
                i "I tried to, but... It wasn't the best moment, with the music and all..."
                i "And what was I supposed to ask her? If she liked perverted stuff?"
                $ fperry = "serious"
                $ ian_perry -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                p "I think it's better you didn't t--{w=0.5}talk to her."
                i "As I said, it's better if you do it yourself."
                p "That's not what you said, but it doesn't matter. I s--{w=0.5}shouldn't have asked you."
                p "It's better if things stay like they are."
                i "Sure, man."
                if ian_emma_sex:
                    "Better if he abandoned the idea..."
        else:
            i "You could've given it a try, at least."
    
    if v5_alison_sex:
        show ianunder at lef3
        show perry at rig3
        with move
        $ fperry = "surprise"
        $ fian = "shy"
        show alisonbra with short
        a "I smell coffee. Oh, good morning, Perry."
        $ fperry = "meh"
        p "G--{w=0.5}g--{w=0.5}good morning."
        i "Want a cup?"
        a "Yes, please. I really need it."
        if v5_perry_club:
            p "You two were really loud last night. I had to wear earplugs."
            $ fian = "blush"
            $ falison = "blush"
            i "You heard? I thought you'd arrived later..."
            p "I arrived when you were in the m--{w=0.5}midst of it. And I heard things I didn't n--{w=0.5}necessarily wanna hear..."
            p "You should try and be more considerate next time."
            p "Anyways... I'll leave you two to... whatever you're doing."
            hide perry with short
            "He was clearly uncomfortable with having Alison in her underwear around."
            $ falison = "smile"
            $ fian = "shy"
            a "Ha ha ha, well, that was awkward!"
            i "Yeah, sorry about that... Inconveniences of living with a flatmate."
            a "Hey, I'm living with my parents right now, so I'm not going to complain."
        else:
            p "So you s--{w=0.5}stayed over..."
            a "Yeah, Ian invited me."
            p "OK, well... I'll leave you two to... w--{w=0.5}whatever you're doing."
            hide perry with short
            "He was clearly uncomfortable with having Alison in her underwear around."
        i "Anyways, I think I'll take a shower. I really need it..."
        a "I'll finish this coffee and get going, then. I have stuff to do."
        
    else:
        $ fperry ="n"
        hide perry2 
        show perry at rig
        with short
        p "So, what about you? Any luck with the ladies?"
        if ian_emma_sex:
            "Again with the questions... I had to make an effort to lie while keeping a straight face."
        i "Nope, not really. I wasn't in that kind of mood last night."
        if alison_jeremy:
            p "And what about Alison and Jeremy? They're still a thing?"
            i "Yeah."
            p "I held Alison to a higher standard... I wonder how long it'll last."
        else:
            p "And what about Jeremy and Alison? Is he still hounding her?"
            i "Yeah, and I'd say last night he finally caught her."
            p "Really? I held Alison to a higher standard..."
        "I finished the cup of coffee."
        i "Anyways, I'm gonna take a shower. I really need one."
    
    scene ianhome with long
    $ fian = "smile"
    $ ian_look = 2
    "After clearing my head and having some lunch I was ready to take on the afternoon."
    if v5_holly_date:
        "I was supposed to meet Holly at the park, so I got ready and left."
        stop music fadeout 2.0
        jump v5hollydate
    else:
        "I had no plans, so I could sit down and work on my book without being disturbed."
        jump v5iansundayend
        
##HOLLY DATE ############################################################################################################################################################################################################
    
label v5hollydate:
    scene park with long
    if ian_charisma > 3:
        $ ian_look = 3
    else:
        $ ian_look = 1
    $ holly_look = 2
    $ fholly = "shy"
    show ian at lef
    with short
    "I arrived in time. Thankfully I had had time to recover from the night of partying and I didn't look too shit-faced."
    "I looked for Holly but I couldn't seem to find her. It was she who saw me and walked up to me."
    play music "music/date.mp3" loop
    show holly3 at rig with short
    h "Hello, Ian."
    if ian_go_holly > 1:
        $ fian = "surprise"
        i "Oh!"
        $ fian = "smile"
    i "Hey there, Holly."
    "It was the first time I saw her dressed like that so I hadn't recognized her from afar."
    if ian_go_holly > 1:
        "She looked really cute... Even more so than usual." 
    else:
        "She looked really cute..."
    h "Thanks for coming."
    i "Why thanks? It's me who asked to meet you."
    $ fholly = "blush"
    h "Oh, yeah... That's true..."
    $ fholly = "shy"
    hide holly3
    show holly2 at rig
    with short
    h "Well, I'm grateful you did anyway."
    i "Let's take a stroll, shall we?"
    $ fholly = "smile"
    "We began walking through the park. It was a nice, sunny afternoon, and people were out enjoying the weather."
    "I saw a lot of couples, too..."
    menu:
            
        "How's your new book coming along?":
            $ renpy.block_rollback()
            i "So, how's the new book coming along? You had a reunion with your editor this Friday, right?"
            h "Oh, yeah... I just showed her what I have so far..."
            i "Did she like it?"
            h "She did. She always does..."
            i "That's good, isn't it? It means you're creating something flawless."
            h "I don't know. I guess I'm my own worst critic and I revise and refine everything a lot before showing it to anybody..."
            i "That's a lot of dedication..."
            h "Yeah... I end up spending most of my free time doing that. I would be doing just that right now, if you hadn't asked me out..."
            $ fian = "n"
            "Maybe I should learn something from Holly's dedication if I wanted to be a professional writer just like her..."
            h "What about you? You told me you were going out with your friends this weekend, right?"
            
        "How was your weekend, Holly?":
            $ renpy.block_rollback()
            i "So Holly, how was your weekend?"
            h "Oh, you know... Nothing special."
            h "I've been writing, reading... I finished a TV series I was watching..."
            h "The same stuff I always do on weekends."
            i "Sounds like you don't go out much."
            h "I guess not... I mean, I do, but I'm mostly on my own most of the time."
            i "So this is an exception?"
            $ fholly = "happyshy"
            if ian_holly < 10:
                $ ian_holly +=1
                play sound "sfx/friendup.mp3"
                show friend_up
            h "You could say it is..."
            hide holly2
            show holly at rig
            with short
            h "What about your weekend? I'm sure it's been way more interesting than mine."
            
        "You're very quiet":
            $ renpy.block_rollback()
            "There was an awkward silence while we walked, like we couldn't find an appropriate topic for conversation..."
            i "You're awfully quiet, Holly..."
            $ fholly = "blush"
            hide holly2
            show holly3 at rig
            with short
            h "Oh... I'm sorry..."
            i "Don't be sorry... I think maybe you're too tense. You shouldn't be."
            h "I'm not tense, I-{w=0.3}I'm..."
            h "I'm sorry."
            $ ian_holly -=1
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ fian = "worried"
            "Looked like I only managed to make her feel more pressured..."
            "It would have to be me who broke the ice."
            $ fian = "n"
            i "So, you know, yesterday I went out with my friends..."
            
    i "We went out to a night club called Blazer. Have you heard about it?"
    h "Nope... I have no knowledge at all when it comes to these things."
    i "It was my first time going there, but I have a friend who works there so he insisted we go..."
    h "And you like those kind of places?"
    if ian_chad > 2:
        i "They're cool, yeah. Maybe the music's not my favorite, but it's fun."
        h "Really? For some reason it's hard for me to imagine you dancing and drinking..."
        i "You should come and see me one of these days, then!"
        $ fholly = "happy"
        "She laughed a bit."
    if ian_chad > 0:
        i "Well... I wouldn't say I do, but I can cope."
        $ fholly = "n"
        h "Cope? Sounds like you're forcing yourself to go there..."
        i "It's not like that. I can have fun there, especially if I'm with my friends."
        i "It's mostly the music I don't like."
    else:
        i "Not really. They're pretty awful."
        $ fholly = "happy"
        "She giggled."
        h "I thought as much... You don't look like the type of person who enjoys night clubs."
        i "I mean, I can go from time to time. They're not my favorite places, but with the right people it can be fun..."
        i "And with enough drinks too, of course."
    $ fholly = "n"    
    h "I've never been to a place like that..."
    $ fian = "surprise"
    i "You've never ever gone out clubbing?"
    hide holly
    hide holly2
    hide holly3
    show holly3 at rig 
    with short
    h "No... I never saw the appeal..."
    $ fian = "n"
    $ fholly = "sad"
    h "Or maybe I was just a bit scared of the atmosphere... I know people there get a bit crazy."
    h "A crowded space where everybody is drinking, trying to hook up and that kind of thing..."
    menu:
        "{image=icon_wits.png}It's sublimation" if ian_wits > 3:
            $ renpy.block_rollback()
            if encourage_holly < 4:
                $ encourage_holly += 1
            $ fian = "smile"
            i "You have to think about it as a way to sublimate human passions. It's our Dionysian aspect."
            $ fholly = "n"
            hide holly3
            show holly2 at rig
            with short
            h "You mean like the Greek Gods, Dionysos and Apollo?"
            i "Exactly. Apollo is the God of order and rational thinking, while Dionysos is the God of chaos, emotions and instincts."
            i "It's hard to refute that we human beings are made of both those aspects, and it's important to find a balance between them..."
            h "I've been neglecting Dionysos a bit too much, I guess..."
            i "It's not good to repress those needs. That's why it's good to go out and drink and dance from time to time."
            $ fholly = "happy"
            hide holly2
            show holly at rig
            with short
            h "That's wise advice. I'll remember that."
            $ fholly = "smile"
            
        "{image=icon_charisma.png}It's healthy!" if ian_charisma > 3:
            $ renpy.block_rollback()
            if encourage_holly < 3:
                $ encourage_holly += 1
            $ fian = "smile"
            i "It's healthy to do so, even if it's just from time to time!"
            h "Drinking alcohol all night long doesn't sound too healthy..."
            i "You can do it in moderation... But I'm not referring to that."
            i "It's healthy for the mind. You can't spend all day everyday just working, or closed off from the world..."
            i "Yeah, going out at night can be chaotic and weird, but it's at those moments when some special bonds are formed between people and friends."
            h "I guess that's something I've been missing... But I don't know if it's something I can do..."
            i "You're stressing out too much. You should just do it one of these days and you'll see it's not so terrible."
            $ fholly = "smile"
            hide holly3
            show holly2 at rig
            with short
            h "You're probably right. Thank you, Ian."
                
        "It's not for everybody":
            $ renpy.block_rollback()
            i "Well, I guess it's not for everybody..."
            h "Probably not."
            i "Still, you could try it one of these days."
            h "It's not something I'm especially interested in, but who knows..."
            $ fholly = "n"
            hide holly3
            show holly2 at rig
            with short
    
    if ian_switch_review or ian_honest_review:
        if v5_ian_showup:
            h "By the way, you haven't told me yet what happened Friday!"
            i "Oh, that..."
            "I told Holly how I snuck into the office and about Mr. Ward's job proposal."
            h "That was a bold move on your part!"
            i "Yeah... At least I hope I managed to stand out. Maybe Mr. Ward will remember me the next time we meet."
            h "I'm sure he will."            
            $ fholly = "sad"
            h "I guess Minerva wasn't very happy about your intervention..."
            if v5_hand_proposal:
                i "Not one bit. And even less when I handed Mr. Ward my book proposal."
                h "You think he'll look at it?"
                i "I can't know... But I'd say I made a good impression. I also have a feeling there's a good chance of me getting that job!"
            else:
                i "Not at all. If stares could kill I'd probably be dead right now..."
                i "But I think it was worth it. I have a feeling there's a good chance of me getting that job!"
            $ fholly = "happy"
            h "I really hope you do!"
        else:
            $ fholly = "sad"
            h "Oh, by the way, I talked to someone from the office. Turns out the rumor I told you about was true after all."
            $ fian = "sad"
            i "So Mr. Ward really offered a co-working opportunity?"
            h "They're looking for beta readers, yeah."
            i "Sounds like a better job than the one at the magazine... But I have other plans."
    else:
        h "By the way, you haven't told me yet what happened Friday!"
        i "Oh, that..."
        "I told her about Mr. Ward's visit at the magazine and how I tried to secure his job offer."
        h "That was a bold move on your part!"
        i "Yeah... At least I hope I managed to stand out. Maybe Mr. Ward will remember me the next time we meet."
        h "I'm sure he will."            
        $ fholly = "sad"
        h "I guess Minerva wasn't very happy about your intervention..."
        if v5_hand_proposal:
            i "Not one bit. And even less when I handed Mr. Ward my book proposal."
            h "You think he'll look at it?"
            i "I can't know... But I'd say I made a good impression. I also have a feeling there's a good chance of me getting that job!"
        else:
            i "Not especially, but what can she do? I did nothing wrong."
            h "No, you didn't."    
    $ fian = "smile"
    $ fholly = "smile"
    "We decided to sit down on the grass to keep chatting."
    "Holly was a really nice girl. She was shy and a bit too insecure, but you could tell she had a really good heart."
    "And she was so cute... Even though she seemed oblivious to it."
    "Or maybe she just didn't want to believe it."
    if ian_go_holly > 1:
        "It was such a shame, because I really liked her..."
        "As we spent more time together and I got to know her a bit better I felt the soft spot I had for her growing..."
    "Talking to her was great, too. She knew a lot about literature and had read a lot more than I had. I could learn a lot from her."
    "And we also had similar tastes about pop culture and shared a lot of opinions."
    $ fholly = "happy"
    h "Ha ha ha, that's right... Oh, I'm having so much fun today. Thank you. Ian."
    i "I told you before, you don't have to thank me. I'm enjoying this too, you know?"
    h "But I'm sure you had other stuff to do on a Sunday afternoon. And you're investing your time in me..."
    i "I don't look at this as an investment."
    i "I could choose what to do this afternoon, and from all those possibilities hanging out with you was the one I liked most."    
    $ fholly = "blush"
    hide holly
    hide holly2
    show holly3 at rig
    with short
    h "Oh, really...?"
    i "Sure. I'm not here out of obligation. I thought that much was clear."
    h "Um, so... I never asked you this, but..."
    h "Do you have a girlfriend?"
    $ fian = "blush"
    "I wasn't expecting that question out of the blue."
    menu:
        "No, but I like someone":
            $ renpy.block_rollback()
            $ v5_tell_holly = "wantgf"
            i "No, I don't, but... I like someone."
            $ fholly = "blush"
            h "Oh...!"
            h "Oh, of course... It's normal."
            i "What's normal?"
            h "That you like... I mean, that you like someone."
            h "I like someone too, but... But that's not important..."
            $ fian = "n"
            i "Why not?"
            h "It's just a silly thing... Forget it."
            h "Look, it's getting late! Sun's setting."
            i "Yeah. I guess we should be going."
            
        "Not at the moment":
            $ renpy.block_rollback()
            $ fian = "n"
            $ v5_tell_holly = "nogf"
            i "No, I don't have one. Not at the moment."
            h "And... something similar to one?"
            if ian_lena_sex:
                "What was Lena to me, exactly? We had slept together already, so I could call her a fling..."
                "We hadn't spent too much time together yet, after all... But she threatened to be of significance."
                "No, she already was..."
                if ian_alison_sex:
                    "There also was Alison, but... No, we had no attachment other than friendship."
                    "It wasn't the same as I felt for Lena."
            elif ian_alison_sex:
                "There was Alison, but... No, we had no attachment other than friendship."
                if v4_ian_date:
                    "Of course there was Lena... But nothing had really happened yet."
                    "But she threatened to be of significance..."
            if ian_cherry_sex or ian_emma_sex:
                "I couldn't call any of my other flings anything more than that."
            $ fian = "smile"
            if ian_lena_sex or ian_alison_sex or ian_cherry_sex or ian_emma_sex:
                i "No, nothing similar other than some occasional fling..."
            else:
                i "No, nothing of that sort."
            h "Oh, I see... That's weird, I thought you'd have one..."
            i "Really? How come?"
            $ fholly = "blush"
            h "Well you're a cool guy, I'd imagine a lot of girls would like to be with you..."
            i "Come on, Holly, you're over-appreciating me!"
            $ fholly = "n"
            h "I don't think so..."
            i "Come on, now I'm blushing... Or maybe it's the light from the setting sun. It's gotten late."
            h "Yeah. I guess we should be going."
            
        "No, and I don't want one":
            $ renpy.block_rollback()
            $ v5_tell_holly = "hategf"
            $ fian = "n"
            i "No, I don't have a girlfriend... And I don't want one right now."
            $ fholly = "n"
            h "Oh, I see..."
            h "..."
            h "I know it's rude to ask, but may I know why...?"
            i "Let's say my last relationship didn't end too nicely. And I don't have the stomach for that again."
            h "I'm sorry to hear that... I can relate to that, somehow."
            h "Heartbreak is... Probably the worst feeling in the world."
            h "Like losing a loved one, but because it's them who chose to leave you..."
            i "Yeah... But I'd prefer not to talk about that just now."
            $ fholly = "surprise"
            h "Oh, I'm sorry! I said too much...!"
            $ fian = "smile"
            i "No, it's OK. It's just that I don't want to sour such a nice afternoon with bitter subjects."
            i "Speaking of which, the sun's setting already..."
            h "Yeah. I guess we should be going."
    
    $ fian = "n"
    $ fholly = "happy"
    h "The afternoon went by so fast!"
    i "Yeah, it did."
    h "Well then, see you tomorrow at the office."
    i "Bye, Holly."
    stop music fadeout 2.0
    hide holly
    hide holly2
    hide holly3
    with short
    show ian at truecenter with move
    $ fian = "n"
    "I didn't know if I should've told her that..."
    if v5_tell_holly == "wantgf":
        i "I wonder what she understood, but it seemed to get her a bit uncomfortable."
        i "Maybe she thought I was speaking of her?"
        if ian_go_holly > 1:
            i "She's not entirely wrong, though..."
        else:
            i "She's cute, though..."
    if v5_tell_holly == "notgf":
        if ian_lena_sex or ian_alison_sex or ian_cherry_sex or ian_emma_sex:
            if ian_lena_sex and ian_alison_sex: 
                i "Maybe I should've told her about that thing I'm having with Lena... and Alison."
            elif ian_lena_sex:
                i "Maybe I should've told her about that thing I'm having with Lena..."
            elif ian_alison_sex:
                i "Maybe I should've told her about that thing I'm having with Alison..."
            if ian_cherry_sex or ian_emma_sex:
                i "Mentioning Emma or Cherry didn't really make sense."
            elif ian_emma_sex:
                i "Mentioning Emma didn't really make sense."
            elif ian_cherry_sex:
                i "Mentioning Cherry didn't really make sense."
            "Other than that I had been pretty honest in my answer."
        else:
            i "I guess the most honest answer is the right one."
    if v5_tell_holly == "hategf":
        i "I don't know if mentioning what happened with Gillian will make her thing I'm a butthurt ex."
        i "Even though I kind of am... Damn."
    jump v5iansundayend       
            
    
##IAN SUNDAY END ############################################################################################################################################################################################################
     
label v5iansundayend:
    
    scene ianroomnight with long
    if v5_holly_date:
        play music "music/normal_day2.mp3" loop
        "I went back home and decided to do some writing to end the weekend on a productive note."
    else:
        stop music fadeout 2.0
        play music "music/normal_day2.mp3" loop
        "I stayed in my room the whole afternoon, doing some writing to end the weekend on a productive note."
    $ ian_look = 2
    $ fian = "n"
    scene ianroomnight 
    show v2_ianwrite 
    with long
    if book_scifi:
        "I had been making good progress with my {color=#3FB305}Science Fiction{/color} novel."
    if book_fantasy:
        "I had been making good progress with my {color=#B30505}Fantasy{/color} novel."
    if book_historical:
        "I had been making good progress with my {color=#D1B402}Historical{/color} novel."
    "I had defined the genre, the call to adventure and the enemy."
    "But every good story has to have a mentor for the protagonist."
    "Someone who guides the main character during his first steps and teaches him about the world... and about himself."
    i "What kind of mentor would be fitting for my story?"
label v5_writebookchoice:
    call screen book_screen_4
    if book_card3 == "talking_animal":
        i "A talking animal sounds fun and cute. It could be a snarky frog or a wise and fluffy dragon."
        i "Or a genetically engineered monkey! The possibilities are endless..."
        i "And maybe I could sneak in a clever metaphor, depending on the animal I choose..."
        menu:
            "Choose this card":
                $ renpy.block_rollback()
                if book_scifi:
                    i "The genetically engineered monkey sounds good... Or maybe a cybernetic raccoon..."
                if book_fantasy:
                    i "It goes well with the fantasy theme, that's for sure."        
                if book_historical:
                    i "Maybe the main character is a bit crazy and he talks to the swines?"
                        
            "Try something else":
                $ renpy.block_rollback()
                jump v5_writebookchoice
        
    if book_card3 == "sage":
        i "The best mentor is a sage. A wise man or a great wizard, like Merlin."
        i "Every great hero has one mentor of that kind..."
        i "An older hero who could not fulfill his destiny and is now entrusting it to he protagonist..."
        menu:
            "Choose this card":
                $ renpy.block_rollback()
                if book_scifi:
                    i "I could make him a scientific genius who's repentant from working for the bad guys..."
                if book_fantasy:
                    i "This will be easy. This archetype fits right in."        
                if book_historical:
                    i "This could be a very interesting experience to portray a great man from History in the book."
                    i "Make him explain his views, which ended up shaping the world we live in..."
                        
            "Try something else":
                $ renpy.block_rollback()
                jump v5_writebookchoice
        
    if book_card3 == "anti_hero":
        i "Who says mentors have to be good-natured characters?"
        i "The protagonist could use some tough love from a battered and cynical veteran."
        i "Someone who would also show him first-hand the grim darkness of the world he's venturing into."
        menu:
            "Choose this card":
                $ renpy.block_rollback()
                if book_scifi:
                    i "Writing an anti-hero is always fun. He could be a galactic bounty hunter or a thug from the underworld..."
                if book_fantasy:
                    i "Writing an anti-hero is always fun. He could be a wandering monster hunter or a mercenary, a sword for hire..."        
                if book_historical:
                     "Writing an anti-hero is always fun, and I'm sure I can find a lot of characters like those in History."
                        
            "Try something else":
                $ renpy.block_rollback()
                jump v5_writebookchoice

    play sound "sfx/keyboard.mp3"
    "I wrote until dinner time and then some more."
    scene ianroomnight with long
    show ian with short
    i "Enough for today... At this rate I think I will make it in time for the contest."
    i "It's been a pretty intense weekend!"
    if v5_ian_showup:
        i "First Mr. Ward's visit at the magazine, and then the night out..."
    else:
        i "That night out surely was something."
    if v5_cindy_shoot:
        i "And the photo-shoot with Cindy, oh God..."
    if v5_alison_sex:
        "The after-party with Alison had been really enjoyable, too. The best part of the weekend, no doubt."
    elif ian_emma_sex:
        "The after-party with Emma had been as incredible as it had been unexpected."
        "The best part of the weekend, no doubt... And probably the wrongest, too..."
        
    if v4_ian_date:
        "I thought about Lena. I wished I could've seen her this weekend..."
        "I decided to text her."
        i "{i}Hey, how was your weekend?{/i}"
        "She replied right away."
        play sound "sfx/sms.mp3"
        l "{i}It's been a bit crazy!{/i}"
        i "{i}Seems you can't get a break even during the weekends!{/i}"
        l "{i}Seems like it! Sometimes I wonder if my life is even normal {image=emoji_laugh.png}{/i}"
        i "{i}Who says what's normal and what's not? Normal is boring, anyways.{/i}"
        l "{i}True, that. How about your weekend?{/i}"
        i "{i}I can't complain. It's been pretty interesting, too. But it could've been better.{/i}"
        l "{i}How so?{/i}"
        i "{i}If you had been in it {image=emoji_shy.png} {/i}"
        l "{i}I want to see you, too {image=emoji_love.png}{/i}"
        $ fian = "happy"
        if ian_lena_sex:
            "I had assumed she was as eager as me to see each other again, and this seemed to confirm it."
        elif v4_ian_kiss:
            "It seems I wasn't the only one interested in seeing each other. She seemed pretty eager, too!"
        else:
            "I had my doubts about Lena's interest, but this answer dispelled them a bit..."
        l "{i}Are you free this Wednesday?{/i}"
        i "{i}I can be.{/i}"
        l "{i}Good {image=emoji_laugh.png} It seems they're doing a live concert at the record store. Maybe we could go.{/i}"
        i "{i}Sounds like a great plan {image=emoji_smile.png}{/i}"
        l "{i}Awesome! See you on Wednesday, then!{/i}"
        $ fian = "smile"
        i "Cool... I'll be seeing her soon..."
        i "I can't wait."
    
    if v5_alison_jeremy:
        play sound "sfx/sms.mp3"
        i "Oh. A message from Jeremy."
        j "{i}Hey dude! How did the night end for you yesterday?{/i}"
        if ian_emma_sex:
            i "I don't think it's a good idea to tell him about Emma... Not through text, at least."
        i "{i}Nothing special, I just went straight home{/i}."
        j "{i}Mine was pretty awesome! Alison was on fire, dude!{/i}"
        if alison_voyeur:
            j "{i}I don't know if it was the alcohol or what, but... Look at this!{/i}"
            stop music fadeout 2.0
            "This time it was a video that Jeremy was sending me. It was about one and a half minutes long."
            play music "music/sex.mp3" loop
            show ian at left with move
            $ fian = "surprise"
            show v5_voyeur1 with long
            "A naked body appeared on screen. Alison's body."
            "I couldn't see her face, but her voice was clear."
            $ fian = "blush"
            a "What are you doing? How many pictures do you wanna take?"
            j "It's not a picture..."
            a "Come on, stop it and get serious."
            "Jeremy poked Alison's sex with the tip of his dick. He wasn't wearing a condom."
            j "I'm serious... I love how your pussy and my cock match."
            a "Stop saying weird things. Drop the phone and fuck me."
            j "You want it, huh? You want my dick inside you?"
            a "Yeah..."
            j "Then put it in."
            show v5_voyeur2 with long
            "Alison hesitated for a moment, but then she did."
            "She grabbed the shaft with her hand and pushed Jeremy's cock inside her pussy."
            a "Nhhh..."
            j "Oh yeah, baby. Slowly, don't hurt yourself..."
            "She had to do it really slowly. It seemed she had trouble fitting it in..."
            "Jeremy's manhood disappeared slowly but surely though, swallowed by Alison's pussy."
            j "Fuck, you're so tight."
            a "Can you stop filming now?"
            j "Don't worry, your face's not showing."
            a "I hope not... Nhhh...!"
            show v5_voyeur3 with long
            "Jeremy began rocking his hips while still filming."
            "It surely looked like a tight fit, since he couldn't really slide his cock in and out easily."
            a "Oh fuck, you're so big..."
            j "You love it baby, don't you?"
            a "Be careful... You're almost tearing me apart..."
            "Alison's boobs bounced up and down with each of Jeremy's gentle thrusts. But it was clear he wanted to go faster."
            "He did gradually."
            j "Ohh baby, so tight...! I won't last long like this!"
            a "Cum outside!"
            j "Of course, baby... Open wide!"
            show v5_voyeur4 with long
            j "Nhaaah!"
            "Jeremy pulled out and jets of cum sprayed Alison's belly, breasts and even her face."
            a "You came so much again..."
            j "I told you, I cum buckets! Especially when the girl is as hot as you..."
            hide v5_voyeur4
            hide v5_voyeur3
            hide v5_voyeur2
            hide v5_voyeur1
            with long
            $ ian_jeremy_gallery = True
            $ ian_jeremy_pics.append("alison_voyeur_v5")
            "After that the video ended."
            show ian at truecenter with move
            "I couldn't believe I had just watched Jeremy fucking Alison. My two friends going at it..."
            if ian_alison_sex:
                "Well, not just a friend. The girl I had been sleeping with recently..."
            i "{i}Dude, do you think you should send me something like that?{/i}"
            j "{i}Incredible, isn't it?{/i}"
            i "{i}That's not what I'm saying... I mean, I doubt Alison would like knowing you sent this to me{/i}."
            j "{i}Well, who's gonna tell her? Not me! {image=emoji_laugh.png} {image=emoji_laugh.png}{/i}."
            j "{i}I'm just sending this to you because you're my bro and I trust you. And because you liked the other pic I showed you {image=emoji_devil.png}{/i}."
            "He had a point. I kinda told him I didn't mind him showing me more stuff like this..."
            "Looking at that video bothered me, though. Not only because I was watching my two friends going at it..."
            "But mostly because how much it turned me on."
        
        else:
            $ fian = "n"
            i "{i}So you two really ended the night at your place{/i}."
            if alison_jeremy == False:
                $ alison_jeremy = True
                if alison_jeremy_block:
                    j "{i}Yeah man. I know you were touchy about the subject, so I wanted to make sure it's OK with you{/i}."
                    $ fian = "serious"
                    i "{i}You know my position already{/i}."
                    j "{i}I know, but I thought you were gonna pull Alison last night, honest. But you left her alone!{/i}"
                    $ fian = "worried"
                    "That was true. The reason Alison jumped on his cock was because I had my interest somewhere else..."
                    i "{i}Anyway, what's done is done. I hope you two had fun{/i}."
                    "I wasn't particularly happy about that, but I couldn't really complain."
                    "I had chosen my priorities that night."
                if alison_jeremy_doubt:
                    j "{i}Yeah man. I know you were a bit uncomfortable with the subject, so I wanted to make sure it's OK with you{/i}."
                    i "{i}Well, that doesn't matter anymore, right? What's done is done{/i}."
                    j "{i}I thought you were gonna pull Alison last night, honest. But you left her alone!{/i}"
                    $ fian = "worried"
                    "That was true. The reason Alison jumped on his cock was because I had my interest somewhere else..."
                    i "{i}Anyway, I hope you two had fun{/i}."
                    "I didn't mind Jeremy bragging, but right now I wasn't interested in hearing it."
                    "Especially when the girl he was bragging about was Alison."
                else:
                    j "{i}You've been enjoying a fine specimen lately! It was time I got a taste, too!{/i}."
                    i "{i}You finally got what you wanted, huh?{/i}"
                    j "{i}I thought you were gonna pull Alison last night, honest. But you left her alone!{/i}"
                    i "{i}Well yeah... I had other stuff to take care of{/i}."
                    j "{i}Other stuff?{/i}"
                    i "{i}Anyways, I'm glad you had a good ending to your night{/i}."
                if alison_jeremy_block == False and alison_jeremy_doubt == False:
                    j "{i}Oh yeah, so much fun {image=emoji_devil.png} {/i}."
                    j "{i}She even let me take a sexy picture! Wanna see it? {image=emoji_crazy.png}{/i}"
                    menu:
                        "Show me":
                            $ renpy.block_rollback()
                            $ alison_voyeur = True
                            $ fian = "shy"
                            i "{i}OK, show me.{/i}"
                            play sound "sfx/xp.mp3"
                            show lust_up
                            $ ian_lust_xp += 1
                            call screen skillsup
                            "I knew I was doing something I shouldn't, but I couldn't refuse Jeremy's offer."
                            "Some kind of morbid curiosity made we want to take a look at Jeremy's and Alison's sexual intimacy..."
                            show ian at left
                            with move
                            show v4_alison_jeremy
                            with short
                            $ fian = "surprise"
                            i "Holy fuck!"
                            $ ian_jeremy_gallery = True
                            $ ian_jeremy_pics.append("v4_alison_jeremy.png")
                            "For a moment I couldn't believe my eyes. Her face was not entirely showing, but that was definitely Alison."
                            if v3_alison_sex:
                                "I had seen them and those were definitely Alison's tits... Wrapped around Jeremy's cock."
                            else:
                                "And she had her breasts wrapped around Jeremy's cock."
                            i "That motherfucker is hung like a horse. It's not even normal... And judging by Alison's mouth, she seems to be into it a lot..."
                            $ fian = "worried"
                            i "{i}How did you even take this pic? You asked her and she let you?{/i}"
                            j "{i}Pretty much, yeah! She said as long as her face wasn't showing...{/i}"
                            j "{i}And not to show it to anybody, which I won't, except to my bro {image=emoji_wink.png}{/i}" 
                            i "Damn..."
                            i "Probably all Hell would break loose if Alison found out I have this pic..."
                            "I looked at it again."
                            i "She's so fucking hot... And she looks so naughty, too..."
                            j "{i}I count on you keeping the secret, bro!{/i}" 
                            i "{i}Of course, I got you.{/i}" 
                            j "{i}Now don't go and masturbate to it! Just kidding, see you at the gym, man.{/i}" 
                            "Masturbate to it?"
                            i "..."
                            $ fian = "blush"
                            hide v4_alison_jeremy
                            with short
                            show ian at truecenter
                            with move
                            "I put the phone away."
                            i "Of course not..."
                            
                        "That's private":
                            $ renpy.block_rollback()
                            $ alison_no_voyeur = True
                            i "{i}No, dude... That's something private between you and her.{/i}"
                            i "{i}I shouldn't see it and you shouldn't offer to show it to me.{/i}" 
                            j "{i}OK, man! I just wanted to share it with you since you're my bro.{/i}"
                            j "{i}See you at the gym!{/i}"
                            i "What a guy..."
                            "I didn't mind Jeremy bragging, but right now I wasn't interested in hearing it."
                            "Especially when the girl he was bragging about was Alison."
              
            else:
                j "{i}Yeah, dude. She was practically begging for it{/i}."
                if ian_alison_sex:
                    j "{i}I thought you were gonna pull her! But you left her alone!{/i}."
                    i "{i}Well yeah... I had other stuff to take care of{/i}."
                    j "{i}Other stuff?{/i}"
                    i "{i}Anyways, I'm glad you had a good ending to your night. Thanks for inviting us and all that{/i}."
                else:
                    "Jeremy as he lived and breathed."
                    j "She's fun."
                "I didn't mind Jeremy bragging, but right now I wasn't interested in hearing it."
                "Especially when the girl he was bragging about was Alison."
        
    i "Well, time to call it a day."
    "I turned the computer off and went to sleep."
    stop music fadeout 2.0
    
##IAN MONDAY ##################################################################################################################################################################################################################
    
    $ month = "May"
    $ day = "Monday"
    $ week = 1
    scene blackbg
    with long
    call screen calendar
    $ fian = "n"
    $ ian_look = 2
    play music "music/normal_day.mp3" loop
    scene ianhome with long   
    show ian with short
    "Next morning I got up and prepared some coffee to kick-start my day before going to work."
    "I was in need of it..."
    i "Monday again... But today's the first of the month. Payday."
    "I checked my account through the phone. I had already received my salary, and also my father's stipend..."  
    if ian_stipend == 2:
        $ ian_money += 4
    else:
        $ ian_money += 3
    play sound "sfx/moneyup.mp3"
    show money_up
    $ fperry = "n"
    if ian_honest_review or ian_switch_review:
        $ ian_job_magazine = 1
        "This was the last month I would be earning my full salary, though. From now on I would be getting barely half of that..."
        if ian_stipend == 2:
            "I didn't like having to rely on Dad's money, but it was really helpful right now."
    show ian at lef with move
    show perry at rig with short
    p "Hey, g--{w=0.5}good morning."
    i "Hey."
    p "Today's the first of the month. R--{w=0.5}remember to pay the rent..."
    menu:
        "I'll pay":
            $ renpy.block_rollback()
            i "I know, I know..."
            $ ian_money -= 2
            play sound "sfx/moneydown.mp3"
            show money_down
            i "I've made the transfer."
            p "Cool."
            
        "Can I pay next month?" if ian_job_magazine == 1:
            $ renpy.block_rollback()
            i "Hey... With my boss cutting hours from my job money's a bit scarce right now."
            i "Can you hold off on my rent this month? I'll pay you next month."
            if ian_perry > 4:
                p "Oh... Well that sucks..."
                i "I'm sure you can ask your dad to help this month..."
                p "Well, I have some m--{w=0.5}money saved up from what my parents gave me for my birthday..."
                p "But you'll pay me back, right?"
                i "Of course, man. When have I not?"
                p "Alright. I hope you can f--{w=0.5}fix this situation with your job."
                i "Yeah, me too. Thanks, dude." 
                "With this I only had to worry about my monthly expenses, food, gym..."
                $ ian_owed_money += 1
                $ ian_money -= 1
                play sound "sfx/moneydown.mp3"
                show money_down
                
            else:
                $ fperry = "meh"
                p "D--{w=0.5}dude, we need to pay the bills, the food and all that..."
                $ fian = "serious"
                i "You mean I need to pay for those. I'm not paying a rent, I'm paying both our living expenses."
                p "We've already talked about this, and you agreed to it w--{w=0.5}when you decided to move here."
                i "It was you who offered me to come live here with you."
                p "And where else would have you gone when your p--{w=0.5}parents kicked you out?"
                i "Whatever man, I'll pay. Just get off my back."
                $ ian_money -= 2
                play sound "sfx/moneydown.mp3"
                show money_down
                
    i "Anyways, I'm off to work."
    scene magazine with long
    if ian_charisma > 3:
        $ ian_look = 3
    else:
        $ ian_look = 1
    $ fminerva = "mad"
    show ian with short
    if ian_job_magazine == 1:
        if v5_ian_showup:
            "I was a bit anxious going back to the magazine after showing up uninvited on Friday."
            "I knew I hadn't done anything wrong, but I had defied Minerva. I knew my fate was hanging from a thread..."
            "I sat down at my desk and began taking care of the assigned tasks. The day went on with surprising normalcy..."
        else:
            "I would've liked to be at the office last Friday, but I had to capitulate before Minerva's whims."
            "I couldn't afford to lose this job... as much as I disliked it."
            "I sat down at my desk and began taking care of the assigned tasks. The day went on normally."
        "I even found time to finish writing that mocking book review I had been working on."
        if ian_honest_review:
            "As soon as I got it done I posted it on-line for people to read and have a laugh."
        else:
            i "I should post it on-line for people to read and have a laugh..."
        if v5_ian_showup:
            $ fian = "worried"
            show ian at lef with move
            show minerva at rig with short
            "Minerva walked by and gave a sour look, but didn't say anything."
            hide minerva with short
            i "..."
            i "That was weird... I assumed she'd call me to her office to scold me or something..."
            i "I can't believe she'll let me off the hook that easily. I wished she would, though!"
            "I could pretend that I had no idea what she had in store for me, but I had some suspicions..."
            "And they weren't good."
            
    else:
        "I sat down at my desk and began taking care of the assigned tasks. I wondered if I would be free from this soon."
        "If I managed to land that new job..."
        show ian at lef with move
        show minerva at rig with short
        if v5_hand_proposal:
            $ fian = "worried"
            "Minerva walked to my desk, and I feared the worst."
            mi "I need to have a word with you."
            "I got up, ready to follow her to her office, but she gestured me to sit back again."
            mi "It'll be quick."
            mi "I found your attitude towards our guest unprofessional and disrespectful last Friday."
            i "I meant no harm."
            mi "You were a bother, though, and embarrassed me. I hope you're aware of how problematic that was."
            "I wanted to defend myself, but I knew I wouldn't get anything out of it."
            i "Yes, ma'am."
            mi "I hope nothing of that sort happens again."
            hide minerva with short
            i "{i}*Sigh...*{/i}"
            "Hopefully I wouldn't have to suffer under her for much longer."
        else:
            "Minerva walked by and gave a sour look, but didn't say anything."
            hide minerva with short
            "She could dislike me all she wanted, but I had done nothing wrong by asking Mr. Ward some questions."
        show ian at truecenter with move
        i "I really hope I get that job..."
    stop music fadeout 2.0
    jump v5lenafriday

################################################################################################################################################################################################################
## LENA FRIDAY ################################################################################################################################################################################################################
################################################################################################################################################################################################################

label v5lenafriday:
    define mk = Character ("Mike", color="#AB2B44")
   
    $ ian_active = False
    $ lena_active = True
    $ week = 4
    $ month = "April"
    $ day = "Friday"
    scene blackbg
    with long
    show active_lena
    with long
    pause 1.0  
    scene blackbg
    with long
    call screen calendar
    scene cafe with long
    play music "music/normal_day2.mp3" loop
    $ flena = "n"
    $ lena_look = 1
    $ ivy_look = 1
    $ fivy = "smile"
    $ fed = "n"
    show lenawork with short
    "It was a quiet afternoon at the café, considering it was Friday."
    $ flena = "sad"
    "I would miss working in this place... I have no idea when, but if things didn't get better soon, my time here would be done."
    if lena_robert_sex:
        "I still had a few nights a week at the restaurant, but they didn't amount to much..."
    else:
        "This had been my last week at the restaurant, too. I would find myself completely jobless very soon..."        
    if v3_seymour_reject:
        $ flena = "worried"
        l "Now I wonder if I should've accepted Seymour's proposal..."
        "It was the only other job offer that had presented itself, but no... I didn't like the guy."
        "And what he said... That I would regret not accepting and would come back to him begging..."
        $ flena = "serious"
        l "No way."
    else:
        "At least there was my collaboration with Seymour Ward."
        "He seemed interested in keeping to work with me, and he was not short on money, that much was clear."
        "I wasn't sure how profitable that business relationship could end up being, but it was my security net right now."        
    $ flena = "n"
    if stalkfap:
        l "I should try and grow that Stalkfap thing... Ivy always tells me how profitable it is for her."
    else:
        l "I wish I could get some money out of Peoplegram, but I don't have nearly enough followers."
    if v4_danny_shoot:
        "This Sunday I had booked a photo-shoot with Danny. I would get some good material I could post."
    if v4_stan_shoot:
        l "I need to tell Stan to take some pictures of me so I can upload something..."
    if cafe_steal:
        $ flena = "drama"
        "My money problems were so bad I had even resorted to stealing from Molly and Ed..."
        "I felt terrible about it, but I really needed that extra cash."
        "It wasn't my fault life was putting me in such a dire position... I wished things could be easier for a chance."
    elif cafe_help:
        $ flena = "serious"
        "I wasn't someone to give up that easily, though."
        "I didn't want Ed and Molly to have to close up shop... It was not fair."
        l "I need to come up with something that could help them..."
        $ flena = "n"
    else:
        l "I hope I can solve my money problems soon."
    show lenawork at rig with move
    show ed at lef with short
    ed "How's it going, Lena?"
    l "All good. Just cleaning these glasses."
    ed "Not many customers today either..."
    $ fed = "sad"
    "He sighed."
    ed "I guess expecting the things to change is just wishful thinking."
    l "The last thing one should lose is hope, right?"
    ed "What I'm worried about is what happens when hope is lost... Is there something left?"
    $ flena = "sad"
    $ fed = "n"
    ed "Oh, but don't let this old man sour your mood with his ramblings. You're still young and your life is full of potential."
    if ed_callout:
        ed "I'm sorry about giving you the two weeks notice prematurely... But I'm worried about the situation and all."
        ed "I hope you understand..."
        l "Of course..."
        $ fed = "sad"
        ed "And I'm sorry about that day, you know... When you had to call me out."
        ed "I know I bothered you. You made it very clear that day."
    elif v1_ed_flirt:
        $ fed = "perv"
        ed "I will miss having such a young and beautiful girl around, that's for sure."
        $ flena ="happy"
        l "Ha ha, don't be silly."
        ed "It's true... Not everyone can say they have a model working for them!"
        ed "I really like the pictures you post on your Peoplegram... They're so beautiful... and so are you, of course!"
        ed "I'm sure you'd be successful with your modeling career!"
        $ flena = "smile"
        l "Thanks, Ed."
        $ fed = "smile"
    elif v1_ed_truth:
        $ fed = "smile"
        ed "I'm sure you'll have a lot of success with your modeling career!"
        $ flena = "n"
        l "I wouldn't say it's a career..."
        ed "You can make it one if you want to! I really like the pictures you post on your Peoplegram, they are so beautiful!"
        ed "And so are you."
        l "Thanks, Ed..."
    else:
        $ fed = "smile"
        ed "I'm sure you'll find something better than this job. It was just a temporary thing either way, right?"
        $ flena = "n"
        l "Well..."
    show ed at lef3
    show lenawork at rig3
    with move
    show ivy with short
    v "Hey there girl!"
    $ flena = "smile"
    $ fed = "surprise"
    l "Ivy! What are you doing here?"
    v "I was in the area and decided to drop by and see you. Have you everything ready for tonight?"
    ed "Is this a friend of yours, Lena?"
    l "Yeah, a friend from high school."
    v "I'm Ivy, nice yo meet you! You must be Lena's boss. She always speaks highly of you!"
    ed "She does?"
    v "Yeah, she always says how nice you are, and how much care you take of her!"
    $ fed = "perv"
    ed "Oh, I see, yeah..."
    v "She's super happy to have you as a boss, right, Lena?"
    l "Uh, sure..."
    v "And she told me you were handsome. I see she wasn't lying!"
    ed "Oh, well, heh heh..."
    v "Tonight I'm taking Lena out partying. It's been ages since we went out together and I'm so thrilled!"
    v "I'm sure you can let her off early today, right?"
    ed "Uh, well, there aren't many customers today, so..."
    v "Great! You're really the best boss in the world, right, Lena?"
    l "Yeah, of course..."
    v "Come on, get changed and let's get outta here. I'll be waiting outside!"
    hide ivy with short
    l "Is it really OK for me to go?"
    ed "Sure, sure... Have fun... See you on Monday, Lena!"
    $ flena = "smile"
    l "Thanks, Ed."
    scene street with long
    "I got changed and left."
    show lena at rig
    show ivy at lef
    with short
    v "There you are."
    l "What was that about?"
    $ fivy = "flirt"
    v "That was so easy! You could manipulate your boss so easily!"
    $ flena = "n"
    l "You're terrible... I'm not gonna do that."
    if v1_ed_flirt:
        "Actually, I had already done it once... When I asked him to let me off early by letting him see me in my underwear..."
    elif ed_callout:
        v "Maybe if you did he wouldn't be firing you."
        l "He's firing me because the business is crumbling..."
    v "Anyways, I just saved you a couple of hours of work so you can be fresh and rested tonight. You're welcome!"
    "We had talked about going out to party last week and Ivy had insisted I went to the club she worked on tonight."
    "Louise would be coming with me, since I didn't want to be left alone while Ivy was busy working."
    v "You have everything ready?"
    l "What should I have ready other than myself?"
    v "Your outfit! What are you going to wear?"
    l "I don't know... I'll find something in my closet."
    $ fivy = "n"
    v "I don't know... It's not like I don't trust your taste, but you've been out of the game for far too long..."
    l "What, you want to be my stylist?"
    v "You wouldn't be able to find anyone better!"
    "She took a look at me, thinking."
    v "Mhh, in fact..."
    v "Come with me to my place! I'll give you something! You have time, right?"
    l "OK, let's go."
    stop music fadeout 2.0
    scene street with long
    "Ivy didn't live too far away. We lived in a small city, after all."
    play music "music/jeremys_theme.mp3" loop
    play sound "sfx/door_home.mp3"
    scene ivyroom with long
    $ fivy = "smile"
    show ivy at lef
    show lena at rig
    with short
    v "Here we are! When was the last time you came to my place?"
    l "Too long ago. You made some changes... All this furniture is new, and you even got a pole installed!"
    v "Yes, girl! Business blooming!"
    l "You bought all of it with the money you make from Stalkfap?"
    v "Stalkfap, the classes at the gym and the gig at Blazer, yeah. But mostly Stalkfap, hee hee!"
    v "I even have a wish list and some guys buy things for me like clothes and stuff..."
    v "Speaking of which... Here."
    "She opened her closet and searched for something. It was full of fancy shoes, bags and all kinds of clothes and dresses."
    v "Take this top. I really like it, but it's a bit too small for me. I think it's perfect for you!"
    v "You can wear it tonight, just find something cute to match with it. A pair of jean shorts will do."
    l "Thanks. So I see things are going really well for you..."
    $ fivy = "flirt"
    v "I can't complain! To be honest, I could quit my two jobs right now. I'm making enough just with Stalkfap and the photo-shoots!"
    $ flena = "surprise"
    l "Really? That's amazing!"
    v "I'm a hard-working girl, though, and I want to save up as much money as possible, so I will keep them."
    v "The job at the club is pretty fun after all, and I need to keep myself in shape, so I might as well get paid for going to the gym!"
    $ flena = "smile"
    l "I'm really happy for you. You've set up a good life for yourself."
    v "There's still so much to be done. I want to get far..."
    $ fivy = "n"
    v "But you have me a bit worried, girl... It's like since you broke up with Axel you've been struggling with everything."
    $ flena = "n"
    l "Well, my struggles date from before Axel, you know that. But it's true that now things are getting pretty complicated."
    v "They shouldn't be! I mean, you have so much potential! I'm your friend and I know it."
    if stalkfap:
        v "How's your Stalkfap account doing?"
        if v3_pg_ian:
            l "Well... I haven't really gotten much out of it..."
            v "Really? How come?"
        else:
            l "I got some pocket money out of it."
            v "Really? That's good... But you can get so much more out of it!"
        v "Let me see what you've been uploading."
        show lena at rig3
        show ivy at lef3
        with move
        show v3_stalkfap2
        if v3_pg_ian:
            show v3_stalkfap3
        else:
            show v3_stalkfap4
        with short
        "I lent Ivy my phone and she scrolled down my profile."
        $ fivy = "sad"
        v "What's this? You have so very few subscribers!"
        v "I'm not surprised, considering what you've been uploading..."
        $ flena = "sad"
        l "What's wrong with it?"
        v "There's barely four pictures here!"
        l "I've only had it for a couple of weeks!"
        v "Still... And they're just the same pictures you post on Peoplegram but without censoring. You need to step it up, girl!"
        if v4_danny_shoot or v4_stan_shoot:
            l "Well, I don't have much to post! I'll be doing a photo-shoot next week, though, to get some new material..."
        else:
            l "Well, I don't have much to post! I need to do new photo-shoots to get some new material, but I don't have any lined up..."
        v "Forget about photo-shoot! Haven't you been listening to what I told you?"
        v "Professional pictures are good for Peoplegram, but what the guys want to see on Stalkfap are sexy selfies!"
        v "It's so easy it's ridiculous! You need to step up your game, seriously!"
        $ flena = "n"
        l "I'll think about it..."
        hide v3_stalkfap2
        hide v3_stalkfap3
        hide v3_stalkfap4
        with short
        show lena at rig 
        show ivy at lef 
        with move
    else:
        v "You never checked out Stalkfap like I told you, right?"
        if v3_check_stalkfap:
            l "I did, actually... I have an account, but never uploaded anything."
            v "Why not? Do it!"
        else:
            l "No, you know that's not my style..."
            v "Ah, bullshit. Don't tell me you're really worried about that?"
        $ flena = "worried"
        l "I don't know... I don't really feel comfortable with it."
        v "Sometimes I just don't get you, girl! You're already posing nude in front of the camera and posting it on Peoplegram."
        v "Why don't you get some real money out of it?"
        l "Because it's not the same... I consider what I do artistic, it has sensibility..."
        v "Oh, come on, don't be a snob. You're not like that. The art is in the eye of the beholder, right?"
        v "Most guys just want art that's a bit spicier!"
        v "I know you're really stressed out with your current situation and all that. But you have the perfect solution right here!"
        "Ivy was really convinced I should do it... I had decided against it in the past, but now things were a bit different."
        "I was in dire need of some economic stability, but was selling my nudes on Stalkfap a business I felt really comfortable with?"
        menu:
            "I'll do it":
                $ renpy.block_rollback()
                $ stalkfap = True
                $ stalkfap_pro = 1
                $ flena = "blush"
                l "Alright... I guess I really need to try this out..."
                $ fivy = "flirt"
                v "Of course! You have a problem and here's the solution! I wouldn't insist if it wasn't working miracles for me!"
                $ flena = "n"
                l "Yeah, I can see that."
                if v3_check_stalkfap:
                    v "So, you already have an account..."
                else:
                    v "So, first of all, let's create an account..."
                v "Do you have any pictures in your phone you can upload?"
                l "I have some from my last photo-shoot with Danny."
                v "OK, let's post those first..."
                show lena at rig3
                show ivy at lef3
                with move
                show v3_stalkfap2 with short
                v "There, done."
                v "Do you have any sexy selfies to post, too?"
                l "Nope... I haven't taken those in a long time."
                v "Well, be sure to take a few and post them regularly. That's what subscribers really wanna see, you know?"
                v "Something homemade and intimate. And naughty, too!"
                $ flena = "blush"
                l "How naughty are we talking about?"
                v "The naughtier the better, of course. You know how guys are. You need to give them something they'll wanna spend their money on."
                v "Now you need to let people know you have set up this account. Let's post a link in your Peoplegram bio..."
                v "{i}\"To see the unedited pictures subscribe to my Stalkfap account\"{/i}."
                v "OK, you're ready yo go!"
                hide v3_stalkfap2 with short
                show lena at rig 
                show ivy at lef 
                with move       
                $ flena = "n"
                l "Thanks, Ivy. Let's see how this goes..."
                
            "It's not for me":
                $ renpy.block_rollback()
                $ flena = "n"
                l "I already thought about it when you first told me, and I stand by the same opinion."
                l "It's just not for me."
                $ fivy = "sad"
                v "I can't say I understand you, Lena... You have problems and here's a solution..."
                l "It could be a solution, for sure, but it's not a solution I feel comfortable with."
                l "Not that I have anything against it or people who do it, of course. But it's not the kind of content I want to produce with my image."
                play sound "sfx/xp.mp3"
                show wits_up
                $ lena_wits_xp += 1
                call screen skillsup
                $ fivy = "n"
                v "You've always been very stubborn! You know I only want to help you, but if that's how you see it I don't know what else I can do for you."
                l "Don't worry, I'll figure something out. And thanks for worrying about me."
                v "Always!"
    $ fivy = "n"    
    v "So, besides this, anything else going on in your life?"
    if ian_lena_sex:
        $ flena = "flirt"
        l "Actually... Ian and I finally slept together."
        $ fivy = "flirt"
        v "You slut! It was about time!"
        v "How was it?"
        l "It was super nice, actually. Even better than I had hoped, considering it was our first time..."
        if lena_robert_sex:
            v "Better than with that other guy? Robert, right?"
            if v4_robert_sex:
                l "Yeah, much better... I mean, with Robert it's fine, but with Ian..."
            else:
                l "Yeah, much better... With Robert it was pretty \"meh\", you know. But with Ian..."
        else:
            v "Really? That's so cool! I'm glad, girl!"
        l "It's like we have so much chemistry."
        v "Those are the good ones. Be sure to keep him around!"
        $ fivy = "serious"
        v "But don't you be catching feelings now, you hear me?"
        $ flena = "sad"
        l "Well..."
        v "That will only bring trouble, and you have enough on your plate right now."
        $ fivy = "smile"
        v "What you need now is to take hold of your own life and set things straight. Don't let some guy complicate things for you."
        v "You've had enough with Axel, believe me. Too soon to get tangled into more romantic bullshit."
        $ flena = "n"
        l "It would seem like you're allergic to it, by the way you're talking."
        v "I'm doing more than fine without any of that!"        
    elif v4_ian_kiss:
        $ flena = "shy"
        l "Oh, well... We went on a date the other day, and we made out..."
        $ fivy = "flirt"
        v "Ohhh, so you fucked him already?"
        l "No, not yet..."
        $ fivy = "sad"
        v "What? How come? Why not?"
        $ flena = "blush"
        l "Well, we're getting there... But I guess we don't wanna rush things. I really like him..."
        $ fivy = "serious"
        v "Don't you be catching feelings now, you hear me?"
        $ flena = "sad"
        l "Well..."
        v "That will only bring trouble, and you have enough on your plate right now."
        $ fivy = "smile"
        v "What you need now is to take hold of your own life and set things straight. Don't let some guy complicate things for you."
        if lena_robert_sex:
            v "I like what you're doing with that Robert guy. That's how you should go about things now, keep guys at a distance and in their place."
        v "You've had enough with Axel, believe me. Too soon to get tangled into more romantic bullshit."
        $ flena = "n"
        l "It would seem like you're allergic to it, by the way you're talking."
        v "I'm doing more than fine without any of that!"        
    else:
        l "Not really..."
        v "What about that guy, Ian? You've been telling me about him..."
        if v4_ian_date:
            l "We went on a date the other day... But nothing really happened."
            $ fivy = "sad"
            v "What? Not even a kiss?"
            l "No..."
            v "What the hell? Stop wasting your time, then..."
            l "It's... complicated."
            $ fivy = "serious"
            v "Oh, for fuck's sake, no complicated things now! You have enough on your plate right now."
            $ fivy = "smile"
            v "What you need now is to take hold of your own life and set things straight. Don't let some guy complicate things for you."
            v "If he's down to fuck, go for it. If not, forget it. And, most important of all, don't be catching feelings for no guy!"
            if lena_robert_sex:
                v "I like what you're doing with that Robert guy. That's how you should go about things now, keep guys at a distance and in their place."
            v "You've had enough with Axel, believe me. Too soon to get tangled into more romantic bullshit."
            $ flena = "n"
            l "It would seem like you're allergic to it, by the way you're talking."
            v "I'm doing more than fine without any of that!"        
        else:
            l "Oh, that... I don't think it'll go anywhere. He's nice and I kinda like him, but right now is just not the time."
            v "Well, good for you to see it early. Last thing you need right now is to waste your time and get tangled on complicated bullshit."
            l "Yeah, I don't know. Things haven't been flowing as smoothly as one could hope. I guess we'll just stay friends."
            v "As long as he doesn't come begging for attention later... But yeah, don't waste too much energy with that."
            if lena_robert_sex:
                v "I like what you're doing with that Robert guy. That's how you should go about things now, keep guys at a distance and in their place."
            v "You've had enough with Axel, believe me. Too soon to get tangled into more romantic bullshit."
            $ flena = "n"
            l "It would seem like you're allergic to it, by the way you're talking."
            v "I'm doing more than fine without any of that!"        
    if v4_axel_date:
        v "And what about Axel? Haven't you seen or talked to Axel after meeting him last week?"
        $ flena = "sad"
        l "No... He hasn't kept in touch or anything..."
        v "Looks like he finally got the message and let it go."
        $ flena = "n"
        l "It would seem so. It's too early to tell, but... I have the impression he did."
    elif v3_axel_call:
        v "And what about Axel? Have you heard from him since that phone call?"
        $ flena = "sad"
        l "No... He hasn't tried to contact me or anything..."
        v "Looks like he finally got the message and he's leaving you be."
        $ flena = "n"
        l "I hope so! It's too early to tell, but... I hope that phone call was what he needed to let things finally go."
    else:
        v "And what about Axel? Has he given you any more trouble?"
        $ flena = "sad"
        l "No, I haven't heard from him or anything. He's keeping his distance it seems..."
        v "Probably he got scared after that incident at the hotel. Or he realized how out of line he was."
        $ flena = "serious"
        l "I hope so. He really did cross the line... I hope he's ashamed of himself and finally reflects on everything he did."
        v "In any case, they say no news is good news."
        $ flena = "n"
        l "Let's hope it stays that way."
    l "I think it's time for me to go home. I need to eat dinner and get changed. And Louise is waiting for me."
    $ fivy = "n"
    v "Oh, yeah. You're coming with her, right?"
    l "Yeah. You'll be working tonight, after all. I don't want to be alone in the club so some creeps can pester me all night."
    v "Don't worry, you'll be at the VIP area. There are no creeps there."
    l "There are creeps everywhere... Anyways, see you later!"
    stop music fadeout 2.0
    
    play music "music/normal_day2.mp3" loop
    scene lenahomenight with long
    "Once back home I ate dinner with Louise."
    $ louise_look = 1
    $ flouise = "smile"
    show lena at rig
    show louise at lef
    with short
    lo "I'm so hyped about tonight! I haven't been out partying since I started my masters!"
    l "Yeah, you've been really busy."
    lo "Yeah, only had time for Jeremy, and not as much as I would've liked..."
    $ flouise = "happy"
    lo "But I'm almost done with my exams! Today I just did the most important one!"
    l "You seem happy, so I assume it went well."
    lo "Yeah, I have a good feeling! I've been working my ass off, after all..."
    lo "But the best thing is that I feel like I've dropped a big weight off my shoulders."
    lo "All that's left are a couple of tiny things I know I'll get right and... I'll be done with my studies!"
    l "Then we have a reason to celebrate tonight."
    lo "Yeah! And I'll be seeing Jeremy, too... I'm curious to see him behind the bar."
    lo "I'm sure he looks very cool and handsome!"
    $ flena = "sad"
    if louise_jeremy:
        "I hadn't forgot the games Jeremy had been playing with Ivy... I hoped he would behave tonight."
    else:
        "Seems like Louise really decided to ignore my warnings about Jeremy and chose to believe him..."
    $ flena = "n"
    "We finished dinner and got ready to go out."
    lo "I'll take a shower first if you don't mind. I'll be quick."
    l "Sure, go ahead."
    hide louise with short
    show lena at truecenter with move
    "Louise seemed to be in a very good mood... It was a bit contagious."
    "I hadn't been in the mood to go out partying lately, but today... Today I had the feeling the night could be really fun."
    if lena_robert_sex and lena_robert_over == False:
        play sound "sfx/sms.mp3"
        "Just then I got a text from Robert."
        r "{i}Hey baby, how are you doing? It sucks that I can't see you this weekend!{/i}"
        l "{i}How's your vacation going?{/i}"
        "Robert had told me he would be traveling with a couple of friends this whole next week."
        r "{i}We're at the airport right now. I can't wait to be on those amazing beaches {image=emoji_tongue.png}{/i}"
        l "{i}I'm jealous! I wish I could afford a trip like that.{/i}"
        r "{i}I'm sure I would enjoy this trip a lot more if you came, too. Maybe next time we can go somewhere a few days, just you and me.{/i}"
        l "{i}I would love to go on vacation... But right now it's just wishful thinking, considering the situation.{/i}"
        r "{i}If it's about money, I don't mind inviting you.{/i}"
        l "{i}You know it's not just about money...{/i}"
        r "{i}Yeah, well... Anyways, do you have any plans for this weekend?{/i}"
        l "{i}Yeah, I'm just getting ready to go partying with a friend {image=emoji_smile.png} {/i}"
        r "{i}No way! You're partying just when I'm outside of town? No fair!{/i}"
        r "{i}Promise me you'll go out clubbing with me when I get back {image=emoji_flirt.png}{/i}"
        l "{i}Sure, we can do that.{/i}"
        r "{i}I'm getting on the plane! Talk to you later. Have fun tonight, even if it's without me!{/i}"
        l "{i}Have a nice trip {image=emoji_kiss.png}{/i}"
    if v4_stan_shoot:
        play sound "sfx/door.mp3"
        $ fstan = "n"
        $ stan_look = 1
        show lena at rig with move
        show stan at lef with short
        st "Uh... You and Louise are done with dinner, right?"
        l "Yeah, feel free to use the kitchen."
        st "OK. I didn't want to... disturb her."
        l "I'm sorry about what happened the other day..."
        st "Oh, it's not your fault. Don't be sorry..."
        l "By the way, Stan, I wanted to ask you a favor."
        $ stan = "surprise"
        st "A favor? What is it?"
        l "Have you been practicing your photography skills?"
        st "A bit, yeah..."
        l "I need someone to take pictures of me for my social media, and I need you to do it."
        $ fstan = "blush"
        st "Me? O-{w=0.3}of course! When?"
        l "How about tomorrow?"
        st "Sure. I don't have plans..."
        $ flena = "happy"
        l "Cool! Thanks, Stan."
        $ fstan = "shy"
        st "You're welcome..."
        
    scene lenaroomnight with long
    $ flena = "n"
    "Soon it was my turn to shower and after that I prepared to go out."
    if stalkfap:
        show lenanude with short
        "Just before getting dressed, what Ivy had told me about Stalkfap came to my mind."
        "If I wanted to make some money out of it I should post some selfies and that kind of stuff..."
        if stalkfap_pro > 0:
            "Since I had already decided I was in this for the money I went ahead with it."            
        else:
            "I got into this Stalkfap thing being a bit tentatively... But now I had to choose to what extent I wanted to invest in this."
            "Was I comfortable with that selfie thing?"
            menu:
                "Post a sexy selfie":
                    $ renpy.block_rollback()
                    $ stalkfap_pro += 1
                    l "I'm in this for the money, after all. I might as well do it."
                    
                "Stick with tasteful nudes":
                    $ renpy.block_rollback()
                    l "No, even if it doesn't get me too much revenue I prefer to stick to my style and vision."
                    l "What I do is tasteful art, not slutty selfies..."
                    l "Anyways, time to get ready for tonight!"
                    jump v5lenaprep
                    
        l "It's not that different from what I already do, after all..."
        scene lenaroomnight
        show v5_stalkfap1
        with long
        "I posed in front of the mirror and looked at the screen of my camera."
        l "Hmm... I want something's that has at least some style to it."
        "I found a pose I thought was both sexy and tasteful. Sensual."
        play sound "sfx/camera.mp3"
        with flash
        $ lena_lena_gallery = True
        $ lena_lena_pics.append("v5_stalkfap1.png")
        "I snapped the pic and spent a couple of minutes editing it, making sure the image was centered and the colors popped."
        "Then I uploaded it to Stalkfap with a caption:"
        "{i}\"About to choose a cute outfit for tonight's girls' night out!\" {image=emoji_music.png}{/i}"
        hide v5_stalkfap1 with short
        l "There, done."
    
label v5lenaprep: 
    $ lena_look = "sexy"
    "I opened my drawer and picked up some clothes."
    show lenabra with short
    l "I should wear something cute but also comfortable."
    scene lenaroomnight with long
    l "Let's see..."
    $ lena_look = 4
    show lena2 with long
    if v4_place == "fortress":
        l "This is what I wore on my date with Ian. I really like this outfit."
    else:
        l "I really like this outfit and I haven't found any occasion to wear it in a long time."
    show lena2 at rig with move
    play sound "sfx/meow.mp3"
    show lola at lef3 with short
    "My cat jumped on the bed and looked at me with curiosity."
    l "What do you think, Lola? You like it?"
    play sound "sfx/purr.mp3"
    hide lola
    show lolahappy at lef3
    with short
    l "I think so too."
    if lena_lust > 2:
        l "Oh, but I have to check out what Ivy lent me."
        hide lena2 with short
        l "Let's see..."
        l "..."
        if lena_lust > 5:
            $ flena = "flirt"
        if lena_lust > 4:
            $ flena = "shy"
        else:
            $ flena = "blush"
        show lenanude at rig
        show lena_sexy at rig
        with short
        if lena_lust > 5:
            l "Oh, wow! Look at this combination! Ivy's top is really cute!"
            l "Cute and sexy... I like how it suits me! Right, Lola?"
        elif lena_lust > 4:
            $ flena = "shy"
            l "Oh, wow... This combination sure is something..."
            l "Ivy's top is pretty sexy... And it suits me really well, right, Lola?"
        else:
            $ flena = "blush"
            l "Oh, wow... Ivy's top is sexier than I thought..."
            l "I don't know if I should wear it with these shorts... The combination is surely eye catching, right, Lola?"
        play sound "sfx/meow.mp3"
        hide lolahappy
        show lola at lef3
        with short
        if lena_lust > 5:
            $ flena = "slut"
            $ v5_lena_sexy = True
            l "Right, I like how I look! Pretty eye catching!"
            l "I know what I'll be wearing tonight. Oh, and it seems Ivy also included a choker to go with it..."
            hide lenanude
            hide lena_sexy
            with short
            $ lena_look = "sexy"
            $ lena_necklace = "choker"
            $ lena_makeup = 1
            $ flena = "happy"
            "I wore it and also applied some makeup to complete the look."
        else:
            l "What should I be wearing tonight?"
            menu:
                "{image=icon_lust.png}Ivy's top and shorts":
                    $ renpy.block_rollback()
                    $ v5_lena_sexy = True
                    if lena_lust > 4:
                        $ flena = "flirt"
                        l "The point of tonight is to go out, have fun and look good! And I really like how I look in this outfit..."
                        l "I'm definitely wearing this tonight!"
                    else:
                        $ flena = "shy"
                        l "Well, I guess the point of tonight is dressing sexy! And I sure do look good in this outfit..."
                        l "I guess I know what I'll be wearing tonight!"
                    l "Oh, and it seems Ivy also included a choker to go with it..."
                    hide lenanude
                    hide lena_sexy
                    with short
                    $ lena_look = "sexy"
                    $ lena_necklace = "choker"
                    $ lena_makeup = 1
                    $ flena = "happy"
                    "I wore it and also applied some makeup to complete the look."
                    
                "Tank top and pink shorts":
                    $ renpy.block_rollback()
                    if lena_lust > 4:
                        $ flena = "shy"
                        l "I guess this outfit is a bit too much... I'm not sure I will be comfortable with all the attention it can attract."
                        l "I just want to be relaxed and have fun tonight."
                    else:
                        l "It's too much, I don't want to look like I'm hoping to attract undesired attention. I just want to be relaxed and have fun tonight."
                    l "I'll better stick to my original idea."
                    hide lenanude
                    hide lena_sexy
                    with short
                    $ flena = "n"
                    $ lena_look = 4
                    "I changed back to my other outfit."
                    
    show lena2 at rig with short
    l "There it is. I'm going, Lola. Don't wait up for me!"
    play sound "sfx/door.mp3"
    scene lenahomenight with long
    show lena2 at rig with short
    l "I'm ready."
    $ louise_look = 2
    show louise2 at lef
    with short
    lo "Me too."
    if v5_lena_sexy:
        $ flouise = "surprise"
        lo "Wow Lena, where did you get that top from?"
        l "Ivy lent it to me. Or gifted it, I'm not sure..."
        $ flouise = "n"
        lo "Of course, it had to be hers."
        l "What?"
        $ flouise = "smile"
        lo "I mean it's so sexy!"
        l "I know! But talk about sexy, you're killing it with that outfit, Louise!"
        $ flouise = "happy"
        lo "You think so? I've been looking for an excuse to wear it. I'm sure Jeremy will like it!" 
    else:
        lo "Oh, I really like your outfit, Lena!"
        l "Thanks! Yours is super striking!"
        lo "I know, right? I've been looking for an excuse to wear it. I'm sure Jeremy will like it!"
    l "Then if we're ready, let's go!"
    stop music fadeout 2.0
    
    scene streetnight with long
    $ flena = "smile"
    $ flouise = "n"
    "We took a cab to get to the club and got in the line."
    show lena2 at rig
    show louise2 at lef
    with short
    lo "It's bursting with people!"
    l "Yeah, it seems this place is pretty popular."
    "We had to wait a bit, but we finally arrived at the end of the queue."
    show lena2 at rig3
    show louise2 at lef3
    with move
    show bouncer with short
    bo "How many?"
    l "Just the two of us. We're friends of Ivy..."
    hide bouncer
    show bouncersmile 
    bo "Oh, sure. She told me you were coming."
    "He let us in for free."
    l "Thanks!"
    if v5_lena_sexy:
        bo "My pleasure, baby. What's your name?"
        $ flena = "shy"
        l "Lena."
        bo "I'm Bob. You know where to find me if you need anything."
        l "Will do! Thanks again!"
    else:
        bo "My pleasure."
    hide bouncersmile with short
    $ flena = "smile"
    lo "Wow, I didn't think a guy like him would be able to crack a smile..."
    if v5_lena_sexy:
        lo "Was he really flirting with you?"
        l "Who knows... I think he was just trying to be nice. Come on, let's go in!"
    else:
        l "That's because we're such nice girls, ha ha! Come on, let's go in!"
    play music "music/dumb.mp3"
    scene blazer with long
    "I could already tell the music was loud from outside. When we stepped inside we were greeted by the flashing lights of the dance floor."
    show lena at rig
    show louise at lef
    with short
    lo "Oh, gosh, I had assumed they would play this kind of music... But this is even harder."
    menu:
        "{image=icon_lust.png}I like it!" if lena_lust > 3 or v5_lena_sexy:
            $ renpy.block_rollback()
            if lena_posh < 5:
                $ lena_posh += 1
            $ v5_lena_music = True
            $ flena = "happy"
            l "Oh, I like it! It's really fun to dance to!"
            lo "With a couple of rounds of drinks already in, preferably."
            l "I mean, it's not something I would listen to while I'm at home... But for a night of partying it's perfect!"
            lo "The lyrics of these songs, though... They're horse shit."
            $ flena = "n"
            l "Well, that's another story..."
            "I could appreciate what Louise was saying. As a songwriter myself I could clearly see how deplorable these lyrics could get..."
            
        "It can be fun to dance to":
            $ renpy.block_rollback()
            l "Well, it's good for what it's supposed to be good, right?"
            l "To dance all night long!"
            lo "I guess so!"
            l "It's not something I would play when I'm at home, but... It will do the trick tonight."
            lo "The lyrics to these songs, though... They're horse shit."
            $ flena = "sad"
            l "Yeah, they're pretty horrible..."
            "As a songwriter I could clearly see the dismal quality and message of the lyrics most of these songs presented."
            
        "It's not my style either":
            $ renpy.block_rollback()
            if lena_posh > 0:
                $ lena_posh -= 1
            $ flena = "sad"
            l "Oh, yeah... That's something we have to put up with no matter how you see it. It's not the kind of music I like, far from it..."
            l "But I guess the rhythm's good for dancing."
            lo "That's the only good thing about it. The lyrics are complete horse shit."
            $ flena = "serious"
            l "Oh, don't get me started with the lyrics... What the hell's on the minds of the men who write them?"
            "As a songwriter I could clearly see the dismal quality and message of the lyrics most of these songs presented."
    
    "The song that was playing right now was as good an example as any other."
    "{image=emoji_music.png} \"{i}Not gonna lie to you baby, anything you want I'll give you{/i}\" {image=emoji_music.png}"
    "{image=emoji_music.png} \"{i}Just get on all fours, that's how I roll{/i}\" {image=emoji_music.png}"
    "{image=emoji_music.png} \"{i}You're gonna be mine tonight, you can bet on it{/i}\" {image=emoji_music.png}"
    "{image=emoji_music.png} \"{i}I'm ice cold and your bum is hot as coal, baby{/i}\" {image=emoji_music.png}"
    if v5_lena_music:
        "But if I just stopped listening to the words and thinking about what they actually meant I could enjoy the music!"
    else:
        "I didn't even want to listen to what they said... Hopefully not all songs were like that, but a worrying majority..."
    $ flouise = "happy"
    lo "Anyways, let's go find Jeremy!"
    $ flena = "smile"
    l "Sure."
    "We crossed the dance floor and got to the bar."
    show lena at rig3
    show louise at lef3
    with move
    $ fjeremy = "smile"
    show jeremy with short
    lo "Baby! It's me!"
    j "Oh, girls, there you are! How do you like my workplace?"
    lo "It looks like it is pretty popular, isn't it?"
    j "Oh yeah, it's the place to be in this city! Even some celebs come by from time to time!"
    $ fjeremy = "flirt"
    "He winked at us."
    j "And you girls have the barman in your pocket! What shall I get you? Free of charge, of course!"
    lo "You're awesome, baby! Vodka for me!"
    j "That's my girl!"
    $ fjeremy = "smile"
    "Jeremy served us our drinks. I really appreciated not having to pay for them, considering the state my economy was in..."
    show louise at left
    show jeremy at centerlef 
    show lena at right
    with move
    $ fivy = "flirt"
    $ ivy_look = "gogo"
    show ivy2 at rig
    with short
    v "There you are, girl!"
    if louise_jeremy:
        $ flouise = "n"
    else:
        $ flouise = "serious"
        $ fjeremy = "n"
    hide louise
    show louise2 at left
    with short
    "Ivy approached me from behind and hugged me."
    "She was already wearing her dancer outfit, and it was certainly revealing!"
    "It looked like a mix between swimsuit and lingerie, with thigh-high socks and black high heels to boot."
    "She looked really striking."
    hide ivy2
    show ivy at rig
    with short
    if v5_lena_sexy:
        v "Damn, you look gorgeous, girl! And I love your makeup, too!"
        l "Thanks! And thanks for the top, I really like it."
        v "It suits you fantastically. You can keep it!"
        if lena_ivy < 10:
            $ lena_ivy += 1
            play sound "sfx/friendup.mp3"
            show friend_up
    else:
        $ fivy = "serious"
        v "Oh, I see you didn't wear the top I gave you..."
        l "It was a bit too revealing for my taste."
        v "Revealing? What are you talking about? It's a perfectly normal top."
        v "Sometimes I really don't get you, Lena."
        if lena_ivy > 2:
            $ lena_ivy -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
        $ fivy = "smile"
    v "Anyways, come with me, I'll let you into the VIP area."
    $ fjeremy = "smile"
    j "See you later, girls! And don't hesitate to come and ask for as many drinks as you want!"
    l "Will do!"
    hide jeremy with short
    show ivy at truecenter
    show lena at rig3
    show louise2 at lef3
    with move
    "Ivy walked us to a raised area to one of the sides of the room and talked to the bouncer controlling the access there, who let us in."
    v "You can go in and out as you please, but if you stay here at some point in the night you'll get free champagne!"
    l "I almost feel bad for all the free stuff we're getting tonight!"
    v "Don't even think about it! Just have fun!"
    v "I'll be back with you in a while. I have to get ready for one of tonight's shows!"
    hide ivy with short
    show louise2 at lef
    show lena at rig
    with move
    lo "Have you noticed? She hasn't said one word to me. She didn't even look at me."
    $ flena = "sad"
    l "Well, she's... She's clueless like that when she's excited."
    "Louise wasn't wrong though. She and Ivy had met a couple times in the past and they never really liked each other for some reason."
    if louise_jeremy == False:
        "And after what I told Louise about her and Jeremy... Seems she disliked her even more."
    $ flouise = "smile"
    hide louise2
    show louise at lef
    with short
    lo "Anyway, let's toast!"
    $ flena = "smile"
    l "Sure!"
    menu:
        "Cheers!":
            $ renpy.block_rollback()
            "We held up our cups and toasted."
            play sound "sfx/toast.mp3"
            l "Cheers!"
            lo "To a night of fun!"
            
        "To our friendship!":
            $ renpy.block_rollback()
            "We held up our cups and toasted."
            play sound "sfx/toast.mp3"
            l "To our friendship! Let's hope we experience a lot more nights like this together!"
            $ flouise = "happy"
            lo "Yes, to our friendship! Four years and counting!"
            play sound "sfx/xp.mp3"
            show charisma_up
            $ lena_charisma_xp += 1
            call screen skillsup
            
        "To your master's degree!":
            $ renpy.block_rollback()
            "We held up our cups and toasted."
            play sound "sfx/toast.mp3"
            l "To your master's degree! You're pretty much done after all your hard work!"
            $ flouise = "happy"
            lo "Yeah! I'm gonna finish a very long and important period in my life! I can't wait!"
            play sound "sfx/xp.mp3"
            show wits_up
            $ lena_wits_xp += 1
            call screen skillsup
            
        "To ourselves!":
            $ renpy.block_rollback()
            "We held up our cups and toasted."
            play sound "sfx/toast.mp3"
            l "To ourselves! To a night of fun and dance and drink!"
            lo "To a night of party!"
            l "Let's burn the night until the sun comes up!"
            if lena_lust < 7:
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
    
    scene v5_lena_dance
    if v5_lena_sexy:
        show v5_lena_dance1
    else:
        show v5_lena_dance2
    if lena_piercing1:
        show v5_lena_dance_p1
    if lena_piercing2:
        show v5_lena_dance_p2
    with long
    if v5_lena_music:
        "The mood was just right and I already felt the music running through my body and moving my limbs."     
    else:
        "The mood was just right. Even if the music wasn't my favorite I could get into the rhythm and enjoy it."       
    "Louise and I began dancing with each other, smiling and letting loose."
    "She moved beautifully, without too much fuss, but with a kind of sober and sensual elegance."
    if v5_lena_sexy:
        "I liked to move around a bit more, putting more pop into my movements, swaying my hips widely and sensually."
    else:
        "I guess we had similar dancing styles. I felt we were doing very well together."
    "Not much else was needed: a nice connection with a good friend, music and flashing lights."
    if v5_lena_sexy:
        "I closed my eyes as I swayed my body, playing with my hair and shaking my ass to the music, being in the moment."
        "It was such a nice and liberating feeling... I had almost forgotten how much I loved partying!"
    else:
        "I closed my eyes as I swayed my body, just being in the moment."
    "Being in the VIP area meant we had all the room we wanted to dance, away from the mass of people that congregated on the dance floor."
    "But since we were on a raised area more than a few people looked at us, some with envy, but most with interest."
    if v5_lena_sexy:
        "I guess we were giving them something of a show... Not that I cared."
        "They could watch all they wanted."
    else:
        "I guess we were giving them something of a show... Was that the reason why they put us in the VIP area?"
    "Just then I noticed something."
    l "Oh, look, Ivy's on the podium...."
    scene v5_ivy2 with long
    "She immediately stole all the eyes that had been looking at Louise and me, and I could understand why."
    "Under the bright and colorful lights she looked completely striking. And her dance moves weren't any less eye-catching."
    "Ivy moved around the pole with very sensual movements, erotic even."
    scene v5_ivy3 with long
    "She mixed in some of the figures I had seen her perform at the studio, and some new."
    "The routine she was performing surely was a thing of beauty... Even if it was a sassy and unabashed kind of beauty."
    $ flouise = "serious"
    $ flena = "n"
    scene blazer
    show louise2 at lef
    show lena at rig
    with long
    lo "How can she dance around in that? She's barely dressed!"
    l "She's wearing what her bosses are telling her to wear."
    lo "Still, I don't see how someone who has a modicum of dignity could feel comfortable prancing around in that..."
    lo "I mean, look at all those guys! They're ogling and drooling over her... Disgusting."
    l "Well, she doesn't seem to mind, that much is clear."
    lo "Must be fun having so little shame."
    show louise2 at lef3
    show lena at rig3
    with move
    hide lena
    show lena2 at rig3
    $ fmike = "smile"
    $ mike_look = 1
    show mike
    with short
    mk "Excuse me, you're Jeremy's girlfriend, right?"
    $ flouise = "n"
    lo "Huh? Yeah, I am... Are you a friend of his?"
    mk "More like an acquaintance. We've met working here at the club."
    mk "I'm Mike."
    $ flouise = "smile"
    hide louise2
    show louise at lef3 
    with short
    lo "I'm Louise, and this is my friend Lena."
    mk "Nice to meet you, girls."
    lo "So you're Jeremy's colleague?"
    mk "Kind of... I'm DJing some nights at the club."
    l "Oh, that's cool. I guess you're not working tonight."
    mk "I am! I'll be at the turntable later. Any beats you girls wanna hear?"
    lo "We could use a break from this kind of music!"
    mk "Don't worry, it's not the stuff I play! More like EDM."
    lo "That sounds like an improvement!"
    lo "I'm out of drink! I'll go ask Jeremy for another round. You want the same, Lena?"
    l "Yeah."
    lo "I'll leave her to your care, Mike. I'll be right back!"
    hide louise with short
    show lena2 at rig
    show mike at lef 
    with move
    hide mike
    show mike2 at lef 
    with short
    "I was left alone with Mike. He had approached us out of the blue..."
    menu:
        "{image=icon_lust.png}He's hot" if lena_lust > 3:
            $ renpy.block_rollback()
            $ v5_mike_flirt += 2
            $ flena = "flirt"
            "I took a good look at Mike. He was pretty hot..."
            "I didn't go out tonight expecting to meet a guy I liked, but... I wasn't closed to the idea."
            "I could poke him a bit, see what kind of vibe he had."
            $ flena = "smile"
            
        "He seems OK":
            $ renpy.block_rollback()
            $ v5_mike_flirt += 1
            "He seemed like an OK guy. He had been quite polite, so I figured I could talk to him a bit."
            
        "I don't want to talk to him":
            $ renpy.block_rollback()
            $ flena = "worried"
            "I wasn't in the mood to make conversation with some random guy, but I didn't want to be rude..."
            "He had been quite polite himself, but he had something about him that put me off."
            "He didn't look like the kind of guy I normally liked, but I forced myself to make some small talk."
            $ flena = "n"
    
    menu v5mikechat:
        "So you're the DJ" if v5_mike_convo1 == False:
            $ renpy.block_rollback()
            $ v5_mike_convo1 = True
            l "So... You're the DJ here, huh?"
            mk "Not every night, and not the whole night. I just go up and do my thing for one or two hours."
            l "Sounds like you're kind of kitchen boy DJ."
            $ fmike = "happy"
            mk "Ha ha ha, yeah, you could say I am! To be honest, I just got the job because my uncle is one of the owners."
            l "Oh, so your family owns this club? You're really a VIP here..."
            mk "A privilege I have not earned but which I'm happy to enjoy, ha ha!"
            l "So what else do you do, other than DJing from time to time?"
            $ fmike = "smile"
            mk "I'm getting started in trading in digital markets, crypto currencies and all that jazz."
            l "Sounds completely alien to me."
            mk "It really is. You'd have to be a nerd to be interested in that subject."
            if v5_mike_flirt > 1:
                l "You don't look like a nerd to me... Quite the opposite."
                $ fmike = "happy"
                mk "Is that a compliment?"
                l "Of course."
                if v5_lena_sexy:
                    mk "I'll take it, then. You don't look half bad, either..."
                else:
                    mk "I'll take it, then. Thanks!"
            else:
                l "I knew there was something fishy about you. So you're a nerd..."
                mk "I failed to hide it, ha ha."
            if v5_mike_convo1 and v5_mike_convo2:
                $ lena_mike += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            $ fmike = "smile"
            jump v5mikechat
            
        "You're friends with Jeremy?" if v5_mike_convo2 == False:
            $ renpy.block_rollback()
            $ v5_mike_convo2 = True
            l "You've known Jeremy for long?"
            mk "About a month, maybe a bit more... He's a really cool guy!"
            l "And he talked to you about Louise?"
            mk "Yeah, he did. He told me he had this really cute goth girlfriend, so when I saw her I imagined it was her."
            l "You must know Ivy too, then."
            mk "Ivy, of course. I doubt there's anyone who doesn't know her at this point. She's become like an icon of Blazer club."
            l "Really? I guess it makes sense... She's the kind of girl who leaves a mark wherever she goes."
            if v5_lena_sexy:
                mk "You look like that kind of girl, too, Lena."
                if v5_mike_flirt > 1:
                    $ flena = "flirt"
                    l "Oh, you think so?"
                    mk "Not a doubt in my mind."
                    l "Hee hee."
                    $ flena = "smile"
                else:
                    l "I don't know about that, but thanks, I guess."
            mk "I assume you and Ivy are friends, too?"
            l "Yeah, since high school." 
            if v5_mike_convo1 and v5_mike_convo2:
                mk "Those are the friendships one must care for, they might last a lifetime!"
                $ lena_mike += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            jump v5mikechat
            
        "{image=icon_lust.png}Is this how you approach girls?" if v5_mike_flirt > 1 and v5_mike_convo1 or v5_mike_flirt > 1 and v5_mike_convo2:
            $ renpy.block_rollback()
            $ v5_mike_convo3 = True
            l "So, is this how you normally approach girls?"
            $ fmike = "n"
            mk "What?"
            l "You really thought Louise could be Jeremy's girlfriend or was it just a lucky shot in the dark? You know, an excuse to approach us."
            $ fmike = "smile"
            mk "Oh, I didn't need an excuse. I never do, believe me. If I want to talk to someone I just do it."
            l "Ohh, I see. I bet this confidence goes a long way when picking up girls."
            mk "Wait, you think I was trying to pick you girls up? I mean, you're real pretty, I'm not blind. But I already have a girlfriend."
            $ flena = "n"
            "Oh, so he was in a relationship... I had the impression he was flirting with me. Had I read him wrong?"
            l "And where's your girl?"
            mk "At home. She's not a big fan of nightclubs. Not enough to be here every night, at least."
            if v5_lena_sexy:
                menu:
                    "Keep flirting with Mike" if v5_lena_sexy:
                        $ renpy.block_rollback()
                        $ v5_mike_dance = True
                        $ flena = "flirt"
                        l "Oh, so you left her home?"
                        mk "She chose to stay, ha ha."
                        l "Isn't she worried some girl tries to steal her man?"
                        $ fmike = "worried"
                        mk "I don't think so. Should she be?"
                        "I touched his biceps. He was strong and ripped..."
                        l "I'm sure many girls want a piece of you."
                        $ fmike = "blush"
                        mk "Well, I have my audience... Ha ha."
                        l "Can you dance? Because girls lose their mind over an athletic, good looking guy who knows how to dance."
                        mk "I guess I'm not half bad at it."
                        scene v5_mike1 
                        if lena_piercing1:
                            show v5_mike1_p1
                        if lena_piercing2:
                            show v5_mike1_p2
                        with long
                        "I leaned on Mike while swaying my hips to the music."
                        l "Show me."
                        if lena_lust < 7:
                            play sound "sfx/xp.mp3"
                            show lust_up
                            $ lena_lust_xp += 1
                            call screen skillsup
                        "I felt a bit of hesitation on Mike's part, but it soon melted away."
                        "He rested his hands on my hips as I slowly began grinding on him."
                        "Him having a girlfriend didn't mean I couldn't play a bit and have some fun. It wasn't like I was doing anything wrong..."
                        "Besides, I had chosen to dress this way tonight for a reason. I enjoyed the attention and the flirting."
                        "As we both began feeling more comfortable with each other our bodies came even closer to each other. He was holding me firmly while I moved my hips sensually."
                        "I could feel his chin on my neck and his hands caressing my thighs as we danced... There was no denying the sexual tension."
                        "I could blame the alcohol, and even though it was true I didn't need much to get tipsy, I hadn't drunk nearly enough to act out of character."
                        "But I guessed I was just in need of feeling sexy and empowered once again..."
                        "I for once was surely enjoying Mike's reaction to me."
                        "It was a fun little game I hadn't played in a long time, and I was glad to see I hadn't gotten rusty at all."
                        "Quite the contrary."
                        "We danced like that for at least ten minutes. Louise was surely taking her time... But she finally came back."  
                        $ flena = "flirt"
                        $ fmike = "flirt"
                        
                    "Wait for Louise to come back":
                        $ renpy.block_rollback()
                        "Him having a girlfriend changed things. Any interest I could've had in him was gone."
                        "He seemed like a cool guy. I didn't mind hanging out around him, but that was it." 
            else:
                "Him having a girlfriend changed things. Any interest I could've had in him was gone."
                "He seemed like a cool guy. I didn't mind hanging out around him, but that was it." 
                        
        "Wait for Louise to come back" if v5_mike_flirt == 0 or v5_mike_convo1 or v5_mike_convo2:
            $ renpy.block_rollback()
            if v5_mike_flirt > 1:
                "Mike had caught my eye, but tonight I was here to have fun with Louise... And I didn't want to get myself tangled with a guy I just met."
                "I kept making some small talk with him until she came back with the drinks."
            elif v5_mike_convo1 or v5_mike_convo2:
                if v5_mike_flirt == 1:
                    "We kept making some small talk until Louise came back with the drinks."
                else:
                    "We kept making some small talk. He wasn't so bad as I had first thought, but I had no further interest in him."
                    "I waited for Louise to come back with the drinks."
            else:
                l "Um, so... What's it you're doing here tonight?"
                mk "I'm DJing, I already told you..."
                "I went through a typical and boring conversation with him, hoping Louise wouldn't take too long to show up."
                "Mike seemed interested in talking to me, but I couldn't really find any enthusiasm in me."
    scene blazer with long
    if v5_mike_dance:
        show lena at rig3
        show mike at truecenter 
        show louise at lef3 
        with short
    else:
        show lena2 at rig3
        show mike2 at truecenter 
        with move
        show louise at lef3 with short
    lo "Second round!"
    "Louise handed me another drink."
    if v5_mike_dance == False:
        hide lena2
        show lena at rig3
        with short
    l "Thanks!"
    $ fmike = "smile"
    mk "It's about time to get to work. I'll leave you girls to it. A pleasure meeting you."
    if v5_mike_dance:
        l "A pleasure indeed."
    else:
        lo "Same!"
    mk "Catch you later."
    hide mike
    hide mike2
    with short
    show lena at rig
    show louise at lef
    with move
    if v5_mike_dance:
        $ flouise = "flirt"
        lo "Well, well, well..."
        lo "I'm gone for ten minutes and look at what I find when I come back."
        l "We were just dancing..."
        lo "Yeah, dancing... Is that how you call it?"
        $ flena = "happy"
        l "I was just having some fun, since you left me alone!"
        lo "It'll try not to! Did you get his number?"
        $ flena = "smile"
        l "No, it didn't come to that... Maybe if I see him later I'll ask him..."
        lo "Oh, I'm sure you'll see him."
    elif v5_mike_flirt == 2:
        $ flouise = "flirt"
        lo "So, what's up with Mike? Your face lit up when you saw him."
        l "Was it that obvious?"
        lo "Why do you think I left you in his hands? Ha ha."
        l "He's handsome and seems like a cool guy. But I'm not interested in him."
        if v5_mike_convo3:
            l "Besides, he has a girlfriend."
            lo "Oh, then forget I said anything."
        else:
            lo "You've discarded him very fast!"
            l "I'm not in the mood tonight! I came to have fun with my friend!"
    elif v5_mike_flirt == 1:
        lo "How was it with Mike?"
        l "Good, he seems like a cool guy. We just talked about some stuff, nothing really important."
        lo "He seemed like he could be interested in you."
        l "Maybe, but he's not my type."
    else:
        lo "How was it with Mike?"
        $ flena = "n"
        l "I entertained him a bit. We just talked about some stuff, nothing really important."
        lo "He seemed like he could be interested in you."
        l "Maybe, but I'm not interested in him one bit."
        lo "You're picky, aren't you?"
        l "He's just not my style."
    stop music fadeout 2.0
    play music "music/edm.mp3"
    "There was a noticeable change of music once Mike took the DJ position."
    lo "Finally... I was needing a rest from that Latin stuff."
    if v5_lena_music:
        "It wasn't bad, but I kinda enjoyed dancing to that other music more..."
    else:
        l "Yeah, me too."
    lo "By the way, you don't mind if I leave with Jeremy at the end of the night, right?"
    $ flouise = "happy"
    lo "We will be going to his place..."
    l "Oh... Of course not."
    if v5_mike_dance:
        "Maybe I could end the night with some company, too..." 
    if v3_spy:
        "I had seen Louise and Jeremy in action... And I could understand why she was so eager to end the night with him."
        if lena_bdick > 1:
            "I hadn't forgotten the size of that cock..."
    lo "What about you? When will you get a new boyfriend?"
    $ flena = "n"
    l "A boyfriend?"
    if ian_lena_sex and lena_robert_sex:
        lo "Yeah! You already slept with Ian, and you have also been seeing Robert..."
        if lena_robert_over:
            l "That thing with Robert is over. And about Ian..."
        else:
            $ flouise = "n"
            lo "Or are you planning on playing both ways? It can be trouble if they find out..."
            l "No, I'm not planning anything... Stuff just happened..."
        l "It's too soon to think about boyfriends!"
        $ flouise = "smile"
    elif ian_lena_sex:
        lo "Yeah! You've been dating Ian and already slept with him!"
        l "I wouldn't say I'm dating him...! But it's true we've started seeing each other..."
        l "But it's too soon to think about boyfriends!"
        $ flouise = "smile"
    elif v4_ian_date and lena_robert_sex:
        lo "Yeah! You've been seeing Ian, right? And you're also hooking up with Robert..."
        if lena_robert_over:
            l "That thing with Robert is over. And about Ian..."
        else:
            $ flouise = "n"
            lo "Or are you planning on playing both ways? It can be trouble if they find out..."
            l "No, I'm not planning anything... Stuff just happened... And Ian..."
        if v4_ian_kiss:
            l "I really like him, but in any case it's too soon to think about boyfriends!"
        else:
            l "I don't know what will happen, but in any case it's too soon to think about boyfriends!"
    elif v4_ian_date:
        lo "Yeah! You've been seeing Ian, right?"
        if v4_ian_kiss:
            lo "You already kissed him, right?"
            l "Yeah, I did... I really like him, but in any case it's too soon to think about boyfriends!"
        else:
            l "I don't know what will happen, but in any case it's too soon to think about boyfriends!"
    elif lena_robert_sex:
        lo "Yeah! You've been seeing Robert for quite a while, right?"
        if lena_robert_over:
            l "That thing with Robert is over."
            lo "Oh, I didn't know... And that other guy, Ian?"
        else:
            l "Yeah, but I'm not interested in a relationship with him!"
            lo "I see... And what about that other guy you told me about, Ian?"
        l "He's nice, but things aren't flowing as I expected. I guess we will just remain friends."
        lo "Seems like you're really picky..."
        l "In any case, it's too soon to think about boyfriends!"        
    else:
        lo "Yeah! You've been alone for a long time now... What about that guy you told me about, Ian?"
        l "He's nice, but things aren't flowing as I expected. I guess we will just remain friends."
        lo "Seems like you're really picky..."
        l "In any case, it's too soon to think about boyfriends!"        
    $ flouise = "happy"
    lo "It's not too soon if it's what your heart desires!"
    l "Well, I'm not sure my heart desires that. Not after Axel..."
    $ flouise = "smile"
    lo "You can't let one bad relationship ruin things for you. You should give love another chance!"
    l "Ivy says quite the opposite. She thinks I shouldn't concern myself with relationships for a long time."
    if louise_jeremy:
        $ flouise = "serious"
        lo "Of course she says that. She prefers to steal boyfriends rather than having one of her own..."
        lo "She doesn't know what love is."
        $ flouise = "n"
    else:
        $ flouise = "n"
        lo "Of course she says that. She doesn't know what love is about..."
    menu:
        "Ivy's not so bad":
            $ renpy.block_rollback()
            $ v5_defend_ivy = True
            l "She's not so bad, you know? I know you two don't see eye to eye in many things, but Ivy's a really nice girl."
            if louise_jeremy == False:
                $ flouise = "serious"
                lo "A really nice girl, flirting with my boyfriend?"
                $ flena = "sad"
                lo "Nice girls don't do that. Sluts do."
                if lena_louise > 3:
                    $ lena_louise -= 1
                    play sound "sfx/frienddown.mp3"
                    show friend_down
                "She was fixated on blaming Ivy for Jeremy's behavior..."
            else:
                lo "I guess it's normal that you think that way, she's your friend, after all..."
                lo "Even if most of the time I don't really understand why."
                l "We've been through quite a lot together."
                
        "It seems to work for her":
            $ renpy.block_rollback()
            l "Well, it seems to be working for her. She looks pretty happy with her life."
            lo "I wonder if that's true or if it's just a facade she's putting up."
            l "She seems to really enjoy herself..."
        
        "She's very different to us":
            $ renpy.block_rollback()
            l "She's very different to us, and so is her outlook on life."
            $ flouise = "smile"
            lo "Yeah, I often wonder how come you two are such good friends..."
            lo "You are way more similar to me than to her. We share more things, wouldn't you say?"
            l "Yeah, probably."
            if lena_louise < 10:
                $ lena_louise += 1
                play sound "sfx/friendup.mp3"
                show friend_up
    
    show lena at rig3
    show louise at lef3
    with move
    $ fjeremy = "happy"
    hide friend_up
    hide friend_down
    show jeremy with short
    j "Hey, ladies! I finally got some time off from the bar."
    $ flena = "n"
    $ flouise = "happy"
    lo "Hi, baby!"
    j "What were you talking about? Anything interesting?"
    $ flouise = "n"
    lo "No. Not really."
    $ fjeremy = "n"
    j "Uh. OK."
    play sound "sfx/sms.mp3"
    $ flouise = "n"
    lo "Oh, I got a message from a friend from college. Wait a minute..."
    $ flouise = "surprise"
    lo "She says the exam results are out!"
    lo "I need to call her! I'll be right back, don't go anywhere!"
    lo "Lena, you take care of my man!"
    $ flena = "worried"
    hide louise with short
    "Louise rushed out of the club so she could make that phone call."
    show lena at rig
    show jeremy at lef
    with move
    $ flena = "n"
    $ fjeremy = "smile"
    j "So... Are you having fun?"
    
##LOUISE GETS WASTED
    
    if louise_jeremy:
        l "Yeah, I am..."
        $ fjeremy = "n"
        j "By the way, I wanted to thank you for not telling Louise about that mishap with Ivy..."
        $ lena_jeremy += 1
        play sound "sfx/friendup.mp3"
        show friend_up
        $ flena = "sad"
        l "I was seriously thinking about doing so, believe me..." 
        l "But I just didn't want to meddle in Louise's relationship and make her suffer. And I wanted to give you the chance to act decently."
        j "And I really appreciate it... I will, of course."
        $ flena = "serious"
        l "I hope you do... Otherwise I will take Louise's side and make her wise to it, don't doubt it." 
        $ fjeremy = "smile"
        j "Message received."
        if v3_breakfast_jeremy:
            j "Though maybe I could bribe you with some more of my famous avocado toasts..."
            $ flena = "smile"
            l "They are not so great that you'd buy me with those."
            j "Oh, so cruel! Attacking my famous and delicious toasts..."
            l "I hope you have some other tricks up your sleeve, because that one's already gotten old!"
            j "Damn, you're ruthless! But I'm sure I can woo you with some other of my many talents..."
        else:
            $ flena = "n"
            l "Just don't be an asshole and hurt my friend."
        $ flouise = "happy"
        show lena at rig3
        show jeremy at lef3 
        with move
        show louise with short
        lo "Guys! I passed!"
        $ fjeremy = "happy"
        $ flena = "happy"
        l "Really? Congratulations!"
        j "Did you get a good grade?"
        lo "Yes, even better than I expected!"
        j "This calls for a celebration!"
        lo "Yes! Let's get another round of drinks! And some shots!"
        $ flena = "smile"
        $ fjeremy = "smile"
        "Jeremy provided what Louise wanted. We toasted, drank and danced."
        "I was taking it kind of easy, but Louise was gulping down glass after glass while dancing with her boyfriend. She was really excited."
        show jeremy at left 
        show louise at centerlef
        show lena at right
        with move
        $ fivy = "flirt"
        show ivy2 at rig with short
        "After a while Ivy came bringing that champagne bottle she had promised before."
        v "I'm back! How's the night going?"
        l "Pretty well! I'm having fun."
        "Ivy looked at Jeremy and Louise. They were having a party of their own, ignoring us."
        $ fivy = "smile"
        hide ivy2
        show ivy at rig
        with short
        v "Really? Don't you feel like a third wheel with those two?"
        l "Let them have their fun. Today's an important day for Louise."
        $ fivy = "flirt"
        v "I saw you've meet Mike, too. He's a pretty cool guy, and hot, too!"
        v "Too bad he has a girlfriend, hee hee."
        if v5_mike_convo3:
            if v5_mike_dance:
                l "I know."
                "But I had the impression that wouldn't be an obstacle for me, if I chose to go for him tonight..."
            else:
                l "I know, he told me about her."
                v "He always does..."
        v "So, how do you like the club? Pretty rad, right?"
        l "I can see it's really popular. Too bad you are working instead of partying with us!"
        v "To be honest working here doesn't feel too different from partying, ha ha!"
        v "Maybe you could work here too, Lena! You just have to polish your dance moves a bit more..."
        if lena_athletics > 3:
            v "You're pretty good already, in fact!"
        l "I never considered it..."
        v "Beats working as a waitress, I'm sure!"
        stop music fadeout 2.0
        play music "music/dumb.mp3" loop
        "I noticed a change in the style of music. It seemed Mike's shift was over."
        "He showed up again a couple of minutes after."
        hide louise
        hide jeremy
        with short
        show lena at rig3
        show ivy at lef3
        with move
        show mike2 with short
        mk "Hey, girls. Did you like the session?"
        hide ivy
        show ivy2 at lef3
        with short
        v "It was great, as always."
        if v5_mike_dance:
            $ flena = "flirt"
            l "Hey, Mike."
            mk "How's it going? Missed me?"
            l "A bit, hee hee."
            $ fivy = "flirt"
            "Ivy read the situation right away, looked at me and winked her eye."
            v "I'll leave you two alone. I have stuff to take care of."
            v "Take good care of her, Mike!"
            mk "Of course."
            hide ivy2 with short
            mk "So... Where did we leave things off?"
            scene v5_mike1 
            if lena_piercing1:
                show v5_mike1_p1
            if lena_piercing2:
                show v5_mike1_p2
            show v5_mike1_smile
            with long
            l "Right here."
            "I leaned against him and began dancing again, grinding close together, just like before."
            "There was no hesitation from his part this time, and he held me tight right away."
            "I was pretty sure that hard thing I was feeling on my ass was his erection..."
            "The way he moved his hips in sync with mine told me he was probably pretty good in bed, and at this point I was certain I wanted to take him there."
            "I was getting so horny..."
            $ fjeremy = "sad"
            $ fmike = "flirt"
            $ flena = "slut"
            scene blazer
            show lena at rig3
            show mike
            show jeremy at lef3
        elif v5_mike_flirt == 2:
            "Mike struck up a conversation with us right away. I didn't mind at all, but I had decided to stop my flirting."
            "We talked and danced for a while. We all were in a good mood and I was having tons of fun."
        elif v5_mike_flirt == 1:
            "Mike struck up a conversation with us right away. He was pretty nice, so I didn't mind at all."
            "We talked and danced for a while. We all were in a good mood and I was having fun."
        else:
            "Mike struck up a conversation with us right away. I guess I would have to indulge him a bit more..."
            "Thankfully this time Ivy was also with me. We talked and danced for a while. We all were in a good mood."
        if v5_mike_dance == False:
            show lena at right
            show ivy2 at centerlef
            show mike2 at rig
            with move
            $ fjeremy = "sad"
            show jeremy at left with short
        
        j "Hey guys, sorry to interrupt... Lena, we have a problem."
        $ flena = "worried"
        $ fmike = "n"
        $ fivy = "n"
        l "A problem?"
        j "It's Louise. She had a bit too much to drink..."
        l "Where's she?"
        j "She puked in the bathroom and is now outside taking a breath of fresh air. But she's in pretty bad shape."
        if v5_mike_dance == False:
            v "Some people can't handle their alcohol..."
        j "She says she wants to go home, but I can't take her. My shift's not over yet."
        j "She was asking for you..."
        $ flena = "sad"
        l "OK... I'm going."
        if v5_mike_dance == False:
            v "What a party pooper, that girl!"
        l "It can happen to anybody... I'll take her home."
        $ flena = "smile"
        l "Thanks for everything, guys. We need to do this again, but next time you can't be working!"
        stop music fadeout 2.0
        if v5_mike_dance:
            mk "I'll help you find your friend."
            l "Cool!"
            "Mike and I left the VIP area and went outside, searching for Louise."
            scene streetnight
            $ flena = "sad"
            show lena at rig
            show mike at lef
            with long
            "She wasn't hard to find. She was sitting on the sidewalk, leaning against a wall."
            show lena at rig3
            show mike at lef3
            with move
            $ flouise = "sad"
            show louise with short
            "Indeed, she wasn't in good shape."
            l "There you are... How are you feeling?"
            lo "Uhhh... I just... wanna get into bed..."
            "She had trouble articulating the words. She was really wasted."
            l "You'll have one hell of a hangover tomorrow..."
            mk "Let me help you."
            "Mike called a taxi and helped me pick Louise up."
            l "Thanks, Mike. Not the way I was expecting the night to end."
            mk "Yeah, me neither... And not just the ending."
            $ fmike = "smile"
            mk "Other unexpected things happened tonight..."
            $ flena = "smile"
            l "Yeah, they did..."
            menu:
                "{image=icon_will.png}Ask Mike to come over" if lena_will > 0:
                    $ renpy.block_rollback()
                    $ lena_mike_sex = True
                    $ flena = "flirt"
                    show will_down
                    play sound "sfx/willdown.mp3"
                    $ lena_will -= 1
                    l "Um... I'm not sure I can take her home on my own..."
                    l "I know I'm being a bother, but would help me carry her to her bed?"
                    $ fmike = "happy"
                    $ lena_mike += 1
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    mk "Oh... Sure, I guess I could do that. It wouldn't feel right to leave you alone with her..."
                    "He knew what he was signing up for as much as I knew what I was offering."
                    "Louise was just serving as the perfect excuse..."
                    jump v5mikehome
                    
                "Say goodbye":
                    $ renpy.block_rollback()
                    "My games with Mike had to come to an end. There were more important things tonight."
                    "Besides, he had a girlfriend. It had been fun flirting with Mike for a bit, that I needed no more from him."
                    $ flena = "n"
                    l "It's been a pleasure meeting you, Mike. And thanks for helping me with Louise."
                    mk "Anytime..."
                    l "Goodnight! Until we meet again."
                    scene streetnight with long
                    "We got into the taxi and it took Louise and me home, where I helped her get into bed."
                    "Her celebration had surely gotten a bit out of hand..."
                    jump v5lenasaturday
            
        else:
            "I left the VIP area and went outside, searching for Louise."
            scene streetnight
            show lena
            with long
            "She wasn't hard to find. She was sitting on the sidewalk, leaning against a wall."
            show lena at rig
            with move
            $ flouise = "sad"
            show louise at lef with short
            "Indeed, she wasn't in good shape."
            l "There you are... How are you feeling?"
            lo "Uhhh... I just... wanna get into bed..."
            "She had trouble articulating the words. She was really wasted."
            l "You'll have one hell of a hangover tomorrow..."
            "I called us a taxi, and I helped her get into bed once we arrived at home."
            "Her celebration had surely gotten a bit out of hand..."
            jump v5lenasaturday
        
##LOUISE BUSTS JEREMY            
            
    else:
        $ flena = "serious"
        l "Let's say I'm trying to take care of my friend. Protect her from lying boyfriends and that sort of thing."
        $ fjeremy = "sad"
        j "Well, yeah, about that... I'm not sure it was necessary you told Louise..."
        l "Oh, you're not sure? I should've saved you the trouble of making up some lies to cover up what you were really doing?"
        l "You're lucky Louise chose to believe all the bullshit you told her."
        if v4_confront_louise:
            l "And believe me, I tried to convince her you were full of shit. But she still chose to believe in you..."
            $ lena_jeremy -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
        j "I know I messed up, OK? I just didn't want to hurt Louise, so I embellished the truth a bit..."
        l "If you didn't want to hurt her you should've acted like a decent boyfriend to begin with... But it's not my place to tell Louise who she should be with."
        l "She chose to stay with you, so I hope you will honor her decision."
        $ fjeremy = "smile"
        j "I will, I will. She's a great gal and she deserves my honesty."
        $ fivy = "flirt"
        show lena at rig3
        show jeremy at lef3
        with move
        $ flena = "n"
        show ivy2 with short
        v "Hey there! I'm back!"
        v "Where's the other one?"
        l "Louise? She went to take a call..."
        v "Well, you don't seem to be missing her, ha ha."
        j "I'm keeping her company."
        v "I saw you've met Mike, too. He's a pretty cool guy, and hot, too!"
        v "Too bad he has a girlfriend, hee hee."
        if v5_mike_convo3:
            if v5_mike_dance:
                l "I know."
                "But I had the impression that wouldn't be an obstacle for me, if I chose to go for him tonight..."
            else:
                l "I know, he told me about her."
                v "He always does..."
        else:
            l "Oh, he does?"
            v "Such a waste, right?"
            "Maybe he wasn't trying to flirt with me, after all..."
        j "Yeah, Mike's a cool dude. Haven't know him for long, but we get along really well!"    
        $ fivy = "smile"
        hide ivy2
        show ivy
        with short
        "As we continued to talk I noticed how Jeremy couldn't avoid staring at Ivy's boobs and ass every five seconds..."
        "But could I really blame him?"
        v "So, how do you like our club? Pretty rad, right?"
        l "I can see it's really popular. Too bad you are working instead of partying with us!"
        v "To be honest working here doesn't feel too different from partying, ha ha!"
        j "As jobs go, ours are pretty cool, huh?"
        v "Maybe you could work here, too, Lena! You just have to polish your dance moves a bit more..."
        if lena_athletics > 3:
            v "You're pretty good already, in fact!"
        l "I never considered it..."
        v "Beats working as a waitress, I'm sure!"
        stop music fadeout 2.0
        play music "music/dumb.mp3" loop
        "I noticed a change in the style of music. It seemed Mike's shift was over."
        "He showed up again a couple of minutes after."
        $ fmike = "smile"
        show lena at right
        show ivy at centerlef
        show jeremy at left
        with move
        show mike2 at rig with short
        mk "What's up?"
        j "Hey bro! Nice session!"
        mk "Thanks. Maybe you can play some music of your own next time."
        j "You'd let me? I'd love that, man!"
        mk "Consider it done, then."
        if v5_mike_flirt == 2:
            if v5_mike_dance:
                $ flena = "flirt"
                l "Hey, Mike."
                mk "How's it going? Missed me?"
                l "A bit, hee hee."
                "We began making conversation, just the two of us."
            else:
                "Mike struck up a conversation with me right away. I didn't mind at all, but I had decided to stop my flirting."
        elif v5_mike_flirt == 1:
            "Mike struck up a conversation with me right away. He was pretty nice, so I didn't mind at all."
        else:
            "Mike struck up a conversation with me right away. I guess I would have to indulge him a bit more..."
        "Jeremy and Ivy were busy with a conversation of their own. The music was loud, so they were talking to each other's ear, very close together."
        "I should've realized letting that happen was a mistake."
        "A big mistake."
        stop music fadeout 2.0
        $ flouise = "serious"
        $ flena = "sad"
        hide mike2 with short
        show louise2 at rig
        with short
        play music "music/danger.mp3" loop
        lo "What are you talking about?"
        $ fjeremy = "n"
        "Louise came back and she was clearly not happy seeing Jeremy and Ivy involved in such private conversation."
        j "Oh, hey babe. Did you pass that exam?"
        lo "I asked what you two were talking about."
        v "We were talking about the worrisome fluctuations of tuna prices, ha ha."
        $ flouise = "mad"
        lo "Don't you dare mock me! Stay away from my boyfriend!"
        $ fjeremy = "sad"
        j "Uh, baby..."
        $ fivy = "flirt"
        hide ivy
        show ivy2 at centerlef
        with short
        v "Why? Do you own him like he was a dog or something?"
        lo "The only bitch here is you!"
        l "Louise...!"
        lo "You know I'm right, Lena! I know you've been hitting on Jeremy, Ivy!"
        v "Oh, so it's me who's been hitting on him? Are you sure about that?"
        j "Girls, please..."
        "The situation was already out of control and neither Jeremy nor I could do anything to reign it in again."
        lo "Of course I'm sure! I only need to take a look at you to know the kind of slut you are."
        $ fivy = "serious"
        hide ivy2
        show ivy at centerlef
        with short
        v "All I'm hearing is jealousy from a frumpy harpy who knows her so called \"boyfriend\" would rather fuck me once than keep fucking you for a lifetime."
        lo "What did you say!?"
        $ fivy = "flirt"
        v "You heard me, minger. Do I really have to spell it out for you?"
        v "I haven't been hitting on your boyfriend. I don't need to. It's him who's been chasing me for quite a while, now."
        j "That's..."
        lo "That's not true! Don't try lying to me! I know Jeremy wants nothing to do with a whore like you!"
        "I didn't know what to do at this point. I wanted to jump between them, but things were too heated up, and I didn't want them to think I was taking sides..."
        v "Oh, you think he doesn't?"
        lo "Keep dreaming!"
        "Ivy picked up her phone, tucked into one of her socks."
        v "So, where did I get this picture from?"
        $ fjeremy = "surprise"
        j "Wait, don't...!"
        show v5_jeremy_selfie with short
        $ flouise = "surprise"
        $ flena = "surprise"
        "Too late."
        "Ivy showed the screen of her phone to Louise."
        "And in it appeared an undeniable telltale image."
        lo "What the...?"
        v "Who do you think sent me this picture? And do you think I asked for it?"
        v "I can read to you the conversation, too, if you want..."
        $ flouise = "mad"
        hide louise2
        show louise at rig
        hide v5_jeremy_selfie
        with short
        lo "You slut...!"
        "Louise raised her hand and jumped towards Ivy, trying to slap her."
        show ivy at left
        show jeremy at centerlef
        with move
        $ fivy = "mad"
        play sound "sfx/punchgym.mp3"
        with vpunch
        $ fjeremy = "sad"
        "Thankfully, Jeremy stepped in between them, restraining Louise."
        j "Stop it, baby! Don't do this!"
        "Louise shoved him away."
        play sound "sfx/punchgym.mp3"
        show jeremy at lef with vpunch
        lo "Don't touch me!"
        lo "You lying piece of shit! Don't you... Don't you..."
        $ flouise = "cry"
        $ flena = "sad"
        "Tears started running down Louise's face."
        lo "I hate you!"
        stop music fadeout 2.0
        hide louise with short
        "She turned around and ran, disappearing into the crowd."
        show lena at rig with move
        j "Fuck..."
        "Jeremy tuned to Ivy."
        $ fjeremy = "serious"
        j "Did you really have to show her that?"
        v "Don't you blame me. She started it, and it's you two who brought me into your fucking drama."
        l "You went too far..."
        v "Oh, not you, too! What was I supposed to do? Shut up and let her slander me?"
        $ fjeremy = "sad"
        j "I guess I should go talk to her..."
        $ flena = "serious"
        l "I doubt she'd want to talk to you. It's better if you stay away."
        $ flena = "sad"
        l "I'll go find her..."
        if v5_mike_dance:
            $ fmike = "sad"
            show mike at right with short
            mk "Do you want me to come with you and help you find her?"
            l "OK..."
        stop music fadeout 2.0
        scene blazer with long
        if v5_mike_dance:
            "Mike and I left the VIP area and searched for Louise around the club."
            scene streetnight
            show lena at rig
            show mike at lef
            with long
            l "She's not outside, either..."
            l "And she's not picking up my calls, nor answering my texts..."
            mk "She must've gone back home..."
            l "The only way to make sure is to go and check..."
            "I sighed."
            l "Not the way I was expecting the night to end."
            mk "Yeah, me neither... And not just the ending."
            $ fmike = "smile"
            mk "Other unexpected things happened tonight..."
            $ flena = "smile"
            l "Yeah, they did..."
            menu:
                "{image=icon_will.png}Ask Mike to come over" if lena_will > 0:
                    $ renpy.block_rollback()
                    $ lena_mike_sex = True
                    $ flena = "flirt"
                    show will_down
                    play sound "sfx/willdown.mp3"
                    $ lena_will -= 1
                    l "Um... To be honest, I'd prefer not going back home all alone. It's pretty late and I lost my friend..."
                    l "I know I'm being a bother, but would you keep me company until I get there? It's not super far..."
                    $ fmike = "happy"
                    $ lena_mike += 1
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    mk "Oh... Sure, I guess I could do that. If it's really not far..."
                    "He knew what he was signing up for as much as I knew what I was offering."
                    "I just hoped to find Louise at home so I could have my mind at ease..."
                    jump v5mikehome
                    
                "Say goodbye":
                    $ renpy.block_rollback()
                    "Well, my games needed to come to an end. There were more important things tonight."
                    "Besides, he had a girlfriend. It had been fun flirting with Mike for a bit, but I needed no more from him."
                    $ flena = "n"
                    l "It's been a pleasure meeting you, Mike. And thanks for helping me look for my friend."
                    mk "Anytime..."
                    l "Goodnight! Until we meet again!"
                    jump v5louisedrama
            
        else:
            "I left the VIP area and searched around the club."
            scene streetnight
            show lena
            with long
            l "She's not outside, either..."
            l "And she's not picking up my calls, nor answering my texts..."
            l "I guess she must've gone straight back home, but I won't feel easy until I'm sure."
            "I texted Ivy telling her that I was leaving to see if Louise had made it home."
            "Not the way I was expecting tonight to end..."
            jump v5louisedrama
        
##LOUISE SEX ################################################################################################################################################################################################################
        
label v5louisedrama:
    
    play music "music/lenas_theme.mp3" loop
    scene lenahomenight_dark with long
    "I took a taxi back home. Louise was still unavailable on the phone..."
    $ flena = "worried"
    play sound "sfx/door_home.mp3"
    show lena with short
    "Once I got home I went straight to Louise's room. But the light creeping through the bathroom door gave her away."
    "I knocked softly on the door."
    l "Louise? Can I come in?"
    "I heard her sobbing. I took that as a yes."
    $ flouise = "cry"
    show lena at rig with move
    show louise at lef with short
    "She was sitting on the floor, curled up next to the toilet, crying. I knelt at her side and tried to comfort her."
    l "Oh, Louise... What are you doing here?"
    lo "I'm such a fool... How could he? With her..."
    lo "How could he do such a thing to me?"
    l "He's an asshole... He doesn't deserve your tears."
    "It took me a couple of minutes to make Louise stop sobbing. When she did I wiped her tears, that had smeared her makeup."
    $ flouise = "sad"
    l "There you go."    
    "I helped her get up."
    l "Come on, let's take you to your room."
    lo "Can we go to yours? I don't want to be in mine... It's where Jeremy and I..."
    l "Sure... Come."
    play sound "sfx/door.mp3"
    scene lenaroomnight
    show lena at rig
    show louise at lef
    with long
    l "I'm glad to see you're in one piece... I was worried when you ran off like that!"
    lo "I just couldn't stand it, being there, looking him in the face..."
    l "I know you must be feeling really shaken up now. And the alcohol doesn't help."
    l "The best you can do right now is sleep it off. Tomorrow you'll see it with different eyes."
    lo "I hope so..."
    hide louise 
    hide lena
    with short
    $ louise_look = 1
    $ lena_look = "sexy"
    "We undressed and sat on the bed. Louise kept circling around what had happened, and I couldn't blame her..."
    show lenabra at rig 
    show louisebra at lef
    with short
    lo "I don't know how I will manage to go on from now on. I thought this time I had found someone for real..."
    lo "But he betrayed me, lied to me..."
    l "I know how that feels, believe me."
    lo "I'm so stupid! I should've listened to you!"
    if v4_confront_louise:
        lo "You told me the truth over and over and I didn't want to believe you!"
        lo "I didn't trust you... I'm so sorry, Lena... I chose to believe that lying, back-stabbing snake in the grass..."
        if lena_louise > 8:
            $ lena_louise = 10
        else:
            $ lena_louise += 2
        play sound "sfx/friendup.mp3"
        show friend_up
    l "Love is blind... These things happen. I don't blame you."
    lo "Oh Lena, you're so good to me... You could be mad at me, but you're still taking care of me..."
    lo "Thanks, Lena... You're someone I can count on when I really need it..."
    $ flena = "smile"
    l "That's what friends are for, right?"
    lo "I... I don't know what I would do if I lost you..."
    stop music fadeout 2.0
    scene v5_louise1 
    if v5_lena_sexy:
        show v5_louise1_choker
    if lena_piercing1:
        show v5_louise1_p1
    if lena_piercing2:
        show v5_louise1_p2
    show v5_louise1_eyes1
    with long   
    "Suddenly, Louise leaned forward and kissed me."
    "And it was not a small, friendly kiss. She meant it."
    "My surprised reaction was to pull back."
    $ flena = "blush"
    $ flouise = "blush"
    scene lenaroomnight
    show lenabra2 at rig
    show louisebra at lef
    with long
    l "Louise..."
    lo "Lena, I... You're my closest friend, the only person who has been helping me..."
    lo "You're so important to me, you..."    
    scene v5_louise1 
    if v5_lena_sexy:
        show v5_louise1_choker
    if lena_piercing1:
        show v5_louise1_p1
    if lena_piercing2:
        show v5_louise1_p2
    show v5_louise1_eyes1
    with long   
    "Louise kissed me yet again."
    menu:
        "{image=icon_friend.png}Kiss her back" if lena_louise > 6 or v2_sleep_louise and lena_louise > 4:
            $ renpy.block_rollback()
            $ v5_louise_sex = True
            $ lena_louise_sex = True
            play music "music/sensual.mp3" loop
            hide v5_louise1_eyes1
            show v5_louise1_eyes2
            with long
            "Without knowing the exact reason why, I closed my eyes and kissed her back."
            "There was something inside of me that was pushing me to surrender to this moment. To let it flow and not stop it."
            "Maybe it was because I felt for Louise, or because I myself was in need of some comfort these days."
            if lena_lust > 3:
                "Or maybe I was just horny and lusting after my friend..."
            "Whichever the reason, I just decided to go with it and get lost in the feeling of Louise's soft lips on mine."
            "She was hesitant at first, we both were. But bit by bit our kisses found courage."
            "And not only our kisses, but our hands, too."
            scene v5_louise2 
            if v5_lena_sexy:
                show v5_louise2_choker
            with long
            "And thus our kisses became more passionate, in turn fanning our lustful desires."
            "We both yearned to feel the other's body, so our chests came together."
            "I could feel the tenderness of Louise's breasts pressing against mine over the hard surface of my bra."
            "Our arms wrapped around each other's backs and our hips, necks and hair were held and caressed by the other's hand." 
            "Our tongues, not wanting to be left behind, searched for each other outside our mouths, meeting in a wet and slippery grind."
            "Deep and passionate kisses tried to fuse us, penetrating one another with our tongues, as our hands explored every inch of soft skin."
            if lena_lust < 7:
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
            "I was really kissing Louise... Feeling her taste, her naked skin..."
            "I felt Louise pull back a bit, interrupting our french kisses."
            $ flouise = "sad"
            $ flena = "blush"
            scene lenaroomnight 
            show louisebra at lef
            show lenabra2 at rig
            with long
            lo "I... This is the first time I've been with a girl."
            lo "I don't know exactly what to do..."
            "She looked a bit insecure. Seems she was asking for some guidance."
            menu:
                "{image=icon_charisma.png}+{image=icon_lust.png}I'll teach you" if lena_lust > 3 and lena_charisma > 3:
                    $ renpy.block_rollback()
                    $ v5_teach_louise = True
                    l "Don't worry... I'll teach you."
                    lo "You've been with a girl before?"
                    l "A couple of times..."
                    l "Now, think about what you would like me to do to you. And just do that to me."
                    lo "OK...."
                    
                "Just relax":
                    $ renpy.block_rollback()
                    l "Just... Just relax. Let it flow, just like you always do with a guy..."
                    lo "It feels kinda different, though..."
                    lo "But I'll try."
                    
                "Do what you'd like being done to you" :
                    $ renpy.block_rollback()
                    l "Um... Just do whatever you'd like someone to do to you."
                    lo "Oh... I see..."
                
            hide lenabra
            show lenatopless at rig
            with long
            "She kissed me again and removed my bra. But it felt more awkward than passionate."
            scene v5_louise3 
            if v5_lena_sexy:
                show v5_louise3_choker
            with long
            "This time her lips deviated from my mouth in favor of my neck, my collarbone, my chest..."
            "As Louise's kisses reached down to their objective, so did her hands. I felt her fingers grasping my breasts, holding them up..."
            "And finally her mouth reached my nipples. A pleasurable shiver ran across my back and a moan escaped me."
            play sound "sfx/mh1.mp3"
            l "Mhh..."
            "I put my hands to work and caressed Louise's hair, arms and shoulders as she continued to kiss my nipples."
            "I could tell Louise hadn't touched boobs other than her own by how clumsily she moved her fingers... Her mouth was another story, though."
            "She slid her moist and hot tongue over my nipples without rushing, slowly, carefully... I could feel them become hard and sensitive after each stroke."
            if v5_teach_louise:
                lo "Am I doing it right?"
                l "Yes... You're doing it great..."
                l "I love how you're running your tongue over my nips... Do it a bit harder..."
                l "Mnnh..."
            else:
                lo "Do you like it?"
                l "Yeah..."
            "She kept at it, encouraged by my words."
            "Her initial awkwardness was giving way to passion once again, and that was fanning my fire too..."
            "The moisture of my pussy was beginning to spill into my panties..."        
            "I found myself wanting Louise to divert her attentions to my pussy... Her caresses were starting to become torture."
            scene v5_louise4
            if v5_lena_sexy:
                show v5_louise4_choker
            if lena_piercing1:
                show v5_louise4_p1
            if lena_piercing2:
                show v5_louise4_p2
            with long
            if v5_teach_louise:
                "I sat back and looked Louise in the eyes. I was almost ashamed of asking this of her... Almost."
                l "I want you to eat me..."
                "I wanted it more than I was ashamed of it. And Louise was so willing to give it to me."
                lo "Yes, of course... I want to do it too."
            else:
                "But just when I thought she would continue like that the whole night, she slid her hands down to my hips and pulled my panties down."
                "I sat back, helping her with the task of removing them."
            "She looked at my legs as she pulled my panties off."
            lo "You have such beautiful legs, Lena... I wish I had legs like yours."
            l "You're really beautiful, too, Louise... You know that."
            "She looked at me and let out a sigh."
            lo "Oh, Lena..."
            scene v5_louise5
            if v5_lena_sexy:
                show v5_louise5_choker
            with long
            play sound "sfx/ah1.mp3"
            "Louise bent over between my legs. I shivered and moaned when I felt her lips on my sex."
            "It was really happening. My friend and flatmate was eating my pussy..."
            l "Nhhh..."
            "She dived right in, kissing it, trapping my clit between her lips, brushing my lower lips with them."
            "I felt Louise's piercing rubbing against my slit. It was hard in comparison to her lips."
            lo "You're really wet, Lena..."
            lo "That must mean you like me."
            l "I do... I like what you're doing to me..."
            if v5_teach_louise:
                l "Use your tongue, too..."
                "She obeyed, pressing down with it, tasting me from bottom to top. She was not shy about using her tongue..."
                l "Lick my clit... Oh, yes, Louise..."
                l "Up and down... Yeah, just like that..."
                "I began moaning. I was feeling really good... But I wanted even more."
                l "Use your fingers, too... Put them inside me..."
            else:
                "She got back to work, adding her tongue to the mix."
                "She pressed down with it, tasting me from bottom to top. She was not shy about using it..."
                "Her tongue stumbled across my slit, finally finding my clit, licking it in circles."
                "I began moaning. Louise felt my pleasure increasing and decided to double her efforts."
            scene v5_louise6_animation
            if lena_piercing1:
                show v5_louise6_p1
            if lena_piercing2:
                show v5_louise6_p2
            with long
            play sound "sfx/oh1.mp3"
            l "Ohhh, Louise...!"
            if v5_teach_louise:
                "She slid two fingers inside my pussy, just like I had told her. I was so wet they slid in like a knife into butter."
                "As she moved her fingers her tongue kept working on my clit with the exact motion I liked, sending shivers up my spine."
                l "Ohhh... Push upwards with your fingers... Rub them harder..."
                "She obeyed, and a sharp stream of pleasure ran through my belly and up my spine."
                "I would cum!"
            else:
                "She slid one finger into my pussy and then, finding it welcoming, a second one."
                "As she moved her fingers her tongue kept circling around my clit, sending shivers up my spine."
                "I felt Louise's lack of skill in how she was using her fingers, but that and her treatment of my clit would be enough to make me cum."
            l "Oh, yes, Louise...! Mhhh...!"
            "My moans signaled my proximity to the breaking point. And Louise didn't let up."
            l "I'm coming... I'm coming...!"
            play sound "sfx/ah4.mp3"
            scene v5_louise6
            if lena_piercing1:
                show v5_louise6_p1
            if lena_piercing2:
                show v5_louise6_p2
            with vpunch
            l "Ahhhh!!"
            "My hips twitched and trembled and my thighs trapped Louise's head as I orgasmed."
            if v5_teach_louise:
                l "Oh, God!"
                "That had been such a wonderful orgasm!"
            else:
                l "Mhhh..."
                "Such a nice orgasm..."
            $ flena = "flirt"
            $ flouise = "happy"
            $ louise_look = 3
            scene lenaroomnight
            show louisebra at lef
            show lenanude at rig
            with long
            lo "Did I really make you cum?"
            l "Yeah, you did..."
            lo "Oh..."            
            menu:
                "Return the favor":
                    $ renpy.block_rollback()
                    $ v5_louise_orgasm = True
                    l "I should return the favor, don't you think?"
                    scene v5_louise7
                    if v5_lena_sexy:
                        show v5_louise7_choker
                    with long
                    "I didn't give her a chance to reply. My lips found hers and our mouths fused in another deep kiss."
                    "I leaned on top of Louise, skin against skin, devouring her with slow and sensual kisses."
                    "The way she moaned was hot and cute at the same time. Her lips were still moist with my juices."
                    l "You taste like me..."
                    "As we made out I snuck my hand between Louise's thighs and found her sex. It was really wet..."
                    play sound "sfx/ah1.mp3"
                    lo "Nhhhah, Lena... Mhhh..."
                    "My mouth suffocated her moans when I kissed her again. My fingers began exploring Louise's pussy, caressing it with slow and deliberate intent."
                    "It wasn't hard for me to find her clit. It was hard and eager for attention. And I was going to give it what was due."
                    "Louise reacted sharply to my touch. Seems like she was really feeling it."
                    l "You're so sensitive..."
                    lo "It's the way you're touching me... I've never felt someone touch me like this..."
                    lo "Mhhh!"
                    "Louise began trembling. She was so close."
                    if lena_lust < 7:
                        play sound "sfx/xp.mp3"
                        show lust_up
                        $ lena_lust_xp += 1
                        call screen skillsup
                    "I glued my mouth to hers as I rubbed her button faster. Louise's pleasure and passion were about to burst, I could feel it in her kisses."
                    play sound "sfx/orgasm1.mp3"
                    lo "Mhhhh!!! Ohh, Lena...!!"
                    with vpunch
                    "She hugged me while the climax cleansed her body, wanting to be embraced by me."
                    stop music fadeout 2.0
                    scene lenaroomnight with long
                    "And just like that we fell asleep, softly panting next to each other after a night high with drama and emotions."
                    "Just what a night out should be... right?"
                    jump v5lenasaturday
                    
                "Go to sleep":
                    $ renpy.block_rollback()
                    stop music fadeout 2.0
                    "I stretched while lying on the bed. I felt so relaxed..."
                    l "Mhh..."
                    scene lenaroomnight with long
                    "Louise laid next to me and hugged me. We were both tired and had no desire to speak unnecessary words."
                    "It had been a night filled with drama and emotions... Just what a night out should be, right?"
                    jump v5lenasaturday
        
        "Reject Louise's advances":
            $ renpy.block_rollback()
            $ lena_reject_louise = True
            $ flena = "sad"
            $ flouise = "blush"
            scene lenaroomnight
            show lenabra2 at rig
            show louisebra at lef
            with long
            "And I pulled back yet again, avoiding her kisses."
            l "I'm sorry, Louise, but... I don't feel this way about you..."
            lo "I'm... I'm sorry, I shouldn't have..."
            lo "Oh, I'm so embarrassed...!"
            l "It's OK, Louise, I understand how you're feeling... But this isn't what you need..."
            lo "I'm so stupid... I'm sorry...!"
            $ flouise = "cry"
            "She began crying again."
            l "No, don't cry...!"
            "My words were not gonna stop her tears. And if she felt like crying, better let her do it."
            scene lenaroomnight with long
            "I let her stay with me on my bed, where she cried herself to sleep."
            "What an end to a night that was supposed to be lighthearted and fun..."
            jump v5lenasaturday
        
##MIKE SEX ################################################################################################################################################################################################################
        
label v5mikehome:   
    
    if louise_jeremy:
        scene lenahomenight_dark with long
        play sound "sfx/door_home.mp3"
        $ flena = "n"
        $ fmike = "smile"
        $ flouise = "sad"
        show lena at rig3
        show louise
        show mike at lef3
        with short
        "We finally arrived at my place. Mike helped me carry Louise to her room."
        l "Thanks. I can take it from here..."
        lo "I need water..."
        mk "I'll get her a glass. Where do you store them?"
        l "Don't worry, I'll take care of that. You can wait in my room, it's that door over there."
        mk "Oh, OK."
        hide mike with short
        "I helped Louise undress and get into bed, and gave her the water she so desperately needed."
        "She would have a big hangover tomorrow..."
        play sound "sfx/door_home.mp3"
        scene lenaroomnight
        show lena2 at rig
        show mike at lef
        with long
        mk "So, will your friend be OK?"
        l "She will... And us? Are we gonna be OK?"
    else:
        scene lenahomenight_dark with long
        play sound "sfx/door_home.mp3"
        $ flena = "sad"
        $ fmike = "n"
        show lena at rig
        show mike at lef
        with short
        "As soon as we got home I went to check Louise's room. The door was closed, so I knocked softly."
        l "Louise?"
        "I heard faint sobbing at the other side."
        $ flena = "n"
        l "Thank God, she's here..."
        mk "She must be in pain, though. Do you want me to go so you can talk to her or something?"
        l "No, no... I'll talk to her tomorrow. And what would be the point of you coming all the way here?"
        $ fmike = "flirt"
        mk "That's what I'm wondering... What's the point of it?"
        $ flena = "flirt"
        l "Oh, do I really have to tell you?"
        mk "I could use some indications, just so we're clear..."
        l "Let's go to my room and I'll give them to you."
        
    scene v5_mike1b
    if lena_piercing1:
        show v5_mike1_p1
    if lena_piercing2:
        show v5_mike1_p2
    with long
    if louise_jeremy:
        "I leaned back against him once more, and he embraced me without hesitation."
        "We both were there for a reason. We wanted the same thing."
        mk "We will, baby... Oh yes, we will."
    else:
        "Once in my room there was no point in keeping up appearances. We both were there for a reason."
        "We wanted the same thing."
        l "How's this for directions?"
        mk "It's pretty clear..."
    play music "music/sex.mp3" loop
    scene v5_mike2
    if lena_piercing1:
        show v5_mike2_p1
    if lena_piercing2:
        show v5_mike2_p2
    with long   
    "This time our canoodling could go as far as we wanted. We weren't at the club anymore."
    "In the intimacy of my room our lips finally found each other's and I tasted Mike."
    "And he didn't need to hide his excitement anymore. His hands caressed my body with an urgency and desire he hadn't shown before."
    "He wasted no time in removing my clothes, feeling my skin, touching my body..."
    "And I enjoyed every second of it. I pressed my ass against his crotch, feeling the bulge under his pants, rubbing it with my butt."
    l "Seems you're pretty excited to be here..."
    mk "You've been teasing me all night long... What did you expect?"
    "He reached down with his hand, rubbing my pussy over my panties."
    play sound "sfx/mh1.mp3"
    l "Nhhh... I had the feeling you were a bad boy. I'm glad I wasn't mistaken..."
    mk "Look who's talking... You've been trying to seduce me all night long, and now you're this wet..."
    l "I was wet from the moment I saw you..."
    menu:
        "Let Mike lead":
            $ renpy.block_rollback()
            mk "Let's see how wet you really are..."
            
        "Take the lead and suck Mike's dick":
            $ renpy.block_rollback()
            $ lena_bj += 1
            $ v5_mike_bj = True
            l "And there's also something I've been wanting to do since I saw you..."
            scene v5_mike3
            if lena_piercing1:
                show v5_mike3_p1
            if lena_piercing2:
                show v5_mike3_p2
            with long   
            "I knelt down and unbuttoned his pants. I had been feeling his junk on my ass all night, but I wanted to taste it..."
            if lena_robert_sex:
                "And I wasn't disappointed with what I found. He was bigger than Robert, and had more girth."
            else:
                "And I wasn't disappointed with what I found. Not one bit."
            if lena_lust < 8:
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
            mk "Oh, baby..."
            "He let out a sigh when I began running my wet tongue across the shaft, using my lips around the glans, kissing, sucking..."
            play sound "sfx/bj1.mp3"
            "Having a hard cock in my mouth was such a turn on."
            mk "So, you were dreaming about sucking my cock while we were dancing at the club?"
            l "Mhh... Yeah..."
            mk "Just sucking it? Don't you want to do anything else with it?"
            l "Oh, yeah... I want you to fuck me... To pound my pussy..."
            l "But first I wanted to taste you. I needed to... Mhhh..."
            "Mike groaned with pleasure."
            mk "You're such a naughty girl, Lena."
            l "You're one to talk. You have a girlfriend, yet you're letting me suck your cock..."
            mk "Well, that's... I find it hard to say no to you."
            "I giggled."
            l "Don't worry, I'm not judging you. If anything, I'm glad you're a naughty boy..."
            "I swallowed his dick and sucked it eagerly, making him moan again."
            "I kept savoring his cock during a few more minutes, until Mike decided it was time for him to take the lead."
            mk "You're driving me crazy, baby. Come here."
    
    scene v5_mike4 with long
    "Mike pushed me to the bed, making me stand on all fours."
    "He grabbed my hips and positioned me to his liking with ease, then knelt down and slid his tongue across my pussy."
    play sound "sfx/ah1.mp3"
    l "Oh, Mike... Mhhh..."
    "He began eating me out pretty intensely from the get go. He wasn't afraid to shove his head between my legs and slurp me up."
    "His tongue didn't discriminate between my clit, my slit and even my asshole. He licked and pleasured all of them..."
    "It was so hot!"
    "He should be doing this to his girlfriend, yet he was doing it to me..."
    "He was going all out, eating me out ferociously. Feeling his passion was making things even more erotic and pleasurable..."
    l "Oh, Mike...! So good! If you keep this up..."
    "He had no intention of stopping. In fact, he increased the intensity."
    "His tongue began pressing down and flicking my clit savagely. Just what I needed."
    "I had been horny for hours now, and the situation had me so excited... I was sensitive and eager to release all my pent up sexual energy."
    "And Mike granted me that."
    l "Fuck, I'm cumming, Mike...!"
    play sound "sfx/ah4.mp3"
    l "I'm cumming!!! Ahhh!!"
    with vpunch
    "I collapsed on the bed, eyes closed, with my legs still slightly trembling."
    scene v5_mike5a with long
    "He got up and leaned forward. I felt his hot, hard cock resting between my butt cheeks."
    mk "That was quick... And so hot."
    mk "See how hard you made me?"
    "He began rocking his hips, sliding his manhood up and down and rubbing it against my butt."
    mk "You're so fucking sexy, Lena... You're driving me insane."
    l "You too... That orgasm was so nice... You--"
    play sound "sfx/oh1.mp3"
    scene v5_mike5b with vpunch
    "Suddenly, I felt his cock entering me."
    "It slid right in with a single, sudden thrust."
    "The unexpected sensation of him filling my pussy brought back shards of intense pleasure from the orgasm I just had."
    "He was inside me, hard, warm, fitting me so perfectly..."
    "But he wasn't wearing a condom...!"
    l "Ahh.. Wait...!"
    menu:
        "Ask Mike to wear protection!":
            $ renpy.block_rollback()
            l "Stop, stop!"
            l "Please, put on a condom..."
            mk "Oh, yeah... Sorry, babe, you turned me on so much I got carried away..."
            scene lenaroomnight with long
            if lena_robert_sex:
                "He pulled out and I handed him one of the condoms I had bought recently to use with Robert."
            else:
                "He pulled out and I handed him one of the condoms I had bought recently, just in case."
            scene v5_mike6
            show v5_mike6_condom
            if lena_piercing1:
                show v5_mike6_p1
            if lena_piercing2:
                show v5_mike6_p2
            with long   
            "He slid his member into me again, this time with proper protection."
            mk "I'm sorry, babe. I didn't mean to cum inside or anything, I promise."
            l "I know... Just fuck me..."
            "This little hiccup had threatened to kill the mood, but I was too excited for that to happen."
            "We both were."
            "In less than a minute the energy was at the same level as before: lust and desire taking over."
            "Mike's hips moved back and forth with fluid rhythm. His thrusts were making my body shake and the bed creak."
            "He was good... Very good..."
            
        "{image=icon_lust.png}Let him continue" if lena_lust > 4:
            $ renpy.block_rollback()
            $ v5_mike_bareback = True
            "He began thrusting his hips, penetrating me slowly."
            scene v5_mike5c
            with long
            "I felt the full length of his cock retracting and then entering me again, grinding so delightfully against the inner walls of my pussy."
            "Skin on skin."
            play sound "sfx/ah3.mp3"
            l "Ahhh...."
            "I couldn't find it in me to tell him to stop. And the desire to do so was being whipped away with each one of Mike's repeated thrusts."
            "It felt so good... His bare, naked cock fucking my pussy..."
            "I hadn't tasted one bare since my time with Axel... And it was a feeling I relished."
            l "Oh, Mike, yes...!"
            mk "You're so tight and hot, Lena!"
            "I could only moan as he fucked me from behind, keeping an energetic and steady rhythm."        
        
    if ian_lena_sex:
        "For some reason Ian slipped into my thoughts. I had been in this same situation with him not long ago..."
        "But if felt different. Both him and Mike felt so good inside me. Both of them turned me on so much."
        if lena_robert_sex:
            "But with Ian I also felt fuzzy and warm inside while having sex. With Mike that sensation was missing, much like with Robert..."
        else:
            "But with Ian I also felt fuzzy and warm inside while having sex. With Mike that sensation was missing..."
        "But that void was filled by a powerful and narcotic excitement. Something akin to what Axel made me feel sometimes... But it had a different quality to it."
    elif lena_robert_sex:
        "It was much better than with Robert. Having Mike fucking me felt more exciting for some reason..."
        "There was this powerful and narcotic sensation. Something akin to what Axel made me feel sometimes... But it had a different quality to it."
    else:
        "Having Mike fuck me was so exciting... There was this powerful and narcotic sensation."
        "Something akin to what Axel made me feel sometimes... But it had a different quality to it."
    "In any case, right now Mike was fucking me like I was his good little slut."    
    if v5_mike_bareback:
        l "Oh, fuck, Mike! Oh fuck, oh fuck...!"
        "That was it. I was about to cum."
        "I had been a very naughty girl. I had picked some very sexy clothes to go out and I had been flirting with a hot guy I had just met."
        "A guy who made me horny, whom I wanted to fuck... even if he had a girlfriend."
        "I had taken him. Seduced him by being slutty."
        "And now he was fucking me like the slut I was."
        play sound "sfx/orgasm1.mp3"
        with vpunch
        l "Cummiiiinggg!!! Ahhheh...!!"
        "My whole body trembled, shaken by an orgasm so intense that it made my mind go blank for a couple of seconds."
        "My body became lax, like warm butter over the bed."
        l "Oh, God... That was... Mhhh..."
        mk "I can see you liked it... You're even naughtier than I thought."
        "His cock was still hard as a rock inside me, twitching"
        l "You can keep going... As long as you cum outside..."
        mk "OK baby... Let's change position..."
        menu:
            "Missionary":
                $ renpy.block_rollback()
                scene v5_mike6
                if lena_piercing1:
                    show v5_mike6_p1
                if lena_piercing2:
                    show v5_mike6_p2
                with long   
                "I rolled on my back and spread my legs apart, welcoming him in."
                "Lust and desire continued to take over our minds and bodies."
                "Mike's hips flowed back and forth with fluid rhythm. His thrusts were making my body shake and the bed creak."
                "He was good... Very good..."
                "I felt so naughty... Making this hot guy I had just met cheat on his girlfriend with me..."
                "I knew what I was doing was wrong, but I felt empowered and so turned on. Mike's desire for me was too overwhelming for him to control..."
                "And I enjoyed getting what I wanted. Especially knowing I shouldn't have it. But he wasn't able to deny it to me."
                "It felt great... for all the wrong reasons."
                mk "Fuck, I'm almost there! I'm gonna cum...!"
                scene v5_mike6b
                if lena_piercing1:
                    show v5_mike6_p1
                if lena_piercing2:
                    show v5_mike6_p2
                with long  
                "He quickly pulled out, grabbed his cock and jerked himself off to orgasm." 
                mk "Here it comes, baby! All for you!"
                show v5_mike6_cum1 with flash
                mk "Ahhh!!"
                show v5_mike6_cum1 with short
                "He sprayed me with his cum, and I welcomed it. It was my reward."
                "Ropes of warm and sticky fluid stained my skin. The stains of lust and a testament to my attractiveness..."
                
            "Riding on top":
                $ renpy.block_rollback()
                scene v5_mike7
                if lena_piercing1:
                    show v5_mike7_p1
                if lena_piercing2:
                    show v5_mike7_p2
                with long   
                mk "Oh fuck, baby...!"
                l "You like this? Just like this?"
                "I dragged my hips across his pelvis, squeezing him inside me."
                mk "Oh yeah. You move like a pro... Fuck, keep it up!"
                "I felt so naughty... Making this hot guy I had just met cheat on his girlfriend with me..."
                "I knew what I was doing was wrong, but I felt empowered and so turned on. Mike's desire for me was too overwhelming for him to control..."
                "And I enjoyed getting what I wanted. Especially knowing I shouldn't have it. But he wasn't able to deny it to me."
                "It felt great... for all the wrong reasons."
                mk "Fuck, I'm almost there! I'm gonna cum...!"
                menu:
                    "Get off Mike!":
                        $ renpy.block_rollback()
                        scene v5_mike6b
                        if lena_piercing1:
                            show v5_mike6_p1
                        if lena_piercing2:
                            show v5_mike6_p2
                        with long  
                        "I heeded Mike's warning and I quickly got off him."
                        "He grabbed his cock and jerked himself off to orgasm."                         
                        show v5_mike6_cum1 with flash
                        mk "Ahhh!!"
                        show v5_mike6_cum1 with short
                        "He sprayed me with his cum, and I welcomed it. It was my reward."
                        "Ropes of warm and sticky fluid stained my skin. The stains of lust and a testament to my attractiveness..."
                        
                    "Don't stop riding Mike!":
                        $ renpy.block_rollback()
                        $ v5_mike_cum = True
                        "I was so close to cumming too...! I didn't want to stop!"
                        "I kept riding him furiously, like one rides a bucking colt."
                        mk "Fuck Lena, I'm not joking! I'm gonna...!"
                        pause (1)
                        with vpunch
                        scene v5_mike7b
                        if lena_piercing1:
                            show v5_mike7_p1
                        if lena_piercing2:
                            show v5_mike7_p2
                        with flash
                        mk "Ahhhhh!!!"
                        "He came. He came inside me. I could feel his warm sperm spreading out."
                        "And seconds later I came, too."
                        play sound "sfx/ah4.mp3"
                        with vpunch
                        l "Ahhhh, fuck yes!!! Ahhh!!"
                        "Third one of the night. And maybe even the best one of those."
                        if lena_lust < 8:
                            play sound "sfx/xp.mp3"
                            show lust_up
                            $ lena_lust_xp += 1
                            call screen skillsup
                        "Mike twitched under me and his cock inside me, spouting every last drop of cum."
                        "It began dripping down his shaft, out of my soaking pussy..."
    
    else:
        "I felt he was getting a bit tired. It didn't seem he'd be able to cum like this, so I decided to mix things up."
        l "I want to ride you..."
        scene v5_mike7
        show v5_mike7_condom
        if lena_piercing1:
            show v5_mike7_p1
        if lena_piercing2:
            show v5_mike7_p2
        with long   
        "Mike didn't object. He lay down on my bed and I climbed on top of him, welcoming his sex into mine once more."
        mk "Oh fuck, baby...!"
        l "You like this? Just like this?"
        "I dragged my hips across his pelvis, squeezing him inside me."
        mk "Oh yeah. You move like a pro... Fuck, keep it up!"
        "I kept riding him hard, feeling how his cock pressured me, hard and ready to burst under the thin latex skin."
        "I felt so naughty... Making this hot guy I had just met cheat on his girlfriend with me..."
        "I knew what I was doing was wrong, but I felt empowered and so turned on. Mike's desire for me was too overwhelming for him to control..."
        "And I enjoyed getting what I wanted. Especially knowing I shouldn't have it. But he wasn't able to deny it to me."
        "It felt great... for all the wrong reasons."
        mk "Fuck, I'm there! I'm already there...!"
        "He gripped my hips as he pushed up with his, finally exploding in an orgasm."
        mk "Mghhh!!"
        with vpunch
        "I stopped my movements gradually, seeing his face of pleasure after the release."
        
    stop music fadeout 2.0
    if v5_mike_cum:
        $ fmike = "blush"
        $ flena = "blush"
    else:
        $ fmike = "flirt"
        $ flena = "slut"
    scene lenaroomnight
    show mikenude at lef
    show lenanude2 at rig
    if v5_mike_bareback and v5_mike_cum == False:
        show lena_cum2 at rig
    with long
    "Mike huffed and puffed, recovering after our intense and passionate dealings."   
    if v5_mike_cum:
        "He looked at me with astonishment while his cum leaked down my thigh."
        mk "Oh shit, we really did it..."
        l "I guess we did..."
        "And it had been my fault. I was the one who got carried away."
        l "Don't worry, it's my responsibility. Tomorrow I'll go fetch a morning-after pill."
        mk "Oh, OK... OK."
        $ fmike = "flirt"
    elif v5_mike_bareback:
        mk "I told you I would cum outside."
        l "I always believed it."
        "His jizz was dripping down my chest and abdomen, leaving shiny streaks on my skin."
    mk "That was incredible, baby... Just incredible."
    $ flena = "flirt"
    if v5_mike_cum:
        l "It was... Wow, I came three times! And what three times!"
    elif v5_mike_bareback:
        l "It was... Wow, I came two times! And what two times!"
    else:
        l "It was... The way you ate me out... Mhhh..."
    mk "You were lovely. Well..."
    "He got up from the bed and started picking his clothes up."
    mk "I'll get going."
    l "Don't you want to spend the night? It's late."
    mk "No, I have to go home... My girlfriend, you know..."
    $ flena = "flirtevil"
    l "Oh, yeah, that's true... In that case, don't you want to take a shower before leaving?"
    l "Maybe we can take it together..."
    $ fmike = "sad"
    mk "No, no, as you said, it's late... And I also normally take a shower at home, first thing after coming back from work."
    $ flena = "n"
    l "OK, suit yourself."
    $ fmike = "smile"
    hide mikenude
    show mike at lef 
    with short
    mk "Anyways, Lena... It's been a pleasure meeting you."
    mk "A real pleasure."
    $ flena = "slutshy"
    l "Same, but I think I gave you ample proof tonight..."
    $ fmike = "flirt"
    mk "Sure, you did."
    $ fmike = "smile"
    mk "I'll see myself out."
    $ flena = "smile"
    play sound "sfx/door.mp3"
    hide mike with short
    l "Wow, what a crazy night... I can't believe what just happened."
    if v5_mike_cum:
        $ flena = "blush"
        l "I really let him cum inside me... That was reckless."
        l "And it shouldn't take long for me to be on my period. These are the most dangerous days..."
        l "Tomorrow I'll go get that pill first thing in the morning."
        $ flena = "flirtshy"
        l "But it was so fucking hot, oh my God..."
    elif v5_mike_bareback:
        $ flena = "blush"
        l "We really did it bareback... But at least he came outside."
        l "Still, it shouldn't take long for me to be on my period. These are the most dangerous days..."
        $ flena = "flirtshy"
        l "In any case, it was so fucking hot, oh my God..."
    else:
        $ flena = "flirtshy"
        l "It was so fucking hot, oh my God..."
        l "Luckily we used a condom. It shouldn't take long for me to be on my period. These are the most dangerous days..."
        l "But I still felt his raw cock inside me, even if it was just a moment..."
    "I was feeling quite pleased, even if a bit irresponsible. But the fun I had had clearly outweighed the other."
    l "Oh Lena, you still have it."
    l "Oh yeah, you have it, and better than ever before."

jump v5lenasaturday

##LENA SATURDAY MORNING ###############################################################################################################################################################################################
        
label v5lenasaturday:
    
    $ day = "Saturday"
    scene blackbg
    with long
    call screen calendar
    scene lenaroom with long
    "It took quite a lot for me to get up the next morning."
    $ lena_necklace = 0
    $ lena_makeup = 0
    $ lena_look = 2
    play music "music/normal_day2.mp3" loop
    if lena_mike_sex:
        play sound "sfx/meow.mp3"
        show lola at lef with short
        "After meowing for ten minutes straight, Lola convinced me to get out of bed and put some food in her bowl." 
        $ flena = "worried"
        show lenanude at rig with short
        l "You can be a real bother, you know that?"
        "The night out had taken a toll on me, but it was a toll I was more than happy to pay."
        "I hadn't drunk that much, but I still had a slight headache. Other than that, I felt good..."
        $ flena = "slutshy"
        "Really good."
        "Mike had fucked me so good... It had been a really crazy situation. I had been a bad girl..."
        if v5_mike_cum:
            $ flena = "sad"
            l "But I need go to the pharmacy and buy the morning-after pill. And I should get back on the pill."
            l "My periods have been a bit irregular lately... Probably because of all this stress I'm under."
            "That should help make them regular."
            scene lenahome with long
            $ lena_look = 1
            play sound "sfx/door.mp3"
            show lena  with short
            "I got dressed, fed Lola and prepared to leave."
        else:
            if v5_mike_bareback:
                l "Even though we had taken some risks... I should consider getting back on the pill."
            else:
                l "It could've been risky, though... I should consider getting back on the pill."    
            l "My periods have been a bit irregular lately... Probably because of all this stress I'm under."
            "That should help make them regular."
            scene lenahome
            with long
            play sound "sfx/door.mp3"
            $ lena_look = 1
            $ flena = "n"
            show lenabra 
            with short
            "I went to the living room, fed Lola and prepared some coffee."
        if louise_jeremy:
            "Louise was still in her room and I doubted she'd come out anytime soon."
            l "She got really wasted last night... I guess she got too excited after learning about her good grade."
            "I couldn't really blame her. I had been on that side of the road too, even if it had been during my teens..."
            l "I'm sure she had a lot of fun. Now she'll have a titanic hangover."
        else:
            $ flena = "sad"
            "I worried about Louise. Last night things had gotten out of hand."
            "I knocked softly on her door."
            l "Louise... Are you awake?"
            l "..."
            l "Do you want to talk about what happened last night?"
            "I heard her shaky voice on the other side of the door."
            lo "I don't want to talk to anybody. Go away."
            $ lena_louise = 3
            play sound "sfx/frienddown.mp3"
            show friend_down
            l "OK..."
            "I was sure she was stingy because I decided to have sex with Mike instead of comforting her..."
            "Maybe I should've kept her company instead, but... I wanted to have fun."
            $ flena = "n"
            "Besides, I had already warned her, but she hadn't listened. I guessed she had to see it with her own eyes to believe it."
            "I wished things had happened some other way, though..."
        if v5_mike_cum:
            l "Anyways, let's go get that pill."                                          
                                          
    elif louise_jeremy == False:
        play sound "sfx/meow.mp3"
        show lola at lef3 with short
        "Lola was hungry and wanted me to feed her. And she wouldn't stop meowing."
        $ flena = "sad"
        if lena_louise_sex:
            $ flouise = "happy"
            show lenanude at rig3 with short
            l "Wait a minute... I'm getting up..."
            show louisenude with short
            lo "Mhh... Good morning, Lena..."
            $ flena = "blush"
            "Louise was still sleeping next to me, naked. Vivid flashes of what had just happened the night before came to mind."
            "I had really had sex with my friend..."
            lo "Ugh... I'm pretty hungover... Do you mind if I stay in bed a bit longer?"
            l "No, suit yourself... I'll go feed the beast." 
            lo "Thanks, Lena... You're the best..."
            $ lena_louise = 12
            play sound "sfx/friendup.mp3"
            show friend_up
        else:
            $ flouise = "sad"
            show lenabra at rig3
            l "Wait a minute... I'm getting up..."
            show louisebra with short
            lo "Nhh... Good morning..."
            $ flena = "blush"
            l "Good morning, Louise..."
            "Tonight had been a crazy and dramatic night. Especially when Louise had tried to kiss me..."
            l "How are you feeling?"
            lo "Like shit... I'm... I'm sorry about yesterday..."
            l "It's OK... I know how horrible these things feel. How confused they can leave you..."
            lo "Confused, yeah... Anyways, sorry for bothering you."
            lo "I'll go to my room and sleep some more... And I won't get out until Monday, I think."
            play sound "sfx/door.mp3"
            hide louisebra with short
            l "Well, that felt quite awkward... I hope she didn't take me rejecting her as something personal."
            $ flena = "serious"
            $ lena_jeremy = 2
            play sound "sfx/frienddown.mp3"
            show friend_down
            l "That guy, Jeremy... He's a real douchebag."
            $ flena = "n"
        play sound "sfx/meow.mp3"
        l "Coming, coming...!"
        scene lenahome with long
        $ lena_look = 1
        show lenabra with short  
        if lena_louise_sex:
            "As I fed Lola I wondered if I should've rejected Louise's advances."
            "It was clear she was in need of an emotional crutch to deal with Jeremy's betrayal and I had been there for her."
            "But wasn't that what friends do? It wasn't like I didn't enjoy it myself..."
            l "I just hope things don't get complicated."
        else:
            "I put food in Lola's bowl and prepared some coffee."
            "The night out had taken a bit of a toll on me, but it had been fun."
            "At least until that fight between Ivy and Louise..."
            
    else:
        play sound "sfx/meow.mp3"
        show lola at lef with short
        "After meowing for ten minutes straight, Lola convinced me to get out of bed and put some food in her bowl." 
        $ flena = "worried"
        show lenabra at rig with short
        l "You can be a real bother, you know that?"
        scene lenahome
        with long
        play sound "sfx/door.mp3"
        $ lena_look = 1
        $ flena = "n"
        show lenabra 
        with short
        "I went to the living room, fed Lola and prepared some coffee."
        "The night out had taken a bit of a toll on me, but it had been fun."
        "At least until Louise got completely wasted and I had to drag her back home..."
        l "She got really wasted last night... I guess she got too excited after learning about her good grade."
        "I couldn't really blame her. I had been on that side of the road too, even if it had been during my teens..."
        l "I'm sure she had a lot of fun. Now she'll have a titanic hangover. I doubt she'll be coming out of her room today."
        
    if v4_stan_shoot:
        if v5_mike_cum:
            show lena at rig
        else:
            show lenabra at rig
        with move
        $ flena = "n"
        $ fstan = "n"
        show stan at lef with short
        st "Oh... Good morning, Lena."
        st "About what you asked me the other day... Are we doing the photo-shoot today?"
        l "Oh, yeah, of course."
        if v5_mike_cum:
            l "I need to go get something... And I should take a shower and get a bit decent."
        else:
            l "I need to take a shower and get a bit decent first, though."
        st "Of course, no rush... I don't have any other plans today, so whenever it's good for you..."
        $ flena = "smile"
        l "OK, I won't make you wait for long."
        jump v5shootstan
    elif v4_danny_shoot:
        l "This afternoon I have the photo-shoot with Danny. I should make sure I'm fresh and composed..."
        jump v5shootdanny
    else:
        l "Good thing I can take the day easy. I need some real rest..."
        jump v5lenasatend
    
##STAN SHOOT  ###########################################################################################
    
label v5shootstan:
    scene lenahome with long
    $ flena = "n"
    if v5_mike_cum:
        "A bit before lunch, after buying the pill and taking a shower, I was ready to begin the shooting."
    else:
        "A bit before lunch, after I had taken a shower and composed myself properly, I was ready to begin the shooting."
    show lena with short
    "Stan was there to take directions. All I had to do was tell him how I wanted things."
    "But what kind of photos was I after?"
    menu:
        "Artistic nudes":
            $ renpy.block_rollback()
            $ v5_art_shoot = True
            $ flena = "smile"
            l "I will keep with what I've been doing: tasteful, artistic pictures."
            l "That's my style, after all. The kind of modeling I do best and the image I want to promote on social media."
            $ flena = "blush"
            l "That meant getting completely naked in front of Stan, though..."
            
        "{image=icon_lust.png}Spicy nudes" if lena_lust > 3 or stalkfap_pro > 0:
            $ renpy.block_rollback()
            $ v5_spicy_shoot = True
            l "I guess I need to spice things up a bit if I want to gain some traction with followers and brands..."
            l "That's what Ivy advised, in any case."
            l "And I guess it's not so different than my usual work... I'm just gonna crank the sexy side more than usual."
            l "Maybe I can wear some sexy underwear, a thong, and take it off for the camera..."
            $ flena = "blush"
            "I just realized that meant doing that in front of Stan. Could I pose like that for him?" 
    
    l "Last time I felt it was OK since I was in my underwear, but now..."
    $ flena = "n"
    l "I can't go thinking like that. This is work and I'm a professional."
    l "I'd much rather work with Danny, but I don't have the financial means. Stan is my budget photographer..."
    l "It's decided."
    stop music fadeout 2.0
    scene lenahome with long
    $ stan_camera = True
    "I let Stan know I was ready and he came out of his room with the camera."
    show stan at lef with short
    st "Where do you want to take the pictures? Here, in the..."
    $ flena = "n"
    $ fstan = "surprise"
    with vpunch
    if v5_art_shoot:
        show lenanude at rig with long
    else:
        $ lena_look = "sexy"
        show lenabra at rig with long
    l "We can do it here. The living room has space and good natural light..."
    if louise_jeremy:
        "I doubted Louise would come out of her room until night, considering how wasted she was yesterday."        
    elif lena_louise_sex:
        "Louise was at a family dinner today and she probably wouldn't come back until night."
    else:
        "I doubted Louise would come out of her room at all today. She was sulking deeply..."
    "It was pretty safe to use the living room for the photo-shoot."
    st "..."
    $ flena = "blush"
    if v5_art_shoot:
        hide lenanude
        show lenanude2 at rig 
        with short
    else:
        hide lenabra
        show lenabra2 at rig 
        with short
    l "Stan?"
    st "Oh, oh yeah!"
    with vpunch
    st "Here it's... It's O-{w=0.2}O-{w=0.2}O-{w=0.2}Okay."
    "How many {i}O{/i}s were those?"
    "Stan's face was red as a tomato and his eyes almost out of their sockets."
    "His reaction was so unprofessional... It made me feel so self-conscious."
    if v5_art_shoot:
        "I really was naked in front of Stan..."
    else:
        "I really was gonna get topless in front of Stan... And things would only get spicier moving forward."
    l "Oh, God."
    st "W-{w=0.3}what? Did you say something to me?"
    $ flena = "n"
    l "No, no..."
    "I took a deep breath and got my mind into work mode."
    "I was here to do a job and I didn't care who the guy on the other side of the camera was."
    if v5_art_shoot:
        play music "music/main_menu.mp3" loop
        scene v5_shoot_home
        show v5_shoot1a
        with long
        "I liked how the light came through the window and played with the curtains."
        "I grabbed one and wrapped it around my body."
        l "Make sure the camera's ISO is right for this exposition."
        st "Yeah, I know... I've been watching many tutorials."
        play sound "sfx/camera.mp3"
        with flash
        "I tried to find a silhouette that would look good with the curtains, playing with the texture of the light over my skin."
        "I couldn't see Stan's face, mostly hidden behind the camera, but I still couldn't shake off the awkward feeling I had before."
        "I hesitated a bit while choosing the poses, especially this next one."        
        scene v5_shoot_home
        show v5_shoot2
        if lena_piercing1:
            show v5_shoot2_p1
        if lena_piercing1:
            show v5_shoot2_p1
        with long
        "I turned to face Stan. The only thing covering my full nakedness from his eyes was that thin, translucent curtain..."
        "I felt naked... Of course I was, but I hadn't felt like this since my first photo-shoot. Maybe not even then."
        "That was why I didn't like to work with amateurs... They made me feel awkward..."
        "And especially Stan... I began wondering if this had been a good idea after all."
        play sound "sfx/camera.mp3"
        with flash
        "Stan kept shooting me as I continued to flow between a few poses."
        "I tried to relax once again. I couldn't express my art properly like this."
        scene v5_shoot3
        if lena_piercing1:
            show v5_shoot3_p1
        if lena_piercing1:
            show v5_shoot3_p1
        with long
        "I abandoned the curtains and closed my eyes, trying to forget about my surroundings."
        "I lay down on the floor, feeling my body, feeling the warm sunlight on my skin..."
        "This was more like it. Now it felt right."
        "I wanted to express something with my photos. Something that went beyond the mere image, something emotional."
        play sound "sfx/camera.mp3"
        with flash
        "Last time Stan kept asking questions and hesitating before taking each picture. I noticed he wasn't like that anymore."
        "It seemed like he had really applied himself and improved his skill."
        play sound "sfx/camera.mp3"
        with flash
        "I let him take nine or ten pictures more and decided to put an end to the shooting."
        "That was enough material for my needs."
        
    else:
        play music "music/sensual.mp3" loop
        scene v5_shoot_home
        show v5_shoot1b
        with long
        "I took off my bra and started with a very simple pose: my back facing the camera, giving it the nice curve of my back and ass."
        "I chose this thong to highlight its shape..."
        l "Make sure the camera's ISO is right for this exposition."
        st "Yeah, I know... I've been watching many tutorials."
        play sound "sfx/camera.mp3"
        with flash
        "I let him take a few pics from that angle. Maybe I had chosen it because it allowed me to cover my breasts from Stan's view?"
        "I felt naked... Of course I was, but I hadn't felt like this since my first photo-shoot. Maybe not even then."
        "That was why I didn't like to work with amateurs... They made me feel awkward..."
        "And especially Stan... I began wondering if this had been a good idea after all."
        play sound "sfx/camera.mp3"
        with flash
        "But I couldn't be shy now. I was trying to sell something sexy to my audience."
        "This was no different from my usual photo-shoots. I had to get into character to create something honest..."        
        scene v5_shoot_home
        show v5_shoot4
        if lena_piercing1:
            show v5_shoot4_p1
        if lena_piercing1:
            show v5_shoot4_p1
        with long
        "I got on my knees and raised my arm up, throwing back my hair in a sensual pose."
        "The camera, and Stan, had a perfect, unobstructed view of my breasts."
        play sound "sfx/camera.mp3"
        with flash
        "That was it, I had to feel sexy. I had to want to seduce the camera..."
        "I looked directly at the objective and I bit my lip while running my hand up my hair."
        play sound "sfx/camera.mp3"
        with flash
        "Last time Stan kept asking questions and hesitating before taking each picture. He wasn't like that anymore."
        "It seemed like he had really applied himself and improved his skill. Though he was completely quiet..."
        "Almost too quiet."
        l "Are the pictures turning out good?"
        st "Y-{w=0.3}y-{w=0.3}yes. Yes, they are."
        "He answered without moving the camera away from his face. I couldn't see his expression, but his voice sounded so tense."        
        scene v5_shoot_home
        show v5_shoot5
        with long
        "But I had already decided his awkwardness wasn't going to affect me."
        "I continued doing my thing. It was time to make use of the tool..."
        l "Get a low angle on this one."
        st "S-{w=0.3}sure."
        "Stan took a knee and pointed up with his camera. I slowly began sliding down the thong."
        "I swayed my hips from side to side without completely pulling down the panties, flirty and teasingly."
        play sound "sfx/camera.mp3"
        with flash
        play sound "sfx/camera.mp3"
        with flash
        "I found this pose really sexy and erotic. When I uploaded this to Peoplegram it would for sure cause a stir amongst my followers..."
        "And that was precisely the idea."
        if stalkfap:
            "I also had my Stalkfap subscribers to consider..."
            scene v5_shoot_home
            show v5_shoot6
            show v5_shoot6_hand
            if lena_piercing1:
                show v5_shoot6_p1
            if lena_piercing1:
                show v5_shoot6_p1
            with long
            "I finished removing the thong and I sat on the floor."
            "I covered my pussy with my hand and I spread my legs."
            "For a second it looked like Stan almost dropped his camera, but he kept it firmly in his hands, continually hiding his face behind it."
            play sound "sfx/camera.mp3"
            with flash
            "This was probably the boldest pose I had ever taken during a professional photo-shoot..."
            if v4_seymour_date:
                "Except maybe in my photo-shoot with Mr. Ward."
                "He had asked me to spread my legs like this... But then I had been wearing lingerie."
                if seymour_shoot > 2:
                    "I had also placed my hand right on top of my crotch..."
                    if seymour_shoot == 4:
                        "Well, I might've done a bit more than just covering it..."
                        "But just a tiny little bit more."
                "Just like then I felt the warmth emanating from my sex to the palm of my hand, only this time much more clearly."
            else:
                "I felt the warmth emanating from my sex to the palm of my hand, skin on skin."
            if stalkfap_pro:
                "But I knew Stalkfap subscribers wanted more. They paid for uncensored content."
                hide v5_shoot6_hand with long
                with vpunch
                "I removed my hand, making my sex visible."
                "A part of my body that had remained hidden during all my professional photo-shoots..."
                "The most intimate nook in a woman's body, the thing so many people were crazy to lay eyes upon."
                "Well, if that was what they wanted, I would give it to them. There was a screen between their eyes and me, and that put them at a whole wide world's distance."
                play sound "sfx/camera.mp3"
                with flash
                play sound "sfx/camera.mp3"
                with flash
                "Stan was in front of me, his body frozen in place like a statue. Only his index finger moved, pressing the camera's button."
                "And no wonder why... I was really showing him everything..."
                "What those other guys would see through a screen, he had it right in front of him. At an arm's length..."
                "I quickly closed my legs and got up."
            else:
                "This should please my subscribers."
                "Stan was in front of me, his body frozen in place like a statue. Only his index finger moved, pressing the camera's button."
                play sound "sfx/camera.mp3"
                with flash
        else:
            "This was spicy enough. No need to completely remove the thong, especially in front of Stan..."
        "With this I had enough material to post for a while."
        "And it should get people talking..."
    
    stop music fadeout 2.0
    $ flena = "smile"
    $ fstan = "blush"
    scene lenahome
    show lenanude at rig
    show stan at lef
    l "OK, we're done... Do you think you could edit the best pics and send them to me?"
    st "Yes, I've also been watching tutorials on how to use editing software..."
    st "Don't expect anything super professional... But I'll do my best."
    l "Thank you so much, Stan. You're really helpful."
    $ fstan = "shy"
    st "A-{w=0.3}anytime you want... You can ask me anything you need."
    $ fstan = "perv"
    st "I'll go to my room now and... work on the pictures..."
    st "I'll send you the results real soon."
    l "OK! Can't wait."
    play sound "sfx/door.mp3"
    hide stan with short
    $ flena = "worried"
    l "I'm still not sure about all this... But what's done is done."
    $ flena = "n"
    l "At least I saved quite a bit of money! I just hope the pictures come out nicely."
    jump v5lenasatend
    
##DANNY SHOOT #######################################################################################
          
label v5shootdanny:  
    
    scene street with long
    $ flena = "n"
    show lena with short
    "After having lunch I went to the studio, where I was to meet with Danny."
    "This time things were a bit different. I wasn't posing for him, rather he was taking photos for me."
    "It had to be me who decided what kind of photo-shoot it was going to be. The artistic direction was in my hands..."
    menu:
        "Artistic nudes":
            $ renpy.block_rollback()
            $ v5_art_shoot = True
            $ flena = "smile"
            l "I will keep with what I've been doing: tasteful, artistic pictures."
            l "That's my style, after all. The kind of modeling I do best and the image I want to promote on social media."
            l "And it's the kind of photography Danny's good at, too."
            
        "{image=icon_lust.png}Spicy nudes" if lena_lust > 3 or stalkfap_pro > 0:
            $ renpy.block_rollback()
            $ v5_spicy_shoot = True
            l "I guess I need to spice things up a bit if I want to gain some traction with followers and brands..."
            l "That's what Ivy advised, in any case."
            l "And I guess it's not so different than my usual work... I'm just gonna crank the sexy side more than usual."
            l "I should wear some sexy underwear, a thong, and take it off for the camera..."
            l "I just hope it doesn't feel weird to do in front of Danny."
            
    scene studio with long
    $ fdanny = "n"
    "When I arrived at the studio Danny was already there, punctual as ever."
    show danny at lef
    show lena at rig 
    with short
    dan "Hi, Lena! I'm so glad to see you!"
    l "Nice seeing you too, Danny. Let's get to work, shall we? I wouldn't want to waste your time."
    dan "Oh, please, don't worry. I have the whole afternoon for you, if you need it."
    l "It shouldn't take too long!"
    dan "So, what do you have in mind? Any style in particular? Just tell me what you want."   
    "I briefly told Danny about my idea for today's photo-shoot."    
    if v5_art_shoot:
        $ fdanny = "smile"
        dan "I see, something we're both familiar with, good. Any specific ideas?"
        l "Give me a moment and let me look around, see if I find something that inspires me..."
        "I checked the equipment room, the lights and the furniture available, searching for ideas."
        "There were some curtains hanging on one of the falls, and I decided it could be interesting to use them."
        stop music fadeout 2.0
        "I stripped down and got ready to begin."
        play music "music/main_menu.mp3" loop
        scene v5_shoot_studio
        show v5_shoot1a
        with long
        "I grabbed the curtains and wrapped them around my body."
        dan "Wait, let me set this light properly... There, I like how it shines through the fabric."
        dan "There, and the rim light on your hip is perfect."
        play sound "sfx/camera.mp3"
        with flash
        "Danny was a true professional and I felt comfortable working with him."
        "I tried to match his skill behind the camera with an interesting silhouette."
        "Something that would look good with the curtains, playing with the texture of the light over my skin."
        dan "Those are really beautiful, Lena, and elegant..."       
        scene v5_shoot_studio
        show v5_shoot2
        if lena_piercing1:
            show v5_shoot2_p1
        if lena_piercing1:
            show v5_shoot2_p1
        with long
        "I turned to face Danny. The only thing covering my full nakedness from him was that thin, translucent curtain, a veil that allowed you to see what was underneath."
        play sound "sfx/camera.mp3"
        with flash
        "Danny kept shooting me as I continued to flow between a few poses, playing with the curtains."
        "It was so easy working with Danny... I felt I could find the right poses naturally, and I had confidence that he would take great pictures of them."
        "Being able to trust him made me feel more at ease and natural before the camera."
        scene v5_shoot3b
        if lena_piercing1:
            show v5_shoot3_p1
        if lena_piercing1:
            show v5_shoot3_p1
        with long
        "I abandoned the curtains and closed my eyes, trying to forget about my surroundings."
        "I wanted to express something with my photos. Something that went beyond the mere image, something emotional."        
        "I lay down on the floor, feeling my body, my breathing, the warm lights on my naked skin..."
        play sound "sfx/camera.mp3"
        with flash
        dan "Oh, this pose is incredible, Lena!"
        play sound "sfx/camera.mp3"
        with flash
        dan "So beautiful... Hold it a bit more. I haven't found a shot this good in a while..."
        "I let Danny take a few more pictures and decided to put an end to the shooting."
        "That was enough material for my needs."
        stop music fadeout 2.0
        scene studio
        show lenanude at rig
        show danny at lef
        with long
        l "Thanks for your help, Danny."
        dan "It was my pleasure. The pictures turned out great, even better than in our last session together!"
        l "You think so?"
        dan "Let me edit them and I'll send them to you as soon as I can."
        l "I can't wait!"
        scene studio with long
        "With that done I could go back home and enjoy the rest of my Saturday."
        jump v5lenasatend   
   
    else:
        dan "Oh, I see... This is something different, I must admit."
        l "Is it an inconvenience?"
        dan "Oh, no. You just do what you have in mind and I'll adapt to it. The weight's on your shoulders!"
        l "Alright, let's do it."
        hide lena with short
        "I stripped down and changed to the clothes I had brought especially for this."
        $ lena_look = "sexy"
        show lenabra at rig with short
        "A cute thong and a pair of black high heels."
        dan "Whenever you're ready."
        play music "music/sensual.mp3" loop
        scene v5_shoot_studio
        show v5_shoot1b
        with long
        "I started with a very simple pose: my back facing the camera, giving it the nice curve of my back and ass."
        "I chose this thong to highlight its shape..."
        dan "Wait, let me set this light properly... There, I like how it shines through the fabric."
        dan "There, and the rim light on your hip is perfect."
        play sound "sfx/camera.mp3"
        with flash
        "Danny was a true professional and I felt comfortable working him him."
        "I tried to match his skill behind the camera with an interesting silhouette."
        dan "Very nice, Lena... This pose is sexy for sure!"
        "I slowly got into character, feeling more comfortable with the poses as I went."
        scene v5_shoot_studio
        show v5_shoot4
        if lena_piercing1:
            show v5_shoot4_p1
        if lena_piercing1:
            show v5_shoot4_p1
        with long
        "Each one was a bit bolder than before, each time I felt a bit more in control."
        "I got on my knees and raised my arm up, throwing back my hair in a sensual pose."
        play sound "sfx/camera.mp3"
        with flash
        dan "Nice, nice... I didn't know you had this playful side, too!"
        "Playful, yeah. This photo-shoot was a game, my own small game."
        "And the name of the game was being sexy. Feeling sexy. I had to want to seduce the camera..."
        "I looked directly at the objective and I bit my lip while running my hand up my hair."
        play sound "sfx/camera.mp3"
        with flash
        "I continued doing my thing and Danny kept shooting. It was time to make use of the tool..."       
        scene v5_shoot_studio
        show v5_shoot5
        with long        
        l "Get a low angle on this one."
        dan "As you wish..."
        "Dan took a knee and pointed up with his camera. I slowly began sliding down the thong."
        "I swayed my hips from side to side without completely pulling down the panties, flirty and teasingly."
        play sound "sfx/camera.mp3"
        with flash
        dan "Damn, Lena, this is too hot! If you post this some people are gonna get a heart attack!"
        l "Hee hee!"
        "I found this pose really sexy and erotic. And Danny was right: when I uploaded this to Peoplegram it would for sure cause a stir amongst my followers..."
        "But that was precisely the idea."
        if stalkfap:
            "I also had my Stalkfap subscribers to consider..."
            scene v5_shoot_studio
            show v5_shoot6
            show v5_shoot6_hand
            if lena_piercing1:
                show v5_shoot6_p1
            if lena_piercing1:
                show v5_shoot6_p1
            with long
            "I finished removing the thong and I sat on the floor."
            "I covered my pussy with my hand and I spread my legs."
            "For a second there I thought to see a shadow of surprise on Danny's face, but he kept his composure, like the professional he was."
            play sound "sfx/camera.mp3"
            with flash
            "This was probably the boldest pose I had ever taken during a professional photo-shoot..."
            if v4_seymour_date:
                "Except maybe in my photo-shoot with Mr. Ward."
                "He had asked me to spread my legs like this... But then I had been wearing lingerie."
                if seymour_shoot > 2:
                    "I had also placed my hand right on top of my crotch..."
                    if seymour_shoot == 4:
                        "Well, I might've done a bit more than just covering it..."
                        "But just a tiny little bit more."
                "Just like then I felt the warmth emanating from my sex to the palm of my hand, only this time much more clearly."
            else:
                "I felt the warmth emanating from my sex to the palm of my hand, skin on skin."
            if stalkfap_pro:
                "But I knew Stalkfap subscribers wanted more. They paid for uncensored content."
                hide v5_shoot6_hand with long
                with vpunch
                "I removed my hand, making my sex visible."
                "A part of my body that had remained hidden during all my professional photo-shoots..."
                "The most intimate nook in a woman's body, the thing so many people were crazy to lay eyes upon."
                "Well, if that was what they wanted, I would give it to them. There was a screen between their eyes and me, and that put them at a whole wide world's distance."
                play sound "sfx/camera.mp3"
                with flash
                play sound "sfx/camera.mp3"
                with flash
                "What those other guys would see through a screen, Danny had it right in front of him. At an arm's length..."
                "But it was OK. He was a professional, and we were just working together."
                "No need to feel awkward about it..."
            else:
                "This should please my subscribers."
                play sound "sfx/camera.mp3"
                with flash
            $ fdanny = "n"
            stop music fadeout 2.0
            scene studio
            show lenanude at rig
            show danny at lef
            with long
        else:
            "This was spicy enough. No need to completely remove the thong, after all."
            $ fdanny = "n"
            stop music fadeout 2.0
            scene studio
            show lenatopless at rig
            show danny at lef
            with long
        "With this I had enough material to post for a while."
        "And it should get people talking..."
        $ flena = "smile"
        l "Thanks for your help, Danny."
        dan "It was my pleasure... I must say that was quite an erotic photo-shoot..."
        l "I think we will get some good pictures, don't you think so?"
        dan "Oh, certainly... Let me edit them and I'll send them to you as soon as I can."
        l "I can't wait!"
        scene studio with long
        "With that done I could go back home and enjoy the rest of my Saturday."
        jump v5lenasatend 
        
        
##LENA SATURDAY NIGHT ###############################################################################################################################################################################################
          
label v5lenasatend:    
    
    scene lenaroomnight with long
    $ lena_look = 1
    $ flena = "n"
    if v4_stan_shoot or v4_danny_shoot:
        play music "music/normal_day2.mp3" loop
    "I spent the rest of the day relaxing, watching a TV series, listening to music, even playing the guitar a bit..."
    "It wasn't until nightfall that I decided to be a bit responsible. It was the end of the month, after all, so it was time to take care of important things."
    show lenabra with short
    l "Time to make ends meet..."
    "I picked up my phone and checked my bank account."
    $ lena_money += 4
    play sound "sfx/moneyup.mp3"
    show money_up
    $ flena = "smile"
    "The salaries from both the café and the restaurant had already been transferred to me."
    if lena_passion == "money":
        "Seeing those numbers on my bank account was one of the best feelings of the month. Too bad they weren't higher..."
    else:
        "Seeing those numbers at the end of the month always gave me security..."
    $ flena = "sad"
    "But this was the last time I would cash those checks in."
    "The café was probably closing for good, unless things got better... But I didn't see how."
    if cafe_help:
        "I said I would help them, but the truth was I had no idea how. I hadn't given it any serious thought yet..."
        "Time was running out, and I had no clue how much was left."
    else:
        "The Van Dykes would still employ me, but for how long? My time was running out, and I had no clue how much was left."
    if lena_robert_sex:
        $ lena_job_restaurant = 1
        "I still had a few nights per week at the restaurant, but I would only earn half as much."
        l "Maybe it's better this way, since working so many nights left me really tired and took a lot of time away from me..."
        l "But I'll need to compensate that loss of money with something else."
    else:
        $ lena_job_restaurant = 0
        "I was done with my job at the restaurant. It was a bittersweet feeling."
        l "I won't miss working so many late nights... But I'll need to compensate that loss of money with something else."
    if v4_seymour_date:
        "Having had that photo-shoot with Mr. Ward had been a helpful extra this month, no doubt."
        if seymour_shoot > 2:
            "Especially considering he had tipped me extra, since it seemed he was so pleased with my performance..."        
    if stalkfap:
        if v3_pg_danny:
            "I had gotten a bit of money from Stalkfap, too. Not too much, but every bit helped."
        else:
            "I hadn't gotten any real money from Stalkfap, yet. Just some pocket money."
        if stalkfap_pro:
            "Hopefully I would earn a more sizable amount moving forward. I was intent on it."
    if cafe_steal:
        $ flena = "worried"
        "I had even stolen from the Van Dykes... That was how worried I was about my financial situation."
        "I felt bad for doing so, especially considering the situation they were in, but I needed to survive."
    l "The rent is not cheap. And add to that food, utilities and other expenses..."     
    $ lena_money -= 3
    play sound "sfx/moneydown.mp3"
    show money_down
    l "And most of my salary is gone."
    l "There's no way I can save up money like this! I'm living day by day... Not good if I want to build a better future for myself."
    l "And I also need to consider my family... Dad is without a job and Mom's salary is really meager."
    l "I always tried to support them financially, even if it's been hard for me."
    $ flena = "serious"
    l "They can't count on my brother, that's for sure..."
    $ flena = "sad"
    l "But I don't know if I'm in a position where I can afford to support them myself."
    l "They don't have anyone else, though..."
    menu:
        "{image=icon_pay.png} Send money to your parents" if lena_money > 0:
            $ renpy.block_rollback()
            $ lena_money_family += 1
            l "They need my help, there's no other way around it... And they are counting on me."
            $ lena_money -= 1
            play sound "sfx/moneydown.mp3"
            show money_down
            "I transferred some money to their account."
            l "I hope I can solve my job situation soon so I can keep sending them money and don't have to worry about it so much."
            
        "I can't afford it right now":
            $ renpy.block_rollback()
            l "I'd like to, but I have my own problems to take care of right now."
            l "When I manage to solve my job situation I'll be in position to help them, but as of now..."
    
    if lena_robert_sex and lena_robert_over == False:
        scene lenaroomnight with long
        $ flena = "n"
        show lenabra with short
        "After dinner, while I was relaxing in my room, I got another text from Robert."
        play sound "sfx/sms.mp3"
        r "{i}Hey babe! How was your night out yesterday?{/i}"
        l "{i}Quite interesting, actually...{/i}"
        if lena_louise_sex:
            $ flena = "blush"
            "I wasn't gonna tell him about what happened between me and Louise, of course..."
            "But I told him about all the drama between Louise, Jeremy and Ivy."
            r "{i}Well, that sucks. You go out to have fun, not to deal with other people's drama {image=emoji_disgust.png}{/i}"
            $ flena = "n"
        else:
            if lena_mike_sex:
                $ flena = "flirt"
                "I wasn't gonna tell him about Mike, of course. But that had been interesting, no doubt!"
                $ flena = "n"
            if louise_jeremy == False:
                "I told him about all the drama between Louise, Jeremy and Ivy."
                r "{i}Well, that sucks. You go out to have fun, not to deal with other people's drama {image=emoji_disgust.png}{/i}"
            else:
                "I told him about our night and how Louise had ended up drinking way too much."
                r "{i}That sucks, but it's inevitable! It always happens to someone when I go out with my dudes {image=emoji_laugh.png}{/i}"
        l "{i}What about your vacation?{/i}"
        r "{i}Oh, it's great! The hotel is kickass and I'm having fun with the guys. We went to the beach today.{/i}"
        l "{i}I'm so jealous {image=emoji_love.png}{/i}"
        r "{i}But I miss you, babe. This would be so much more awesome with you.{/i}"
        r "{i}The two of us on the beach, you in a sexy bikini, drinking mojitos under the sun... {image=emoji_fire.png} {image=emoji_fire.png}{/i}"
        r "{i}Wish you were here, baby!{/i}"
        "I wasn't sure how to feel about what Robert was telling me. Sounded kinda romantic, right?"
        r "{i}What are you doing now, by the way?{/i}"
        l "{i}Just chilling in my room. Why?{/i}"
        r "{i}Since I'm missing you so much... Why don't you send me a picture so I can see you?{/i}"
        l "{i}So you want a picture?{/i}"
        r "{i}Yeah, like this one.{/i}"
        show lenabra at right with move
        play sound "sfx/sms.mp3"
        show v5_sexting2 with short
        $ flena = "shy"
        $ lena_robert_gallery = True
        $ lena_robert_pics.append("v5_sexting2.png")
        "I wasn't expecting that."
        r "{i}You see how much I miss you? This is how I get when I think about you being here with me...{/i}"
        l "Seems like Robert's in a raunchy mood..."
        menu:
            "Sext with Robert":
                $ renpy.block_rollback()
                $ v5_robert_sexting = True
                $ flena = "flirt"
                stop music fadeout 2.0
                "I felt playing along could be fun. It had been ages since I had done a bit of sexting."
                scene lenaroomnight with long
                "I stripped down and took a picture similar to the one he had just sent me."
                play sound "sfx/camera.mp3"
                show v5_sexting1 with short
                if lena_piercing1:
                    show v5_sexting1_p1
                if lena_piercing2:
                    show v5_sexting1_p2
                $ lena_lena_gallery = True
                $ lena_lena_pics.append("v5_sexting1.png")
                "I sent the picture to him."
                l "{i}You mean a pic like this? {image=emoji_flirt.png} {/i}"
                if lena_lust < 8:
                    play sound "sfx/xp.mp3"
                    show lust_up
                    $ lena_lust_xp += 1
                    call screen skillsup
                r "{i}Oh yeah baby, just like that!{/i}"
                r "{i}Damn you're so hot baby! I love it {image=emoji_fire.png} {image=emoji_fire.png} {image=emoji_fire.png}{/i}"
                r "{i}Send me another one. I want to see your body from the front.{/i}"
                l "Seems like he's quite demanding..."
                l "Well, since I'm already down with it, let's play some more."
                play sound "sfx/camera.mp3"
                scene lenaroomnight
                show v5_sexting3 
                if lena_piercing1:
                    show v5_sexting3_p1
                if lena_piercing2:
                    show v5_sexting3_p2
                with short
                $ lena_lena_gallery = True
                $ lena_lena_pics.append("v5_sexting3.png")
                l "{i}This is what you want?{/i}"
                r "{i}Fuck yeah baby {image=emoji_glasses.png}{/i}"
                r "{i}I can't believe how hot you are. You drive me crazy.{/i}"
                l "{i}Oh yeah? How so? {image=emoji_kiss.png}{/i}"
                r "{i}If my cock was hard before, it's going to burst now.{/i}"
                r "{i}I'm stroking it right now...{/i}"
                l "{i}You're touching yourself while looking at me? You must really like me...{/i}"
                r "{i}I love you, baby. And you? You like me touching myself while looking at your pics?{/i}"
                l "{i}Yes, I do {image=emoji_devil.png} {image=emoji_fire.png}{/i}"
                r "{i}Send me a picture touching yourself. I want you to masturbate like I'm doing right now.{/i}"
                l "Mhh, this is getting hot!"                
                play sound "sfx/camera.mp3"
                scene lenaroomnight
                show v5_sexting4 
                if lena_piercing1:
                    show v5_sexting4_p1
                if lena_piercing2:
                    show v5_sexting4_p2
                with short
                $ lena_lena_gallery = True
                $ lena_lena_pics.append("v5_sexting4.png")
                "I sent him the pic he was asking for."
                "My pussy was getting wet... I began playing a bit with it."
                r "{i}Oh fuck baby, I'm stroking my cock so hard.{/i}"
                r "{i}I love jerking off to your pics. I've done it so many times.{/i}"
                l "Wait, that means he's been doing it before? He must have been jerking himself off to the pics I post on Peoplegram...!"
                if lena_lust > 5:
                    "I could find the idea a bit unsettling but knowing he was so turned on because of me was kinda hot."
                    "We were more than simple co-workers now anyway."
                    r "{i}I wish it was my cock in place of your hand in that picture!{/i}"
                    "Things were getting heated up, and so was I..."
                    play sound "sfx/camera.mp3"
                    scene lenaroomnight
                    show v5_sexting5 
                    if lena_piercing1:
                        show v5_sexting5_p1
                    if lena_piercing2:
                        show v5_sexting5_p2
                    with short
                    $ lena_lena_gallery = True
                    $ lena_lena_pics.append("v5_sexting5.png")
                    "I took another pic and sent it to Robert."
                    l "{i}And I wish I was sucking your cock right now {image=emoji_devil.png}{/i}"
                    "I kept playing with my pussy while waiting for his reply. I was so wet..."
                    r "{i}Holy fuck , baby {image=emoji_fire.png} {image=emoji_fire.png} {image=emoji_fire.png}{/i}"
                    r "{i}I wish I had you choking on my big cock right now!{/i}"
                    l "Ohh, cocky..."
                    l "{i}Yeah, choke me and fill my mouth with your cum {image=emoji_cum.png} {image=emoji_cum.png}{/i}"
                    
                else:
                    "The idea was kind of hot but also a bit creepy... He had been using my pics to masturbate while we were mere co-workers."
                    r "{i}I wish it was my cock in place of your hand in that picture!{/i}"
                    l "{i}You'll have to wait until you come back.{/i}"
                    
                stop music fadeout 2.0
                $ flena = "shy"
                scene lenaroomnight
                show lenanude
                with long
                "After that Robert stopped answering for about three or four minutes."
                l "{i}You came, right?{/i}"
                play sound "sfx/sms.mp3"
                r "{i}Yeah baby {image=emoji_wink.png} {image=emoji_cum.png} {image=emoji_cum.png}{/i}"
                r "{i}You are incredible! Can't wait to be back and get a hold of you...{/i}"
                r "{i}I'm going to bed, tomorrow will be a long day! Night baby {image=emoji_kiss.png}{/i}"
                if lena_lust > 5:
                    $ flena = "slut"
                    l "Fuck, I'm way too horny to have it end like this..."
                    scene v4_solo1
                    if lena_piercing1:
                        show v4_solo1_p1
                    if lena_piercing2:
                        show v4_solo1_p2
                    with long
                    "I was still masturbating enthusiastically."
                    l "Mhh, so good... I need to finish this off."
                else:
                    l "Now what do I do with this horniness that's gotten into me?"
                    "My hand was still rubbing my clit softly."
                    $ flena = "sluthshy"
                    l "Well, since I'm already touching myself I could finish off what I started..."
                    scene v4_solo1
                    if lena_piercing1:
                        show v4_solo1_p1
                    if lena_piercing2:
                        show v4_solo1_p2
                    with long
                "Thankfully tomorrow would be an easy day. I didn't have anything to do... nor did I want to."
                "And this was the best prelude to a day like that."
                if lena_lust > 5:
                    "That sexting had me turned on... I could use Robert fucking me now."
                    scene v4_robert4 with long
                    if v4_robert_repeat:
                        "I remembered the last time Robert and I fucked."
                        "He gave it to me on all fours while I touched myself, like I was doing just now..."
                    else:
                        "I imagined him giving it to me..."
                        "On all fours while I touched myself, like I was doing just now..."
                    play sound "sfx/ah1.mp3"
                    l "Oh, fuck, feels soo good...!"
                else:
                    stop music fadeout 2.0
                    play sound "sfx/ah1.mp3"
                "I kept playing with myself until I orgasmed."
                "I fell asleep right afterwards."
                scene fade with long
                pause (1)
                jump v5lenawednesday
                
            "I don't want to":
                $ renpy.block_rollback()
                $ flena = "n"
                hide v5_sexting2 with short
                show lenabra at truecenter with move
                l "{i}No thanks, I'll pass.{/i}"
                r "{i}What do you mean you don't want to? Come on baby, I sent you one {image=emoji_disgust.png} {/i}"
                l "{i}Thanks, even though I didn't ask for it! But I'm not comfortable sending you those kind of pictures.{/i}"
                r "{i}You know you can trust me, come on.{/i}"
                l "{i}That's not gonna happen.{/i}"                
                play sound "sfx/xp.mp3"
                $ lena_charisma_xp += 1
                show charisma_up
                call screen skillsup
                "His persistence could get really annoying."
                r "{i}OK OK, what a way to kill the mood  {/i}"
                $ lena_robert -= 2
                play sound "sfx/frienddown.mp3"
                show friend_down
                stop music fadeout 2.0
                l "{i}Have fun tomorrow.{/i}"
                "I put down the phone."
                "Thankfully tomorrow would be an easy day. I didn't have anything to do... nor did I want to."
                l "I've been so burned out lately. I really need a day like this."
                jump v5lenawednesday
                
            "I'm not in the mood":
                $ renpy.block_rollback()
                $ flena = "n"
                hide v5_sexting2 with short
                show lenabra at truecenter with move
                l "{i}Sorry... Not in the mood right now.{/i}"
                r "{i}Come on baby, I sent you one {image=emoji_disgust.png} {/i}"
                l "{i}Thanks, even though I didn't ask for it... But I don't look good at all right now.{/i}"
                l "{i}My hair is all messed up and I have no makeup on.{/i}"
                r "{i}I don't care about any of that. I just want to see you, come on, please.{/i}"
                $ flena = "sad"
                l "{i}No, Robert, sorry... Not today.{/i}"
                $ lena_robert -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                stop music fadeout 2.0
                "His persistence could get really annoying."
                r "{i}Geez, OK... {/i}"
                r "{i}I'm going to bed, tomorrow will be a long day. Night baby.{/i}"
                l "{i}Have fun!{/i}"
                "I put down the phone."
                "Thankfully tomorrow would be an easy day. I didn't have anything to do... nor did I want to."
                l "I've been so burned out lately. I really need a day like this."
                jump v5lenawednesday                
           
    else:
        l "Anyways, tomorrow will be an easy day. I don't have anything to do... nor do I want to."
        l "I've been so burned out lately. I really need a day like this."
        jump v5lenawednesday    
        
##LENA WEDNESDAY ###############################################################################################################################################################################################
   
label v5lenawednesday:        
    
    stop music fadeout 2.0
    $ day = "Wednesday"
    $ week = 1
    $ month = "May"
    scene blackbg
    with long
    $ lena_look = 1
    $ flena = "n"
    call screen calendar
    scene cafe with long
    "After a mostly relaxing Sunday my week started again."
    show lenawork with short
    if lena_job_restaurant == 1:
        "I had worked Monday and Tuesday at the restaurant, and I had another shift tomorrow, but that was it."
        "My week felt quite less heavy than these last few months... Too bad my pockets would be emptier, too."
    else:
        "Not having to go to work at the restaurant felt weird. I owned my nights again, and I felt much more rested."
        "My week felt much less heavy than these last few months... Too bad my pockets would be emptier, too."
    if v4_ian_date:
        $ flena = "smile"
        "In any case, tonight I had a date with Ian and I was looking forward to it. Watching some live music at the record store seemed like a great plan, too."
        if ian_lena_sex:
            $ flena = "flirt"
            "Last time it had been so nice... I really enjoyed having sex with him, and I hoped tonight we could do it again."
            $ flena = "n"
            "But first I had to go to the gym. Which reminded me what Holly had told me."
            $ flena = "sad"
            "She had feelings for Ian, too..."
        elif v4_ian_kiss:
            $ flena = "shy"
            "Last time we had connected so well. I really liked how kissing him had felt..."
            "And maybe, just maybe... Tonight there would be more than just kisses..."
            $ flena = "n"
            "But first I had to go to the gym. Which reminded me what Holly had told me."
            $ flena = "sad"
            "She had feelings for Ian, too..."
        else:
            "Last time I had had fun with him, even though I had felt a bit awkward at some moments..."
            $ flena = "sad"
            "But that was mainly because I knew Holly had feelings for Ian..."
            "And before my date with Ian I had to go to the gym, where I would probably see her."
    else:
        "In any case, having that extra energy was helping me tackle day to day life in a better mood."
        "I was eager to burn some of that energy at the gym this afternoon... And after that I also wanted to check out the record store."
        "I had learned they were playing some live music tonight, and I was curious about it."
    $ fmolly = "n"
    $ flena = "n"
    show lenawork at rig with move
    show molly at lef with short
    mo "Everything good, Lena?"
    l "Yeah. Business as usual, though today quite a few people came in!"
    mo "Yeah, today wasn't a bad day... I just wish we could have many more like these."
    $ flena = "sad"
    l "Yeah... Still no solution in sight?"
    $ fmolly = "sad"
    mo "I'm afraid not... Ed is trying to find someone who wants to buy the business, but if he doesn't we'll have to close up shop soon either way..."
    l "I wish I could do something..."
    mo "No, it's us who wish they could! I'm so sorry leaving you without a job."
    l "It's not your fault..."
    if cafe_steal:
        mo "By the way, Lena... I've been checking the numbers and there's this one day that we cashed in so little money..."
        $ flena = "worried"
        mo "It's almost as if that day there had been barely any customers, even fewer than normal..."
        mo "Do you know something about it?"
        l "No... Maybe I made a mistake when counting the drawer or something like that..."
        mo "That's one of the possibilities I had in mind..."
        $ fmolly = "n"
        mo "Anyways, don't worry about it. These things happen."
        $ flena = "n"
        "Cold sweat ran down my back. That had been close... I almost got caught!"
    l "Well, it's my time to go. I'll see you tomorrow!"
    
    if encourage_holly == 3:
        $ holly_gym = True
    play music "music/jeremys_theme.mp3" loop
    scene polegym
    with long
    $ ivy_look = 2
    $ lena_look = 2
    $ holly_look = 3
    $ flena = "n"
    $ fivy = "n"
    $ fholly = "n"
    "I changed and went to the studio. Despite everything that had been happening, today I was in a good mood."
    show lena at rig 
    show ivy at lef
    with short
    v "Hey Lena! Ready to break a sweat? We're gonna build some booty today!"
    l "Oh, no, squats again? I hate those."
    v "Don't be a crybaby. There's no investment with a better payoff, except maybe a boob job!"
    v "You're a lucky girl and don't need one, so at least pay in sweat for a nice ass!"        
    if holly_gym:
        v "By the way, look who showed up too!"
        show ivy at lef3
        show lena at rig3
        with move
        show holly3 with short
        h "Hi..."
        $ flena = "smile"
        l "Holly! You decided to sign up to the gym?"
        h "Yeah... I thought I could give it a try... Even though I completely feel like a fish out of the water."
        v "Don't worry about it babe, you'll learn to breathe this air. You just need some determination!"
        hide holly3
        show holly2 
        with long
        $ fholly = "smile"
        h "I'll try my best."
        v "You'll see, if you stick with us we'll show you the sweet side of life, right Lena?"
        if lena_lust > 5:
            l "Yeah, we will!"
            $ fholly = "happy"
            h "Cool!"
        elif lena_lust > 3:
            l "We'll have fun together, that much is for sure."
            h "I'd like that."
        else:
            l "There are a lot of sweet sides to life, you just have to find the one you like..."
            v "Come on, that's no way to motivate someone!"        
    v "Let's get working!"
    scene v2_gym 
    if lena_piercing1:
        show v2_gym_p1
    if lena_piercing2:
        show v2_gym_p2
    with long
    "Ivy began the class and put us through torture."
    play sound "sfx/xp.mp3"
    $ lena_athletics_xp += 1
    show athletics_up
    call screen skillsup
    "After thirty minutes of aching and sweating she finally let us off the hook and I could catch my breath."
    if holly_gym:
        "Holly was barely able to keep herself upright and was now sitting in a corner, drinking water and looking like she was about to pass out."
    scene polegym
    $ fivy = "smile"
    $ flena = "sad"
    show lena at rig
    show ivy2 at lef
    with long
    if holly_gym:
        v "Poor thing, look at her. She's giving it her all, though!"
        if v4_ian_date:
            l "I'm spent, too! I don't think it's a good idea coming to your classes just before a date!"
            v "Oh, so you have a date? With whom?"
            $ flena = "smile"
            l "Ian."
            v "I see, I see..."
        else:
            l "I'm spent, too! My legs will hurt like hell tomorrow!"
            v "Stop complaining! You'll be fine, I've been teaching you for quite a while now!"
    else:
        if v4_ian_date:
            l "I'm spent! I don't think it's a good idea coming to your classes just before a date!"
            v "Oh, so you have a date? With whom?"
            $ flena = "smile"
            l "Ian."
            v "I see, I see..."
        else:  
            l "I'm spent! My legs will hurt like hell tomorrow!"
            v "Stop complaining! You'll be fine, I've been teaching you for quite a while now!"
    if louise_jeremy:
        v "By the way, how did Saturday's night end for you?"
        hide ivy2
        show ivy at lef
        with short
        v "Your friend Louise got really wasted. It was quite embarrassing, not being able to hold her alcohol at her age..."
        l "She got a bit too careless, but she was very happy because she's almost done with her masters degree."
        if lena_mike_sex:
            $ fivy = "flirt"
            v "Anyways, that's not what's interesting. You took Mike home, right?"
            $ flena = "shy"
    else:
        $ fivy = "serious"
        hide ivy2
        show ivy at lef
        with short
        v "By the way, your friend Louise better not try and lay a hand on me again."
        $ flena = "sad"
        v "She was lucky I didn't have the bouncers throw her out."
        l "That was... really unfortunate. But you provoked her... Did you really have to show her that picture?"
        v "She was calling me a slut and telling lies, so I had to put her in her place."
        $ fivy = "smile"
        v "I never tried to steal her boyfriend from her. If I did she would've been without a boyfriend much sooner!"
        v "Besides, you also told her Jeremy was lying to her and that she should break up with him. I just showed her the proof she needed to believe you!"
        l "In any case... It wasn't nice and I regret that it happened."
        v "Yeah, I guess you had to put up with her annoying drama afterwards, right?"
        if lena_mike_sex == False:
            $ flena = "blush"
            l "Yeah, that and... she tried to kiss me."
            v "What? No way! Ha ha ha!"
            v "What did you do?"
            if lena_louise_sex:
                l "Um, well, we... I got kinda dragged into the situation and..."
                v "Oh no. Don't tell me you lezzed out with her!"
                l "Shhh, lower your voice!"
                l "We... We slept together, yeah, but it was just one of those crazy things that can happen after drinking and partying..."
                v "I can't believe you, Lena. With that girl!"
                l "Well, she's my friend and I care for her..."
                v "I think it was a mistake, and I don't say this often. That girl is a real mess, watch yourself around her..."
            else:
                $ flena = "sad"
                l "I rejected her, of course. She was only looking for a way to plug her wound, but that won't heal it."
                v "Wise choice. That girl is a real mess, isn't she?"
                v "Watch out around her..."
        else:
            $ flena = "shy"
            l "Well, no... I was busy with other things..."
            $ fivy = "flirt"
            v "Oh, yeah... You took Mike home, right?"
            
    if lena_mike_sex:
        l "Yeah, I did..."
        hide ivy2
        show ivy at lef
        with short
        v "You slut! You fucked him, didn't you!?"
        l "Shhh, lower your voice! Yeah, of course I fucked him."
        v "He's really hot, right? I would like to have a taste myself, but since he has a girlfriend I never really tried..."
        v "But that didn't seem to matter to you!"
        l "Hey, he wanted a piece of me, too. It's not like I'm the only one at fault!"
        v "Of course not... And how was it? Is he any good?"
        $ flena = "flirt"
        l "Yeah, he is... It was a wild night!"
        v "That's my girl, ha ha! Will you see him again?"
        l "I don't think so. I didn't even get his phone number..."
        v "Oh, luckily for you I happen to have it! I'll share it with you later."  
        
    $ fholly = "sad"    
    if v4_ian_date:
        v "And now you have a date with Ian, huh?"
        l "Yeah. I will leave a bit earlier and shower at home so I can get changed."
        if holly_gym:
            show lena at rig3
            show ivy at lef3
            with move
            show holly3 with short
            h "Oh, so you'll be seeing Ian?"
            $ flena = "sad"
            l "Uh, yeah... We're going to the record store... They'll be playing live music."
            l "Wanna come?"
            h "No, no! I don't want to be a bother... Besides, I'm expected home for dinner."
            h "Just say hi to him for me... No, what am I saying...?"
            $ fholly = "smile"
            show holly2
            show holly3 
            with short
            h "Just have fun."
            "It was hard not to feel sorry for Holly, but... What was I supposed to do?"
        else:
            v "Have fun then! And be sure to tell me everything!"
        jump v5ianlenadate
    else:
        if holly_gym:
            show lena at rig3
            show ivy at lef3
            with move
            show holly2 with short
            h "Whew... I feel like I'm gonna die..."
            v "Don't be a drama queen! You'll be fine! A bit sore the next couple of days, but you know what they say:"
            v "No pain, no gain!"
            l "That tends to be true, yeah."
            h "I know, I know... I'm just not used to this kind of pain. And so much of it!"
            v "You'll get better, don't worry. And you'll learn to love the pain!"
            h "I don't see that happening, but... OK."
            l "Girls, I'm gonna hit the showers early. There's this thing I wanna go to..."
            l "They're playing live music at the record store. Why don't we go together?"
            h "I'd like to, but I can't... I'm expected home for dinner."
            l "What about you, Ivy?"
        else:
            l "I'm gonna hit the showers. There's this thing I wanna go to..."
            l "They're playing live music at the record store. Why don't we go together?"
        v "The plan doesn't sound too appealing, to be honest, but..."
        v "OK, since it's with you!"
        
        jump v5lenarecordstore
        
##IAN DATE ##############################################################################################################################################################################################################

label v5ianlenadate:
    
    $ ian_lena_dating = True
    
    stop music fadeout 2.0
    scene lenaroomnight with long
    $ ian_look = 3
    $ fian = "smile"
    $ flena = "n"
    $ lena_look = 1
    "Once home, I took a quick shower and made sure to be presentable."
    if stalkfap_pro:
        show lenanude with short
        "While I dried my hair it occurred to me to check my Stalkfap account, to see how my last picture was doing."
        show lenanude at rig3 with move
        show v5_stalkfap_post
        if lena_piercing1:
            show v5_stalkfap_post_p1
        if lena_piercing2:
            show v5_stalkfap_post_p2
        with short
        l "Oh, some more people subscribed! Let's see what they commented..."
        "\"{i}I can't believe your beauty Lena, you're like a dream come true!{/i}\""
        $ flena = "smile"
        "\"{i}Mhhh so sexy baby, but why hide your boobs? You showed them in the other pic...{/i}\""
        "\"{i}Nice pic but show boobs pls{/i}\""
        $ flena = "sad"
        "\"{i}Why are you covering up? We're paying for uncensored content, what's the point if you censor it with your hand? I'll unsubscribe if that's the case.{/i}\""
        l "Seems like they're not too pleased..."
        "There were a couple more comments, all stating that they wanted me to show my boobs."
        l "Damn... I thought it was a good picture! And most of the comments feel like complaints..." 
        "One of them had already threatened to unsubscribe, even. Things didn't seem to be going good...!"
        $ flena = "n"
        l "Damn, they want to see my boobs, then here you go."
        play sound "sfx/camera.mp3"
        show v5_stalkfap2 with flash
        $ lena_lena_pics.append("v5_stalkfap2.png")
        "I took a quick selfie and posted it without even editing it."
        "I was gonna be late to my date otherwise!"
        l "Time to get dressed. What should I pick...?"
        scene lenaroomnight with long        
    $ lena_look = 4
    show lena with short
    l "There, not too shabby! I wish my legs didn't feel so weak after that workout!"
    scene street2night with long
    show lena at rig with short
    "This time I arrived before Ian, but he showed up barely three minutes later."
    show ian at lef with short
    i "Oh, you beat me to it this time."
    $ flena = "n"
    l "Two to one, you're still winning. But I'll take the lead, just give me some time."
    $ fian = "happy"
    i "That means we're gonna keep meeting at least until you manage to surpass me? I think I'll be one hour early to our dates from now on..."
    $ flena = "happy"
    l "I'm afraid we'll keep meeting for a very long time, then!"
    $ fian = "smile"
    i "That's the idea..."
    "Oh, he was so sweet...!"
    l "Well, shall we go in?"
    i "After you."
    play music "music/flirty.mp3" loop
    scene recordstore with long
    $ flena = "smile"
    "There were more people than I expected. Most of the stools were taken, and the musicians were already starting their jam session."
    show ian at lef
    show lena at rig
    with short
    i "Do you want something to drink? I could use a beer."
    l "Sure, why not? Let's get one."
    "We went to the bar to get a couple of beers as the song progressed from the intro to the first verse. It was indie and jazzy."
    $ emma_look = 1
    $ femma = "n"
    show lena at rig3
    show ian at lef3
    with move
    show emma with short
    i "A couple of beers, please."
    $ femma = "smile"
    e "Ian! I didn't know you were coming!"
    i "It slipped my mind to let you know, sorry."
    if ian_emma_sex:
        $ femma = "flirt"
        e "Don't worry, slips aren't always bad, huh?"
        $ fian = "shy"
        i "Uh, ha ha, yeah."
        $ fian = "smile"
    $ femma = "n"
    e "Oh, hi! Lena was it, right?"
    if lena_emma > 4:
        l "Yes. And you're Emma if I remember correctly."
        e "The one and only!"
    elif lena_emma > 3:
        l "Yes. And you're... Eva, if I'm not mistaken."
        e "Close enough! Emma."
    else:
        l "Yes, and you were... Rebecca?"
        e "Not even close. Emma. You seriously think I look like a Rebecca?"
        l "No, no, sorry. I can be really bad with names."
    e "Do you know who also showed up here tonight?"
    i "Nope. Who?"
    e "There you have them!"
    $ fcindy = "n"
    $ fwade = "n"
    hide emma with short
    show ian at rig
    show lena at right
    with move
    show cindy2 at centerlef
    show wade at left
    with short
    $ flena = "n"
    "Emma pointed to a couple I didn't know."
    "One was a tall and handsome guy, but with questionable taste in clothes and a bit of a belly."
    "The other one was a really beautiful blonde with striking green eyes."
    if ian_go_cindy > 1:
        i "Oh, hey, guys...!"
        $ fwade = "smile"
        $ fcindy = "surprise"
        w "Hey dude, what are you doing here?"
        if v5_cindy_shoot:
            $ fcindy = "blush"
        else:
            $ fcindy = "n"
        c "Oh...! Hi, Ian."
        $ fian = "shy"
        i "Hey... So Lena told me about this gig and we decided to come check it out..."
        w "Same as me and Cindy."
        $ fcindy = "n"
        i "These are my friend Wade and his... girlfriend Cindy."
    else:
        i "Oh, hey, guys!"
        $ fwade = "smile"
        w "Hey dude, what are you doing here?"
        c "Hi, Ian!"
        i "So Lena told me about this gig and we decided to come check it out..."
        w "Same as me and Cindy."
        i "These are my friend Wade and his girlfriend Cindy."
    $ lena_wade_agenda = True
    $ lena_cindy_agenda = True
    l "Nice to meet you..."
    "I wasn't expecting to meet Ian's friends tonight... and it wasn't something I was thrilled about. I wanted a more calm and intimate date..."
    "The green eyed girl showed quite some interest in me. She interrogated me rather abruptly."
    c "So you're Lena! We finally get to meet you. Ian has been speaking a ton about you."
    $ fian = "blush"
    $ flena = "blush"
    i "Well, that's not exactly..."
    c "Well, not a ton, but you get my meaning. I imagined you'd be a bit taller..."
    c "But it's easy to tell you're a model!"
    "How much had Ian told them about me? And why was I getting weird vibes from this girl?"
    $ flena = "n"
    l "Well, he hasn't told me about you guys, so I don't really know what to say... You're also friends with Perry and Jeremy?"
    w "Yeah, and with Emma, the bartender girl too."
    $ fian = "smile"
    i "We all went to high school together, except Cindy."
    hide cindy2
    show cindy at centerlef 
    with short
    c "Yeah, but tell me a bit more about your job as a model. I'm curious."
    "She didn't seem to be giving me the option to decline her demand..."
    menu:
        "It's a job like any other":
            $ renpy.block_rollback()
            "I wasn't exactly feeling like entertaining her... Especially when I felt I was being measured."
            l "It's nothing special, really... Just a job like any other."
            c "Really? Doesn't look like it to me."
            l "It does, when you're inside that world. I should know."
            c "Oh, too bad. I expected you'd have some interesting stories to tell."
            l "Don't we all? But today I'd rather enjoy the music instead of talking about myself."
            $ fcindy = "serious"
            $ lena_cindy -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            c "Oh. OK."
            "It seems like that stung her ego. It was pretty swollen..."
            "I looked at Ian, asking him without words to move on with our date. He understood."
            i "Well guys, we'll leave you to your date. We didn't mean to intrude."
            w "No intrusion at all."
            i "Let's go see if we can find a place to sit down..."
            l "Nice to meet you!"
            w "Bye!"
                
        "What do you want to know?":
            $ renpy.block_rollback()
            l "What do you want to know?"
            c "How does one normally get in?"
            l "There are many ways... I did it through a friend who was already modeling. Basically you just need to know a photographer."
            c "But like, do they contact you or you hire them...?"
            l "It depends. It's a word of mouth thing, usually. You start working with a friend, or a friend of a friend, then they talk about you or they see your work and they contact you."
            c "I see..."
            "She fired a couple more routine questions. Not the subject I was hoping to discuss tonight... but I tried to be polite to Ian's friend."
            "Thankfully he felt my awkwardness and decided to intervene."
            i "Well guys, we'll leave you to your date. We didn't mean to intrude."
            w "No intrusion at all."
            i "Let's go see if we can find a place to sit down..."
            l "Nice to meet you!"
            c "Bye!"
            
        "I'm not here to talk about work":
            $ renpy.block_rollback()
            "Well, I didn't like her rude manners, and I decided to let her know."
            l "I'd rather not talk about work on my night off, if you don't mind."
            "I said it very politely, and with a smile, of course."
            $ fcindy = "serious"
            $ lena_cindy -= 2
            play sound "sfx/frienddown.mp3"
            show friend_down
            "But she caught my meaning. Of course she did, same as I did hers."
            c "Alright... It's just that it seems to be something really interesting... I imagined it'd be something you'd like to talk about."
            $ fian = "worried"
            l "It's nothing special, really. I'd just rather enjoy the music and the company."
            "I looked at Ian. It seemed he was onto the weird vibe that had settled."
            "Wade, on the other hand, looked as aware of it like a hunter in a moonless night."
            $ fian = "n"
            i "Uh, so... We'll leave you to your date. We didn't mean to intrude."
            w "No intrusion at all."
            l "Nice to meet you!"
            w "Bye!"
    
    hide cindy 
    hide wade
    with short
    show ian at lef
    show lena at rig
    with move
    i "Sorry about that. I had no idea they'd be here."
    l "Don't worry. Seems like I already know most of your social circle, huh?"
    i "It would seem so... I have no clue about yours, though. Aside from Ivy."
    l "It's pretty small... I already told you about Louise and Stan... Maybe I can introduce you to them one of these days."
    "We drank our beers while listening to the band. They were pretty good!"
    $ flena = "smile"
    l "I like them! What do you think?"
    i "Not my kind of music exactly, but I'm enjoying it. Have you been writing recently?"
    $ flena = "n"
    if v3_ian_date and v2_holly_song:
        l "Not really, apart from that one I showed you at my place... I've been polishing it a bit, but no new songs..."
    else:
        l "Not really... I've been polishing one I wrote recently but not too much going on..."
    i "Why don't you play here one of these days? You could ask Emma to set you up!"
    $ flena = "worried"
    l "Who, me?"
    i "Yeah, it could be a good way to play in front of an audience and start making some noise... Letting people disover your music..."
    l "No way... I can't play in front of these many people."
    i "This isn't that many people..."
    l "Besides, nobody would come. Nobody knows I even play."
    i "That's why yopu have to let them know. Besides, you'd have at least one spectator. I would come."
    $ flena = "shy"
    l "That makes me even shyer, ha ha..."
    $ flena = "n"
    l "But enough about that... What have you been up to?"
    "We talked about our weeks. He told me about his struggles at work and about his night out."
    if lena_louise_sex or lena_mike_sex:
        "I did the same, omitting some parts, of course..."
    else:
        "I did the same."
    if louise_jeremy == False:
        $ fian = "sad"
        i "So that's what happened with Jeremy and Louise... Damn, that guy..."
        l "Really appalling."
    $ fian = "smile"
    "We didn't need to talk all the time, though. We stood silently one beside the other, listening to the music."
    "It wasn't awkward. It didn't feel like there was something that needed to be said, nor the tension to say it."
    "It felt nice, like I could relax and just be."
    if v4_ian_kiss:
        $ flena = "shy"
        "We were shoulder to shoulder, and at one point of the night Ian held my hand."
        "When was the last time someone held my hand? And when was the last time I blushed and smiled so stupidly?"
    else:
        "We were shoulder to shoulder, very close together... But there was still a tension keeping us apart."
        "My fault for acting hesitant last time..."
    "We had a second beer and stayed until the concert ended. Then we said goodbye to Ian's friends and left."
    stop music fadeout 2.0
    $ flena = "smile"
    $ fian = "smile"
    scene street2night
    show ian at lef
    show lena at rig
    with long
    "We walked one beside the other, without any rush. The night and the streets were silent."
    l "It was a nice performance, and I liked the ambience."
    i "They do this kind of thing quite often. We could come again."
    l "I would love it."
    "Ian suddenly stopped."
    $ flena = "n"
    l "Huh?"
    play music "music/main_menu.mp3" loop
    scene street2night 
    show v5_ian_kiss
    with long
    "He grabbed my hand and pulled me towards him, kissing me."
    if v4_ian_kiss == False:
        "It shocked me for a couple of seconds, but then I closed my eyes and kissed him back."
        "This was what we should've done last time... but we didn't dare."
        "I was happy Ian finally did. We could finally address our true feelings."
    else:
        "I closed my eyes and kissed him back. I was greeted with the familiar and soft sensation of his lips on mine."
        if ian_lena_sex:
            "And that was not the only familiar sensation I got from him..."
        "We had been waiting all night for this moment."
        "The moment of coming together once again, of embracing each other, of addressing our true feelings..."
    "We stood in the middle of the street, kissing deeply, unconcerned with our surroundings."
    "And nothing and no one disturbed us."
    if ian_lena_sex == False and v4_ian_kiss:
        "We took our time, savoring each other with care. But that care wasn't the whole extent of our lust, oh no."
        "And the more we kissed the more that lust was being revealed."
        "Passion was overflowing from both ends... A passion that wanted sublimation."
    $ flena = "flirt"
    $ fian = "shy"
    scene street2night
    show ian at lef
    show lena at rig
    with long
    if ian_lena_sex:
        l "So... We're not far away from my place... We could, you know..."
        i "Yeah, I was thinking the same thing..."
        $ fian = "sad"
        $ flena = "n"
        play sound "sfx/ring.mp3"
        i "Oh, sorry... I gotta take this. Someone's been sending me texts the whole night long, but I didn't want to look at my phone..."
        l "Go ahead, it might be important."
        hide ian
        show ian_phone at lef
        with short
        i "Yes?"
        $ fian = "serious"
        i "What? No, I haven't seen your messages... I'm busy, dude!"
        i "What!? What do you mean you can't get home?"
        $ fian = "worried"
        i "Wait up, Perry. Where did you lose your keys? You can't remember? Really?"
        $ flena = "sad"
        i "And you lost your wallet, too!? Yeah, lost, stolen, whatever. Dude, can't you go to your parents' place?"
        i "What? Come on, man..."
        i "..."
        i "Shit. OK, OK, I'm going. Stay put."
        hide ian_phone
        show ian at lef
        with short
        $ fian = "n"
        i "My flatmate has had some problems..."
        l "Yeah, I overheard. I guess it'll have to wait for another night, right?"
        i "So it seems... Damn, I'm sorry."
        l "It's not your fault. If anything, you're being a good friend."
        $ fian = "serious"
        i "I'll kill him, I swear."
        $ flena = "n"
        l "Don't worry. There'll be other chances. Plenty."
        $ fian = "smile"
        i "If that's the case... I can leave a bit less bummed."
        l "See you soon, OK?"
        i "Whenever you like."
        hide ian with short
        "We kissed goodbye and we went our separate ways."
        $ flena = "sad"
        l "Ahhh, I wanted to sleep with him so bad... That was unfortunate."
        l "Thankfully we already did it once, else I would be biting my nails right now!"
        $ flena = "shy"
        if v5_robert_sexting:
            l "Well, I guess I'll need to take care of things with my own hands, today... Again."
        else:
            l "Well, I guess I'll need to take care of things with my own hands, today..."
        "But I could wait. I already had it once, and I knew I liked it."
        jump master_script
    elif v4_ian_kiss:
        l "Say... We don't really need to stand in the middle of the street. I don't live far from here, if you don't mind walking me home..."
        i "I don't mind at all."        
    else:
        "When our kiss ended both of us felt a bit awkward."
        i "Sorry, that was a bit sudden..."
        l "No, I... I was expecting it to happen."
        $ fian = "smile"
        i "Glad to know that's the case, then. I wasn't sure..."
        l "I hope I have dispelled your doubts..."
        scene street2night 
        show v5_ian_kiss
        with long
        "This time it was me who kissed him. It felt as good as I had suspected it would."
        "We went deep and slow, making the moment last. Savoring each other with care."
        "But that care wasn't the whole extent of our lust, oh no. And the more we kissed the more that lust was being revealed."
        "Passion was overflowing from both ends... A passion that wanted sublimation."
        menu:
            "Take Ian home":
                $ renpy.block_rollback()
                $ flena = "flirt"
                $ fian = "shy"
                scene street2night
                show ian at lef
                show lena at rig
                with long
                l "Um, say... We don't really need to stand in the middle of the street. I don't live far from here, if you don't mind walking me home..."
                i "No, no... I don't mind at all, of course..."  
                        
            "End the night":
                $ renpy.block_rollback()
                "But for some reason, now didn't feel like the right time."
                "I liked Ian a lot but... I didn't want to rush things. I feared that rushing them would spoil what we had going."
                $ flena = "blush"
                $ fian = "shy"
                scene street2night
                show ian at lef
                show lena at rig
                with long
                stop music fadeout 2.0
                l "Um, so... Tonight was a great night. Thanks, Ian..."
                i "Yeah, it was..."
                $ flena = "shy"
                l "Well, I can get home on my own from here. See you soon, OK?"
                $ fian = "sad"
                i "Uh, oh... Sure."
                $ fian = "smile"
                i "Whenever you like."
                hide ian with short
                show lena at truecenter with move
                "Like this was enough for now. I didn't want Ian to think I was an easy girl, only looking to hook up..."
                "I felt he had the potential to become something more..."
                jump master_script
    
    l "Let's go, then."
    stop music fadeout 2.0
    play sound "sfx/door_home.mp3"
    scene lenahomenight_dark with long
    show ian at lef
    show lena at rig
    with short
    if v3_ian_date:
        l "This way."
        "It wasn't the first time Ian was at my place. He followed me swiftly to my room."
    else:
        i "So... this is your place?"
        l "Yes, come on in... Let's go directly to my room, I don't want to disturb my flatmates."
        i "Sure."
    play sound "sfx/door.mp3"
    scene lenaroomnight
    show ian at lef3
    show lena at rig3
    with long
    if v3_ian_date:
        l "Sorry, I know my room's a bit small, but..."
        i "It's OK..."
        play sound "sfx/meow.mp3"
        show lola 
        with short
        $ fian = "smile"
        $ flena = "n"
        "Lola jumped on the bed, curious about the new visitor."
        i "Oh, hello there kitty."
        l "Watch out, she's not..."
    else:
        l "So, this is my room. It's a bit small, but it's all I need..."
        i "I really like the lights. And..."
        play sound "sfx/meow.mp3"
        show lola 
        with short
        $ fian = "smile"
        $ flena = "n"
        i "Oh, you have a cat!"
        l "Oh, yes, her name's Lola. Watch out, she's not..."
    "Before I could warn Ian, he extended his hand towards Lola."
    "He stopped just before touching her, letting her sniff him out."
    "Then he scratched her forehead and Lola closed her eyes, enjoying herself."
    play sound "sfx/purr.mp3"
    hide lola
    show lolahappy 
    i "She's so cute."
    l "That's strange, she normally doesn't let people pet her. Especially guys..."
    i "She doesn't seem to mind."
    "I joined him in petting Lola. She made her rear stick out, tail pointing up, asking for more caresses."
    i "She's really enjoying herself..."
    l "She is..."
    "As we petted Lola, my hand found Ian's and we exchanged caresses amongst Lola's fur."
    "I looked up at him only to discover his amber eyes already staring at me."
    play music "music/ourredstring.mp3" loop
    scene lenaroomnight
    show v5_ian_kiss
    with long
    "We kissed again, pulled together by some kind of gravity."
    "My hands wanted to be tangled in his hair and under his shirt. I wanted to be caught in his embrace."
    scene v4_lena1
    if lena_piercing1:
        show v4_lena1_p1
    if lena_piercing2:
        show v4_lena1_p2
    with long
    "My lips were hungry for his kisses, and my touch for his body. And Ian was no stranger to this feeling."
    "As we continued to kiss our clothes began littering the floor, thrown away with disregard."
    "I finally felt his hands directly on my naked skin, as his fingers descended down my back and held my hips, pulling me closer towards him."
    "His body was so incredibly warm... I felt I was about to start sweating just by making out."
    "His tongue entangled with mine performing a wet and luscious dance. Our desires had been set free and were mixing together..."
    "Ian's hands didn't venture outside the safe zone. It seemed like he was hesitant to extend his caresses to my ass or breasts."
    "That was his lovely awkwardness at work... It was to be expected for him to be a bit shy."
    scene v4_lena3
    if lena_piercing1:
        show v4_lena3_p1
    if lena_piercing2:
        show v4_lena3_p2
    with long
    "But that hesitation didn't last for long. He slowly began conquering new territory with my implicit consent."
    "He made me lie down on the bed, his hands caressing my neck, my hair, my belly, my breasts..."
    "I shivered when I felt the brush of his touch on my sensitive nipples. I kissed him deeper."
    "Ian could feel how much I wanted this. How much I wanted him."
    "And he was determined to please me."
    scene v4_lena3b
    if lena_piercing1:
        show v4_lena3_p1
    if lena_piercing2:
        show v4_lena3_p2
    with long
    "His hand ran down my belly, slowly but deliberately. It snuck under my panties, his fingertips sliding over my mons pubis..."
    "The anticipation was almost unbearable... The heat emanating from his fingers too..."
    play sound "sfx/mh1.mp3"
    "And when they finally reached my slit, a jolt of ecstasy spread across my whole body."
    "Ian sank his fingers in, gently, going over the entire length of my sex, soaking them with my moisture."
    "He didn't take long to find my clit, stimulating it with slow and light strokes."
    "Meanwhile, his lips were busy with mine, or took a detour to my neck and collarbone from time to time."
    play sound "sfx/ah1.mp3"
    l "Ohh... Ian... It's so good..."
    "I didn't need to tell him. He was good at reading me."
    "He noticed how my pleasure and excitement were growing, so he increased the pressure and speed of his fingers."
    "The way he was touching me was in perfect sync with what my body needed and desired. I couldn't stop moaning and shivering."
    "The pleasure was building up rapidly. Too rapidly."
    l "Ian, I... Ahhh...!"
    "He doubled down. His fingers were about to take me to Heaven."
    play sound "sfx/oh1.mp3"
    with vpunch
    l "Ohhhh...!!"
    "I squeezed my legs together, trembling, almost like I was hit by a seizure. And in truth it was exactly that."
    "An orgasmic seizure that made me feel like my body was melting. He had given me such an amazing orgasm using just his hand!"
    l "Oh, God..."
    i "Are you alright?"
    scene v4_lena2 with long
    l "You have no idea."
    "I would've liked to enjoy the aftermath of my climax a bit more, but it was my turn to take the initiative."
    "I wanted to show Ian I liked to give pleasure as much as I liked to receive it."
    "I took off my panties with a playful smile and climbed on top of him."
    "Our lips met again in a deep and passionate kiss while my hands slid down his chest and torso, feeling Ian's build."
    "He was lean and quite athletic and had broad shoulders. He was handsome, too... I found everything about him attractive."
    if lena_bdick > 1:
        "I wondered what he would be hiding under his pants... I hoped I wouldn't be disappointed..."
    "Ian began letting loose as he felt my unrestrained passion."
    "His hands became bolder, exploring my body slowly, thoroughly, attentively..."
    "He dug his fingers into my butt cheeks and ran them down my thighs, making me shiver."
    "My pussy was ready for a second round and my hips wanted to move on their own..."
    "As we kissed I began grinding on top of him, pressing my crotch down on his."
    "I could feel the bulge under his pants, and I knew I wouldn't be disappointed..."
    menu:
        "Suck him off":
            $ renpy.block_rollback()
            if lena_bj < 3:
                $ lena_bj += 1
            "I had no rush... I wanted to enjoy him, to enjoy the moment..."
            "And I wanted him to enjoy me."
            scene v4_lena4
            with long
            "I moved down to between his legs and unbuttoned Ian's fly."
            "His erect member greeted me when I pulled his pants away."
            i "Lena... What are you trying to...?"
            i "Oh...!"
            "His words were interrupted when I soothed his worrying."
            play sound "sfx/mh1.mp3"
            "I grabbed his cock and brought it to my lips, kissing the tip."
            if lena_bdick > 1:
                "He wasn't packing a monster cock, but he had length and girth to spare."
                if lena_robert_sex:
                    "It was just a bit longer than Robert's, but noticeably thicker."
                    if lena_mike_sex:
                        "And about the same size as Mike's..."
                elif lena_mike_sex:
                    "It was about the same size as Mike's..."
            else:
                if lena_robert_sex:
                    "It was just a bit longer than Robert's, but noticeably thicker."
                    if lena_mike_sex:
                        "And about the same size as Mike's..."
                else:
                    "He was well endowed, that much was true..."
                    if lena_mike_sex:
                        "It was about the same size as Mike's..."
            play sound "sfx/bj1.mp3"
            "I took my time kissing and licking his manhood, getting to know it, its shape, its taste..."
            "Noticing Ian's reactions depending on where and how I licked him, the way he tensed his body, how his breathing changed, when he sighed..."
            "I spent several minutes with it, and each time I felt more excited, more willing to be taken by Ian..."
            "And this time it wasn't me who decided to take the lead."
            i "Lena, that's enough. I can't wait anymore, I want to be inside of you..."
            l "Just what I wanted to hear..."
            "I reached out and grabbed a condom from the drawer."
            if v5_mike_bareback:
                "I would've liked to feel him raw, but this time I wasn't going to be so irresponsible..."
            scene v4_lena5
            if lena_piercing1:
                show v4_lena5_p1
            if lena_piercing2:
                show v4_lena5_p2
            with long
            "He put on the condom and took position between my legs."
            
        "Have sex":
            $ renpy.block_rollback()
            "I wanted to feel it inside me so badly... I couldn't wait."
            "I reached out and grabbed a condom from the drawer."
            if v5_mike_bareback:
                "I would've liked to feel him raw, but this time I wasn't going to be so irresponsible..."
            l "Ian... I want you inside me..."
            scene v4_lena5
            if lena_piercing1:
                show v4_lena5_p1
            if lena_piercing2:
                show v4_lena5_p2
            with long
            "He didn't argue. Instead, he began unbuttoning his pants and I helped him pull them off."
            "He put on the condom and took position between my legs."
            if lena_bdick > 1:
                "He wasn't packing a monster cock, but he had length and girth to spare."
                if lena_robert_sex:
                    "It was just a bit longer than Robert's, but noticeably thicker."
                    if lena_mike_sex:
                        "And about the same size as Mike's..."
                elif lena_mike_sex:
                    "It was about the same size as Mike's..."
            else:
                if lena_robert_sex:
                    "It was just a bit longer than Robert's, but noticeably thicker."
                    if lena_mike_sex:
                        "And about the same size as Mike's..."
                else:
                    "He was well endowed, that much was true..."
                    if lena_mike_sex:
                        "It was about the same size as Mike's..."
               
    "His amber eyes found mine in my dimly lit room."
    "The small light bulbs hanging from the ceiling were reflected in his irises, making them shine like gold."
    "A gold that was staring directly into my eyes, locked in place by a magnetic force that bound Ian and me."
    l "Go slowly..."
    i "Yeah, that was my intention."
    "Hearing him whisper and feeling the tip of his cock slide against my slit sent a shiver up my spine and I couldn't help but tremble."
    "Finally it was going to happen... Deep down I had been wanting this since I had first laid eyes on Ian."
    "And as I got to know him a bit better, that desire had only grown. And now..."
    play sound "sfx/ah1.mp3"
    l "Ahh..."
    "I moaned when I felt the head of Ian's sex penetrate me."
    "He began pushing it in slowly, making sure I had room for him."
    "Bit by bit he slid his manhood in, taking his time, his eyes on mine, looking at my reactions, reading my feelings."
    "He was making love to me."
    scene v4_lena6
    with long
    "It didn't take Ian long to be fully inserted in me. I was wet and welcoming."
    "He began moving his hips slowly, delighting us both with the feeling of his cock sliding in and out of my pussy."
    "That pleasurable trail, that ecstatic contraction and expansion..."
    play sound "sfx/ah3.mp3"
    l "Ohhh, Ian..."
    i "Mhh..."
    "He kissed me on the lips, on the cheek, on the ear, on the neck..."
    l "Ohh, yes..."
    "And his hips were not stopping. No, their movement was getting faster and more intense..."
    "The way his cock filled my pussy, the way it rubbed against the walls, it was so good... It fit so well..."
    "And his tongue was tracing wet paths around my neck, making me shiver with pleasure."
    "I found myself moving my hips to Ian's rhythm without even thinking. Faster and faster..."
    l "Mhhh, Ian, oh God..."
    "My breathing was turned into constant moaning as pleasure threatened to overtake me."
    "That was a threat I did not resist."
    play sound "sfx/oh1.mp3"
    with vpunch
    l "Oaahhhh!!"
    "I embraced him, clasping my hands around his arms, as my mind and body were washed away by an intense orgasm."
    "Ian's warmth, his smell, his touch, that was all I had awareness of during those intense but fleeting seconds."
    "They were acting like an aphrodisiac that made my climax even more intense."
    menu:
        "Keep going":
            $ renpy.block_rollback()
            "I took a few seconds to let the orgasm fade away."
            "Ian was panting on top of me, but he was not done yet. I was not done yet."
            scene v4_lena7
            if lena_piercing1:
                show v4_lena7_p1
            if lena_piercing2:
                show v4_lena7_p2
            with long
            "I pushed Ian and made him turn over without him having to pull out. His hard cock was still deep inside me..."
            l "Now's your time to enjoy yourself..."
            i "Did you have the feeling I, ahh... I  wasn't enjoying myself before?"
            l "I want you to enjoy yourself until you come."
            "I began riding him, swaying my hips slowly, letting him catch his breath."
            "I could feel his dick growing even more inside me, getting hard as a rock again."
            "That turned me on so much...!"
            l "Oh, yeah, Ian..."
            "He huffed and puffed."
            i "Damn, Lena..."
            "His voice sounded less gentle now. He was letting his excitement overpower him, his lust take over..."
            "He kissed me again, but this time his lips didn't stop at my neck. They found my boobs and sucked on my nipples."
            "That encouraged me to make my hip movements further. With each move his cock almost slid out of my pussy, only for it to be plunged deep inside it again."
            if lena_lust < 8:
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
            i "Oh, God..."
            l "Is this how you like it?"
            i "If you keep this up, I'll..."
            "Hearing him whisper that in my ear made me so excited again...!"
            l "Yes, cum. I want you to cum!"
            "Ian held my hips, guiding their motion to his liking."
            "I could feel his trembling, at the brink of orgasm..."
            with flash
            with vpunch
            i "Ahhhh...!!"
            "He let out a long groan as his whole body shook under me, his hips and manhood twitching with jolts of pressure."
            "And feeling that was just the last little push I needed to cum myself."
            play sound "sfx/oh1.mp3"
            with vpunch
            l "Ohhh, I'm cumming! I'm cumming again...!"
            i "Lena...!"
            scene v4_lena8
            with long
            "I collapsed next to Ian, in his arms, struck by a new wave of bliss."
            if v5_mike_cum:
                "Three times... I had orgasmed three times in a row, just like with Mike..."
            elif lena_mike_sex:
                "Three times... I had orgasmed three times in a row, even more than with Mike..."
            else:
                "Three times... I had orgasmed three times in a row!"
            "We both panted, tired and satisfied."
            l "That was... awesome..."
            i "It was... You have no idea how much I enjoyed it..."
            "I smiled at him and pointed at the condom, filled with his jizz."
            l "I get a slight idea..."

        "Rest":
            $ renpy.block_rollback()
            scene v4_lena8
            with long
            "I took a few seconds to let the orgasm fade away, with Ian panting on top of me."
            "When I released him he lay next to me."
            if v5_mike_cum:
                "I had had two marvelous orgasms... I had three with Mike, but I did it bareback with him, ant that was a plus..."
            elif v5_mike_bareback:
                "I had had two marvelous orgasms... Just like with Mike."
            l "That was... awesome..."
            l "You didn't finish, did you...?"
            i "No, but don't worry, it's OK. I enjoyed it a lot."
            
    "I closed my eyes, leaning on Ian's chest, his arm around me."
    l "I haven't been this relaxed in ages..."
    i "You must be tired. It's late and it's been a long day..."
    l "Yeah... I..."
    l "Good night, Ian."
    i "Good night."
    "I felt so comfortable... Like it was the first time I could really rest in months."
    "I faded into sleep with a peaceful smile on my face..."
    stop music fadeout 2.0
    show blackbg
    with long
    pause (1)
    jump master_script
    
##ALONE ##############################################################################################################################################################################################################
    
label v5lenarecordstore:
    
    if stalkfap_pro:
        scene polegym with long
        $ lena_look = 1
        "While we were drying our hair in the locker room Ivy asked about my Stalkfap."
        show lenatopless at rig
        show ivybra at lef
        with short
        v "Have your subscribers increased?"
        l "I haven't checked yet..."
        v "Did you do what I told you, at least?"
        l "Yeah, yeah, I uploaded a selfie..."
        show lenatopless at rig3
        show ivybra at lef3
        with move
        show v5_stalkfap_post
        if lena_piercing1:
            show v5_stalkfap_post_p1
        if lena_piercing2:
            show v5_stalkfap_post_p2
        with short
        l "Looks like some more people subscribed!"
        v "What did they comment?"
        "I read what my viewers had written aloud."
        l "\"{i}I can't believe your beauty Lena, you're like a dream come true!{/i}\""
        $ flena = "smile"
        l "\"{i}Mhhh so sexy baby, but why hide your boobs? You showed them in the other pic...{/i}\""
        l "\"{i}Nice pic but show boobs pls{/i}\""
        $ flena = "sad"
        l "\"{i}Why are you covering up? We're paying for uncensored content, what's the point if you censor it with your hand? I'll unsubscribe if that's the case.{/i}\""
        "There were a couple more comments, all stating that they wanted to show my boobs."
        l "Seems like they're not too pleased..."
        v "Of course they aren't! You gotta give them what they want!"
        l "I thought it was a good picture!"
        v "Well, you see most of the comments feel like complaints... One of them has already threatened to unsubscribe!"
        l "What should I do?"
        v "Just post a selfie of your boobs and be done with it! It's that simple."
        l "OK..."
        play sound "sfx/camera.mp3"
        show v5_stalkfap2b with flash
        $ lena_lena_pics.append("v5_stalkfap2b.png")
        "I took a quick selfie and posted it without even editing it."
        l "Done. Let's get going, I don't wanna be late."
    
    stop music fadeout 2.0
    scene street2night with long
    $ lena_look = 1
    $ ivy_look = 1
    $ flena = "n"
    $ ivy = "n"
    if holly_gym:
        "We got dressed, said goodbye to Holly and went to the record store. Ivy followed me."
    else:
        "We got dressed and left for the record store. Ivy followed me."
    show lena at rig
    show ivy at lef
    with short
    v "That store is in this neighborhood? I guess I shouldn't expect much, then..."
    l "It's a cool place, I like it!"
    v "Well, I already know you have weird tastes when it comes to some stuff..."
    if holly_gym:
        v "By the way, that girl, Holly, she's not too adventurous, right?"
        v "She couldn't come with us because she was expected home for dinner... So what?"
        v "How old is she? Twenty... three?"
        l "Twenty-four, I think."
        v "Maybe it's about time she stopped acting like a fourteen year old, then."
        l "Poor Holly... Let her be how she needs to be. It's true she could use some more confidence, though."
        v "She hasn't even hatched, even less learned to fly... You and I did it pretty early, huh?"
        l "That means we can be good teachers to her."
        $ fivy = "flirt"
        v "Teachers, huh? Sounds like fun..."  
        $ fivy = "n"
    
    play music "music/flirty.mp3" loop
    scene recordstore with long
    "There were more people than I expected. Most of the stools were taken, and the musicians were already starting their jam session."
    $ flena = "smile"
    show ivy at lef
    show lena at rig
    with short
    l "I like the ambience! Do you want something to drink? They sell beers and other stuff at the bar over there."
    v "Uh-huh."
    "Ivy was distracted texting with someone on her phone."
    "She followed me to get a couple of beers as the song progressed from the intro to the first verse. It was indie and jazzy."
    $ emma_look = 1
    $ femma = "n"
    show lena at rig3
    show ivy at lef3
    with move
    show emma with short
    l "A couple of beers, please."
    $ femma = "smile"
    if v2_ian_date:
        e "Oh, hi! I know you! It was Lena, right?"
        if lena_emma > 4:
            l "Yes. And you're Emma if I remember correctly."
            e "The one and only!"
        elif lena_emma > 3:
            l "Yes. And you're... Eva, if I'm not mistaken."
            e "Close enough! Emma."
        else:
            l "Yes, and you were... Rebecca?"
            e "Not even close. Emma. You seriously think I look like a Rebecca?"
            l "No, no, sorry. I can be really bad with names." 
    else:
        e "Oh, hi! You're the girl who bought a guitar a few weeks ago, right?"
        l "Yeah."
    e "Good to see you around here! Here you go, your drinks..."
    $ femma = "surprise"
    "She then saw Ivy and her eyes opened wide."
    e "Wait a minute, you're that go-go dancer from Blazer, right!"
    v "Uh? Oh, yeah, I dance there."
    $ femma = "smile"
    e "I saw you the other night! I must say I was amazed, the way you move on that pole is amazing!"
    $ ivy = "smile"
    v "Thank you. I give classes too, if you're interested."
    e "Maybe I'll think about it! Enjoy the night!"
    hide emma
    with short
    $ fivy = "n"
    show lena at rig 
    show ivy at lef
    with move
    "Ivy and I stood there, listening to the music and sipping our drinks."
    v "Say, why don't you come play here sometime?"
    $ flena = "worried"
    l "Who? Me?"
    if v3chativy2:
        v "Yeah. You told me you were writing songs again, right? You've always liked it quite a lot."
    else:
        v "You used to play the guitar and write songs. I remember you liked it quite a lot."
    l "I can't play in front of this many people... Besides, nobody would come."
    v "Yes they would."
    l "Nobody even knows I play and write!"
    v "You can let them know... I'm just saying."
    $ flena = "n"
    "We turned our attention back to the concert. At least, I did."
    "I was enjoying watching the band play, but Ivy seemed quite absorbed with her phone, still texting."
    v "Wait, I need to make a call. Be right back."
    l "Sure..."
    hide ivy with short
    "I continued to enjoy the music on my own. After a few minutes somebody poked me in the shoulder, but it wasn't Ivy."
    show lena at rig3
    with move
    $ fwade = "n"
    $ fcindy = "n"
    show cindy2
    show wade at lef3
    with short
    c "Excuse me, your name's Lena, right?"
    $ flena = "worried"
    "I turned around to face two people I didn't know. One was a tall and handsome guy, but with questionable taste in clothes and a bit of a belly."
    "The other one was a really beautiful blonde with striking green eyes."
    l "Yes... Do we know each other?"
    c "I'm a friend of Ian. He showed me your Peoplegram once and I recognized you."
    l "Oh..."
    c "I'm Cindy and this is my boyfriend Wade."
    w "Hey."
    $ flena = "n"
    l "Nice to meet you."  
    $ lena_wade_agenda = True
    $ lena_cindy_agenda = True
    "I wasn't expecting to meet Ian's friends tonight... and it wasn't something I was thrilled about. I was hoping to have an easy and relaxing night out..."
    "How much had Ian told them about me? And why was I getting weird vibes from this girl?"
    "She showed quite some interest in me. She interrogated me rather abruptly."
    c "You look really similar to your pics, so I guess they didn't really edit them that much... But I thought you'd be taller."
    l "Um, well... I guess I have long legs for my stature."
    c "Tell me a bit more about your job as a model. I'm curious."
    "She didn't seem to be giving me the option to decline her demand..."
    menu:
        "It's a job like any other":
            $ renpy.block_rollback()
            "I wasn't exactly feeling like entertaining her... Especially when I felt I was being measured."
            l "It's nothing special, really... Just a job like any other."
            c "Really? Doesn't look like it to me."
            l "It does, when you're inside that world. I should know."
            c "Oh, too bad. I expected you'd have some interesting stories to tell."
            l "Don't we all? But today I'd rather enjoy the music instead of talking about myself."
            $ fcindy = "serious"
            $ lena_cindy -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            c "Oh. OK."
            "It seems like that stung her ego. It was pretty swollen..."
                
        "What do you want to know?":
            $ renpy.block_rollback()
            l "What do you want to know?"
            c "How does one normally get in?"
            l "There are many ways... I did it through a friend who was already modeling. Basically you just need to know a photographer."
            c "But like, do they contact you or do you hire them...?"
            l "It depends. It's a word of mouth thing, usually. You start working with a friend, or a friend of a friend, then they talk about you or they see your work and they contact you."
            c "I see..."
            "She fired a couple more routine questions. Not the subject I was hoping to discuss tonight... but I tried to be polite to Ian's friend."
            
        "I'm not here to talk about work":
            $ renpy.block_rollback()
            "Well, I didn't like her rude manners, and I decided to let her know."
            l "I'd rather not talk about work on my night off, if you don't mind."
            "I said it very politely, and with a smile, of course."
            $ fcindy = "serious"
            $ lena_cindy -= 2
            play sound "sfx/frienddown.mp3"
            show friend_down
            "But she caught my meaning. Of course she did, same as I did hers."
            c "Alright... It's just it seems to be something really interesting... I imagined it'd be something you'd like to talk about."
            l "It's nothing special, really."
            
    l "Anyways, I need to go find my friend. A pleasure meeting you. Say hi to Ian on my behalf."
    w "Will do."
    c "Bye."  
    stop music fadeout 2.0
    scene street2night
    show lena at rig
    with long
    $ flena = "n"
    l "Well, that was kinda awkward."
    show ivy2 at lef with short
    "Ivy was still talking on the phone."
    v "Yeah, yeah, and then she said: \"you stole that look from me!\""
    v "Bitch, like I was interested in copying you. Everybody knows you got your first tattoo after I got one, same with the dyed hair..."
    "She finally saw me, waiting."
    v "Anyways, I'm with a friend now. I'll talk to you later."
    "She hung up the phone and came to where I was."
    v "Wanna go back and have another beer?"
    l "Nah, I'm good... I've seen enough for today, we can go."
    v "OK!"
    "I had liked the event. Next time I would come with better company, though."    
    jump master_script

    
screen book_screen_4:
    
    imagebutton idle "card4_talkinganimal.png" hover "card4_talkinganimal_hover.png" focus_mask True action SetVariable("book_card3", "talking_animal") , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "card4_sage.png" hover "card4_sage_hover.png" focus_mask True action SetVariable("book_card3", "sage")  , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "card4_antihero.png" hover "card4_antihero_hover.png" focus_mask True action SetVariable("book_card3", "anti_hero") , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
        