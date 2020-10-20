##################################################################################################################################################################################################################
###################################################### CHAPTER 1 TWO SIDES OF THE COIN ################################################################################################
##################################################################################################################################################################################################################
label chapter_one:

##WEDNESDAY #####################################################################################################################################################################################################################
    
    show blackbg
    with long
    call screen chapter_title
    
    if tutorial_menu:
        show screen ui
        $ _game_menu_screen = "phone"
        $ quick_menu = True
        
    play sound "sfx/door_home.mp3"
    scene ianhomenight
    $ fian = "n"
    with Dissolve (1.5)
    "After a short walk I climbed up the stairs and opened the door to my flat."
    show ian at lef3
    with short
    i "Hey."
    "I let my flatmate know I had arrived as I walked into the living room."
    if tutorial1:
        $ tutoria1 = False
        call screen basetutorial
label chapterone:
    if tutorial2:
        $ tutorial2 = False
        call screen tutorial2screen
    play music "music/perrys_theme.mp3"
    $ fperry = "n"
    show perry
    with short
    p "Hey, dude. W--{w=0.5}Wade's here."
    $ fwade = "smile"
    show wade at rig3
    with short
    $ ian_agenda = True
    $ ian_perry_agenda = True
    $ ian_wade_agenda = True
    w "What's up, Ian?"
    w "Perry told me to drop by and have a beer."
    if tutorial3:
        $ tutorial3 = False
        call screen tutorialagenda
label endtutorial:
    $ fian = "smile"
    i "Cool to see you, man. We don't get to see you much these days."
    $ fwade = "n"
    w "You know, I'm kinda busy with my job and all that."
    i "Sure. We all are..."
    "I looked at Perry."
    i "Well, not him."
    p "Shut up man, not that again."
    p "You're living at my p--{w=0.5}place, so don't complain."
    $ fian = "n"
    i "At your parents' place."
    p "My family's p--{w=0.5}place, yeah, so what?"
    p "I'm still providing you with a roof over your head."
    i "Well, yeah, and I'm paying for it! Just give me a beer and get off my back."
    "He threw me a can and I caught it, took a seat, cracked it open and took a sip."
    play sound "sfx/beer.mp3"
    i "Ahhh..."
    p "It's you who got on my back to b--{w=0.5}begin with."
    i "Yeah, whatever."
    i "So, Wade, how are things with Cindy?"
    w "It's going well. She's on her way, in fact."
    w "She should be at the door anytime."
    i "Oh, cool. We get to see her, too."
    "Wade, same as Perry, was an old high school friend."
    "We used to hang out a lot back then, but he devoted less time to us since he got a job... {p=1.5}and a girlfriend."
    "They had been living together for six months now, and in these six months I could count on the fingers on one hand how many times Wade had agreed to meet with us."
    "At twenty seven years of age, I guess he already was growing old..."
    "Damn, we all were."
    play sound "sfx/doorbell.mp3"
    "The doorbell rang that instant, as Wade had predicted."
    w "Here she is."
    p "Open the door for her, Ian."
    i "Man, I just sat down... Must I really do everything?"
    p "I just handed you a beer, dude."
    i "Without getting your ass off the chair."
    "I got up as I complained, since I knew it was a lost battle."
    "Perry was as stubborn as an ox, and as lazy. I wasn't convincing him to get up."
    "Wade didn't seem eager to get his ass off the chair either."
    "They really were birds of a feather."
    play sound "sfx/doorbell.mp3"
    hide perry
    hide wade
    with short
    show ian at left
    with move
    i "Coming, coming! How impatient."
    play sound "sfx/door.mp3"
    show cindy2
    with long
    i "Hey."
    c "Hi, Ian! How's it going?"
    i "Same old same old. Come on in."
    $ ian_cindy_agenda = True
    show ian at centerlef
    show cindy2 at rig
    with move 
    show perry at left
    $ fwade = "smile"
    show wade at right 
    with short
    "Cindy greeted her boyfriend with a kiss and sat next to him."
    c "Is there a beer for me?"
    $ fwade = "n"
    hide cindy2
    show cindy at rig
    with short
    menu:
        "Sure, grab one":
            $ renpy.block_rollback()
            i "Sure... Grab one."
            play sound "sfx/friendup.mp3"
            $ ian_cindy += 1
            show friend_up
            c "Thank you!"
            "She had no qualms in asking for beer or anything else. Too bad she rarely offered one herself."
            hide perry
            $ fperry = "serious"
            show perry2 at left
            with short
            p "But just one, OK?"
            $ fcindy = "serious"
            c "Don't be cheap, it's just beer!"
            p "But I b--{w=0.5}bought these."
            c "Sure, sure. I'll just have one."
            p "OK. It's just you should ask me, not Ian."
            $ fcindy = "flirt"
            c "I didn't ask him directly. He just offered it to me."
            "Perry looked at me."
            play sound "sfx/frienddown.mp3"
            $ ian_perry -= 1
            show friend_down
            p "That's true."
            i "Leave me alone, man. It's just one beer, as she said."
            "I handed a beer to Cindy and she joined us."
            $ fcindy = "n"
            hide perry2
            $ fperry = "n"
            show perry at left
            with short
            
        "You could bring your own beers sometime":
            $ renpy.block_rollback()
            $ fian = "serious"
            i "You know, you could bring your own beer sometimes."
            $ fcindy = "serious"
            play sound "sfx/frienddown.mp3"
            $ ian_cindy -= 1
            show friend_down
            c "Excuse me?"
            i "I mean, we always invite you to beers, but you never brought a six-pack with you."
            c "Really, Ian? You're going to be this cheap?"
            c "It's just a beer, for fuck's sake."
            $ fian = "sad"
            i "Hey, I'm just saying."
            "Perry handed Cindy a beer, interrupting our conversation."
            p "Here you go. But just one, OK? I b--{w=0.5}bought these ones."
            c "Who cares who bought what..."
            $ fcindy = "n"
            $ fian = "n"
            
        "Ask Perry":
            $ renpy.block_rollback()
            play sound "sfx/friendup.mp3"
            $ ian_perry += 1
            show friend_up
            i "I don't know, you need to ask Perry. He bought them."
            c "I can surely have one."
            "She had no qualms in asking for beer, or anything else for that matter."
            "Too bad she rarely offered one herself."
            p "Well, if it's j--{w=0.5}just one..."
            "Perry handed a beer to Cindy and she joined us."
            
    play sound "sfx/beer.mp3"        
    c "Cheers!"
    i "You look cheerful. Did something good happen?"
    c "Mhhh, not really. You know I'm a cheerful person!"
    "Cindy's attitude surely was a stark contrast to Wade's, who lately had been showcasing the energy level of a depressed maggot..."
    "It was like he had grown old way too quickly. I hoped I wasn't on my way to becoming like him..."
    "Though, all things considered, I wished my life was more like Wade's."
    "He had a stable job and a damn beautiful girlfriend..."
    "I looked at Cindy. She was pretty, slender, with beautiful green eyes..."
    "Any guy's dream girlfriend... If it weren't for that bitchy attitude she sometimes had."
    c "What's with that absorbed look on your face, Ian?"
    $ fian = "insecure"
    i "Uh, ah... Nothing... I was just thinking about... stuff."
    w "You're always worrying too much about stuff, dude."
    c "What are you worried about? That book you were trying to write?"
    i "Oh, that..."
    c "How's it going?"
    i "It's a long way from being finished. I'd say I barely gotten started..."
    c "So no publication date on sight?"
    i "If I'm being realistic, that probably will never happen."
    p "What about that literary contest you told me about? If you win you get your book published, right?"
    i "Yeah, but winning it would be a miracle. Besides, I need to finish the book first!"
    w "You should get real and get an actual job. We're not kids anymore..."
    c "At least he's not giving up on his dream."
    i "And I have an actual job at the magazine..."
    w "An internship."
    i "Can we change the subject? I don't want to get even more depressed."
    p "Oh, yeah, speaking about that."
    $ fian = "smile"
    $ fperry = "happy"
    p "I talked with Em--{w=0.5}Emma the other day, and she said we should go to the Fortress this Friday."
    i "It's been a while since we saw her. I'm in."
    p "What ab--{w=0.5}about you, Wade?"
    w "I don't know man, I'm beat on Fridays after having worked all week..."
    p "Oh, come on man!"
    "Unsurprisingly, Cindy made the choice for him."
    c "We'll be there."
    p "Really?"
    c "Yeah, I feel like going out. We're staying at home way too much lately."
    w "OK, sure, we can go for a while."
    p "Awesome."
    scene ianhomenight
    with long
    "We finished our beers as we continued to chat for a while, until Wade and Cindy finally decided to leave."
    stop music fadeout 2.0
    $ fperry = "meh"
    show perry2 at rig
    with short
    p "They left early."
    $ fian = "n"
    show ian at lef
    with short
    i "It's Wednesday. I think they left at a reasonable hour."
    p "Considering we barely see Wade anymore, he could've stayed longer."
    i "You've seen how he's like, now. If it weren't for Cindy, we wouldn't even be seeing him on Friday."
    p "He's a lucky bastard."
    "Perry looked at me."
    p "What about you?"
    $ fian = "sad"
    i "About me, what?"
    p "You know, girls."
    p "Have you been with someone since Gillian yet?"
    "Gillian..."
    "Hearing that name still made my guts wrench."
    i "You know I haven't..."
    p "And when are you going to change that?"
    menu:
        "Refuse to answer":
            $ renpy.block_rollback()
            $ fian = "serious"
            i "Leave me alone, dude."
            i "I don't want to talk about that."
            p "Shit, y--{w=0.5}you're still sensitive about that."
            i "Of course I am."
            p "It's been a year already, hasn't it?"
            i "I'm going to my room. Goodnight."
            
        "Tell him about the waitress":
            $ renpy.block_rollback()
            $ ian_tell_lenaperry = True
            i "Well, now that you mention it..."
            $ fian = "smile"
            i "Today I spoke with an incredibly beautiful girl."
            if ian_perry == 4:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_perry += 1
            p "Really? W--{w=0.5}where?"
            i "At that cafe I go to sometimes to write. She's a new waitress there."
            p "Asking for coffee at the counter is not speaking..."
            i "I know that, idiot. We had an actual conversation."
            if v1_name_wits or v1_name_charisma:
                i "She even gave me her name."
                $ fperry = "surprise"
                p "Really?"
                i "Yeah. Lena."
                $ fperry = "n"
                p "Seems like you had a real conversation, yeah."
                p "How did you do that?"
                i "What?"
                p "Asking her name. I always get so nervous in front of a beautiful girl."
                if v1_name_wits:
                    i "To be honest, she just gave it to me. I didn't ask her for it or anything."
                    p "No way."
                    i "I swear."
                    p "I'm sure you t--{w=0.5}tricked her somehow, using one of those mind games of yours, with your fancy words..."
                    i "I didn't trick anybody. But I guess words do have power."
                    p "You sound like a scammer."
                if v1_name_charisma:
                    i "I don't know, it just came out natural."
                    i "I introduced myself and then she gave me her name, too."
                    p "That's ballsy."
                    p "She p--{w=0.5}probably felt forced, since you gave her your name first."
                    i "Oh, come on, man. Only you could see it that way!"
                    p "So you're into forcing girls now, huh? Ha ha ha."
                i "Shut up."
            else:
                p "What's her name?"
                $ fian = "sad"
                i "I didn't ask her..."
                p "Then it wasn't a real c--{w=0.5}conversation."
                i "I guess I'll have to ask her next time, but it's not easy, you know?"
                p "I know, I know. I also get super nervous in front of a beautiful girl."
            p "So what was the conversation about?"
            i "I don't know, books and stuff..."
            p "Doesn't sound too personal."
            i "I guess not. But it's a start."
            i "I will talk to her again next time I go there, I guess."
            p "Just don't get your hopes up."
            i "Thanks for the encouragement, friend."
            i "Anyways, I'm going to my room. Goodnight."    
            
        "Deflect the question":
            $ renpy.block_rollback()
            "I didn't want to talk about that, so I deflected the question."
            $ fian = "happy"
            i "I'm more interested in hearing about what's up with you and Emma."
            p "What's up with what?"
            i "You know, you and her..."
            $ fperry = "sad"
            p "A--{w=0.5}again with that? I'm n--{w=0.5}n--{w=0.5}n--{w=0.5}not interested in her."
            "I teased him a bit."
            i "So you say, but..."
            p "I've already told you, she's just a g--{w=0.5}good friend, like she's w--{w=0.5}with you."
            i "I don't think I'm as friendly with her as you are..."
            p "Sh--{w=0.5}shut up, dude. You're always spouting nonsense."
            i "If you say so."
            i "I'm going to my room. Goodnight."    
    
    play sound "sfx/door.mp3"
    scene ianroomnight
    $ fian = "n"
    show ian
    with long
    "I took off my hoodie and threw it on the bed."
    hide ian
    show ianunder
    with short
    i "That Perry is way too nosy."
    i "..."
    i "I should do something to clear my head."
    
    menu:
        "Work on your book":
            $ renpy.block_rollback()
            "I decided to use the time to try and work on my book."
            "I sat down in front of the computer, opened the document and got ready to type."
            i "..."
            "I thought about the structure of the book. I had a lot to re-consider and figure out..."
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            i "..."
            "My fingers hovered over the keyboard, unsure of what to type."
            i "..."
            "The conversation with Wade and Cindy had left me a bit anxious."
            i "..."
            "There was such a long road ahead just to finish the book."
            "A road that would probably be for nothing."
            "How many hours invested in a project that would get zero results?"
            $ fian = "worried"
            i "Ahh, man, I can't write."
            i "I'm completely blocked."
            "I gave up and leaned back on the chair, staring at the wall."
            i "Damn."
            
        "Jerk off":
            $ renpy.block_rollback()
            "I decided jerking off was a good idea."
            "It's one of the best ways to relax, after all!"
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            scene ianroomnight
            show v1_ianfap_animation
            with long
            "I sat in front of the computer and browsed for some porn."
            "After finding a video that suited my mood, I unzipped my pants and greeted my schlong."
            i "Alright..."
            "I began getting into it as I watched the scene play out..."
            "The girl seemed to be having the time of her life while being spitroasted."
            "She was so hot and beautiful, but for some reason I just couldn't get myself into the right mood."
            "Something was off."
            "The girl in the video... She was a redhead. Same as..."
            scene ianroomnight
            $ fian = "worried"
            show ianunder
            with short
            
        "Do nothing":
            $ renpy.block_rollback()
            "I wasn't feeling like doing anything, to be honest."
            "I laid down on the bed, staring at the ceiling, letting my mind wander off."
            "I thought about the conversation at the cafe, about the review, about my book..."
            "But my mind kept coming back to the name Perry had just uttered."
            "I tried to avoid thinking about it, but my mind came back to that thought, trapped in a loop."
            $ fian = "worried"
            i "Damn."    
            "I sat up and stared at the wall."
    play music "music/lenas_theme.mp3"
    "Gillian."
    "Why did Perry have to mention her?"
    if v1_name_wits or v1_name_charisma:
        "I had been in a good mood after having that conversation with Lena, but that was gone now."
    else:
        "I had been in a good mood after having that conversation with the waitress, but that was gone now."
    "No, it was my fault, not his."
    "It has already been a year since we broke up."
    "Worst year of my life, probably."
    "I knew I shouldn't do it, but I took out my phone and searched for that picture."
    scene ianroomnight
    show v1_gillian
    with long
    $ ian_gillian_gallery = True
    $ ian_gillian_pics.append("v1_gillian.png")
    "Our last photo together."
    "Gillian..."
    "Four years we had spent together."
    "Four years next to the girl I thought was the love of my life..."
    "Four years that ended up in the trash, along with my feelings, my self-esteem and my trust."
    i "Fuck."
    scene ianroomnight
    $ fian = "depress"
    show ianunder
    with short
    "I put the phone away."
    "I was only hurting myself looking at that picture."
    "I had been hoping that wound would've stopped hurting after a whole year, but it seemed I was just being naive."
    "It still ached. It still weighed on me."
    "Way more than it should."
    stop music fadeout 2.0
    scene blackbg
    with long
    call screen calendar
    
##THURSDAY #####################################################################################################################################################################################################################

## V1 WORK ###############################################################################################  
    
    play music "music/normal_day.mp3" loop
    show magazine
    with long
    "Next morning I went to the office."
    $ fian = "n"
    show ian
    with short
    "I had submitted the review first thing in the morning and now I was taking care of some unimportant tasks."
    i "What a waste of time..."
    "Just before my shift ended, Minerva came out of her office and asked for our attention."
    show ian at lef3
    with move
    show minerva
    with short
    $ ian_minerva_agenda = True
    mi "The ones who submitted the book reviews this morning, please come here and pay attention."
    "Me and the other interns gathered around the boss."
    $ fminerva = "smile"
    show holly2 at rig3
    with short
    h "You called?"
    mi "Oh, yes Holly. Come here, dear."
    mi "So I took a look at the reviews during morning..."
    mi "Let's see..."
    $ fminerva = "mad"
    mi "Who was assigned to review \"Fangs on my neck\"?"
    mi "Oh, yeah, Ian. Of course."
    $ fholly = "serious"
    "I looked at her and held in a sigh."
    "I knew what was coming."
    menu:
        "So what's the problem this time?":
            $ renpy.block_rollback()
            "I decided to face it head on."
            $ fian = "serious"
            i "So what's the problem this time?"
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            "Minerva gave me a stern and disgusted look."
            play sound "sfx/frienddown.mp3"
            $ ian_minerva -= 1
            show friend_down
            mi "So you are well aware there is a problem."
            i "I know there's always one..."
            mi "Then you should try to do a better job and take these reviews more seriously."
            
        "Did I do something wrong?":
            $ renpy.block_rollback()
            i "Did I do something wrong?"
            mi "Something wrong? I don't know, what do you think?"
        
        "Stay silent":
            $ renpy.block_rollback()
            $ fian = "depress"
            "I decided to stay silent."
            "No point in arguing with the boss... Even if I knew she was wrong."    
    
    "She took a paper and read an excerpt from my review."
    mi "\"McDollinger's straightforward and uncomplicated style doesn't detract from the enjoyment one can get from this light-hearted story...\"."
    mi "Do you think that's OK?"
    i "I mean, it's my opinion and I don't think I'm saying anything that's not true."
    mi "Well, you're just an intern, nobody's concerned about your opinion."
    mi "You need to write an analysis, not an opinion."
    i "Well, that's my analysis!"
    "Minerva scoffed as she looked at me and then back at the paper."
    mi "\"McDollingers elegant and swift prose gives the reader a story bursting with passion that he will get hooked on\"."
    mi "How about that way of phrasing it?"
    mi "I came up with that in three seconds. It is not that hard."
    menu:
        
        "That sounds better, yeah":
            $ renpy.block_rollback()
            $ fian = "depress"
            i "Sure... That sounds better, yeah."
            $ fminerva = "n"
            play sound "sfx/friendup.mp3"
            $ ian_minerva += 1
            show friend_up
            mi "Alright."
            mi "Keep in mind what I told you and fix the review for tomorrow, OK?"
            i "Will do."
            "It was so frustrating sucking up to her..."
            "But at least she seemed pleased when I did that."
        
        "That's just sugar-coating it":
            $ renpy.block_rollback()
            $ fian = "serious"
            i "That's just sugar-coating it."
            i "That way of phrasing it paints the truth of the facts with a misleading color."
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            i "Her prose is basic and the romance is quite bland, to be honest."
            "Minerva scoffed again. She was clearly not pleased with me."
            "Not at all."
            play sound "sfx/frienddown.mp3"
            $ ian_minerva -= 1
            show friend_down
            mi "This is not how we do things in this magazine."
            mi "Learn that at once. You're behind already."
            mi "I want a presentable review ready for tomorrow."
            i "Sure."
            
        "Stay silent":
            $ renpy.block_rollback()
            i "..."
            "What she was saying was bullshit, but it wasn't wise calling her on it."
            "She was the boss after all. And she loved to be right."
            "Best to just keep quiet and take it."
            mi "I hope I've made myself clear, though you're not giving me too many signs that you got it."
            i "I've got it."
            mi "I hope so. I want this review fixed by tomorrow. got it?"
            i "Got that too."
            mi "Good."
    mi "Let's see this one..."
    $ fminerva = "n"
    mi "Oh, yes, Holly."
    mi "Great job, as always."
    $ fholly = "blush"
    mi "I have nothing to say about your review, it's the best of the bunch."
    h "Oh... Thank you..."
    mi "It's a pleasure to have you working with us."
    mi "Anyway, that's all I had to discuss."
    $ fholly = "n"
    mi "The ones that don't have another review assigned will get one soon."
    mi "Other than that, keep working."
    pause 0.5
    $ fminerva = "mad"
    mi "Oh, and be sure you don't forget about your review, Ian."
    mi "Chop chop."
    hide minerva
    $ fian = "serious"
    with long
    "She turned around and left."
    i "For fuck's sake..."
    "She was a total bitch."
    hide holly2
    $ fholly = "blush"
    show holly3 at rig3
    with short
    h "..."
    show holly3 at rig
    with move
    h "Um..."
    "I just noticed Holly had stayed after the other interns had been dismissed."
    $ fian = "n"
    $ ian_holly_agenda = True
    i "Yes?"
    h "She's... She's quite tough with you, isn't she...?"
    i "I've been thinking she might have something personal against me, to be honest!"
    i "I think she disliked me from the day I set foot in this office."
    hide holly3
    show holly2 at rig
    with short
    h "If it's any consolation, I think what you wrote is true."
    h "McDollinger isn't too great when it comes to writing..."
    i "Ah, finally! Someone's on my page!"
    h "I'm sure Minerva thinks so too. But she just wants you to write the review in a praising way."
    i "I try! But some things are just lies, and I feel stupid writing them."
    h "Well, I think it's pretty cool that you write what you really think..."
    i "Even if I get into trouble every time?"
    $ fholly = "smile"
    h "You stand for your ideas. That's very noble."
    $ fian = "smile"
    i "Well, thank you."
    $ fholly = "shy"
    h "Oh, it's... It's nothing."
    i "I wished the boss would like me half as much as she likes you."
    i "Her demeanor changes completely when she addresses you!"
    $ fholly = "n"
    h "Um, well... I guess she likes having an up-and-coming writer at the office."
    i "I'd say you're more than just an up-and-coming writer at this point."
    h "I wouldn't say that..."
    i "Oh, come on. You have published two books already, and people are going crazy waiting for the third one."
    i "You're killing it."
    hide holly2
    show holly3 at rig
    with short
    h "I guess I've been lucky..."
    i "You're just a great writer, that's all. I'm jealous."
    h "Thanks..."
    $ fholly = "blush"
    h "..."
    h "Say, would you like me to help you with rewriting the review?"
    h "It shouldn't take too much effort."
    i "You'd do that?"
    h "Yeah! Right now I have an appointment with my publisher, but..."
    h "I could help you during lunch break tomorrow."
    $ fian = "happy"
    i "Sure, that sounds great! Thanks Holly!"
    $ fholly = "shy"
    h "It's nothing..."
    i "Well then, I'm off too. See you tomorrow."
    h "Bye!"
    stop music fadeout 2.0
    scene street
    $ fian = "n"
    show ian
    with long
    "I grabbed my bag and left the office."
    "I felt I was wasting my time there, but I had to finish my internship."
    "And that was my only source of income, other than what my parents sent me each month..."
    "At twenty-seven years of age I still had to depend on my parents to get by..."
    "How fucking pathetic."
    "On the other hand there was Holly. She was only twenty-four, but was already having a very successful career writing books."
    "She won the last edition of that literary contest I was aiming for and got her book published, and it was a big hit."
    "She managed to get quite a big following, her second book was also very successful and she was about to publish the third one... All in just one year."
    "The way I saw it, she should be as happy as a person could be, living the dream..."
    "But instead she looked rather timid and insecure..."
    
## V1 GYM ###############################################################################################  

    scene gym
    with long
    play music "music/jeremys_theme.mp3" loop
    "I arrived at the gym for Thursday's training session."
    $ ian_look = 7
    show ian at lef
    with short
    "I got changed and stepped onto the mat."
    $ jeremy_look = 2
    $ fjeremy = "smile"
    show jeremy at rig
    with short
    j "My man! Here you are!"
    i "Hey, Jeremy."
    $ ian_jeremy_agenda = True
    j "What's with the long face?"
    i "Tough day at the office."
    j "That bitch of a boss you have is still giving you trouble?"
    i "Yup."
    j "Well, you can take it out on me! Let's do some sparring!"
    show headgear at lef
    with short
    "I put on my headgear and adjusted my gloves."
    $ fjeremy = "happy"
    j "Are you still worried about your pretty face getting banged up?"
    i "Unlike you, I need my head in good condition to work."
    i "Besides, you're way better at this than I am."
    j "You're getting better... Sort of."
    j "Let's go!"
    scene gym
    show v1_kickboxing1
    with short
    "Jeremy and I used to be friends when we were kids at school."
    "We used to take karate lessons together when we were like twelve years old, and we liked to play and hang out together."
    "We lost touch for a bit when we got into college, but I found out he was training at this gym and decided to sign up half a year ago."
    "Seems like he had continued training martial arts, unlike me, and now he always kicked my ass when we practiced."
    j "Guard up!"
    "We started circling each other, throwing techniques lightly."
    "I tried to reach him with my punches, but it was as useless as ever."
    i "You're much taller than me, I can't reach you!"
    j "Then find a way!"
    play sound "sfx/punchgym.mp3"
    scene gym
    show v1_kickboxing2
    with vpunch
    i "Ugh!"
    "Jeremy effortlessly landed a straight right that knocked my head back."
    scene gym
    show v1_kickboxing1
    with short
    i "That's not fair, your arms are twice as long as mine!"
    "Jeremy smiled as he danced around me."
    j "I'm like a sniper!"
    i "You have gorilla arms, dude."
    play sound "sfx/punchgym.mp3"
    scene gym
    show v1_kickboxing2
    with vpunch
    i "Umf!"
    j "Don't be a pussy and stop complaining!"
    j "Guard up, head movement!"
    scene gym
    show v1_kickboxing1
    with short
    i "Fuck..."
    "We sparred for a bit, but Jeremy picked me apart with punches as he pleased, while I struggled to even reach him, and failed."
    "Rather than help me blow off some steam, it was making me more frustrated..."
    scene gym
    $ fian = "serious"
    show ian at lef
    show headgear at lef
    $ fjeremy = "smile"
    show jeremy at rig
    with short
    i "Man, my head feels like a piñata..."
    j "Come on Ian, don't give up."
    i "You just want a punching bag that moves and fires back."
    $ fjeremy = "happy"
    j "It's way more fun than punching the heavy bag, ha ha!"
    menu:
        "I'm done for today":
            $ renpy.block_rollback()
            hide headgear
            with short
            $ fian = "sad"
            with short
            i "Nah, man... I'm done for today."
            $ fjeremy = "n"
            j "That's too bad."
            i "I've had my ass handed to me plenty already."
            j "That's not the spirit!"
            i "Then maybe try going easy on me!"
            $ fjeremy = "smile"
            j "But where's the fun in that?"
            i "You're such a prick sometimes."
            "Jeremy patted me on the shoulder."
            j "Come on, let's hit the showers."
            jump v1endtraining
            
        "Let's go again!":
            $ renpy.block_rollback()
            "I didn't want to let him get away with it."
            "If I could only punch him back once...!"
            i "Alright, let's go again!"
            j "That's the spirit!"
            jump wen_training
            
label wen_training:
    
    $ ian_lowkick = True
    show ian at lef3
    show headgear at lef3
    show jeremy at rig3
    with move
    $ fian = "n"
    $ fjeremy = "n"
    show wen
    with short
    wen "You won't be able to lay a hand on him like that."
    i "Huh?"
    j "Hey, Wen."
    $ ian_wen_agenda = True
    "I had never spoken with Wen, but I had seen him almost every time I came to the gym."
    i "You were watching us?"
    wen "Yeah. He has a very big reach advantage over you. Besides, his boxing skills are way better."
    i "I'm well aware of that."
    wen "Doing the same will get you the same results."
    i "What should I do, then?"
    $ fjeremy = "smile"
    j "Are you gonna coach him against me? Come on Wen, we're pals, ha ha."
    wen "He needs it."
    "The short Asian dude looked at me."
    wen "Use your head!"
    if ian_wits > 0:
        i "I can't reach him with my punches, so I need to find another way."
        wen "Exactly. Get into position."
    else:
        i "I have to headbutt him?"
        j "Ha ha ha! You're such a moron sometimes."
        wen "That would be pretty satisfying, but I doubt you'll be able to reach him, ha ha."
        wen "Get into position and listen."
    scene gym
    show v1_kickboxing1
    with short
    "I got into my guard in front of Jeremy once again."
    wen "If you can't reach his body with your arms, go for his legs."
    wen "Use low kicks!"
    play sound "sfx/punchgym.mp3"
    scene gym
    show v1_kickboxing3
    with short
    "I did as Wen told me, moved around and landed a leg kick on Jeremy."
    play sound "sfx/xp.mp3"
    show athletics_up
    $ ian_athletics_xp += 1
    call screen skillsup
    scene gym
    show v1_kickboxing1
    with short
    j "I guess that works."
    wen "OK, now put more hips into it!"
    wen "Move, feint up top, and when you kick pivot on your foot, twist your hips and drive your body weight behind the kick."
    wen "And try landing with your shin!"
    play sound "sfx/punch.mp3"
    scene gym
    show v1_kickboxing4
    with vpunch
    j "Ouch!"
    i "That felt good!"
    j "That stung."
    scene gym
    show v1_kickboxing1
    with short
    wen "Good kick!"
    play sound "sfx/punch.mp3"
    scene gym
    show v1_kickboxing2
    with vpunch
    i "Oof!"
    "The joy was short lived, since Jeremy wobbled my head back with another punch."
    j "I'm not gonna let you tee off on me."
    scene gym
    show v1_kickboxing1
    with short
    "I looked at Wen."
    i "He still has more reach with his arms than I have with my legs!"
    play sound "sfx/punchgym.mp3"
    scene gym
    show v1_kickboxing2
    with vpunch
    i "Ouch!"
    scene gym
    show v1_kickboxing1
    with short
    wen "Step in when he throws his punch and move your head off the center-line!"
    "I tried what he was telling me."
    play sound "sfx/punch.mp3"
    scene gym
    show v1_kickboxing5
    with vpunch
    "I moved my head to the left as I kicked, swaying out of the way of Jeremy's punch, and landed a kick with all my body weight behind it!"
    j "Oh, shit! That one did hurt!"
    scene gym
    show v1_kickboxing1
    with short
    j "I'm gonna have to get serious!"
    play sound "sfx/punch.mp3"
    scene gym
    show v1_kickboxing2
    with vpunch
    i "Agh!"
    "After that, Jeremy timed my attempts at kicking him, avoiding them and punching me in return."
    scene gym
    $ fian = "worried"
    show ian at lef3
    show headgear at lef3
    $ fjeremy = "smile"
    show jeremy at rig3
    show wen
    with short
    i "OK, that's enough... I'm starting to feel dizzy after getting punched so much."
    wen "Good thing you're wearing headgear, ha ha."
    i "Thanks for the advice, Wen, but in the end he's just much better than I am."
    j "I've been training hard, baby!"
    wen "You're always going to have it tough striking against a guy like him."
    hide wen
    show wensmile
    "He looked at Jeremy and smiled."
    wen "There are always other ways to face him, though."
    menu:
        "I've had enough for today":
            $ renpy.block_rollback()
            hide headgear
            with short
            $ fian = "n"
            with short
            i "I've had enough training for today... I'm beat."
            "Jeremy fist bumped me."
            j "It was a good sparring session, thanks dude."
            i "Thanks for the coaching, Wen."
            wen "Anytime."
            j "Come on, let's hit the showers."
                    
        "What other ways?":
            $ renpy.block_rollback()
            $ fian = "n"
            i "Other ways to face him? What other ways?"
            wen "Well, striking is not the only aspect of martial arts."
            wen "You could use grappling."
            hide jeremysmile
            show jeremy at rig3
            j "Grappling's pretty lame, dude."
            menu:
                "Yeah, not interested":
                    $ renpy.block_rollback()
                    i "Yeah, striking is the fun part."
                    wen "Jiu Jitsu can be very fun, too."
                    wen "Though I can see the appeal of putting someone to sleep with a punch, ha ha."
                    hide headgear
                    with short
                    i "Well, I've had enough training for today... I'm beat."
                    "Jeremy fist bumped me."
                    j "It was a good sparring session, thanks dude."
                    i "Thanks for the coaching, Wen."
                    wen "Anytime."
                    j "Come on, let's hit the showers."
                            
                "Teach me some grappling!":
                    $ renpy.block_rollback()
                    $ ian_grappling = True
                    i "Sure, teach me some grappling!"
                    i "If Jeremy doesn't like it, I'm sure it's pretty good."
                    wen "Cool, let me show you."
                    hide ian
                    hide headgear
                    with short
                    show wensmile at lef3
                    with move
                    "Wen stepped onto the mat and got in front of Jeremy."
                    wen "Try punching me."
                    j "Oh, man..."
                    wen "It's something like this..."
                    play sound "sfx/punchgym.mp3"
                    scene gym
                    show v1_grappling1
                    with short
                    wen "When he tries to punch me I time it..."
                    wen "Deflect it..."
                    show v1_grappling2
                    with vpunch
                    wen "And close the distance!"
                    "Wen stepped into Jeremy's reach quickly, wrapping his arms around his neck in a tight grip."
                    wen "That way I'm nullifying his reach and his most powerful weapons."
                    wen "He can't punch or kick me from this position..."
                    "Jeremy struggled to get free, but Wen was holding him in place."
                    "He squeezed his grip even more, making Jeremy's face wince with pain and discomfort."
                    wen "And if I squeeze hard enough he will end up surrendering, ha ha!"
                    "It seemed like Jeremy was stuck in that position and there was not much he could do."
                    j "OK, OK, let go of me..."
                    scene gym
                    $ fian = "smile"
                    show ian at lef3
                    $ fjeremy = "n"
                    show jeremy at rig3
                    show wensmile
                    with short
                    wen "So that's one way of doing it."
                    j "That's lame, dude. It was just hugging."
                    i "I guess you just hugged him really tightly."
                    wen "Well, at least you won't get your face busted from punching range."
                    j "The best defense is a good offense."
                    wen "Techniques are just tools. The more you know, the better."
                    wen "Do as you will with that knowledge."
                    play sound "sfx/xp.mp3"
                    show athletics_up
                    $ ian_athletics_xp += 1
                    i "Thanks for the lesson."
                    if chapter == 2:
                        jump v2endtraining 
                    else:
                        wen "Anytime."
                    j "Come on Ian, let's hit the showers."
   
    jump v1endtraining
                            
## V1 JEREMY and ALISON ###############################################################################################  
 
label v1endtraining:
    stop music fadeout 2.0
    scene streetnight
    with long
    $ fian = "smile"
    $ ian_look = 1
    $ fjeremy = "smile"
    $ jeremy_look = 1
    show ian at lef
    show jeremy at rig
    with short
    i "I think you punched me too much today."
    if ian_lowkick:
        j "Well, you nailed me with a couple of good leg kicks, too!"
        i "It was about time you felt some pain, too!"
        j "No pain no gain, baby."
        if ian_grappling:
            j "Though I wouldn't lose my time with that Jiu Jitsu stuff, if I were you."
            j "Wen really likes it, but I think that shit's gay as fuck."
    else:
        j "Come on, I went easy on you."
        j "Those were not punches, just light taps!"
    i "Oh, by the way..."
    i "Tomorrow the gang is meeting at the Fortress for some beers. Wanna join?"
    j "It's been a while since I saw Wade and Perry, but you know I can't."
    j "I work Friday nights."
    i "That's true. How's the bartender job going?"
    $ fjeremy = "happy"
    j "It's fucking awesome."
    "Jeremy had started working as a barman at a nightclub called Blazer."
    "From what I had heard, it was the hot spot for clubbing in town."
    i "I never imagined you'd end up enjoying something like that. Though it actually suits you."
    "Jeremy had changed a lot over the years."
    "When we were kids, he used to be as nerdy as Perry, Wade and I were."
    "At some point he had decided to do a full one-eighty on that, though."
    j "What's not to love?"
    i "Well, working on weekends, the loud music, serving drunkards all night..."
    j "You have no idea of the amount of hot chicks that go to that club!"
    j "And they all have to talk to the bartender, so... It's super easy to get numbers!"
    i "Seems like you're making the most of it."
    j "Dude, you have no idea. I've only been working there for a couple of weeks, but check this out..."
    show ian at left
    show jeremy at right
    with move
    show v1_selfiejeremy
    with short
    $ fian = "surprise"
    "Jeremy pulled out his phone and showed me a picture."
    "It was a naked selfie of a girl who had just taken a shower..."
    "And she had the most perfect body I had ever seen!"
    i "Wow, who's that? You know her?"
    j "Yeah, dude. She's one of the go-go dancers that work at the club."
    i "She sent you this?"
    j "She sure did!"
    menu:
        "She's so fucking hot!":
            $ renpy.block_rollback()
            $ fian = "shy"
            i "Dude, she's so fucking hot!"
            j "I know, right?"
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            j"You should see the outfits in which she dances at the club."
            j "Gets me so hard I knock the glasses off the counter with my erection while I'm working!"
            $ fian = "disgusted"
            i "Thanks for that mental image..."
            $ fian = "smile"
            i "How did you manage to get her to send you that?"
            j "We were texting and she just did it, I didn't ask her to."
            $ fian = "n"
            i "Jeez... You really have it easy."
            hide v1_selfiejeremy
            with short
            show ian at lef
            show jeremy at rig
            with move
            
        "Lucky bastard":
            $ renpy.block_rollback()
            $ fian = "serious"
            i "You lucky bastard..."
            i "How did you manage to get her to send you that?"
            j "We were texting and she just did it, I didn't ask her to."
            $ fian = "n"
            i "Jeez... You really have it easy."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_jeremy += 1
            hide v1_selfiejeremy
            with short
            show ian at lef
            show jeremy at rig
            with move
            
        "No need for me to see this":
            $ renpy.block_rollback()
            $ fian = "sad"
            hide v1_selfiejeremy
            with short
            show ian at lef
            show jeremy at rig
            with move
            $ fian = "sad"
            i "Then there's no need for me to see this. She sent it to you, not me."
            j "So?"
            i "She wasn't intending for me to see it."
            j "Dude, you think she cares? You should see the outfits in which she dances at the club."
            j "Gets me so hard I knock the glasses off the counter with my erection while I'm working!"
            $ fian = "disgusted"
            i "Thanks for that mental image..."
            $ fian = "n"
            
    i "So, have you slept with her?"
    j "No, I haven't fucked her yet. But things look quite promising!"
    j "I think she's into me."
    i "I'd say so, considering the picture she sent you..."
    j "I have my hopes high! She's the hottest girl I've ever met."
    j "If I fail to hit that I will cut my dick off!"
    i "Well, good luck with that."
    $ fjeremy = "smile"
    j "What about you, man? Any chicks in your sights?"
    $ fian = "sad"
    j "Ready to pull the trigger on someone?"
    "First Perry and now Jeremy. Why was everybody asking me that lately?"
    i "Nah, not really..."
    i "Though yesterday I met a really cute girl."
    j "Really? Where?"
    if v1_name_wits or v1_name_charisma:
        $ fian = "smile"
        "I told him about my meeting with Lena at the cafe."
        "I guess I felt compelled to do so after Jeremy had bragged about his success with women..."
        j "Sounds cool, man."
        if v1_name_wits:
            j "So she gave you her name first without you asking her for it?"
            j "That's a good sign, I'd say she's interested."
        if v1_name_charisma:
            j "Good move introducing yourself like that."
            j "Chicks love a confident approach."
        i "I can't tell if that's the case indeed, but one can hope."
        j "Be optimistic, dude!"
    else:
        $ fian = "n"
        "I told him about my meeting with the waitress at the cafe."
        "I guess I felt compelled to do so after Jeremy had bragged about his success with women..."
        j "So you didn't get her name? That's a shame."
        j "You should've closed strong."
        i "I know, it was my mistake. I just didn't know how to bring it up."
        j "Just ask her, or introduce yourself. Plain and simple."
        j "You need to be more confident, man."
    j "You have any picture of her?"
    i "No, I don't."
    j "Pity, I would've liked to see if she's as pretty as you said."
    play sound "sfx/ring.mp3"
    "Then my cell phone rang. I was getting an unexpected call."
    i "Wait up."
    j "Sure."
    hide ian
    $ fian = "smile"
    show ian_phone at lef
    with short
    i "Yes?"
    show phone_alison at left
    with short
    a "Hi, Ian!"
    i "Hey, Alison! What's up?"
    $ ian_alison_agenda = True
    a "I was just thinking about you. It's been more than a month since we last saw each other!"
    i "Oh, yeah, I guess that's true."
    a "I know I've been very busy with my new work and all that, but it's about time you and me caught up!"
    i "Sure, that would be cool."
    i "In fact, I'm with Jeremy right now and I was telling him..."
    j "Hi, Alison!"
    i "He says hi. So, I was telling him that me and the guys are going out for beers tomorrow night."
    i "Do you wanna come?"
    a "I have to get up early on Saturday... I was thinking more like having lunch tomorrow."
    $ fian = "n"
    i "You can't come at night?"
    a "I can, but I'll have to leave quite early. If we meet for lunch we will have more time."
    $ fian = "sad"
    "Holly had offered to help me tomorrow during lunch..."
    "But I hadn't seen Alison in quite some time."
    $ fjeremy = "evil"
    "Jeremy hit me with his elbow and whispered with a sly smile."
    j "Dude, say yes."
    j "You, Alison and her two big knockers all alone on a lunch date!"
    "He made a gesture with his hands, like he was playing with a pair of invisible giant boobs."
    i "Shut up."
    a "What?"
    i "Oh, nothing."
    menu:
        a "So, what's it gonna be?"
        
        "Meet Alison for lunch":
            $ renpy.block_rollback()            
            $ v1_alisonlunch = True
            $ fian = "smile"
            $ fjeremy = "happy"
            i "Alright, let's meet tomorrow for lunch."
            a "Great!"
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_alison += 1
            a "I'll meet you at your office, so we can eat somewhere in the area."
            a "See you tomorrow! Kisses!"
            hide phone_alison
            hide ian_phone
            show ian at lef
            with short
            j "Kisses, huh?"
            i "Stop meddling."
            j "Dude, sometimes you just need help. You're so clueless."
            i "Clueless?"
            j "Will you please just go and give Alison the D?"
            i "Alison and I are just friends, and have been for a ton of years."
            i "She doesn't want my \"D\", and I'm not planning on giving it to her."            
            
        "Meet her at night with the others":
            $ renpy.block_rollback()
            $ fian = "n"
            $ fjeremy = "n"
            i "I already have plans for tomorrow during lunchtime."
            i "It's better if you come join us at night."
            a "Oh, alright."
            a "I'll drop by and say hello, then."
            i "See you tomorrow, then!"
            a "Bye!"
            hide phone_alison
            hide ian_phone
            show ian at lef
            with short
            j "Dude, you passed up a good opportunity."
            i "Alison and I are just friends, and have been for a ton of years."
            i "There's no opportunity to gain or lose here."
            $ fjeremy = "happy"
            
    j "Whatever, dude... Alison's pretty hot."
    j "I wouldn't mind sticking my cock between those juicy tits and..."
    i "Dude, enough. Just shut up."
    i "Anyways, see you next time at the gym."
    j "Sure. Say hello to the gang for me."
    i "I will."
    j "I'll try to meet with you guys next time."
    j "See ya!"
    $ day = "Friday"
    scene blackbg
    with long
    call screen calendar

##FRIDAY #####################################################################################################################################################################################################################
      
    if v1_name_wits or v1_name_charisma:
        $ v1_name = True
    $ holly_change = 0
        
    scene magazine
    $ fian = "n"
    show ian
    with long
    "I spent the next morning doing chores at the office."
    "Sending e-mails, arranging events, reviewing applications for advertisements..."
    "The only remotely creative stuff I got to do for the magazine was writing book reviews."
    "And that sucked, too."
    i "*{i}Sigh...{/i}*"
    i "Working here was as exciting as watching paint dry."
    show ian at lef
    with move
    $ fholly = "n"
    show holly3 at rig
    with short
    h "Hi, Ian."
    i "Oh, hey Holly."
    h "Should we... go grab some lunch so I can help you with your review?"
    if v1_alisonlunch:
        $ fian = "sad"
        i "About that..."
        i "Sorry, a friend of mine called yesterday and asked me to have lunch with her."
        $ fholly = "sad"
        i "I haven't seen her in a long time, so..."
        hide holly3
        show holly2 at rig
        with short
        h "Oh... Oh yeah, of course."
        i "I'm sorry, especially since you offered to help me..."
        h "No, it's OK! I understand."
        i "Maybe another time?"
        h "Well, Minerva wanted your review before the end of today, didn't she?"
        i "Yeah... Well, then you can help me with the next one."
        i "I'm bound to write something she hates again, so..."
        h "Sure. Next time, then."
        play sound "sfx/frienddown.mp3"
        show friend_down
        $ ian_holly -=1
        i "Sorry, I should've told you before about the change of plans. But I don't have your number!"
        $ fholly = "blush"
        h "Oh, right. Should I... give it to you?"
        i "Sure."
        "We exchanged numbers."
        i "This way we'll make sure this doesn't happen again."
        h "Yeah."
        i "Well, gotta go. See you on Monday, Holly."
        h "Have fun."
        jump v1alison
        
    else:
        $ fian = "smile"
        i "Of course. Let me just finish sending a couple of e-mails..."
        i "OK, let's go."
        play sound "sfx/friendup.mp3"
        show friend_up
        $ ian_holly +=1
        $ fholly = "happy"
        h "Alright."
        jump v1holly
    
## V1 ALISON LUNCH ############################################################################################### 

label v1alison:
    
    scene street
    $ fian = "smile"
    show ian at lef
    with long
    "I went down to the street and looked for Alison."
    "She said she would come to meet me near the magazine..."
    $ falison = "smile"
    show alison at rig
    with short
    a "Ian!"
    i "Hey, Alison."
    a "It's about time we saw each other!"
    i "Well, it's you who has been missing lately!"
    a "I know, I  know. My life's a mess!"
    a "Let's go eat some lunch. Do you know a place around here?"
    i "Well... I do, yeah."
    i "This way."
    play music "music/flirty.mp3" loop
    scene cafe
    show ian
    $ falison = "n"
    show alison at lef3
    with long
    "The first place that came to my mind was that cafe."
    "It was very close and I liked the spot. Besides..."
    "I had been wanting to come back since Wednesday."
    a "Oh, this place's pretty cozy. I didn't know you had such good taste."
    i "Obviously I do."
    $ falison = "smile"
    a "That hoodie you're wearing says otherwise, ha ha!"
    $ fian = "sad"
    i "What's wrong with it?"
    show lenawork at rig3
    $ flena = "n"
    $ falison = "n"
    with short
    if v1_name_wits or v1_name_charisma:
        l "Welcome."
        $ flena = "smile"
        l "Hi Ian."
        $ fian = "happy"
        i "Hello again."
        "The fact that she remembered my name put a smile on my face."
        l "Having lunch today?"
        i "Yeah."
        "She looked at Alison."
        $ flena = "n"
        l "Alright, take a seat over here."
        l "I'll be right back with the menu."
        hide lenawork
        with short
        a "Who's this girl? She's really beautiful!"
        i "I just met her the other day. I came here to write and ended up chatting with her."
        $ falison = "flirt"
        a "Ohh, so that's why you wanted to come here?"
        $ fian = "insecure"
        i "No, that's not it... I like this place."
        i "I just talked with her once."
        a "Enough to know her name..."
        show lenawork at rig3
        $ fian = "n"
        $ falison = "n"
        with short
        l "Here's the menu. I'd recommend our eggs Benedict, they're delicious!"
        a "Thanks."
        "Alison and I ordered our lunch and Lena brought it for us."
        "I wanted to talk with Lena again, but being with Alison, it didn't feel right."
        "We barely knew each other, after all, and she was focused on doing her job right now."
        "It felt wrong to disturb her..."
        "I should get back alone some other day."
        hide lenawork
        with short
        show ian at lef
        show alison at rig
        with move
        $ fian = "smile"
        "In any case, I was there to talk to Alison."
        "I decided to concentrate on her."
        
    else:
        wai "Welcome..."
        $ flena = "smile"
        $ fian = "smile"
        wai "Oh, hello again."
        i "Hey... We've come for some lunch."
        $ flena = "n"
        wai "Sure. Take a seat over here."
        wai "I'll be right back with the menu."
        $ fian = "n"
        i "Thanks..."
        hide lenawork
        with short
        a "She's pretty cute... Do you know her?"
        i "No, not really."
        i "We just made some small talk the other day, that's all."
        show lenawork at rig3
        with short
        wai "Here's the menu."
        a "Thanks."
        "Alison and I ordered our lunch and the waitress brought it for us."
        "I felt awkward... The conversation we had the other day had been pretty nice, and I had wanted to ask her name..."
        "Instead, I was treating her like she was nothing more than a waitress."
        hide lenawork
        with short
        show ian at lef
        show alison at rig
        with move
        $ fian = "smile"
        "In any case, I was there to talk to Alison, not the waitress."
        "I decided to concentrate on her."
    a "So, what's up with you?"
    i "With me? I should be the one asking you that."
    $ fian = "sad"
    i "I haven't heard much of you since all that happened..."
    $ falison = "sad"
    a "Yeah, I've been hitting a rough patch lately..."
    i "How's the new job going?"
    a "Honestly? It sucks pretty bad."
    a "I'm overqualified for the position, but can you imagine I can't find anything better?"
    i "The economy in this city is pretty screwed... We're all struggling to find a decent job."
    a "Can you believe I had all my life set up?"
    a "Gone through college, got my master's degree, top of the class... I did little else other than studying during those years."
    i "You always took your studies very seriously. That's why you landed a great job right after finishing them."
    $ falison = "serious"
    a "Yeah, great... It was a big company, and I devoted many hours to it."
    a "And then it turns out the CEO is a crooked imbecile!"
    a "If you're going to commit fiscal fraud and embezzle money, at least be smart and don't get caught!"
    i "Yeah, that sucked... The company went bankrupt and you lost your job."
    a "If only! They owe me a lot of money, too!"
    a "And just while all that happens, my boyfriend decides to break up with me."
    $ falison = "n"
    a "I'm just the luckiest woman in the world, ain't I? Ha ha."
    $ fian = "smile"
    i "At least you can laugh about it."
    a "The only other thing I could do is cry, and I don't feel like it to be honest."
    menu:
        "You're a very tough girl":
            $ renpy.block_rollback()
            i "You're a really tough girl, Alison."
            i "I admire you."
            a "You do? Ha ha."
            a "Well, I have no other option pretty much, so I'm only doing the only thing I can do."
            i "You could do nothing."
            a "Like Perry? No thanks!"
            i "Hey, don't be cruel."
            a "In any case, I'm not giving up, that's for sure."
            i "Glad to hear."
            $ fian = "n"
            i "I could use some of that strength."
            a "How come?"
            
        "{image=icon_charisma.png}You have everything that's needed to succeed" if ian_charisma > 0:
            $ renpy.block_rollback()
            $ v1_encourage_alison = True
            i "Man, I hate to see these things happening to you."
            i "You were set up for success... And still are."
            a "I am?"
            i "Of course, you have everything that's needed to succeed!"
            $ falison = "surprise"
            a "Me? How come?"
            i "You're the smartest person I know, you have a great education and any business would love to have you."
            i "You're still young, you're fun, tough, full of energy and very attractive."
            i "In summary, you have everything you need to win at life."
            $ falison = "flirt"
            a "So I'm very attractive?"
            i "Come on, like you don't know that already."
            $ falison = "n"
            a "Ha ha, I don't know about that. If I were as wonderful as you say, I wouldn't be in this predicament."
            $ fian = "n"
            i "Sometimes the things that happen to us are out of our control..."
            a "Speaking of which..."
            
        "I would be devastated in your place":
            $ renpy.block_rollback()
            $ fian = "sad"
            i "I would be devastated in your place."
            a "I guess you would just wear it worse than I do."
            a "You can be a bit of a drama queen sometimes."
            i "Me, a drama queen?"
            a "When you broke up with Gillian you were very theatrical about it."
            $ fian = "serious"
            i "I think I have all the right to feel as I did."
            a "Oh, sorry. It's still a touchy subject?"
            i "It's... It's just that you can be quite insensitive sometimes."
            a "Well, excuse me. I'm not an artist like you guys."
            a "I guess I'm not in touch with all those emotional things as you are."
            i "Yeah, whatever."
            $ fian = "n"
            
    a "How are you doing?"
    i "I don't have much to tell, to be honest."
    i "I'm stuck with my internship, living with Perry, trying to write my book..."
    i "My life's not very exciting."
    a "Awww, come on."
    "She pinched my cheek in some sort of tender gesture."
    i "I'm hoping to change that, of course..."
    i "Too bad you can't come tonight."
    a "I'm still adjusting to my new job, and money's tight..."
    a "But we should see each other way more often!"
    $ fian = "smile"
    i "I would like that."
    i "Well, I need to get going. I have a book review to submit to my boss."
    a "Yeah, I have things to do, too."
    if v1_encourage_alison:
        a "Thanks for your nice words, by the way."
        a "It's not often I hear you say those things!"
        i "Well, you need to hear them."
        "Alison smiled and kissed me on the cheek."
    $ falison = "n"
    show ian at lef3
    show alison at truecenter
    with move
    $ flena = "n"
    show lenawork at right
    with short
    "We paid at the counter."
    if v1_name_wits or v1_name_charisma:
        l "Did you like the food?"
        a "It was pretty good, yeah."
        i "Your recommendation was spot on."
        l "Glad to be of service. Have a nice day!"
        a "You too. Bye!"
        $ fian = "n"
        i "See you soon."
        l "Bye!"
        hide lenawork
        with short
        "I didn't have the chance to really speak to her today."
        "After that chat the other day, today felt like she was just a waitress and I just a client..."
        "It felt like something between awkward and underwhelming."
        
    else:
        $ fian = "sad"
        wai "Thank you. Have a good day!"
        a "Bye!"
        i "Yeah, bye..."
        hide lenawork
        with short
        "Seems like she was giving me no chance to talk to her today."
        "I still hadn't asked her name..."
    "But I had had a very nice time with Alison, at least."
    "I was glad to see her, and hoped to see her again soon."
    stop music fadeout 2.0
    jump v1nightout
    
  
## V1 HOLLY LUNCH ###############################################################################################
  
label v1holly:
    
    scene street
    with long
    $ fian = "smile"
    $ fholly = "n"
    show ian at lef
    show holly at rig
    with short
    i "Do you have any place in mind?"
    h "Yes, I know a cafe just around the corner..."
    h "It's cozy and I love the eggs Benedict they cook there!"
    i "I know the place... I like to go there to write from time to time."
    $ fholly = "happy"
    h "Really? Me too!"
    i "It's weird we have never met there, then."
    hide holly
    $ fholly = "shy"
    show holly3 at rig
    with short
    h "Y--{w=0.5}Yeah..."
    i "Come on, let's go."
    play music "music/normal_day.mp3" loop
    scene cafe
    with long
    $ fian = "smile"
    $ fholly = "n"
    show ian
    show holly at lef3
    with short
    "I hadn't planned coming back to the cafe again, but here I was."
    if v1_name_wits or v1_name_charisma:
        "I would see Lena again. I should play it cool."
        $ flena = "n"
        show lenawork at rig3
        with short
        $ flena = "smile"
        l "Oh, hi Ian."
        i "Hey, hello again."
        "The fact that she remembered my name put a smile on my face."
        i "How are you doing?"
        l "Working hard, ha ha."
        i "We're going to give you a bit more trouble, then. We've come for some lunch."
        l "No trouble at all."
        l "Take a seat over here. I'll be right back with the menu."
        hide lenawork
        with short
        h "I didn't know you were friends with the waitress."
        i "I wouldn't say we're friends. We just made some small talk the other day."
        h "I've seen her before. She's so pretty..."
        menu:
            "Yeah, she is":
                $ renpy.block_rollback()
                $ holly_change += 1
                i "Yeah, she is..."
                
            "I haven't noticed":
                $ renpy.block_rollback()
                $ fian = "blush"
                i "Uh, is she? I never noticed..."
                "I was lying, of course. But I didn't want to sound like a creep or something..."
                $ fian = "smile"
        i "Did you know she also likes literature?"
        h "Oh, really?"
        show lenawork at rig3
        with short
        l "Here's the menu, guys."
        l "I'd recommend our eggs Benedict, they're delicious!"
        i "Holly just told me the same thing before coming here."
        h "They're really good..."
        "Lena smiled at her."
        l "You have good taste."
        $ fholly = "shy"
        hide holly
        show holly3 at lef3
        with short
        h "T--{w=0.5}Thanks. You too."
        $ fholly = "blush"
        $ fian = "worried"
        $ flena = "worried"
        with short
        i "..."
        "Damn, that was an awkward answer."
        "Holly realized it and got visibly flustered, her cheeks completely red."
        "I felt the urge to break the ice and save her from that embarrassing situation."
        if ian_charisma == 0:
            "I felt I was going to make a fool out of myself too, but I had to keep talking now."
        else:
            "I had an idea of how to make Holly feel better."
        $ fian = "smile"
        i "Did you know Holly is a professional writer?"
        $ flena = "smile"
        l "Really?"
        $ flena = "worried"
        $ fian = "worried"
        l "Wait..."
        $ flena = "surprise"
        l "You're Holly Watson?"
        l "The author of \"The Ice Flower\"?"
        h "Y--{w=0.5}Yes."
        $ flena = "happy"
        l "I love your books!"
        $ fholly = "n"
        i "So you know her?"
        l "Yes! I read your two books a few months ago and I was hooked."
        l "I knew we lived in the same city, but I can't believe you have been coming to this cafe all along."
        $ fian = "smile"
        i "It's such a coincidence. Holly and I work together at the magazine I told you about."
        l "That's cool. My name's Lena, by the way. I'm a fan."
        h "Nice to meet you, Lena."
        
    else:
        $ v1_name = True
        "I would see the waitress again. Should I ask her name this time?"
        $ flena = "smile"
        show lenawork at rig3
        with short
        wai "Oh, hello again."
        i "Hey... How are you doing?"
        wai "Working hard, ha ha."
        i "We're going to give you a bit more trouble, then. We've come for some lunch."
        wai "No trouble at all."
        wai "Take a seat over here. I'll be right back with the menu."
        $ fian = "n"
        i "Thanks..."
        hide lenawork
        with short
        h "I didn't know you were friends with the waitress."
        i "I wouldn't say we're friends. In fact I don't even know her name."
        i "We just made some small talk the other day."
        h "I've seen her before. She's so pretty..."
        i "Did you know she also likes literature?"
        h "Oh, really?"
        $ flena = "n"
        show lenawork at rig3
        with short
        wai "Here's the menu, guys."
        wai "I'd recommend our eggs Benedict, they're delicious!"
        i "Holly just told me the same thing before coming here."
        h "They're really good..."
        "The waitress smiled at her."
        wai "You have good taste."
        h "T--{w=0.5}Thanks. You too."
        $ fholly = "blush"
        hide holly
        show holly3 at lef3
        $ fian = "worried"
        $ flena = "worried"
        with short
        "..."
        "Damn, that was an awkward answer."
        "Holly realized it and got visibly flustered, her cheeks completely red."
        "I felt the urge to break the ice and save her from that embarrassing situation."
        i "You told me you liked literature the other day, right?"
        $ flena = "n"
        wai "Huh? Yeah."
        $ fian = "smile"
        if ian_charisma == 0:
            "I felt I was going to make a fool out of myself too, but I had to keep talking now."
        else:
            "I had an idea of how to make Holly feel better."
        i "Did you know Holly is a professional writer?"
        $ flena = "smile"
        wai "Really?"
        $ flena = "worried"
        $ fian = "worried"
        wai "Wait..."
        $ flena = "surprise"
        wai "You're Holly Watson?"
        wai "The author of \"The Ice Flower\"?"
        h "Y--{w=0.5}Yes."
        $ flena = "happy"
        wai "I love your books!"
        $ fholly = "n"
        i "So you know her?"
        wai "Yes! I read your two books a few months ago and I was hooked."
        wai "I knew we lived in the same city, but I can't believe you have been coming to this cafe all along."
        $ fian = "smile"
        i "It's such a coincidence. Holly and I work together at the magazine I told you about."
        l "That's cool. My name's Lena, by the way. I'm a fan."
        h "Nice to meet you, Lena."
        "Lena looked at me."
        l "Sorry, I still haven't asked your name..."
        i "I'm Ian."
        l "Cool. We finally can call each other by our actual names, ha ha."
        
    l "Sorry, I have to take care of the other tables... And bring you your food!"
    i "Don't let us keep you."
    l "Maybe we can talk another time, when things are more calm."
    h "Sure... I come here often."
    l "I know."
    hide lenawork
    with short
    if v1_name_wits == False and v1_name_charisma == False:
        "So I finally learned her name... Lena."
        "This was not how I had planned things out, but I got what I wanted in the end."
    "I looked at Holly."
    i "So this is what being a famous writer feels like..."
    h "I'm not famous... I just have some following..."
    i "I'd say being fangirled all over by a waitress at a random place qualifies as being famous, ha ha."
    h "I don't know..."
    i "You should embrace it. As I see it, you're living the dream, enjoy it."
    i "I'd love to be in your situation."
    h "I guess you're right... But it still feels weird."
    menu:
        "Weird? How?":
            $ renpy.block_rollback()
            $ fian = "sad"
            i "Weird? How?"
            h "Well... It's hard to explain..."
            h "I guess it's just that I'm so used at writing for myself..."
            h "I close myself off in my little world and write the stories that \"feel\" right to me."
            i "So you mean you write for your own enjoyment."
            h "Yes, that's it. I've never been used to share those with the public."
            i "Well, that's what being a professional writer is about!"
            h "I know, and I always wanted to be one..."
            h "But it just feels weird having people reach out to me because they've been touched by what I wrote."
            i "I guess I can see your point..."
            $ fian = "smile"
            
        "{image=icon_wits.png}I totally get what you mean" if ian_wits > 0:
            $ renpy.block_rollback()
            i "Yeah, I totally get what you mean..."
            i "Writing is a very lonely activity... You close yourself off from the outside world to explore the one within you."
            $ fholly = "smile"
            h "Yes! I'm so used to just be by myself, in my own world..."
            h "It feels really weird to see the stories I come up with reach other people, and how they react."
            i "I guess we all write for ourselves and then hope others relate to our work and feel like it's also part of them..."
            $ fholly = "happy"
            "Holly looked me with a spark in her eyes that I hadn't seen before."
            h "Yes, I think that's exactly it..."
            h "And well... I guess I never expected people to react this way to my stories."
            h "I've never been that much in touch with the \"outside world\", yet now they reach out to me..."
            i "That's because you created something of great value."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_holly += 1
            $ fholly = "shy"
            h "Oh... Thank you..."
            
        "You should be super happy!":
            $ renpy.block_rollback()
            i "Why? You should be super happy!"
            i "You're achieving the goal of any professional writer."
            h "I know that a professional writer can't be one without an audience, but..."
            h "I guess I've never considered the readers when I wrote. I just did it for myself, writing the stories that \"felt\" right to me."
            h "And to see that those stories have an effect on people, that cause them to reach out to me..."
            h "It's just weird."
            i "Ahhh, that would be so nice..."
            i "As I said, embrace it."
            h "I'm trying..."

    hide holly3
    $ fholly = "n"
    show holly2 at lef3
    with short
    h "Anyways, I should help you with your review, right?"
    h "That's why we came here, after all..."
    i "Sure."
    "We finished lunch as we discussed how we could improve my book review to meet Minerva's standards."
    "Holly provided very useful insight on how she wrote hers. It still felt like I was lying, but I knew that was the only way to do what was being asked of me."
    i "Thanks, Holly. These are some very helpful notes."
    h "Don't mention it... I know it's a bit frustrating, but this is what the magazine wants."
    i "Let's get back then. I need to re-write it and place it on Minerva's desk right away."
    $ flena = "smile"
    show lenawork at right
    with short
    "We paid at the counter."
    l "I hope you enjoyed the meal."
    i "Thanks for the recommendation. The eggs were amazing."
    l "Sorry to have bothered you before. I was just really surprised to learn who you really were, Holly."
    h "It's no bother at all... I'm so glad you liked my books."
    l "Maybe next time you can tell me a bit more about them? I have a few questions I would love to discuss directly with the author!"
    "Holly smiled at her."
    h "I would love that."
    if v1_name_wits or v1_name_charisma:
        "Then Lena turned to me."
        l "And we can keep discussing the sorry state of the book industry, Ian."
        i "Whenever you want."
    l "See you soon!"
    h "Bye!"
    hide lenawork
    with short
    "It had been a really unexpected coincidence that Lena was one of Holly's readers."
    if v1_name_wits or v1_name_charisma:
        "She wanted to meet her and talk to her... But she hadn't forgotten about me."
        "Could I hit her up and take her up on her offer?"
    else:
        "She seemed more interested in her than in me... But it was only natural."
        "At least I had something new in common with Lena now, something I could talk to her about."
        "And I had learned her name..."
    stop music fadeout 2.0
    jump v1nightout

## V1 ROCKBAR #######################################################################################################################################################################################################################

label v1nightout:   
    
    $ v1chatbaralison = False
    $ v1chatbarperry = False
    $ v1chatbaremma = False
    $ v1chatbarperryinterrupt = False
    $ v1chatbarpast = False
    $ v1chatbarfunny = False
        
    scene ianhomenight
    $ fian = "n"
    show ian at lef
    with long
    "After I handed the modified book review to Minerva I went back home, had a shower and ate dinner."
    "Soon, it was time to leave and meet the guys over at the bar."
    $ fperry = "happy"
    show perry at rig
    with short
    p "Are you ready?"
    i "Yeah. You seem pretty pumped about today."
    p "It's been a while s--{w=0.5}since we gathered the gang to go get some beers."
    $ fian = "happy"
    i "And it's been a while since you got to see Emma."
    hide perry
    show perry2 at rig
    $ fperry = "meh"
    p "Again with t--{w=0.5}t--{w=0.5}that?"
    p "I hope you k--{w=0.5}keep your mouth s--{w=0.5}shut and don't make any stupid c--{w=0.5}comment like this tonight."
    i "Don't worry, my lips are sealed."
    p "It better be t--{w=0.5}true."
    if v1_alisonlunch == False:
        $ fian = "smile"
        hide perry2
        $ fperry = "n"
        show perry at rig
        with short
        i "Oh, by the way, Alison called yesterday."
        i "She said she'd drop by tonight, too."
        p "Oh, Alison? OK, that's cool."
    i "Well then, let's go."
    
    play music "music/rock_bar.mp3" loop
    scene rockbar
    with long
    "The Fortress was not far from our place and we knew it well."
    "We had been coming to this bar regularly for the past few years."
    "We liked the music and the beer was affordable. It just felt like the right place for us."    
    $ fian = "smile"
    show ian at lef3
    $ fperry = "n"
    show perry at rig3
    with short
    p "Emma texted me that she had already arrived..."
    i "There she is."    
    $ femma = "n"
    show emma
    with short
    e "Hey guys! Long time no see!"
    "Emma greeted us with one big hug for each."
    "She was that kind of easy-going and optimistic person one finds so easy to be around of."
    $ ian_emma_agenda = True
    p "Let's get some b--{w=0.5}beers and take a seat."
    
    if v1_alisonlunch == False:
        $ fian = "smile"
        show ian at centerlef
        show perry at right
        show emma at rig
        with move
        $ falison = "n"
        show alison at left
        with short
        a "Hello, guys!"
        i "Oh, hey Alison!"
        e "Oh, I didn't know you were coming!"
        a "Yeah, I'm just dropping by for an hour or so. I need to get up early in the morning tomorrow."
        p "Really? You can't even afford to get a Friday night off?"
        a "Not right now. I'm still trying to adapt to my new job."
        a "Not that you would understand something like that."
        hide perry
        $ fperry = "meh"
        show perry2 at right
        with short
        p "W--{w=0.5}what's that supposed to mean?"
        a "It means you'd need to get a job to understand, ha ha."
        p "Yeah, right..."
        "Alison took a seat next to me."
        hide perry2
        $ fperry = "n"
        show perry at right
        with short
        a "It's been ages since I came to this bar... I feel like a teenager again."
        a "So, how have you guys been?"
        $ fian = "n"
        i "You know, same old, same old..."
        a "Still doing that internship you hate at the magazine?"
        i "Indeed. I had trouble with my boss yesterday, yet again..."
        e "She's still going after you?"
        i "Yeah, she has something against me, I swear..."
        a "Did you give her reasons?"
        if ian_charisma > 0:
            $ fian = "smile"
            i "Me, reasons? I couldn't even if I wanted too, I'm a lovable guy through and through."
            a "You're right about that."
        else:
            i "Nothing out of the ordinary or so outrageous that she would cross me like this!"
            a "You never know, sometimes you just get on somebody's nerves without really knowing why."
            i "I'm not sure I want her to tell me."
        p "So Emma, what have you been up to?"
    else:
        e "I'm glad to see you guys. Sorry about not keeping in touch too much."
        i "That's OK, we've all had our own stuff to take care of."
        p "So, what have you been up to?"
    e "Oh man, lots of changes."
    
    e "I just moved to a new flat."
    i "Again? You moved like three or four months ago."
    e "Yeah... It seemed like a fun place to be, but it was too crazy!"
    menu:
        
        "Why was it crazy?":
            $ renpy.block_rollback()
            i "Crazy? Why was it crazy?"
            e "Oh, you know, the people living there."
            e "My flatmates liked to throw parties almost every day. The house was always full of people."
            menu:
                "That sounds like fun":
                    $ renpy.block_rollback()
                    $ fian = "smile"
                    i "That sounds like fun, actually."
                    play sound "sfx/xp.mp3"
                    show charisma_up
                    $ ian_charisma_xp +=1
                    call screen skillsup
                    e "Yes, it was! But what's not fun is living in the house where all the parties are held!"
                    e "It was very dirty, the toilet was always splashed with piss or even vomit..."
                    p "Fuck, that's disgusting."
                    $ femma = "smile"
                    e "One morning I was going to take a shower and found some dude passed out in the bathtub."
                    p "You didn't even know who he was?"
                    e "No freaking clue, dude."
                    $ femma = "n"
                    i "Well, that sounds pretty inconvenient, yeah!"
                    p "No wonder you wanted to move."
                        
                "That sounds bothersome":
                    $ renpy.block_rollback()
                    $ fian = "serious"
                    i "That sounds really bothersome."
                    i "Not being able to relax and concentrate at home... I would go crazy."
                    play sound "sfx/xp.mp3"
                    show wits_up
                    $ ian_wits_xp +=1
                    call screen skillsup
                    e "You have no idea. At first it was fun, meeting new people every week, getting wasted and having fun..."
                    e "But man, the place was dirty! The toilet was always splashed with piss or even vomit..."
                    p "Fuck, that's disgusting."
                    $ femma = "smile"
                    e "One morning I was going to take a shower and found some dude passed out in the bathtub."
                    p "You didn't even know who he was?"
                    e "No freaking clue, dude."
                    $ femma = "n"
                    $ fian = "smile"
                    i "See? I wouldn't even be able to last for three days living there."
                    p "No wonder you wanted to move." 
                    
                "Were there hot chicks?":
                    $ renpy.block_rollback()
                    $ fian = "shy"
                    i "Were there any hot chicks?"
                    $ femma = "smile"
                    e "Do you guys think about any other stuff? Ha ha."
                    play sound "sfx/xp.mp3"
                    show lust_up
                    $ ian_lust_xp +=1
                    call screen skillsup
                    i "It's important information."
                    e "I guess there were some, yeah."
                    $ fian = "smile"
                    i "Hey, and you never invited us!"
                    e "Sorry! But that house was chaos."
                    p "How so?"
                    e "It was so damn dirty! The toilet was always splashed with piss or even vomit..."
                    p "Fuck, that's disgusting."
                    $ femma = "smile"
                    e "One morning I was going to take a shower and found some dude passed out in the bathtub."
                    p "You didn't even know who he was?"
                    e "No freaking clue, dude."
                    $ femma = "n"
                    i "That's pretty awful... But the hot chicks make up for it!"
                    e "Ha ha, shut up."
                    p "No wonder you ended up moving."
                
        "Good thing you moved then":
            $ renpy.block_rollback()
            $ fian = "smile"
            i "Good thing you moved, then."
            p "It seems you can't stay in just one place, though..."
            e "I guess it's just how it is!"
                
    if v1_alisonlunch == False:
        a "Moving is the worst. I had to do it a while ago too, after I broke up with my boyfriend."
        $ femma = "surprise"
        e "You broke up with him? You two had been together for like, two years or something like that right?"
        a "Yes, almost two years. We even decided to move together, but it obviously didn't work out."
        $ femma = "sad"
        e "I'm sorry to hear that."
        a "Well, better to learn he was not the man of my life now rather than ten years in the future."
        $ femma = "n"
        e "Well, that's a good way to see it."
        i "I don't know how you manage to always be so optimistic."
        a "I don't surrender easily. Though sometimes life likes to give me reasons to!"
            
    menu v1chatbar:
            
        "Ask about Emma's life" if v1chatbaremma == False:
            $ renpy.block_rollback()
            $ v1chatbaremma = True
            i "By the way, Emma, did you find a job yet?"
            $ femma = "sad"
            e "Not yet... It's proving difficult."
            p "Finding a job is very hard."
            if v1_alisonlunch == False:
                a "Especially if you don't try..."
                p "What was that?"
                a "Nothing."
            e "I've been to several interviews already, but it seems I'm not the kind of person they're looking for."
            p "How so?"
            e "Mhhh, well, for example, the interview I had this week..."
            $ femma = "n"
            e "They asked us which animal we identified as."
            e "The other candidates all named animals like the eagle, the lion, the dolphin..."
            p "So pretentious."
            if v1_alisonlunch:
                i "Of course, you have to market yourself..."
            else:
                a "Of course, you have to market yourself. It's basic."
            p "And what animal did you identify yourself as?"
            $ femma = "smile"
            e "The cockroach."
            $ fperry = "sad"
            $ fian = "happy"
            if v1_alisonlunch:
                p "Really?"
            else:
                a "What? Really?"
            i "Ha ha ha, why would you do that?"
            e "Man, cockroaches are awesome!"
            e "I told them the cockroaches are the toughest animal there is, if we had a nuclear war they would be the only ones to survive and inherit the earth!"
            e "They are resourceful and always find a way to survive. What more do you want when you hire someone like that?"
            i "I guess it's one way to see it."
            p "I'm not surprised they didn't give you the job, though."
            if v1_alisonlunch == False:
                a "You need to learn to sell yourself. That's almost as important as your resume when getting a job!"
            $ femma = "n"
            $ fperry = "n"
            $ fian = "n"
            e "I know, I know. I guess I'm just too honest."
            jump v1chatbar
                
        "Ask about Perry's life" if v1chatbarperry == False:
            $ renpy.block_rollback()
            $ v1chatbarperry = True
            i "What's up with you, Perry?"
            i "Any news about that guy who wanted to hire you?"
            hide perry
            $ fperry = "meh"
            if v1_alisonlunch:
                show perry2 at rig3
            else:
                show perry2 at right
            with short
            p "Not really..."
            e "Hire you? For what?"
            p "He said he was looking for someone to do some storyboards for him..."
            if v1_alisonlunch == False and v1chatbaralison == False:
                $ v1chatbarperryinterrupt = True
                $ v1chatbaralison = True
                p "So I was t--{w=0.5}thinking..."
                a "You have to be careful with who hires you. You know what happened to my previous boss?"
                a "He's in jail."
                e "In jail?"
                $ femma = "sad"
                a "Oh, you don't know about my last job?"
                e "Nope, what happened?"
                "I knew the story, so I helped put Emma up to speed."
                i "Turns out the CEO of the company she was working for was caught embezzling and committing fiscal fraud."
                a "Yep, needless to say, he was put in jail and the company went bankrupt. And I lost my job."
                $ falison = "serious"
                a "And they owe me a lot of money, too..."
                a "I put a lot of effort into the company and my stupid boss blew everything up."
                e "Geez, that's bad... Corrupt businessmen are a blight on this world!"
                a "I mean, if you're going to commit fraud and steal, at least don't get caught!"
                $ femma = "n"
                a "Now I have to suffer thanks to his incompetence!"
                p "Sounds like you have it rough..."
                hide perry2
                show perry at right
                with short
                $ fperry = "n"
                p "It must be f--{w=0.5}frustrating losing all you worked for after all those years in c--{w=0.5}college studying like crazy."
                $ falison = "sad"
                p "And you break up with your b--{w=0.5}boyfriend at the same time... How old are you?"
                p "You're twenty-nine already, right?"
                a "I'm twenty-eight!"
                p "Right. You were always t--{w=0.5}the oldest in class."
                "Perry was probably trying to cheer her up or something like that, but he was doing a dismal job."
                "He was so clueless sometimes."
                "Better to change the subject."
                $ falison = "n"
            else:
                e "That's cool!"
                p "Well, yeah, but he said I would only get p--{w=0.5}paid if the project is greenlit, so..."
                i "That's shitty."
                e "Yeah, we upcoming artists always have to sell our work cheap..."
                i "Only if you get a name for yourself do clients start to treat you like a normal professional instead of taking you for a fool."
                if v1_alisonlunch == False:
                    a "That's a problem I don't envy you for, you bunch of bohemians."
                p "In any case, he hasn't told me if he wants me to do the storyboards after all or not."
                i "You should get back to him and press him a bit on the issue."
                p "I'll see ab--{w=0.5}about that."
                p "C--{w=0.5}can we change t--{w=0.5}the subject?"
                hide perry2
                hide perry
                $ fperry = "n"
                if v1_alisonlunch:
                    show perry at rig3
                else:
                    show perry at right
                with short
            jump v1chatbar
            
        "Ask about Perry's life... again" if v1chatbarperryinterrupt:
            $ renpy.block_rollback()
            $ v1chatbarperryinterrupt = False
            i "So Perry, you were telling us about that storyboard gig you had..."
            p "Oh, yeah."
            if ian_perry < 6:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_perry+= 1
            "Alison had interrupted him quite mercilessly and I wanted to give Perry some attention."
            p "So, this dude wanted me to make some storyboards for some advertising or something..."
            e "That's cool!"
            p "Well, yeah, but he said I would only get p--{w=0.5}paid if the project is greenlit, so..."
            i "That's shitty."
            e "Yeah, we upcoming artists always have to sell our work cheap..."
            i "Only if you get a name for yourself do clients start to treat you like a normal professional instead of taking you for a fool."
            if v1_alisonlunch == False:
                a "That's a problem I don't envy you for, you bunch of bohemians."
            p "In any case, he hasn't told me if he wants me to do the storyboards after all or not."
            i "You should get back to him and press him a bit on the issue."
            p "I'll see ab--{w=0.5}about that."
            p "I g--{w=0.5}guess that's all I have to tell."
            hide friend_up
            jump v1chatbar
                
        "Ask about Alison's life" if v1_alisonlunch == False and v1chatbaralison == False:
            $ renpy.block_rollback()
            $ v1chatbaralison = True
            i "So, Alison, any news about your old boss?"
            a "Yeah, he's in jail."
            e "In jail?"
            $ femma = "sad"
            a "Oh, you don't know about my last job?"
            e "Nope, what happened?"
            "I knew the story, so I helped put Emma up to speed."
            i "Turns out the CEO of the company she was working for was caught embezzling and committing fiscal fraud."
            a "Yep, needless to say, he was put in jail and the company went bankrupt. And I lost my job."
            $ falison = "serious"
            a "And they owe me a lot of money, too..."
            a "I put a lot of effort into the company and my stupid boss blew everything up."
            e "Geez, that's bad... Corrupt businessmen are a blight on this world!"
            a "I mean, if you're going to commit fraud and steal, at least don't get caught!"
            $ femma = "n"
            a "Now I have to suffer thanks to his incompetence!"
            p "Sounds like you have it rough..."
            $ falison = "sad"
            p "It must be f--{w=0.5}frustrating losing all you worked for after all those years in c--{w=0.5}college studying like crazy."
            p "And you break up with your b--{w=0.5}boyfriend at the same time... How old are you?"
            p "You're twenty-nine already, right?"
            a "I'm twenty-eight!"
            p "Right. You were always t--{w=0.5}the oldest in class."
            "Perry was probably trying to cheer her up or something like that, but he was doing a dismal job."
            "He was so clueless sometimes."
            "Better to change the subject."
            $ falison = "n"
            jump v1chatbar
            
        "Wait for Cindy and Wade":
            $ renpy.block_rollback()
            
    e "What's up with Wade? He said he was coming, right? I haven't seen him since forever."
    p "Yeah, we managed to make him agree to come."
    i "Well, we didn't. Cindy did."
    e "They are living together, right?"
    p "Yup. Six months."
    if v1_alisonlunch:
        e "Good for them."
        $ fian = "n"
        i "I'm not so sure about that."
        e "Why not?"
    else:
        a "Good for them."
        $ fian = "n"
        i "I'm not so sure about that."
        a "Why not?"
    p "Well, you know Wade. Since he's living with Cindy he doesn't want to go out anymore."
    e "Well, he's always been very chill."
    i "But we used to go out often back then. He loved to go out and score with chicks."
    "Perry looked at me."
    p "He was pretty good at it... Much better than us."
    e "Oh, yeah, I remember. He always had some girl to spend time with."
    if v1_alisonlunch == False:
        a "Well, he's tall and handsome. It's only natural girls flock around him."
        i "He has those gifts, that's for sure..."
    e "I guess he doesn't need to do that anymore, since he's found a girl he wants to live with."
    i "Yeah, but it seems he's lost his fire."
    if v1_alisonlunch == False:
        a "Sometimes that happens. Wade was never the most energetic dude to begin with."
    p "And he's gotten fat."
    if v1_alisonlunch == False:
        a "Well, that's not so good."
        e "He's just enjoying his life in a different way, guys."
        a "By the way, isn't Jeremy coming?"
        i "No, he's working at a club Friday nights."
        $ falison = "flirt"
        a "I haven't seen him in ages... But I saw a picture of him and he's looking good!"
        i "Yeah, he's going to the gym a lot..."
        a "Too bad he's not coming. I would've liked seeing him."
        $ falison = "n"
        i "Maybe next time..."
    else:
        e "He's just enjoying his life in a different way, guys."
    c "Hey, guys!"
    $ fperry = "n"
    $ fian = "n"
    $ femma = "n"
    show ian at truecenter
    show emma at rig5
    show perry at right5
    with move
    if v1_alisonlunch == False:
        hide alison
    $ femma = "smile"
    $ fian = "smile"
    $ fwade = "smile"
    $ fcindy = "n"
    show wade2 at left5
    show cindy2 at lef5
    with short
    "Cindy touched me on the shoulder and I turned around to greet her and Wade."
    i "Here you are."
    hide cindy2
    $ fcindy = "serious"
    show cindy at lef5
    with short
    c "Sorry for the delay. Someone had trouble getting his butt off the couch."
    w "I told you I had to take revenge on that guy. He had been beating my ass all afternoon playing online."
    c "Ugh, men and their silly games."
    $ fcindy = "n"
    e "How are you guys? Long time no see, Wade!"
    w "Nice to see you, Emma. You look like you're doing great."
    e "Oh, you know me. I don't like to find reasons to complain."
    $ femma = "n"
    if v1_alisonlunch == False:
        hide emma
        $ falison = "smile"
        show alison at rig5
        with short
        a "Hey Wade!"
        w "Alison! I didn't know you were coming."
        a "You know me, I dropped by at the last minute."
        $ falison = "n"
        a "I can't stay for much longer, though."
        w "Let's catch up, then."        
    "We ordered another round of beers and toasted."
    "It was nice being together with the guys again."
    "As we grew older, it didn't happen as often as it used to."
    "We drank and talked, just chilling, having a real good time."
    if v1_alisonlunch == False:
        a "Well guys, time for me to go. I have responsibilities to attend to."
        c "It was great seeing you, Alison."
        w "Yeah, like in the good old times."
        "Alison said goodbye to everyone, leaving me for last."
        a "Well, it was short but intense. It's always nice seeing you, Ian."
        menu:
            "It's nice seeing you too":
                $ renpy.block_rollback()
                i "Yes, the same goes for you. It's really nice seeing you too."
                "She pinched my cheek in some sort of tender gesture."
                a "See you soon, OK?"
                i "Sure."                
            "{image=icon_charisma.png}We should do this more often" if ian_charisma > 0:
                $ renpy.block_rollback()
                $ v1_alisonoften = True
                i "We should do this more often."
                a "Well, you can always call me if you want to see me."
                i "Sure... I will."                
            "Take care":
                $ renpy.block_rollback()
                i "Take care."
                a "I will. I'm a big girl, you know."
        "She waved her hand at us one last time."
        a "Bye, guys!"
        hide alison
        $ femma = "n"
        show emma at rig5
        with short
    menu v1chatbar2:
        "Talk about the old times" if v1chatbarpast == False:
            $ renpy.block_rollback()
            $ v1chatbarpast = True
            i "Sometimes I miss those good old times in high school..."
            p "Good old times? We were a b--{w=0.5}bunch of nerds, have you forgotten?"
            w "Hey, speak for yourself."
            p "You were a nerd as m--{w=0.5}much as any of us back then, W--{w=0.5}wade."
            e "We were not the most popular kids, that's for sure ha ha."
            i "Well, you never cared about that. That's why you were quite popular despite being a nerd, Emma."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_emma += 1
            c "I can't get over the fact you four played in a band together back in high school."
            c "That's not nerdy."
            e "Oh, I can assure you we played nerdy music."
            w "And I was high most of the time."
            c "Still, I would've liked to see you play!"
            i "There must be a few videos somewhere on my hard drive..."
            w "I don't know if we should revisit that."
            p "C--{w=0.5}come on, we were pretty good actually!"
            c "I know Wade played guitar..."
            w "And I also sang the chorus."
            c "You played the bass, right Ian?"
            i "Yeah."
            e "And I played the drums!"
            c "Really? Then, the singer was..."
            $ fcindy = "sad"
            $ fperry = "meh"
            p "..."
            p "W--{w=0.5}what?"
            c "You were the singer, Perry?"
            p "Yes, of course."
            c "Oh. That's... interesting."
            "I leaned into Cindy's ear and I whispered."
            i "He doesn't stutter when he sings."
            $ fcindy = "surprise"
            c "Ooooh, I see."
            $ fcindy = "n"
            c "Have you thought about getting back together and playing sometime?"
            i "It's been far too long. We were kids back then."
            $ fperry = "happy"
            p "But it w--{w=0.5}would be fun to play again sometime."
            w "I don't have the time or energy for that, man. Forget it."
            $ fperry = "n"
            p "You're a p--{w=0.5}party pooper, dude..."
            hide friend_up
            jump v1chatbar2
            
        "Talk about a funny story" if v1chatbarfunny == False:
            $ renpy.block_rollback()
            $ v1chatbarfunny = True
            w "By the way, this just came to mind..."
            w "Do you guys know anything else about that dude that wreaked havoc on Ian's birthday party?"
            w "What's become of him?"
            i "Oh fuck, that dude. I don't know, he was Perry's friend."
            hide perry
            $ fperry = "meh"
            show perry2 at right5
            with short
            p "What, you're gonna blame me again for what happened?"
            $ fian = "serious"
            i "Well, it was not my fault, that's for sure."
            e "What happened? I missed that party, so I don't know the story."
            w "Oh, you're gonna love it."
            $ fian = "smile"
            $ fcindy = "serious"
            c "It's disgusting."
            i "OK, so, it was my twenty-seventh birthday, and I invited these people to my place to celebrate."
            p "Your parents' place."
            $ fcindy = "n"
            $ fian = "serious"
            i "Well, yeah, technically my parents' place. The place where I lived."
            e "So?"
            i "Well, so I invited some people, and Perry asked me if this friend of his could come."
            i "I wasn't sure at first, since we were already quite a few people, but he insisted to the point of saying that if his friend couldn't come, he wouldn't come to my birthday either."
            p "I'm a loyal friend."
            i "To whom?"
            p "Hey shut up man, there was no way for me to know what would happen."
            c "But you knew the guy, you should've seen it coming."
            e "What the hell happened?"
            i "Well, first of all he got wasted as fuck."
            w "We think he was on drugs too, most probably."
            i "He began creeping people out, talking nonsense and acting kind of crazy."
            $ fcindy = "serious"
            $ fian = "sad"
            c "He was really touchy and inappropriate, too."
            i "He then stumbled and fell face first into my father's drink cabinet, smashing all the glasses and a few bottles."
            $ femma = "surprise"
            $ fwade = "happy"
            w "That's not the best part."
            i "He then locked himself up in the bathroom. We couldn't open the door and he was not answering."
            c "We thought he might have died from alcohol poisoning or something."
            p "Well, he was alive in the end."
            i "Well yeah, we had to pry the door open and..."
            w "And we found him passed out, surrounded in his own shit, piss and puke!"
            w "Ha ha ha! He puked, pissed his pants and shat himself all at the same time!"
            w "Hat trick! Ha ha ha!"
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_wade += 1
            e "Oh my God, that had to be a sight to behold."
            w "It was epic!"
            $ femma = "sad"
            $ fian = "mad"
            i "Yeah, so epic that my parents kicked me out."
            e "So that's the reason you're living with Perry? They kicked you out?"
            i "Yeah, all because Perry was hellbent on bringing this fucking guy to my party!"
            w "Ha ha ha, it was hilarious!"
            $ fperry = "mad"
            p "W--{w=0.5}well, you were a bit old to be living with your parents still. It was time for you t--{w=0.5}to leave."
            i "Says you, who has a flat for free provided by your parents!"
            p "It's not my fault that my family has a few p--{w=0.5}properties."
            p "It would be dumb of me to live somewhere where I have to pay a rent, having a house for free."
            p "That's burning money."
            i "Yet you make me pay you a rent!"
            p "Well, a home is not sustained for free!"
            $ femma = "smile"
            e "Calm down, guys! These things can happen, I would know!"
            e "It was a shitty situation -no pun intended- but now you have a really funny story to tell for it."
            $ fian = "sad"
            $ fperry = "n"
            $ fwade = "smile"
            $ fcindy = "n"
            $ femma = "n"
            i "Yeah, and I got kicked out too..."
            $ fian = "smile"
            hide friend_up
            jump v1chatbar2
            
        "Play a game of pool":
            $ renpy.block_rollback()
            c "Hey guys, let's do something."
            c "I feel like playing a game of pool, what do you say?"
            w "Sounds good."
            i "Alright, I'm in."
            p "I'm not feeling like it. I'd prefer to stay here just talking."
            e "I'll stay with you then."
            $ fperry = "happy"
            p "Oh, that's cool, that's cool."
            p "Go ahead and go play, guys."
            i "Sure."
            jump v1pool
            
        "Just drink beer":
            $ renpy.block_rollback()
            "We finished our second round of beers and I ordered the third."
            c "Let's do something."
            c "I feel like playing a game of pool, what do you say?"
            i "I'll pass. I prefer just to stay here chatting."
            p "Yeah, me too."
            $ fcindy = "serious"
            c "You can be a bit boring, guys."
            c "Let's do a one on one, Wade."
            w "Alright."
            hide cindy
            hide wade2
            hide perry2
            show perry at right5
            $ fperry = "n"
            with short
            $ fian = "smile"
            $ femma = "n"
            show ian at lef3
            show emma at truecenter
            show perry at rig3
            with move
            "The couple left the table and went to play a game of pool."
            e "You don't want to go?"
            p "Cindy can be a bit too competitive. I'm not feeling like putting up with that."
            i "Same."
            e "I see. She's a funny girl."
            e "She seems to have a lot more energy than Wade, though..."
            "Emma, Perry and I continued drinking and chatting."
            "After the fourth round, I started to feel the alcohol clearly kicking in."
            p "Let's get another round."
            e "I'm fine, thanks."
            menu:
                "Enough for me, too":
                    $ renpy.block_rollback()
                    i "I'm set. Enough for me, too."
                    $ fperry = "mad"
                    p "That's so weak."
                    $ fperry = "meh"
                    p "Well, I'm gonna get another round for myself."
                    i "Suit yourself, just don't make me carry you home tonight."
                    p "When the hell has that ever happened?"
                    i "I don't want today to be the first time."
                    p "Whatever."
                    $ fperry = "happy"
                    "Perry got his drink and we continued chatting while he gulped it down."
                    
                "I want another one!":
                    $ renpy.block_rollback()
                    $ v1_drunk = True
                    $ fian = "happy"
                    $ fperry = "happy"
                    i "Another one for me!"
                    p "That's the spirit!"
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    $ ian_perry += 1
                    "We toasted and gulped down our fifth beer."
                    $ fian = "smile"
                    hide friend_up
            "After a while Wade and Cindy came back after finishing a couple of games of pool."
            $ fperry = "happy"
            $ fian = "smile"
            $ femma = "n"
            show perry at right5
            show ian at truecenter
            show emma at rig5
            with move
            $ fcindy = "flirt"
            $ fwade = "sad"
            show cindy2 at lef5
            show wade at left5
            with short
            e "Who won?"
            c "Me! Two to zero, nihil, nada!"
            w "You just got super lucky."
            c "You got destroyed!"
            $ fcindy = "n"
            $ fwade = "n"
            w "Whatever."
            jump v1barend
    
## POOL ######################### ####################### ####################### ####################### ####################### 

label v1pool: 
    
    scene rockbar
    $ fian = "smile"
    $ fcindy = "n"
    $ fwade = "smile"
    show ian at rig3
    show cindy
    show wade3 at lef3
    with long
    "The three of us took our beers and moved to the pool table."
    w "We're three people. How shall we do this?"
    c "Do you know how to play, Ian?"
    i "Barely. I've only played a few times."
    c "So Wade, it's you against me and Ian teams up with one of us."
    menu:
        "Join Wade":
            $ renpy.block_rollback()
            $ v1_teamwade = True
            i "How about we kick her ass, Wade?"
            $ fwade = "n"
            w "How bad are you actually?"
            $ fian = "sad"
            i "Eh... I don't know how to measure that."
            w "I'm just worried you're going to be a disadvantage rather than an asset..."
            i "Well, thanks for the trust... I thought the important part was having fun."
            w "Oh, you don't know her."
            $ fcindy = "flirt"
            c "Why don't we bet some money? To make things more interesting."
            i "Money?"
            c "Yeah, hard, shiny cash."
            c "We put the money on the table, winner takes all."
            w "But if you win you take double what you bet, and we just take fifty percent each. It's not fair."
            c "If that worries you it's because you know there's a good chance of you two men losing to a single girl."
            
        "Join Cindy":
            $ renpy.block_rollback()
            $ v1_teamcindy = True
            i "Sorry Wade, but I'm sure that siding with Cindy is siding with the winner."
            $ fwade = "happy"
            w "Go ahead, the way I see it, since you don't know how to play, having you on the team is a disadvantage rather than an asset."
            $ fian = "worried"
            $ fcindy = "serious"
            c "Now that you put it that way..."
            i "Hey! Thanks for the appreciation, guys."
            c "Well, even if I have a disadvantage I can still beat you!"
            w "We'll see about that!"
            $ fcindy = "flirt"
            c "Yeah? Why don't we bet some money then?"
            i "Money?"
            c "Yeah, hard, shiny cash."
            c "If you beat us, both Ian and I will pay you. But if you lose, you'll have to pay twice, to both of us!"
            $ fwade = "n"
            w "That's unfair, you stand to win the same as me but I stand to lose double the money!"
            c "If that worries you it's because you know there's a good chance of you losing to us."
            
    $ fwade = "serious"
    w "...!"
    w "Alright, get ready to eat dirt."
    c "It's on!"
    "Damn, they were a very competitive pair..."
    
    menu:
        "{image=icon_pay.png}Let's bet":
            $ renpy.block_rollback()
            i "Alright, here's the money."
            play sound "sfx/moneydown.mp3"
            show money_down
            $ ian_money -= 1
            "I hoped we would win, or else I would really miss that money..."
        "I'm out":
            $ renpy.block_rollback()
            $ v1_teamcindy = False
            $ v1_teamwade = False
            i "Sorry guys, but I'm tight on money."
            i "I don't wanna bet, so I'm out."
            c "Really? You're a coward..."
            i "Look, I just wanted to have fun playing a game of pool. I don't want to lose any money."
            c "Well, then it's you against me, Wade!"
            w "Prepare to lose!"
            "I left them to their competitive fight and went back to Emma and Perry."
            scene rockbar
            $ fian = "smile"
            $ femma = "n"
            $ fperry = "n"
            show ian at lef3
            show emma at truecenter
            show perry at rig3
            with long
            p "Back so soon?"
            i "They wanted to bet money. I can't afford that."
            p "Well done. Come drink some beer."
            i "Cindy can be a bit too competitive. I'm not feeling like putting up with that."
            e "I see. She's a funny girl."
            e "She seems to have a lot more energy than Wade, though..."
            "Emma, Perry and I continued drinking and chatting."
            "After the fourth round, I started to feel the alcohol clearly kicking in."
            p "Let's get another round."
            e "I'm fine, thanks."
            menu:
                "Enough for me, too":
                    $ renpy.block_rollback()
                    i "I'm set. Enough for me, too."
                    $ fperry = "mad"
                    p "That's so weak."
                    $ fperry = "meh"
                    p "Well, I'm gonna get another round for myself."
                    i "Suit yourself, just don't make me carry you home tonight."
                    p "When the hell has that ever happened?"
                    i "I don't want today to be the first time."
                    p "Whatever."
                    $ fperry = "happy"
                    "Perry got his drink and we continued chatting while he gulped it down."
                    
                "I want another one!":
                    $ renpy.block_rollback()
                    $ v1_drunk = True
                    $ fian = "happy"
                    $ fperry  = "happy"
                    i "Another one for me!"
                    p "That's the spirit!"
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    $ ian_perry += 1
                    "We toasted and gulped down our fifth beer."
                    $ fian = "smile"
                    hide friend_up
            "After a while Wade and Cindy came back after finishing a couple of games of pool."
            $ fian = "smile"
            $ fperry = "happy"
            $ femma = "n"
            show perry at right5
            show ian at truecenter
            show emma at rig5
            with move
            $ fcindy = "flirt"
            $ fwade = "sad"
            show cindy2 at lef5
            show wade at left5
            with short
            e "Who won?"
            c "Me! Two to zero, nihil, nada!"
            w "You just got super lucky."
            c "You got destroyed!"
            $ fcindy = "n"
            $ fwade = "n"
            w "Whatever."
            jump v1barend
            
    scene v1_pool_bg
    show v1_pool_base
    show v1_pool_wade1
    show v1_pool_cindy1
    show v1_pool_ian1
    with long
    "We left the money on the table and took positions around the pool table."
    "I hoped I could get those bills right back into my pocket... Money was already tight as it was!"
    w "OK, let's do this."
    if v1_teamcindy:
        "We flipped a coin to see who would break and Wade won."
        w "OK, I'm starting."
        hide v1_pool_wade1
        show v1_pool_wade2
        with short
        play sound "sfx/cue.mp3"
        "Wade took the first shot, and two balls went into the pockets."
        i "Two down from the get go? You gotta be kidding me!"
        c "Wait, he sank a spotted ball and a striped one!"
        hide v1_pool_wade2
        show v1_pool_wade1 with short
        c "Don't you know the rules?"
        menu:
            "I know the rules":
                $ renpy.block_rollback()
                i "Yes. That means he gets to choose what balls he wants to play, spots or stripes."
                c "And it also means he potted one of our balls for us. Thanks!"
                w "It wasn't the best break, but whatever..."
                w "I'm going with spots."
                c "Stripes for us, then."
            "What does that mean?":
                $ renpy.block_rollback()
                i "What does that mean?"
                w "Dude, you really are clueless."
                w "I have to choose one, spots or stripes, and pot only those balls."
                w "Then I have to sink in all those balls to get to the eight-ball, then sink that in and win."
                i "Which one are you picking?"
                w "I'll go with spots."
                c "Stripes for us, then."
                c "At least he potted one of our balls for us. Thanks!"
                w "It wasn't the best break, but whatever..."
        c "My turn now."
        hide v1_pool_cindy1
        show v1_pool_cindy2
        with short
        play sound "sfx/cue.mp3"
        "Cindy took her shot and she sank the ball she was going for."
        c "Yes!"
        i "That was a really good shot."
        c "We get another shot. Come on, take it."
        hide v1_pool_cindy2
        show v1_pool_cindy1
        hide v1_pool_ian1
        show v1_pool_ian2
        with short
        i "Mhh, let's see..."
        "Cindy pointed at a ball."
        c "Try this one. It's a very easy one, you should be able to hit it even if you're not that good."
        "I tried to find a good angle. The shot seemed fairly straightforward..."
        w "Even you can't miss this one, dude."
        i "Shut up."
        "I wanted to play just to have fun, but I was already feeling the pressure with these two ..."
        "And there was money at stake!"
        menu:
            "Hit the ball carefully...":
                $ renpy.block_rollback()
                "I didn't want to mess up. A gentle stroke should be enough..."
                play sound "sfx/cue.mp3"
                "I hit the ball, and it rolled slowly into the right direction..."
                i "Come on..."
                "It stopped just at the edge of the pocket."
                i "You gotta be kidding me!"
                w "You need to put some pop into your strike, dude!"
                c "You hit it too softly... But it's OK, this ball is in the perfect position."
                c "I'll take care of it in the next round."
                w "Pool requires more determination, Ian."
            
            "Hit the ball following through" if ian_athletics > 0:
                $ renpy.block_rollback()
                $ v1_poolpoints += 1
                "I took aim, practiced my strike and..."
                play sound "sfx/cue.mp3"
                "I hit the ball with a determined thrust, just like I did when throwing a punch at the gym."
                i "It went in!"
                c "Great shot, Ian!"
                w "Well, there's no way anyone could fail such an easy shot! Don't get too excited."
                w "The merit is in sinking the difficult shots."
            
            "Hit the ball hard!":
                $ renpy.block_rollback()
                $ v1_poolpoints -= 1
                "I just went for it and put everything on my strike."
                play sound "sfx/cue.mp3"
                i "Oops!"
                "I hit the ball so hard it bounced off the table and onto the floor!"
                i "Damn..."
                c "Ian!"
                w "Ha ha, you are such a brute. And thanks to this foul now I get to place the cue-ball where I want for a perfect shot."
                c "You're giving him too much advantage!"
                i "Sorry, it's not like I did it on purpose!"
                w "Pool requires finesse..."
        hide v1_pool_ian2
        show v1_pool_ian1
        hide v1_pool_wade1
        show v1_pool_wade2
        with short
        w "Let me show you."
        play sound "sfx/cue.mp3"
        "Wade hit another ball and he scored again."
        w "That's how it's done!"
        hide v1_pool_cindy1
        show v1_pool_cindy2
        hide v1_pool_wade2
        show v1_pool_wade1
        with short
        c "Don't get too carried away..."
        if v1_poolpoints == 1:
            c "We're tied, but..."
            "Cindy got down on the ball, planned her shot..."
            play sound "sfx/cue.mp3"
            "And she sank the ball."
            c "We're taking the lead!"
            i "Nice!"
            w "Let's see for how long!"
        elif v1_poolpoints == 0:
            c "You might be winning, but..."
            "Cindy got down on the ball I had left at the edge of the pocket, planned her shot..."
            play sound "sfx/cue.mp3"
            "And she sank the ball."
            c "We're tied, now."
            i "Good job."
            w "Don't get so excited, that ball was practically in already."
        else:
            c "We can still turn this around..."
            "Cindy got down on the ball, planned her shot..."
            play sound "sfx/cue.mp3"
            "And she sank the ball."
            i "Nice shot!"
            w "I'm still in the lead, tough."
        hide v1_pool_cindy2
        show v1_pool_cindy1
        hide v1_pool_wade1
        show v1_pool_wade2
        with short
        play sound "sfx/cue.mp3"
        "We continued playing, sinking more balls."
        "It was my turn again."
        hide v1_pool_ian1
        show v1_pool_ian2
        hide v1_pool_wade2
        show v1_pool_wade1
        with short
        if v1_poolpoints == 1:
            c "Come on, Ian. We're in the lead, and I want us to keep it that way."
        elif v1_poolpoints == 0:
            c "Come on Ian, we're tied and can't let him take the lead."
        else:
            c "Come on Ian, we're behind... We need to close the distance with him."
        i "Let me try..."
        "This time the situation wasn't as straightforward as before."
        show v1_poolshot1 
        with short
        c "You should try to hit ball number ten and pot it in the top left pocket..."
        i "Ball eleven is kind of in the way..."
        c "Yeah... Is there a way you could hit it?"
        c "Though the clearest shot seems to be number ten..."
        c "Maybe you can try and hit the cue-ball at an angle..."
        w "Please, go ahead. I can't wait to see what happens, ha ha."
        "I tried to think on the best way to hit the cue ball."
        if ian_athletics > 0:
            "It didn't seem well aligned with ball number ten..."
        if ian_wits:
            "I had the feeling that striking it on the left could be a good idea, but why...?"
        i "I don't want to mess this up."
        call screen v1poolgame
        if v1_hitball == 1:
            $ renpy.block_rollback()
            $ v1_poolpoints +=2
            hide v1_poolshot1 
            show v1_poolshot1_left
            with short
            "I went with my gut feeling and hit the cue-ball on the left."
            "And the results were better than I expected!"
            "The cue-ball hit ball number eleven and bounced to hit number ten, my original goal."
            "And I sank both of them at the same time!"
            hide v1_poolshot1_left
            with short
            w "What the fuck?"
            "Cindy jumped, full of excitement."
            c "What an awesome shot, Ian!"
            w "You have no idea how you did that."
            i "It went just as I had planned it, heh heh."
        
        elif v1_hitball == 2:
            $ renpy.block_rollback()
            if v1_poolpoints > 0:
                $ v1_poolpoints -= 1
            hide v1_poolshot1 
            show v1_poolshot1_center
            with short
            "I hit the cue-ball at its center."
            "It was a good strike, but unfortunately the trajectory was all wrong."
            "The cue-ball bounced on the table and cleared ball number ten, leaving it in a worse position than it was before..."
            hide v1_poolshot1_center
            with short
            c "No! What are you doing?"
            i "Sorry, it was a difficult shot!"
            w "Ha! Noob. I got this..."
            
        elif v1_hitball == 3:
            $ renpy.block_rollback()
            $ v1_poolpoints +=1
            hide v1_poolshot1 
            show v1_poolshot1_right
            with short
            "Hitting the cue-ball on the center seemed like a bad idea, so I chose right."
            "I had a crazy idea that could work... and it did!"
            "The ball bounced on the table and ended up hitting ball eleven, potting it in."
            hide v1_poolshot1_right
            with short
            i "Score!"
            c "Nice shot, Ian!"
            w "You're not as bad as you made us think..."
            "That one went surprisingly well."
            
        if v1_poolpoints > 2:
            hide v1_pool_ian2
            show v1_pool_ian1
            hide v1_pool_cindy1
            show v1_pool_cindy2
            with short
            "We continued playing. Cindy and I were doing great."
            "Wade was too far behind to catch up with us."
            play sound "sfx/cue.mp3"
            "Cindy ended up sinking the eight-ball, granting us the victory."
            
        elif v1_poolpoints > 0:
            hide v1_pool_ian2
            show v1_pool_ian1
            hide v1_pool_wade1
            show v1_pool_wade2
            with short
            "The game was pretty close..."
            play sound "sfx/cue.mp3"
            "We sank the balls at an even pace. At one point it seemed Wade was about to take the lead..."
            hide v1_pool_wade2
            show v1_pool_wade1
            hide v1_pool_cindy1
            show v1_pool_cindy2
            with short
            c "Mhhh... I'm not sure about this."
            w "It's a pretty hard shot. Good luck with that."
            "Cindy looked at Wade."
            c "Come over here, baby. What do you think?"
            hide v1_pool_wade1
            show v1_pool_wade3
            with short
            w "Mhhh... I see..."
            c "Which ball would you hit?"
            w "I can't tell you. We're playing against each other."
            c "Aw, come on. I'm just undecided."
            w "Too bad."
            c "Well... It'll be too bad if someone has to sleep on the couch tonight."
            w "W--{w=0.2}what?"
            c "I mean, I'm just asking my boyfriend for his opinion. It's not like I'm asking you to play for me."
            c "But you won't even give me that... I thought you valued our relationship more than a silly game of pool."
            w "Well, I... I'd hit that one, trying to get it from the right..."
            c "Oh, I see."
            play sound "sfx/cue.mp3"
            "Cindy took the shot and potted the ball successfully."
            c "Yeah! I'm the best!"
            "After that, we took the lead and Cindy ended up sinking in the eight-ball, granting us the victory."
            
        else:
            hide v1_pool_ian2
            show v1_pool_ian1
            hide v1_pool_wade1
            show v1_pool_wade2
            with short
            "We continued playing, but I had messed up too much..."
            "Cindy and I were too far behind to catch up with Wade."
            play sound "sfx/cue.mp3"
            "He ended up sinking the eight-ball and beating us."
            
        scene rockbar
        show ian at rig3
        show cindy2
        show wade3 at lef3
        if v1_poolpoints > 0:
            $ fian = "smile"
            $ fcindy = "smile"
            $ fwade = "sad"
        else:
            $ fwade = "happy"
            $ fcindy = "mad"
            $ fian = "worried"
        with long
        if v1_poolpoints > 0:
            $ v1_poolcindywin = True
            c "We won!"
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_cindy += 1
            if v1_poolpoints > 2:
                c "You were amazing, Ian! That trick shot put us really ahead."
                w "He has no idea how he pulled that off."
                c "Well, he did, didn't he? Don't be so butthurt!"
                play sound "sfx/frienddown.mp3"
                show friend_down
                $ ian_wade -= 1
                w "I'm not, I'm just saying..."
            else:
                w "Well, you had a little help there..."
                c "Yeah, Ian was quite helpful! He played way better than we expected!"
                play sound "sfx/frienddown.mp3"
                show friend_down
                $ ian_wade -= 1
                w "I meant myself. I helped you."
                c "That wasn't helping. I just asked you a question."
                w "It was helping!"
            c "Whatever. Just pay up!"
            play sound "sfx/moneyup.mp3"
            show money_up
            $ ian_money += 2
            i "Awesome."
            "The bet had paid off."
            c "Great job, Ian."
            i "It's been a pleasure playing with you."
            c "You made the right choice siding with me."
            i "I knew we would win."
            w "Have you stopped celebrating? Come on, let's go back to the others..."            
        else:
            w "You lost."
            c "You don't have to say it. We know."
            "Cindy gave me a bitter look."
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_cindy -= 1
            i "Hey, don't look at me like that. I told you I wasn't good at this."
            c "Well, you made me lose money."
            i "It was your idea to make a bet!"
            i "Besides, your boyfriend is collecting the prize. I'm sure you'll get your money back, unlike me..."
            w "Money's for the winners. Losers will have to accept their humiliating defeat, ha ha."
            c "Hmpf!"
            c "This was disastrous. Let's go back to the others..."
            "Great, not only had I lost my money but I managed to get Cindy mad at me."
            "I should've stayed with Perry and Emma..."
        jump v1barend2
        
    elif v1_teamwade:
        "We flipped a coin to see who would break and we won."
        w "OK, I'm starting."
        hide v1_pool_wade1
        show v1_pool_wade2 
        with short
        play sound "sfx/cue.mp3"
        "Wade took the first shot, and two balls went into the pockets."
        i "Cool, two down from the get go!"
        c "Yeah, but you sank a spotted ball and a striped one!"
        hide v1_pool_wade2
        show v1_pool_wade1 
        with short
        c "Don't you know the rules?"
        menu:
            "I know the rules":
                $ renpy.block_rollback()
                i "That means we get to choose what balls we want to play, spots or stripes."
                c "And it also means you've sank one of my balls for me. Thanks!"
                w "It wasn't the best break, but whatever..."
            "What does that mean?":
                $ renpy.block_rollback()
                i "What does that mean?"
                w "Dude, you really are clueless."
                w "We have to choose one, spots or stripes, and potting only those balls."
                w "We have to sink in all those balls to get to the eight-ball, then sink that in and win."
                i "OK, so now we have to pick one of the two and play only those."
                w "Yeah."
                c "It also means you've sank one of my balls for me. Thanks!"
                w "It wasn't the best break, but whatever..."
        w "I'm picking stripes."
        c "Alright, then spots for me."
        w "I sank a ball, so I get another turn..."
        hide v1_pool_wade1
        show v1_pool_wade2
        with short
        play sound "sfx/cue.mp3"
        "Wade took another shot, but this time he didn't manage to sink any ball."
        c "Ha! Now let me show you how it's done."
        hide v1_pool_cindy1
        show v1_pool_cindy2
        hide v1_pool_wade2
        show v1_pool_wade1
        with short
        c "Let's see..."
        play sound "sfx/cue.mp3"
        "Cindy took her shot and she sank the ball she was going for."
        c "Yes! Now I'm in the lead, since you potted one of my balls earlier."
        w "It's too early to get so carried away."
        c "I just know I'm gonna win this..."
        "We continued playing, and now the turn was ours again."
        hide v1_pool_wade1
        show v1_pool_wade2
        hide v1_pool_cindy2
        show v1_pool_cindy1
        with short
        w "Wade took the cue and bent over the table, searching for an optimal target."
        menu:
            "Hey, it's my turn":
                $ renpy.block_rollback()
                i "Hey, it's my turn."
                hide v1_pool_wade2
                show v1_pool_wade1
                with short
                w "Huh?"
                i "It's my turn now. I haven't played yet."
                c "Yes, let him play."
                w "Well... OK."
                hide v1_pool_ian1
                show v1_pool_ian2
                with short
                w "See that ball over there? Go for it."
                w "It's a super easy shot. Please don't miss."
                i "I'll do my best."
                w "I don't want to lose, man."
                i "I don't either, so stop stressing me out!"
                "I wanted to play just to have fun, but I was already feeling the pressure with these two ..."
                "And there was money at stake!"
                menu:
                    "Hit the ball carefully...":
                        $ renpy.block_rollback()
                        "I didn't want to mess up. A gentle stroke should be enough..."
                        play sound "sfx/cue.mp3"
                        "I hit the ball, and it rolled slowly into the right direction..."
                        i "Come on..."
                        "It stopped just at the edge of the pocket."
                        i "You gotta be kidding me!"
                        c "You hit it way too softly!"
                        w "Fuck! You need to put some pop into your strike, dude!"
                        w "Well, it could be worse. This ball's as good as potted in that position."
                        w "I'll take care of it in the next round."
                        "Cindy seemed amused."
                        c "Pool requires more determination, guys."
                    
                    "Hit the ball following through" if ian_athletics > 0:
                        $ renpy.block_rollback()
                        $ v1_poolpoints += 1
                        "I took aim, practiced my strike and..."
                        play sound "sfx/cue.mp3"
                        "I hit the ball with a determined thrust, just like I did when throwing a punch at the gym."
                        i "It went in!"
                        w "Good shot, dude."
                        c "Beginner's luck."
                        w "Not even a noob could've failed that shot."
                        i "Hey, credit where credit's due."
                    
                    "Hit the ball hard!":
                        $ renpy.block_rollback()
                        $ v1_poolpoints -= 1
                        "I just went for it and put everything in my strike."
                        play sound "sfx/cue.mp3"
                        i "Oops!"
                        "I hit the ball so hard it bounced off the table and onto the floor!"
                        i "Damn..."
                        w "Dude!"
                        c "Ha ha, you are such a brute, Ian! And thanks to this foul now I get to place the cue-ball where I want for a perfect shot."
                        w "Dude, you're giving her too much advantage!"
                        i "Sorry, it's not like I did it on purpose!"
                        c "Pool requires finesse."
                
            "Let him play":
                $ renpy.block_rollback()
                $ v1_poolpoints += 1
                "In fact it was my turn, but I let Wade keep playing."
                "I wasn't sure about my abilities at all, and there was money at stake..."
                play sound "sfx/cue.mp3"
                w "Another one in!"
                c "Well, we're still tied!"
                w "Not for long."
                
        hide v1_pool_ian2
        show v1_pool_ian1
        hide v1_pool_ian2
        show v1_pool_ian1
        hide v1_pool_cindy1
        show v1_pool_cindy2
        with short
        c "My turn."
        play sound "sfx/cue.mp3"
        "Cindy hit another ball and she scored again."
        c "That's how it's done!"
        hide v1_pool_cindy2
        show v1_pool_cindy1
        hide v1_pool_wade1
        show v1_pool_wade2
        with short
        w "Don't get too carried away..."
        if v1_poolpoints == 1:
            w "We're tied, but..."
            "Wade got down on the ball, planned his shot..."
            play sound "sfx/cue.mp3"
            "And he sank the ball."
            w "We're taking the lead!"
            i "Nice!"
            c "Let's see for how long!"
        elif v1_poolpoints == 0:
            w "You might be winning, but..."
            "Wade got down on the ball I had left at the edge of the pocket, planned his shot..."
            play sound "sfx/cue.mp3"
            "And he sank the ball."
            w "We're tied, now."
            i "Good job."
            c "Don't get so excited, to me you just wasted a turn."
        else:
            w "We can still turn this around..."
            "Wade got down on the ball, planned his shot..."
            play sound "sfx/cue.mp3"
            "And he sank the ball."
            i "Nice shot!"
            c "I'm still in the lead, though."
        hide v1_pool_wade2
        show v1_pool_wade1
        hide v1_pool_cindy1
        show v1_pool_cindy2
        with short
        play sound "sfx/cue.mp3"
        "We continued playing, sinking more balls."
        "It was my turn again."
        hide v1_pool_cindy2
        show v1_pool_cindy1
        hide v1_pool_wade1
        show v1_pool_wade2
        with short
        w "Let's see..."
        if v1_poolpoints == 1:
            w "We're in the lead, and I want us to keep it that way..."
        elif v1_poolpoints == 0:
            w "We're tied and can't let her take the lead..."
        else:
            w "We're behind... We need to close the distance with her."
        "Seems like Wade was going to steal my turn again unless I said something."
        menu:
            "Hey, it's my turn again.":
                $ renpy.block_rollback()
                i "Hey, dude. It's my turn. Again."
                w "I don't know man, this one's a difficult shot."
                play sound "sfx/xp.mp3"
                show charisma_up
                $ ian_charisma_xp += 1
                call screen skillsup
                i "But I'm playing too. My money's at stake same as yours."
                w "..."
                w "Alright... I hope you know what you're doing."
                hide v1_pool_ian1
                show v1_pool_ian2
                hide v1_pool_wade2
                show v1_pool_wade1
                with short
                "Wade reluctantly gave up his spot to me and I aimed down my sights."
                "This time the situation was not as straightforward as before."
                show v1_poolshot1 
                with short
                w "You should try to hit ball number ten and pot it in the top left pocket..."
                i "Ball eleven is kind of in the way..."
                w "Yeah... Is there a way you could hit it?"
                w "Though the clearest shot seems to be number ten..."
                w "Maybe you can try and hit the cue-ball at an angle..."
                w "I don't know, I told you it was a difficult shot."
                c "I can't wait to see you mess up, ha ha."
                "I tried to think on the best way to hit the cue ball."
                if ian_athletics > 0:
                    "It didn't seem well aligned with ball number ten..."
                if ian_wits:
                    "I had the feeling that striking it on the left could be a good idea, but why...?"
                i "I don't want to mess this up."
                call screen v1poolgame
                if v1_hitball == 1:
                    $ renpy.block_rollback()
                    $ v1_poolpoints +=2
                    hide v1_poolshot1 
                    show v1_poolshot1_left
                    with short
                    "I went with my gut feeling and hit the cue-ball on the left."
                    "And the results were better than I expected!"
                    "The cue-ball hit ball number eleven and bounced to hit number ten, my original goal."
                    "And I sank both of them at the same time!"
                    hide v1_poolshot1_left
                    with short
                    c "What the hell?"
                    "Wade smiled and high-fived me."
                    w "Awesome shot, Ian!"
                    c "You have no idea how you did that."
                    i "It went just as I had planned it, heh heh."
                
                elif v1_hitball == 2:
                    $ renpy.block_rollback()
                    if v1_poolpoints > 0:
                        $ v1_poolpoints -= 1
                    hide v1_poolshot1 
                    show v1_poolshot1_center
                    with short
                    "I hit the cue-ball at its center."
                    "It was a good strike, but unfortunately the trajectory was all wrong."
                    "The cue-ball bounced on the table and cleared ball number ten, leaving it in a worse position than it was before..."
                    hide v1_poolshot1_center
                    with short
                    w "No, dude! What are you doing?"
                    i "Sorry, it was a difficult shot!"
                    c "Ha! I'm sorry guys, I got this..."
                    
                elif v1_hitball == 3:
                    $ renpy.block_rollback()
                    $ v1_poolpoints +=1
                    hide v1_poolshot1 
                    show v1_poolshot1_right
                    with short
                    "Hitting the cue-ball on the center seemed like a bad idea, so I chose right."
                    "I had a crazy idea that could work... and it did!"
                    "The ball bounced on the table and ended up hitting ball eleven, potting it in."
                    hide v1_poolshot1_right
                    with short
                    i "Score!"
                    w "Hey, nice shot, Ian!"
                    c "You're not as bad as you made us think..."
                    "That one went surprisingly well."
                
            "Let him play":
                $ renpy.block_rollback()
                "I didn't want to mess it up... I decided to let Wade continue playing."
                play sound "sfx/cue.mp3"
                "He took his shot, but this time he failed miserably."
                w "Fuck, no!"
                c "Ha ha ha! You messed up big time."
                w "Damn..."
                i "Dude, I thought you were good at this."
                w "I am! Everyone can make mistakes, alright?"
            
        if v1_poolpoints > 2:
            hide v1_pool_ian2
            show v1_pool_ian1
            hide v1_pool_wade1
            show v1_pool_wade2
            with short
            "We continued playing. Wade and I were doing great."
            "Cindy was too far behind to catch up with us."
            play sound "sfx/cue.mp3"
            "Wade ended up sinking the eight-ball, granting us the victory."
            
        elif v1_poolpoints > 0:
            hide v1_pool_ian2
            show v1_pool_ian1
            hide v1_pool_wade1
            show v1_pool_wade2
            with short
            "The game was pretty close..."
            play sound "sfx/cue.mp3"
            "We sank the balls at an even pace. At one point it seemed Cindy was about to take the lead..."
            hide v1_pool_wade2
            show v1_pool_wade1
            hide v1_pool_cindy1
            show v1_pool_cindy2
            with short
            c "Mhhh... I'm not sure about this."
            w "It's a pretty hard shot. Good luck with that."
            "Cindy looked at Wade."
            c "Come over here, baby. What do you think?"
            hide v1_pool_wade1
            show v1_pool_wade3
            with short
            w "Mhhh... I see..."
            c "Which ball would you hit?"
            w "I can't tell you. We're playing against each other."
            c "Aw, come on. I'm just undecided."
            w "Too bad."
            c "Well... It'll be too bad if someone has to sleep on the couch tonight."
            w "W--{w=0.2}what?"
            c "I mean, I'm just asking my boyfriend for his opinion. It's not like I'm asking you to play for me."
            c "But you won't even give me that... I thought you valued our relationship more than a silly game of pool."
            w "Well, I..."
            menu:
                "{image=icon_charisma.png}Hey, that's cheating" if ian_charisma > 1:
                    $ renpy.block_rollback()
                    $ v1_poolpoints += 1
                    i "Hey, that's cheating, Cindy."
                    c "How is that cheating?"
                    i "Well, you're openly coercing him to give you valuable information that will help you win."
                    c "It's just a doubt I have..."
                    i "Well, I'm sure you'd be pretty mad if I was the one asking."
                    c "No I wouldn't..."
                    i "Wade is my teammate, not yours, so you can't ask him. It's just common sense."
                    i "I wouldn't mind if we hadn't bet money, but we did... And it was your idea."
                    "Cindy looked at me, trying to find a counter argument, but she knew full well I was right."
                    hide v1_pool_wade3
                    show v1_pool_wade1
                    with short
                    c "Alright, it's not like I need that advice..."
                    "She aimed down her sights and took a decision."
                    play sound "sfx/cue.mp3"
                    "The wrong one."
                    "She didn't pocket any ball."
                    c "Shit..."
                    if v1_poolpoints > 2:
                        hide v1_pool_wade1
                        show v1_pool_wade2
                        hide v1_pool_cindy2
                        show v1_pool_cindy1
                        with short
                        "We had an edge and we used it."
                        "The game was almost ending, and we managed to stay in front of Cindy long enough."
                        play sound "sfx/cue.mp3"
                        "Wade managed to sink in the eight-ball, granting us the victory!"
                    else:
                        c "Doesn't matter. I'm winning still!"
                        "She was..."
                        "We continued playing, but Cindy was edging us..."
                        "In the end, we were unable to overcome the distance that separated us."
                        play sound "sfx/cue.mp3"
                        "She ended up sinking the eight-ball and beating us."
                    
                "Don't tell her, dude!":
                    $ renpy.block_rollback()
                    $ v1_poolpoints += 1
                    i "Don't tell her dude!"
                    c "Why shouldn't he tell me?"
                    i "Because that's cheating."
                    c "How's that cheating?"
                    i "It's obvious! You're trying to get help from him, but he's my teammate, not yours."
                    c "Well, he's my boyfriend, not yours."
                    i "Yeah, but right now we're playing a game and there's money at stake."
                    i "We're rivals."
                    w "He's right..."
                    hide v1_pool_wade3
                    show v1_pool_wade1
                    with short
                    play sound "sfx/frienddown.mp3"
                    show friend_down
                    $ ian_cindy -= 1
                    c "Well, fuck off you two, it's not like I need that advice."
                    "She aimed down her sights and took a decision."
                    play sound "sfx/cue.mp3"
                    "The wrong one."
                    "She didn't pocket any ball."
                    c "Shit..."
                    if v1_poolpoints > 2:
                        hide v1_pool_wade1
                        show v1_pool_wade2
                        hide v1_pool_cindy2
                        show v1_pool_cindy1
                        with short
                        "We had an edge and we used it."
                        "The game was almost ending, and we managed to stay in front of Cindy long enough."
                        play sound "sfx/cue.mp3"
                        "Wade managed to sink in the eight-ball, granting us the victory!"
                    else:
                        c "Doesn't matter. I'm winning still!"
                        "She was..."
                        "We continued playing, but Cindy was edging us..."
                        "In the end, we were unable to overcome the distance that separated us."
                        play sound "sfx/cue.mp3"
                        "She ended up sinking the eight-ball and beating us."
                    
                "Stay silent":
                    $ renpy.block_rollback()
                    "That was so dirty...!"
                    "But I understood Wade's predicament. She had him right were she wanted him..."
                    "In the end, he couldn't go against his girlfriend."
                    w "Well... I'd hit that one, trying to get it from the right..."
                    c "Oh, I see."
                    play sound "sfx/cue.mp3"
                    "Cindy took the shot and potted the ball successfully."
                    c "Yeah! I'm the best!"
                    w "You're welcome..."
                    "That was the final nail in our coffin."
                    "We continued playing, but Cindy was edging us..."
                    "In the end, we were unable to overcome the distance that separated us."
                    play sound "sfx/cue.mp3"
                    "She ended up sinking the eight-ball and beating us."
            
        else:
            hide v1_pool_ian2
            show v1_pool_ian1
            hide v1_pool_cindy1
            show v1_pool_cindy2
            with short
            "We continued playing, but we had messed up too much..."
            "Wade and I were too far behind to catch up to Cindy."
            play sound "sfx/cue.mp3"
            "She ended up sinking the eight-ball and beating us."
            
        scene rockbar
        show ian at rig3
        show cindy2
        show wade3 at lef3
        if v1_poolpoints > 2:
            $ fian = "smile"
            $ fcindy = "mad"
            $ fwade = "happy"
        else:
            $ fwade = "sad"
            $ fcindy = "flirt"
            $ fian = "worried"
        with long
        if v1_poolpoints > 2:
            $ v1_poolwadewin = True
            w "Yeah, we won!"
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_wade += 1
            w "We made a good team in the end, Ian!"
            c "You guys are unbelievably lucky!"
            w "It's not luck! We're just better than you are."
            i "I wasn't so bad after all, huh?"
            "Cindy gave me a bitter look."
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_cindy -= 1
            c "It's just a silly game, I don't know why you're so happy."
            i "Not so silly, since I'm cashing in!"
            play sound "sfx/moneyup.mp3"
            show money_up
            $ ian_money += 2
            i "Awesome."
            "The bet had paid off."
            w "Good job, dude."
            i "I knew we would win."
            c "Have you stopped celebrating? Come on, let's go back to the others..."            
        else:
            c "Ha! I win, I win!"
            c "I'm sorry, losers!"
            i "You're not sorry in the least bit."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_cindy += 1
            c "Ha ha, yeah, you're right."
            c "Sorry not sorry."
            c "And all the money goes to me!"
            "Damn... I would miss that money..."
            "Cindy was a sore loser, but an even worse winner. Now I had to bear her making fun of us."
            "I should've stayed with Perry and Emma..."
            "Well, at least she seemed happy..."
            w "This was disastrous.... I would've been better off playing by myself."
            i "Well, then don't invite me to play next time."
            w "Whatever... Let's go back to the others..."
        jump v1barend2
        
           
## FIGHT ############################################### ####################### ####################### #######################   
label v1barend2:
    
    scene rockbar
    $ fperry = "happy"
    $ fian = "smile"
    $ femma = "n"
    $ fcindy = "n"
    $ fwade = "n"
    show perry at right5
    show ian at truecenter
    show emma at rig5
    show cindy2 at lef5
    show wade at left5
    with long
    "We sat with Emma and Perry and finished our beers."
    "Seems like both of them had been having a good time chatting while we were gone."
    "They barely noticed us when we came back."
    "After a short while, Wade got up again."
    jump v1barend
    
label v1barend:
    
    w "Guys, we're gonna get going."
    p "So soon?"
    w "It's pretty late, dude."
    i "Let's do this again soon!"
    c "I agree, it's been a fun night!"
    e "Yes, I promise to keep more in touch now. My life's not as chaotic now that I moved to a more normal flat!"
    w "Cool. See you soon, then."
    c "Bye!"
    hide cindy2
    hide cindy
    hide wade2
    hide wade
    hide perry2
    $ fian = "smile"
    $ fperry = "n"
    $ femma = "n"
    show perry at right5
    with short
    show ian at lef3
    show emma at truecenter
    show perry at rig3
    with move
    p "Another round?"
    e "Not for me. I won't take long to get going, too."
    if v1_drunk:
        i "Another one for me."
        p "My man!"
        "I was in a good mood, probably because I was pretty drunk."
        "I wanted to keep going a bit more."
        "Perry brought me another drink, we toasted and finished it before calling it a night." 
        i "OK, let's go."
        i "Oops!"
        "I lost my balance when I got up and had to lean on the table to avoid falling."
        e "Dude, you're pretty drunk! Ha ha."
        i "Just a bit."
        p "Amateur. You can't handle your booze."
        play sound "sfx/fall.mp3"
        hide perry
        $ femma = "smile"
        $ fian = "happy"
        with vpunch
        "Perry tried to get up, but he fell face first on the floor."
        p "Fuck!"
        i "Ha ha ha! You can handle it just right, can't you?"
    else:
        p "Ian?"
        $ fperry = "meh"
        i "I'm good, man. You've been drinking non stop the whole night."
        i "What's this, your sixth beer?"
        p "Who cares."
        "Perry got another beer and we waited for him to finish it to call it a night."
        i "OK, let's go."
        p "Let's."
        play sound "sfx/fall.mp3"
        hide perry
        $ femma = "smile"
        $ fian = "happy"
        with vpunch
        "Perry tried to get up, but he fell face first on the floor."
        p "Fuck!"
        i "Ha ha! Dude! Are you alright?"
    $ fperry = "mad"
    show perry2 at rig3
    with short
    p "Y--{w=0.5}yeah. Let's get outta here."
    stop music fadeout 2.0
    
    scene street2night
    $ fian = "smile"
    $ femma = "n"
    $ fperry = "n"
    show ian at lef3
    show emma
    show perry at rig3
    with long
    "The street in front of the bar was quite full of people, some smoking and chatting, some leaving just like us, some others just passing by."
    e "Well, it's been super nice to see you guys!"
    i "Let's do this again soon."
    e "I promise I'll keep more in touch."
    p "Bye, Emma."
    hide emma
    with short
    p "..."
    p "Ah, sh--{w=0.5}she's so nice."
    i "Let's go home."
    p "W--{w=0.5}wait, I need to pee."
    $ fian = "serious"
    i "Dude, why didn't you go before we left the bar?"
    $ fperry = "mad"
    p "C--{w=0.5}calm down, we're right at the door."
    p "I'll be q--{w=0.5}quick. Besides, I want to buy another beer for the walk back home."
    i "Dude, another one?"
    $ ian = "sad"
    hide perry
    with short
    i "You can't win with this guy..."
    if v1_drunk:
        i "Shit, I'm pretty drunk."
    else:
        i "..."
    "I looked around as I waited, just to pass the time, but then my heart stopped."
    scene street2night
    show v1_hookup
    with short
    "A couple was passionately making out in the corner."
    "The guy was groping her quite shamelessly and she was kissing him with fervor."
    "A redhead girl."
    "Was she...?"
    "My heart started racing. Gillian?"
    "No, it couldn't be. She was no longer in town."
    "But what if...?"
    "I didn't know what to do. But I had to make sure."
    "I got closer, trying to get a look at her."
    scene street2night
    $ fian = "worried"
    show ian
    with short
    i "It's not her..."
    "I let out a sigh of relief. It was not Gillian, just some random girl."
    $ fian = "depress"
    "But what would I have done if it had really been her?"
    "Walk away? Confront them?"
    "I suddenly felt like shit."
    "How could this be? How come that by simply seeing a girl that resembled my ex-girlfriend my heart raced like this?"
    $ fian = "depress"
    drunk "Get out of my fucking way, idiot!"
    "Sudden shouting made me turn my attention into the opposite direction."
    "There was a fight going on..."
    $ fian = "worried"
    show ian at lef3
    with move
    $ fian = "surprise"
    $ fperry = "sad"
    $ frobert = "mad"
    $ robert_splash = True
    $ robert_hurt = 1
    show perry at rig3
    show robert
    with short
    play music "music/danger.mp3" loop
    "And the one involved was Perry!"
    p "S--{w=0.5}sorry, dude."
    drunk "Watch your step, you four-eyed fuckwad!"
    $ fian = "worried"
    $ fperry = "meh"
    p "Chill, I already s--{w=0.5}said s--{w=0.5}sorry."
    drunk "You said s--{w=0.2}s--{w=0.2}s--{w=0.2}sorry? What good does that make?"
    drunk "You spilled all your fucking beer on my clothes!"
    p "I'm a vi--{w=0.5}victim too, that beer costed me money..."
    play sound "sfx/fall.mp3"
    hide perry
    with vpunch
    p "Hey!"
    "The dude pushed Perry violently, making him fall to the ground."
    menu:
        "Stay out of it":
            $ renpy.block_rollback()
            $ fian = "serious"
            "I decided to stay out of it."
            show ian at left
            with move
            "I was in no mood to get into a fight, and besides, Perry had brought that on himself."
            "I always told him he should go easy on the booze, because he usually turned into an obnoxious drunkard."
            $ fperry = "sad"
            show perry at rig3
            with short
            p "O--{w=0.5}OK dude, I want no trouble..."
            drunk "Then get yourself a new pair of glasses, because it's obvious that you're not seeing straight, idiot."
            $ fian = "sad"
            $ perry_glasses = False
            with vpunch
            "The guy snatched Perry's glasses, threw them to the floor and stomped on them."
            p "My g--{w=0.5}glasses!"
            drunk "Be thankful I'm not stomping your face! Look at my shirt, the mess you made..."
            drunk "Fuck!"
            hide robert
            with short
            "He pushed Perry aside once again and he left, cursing as he walked down the street."
            stop music fadeout 2.0
            p "..."
            $ fian = "sad"
            $ fperry = "sad"
            show ian at lef
            show perry at rig
            with move
            hide perry
            show perry2 at rig
            $ fperry = "mad"
            with short
            i "Hey, dude... What happened?"
            p "This fucking ass--{w=0.5}asshole, he was walking down the street, d--{w=0.5}drunk as a skunk, and he bumped into me..."
            p "T--{w=0.5}thanks for your help, by t--{w=0.5}the way."
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_perry -= 2
            i "Sorry man, I didn't know what was going on. And I didn't want to get my face punched in."
            p "Whatever, man. I j--{w=0.5}just don't want to talk about it."
            p "Let's just fucking go h--{w=0.5}home."
            jump v1draw
            
        "Intervene":
            $ renpy.block_rollback()
            $ v1_perry_help = True
            "I rushed to intervene."
            $ fian = "worried"
            show ian at lef
            show robert at rig3
            with move
            i "Hey, hey, hey!"
            i "Stop that!"
            drunk "What? You want some, too?"
            menu:                    
                "Chill out, dude":
                    $ renpy.block_rollback()
                    i "Chill out, dude."
                    drunk "Don't tell me to chill out! Have you seen what your friend has done?"
                    i "He's spilled his beer on you by accident. He didn't do it on purpose."
                    drunk "It's still his fault, he should've walked with his eyes open!"
                    drunk "Now I have to go back home wet and smelling of cheap fucking beer!"
                    jump v1_fighttalk
                    
                "Touch him again if you dare":
                    $ renpy.block_rollback()
                    $ fian = "mad"
                    i "Touch my friend again, if you dare, and you'll answer to me."
                    hide robert
                    show robertfight at rig3
                    with short
                    drunk "You don't scare me, wimp!"
                    jump v1_fight
            
        "Attack!":
            $ renpy.block_rollback()
            $ v1_perry_help = True
            $ fian = "mad"
            "My first instinct was to attack the guy!"
            play sound "sfx/punchgym.mp3"
            show ian at lef
            show robert at rig3
            with move
            with vpunch
            "I rushed to him and pushed him away from Perry."
            drunk "What the fuck?"
            hide robert
            show robertfight at rig3
            with short
            jump v1_fight
    

label v1_fight:
    stop music fadeout 1.0
    play music "music/fight.mp3" loop
    drunk "You want some of this!?"
    "As soon as the guy got into fighting position in front of me, I knew I was in some real trouble."
    "I had seen enough to notice that his boxing guard was no joke. That guy knew how to fight."
    "He was probably training boxing or some other contact sport..."
    "And looking at his face, it seemed like he had gotten into a fight recently."
    "He had some experience, that was for sure..."
    if ian_wits > 0:
        if v1_drunk:
            "I could see he was visibly drunk, but fuck, so was I..."
        else:
            "But I could see he was visibly drunk. Maybe that gave me an edge in this confrontation."
    elif v1_drunk:
        "And to make things worse, I was fucking drunk!"
    show robertfight at truecenter
    show ian at lef3
    with move
    "He moved closer to me, with clear intent of throwing a punch."
    "Fuck, was I really going to do this!?"
    $ renpy.block_rollback()
    $ timeout_label = "v1punchestimeout"
    menu:
        "Hey, stop!":
            $ renpy.block_rollback()
            $ v1_fight = True
            $ fian = "surprise"
            "I chickened out when I saw him raising his fist against me."
            i "Hey, dude, stop! Let's talk this out...!"
            drunk "Arghhh!"
            play sound "sfx/punch.mp3"
            scene street2night
            show v1_fight1
            with vpunch
            "He attacked without heeding my plea."
            "I put my arms up and tried to defend myself."
            "There was no backing down now, I had to fight!"
            if v1_drunk:
                "Unfortunately, I was too drunk to really know what the hell was going on."
                "I just flailed my arms around, trying to block his punches and hopefully landing a few of my own."
            else:
                "I blocked the shot and tried to hit him back, but he got all over me, flailing his arms, trying to hit me furiously."
                "I couldn't get any space to get a clean hit in!"
            guy "Fight! They're fighting!"
            jump v1punches
            
        "{image=icon_athletics.png}Punch him!" if ian_athletics > 0:
            $ renpy.block_rollback()
            "The best defense is a good offense!"
            i "Argh!"
            play sound "sfx/punch.mp3"
            scene street2night
            show v1_fight1
            with vpunch
            "I jumped on him and tried to get the first hit in."
            if v1_drunk:
                "Unfortunately, I was so drunk my punch completely missed."
                "He attacked back, and chaos ensued."
                "I was too drunk to really know what the hell was going on."
                "I just flailed my arms around, trying to block his punches and hopefully landing a few of my own."
            else:
                "My punch glanced him and he hit back. I'm not sure how, but I managed to block it."
                "I tried to hit him back, but he got all over me, flailing his arms, trying to hit me furiously."
                "I couldn't get any space to get a clean hit in!"
            guy "Fight! They're fighting!"
            jump v1punches
            
        "{image=icon_athletics.png}Low kick!" if v1_drunk == False and ian_lowkick:
            $ renpy.block_rollback()
            $ v1_fight_kick = True
            jump v1kicks
            
        "{image=icon_athletics.png}Close the distance!" if v1_drunk == False and ian_grappling:
            $ renpy.block_rollback()
            $ v1_fight_grappling = True
            jump v1closedistance
    

label v1punchestimeout:
    $ renpy.block_rollback()
    $ fian = "surprise"
    "I chickened out when I saw him raising his fist against me."
    i "Hey, dude, stop! Let's talk this out...!"
    drunk "Arghhh!"
    play sound "sfx/punch.mp3"
    scene street2night
    show v1_fight1
    with vpunch
    "He attacked without heeding my plea."
    "I put my arms up and tried to defend myself."
    "There was no backing down now, I had to fight!"
    if v1_drunk:
        "Unfortunately, I was too drunk to really know what the hell was going on."
        "I just flailed my arms around, trying to block his punches and hopefully landing a few of my own."
    else:
        "I blocked the shot and tried to hit him back, but he got all over me, flailing his arms, trying to hit me furiously."
        "I couldn't get any space to get a clean hit in!"
    guy "Fight! They're fighting!"
    jump v1punches

label v1punches:
    $ v1_fight = True
    play sound "sfx/punch.mp3"
    with vpunch
    "Blows started raining down and I did the only thing I could: hit him back recklessly as he did the same."
    girl "Somebody stop them!"
    "Some of the hits just glanced me or I didn't even feel them."
    play sound "sfx/punch.mp3"
    with vpunch
    i "Agh!"
    "I definitely felt that one. He got me right in the eye."
    "I gritted my teeth and threw a punch blindly, hoping to hit him with all the strength I could muster."
    play sound "sfx/punch.mp3"
    with vpunch
    drunk "Oof!"
    "A satisfying sense of impact and his grunt let me know that my punch had landed and hurt him."
    play sound "sfx/xp.mp3"
    show athletics_up
    $ ian_athletics_xp += 1
    call screen skillsup
    if v1_drunk:
        "We were just two drunkards flailing their arms and pulling on each other's shirts, trying to hurt one another, surrounded by entertained bystanders."
    else:
        "All technique and finesse went out the window as we threw haymakers and pulled on each other's shirts, trying to get a hold of one another, surrounded by entertained bystanders."
    "Fortunately, some of them had a conscience."
    girl "Enough!"
    guy "OK, stop guys! That's enough!"    
    $ v1_fight = True
    $ ian_hurt = 1
    $ robert_hurt = 2
    $ fian = "mad"
    scene street2night
    show robert at rig
    show ian at lef
    with short
    stop music fadeout 2.0
    "Several people got in between us and broke up the fight."
    show robert at right
    show ian at left
    with move
    drunk "Motherfucker, I'll kill you!"
    i "Come get some more if you're so brave!"
    "People drove us apart, de-escalating the situation."
    hide robert
    with short
    "They took that guy away, finally ending the conflict."
    $ fian = "serious"
    $ fperry = "sad"
    show perry at rig
    show ian at left
    with short
    p "D--{w=0.5}dude, are you OK?"
    show ian at lef
    with move
    i "Barely."
    p "Holy shit, that was in--{w=0.5}intense!"
    if v1_drunk:
        $ fian = "disgusted"
        i "Fuck, I'm getting all dizzy now. I feel I'm about to throw up."
        p "Let's go home so you can s--{w=0.5}sleep it off."
        p "And you need to put some ice on that eye..."
        i "Yeah..."
    else:
        i "Fuck, he got me right in the eye..."
        p "Let's go home and put some ice on it."
        i "Sure..."
    jump v1draw
         
label v1kicks:
    "I remembered what Wen had taught me yesterday. My body acted before I could really think it through."
    play sound "sfx/punch.mp3"
    scene street2night
    show v1_fight2
    with vpunch
    "I leaned to the side, avoiding the punch, and whipped out a low kick that caught him by surprise."
    drunk "Mphf!"
    scene street2night
    $ fian = "mad"
    show ian at lef
    show robertfight at rig    
    with short
    drunk "Motherfucker...!"
    drunk "Ahhh!"
    "He charged again, but I already knew how to counter him."
    play sound "sfx/punch.mp3"
    scene street2night
    show v1_fight2
    with vpunch
    drunk "Agh!"
    "This time I swayed back, avoiding his punch, and punished his leg again."
    scene street2night
    $ fian = "mad"
    show ian at lef
    show robertfight2 at rig
    with short
    "He lost his balance and stumbled on his leg."
    "That had really hurt him!"
    "I stepped in and kicked him again, putting all my body weight behind it."
    play sound "sfx/big_punch.mp3"
    scene street2night
    show v1_fight2
    with vpunch
    "I twisted my hips and slammed my shin into his bruised thigh, making him scream in pain."
    drunk "Aaaugh!"
    play sound "sfx/xp.mp3"
    show athletics_up
    $ ian_athletics_xp += 1
    call screen skillsup
    scene street2night
    show ian at lef
    show robertlose at rig
    with short
    stop music fadeout 2.0
    drunk "S--{w= 0.2}stop, dude! You win, you win!"
    "He stumbled back, limping on his leg, barely able to stand."
    "That last kick had really done the job."
    i "Get the fuck out of here."
    hide robertlose
    with short
    "He turned around and walked away, holding his leg and limping."
    $ fian = "worried"
    $ fperry = "happy"
    show ian at lef
    show perry at rig
    with short
    p "Dude, that was awesome!!"
    i "Holy shit, that was crazy."
    "Now that it was over, I felt the adrenaline dump take over my body."
    i "Fuck, I'm even shaking."
    p "You ki--{w= 0.5}ki--{w= 0.5}ki--{w= 0.5}kicked his ass!"
    i "I guess I did..."
    "Only at that moment did I become aware of the crowd of bystanders that had been watching our fight."
    $ fian = "serious"
    i "Dude, do you always need to get into trouble? I got in a fight because of you!"
    $ fperry = "meh"
    p "Because of me? He was the one who w--{w= 0.5}was not looking where he was going!"
    p "He b--{w= 0.5}bumped on me and made me drop my precious beer!"
    $ fperry = "n"
    p "But you k--{w= 0.5}kicked his ass. That was epic, I tell you."
    $ fian = "sad"
    "It was hard being mad, considering how things went."
    "It could've ended up badly, but I had been lucky."
    "And I felt quite the badass, to be honest..."
    i "Come on, let's go home before any more weird stuff happens."
    jump v1draw    
    
label v1closedistance:
    "I remembered what Wen had taught me yesterday. My body acted before I could really think it through."
    play sound "sfx/punchgym.mp3"
    scene street2night
    show v1_fight3
    with vpunch
    drunk "...!"
    "I avoided his punch and closed the distance like Wen had done with Jeremy."
    "I locked my hands and squeezed the guy with all my strength."
    drunk "What the fuck? Let go of me, man!"
    "He tried to get free, but I was keeping him tight to my body."
    play sound "sfx/xp.mp3"
    show athletics_up
    $ ian_athletics_xp += 1
    call screen skillsup
    "From that position he couldn't punch or kick me, but he was trying desperately to get loose."
    "He tried to knee me in the groin, but couldn't get the angle, hitting my thigh instead."
    "I squeezed as hard as I could, and though it was obvious I was hurting him, that wouldn't be enough to make him stop completely."
    "I had to reason with him."
    i "Dude, chill! Stop it!"
    drunk "Just fucking let me go, faggot!"
    "The bystanders had begun to form a crowd around us, entertained by our scuffle."
    i "I don't want to fight!"
    drunk "Stop hugging me motherfucker!"
    "He was just too drunk to be reasoned with."
    girl "Enough!"
    "Fortunately, bystanders took the chance to jump in and break the fight apart."
    stop music fadeout 2.0
    scene street2night
    show robertfight at rig
    $ fian = "mad"
    show ian at lef
    with short
    drunk "I'll fucking kill you, man!"
    guy "OK, stop guys! That's enough!"
    show robertfight at right
    show ian at left
    with move
    "He still wanted to fight, but a few people held him back."
    i "Get lost!"
    drunk "That was pathetic, hugging me like that! Who do you think I am, your fucking girlfriend?"
    drunk "You're so scared you got confused? Are you gonna pee your pants, too?"
    "I heard some of the bystanders laughing."
    drunk "Fight like a man!"
    i "I don't even wanna fight, just fucking leave!"
    hide robertfight
    show robert at right
    with short
    "He spat on the floor and flipped me the bird."
    drunk "You're not worth my time, loser."
    hide robert
    $ fian = "worried"
    with short
    show ian at lef
    with move
    $ fperry = "sad"
    show perry at rig
    with short
    p "Wow, t--{w= 0.5}that was intense...!"
    p "Are you hurt?"
    i "I'm alright... He just hit me in the thigh a bit. Tomorrow it'll be sore."
    "Now that it was over, I felt the adrenaline dump take over my body."
    i "Fuck, I'm even shaking."
    $ fian = "serious"
    i "Dude, do you always need to get into trouble? I got in a fight because of you!"
    $ fperry = "meh"
    p "Because of me? He was the one who w--{w= 0.5}was not looking where he was going!"
    p "He b--{w= 0.5}bumped on me and made me drop my precious beer!"
    i "Whatever... Let's get back home before anything else happens."
    $ fian = "sad"
    "Considering how things could've turned out, I considered myself lucky."
    "I had escaped unharmed from a fight... But it was hard not to feel like crap after how that thing went."
    "I should've tried to punch him at least, if I was getting into a fight."
    jump v1draw

label v1_fighttalk:
    
    menu:
        "He's my friend, leave him alone":
            $ renpy.block_rollback()
            $ fian = "serious"
            i "Look, I know my friend is drunk and probably he wasn't looking where he was going."
            i "But let's be honest, you probably weren't either. And he's my friend, so I can't let you do this to him."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            i "I'm sure you understand, you'd do the same for one of your friends."
            drunk "Where are you getting at? Are you saying I have to fight you to get to him?"
            drunk "Because I can take you both!"
            menu:
                "Look, we're sorry":
                    $ renpy.block_rollback()
                    $ renpy.block_rollback()
                    $ fian = "sad"
                    i "Look man, we're sorry."
                    i "My friend was having a good time, he got drunk and he bumped into you and spilled his beer."
                    i "And me... I don't even know what I'm apologizing for."
                    i "What more do you want?"
                    $ frobert = "serious"
                    drunk "Fuck, you're so pathetic I don't even want to kick your ass anymore."
                    drunk "You and your friend are a pair of losers that get their asses kicked by life on a daily basis."
                    drunk "Getting my hands dirty with trash like you is not even worth the thought."
                    drunk "Have fun with your pathetic lives, you wimps."
                    stop music fadeout 2.0
                    hide robert
                    with short
                    "After spouting all that, the guy spat on the floor and went on his way."
                    i "..."
                    $ fperry = "sad"
                    show perry at rig
                    with short
                    i "Hey, dude... Are you alright?"
                    p "Yeah... I don't know what hurt the most, him shoving me or those words he said."
                    i "Forget about him... He's just an angry drunk."
                    p "Well, isn't there a saying that goes: if you want to know the truth, ask a child or a drunk man?"
                    i "Just forget it. Let's go home..."
                    jump v1draw                    
                                
                "{image=icon_charisma.png}I get you, man" if ian_charisma > 0 and v1_drunk == False:
                    $ renpy.block_rollback()
                    $ v1_fight_charisma = True
                    $ fian = "n"
                    i "Look, I get you, man."
                    i "You look like you've had a rough night, or a rough week maybe, and so did I."
                    $ frobert = "serious"
                    i "I would get mad as fuck if some drunkard spilled his beer all over my clothes."
                    i "But this is only making things worse."
                    drunk "He should've apologized."
                    i "Of course he's sorry, it's not like he did it on purpose!"
                    i "But if you get in his face and shove him all of a sudden, it makes settling things peacefully difficult."
                    drunk "..."
                    i "He's my friend, and I know he has the ability to get on people's nerves easily. But he's a good guy, and I would like to spare him the trouble."
                    stop music fadeout 2.0
                    $ frobert = "n"
                    drunk "Well, you're his friend after all."
                    drunk "Sorry man, I'm just in a foul mood."
                    $ fian = "smile"
                    i "It's OK. Let's just shake hands and try to end the night on a lighter note."
                    i "We have enough drama in our lives as it is."
                    drunk "Sure."
                    "We shook hands and I sent him on his way."
                    i "Don't get in trouble before you get home!"
                    drunk "It's under control."
                    hide robert
                    $ fian = "worried"
                    with short
                    i "Whew..."
                    $ fperry = "meh"
                    show perry at rig
                    with short
                    p "How did you do that?"
                    i "Charisma, I guess."
                    p "What an ass--{w= 0.5}asshole..."
                    i "Can you stop getting into trouble, man?"
                    p "It was not my fault! I'm the v--{w= 0.5}victim here!"
                    i "You could've ended up much worse if it wasn't for me."
                    p "You really did turn it around..."
                    i "Come on, let's go before any more weird shit happens."
                    jump v1draw
                    
                "You should be the one to apologize":
                    $ renpy.block_rollback()
                    i "The way I see it, you should be the one to apologize."
                    i "Two drunks bumped into each other and one got unreasonably violent, and that's you."
                    drunk "The fuck I should apologize for? Are you stupid?"
                    drunk "You're the one who should apologize!"
                    play sound "sfx/punchgym.mp3"
                    $ fian = "mad"
                    show robert at rig
                    show ian at left
                    with vpunch
                    "He shoved me away violently, like he had done with Perry."
                    drunk "Say sorry right now!"
                    show ian at lef3
                    with move
                    i "Dude, you're pissing me off."
                    drunk "So? What you gonna do about it, tough guy?"
                    hide robert
                    show robertfight at rig
                    with short
                    "Shit, it was clear he was looking for a fight. And he had gotten himself one."
                    with short
                    jump v1_fight
            
        
        "You're being an asshole":
            $ renpy.block_rollback()
            $ fian = "serious"
            i "Dude, you're being an asshole about this."
            drunk "What did you say?"
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            i "It's just some beer. Sure, it's bothersome, but it's nothing the washing machine can't solve."
            drunk "Did you call me an asshole?"
            "Fuck... This guy couldn't be reasoned with."
            menu:
                "Look, we're sorry":
                    $ renpy.block_rollback()
                    $ renpy.block_rollback()
                    $ fian = "sad"
                    i "Look man, we're sorry."
                    i "My friend was having a good time, he got drunk and he bumped into you and spilled his beer."
                    i "And me... I don't even know what I'm apologizing for."
                    i "What more do you want?"
                    $ frobert = "serious"
                    drunk "Fuck, you're so pathetic I don't even want to kick your ass anymore."
                    drunk "You and your friend are a pair of losers that get their asses kicked by life on a daily basis."
                    drunk "Getting my hands dirty with trash like you is not even worth the thought."
                    drunk "Have fun with your pathetic lives, you wimps."
                    stop music fadeout 2.0
                    hide robert
                    with short
                    "After spouting all that, the guy spat on the floor and went on his way."
                    i "..."
                    $ fperry = "sad"
                    show perry at rig
                    with short
                    i "Hey, dude... Are you alright?"
                    p "Yeah... I don't know what hurt the most, him shoving me or those words he said."
                    i "Forget about him... He's just an angry drunk."
                    p "Well, isn't there a saying that goes: if you want to know the truth, ask a child or a drunk man?"
                    i "Just forget it. Let's go home..."
                    jump v1draw                    
                    
                "{image=icon_charisma.png}I get you, man" if ian_charisma > 1 and v1_drunk == False:
                    $ renpy.block_rollback()
                    $ v1_fight_charisma = True
                    $ fian = "n"
                    i "Look, I get you, man."
                    i "You look like you've had a rough night, or a rough week maybe, and so did I."
                    $ frobert = "serious"
                    i "I would get mad as fuck if some drunkard spilled his beer all over my clothes."
                    i "But this is only making things worse."
                    drunk "He should've apologized."
                    i "Of course he's sorry, it's not like he did it on purpose!"
                    i "But if you get in his face and shove him all of a sudden, it makes settling things peacefully difficult."
                    drunk "..."
                    i "He's my friend, and I know he has the ability to get on people's nerves easily. But he's a good guy, and I would like to spare him the trouble."
                    stop music fadeout 2.0
                    $ frobert = "n"
                    drunk "Well, you're his friend after all."
                    drunk "Sorry man, I'm just in a foul mood."
                    $ fian = "smile"
                    i "It's OK. Let's just shake hands and try to end the night on a lighter note."
                    i "We have enough drama in our lives as it is."
                    drunk "Sure."
                    "We shook hands and I sent him on his way."
                    i "Don't get in trouble before you get home!"
                    drunk "It's under control."
                    hide robert
                    $ fian = "worried"
                    with short
                    i "Whew..."
                    $ fperry = "meh"
                    show perry at rig
                    with short
                    p "How did you do that?"
                    i "Charisma, I guess."
                    p "What an ass--{w= 0.5}asshole..."
                    i "Can you stop getting into trouble, man?"
                    p "It was not my fault! I'm the v--{w= 0.5}victim here!"
                    i "You could've ended up much worse if it wasn't for me."
                    p "You really did turn it around..."
                    i "Come on, let's go before any more weird shit happens."
                    jump v1draw
                
                "You should be the one to apologize":
                    $ renpy.block_rollback()
                    i "The way I see it, you should be the one to apologize."
                    i "Two drunks bumped into each other and one got unreasonably violent, and that's you."
                    drunk "The fuck I should apologize for? Are you stupid?"
                    drunk "You're the one who should apologize!"
                    play sound "sfx/punchgym.mp3"
                    $ fian = "mad"
                    show robert at rig
                    show ian at left
                    with vpunch
                    "He shoved me away violently, like he had done with Perry."
                    drunk "Say sorry right now!"
                    show ian at lef3
                    with move
                    i "Dude, you're pissing me off."
                    drunk "So? What you gonna do about it, tough guy?"
                    hide robert
                    show robertfight at rig
                    with short
                    "Shit, it was clear he was looking for a fight. And he had gotten himself one."
                    with short
                    jump v1_fight
        
            
        "Shove him away!" if v1_drunk:
            $ renpy.block_rollback()
            $ fian = "mad"
            "That guy was a piece of shit and couldn't be reasoned with."
            "Maybe it was because I was drunk, but I couldn't find the patience to deal with this guy."
            i "Fuck it."
            play sound "sfx/punchgym.mp3"
            show robert at right
            with vpunch
            "I shoved him away violently, like he had done with Perry."
            drunk "What the fuck?"
            hide robert
            show robertfight at rig3
            with short
            jump v1_fight

## V1 DRAW ###################################################################################################################################################################################################################################### 

label v1draw:
    $ day = "Saturday"
    scene blackbg
    with long
    call screen calendar
    scene ianroom
    with long
    "I had no rush getting up the next morning."
    i "..."
    i "... ..."
    $ ian_look = 3
    show ianunder
    if v1_fight:
        $ ian_hurt = 1
    if v1_drunk:
        $ fian = "depress"
    else:
        $ fian = "n"
    with long
    i "What time is it...?"
    if v1_drunk:
        i "Damn... I drank a few too many beers last night."
        i "I'm a bit hungover..."
        "I got up, needing to drink some water."
    else:
        "I could stay in bed longer, but I was a bit restless."
        "I decided to get up."
    i "Mphf..."
    "Last night had been quite crazy. That fucking dude..."
    if v1_fight_kick:
        "I had been involved in my first real street fight. And I had won."
        "In pretty spectacular fashion, if I had to be honest."
        i "You just kicked a drunk guy. Don't flatter yourself too much..."
    elif v1_fight_grappling:
        "I had been involved in my first real street fight. I wasn't sure if I had won, though..."
        "I had escaped unharmed, at least."
        i "Well... My leg hurts a little... But at least he didn't punch me in the face."
    elif v1_fight_charisma:    
        "If I hadn't used my brain and my words, that would've ended in a street fight."
        "I had managed to diffuse the situation, but a part of me was left wondering what would have happened if we had fought."
        i "He would've given me a black eye or something, probably..."
        i "Best to avoid it."
    elif v1_fight:
        "I had been involved in my first real street fight. I knew I hadn't lost..."
        "But I didn't feel like the winner, that's for sure."
        i "I guess my performance was fucking lame... Far from one of those Hong Kong movies."
        "I touched my eye. It hurt."
        i "I hope this black eye goes away soon... I don't want everybody asking about it."
        i "Though I guess that's unavoidable..."
    elif v1_perry_help: 
        "I had avoided a fight and defended Perry. But a part of me wished we had just slugged it out."
        i "If we had fought he would've given me a black eye or something, probably..."
        "But somehow all those insults he spewed at the end felt as bad as having been punched in the face."
        "I felt like a coward..."
        i "No, better to just avoid a fight. Who knows what could've happened."
        i "I for sure didn't want to end the night at the hospital."
    else:
        "He had humiliated Perry to his heart's content."
        "It had been pretty violent... And I felt quite heartless for not having stepped in."
        i "I know Perry sometimes deserves it, but he's still my friend..."
        i "I should apologize."
    "I shook my head and tried to clear my head."
    "Before that, the night had been really fun."
    "It had been long since I had such a good night with my friends."
    scene ianroom
    $ ian_look = 2
    show ian
    with short
    "I got dressed and went to the kitchen to get some breakfast."
    play sound "sfx/door.mp3"
    scene ianhome
    show ian at lef
    $ fian = "n"
    with short
    "I found Perry was already up, sitting on the couch and drinking some coffee."

    $ fperry = "sad"
    show perry at rig
    with short
    i "Hey."
    p "Hey."
    i "You don't look so good. Hungover much?"
    p "A bit... Man, how many b--{w=0.5}beers did I have yesterday?"
    i "I don't know, like seven or eight? Maybe more."
    p "I'm getting weak."
    i "You're getting old."
    if v1_fight_kick or v1_fight_grappling or v1_fight_charisma:
        if v1_fight_kick:
            $ fperry = "happy"
            p "Maybe I should start training like you do, M--{w=0.5}Mr. Woodchopper!"
            i "Woodchopper?"
            p "Yeah, you chopped that guy's legs down! He deserved that so much."
            $ fian = "smile"
            i "That's a cool nickname, ha ha."
            i "I think it would be good for you to drop by the gym one day."
            i "Maybe you'll like it."
            $ fperry = "n"
            p "Nah, I absolutely doubt it."
            p "B--{w=0.5}by the way, I still haven't thanked you for yesterday..."
        elif v1_fight_grappling:
            $ fperry = "happy"
            p "Maybe I should start t--{w=0.5}training like you do, Mr. Care Bear!"
            i "Mr. Care Bear?"
            p "Yeah, you hugged that guy to a victory yesterday!"
            $ fian = "serious"
            i "Fuck you dude, I did that to save you."
            $ fian = "n"
            $ fperry = "n"
            p "I know, I was just joking... I owe you."
            p "I haven't thanked you yet for helping me..."
            $ fian = "smile"
        elif v1_fight_charisma:    
            $ fperry = "n"
            p "Where's that charisma you displayed y--{w=0.5}yesterday?"
            i "It's offline during mornings."
            p "I'm still amazed with how you t--{w=0.5}turned the situation around."
            p "That guy wanted to punch our faces in and you managed to give him a handshake and send him on his way."
            $ fian = "smile"
            i "The power of diplomacy."
            p "By the way, I still haven't thanked you for yesterday..."
        play sound "sfx/friendup.mp3"
        show friend_up
        $ ian_perry += 1
        p "If it weren't for you, that dude would've probably k--{w=0.5}killed me."
        i "Hey, that's what friends are for."
        p "I know I can be a bit of an asshole sometimes, especially when I'm drunk."
        i "Drunk or sober, I don't know if I can notice the difference, ha ha."
        p "Anyways, I just wanted to say t--{w=0.5}thanks for that."
        i "No worries. I got you."
    elif v1_fight:
        $ fperry = "meh"
        p "How's your eye, b--{w=0.5}by the way?"
        i "Black and swollen."
        p "Does it hurt?"
        i "No, not if I don't touch it."
        p "Last night was pretty intense, huh?"
        p "I know I haven't thanked you yet for saving my ass..."
        play sound "sfx/friendup.mp3"
        show friend_up
        $ ian_perry += 1
        p "If it weren't for you, that dude would've probably k--{w=0.5}killed me."
        i "Hey, that's what friends are for."
        p "I know I can be a bit of an asshole sometimes, especially when I'm drunk."
        p "I'm sorry you got a black eye because of me."
        i "It's OK. I guess I provoked him, too."
        p "Anyways, I just wanted to say t--{w=0.5}thanks for that."
        i "No worries. I got you."
    elif v1_perry_help: 
        $ fperry = "n"
        p "By the way, I wanted to say t--{w=0.5}thanks for yesterday."
        play sound "sfx/friendup.mp3"
        show friend_up
        $ ian_perry += 1
        p "If it weren't for you, that dude would've probably k--{w=0.5}killed me."
        i "Hey, that's what friends are for. I'm glad he didn't kill nobody."
        p "No, but it was a pretty shitty situation nonetheless."
        p "He got off on us, huh?"
        i "Yeah. Maybe we should've punched him."
        p "Maybe we could've ganged up on him. You distract him and I sock him from behind..."
        i "You wouldn't have done that."
        p "No, I guess not. But one can always imagine."
        p "Anyways, I just wanted to say t--{w=0.5}thanks for that."
        i "No worries. I got you."
    else:
        $ fian = "sad"
        i "Hey, by the way... Sorry about yesterday."
        $ fperry = "meh"
        i "I know I should've helped you or something, but..."
        menu:
            "{image=icon_wits.png}Sometimes you just deserve it" if ian_wits > 0:
                $ renpy.block_rollback()
                i "Dude, you deserve that sometimes, you know that?"
                p "..."
                i "I mean, I'm sorry, I should've done something, but I was scared too and I didn't want to end up in the hospital."
                p "I know it was my p--{w=0.5}problem, not yours..."
                i "If he had started to hit you I would've tried to stop him... But I was having a great night and I didn't want it to end like that."
                p "I know, I'm sorry."
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_perry += 1
                p "I know I can be an asshole sometimes, especially when I d--{w=0.5}drink too much."
                p "I didn't want to drag you into my problems, but it's not l--{w=0.5}like I had been searching for it. I just bumped into the f--{w=0.5}fucking guy."
                p "And a little help would've been nice, that's all."
                
            "I didn't want to end up in the hospital":
                $ renpy.block_rollback()
                i "I just didn't want to end up in the hospital."
                p "Nobody ended in the h--{w=0.5}hospital. Just my glasses. If there was a h--{w=0.5}hospital for glasses."
                i "Well, you never know with those kind of guys. He was super drunk..."
                p "So you wouldn't have minded if it had been me w--{w=0.5}who ended up in the hospital?"
                i "I didn't say that. If he had started to punch you I would've done something..."
                p "I'll have to t--{w=0.5}trust your word on that."
                
            "I was scared":
                $ renpy.block_rollback()
                i "I was scared. I didn't know what to do."
                p "T--{w=0.5}telling him to leave me alone would've been nice."
                p "But whatever, it was not that big of a deal in t--{w=0.5}the end."
                p "He just crushed my glasses and now I have to go b--{w=0.5}buy new ones, but that's it."
                i "Sure... OK."
                
    p "By the way..."
    p "There's this t--{w=0.5}thing a friend of mine told me."
    i "What thing?"
    p "This afternoon, at an art gallery close by."
    p "It seems they do drawing workshops, from time to t--{w=0.5}time."
    i "So you're going?"
    p "I wanted to, but I don't wanna go alone."
    $ fian = "n"
    i "I don't know man, I haven't drawn anything in years."
    p "Y--{w=0.5}you used to like it."
    i "And I also liked to play the bass, and I stopped doing that too. Writing's my thing."
    p "Anyways, I don't wanna go alone. And you could come."
    p "What's cool is that they have nude models posing in these workshops..."
    if ian_lust > 1:
        "The words \"nude models\" caught my attention."
        i "Tell me more..."
        $ fperry = "n"
        p "I knew you'd be interested."
    else:
        i "So what?"
        p "So what? Don't tell me you've never been c--{w=0.5}curious about that."
        i "I don't know."
    i "Those nude models could be grannies, as far as I know."
    p "No, my friend told me they always pick young and hot girls!"
    i "Are you sure it's an art gallery and not a sex shop or something?"
    p "I'm telling you what I know, dude!"
    p "Let's go c--{w=0.5}check it out, that way we can see for ourselves."
    i "I don't know..."
    p "You have nothing better t--{w=0.5}to do, anyways."
    i "I have to work on my book."
    p "Yeah, and are you going to do that?"
    i "..."
    i "Alright, let's go."
    $ fperry = "happy"
    p "Awesome."
    p "We should leave around five."
    i "OK. Now let me go get some breakfast."
    
    scene gallery2
    with long
    "Perry and I arrived at the gallery."
    $ ian_look = 1
    show ian at lef
    show perry at rig
        
    with short
    i "It's been long since I've been to a museum... I should come more often."
    p "We're not here to admire the paintings. We've come to admire other things..."
    i "You perv."
    p "Look who's talking. You're here, too, aren't you?"
    i "Because you asked me to come!"
    p "Shhh! Don't raise your voice. Come, let's get a spot."
    "They had set up some folding chairs around a podium for the assistants to sit."
    "Perry and I grabbed a wooden board, some paper and a few pencils."
    scene gallery2
    show v1_draw1
    if v1_fight:
        show v1_draw1_hurt
    with short
    "I took a seat and prepared the paper."
    "I hadn't drawn in quite some time... I had no idea if I would be able to do something that wouldn't utterly suck."
    i "I guess I'm just wasting my time..."
    "I had been doing that way too much lately. But what else was worth doing?"
    "While I was thinking about this stuff, the model stepped onto the podium."
    stop music fadeout 2.0
    scene gallery2
    show v1_draw2
    if v1_fight:
        show v1_draw2_hurt
    with short
    "I raised my eyes and what I saw left me perplexed."
    "Or should I say, \"who\" I saw."
    scene gallery2
    show v1_drawpose1
    with long
    pause 1
    if v1_name:
        "Lena."
    else:
        "The waitress."
    jump chapter_one_lena

label chapter_one_lena:   

##WEDNESDAY #####################################################################################################################################################################################################################
    $ timeout_label = None
    $ ian_active = False
    $ lena_active = True
    $ save_name = "Lena: Chapter One"
    
    $ day = "Wednesday"
    scene blackbg
    with long
    show active_lena
    with long
    pause 1.0  
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    "..."
    play sound "sfx/meow.mp3"
    pause (1)
    "... ..."
    show lola at lef
    with short
    "... ... ..."
    play sound "sfx/meow.mp3"
    pause (1)
    l "Ahhh, alright, alright..."
    $ flena = "worried"
    $ lena_look = 1
    show lenabra at rig
    with long
    $ lena_agenda = True
    $ lena_lola_agenda = True
    play music "music/normal_day.mp3" loop
    l "I'm getting up."
    l "Sometimes I really hate you, Lola."
    "I rubbed my eyes and sat on the bed for a second, trying to make my headache go away."
    play sound "sfx/purr.mp3"
    hide lola
    show lolahappy at lef
    "Lola jumped on the bed and rubbed herself against my thigh."
    l "I'm going, I'm going... Can you give me just a second?"
    "Last night at the restaurant had been a rough one. I came home late and had trouble sleeping."
    "And my lovely cat wouldn't let me sleep."
    "I finally got up and walked to the kitchen to feed her."
    play sound "sfx/door.mp3"
    scene lenahome
    show lenabra at rig3
    with long
    st "Oh."
    $ fstan = "blush"
    show stan at lef3
    with short
    st "G--{w=0.5}good morning, Lena."
    l "Good morning, Stan."
    $ lena_stan_agenda = True
    "My flatmate was already up, making breakfast."
    l "What time is it?"
    st "Ten o'clock."
    "So I had only slept like... five hours."
    l "Louise already left, right?"
    st "Yes, she leaves at half past eight every morning."
    l "We live together, but I barely get to see her... Our schedules are too different."
    "I grabbed Lola's food and poured some into her bowl."
    play sound "sfx/meow.mp3"
    show lola_b
    with short
    st "Um, say... Do you want me to make some breakfast for you, too?"
    menu:
        "That would be nice":
            $ renpy.block_rollback()
            $ flena = "smile"
            l "Oh, yes. That would be nice. Thank you, Stan."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ lena_stan += 1
            $ fstan = "shy"
            st "At your service."
            show lenabra at rig3
            
        "I don't want to bother you":
            $ renpy.block_rollback()
            $ flena = "n"
            l "Don't worry. I don't want to bother you."
            st "It's no bother, none at all."
            st "I'm already preparing mine, I can prepare yours, too..."
            st "I mean, it's barely any extra work on my part..."
            l "Well, if you insist I'll have to accept."
            $ fstan = "shy"
            st "Cool."
            
        "I'm not hungry and I need to go":
            $ renpy.block_rollback()
            l "No, it's not necessary. I'm not hungry."
            l "Besides, I need to get going soon."
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ lena_stan -= 1
            st "Uh... OK."
            l "I'm going to take a shower."
            hide lola_b
            hide stan
            with short
            "My head still hurt and I needed to clear it."
            "I had to be at work in just a couple of hours..."
            jump v1_workcafe
      
    "I took a seat on one of the stools as Lola ate her breakfast and Stan prepared mine."
    l "So, how's the job going?"
    st "Uh? Oh, it's going OK... Nothing new."
    l "You do everything from your room?"
    st "Almost everything, yeah. There's really no need for a computer engineer to go to an office."
    st "We can coordinate everything through the internet."
    l "I guess that's the future, huh?"
    "Stan served me a couple of toasts and a coffee."
    l "Thanks!"
    l "I wish I could work like that, too."
    st "It can get pretty boring sometimes, being in your room all day..."
    st "Though it doesn't particularly bother me..."
    l "I would go work at the park. Or at a nice cafe."
    l "Or I could even take my laptop and work while I'm traveling all around the world..."
    l "Sounds like a dream, doesn't it?"
    st "Yeah, I guess..."
    l "Anyway, I should go take a shower. I'm not so lucky, so I have to be at work in less than an hour."
    l "Thanks for the breakfast!"
    st "Anytime..."    
         
label v1_workcafe:
    
    scene street
    $ flena = "n"
    show lena
    with long
    "I hurried to the cafe. I was being late."
    "I had barely any time to do stuff during mornings, especially if I had worked night shifts the day before..."
    l "I'm in dire need of a bit of time for myself."
    l "But I'm also in dire need for money to pay the bills..."
    l "Luckily, I'm off this afternoon."
    "But first, I had to work."
    scene cafe
    show lena at rig
    with long
    "I arrived just in time."
    l "Good morning!"
    $ fmolly = "n"
    show molly at lef
    with short
    mo "Hello, Lena!"
    l "Sorry, I'm almost late."
    mo "Oh, you're just in time, so don't worry about it."
    l "I'll go change and I'll be ready in a minute."
    mo "Take it easy. You're a live wire!"
    "Ms. Van Dyke was really nice to me. She was a lovely woman."
    $ lena_molly_agenda = True
    hide lena
    show lenawork at rig
    with long
    l "Ready."
    mo "Well then you can set the tables while I finish making sure everything else is ready."
    l "Can do."
    hide molly
    with short
    show lenawork at truecenter
    with move
    "She had hired me three weeks ago, and this was one of the best jobs I remembered having."
    "I mean, I was just a waitress, but the mood of the place was pleasant."
    "I had had a few horrible bosses, but Ms. Van Dyke never pushed me or acted unfairly."
    "On the contrary, she was really generous and even asked me to take it easy..."
    "Too bad she and her husband couldn't afford to pay much."
    $ fed = "n"
    show ed at lef3
    with short
    ed "Hello Lena!"
    l "Oh, good morning Mr. Van Dyke!"
    $ lena_ed_agenda = True
    "He had gone shopping and was carrying two bags full of ingredients."
    l "Do you need my help carrying those bags to the kitchen?"
    ed "Ha ha, don't worry! I may be getting old, but I can still take care of this!"
    hide ed
    with short
    "He was as nice and welcoming as his wife."
    "They were a really adorable couple. They had been running this cozy café for some years, they owned the business and and despite their age they did everything themselves."
    "Molly prepared delicious cakes and pies while he took care of the kitchen. Mr Van Dyke prepared one of the best eggs Benedict I had ever tasted!"
    "They had no children of their own to help them with the business, so they finally decided to hire someone like me to that end."
    scene cafe
    with long
    pause (1)
    show lenawork at rig
    with short
    "The day's work went on as usual."
    "In only a couple more hours I would be free for the rest of the day."
    "I checked the tables to see if any of the clients needed service. There he was."
    $ ian_look = 1
    $ fian = "n"
    show ian at lef
    with short
    "I had noticed him the first time he came, like two weeks ago."
    "He always came with a book and a laptop to read, write and get disheartened."
    "It was fun seeing his expressions of frustration while he tried to work."
    "Not because I liked to see him suffer, but because it looked kind of cute."
    "He had finished up his coffee a while ago, so I decided to ask him if he wanted more."
    l "Do you want anything else?"
    i "Huh?"
    "He stared at me for a second, stunned, before reacting."
    pause 0.5
    i "Oh, sorry, yeah. Another latte, please."
    l "Coming right away."
    hide ian
    with short
    "I went to get him his latte while chuckling."
    "He had something about him that I liked. Some kind of charming clumsiness... Something I couldn't clearly describe."
    "But what I think really caught my eye was something you could only see if you looked at him carefully."
    "I could see a quiet sadness peeking through his eyes, some kind of melancholy weighing on them..."
    show ian at lef
    with short
    l "Here you go."
    i "Oh."
    i "Yeah, thanks."
    "He took his latte and returned his attention to his laptop. He seemed really focused."
    "I was curious about what he was doing. I peeked at the book lying on the table and I smiled."
    "Was he really reading a vampire romance novel for teenagers?"
    "I decided to play a little bit with him to see how he would react."
    $ flena = "smile"
    l "\"Fangs on my Neck\". Is it good?"
    "He looked up at me with that stunned expression once again, and I had to contain a chuckle."
    if v1_answer_cafe1:
        $ fian = "surprise"
        i "Oh, no, it's not the kind of book I usually read!"
        $ fian = "insecure"
        i "I mean, it's not something I read because I like it."
        $ flena = "happy"
        "I couldn't hold my chuckle in anymore. He looked so nervous, poor thing."
        l "That's funny."
        l "I've met a lot of people that hate to read. But not someone who reads something he actively hates."
        i "Believe me, I wouldn't read this if I could afford not to."
        $ flena = "n"
        l "So you have a reason to force yourself?"
    elif v1_answer_cafe2:
        i "Well... It's terrible."
        $ flena = "happy"
        "I chuckled at his honest and stoic answer."
        $ fian = "smile"
        "He seemed like a fun guy, so I tried teasing him a bit."
        l "I used to read these kind of books when I was like, twelve or thirteen. But I see they have an older audience, too."
        i "Please, don't be mistaken. I'm not reading this for my enjoyment!"
        l "You're not? What brings you to put yourself through such torture, then?"
    elif v1_answer_cafe3:
        $ fian = "worried"
        i "Euh, it's, eh... Passable."
        $ flena = "happy"
        "It was so hard holding in my chuckle. It was so obvious he was trying to be politically correct to avoid offending me by accident."
        "It made me want to tease him a bit more."
        l "Not bad, huh... Do you recommend it to me, then?"
        $ fian = "smile"
        i "It depends. Do you like poorly written stories that pander to a demographic too young to spot a cliché when they see it?"
        l "I don't think so."
        i "Well, then this book will surely disappoint you."
        $ flena = "happy"
        l "That's not a very good recommendation."
        $ fian = "worried"
        i "*{i}Sigh...{/i}* Yeah, I know. I guess I'm not very good at my job."
        $ flena = "n"
        l "What job?"  
        $ fian = "n"
    i "I'm doing an internship at a literature magazine, writing reviews on books and stuff."
    l "Really? That sounds cool."
    i "Not cool at all... I don't get to choose what to review."
    i "And the things I have to read... Well, don't get me started on those."
    l "Those reviews must be worth the read, ha ha."
    $ fian = "sad"
    i "If only...!"
    i "If I wrote what I really thought, they would fire me in a week."
    i "They don't want a review, they just want me to write propaganda so the book sells and the publishers are happy."
    $ flena = "n"
    l "That's pretty sad."
    if v1_answer_cafe4:
        $ fian = "serious"
        i "I'm really fed up with it, to be honest."
        i "They've turned me into an ill-paid salesman."
        "Oops, seems I had made him mad or something?"
        "That was not what I was going for... Better give him some space."
        play sound "sfx/frienddown.mp3"
        show friend_down
        $ ian_lena -= 1
        l "Damn, that's... tough."
        l "The book industry can be very frustrating! Good luck with that!"
        $ fian = "worried"
        i "Sure, thanks..."
        "I smiled politely, turned around and went to take care of another table."
        
    elif v1_answer_cafe5:
        $ fian = "n"
        i "Anyways, sorry. I didn't intend to vent."
        i "It's pretty boring, rather than sad."
        $ flena = "serious"
        l "No, I think it's really sad."
        l "And not only when books are concerned. In music, too."
        l "Publishers are hurting new voices and real artists by flooding the market with easy-to-sell crap."
        "Thinking about that made my blood boil. Why did people have to be like that?"
        "It affected many artists. Me among those."
        i "Yeah, it's a real curse..."
        $ flena = "n"
        "In the end it had been me who had started venting all of a sudden... I hoped he didn't think I was weird."
        l "Still, I think working in the book industry is very cool."
        l "I hope you can find a way to enjoy it!"
        "I smiled, turned around and went to take care of another table."
        
    elif v1_answer_cafe6:
        $ fian = "n"
        i "This is how the industry works, you know?"
        i "Publishers only want to earn money."
        i "They get a big name author to write about what's popular in pop culture..."
        i "And then they pay the magazines underhand to write good reviews that act as good publicity."
        "Apparently he was deep into the publishing world. He was probably frustrated, much like I was with the creative industry."
        $ flena = "serious"
        l "I see! It's the same as with the music industry."
        l "They push out the most commercial, soul-less and simple-minded products possible!"
        l "Publishers are hurting new voices and real artists by flooding the market with easy-to-sell crap."
        i "Yeah, it's a real curse..."
        $ flena = "shy"
        l "Sorry, I got a bit carried away, ha ha..."
        $ flena = "smile"
        "I had started to vent on him all of a sudden... I hoped he didn't think I was weird."
        l "Seems like we see eye to eye on this!"
        "I took a quick look over my shoulder. There was work to be done, but I was enjoying talking to this guy..."
        play sound "sfx/friendup.mp3"
        show friend_up
        $ ian_lena += 1
        l "Well, duty calls. I have work to do."
        l "Good luck with that!"
        i "Sure, thanks!"   
    hide ian
    $ flena = "n"
    with short
    "So he was working at a literature magazine... He was probably an aspiring author himself."
    "An interesting human being..."
    if v1_answer_cafe4:
        "Even if he had a bit of a weird temper."
    elif v1_answer_cafe6:
        "And he seemed pretty witty!"
    "I continued working and even served him a third latte, but I didn't want to disturb him. He looked really focused."
    "Half an hour later, he came to the counter to pay."
    $ fian = "n"
    show ian at lef
    with short
    i "How much is it?"
    l "Ten dollars and fifty cents."    
    if v1_name_charisma:
        i "Here you go. My name's Ian, by the way."
        l "Oh." 
        "I wasn't expecting him to introduce himself all of a sudden."
        "Maybe he was not as timid as I had initially thought."
        $ flena = "smile"
        l "I'm Lena, nice to meet you."
        i "Cool. The coffee was good, but I liked the conversation just as much."
        $ flena = "happy"
        "I couldn't help but smile when hearing that compliment. So sweet."
        "But I couldn't show him my weakness! I had to come back with something witty..."
        l "Better than the book you had to read, that's for sure!"
        $ fian = "happy"
        i "That's not hard to achieve at all, ha ha."
        i "Well, Lena, I guess I'll see you around then."
        l "I'll be here."
        i "See you!"
        hide ian
        $ flena = "n"
        with short
        "He waved his hand at me before getting out and going back home."
        l "Mhh... So his name's Ian..."
        l "He seems like a nice guy!"
        l "I'm glad I talked to him."
        
    elif v1_name_wits:
        i "Well, those are some expensive lattes."
        $ flena = "smile"
        l "Ha ha, blame yourself for liking fancy stuff."
        $ fian = "smile"
        i "Our economy's so bad that now a simple latte is considered fancy?"
        $ flena = "happy"
        "Was he trying to play me like I had played him before? Smart."
        "I smiled before voicing my comeback."
        l "If they are prepared with as much care and love as the ones I make, yes."
        i "So that's why today's lattes tasted better than usual."
        l "Come on, now you're just messing with me."
        i "Ha ha, yes, I definitely am."
        l "My name's Lena, by the way."
        "I was having fun with him. At this point of the conversation I thought it was appropriate to exchange names."
        i "Oh. I'm Ian. Nice to make your acquaintance."
        "He seemed to lose his cool a bit there. He was not expecting me to introduce myself?"
        l "So formal, ha ha."
        l "Nice to meet you too. I guess I'll be seeing you around?"
        i "Yeah, I come to this cafe from time to time."
        l "Till next time, then!"
        hide ian
        $ flena = "n"
        with short
        "He waved his hand at me before getting out and going back home."
        l "Mhh... So his name's Ian..."
        l "He seems like an interesting guy!"
        l "I'm glad I talked to him."
        
    else:
        i "Sure, here you go..."
        "He looked indecisive while handing me the money."
        l "Thank you very much."
        i "No, thank you."
        "He stepped back, ready to leave. I thought we would have a bit of banter before that..."
        l "Hope to see you again!"
        i "I will come some other time, yeah."
        i "Bye."
        hide ian
        with short
        "He gave me a last look and nodded his head before getting out and going back home."
        $ flena = "sad"
        l "Well, that was awkward..."
        "I had the impression we had clicked together quite well with our short, nice conversation, but maybe it had been only my impression..."
        l "Or maybe he's just really shy."
        l "I thought he'd ask my name, at least..."
        $ flena = "n"
        
    scene cafe
    with long
    "A bit later, Ms. Van Dyke informed me that my shift was over."
    show lenawork at rig
    show molly at lef
    with short
    mo "You're done for today, Lena. We can take care of things ourselves from this point!"
    l "Thank you so much, Ms. Van Dyke!"
    mo "You're making me feel old calling me Ms. Van Dyke all the time!"
    mo "Please, call me Molly."
    $ flena = "smile"
    l "Sure, Molly."
    l "I'm leaving, Mr. Van Dyke!"
    show ed at left
    with short
    "He popped his head out of the kitchen."
    ed "See you tomorrow, Lena!"
    stop music fadeout 2.0
    scene streetnight
    show lena2
    with long
    "I got changed and went to my next appointment."
    "I had to meet Ivy at the gym..."
    
## POLEDANCE #############################################################


    play music "music/jeremys_theme.mp3"
    scene polegym
    with long
    "I got changed and stepped into the studio."
    $ flena = "n"
    $ lena_look = 2
    show lena2 at rig
    with short
    "I took a moment to go speak with Ivy while the other girls were arriving."
    $ fivy = "n"
    $ ivy_look = 2
    show ivy at lef
    with long
    l "Hey."
    v "Lena! You came."
    $ flena = "smile"
    l "I told you I was not gonna miss class today."
    v "Well, you've missed plenty."
    l "Well, you know I'm..."
    v "Yes, yes, you're super busy with your two jobs."
    v "You need to do better, girl! Thankfully, you have me."
    v "I have to give you good news after the class."
    l "Good news?"
    "She winked at me."
    v "And good money."
    hide ivy
    $ fivy = "smile"
    show ivy2 at lef
    with short
    v "Girls, come on! Let's get the class started!"
    show ivy2 at left
    $ flena = "smile"
    show lena2 at right
    with move
    "Each one took position next to a pole and Ivy turned the music on."
    v "OK, follow me!"
    v "We're gonna start with our basic warm-up, then we're gonna refresh the moves we did on Monday!"
    $ lena_ivy_agenda = True
    scene polegym
    show v1_pole1
    with long
    "Ivy and I had been very close friends since high school."
    "We had lived through a lot together, all the drama and turmoil of out teenage years..."
    "Even though we had different personalities we understood each other very well. And we had more things in common than an outside observer could tell at first glance."
    "It was because of her that I was doing some of the stuff that I was doing..."
    "Lately it had been hard for us to meet as much as we used to, so I decided to join her classes at the pole dance studio."
    "She had landed the job a few months ago, and things seemed to be going well for her. I was glad."
    scene polegym
    with long
    "After forty-five minutes of intense exercise, Ivy clapped her hands and dismissed the class."
    $ fivy = "n"
    show ivy at left
    $ flena = "worried"
    show lena at right
    with short
    v "Good job, girls! I'll see most of you next Friday!"
    show ivy at lef
    show lena at rig
    with move
    l "Whew, pole dancing is such a tough workout!"
    v "Perfect to keep you fit!"
    l "I don't think I need that, considering how many hours I'm working already."
    l "Maybe I should find something relaxing to do in my spare time!"
    v "I don't get why you're still working at night at that restaurant. Especially since you got that cafe job recently."
    $ flena = "n"
    l "Easy. I need the money."
    $ fivy = "smile"
    v "Well, I need the money too, but I'm a bit smarter about it than you!"
    menu:
        "My area of expertise is different from yours":
            $ renpy.block_rollback()
            l "Let's just say my professional area of expertise is different from yours."
            $ fivy = "serious"
            v "Ugh, you and your fancy way of saying things!"
            play sound "sfx/xp.mp3"
            show wits_up
            $ lena_wits_xp += 1
            call screen skillsup
            $ fivy = "n"
            v "But tell me this, smart-ass:"
            v "Would you consider your area of expertise to be serving tables and making coffees?"
            $ flena = "sad"
            l "Uh, well..."
            v "See? I don't know why you're wasting your time with those things!"
            v "If you were clever you'd be doubling up in your job as a model."
            
        "I'm really glad for you":
            $ renpy.block_rollback()
            $ flena = "smile"
            l "Yes, I'm glad it's going well for you."
            l "You've always loved dancing and clubbing, so this and the gig at Blazer are perfect for you!"
            play sound "sfx/xp.mp3"
            show charisma_up
            $ lena_charisma_xp += 1
            call screen skillsup
            v "Well, you could do the same as I do!"
            l "Me, at the club? Oh, no thanks!"
            v "Not at the club, silly. I already know a bookworm like you would never be able to work there."
            v "I mean the modeling stuff."
        
        "If I was as hot as you I'd get better jobs":
            $ renpy.block_rollback()
            l "Well, if I was as hot as you I'd get better jobs!"
            hide ivy
            $ fivy = "smile"
            show ivy2 at lef
            "Ivy caressed her curvaceous hips in an overly sensual gesture."
            v "You envy this body? Ha ha ha!"
            play sound "sfx/xp.mp3"
            show lust_up
            $ lena_lust_xp += 1
            call screen skillsup
            v "But you wouldn't cut it working nights at the club."
            v "In fact, you aren't already doing it because you don't want to. You know I can get you in."
            l "Pass."
            v "I thought so. But serving tables and making coffees doesn't suit you at all either!"
            l "What else can I do? Not easy finding a job without a college degree."
            v "You don't need that to be a model!"
        
        "Well, I'm not dumb":
            $ renpy.block_rollback()
            l "Well, I'm not dumb?"
            v "Are you sure about that?"
            v "If you were clever you'd be doubling up in your modeling career!"
    
    v "Have you had any gigs recently?"
    l "In fact, yes. An art gallery contacted me to pose for some life-drawing sessions..."
    $ fivy = "serious"
    v "Life-drawing sessions?"
    l "Yeah, I pose for people to draw me. I've done it once and I'm going again this Saturday. It's an interesting experience..."
    v "Stop wasting your time. There's no money to be made there."
    $ fivy = "n"
    v "The business is in doing photo-shoots! There's good money and you use the pictures to promote yourself through social media."
    l "You know I'm not too fond of social media..."
    v "You're dumb! You have so much potential!"
    v "Photographers love working with you!"
    l "I guess I would need to get deeper into the business and get to know more of them..."
    $ fivy = "smile"
    v "Well, as I said, you have me."
    v "I've gotten you a photo-shoot with Danny! Ta-dah!"
    $ flena = "worried"
    l "Danny? Who's Danny?"
    v "Don't you remember him? Woody's friend, the photographer. You worked with him."
    l "I worked with Woody, but I haven't worked with no Danny..."
    v "Yeah, yeah, you worked with Woody, and Danny was the guy who came afterwards when we were drinking wine!"
    v "The one who said that he would like to take pictures of you so much! Remember?"
    l "Barely. We practically didn't talk, not even exchanged contact info."
    $ lena_danny_agenda = True
    v "Well, he was dying to work with you, so I set you two up. The photo-shoot's on Friday!"
    $ flena = "surprise"
    l "Wait, I work on Fridays!"
    v "You have a break during the afternoon, right?"
    l "But it's barely two and a half hours! It's not enough by any means."
    v "Well, I'm sure your boss will let you get off earlier if you ask her."
    menu:
        "You could've asked me before setting this up":
            $ renpy.block_rollback()
            $ flena = "serious"
            l "At least you could've asked me before setting this up."
            $ fivy = "serious"
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ lena_ivy -= 1
            v "I was expecting a thank you at least!"
            l "I mean, yeah, the extra money's always welcome but..."
            $ flena = "n"
            l "I just like to know of the plans that are made when I'm involved. To set up my week, at least."
            l "My life is chaotic enough as it is."
            $ fivy = "n"
    
        "I wish you had told me in advance":
            $ renpy.block_rollback()
            $ flena = "sad"
            l "I just wish you had told me in advance, to make plans."
            l "My life is already chaotic enough as it is."
            v "Well, I just set that up yesterday, so I'm letting you know pretty early all things considered!"
            $ flena = "n"
            l "Well, the extra money will surely be welcome."
            v "Yay! I knew you'd be happy about it!"
            
        "Thanks for getting me a photo-shoot":
            $ renpy.block_rollback()
            $ flena = "n"
            l "Well, in any case the extra money will surely be welcome."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ lena_ivy += 1
            v "Yay! I knew you'd be happy about it!"
            l "Thanks for helping me out."
            v "You know I like to take care of my best friend!"
            l "Though the timing spells trouble..."
    
    v "Come on, it's not a big deal."
    v "And I'm sure they'll let you leave earlier if you ask them tomorrow."
    l "I'll see what I can do."
    v "Cool. I'll send you the location later."    
    v "You should do more of this and less of serving tables!"
    v "That way you'd have more time for learning the pole. You're still a bit clumsy!"
    menu:
        "Give me a few tips":
            $ renpy.block_rollback()
            $ flena = "smile"
            l "Well, why don't you give me a few tips?"
            $ fivy = "smile"
            v "Wanna put in some extra minutes?"
            l "Please."
            v "OK, but only because it's for you."
            scene polegym
            show v1_pole1
            with long
            "I held onto the pole once again and started the routine Ivy had been teaching."
            v "You look like a bunch of bananas hanging from a palm tree."
            l "That's very unflattering."
            v "Use your legs, grip the pole with your thighs... And straighten your spine!"
            v "OK, that's more like it."
            play sound "sfx/xp.mp3"
            show athletics_up
            $ lena_athletics_xp += 1
            l "Oh, I see. I don't need to use so much arm strength to hold onto the pole like this."
            v "Am I a great teacher or what?"
            "I practiced for a few more minutes until I was satisfied."
            scene polegym
            $ fivy = "n"
            show ivy2 at lef
            $ flena = "n"
            show lena at rig
            with short
            stop music fadeout 2.0
            l "Thanks, now I get it."
            v "Hey, wanna see the routine I'm working on right now?"
            menu:
                "Sure, show me!":
                    $ renpy.block_rollback()
                    l "Sure, show me!"
                    play music "music/ivys_theme.mp3"
                    pause 1
                    scene polegym
                    show v1_pole2
                    with long
                    pause 1.5
                    "Ivy held onto the pole and lifted herself up like it was nothing."
                    "She flowed from one pose to the next effortlessly, all the while spinning around with elegance."
                    "She contorted her body, spreading her legs wide."
                    "Her shiny heels traced sensual arches around the pole while she maneuvered her body."
                    l "Wow."
                    "The gap in ability between us was made obvious by her sultry moves."
                    "She did everything without losing eye-contact or twisting her expression, locked into a flirty smile."
                    "I had no idea how she was achieving some of those poses, but she made it look easy."
                    play sound "sfx/xp.mp3"
                    show lust_up
                    $ lena_lust_xp += 1
                    "And sexy."
                    stop music fadeout 2.0
                    scene polegym
                    $ fivy = "smile"
                    show ivy at lef
                    $ flena = "happy"
                    show lena at rig
                    with long
                    v "So, how do you like it?"
                    l "It was amazing, Ivy! You've really become a pro."
                    v "Not by a long shot, but I can do pretty well."
                    l "I don't know what other feedback to give you, I think it was just perfect."
                    v "Good."
                    
                "I should get going":
                    $ renpy.block_rollback()
                    $ flena = "n"
                    l "Actually, I should get going."
                    $ fivy = "serious"
                    v "Oh. OK."
                    l "Besides, I can't give you any useful feedback! I'm nowhere near your level."
                    v "No, you're not..."
                    $ fivy = "n"
            v "Come on then, let's get going."
        
        "I'm not that bad":
            $ renpy.block_rollback()
            l "Hey, I'm not that bad."
            stop music fadeout 2.0
            v "Sure if you say so... What do I know, I'm just the teacher."
            v "Come on then, let's get going."
    
    $ gallery_scene1 = True
    scene streetnight
    with long
    "We took a shower and left the studio."
    $ lena_look = 1
    $ ivy_look = 1
    $ flena = "n"
    $ fivy = "n"
    show lena at rig
    show ivy at lef
    with short
    "I checked the time on my phone and saw a missed call."
    play sound "sfx/sms.mp3"
    "It was from Mom."
    "I sighed. I hadn't called her in a while."
    "It was about time I did..."
    v "So, how's your love life going?"
    $ flena = "worried"
    with vpunch
    l "What a question to ask out of the blue!"
    v "What? I care about you and I want to know what's going on in your life!"
    v "Any guys on your radar?"
    $ flena = "sad"
    l "Not really. I haven't been in the mood since what happened with Axel."
    v "But that was like three or four months ago!"
    l "Four months and one week."
    $ fivy = "surprise"
    v "See!?"
    $ fivy = "n"
    v "Come on, girl! It's been almost half a year now!"
    v "And you're telling me you haven't been in the mood for that long?"
    l "I've had other things to worry about..."
    v "How many guys could you have boned during all this time?"
    l "I don't want to \"bone\" anyone."
    $ fivy = "flirt"
    v "What about that guy you told me about, your co-worker from the restaurant?"
    l "Robert? Nothing's happened. "
    v "Why not? He seemed pretty interested from what you told me."
    l "I know he is, but it's just... I'm just not interested."
    "So many questions... I decided to change the subject."
    $ flena = "n"
    $ fivy = "n"
    l "Anyways, what about you?"
    v "Meh, you know, I'm not exactly looking for a boyfriend."
    l "But you said you wouldn't mind if you came across the right guy..."
    v "Yeah, but that hasn't happened. A relationship is too much trouble..."
    "It probably wasn't easy finding a stable boyfriend for someone with a lifestyle like Ivy's."
    "He'd need to be just like her, but with a dick instead of tits."
    v "I'm seeing a few guys, but nothing too serious to be honest."
    l "Well, if that works for you."
    v "Anyways! I miss you so much!"
    $ fivy = "sad"
    v "This is awful. We barely get to see each other lately!"
    v "Promise me you'll come next Monday."
    $ flena = "smile"
    l "I promise."
    $ fivy = "smile"
    v "You need to tell me about the photo-shoot and all that!"
    l "Don't worry, I will. See you then!"
    
## V1 LENA NIGHT HOME ######################################################################################################
    
    play sound "sfx/door_home.mp3"
    scene lenahomenight
    with long
    "I came back home in time for dinner."
    $ flena = "n"
    show lena at rig
    with short
    l "Ah, I love my free nights."
    $ fstan = "n"
    show stan at lef
    with short
    st "Oh, hey, Lena."
    "Stan was just finishing preparing his own dinner."
    l "That smells nice!"
    st "I just heated up some meatballs my mother gave me last time I visited her..."
    if lena_stan > 3:
        st "I left a few for you, if you want them."
        $ flena = "happy"
        l "You did that? Thank you, Stan."
        $ fstan = "perv"
        st "Y--{w=0.5}you're welcome."
        st "I'll go eat dinner... in my room."
        "He turned around and disappeared into his bedroom quite hastily for some reason."
    else:
        st "The kitchen's yours."
        l "Thanks, Stan."
        "He took his dinner and went back to his bedroom."
    play sound "sfx/door.mp3"
    hide stan
    with short
    "I didn't spend too much time at the flat all things considered, but Stan rarely left his room."
    "He did everything there, eat, work, play, sleep..."
    "I didn't feel like I was sharing a flat most of the time."
    if lena_stan > 3:
        l "Anyways, let's see if these meatballs taste as delicious as they smell..."
        scene lenahomenight
        with long
        "While the meatballs heated up in the microwave I changed into something more comfortable."
    else:
        l "Anyways, let's cook something..."
        scene lenahomenight
        with long
        "While the dinner cooked I changed into something more comfortable."
    $ flena = "n"
    show lenabra at rig
    with long
    "I got my dinner, accommodated myself on the couch, put on some music and proceeded to eat while I read a book."
    play sound "sfx/meow.mp3"
    show lola_b at right
    with short
    "Lola jumped on the couch too, curling up next to me. I petted her a bit."
    l "Hey Lola. Have you been lonely?"
    "Louise found me like this when she came back home."
    play sound "sfx/door_home.mp3"
    show louise2 at lef
    with long
    lo "I'm home."
    $ lena_louise_agenda = True
    l "Hey."
    lo "What are you doing? Reading and having dinner at the same time? And petting the cat, too?"
    l "Yup."
    lo "You can be really weird, you know?"
    l "Why? You wouldn't find it weird if I was watching TV. And this book's way more interesting."
    lo "I guess... But you don't have to hold the TV in one hand and the fork in the other one."
    if lena_stan > 3:
        "I stuffed my mouth with another one of Stan's mom's meatballs."
        l "Mhh... These are really good, you should try them!"
        lo "What are those?"
        l "Some meatballs Stan's mom prepared. He gave me a few."
        $ flouise = "sad"
        lo "And you're eating them?"
        l "Why shouldn't I?"
        lo "I don't know, aren't you afraid he..."
        "She lowered her voice."
        lo "That he slipped something weird into the food or something..."
        l "Are you hearing yourself? How can you think something like that?"
        lo "Hey, it happens more often than you'd think."
    else:
        lo "You're having dinner alone, I see."
        l "Yeah, Stan took his to his room."
        lo "Of course he did... He can't be outside his man-cave for more than fifteen minutes straight."
    lo "He's such a weird guy..."
    l "I thought you'd be used to him already. You've been living here far longer than I have."
    lo "I don't know if I'll ever get used to that weirdo."
    if lena_stan > 3:
        l "Come on, he's not that bad. I think he's actually nice."
    else:
        l "He doesn't bother me too much."
    $ flouise = "serious"
    lo "Really? Don't tell me you haven't noticed how he looks at you?"
    lo "I'm sure you've noticed his filthy stare all over your body, especially when you are dressed like that."
    l "I'm at home, I want to be comfortable!"
    lo "So do I, but I can't with him creeping about!"
    l "Shhh! He might hear you..."
    lo "Sorry, it just gets on my nerves. Maybe it's easier for you since you are not self-conscious at all about your body..."
    lo "Even Lola dislikes him."
    "Louise petted my cat."
    play sound "sfx/purr.mp3"
    hide lola_b
    show lolahappy_b at right
    l "Lola dislikes most guys, for some reason."
    lo "Thankfully he doesn't come out of his room often."
    l "By the way, where are you coming from this late on a Wednesday night?"
    $ flouise = "happy"
    lo "Let me drop my things and get comfortable too and I'll tell you right away!"
    hide louise2
    with short
    "I had met Louise at college, four years ago, and we quickly became good friends."
    "She was studying linguistics and literature, same as me. Unfortunately I had been forced to drop out two years ago..."
    "If that hadn't happened, I would probably be on my way to getting my master's degree, like Louise was."
    "I had been living on my own after breaking up with Axel, but I couldn't really afford it. I needed to find another place."
    "And it just so happened that the girl who had been living in this flat before me had just left."
    "Louise and Stan needed to find a new flatmate, and I decided to jump in as soon as Louise told me about it."
    $ flouise = "smile"
    $ louise_look = 2
    show louisebra at lef
    with short
    lo "OK, here I am."
    "She jumped onto the couch next to me. She looked really happy and excited."
    l "Don't tell me. It's about a guy."
    $ flouise = "happy"
    lo "Is it that obvious?"
    l "I know you enough to get what that smile is about! So you were with him right now?"
    lo "Yes, we went out for a quick dinner."
    l "So, how serious is it? If you're telling me about him, it must be important!"
    lo "Yeah, you know I don't like to talk about guys if I'm not sure things are going well..."
    lo "We've been seeing each other for about two months but I didn't wanna jinx it, so I didn't say anything..."
    lo "But well, now it's a done deal."
    l "He's your official boyfriend?"
    "She giggled with happy excitement."
    lo "Yes."
    $ flena = "happy"
    l "Congratulations!"
    lo "It was about time someone decent appeared in my life!"
    menu:
        "I'm really happy for you":
            $ renpy.block_rollback()
            l "I'm really happy for you. I know you have been wanting to find somebody for quite a while."
            lo "Yeah, but never had any luck. All the guys were assholes..."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ lena_louise += 1
            lo "But this one seems the one! Fingers crossed!"
            lo "But I feel he really likes me. It can probably grow into real, deep love..."
            lo "He's so different from me, though!"
            $ flouise = "n"
            $ flena = "n"
            
        "Does that mean I will be seeing even less of you?":
            $ renpy.block_rollback()
            $ flena = "sad"
            l "Does that mean I'll be seeing even less of you, though?"
            $ flouise = "n"
            lo "No, I hope not..."
            l "It's hard for us to spend time together, even though we're flatmates!"
            lo "Well, this master's degree is taking a ton of time... And you are always working!"
            lo "But I won't forget about my best friend just because I have a boyfriend now!"
            $ flena = "n"
            
        "You shouldn't get too carried away":
            $ renpy.block_rollback()
            $ v1_lena_louisecarriedaway = True
            $ flena = "n"
            l "You should try not to get too carried away, though."
            $ flouise = "serious"
            lo "What a mood-killer you are..."
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ lena_louise -= 1
            lo "I'm just trying to be happy here."
            l "Yes, and that's great, I'm just saying you should take it easy and not put down too many expectations in it."
            $ flouise = "n"
            lo "What I said, a total mood-killer."
                            
    lo "But enough talking about me."
    l "You still need to tell me more about him!"
    lo "Some other time. You know I'm not so fond of talking about my life all the time."
    lo "How about you? The new job's going good?"
    menu:
        "Tell Louise about your life":
            $ renpy.block_rollback()
            l "Yes, it's much better than the restaurant. And my boss is pure love."
            l "She is so nice she even tells me when it is time for me to go before I even do."
            lo "Unlike most bosses, who push you to work extra time. She sounds very motherly, yeah."
            l "Motherly, that's the word. She's almost the exact opposite of my Mom..."
            lo "Have you talked to her recently?"
            l "No... She called me while I was at the gym. I need to call her back."
            l "But I don't have the energy for it right now, to be honest."
            lo "In all honesty, I don't know where you get all that energy from. You work two jobs and take pole dancing lessons?"
            lo "And you've had to deal with so much shit..."
            l "Yeah. And I have a photo-shoot this Friday."
            lo "Oh, cool. Another thing I don't know how you manage to do."
            l "What? Posing?"
            lo "Yeah, posing butt-naked!"
            l "I just think it's not such a big deal. Everyone has a body. It's natural."
            lo "I'm not saying it's not natural, just that I would feel a bit creeped out being naked in front of a guy with a camera!"
            l "I only work with photographers whose style I like, the ones that do real art."
            l "It's not something vulgar at all. It's always in very good taste."
            lo "Still, I would feel quite uncomfortable, I think."
            "We chatted for a few more minutes until I felt my eyes starting to get heavy."
            "I had barely slept the night before."
            
        "Go to sleep":
            $ renpy.block_rollback()
            l "Yeah, everything's good. Not much to tell, to be honest."
            lo "I see."
            "I wasn't in the mood to talk much. I had barely slept the night before, after all."
    l "I'm a bit tired! I think I'll go to bed."
    lo "Sure. I won't stay up much longer either."
    l "Good night!"
    
    
## THURSDAY #####################################################################################################################################################################################################################
    $ day = "Thursday"
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    "..."
    play sound "sfx/meow.mp3"
    show lola at lef
    with short
    l "Ugh, you can be a real pain, you know that, Lola?" 
    $ flena = "n"
    show lenabra at rig
    with short
    "I got up to attend to my cat's demands. Luckily I had slept much better that night."
    "I felt refreshed and with enough energy to take on the day."    
    "I looked at my phone. I had two other missed calls from Mom."
    l "I guess I should call her..."
    "I couldn't find a good excuse to postpone it, so I decided to just do it and get it over with."
    hide lola
    with short
    show lenabra at truecenter
    with move
    l "Let's go. First thing in the morning..."
    hide lenabra
    show lenabra_phone
    with short
    l "..."
    show phone_mom_smile at lef3
    with short
    lm "Hello, honey!"
    l "Hi Mom. How are you doing?"
    lm "Fine, I'm fine. You're so hard to get on the phone, you know that?"
    l "I'm very busy lately, working two jobs and doing my thing..."
    l "Dad's OK?"
    lm "Yeah, he's still in remission."
    l "Are you making sure he takes things easy?"
    lm "You know him, he's stubborn as an ox, but I'm managing."
    l "Don't overwork yourself too much. You have the money from the bakery and what I'm sending you."
    hide phone_mom_smile
    show phone_mom_sad at lef3
    lm "You're the one who's overworking herself! You're working two jobs and even doing that modelling stuff just so you can help us financially..."
    lm "It should be the other way around..."
    l "You've spent a ton of money raising me. It's only fair I return the favour, at least until Dad's feeling better."
    lm "Still, I don't like having to depend on you... It should be the other way around."
    l "Anyways, how are things? Any news?"
    lm "Nothing much has happened, aside from that thing with uncle Troy."
    l "Uncle Troy? What happened to him?"
    lm "Oh, didn't I tell you?"
    lm "He died."
    $ flena = "surprise"
    l "Uncle Troy died!?"
    l "I used to play with him when I was a kid... And he'd always buy me my favorite chocolate when he came to visit us!"
    $ flena = "mad"
    l "How the hell did you forget to tell me something like that?"
    lm "I wouldn't have if you called more often!"
    l "When did this happen?"
    lm "I don't know, like a month ago..."
    $ flena = "sad"
    l "And you didn't even think about calling me and letting me know? At least I could've gone to his funeral!"
    hide phone_mom_smile
    show phone_mom at lef3
    lm "Well, you're always so busy... And it had been like two or three years since you last saw him."
    l "He's still my family."
    lm "That's what I always tell you, and yet you never call!"
    l "Look, forget it mom..."
    l "I'll call more often, alright?"
    lm "I hope so! Now tell me about you, honey. Are you taking care of yourself?"
    l "I'm doing fine. I've recently found a new job in a cafe, it's quite nice..."
    lm "You know your father and I are really worried about you. Being on your own like that..."
    l "I'm not on my own. I'm sharing a flat with a friend of mine and another guy."
    lm "It's so sad you broke up with Axel..."
    $ flena = "serious"
    l "Mom, stop."
    lm "I know relationships can be complicated and people make mistakes, but at least you had someone to take care of you..."
    l "I said stop. I don't wanna hear it again."
    lm "You made such a good couple. You should reconsider forgiving him..."
    $ flena = "mad"
    l "Gosh, what is it that you don't understand? I'm done with him!"
    l "And I don't want to talk about him! Even less if you defend him!"
    lm "I can't stand it when you get like this! Relax!"
    lm "I'm not defending him, I just want you to be happy, and you're not since you two broke up."
    l "We broke up for a reason, you know that. I don't want to keep discussing it."
    l "Bye."
    hide phone_mom
    hide lenabra_phone
    $ flena = "serious"
    show lenabra
    with vpunch
    $ lena_lenamom_agenda = True
    $ lena_lenadad_agenda = True
    "I hung up."
    "She always did the same. No wonder I avoided calling her as much as I did."
    l "Damn, now she's put me in a bad mood..."
    l "She always manages to do it!"
    "What a way to start my day..."
    l "I hope the day gets better from this point on!"
    "Little did I know what was about to happen..."
    
    play music "music/normal_day.mp3" loop
    scene cafe
    $ flena = "n"
    show lena2 at rig3
    with long
    "After taking a shower and having breakfast I went to work."
    l "Good morning!"
    $ fed = "n"
    show ed at lef3
    with short
    ed "Good morning, Lena!"
    "I noticed Molly was missing."
    l "Where's the boss?"
    ed "Oh, she's not coming today. She's feeling under the weather."
    $ flena = "worried"
    l "Really? She looked fine yesterday!"
    $ fed = "sad"
    ed "Yeah, she rarely tells people if she's not in good health, to avoid making them worried..."
    ed "She always works hard and puts so much effort into things, and always does it with a smile."
    ed "But I guess we're not young anymore!"
    l "Is it serious?"
    $ fed = "n"
    l "She shouldn't push herself so hard."
    ed "I've told her many times, but she doesn't know how to do things any other way."
    l "And still she puts others before herself... Yesterday she told me I should go home despite her feeling ill."
    l "I feel bad for having to ask this, now..."
    ed "Ask what?"
    l "Well, there's this thing tomorrow... A friend of mine got me a gig and I would need to leave a bit earlier..."
    $ fed = "sad"
    ed "Oh..."
    l "I know it's problematic, since Molly is ill..."
    ed "A bit, yeah... May I ask what is this gig is that you mentioned?"
    $ flena = "blush"
    l "Um, well..."
    menu:
        "Tell the truth":
            $ renpy.block_rollback()
            $ v1_ed_truth = True
            l "I have a photo-shoot."
            $ fed = "surprise"
            ed "A photo-shoot? Like a model?"
            l "Yeah. It's something I do from time to time to get some extra money."
            $ fed = "smile"
            ed "Oh, I never knew! But it makes sense, since you're such a beautiful lass."
            ed "What kind of photos do you take?"
            l "Well, um, mostly artistic nudes."
            $ fed = "sad"
            ed "Oh. I see."
            $ fed = "n"
            ed "I was going to ask you if you could show me some pictures, but that would be totally inappropriate, ha ha."
            l "So, can I get off a bit earlier tomorrow?"
            ed "Oh, yeah. I must admit it's troublesome for me, since my wife's absent..."
            $ fed = "smile"
            ed "But I'm sure I can manage. It seems it's really important for you."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ lena_charisma_xp += 1
            call screen skillsup
            $ flena = "smile"
            l "I wouldn't ask if it wasn't. Thank you so much, Mr. Van Dyke."
            ed "Please, call me Ed. And don't mention it."            
            
        "Lie":
            $ renpy.block_rollback()
            $ flena = "worried"
            l "I, uh... I need to help a friend."
            "I would've facepalmed if I could."
            ed "Help with what?"
            l "He's playing at the music store and needs me to help him with some technical stuff."
            "That was such a weak excuse, but I couldn't come up with anything else on the spot."
            ed "I'm sure he can find somebody else who can help him."
            ed "I'm sorry Lena, but with Molly absent I need you here..."
            ed "Your shift doesn't end late, you'll probably be able to get there in time to help him before his gig starts, right?"
            l "I don't know... Maybe..."
            $ fed = "n"
            
    ed "Well, let's get to work."
    l "Alright."
    scene cafe
    show lenawork
    if v1_ed_truth:
        $ flena = "n"
    else:
        $ flena = "sad"
    with long
    "I got changed and began my shift."
    if v1_ed_truth:
        "Mr. Van Dyke was as nice as his wife. I had never had such understanding and sympathetic bosses."
        "I was glad I had gotten this job... Even though I felt bad for leaving him hanging while Molly was ill."
        "Sometimes Ivy really made things complicated for me..."
    else:
        "No wonder Mr. Van Dyke wouldn't let me go early, with such a pathetic pretext."
        "But for some reason I felt ashamed of telling him I was working as a model."
        "I guess I didn't want to mix that aspect of my life with work. It could be troublesome."
        "But now I'd need to find another excuse..."
    "As I worked, I thought about the guy I had met yesterday."
    if v1_name_wits or v1_name_charisma:
        "Ian."
    "We had a short conversation, but a rather nice one at that." 
    if v1_answer_cafe2:
        "Despite his shy look, he had some charisma about him."
        if v1_answer_cafe5:
            "And seemed to be quite witty, too!"   
        if v1_answer_cafe4:
            "Even if he got a bit frustrated at one point..." 
    elif v1_answer_cafe6:
        "He looked a bit shy, but he seemed to be quite witty."
        if v1_answer_cafe4:
            "Even if he got a bit frustrated at one point..." 
    elif v1_answer_cafe4:
        "Even if he got a bit frustrated at one point..."        
    else:
        "He was a remarkable fellow."
    "I wondered if he would come by again today, but he didn't."
    stop music fadeout 2.0
    scene cafe 
    with long
    "My shift ended and I got ready to go to the restaurant."
    
    play music "music/fancy.mp3" loop
    $ ian_hurt = 0
    $ robert_hurt = 0
    $ robert_splash = False
    scene restaurant
    with long
    "I had been working at this restaurant for around four months now."
    "It was on the top floor of a five star hotel, and it was really fancy."
    "The pay was shitty, though."
    $ flena = "n"
    $ lena_look = 2
    show lenawork
    with long
    "I couldn't get by with just this job, so I had had to find me a second one."
    "I liked working at the café, but here... Let's just say it wasn't the best."
    show lenawork at rig
    with move
    $ robert_look = 2
    $ frobert = "n"
    show robert at lef
    with short
    r "Lena, have you finished cleaning the glasses?"
    l "Yeah."
    r "And have you prepared the wines?"
    l "Yup."
    r "Remember that today we're serving the special Dom Pérignon Rosé, don't get it mixed up with the regular one."
    l "I got it."
    "I doubted the clients would notice the difference. But hey, they liked feeling special."
    $ frobert = "smile"
    r "You're the best. It's a pleasure having an assistant like you."
    l "You know me, always trying my best."
    r "OK, let's get ready. Service's starting."
    hide robert
    with short
    "I worked five nights a week at the restaurant, and it was pretty chaotic, since I had no regular shifts."
    "It was a stressful job, with very demanding clients. But it had kept my mind occupied and put some money in my pockets."
    "As Ivy pointed out, this wasn't what I really wanted to do with my life. Not at all."
    "But I had to pay the bills. Rent, food... And help my parents."
    "Since Dad got diagnosed with cancer two years ago things had become tough."
    "He couldn't keep working anymore and had to sell the bakery to repay the loans... And I had to quit college to help pay for the treatment."
    "He had been on remission for almost a year now, but his health was not what it used to be."
    "Sometimes I felt trapped in a vicious circle, hoping to improve my situation but never really finding any opportunity..."
    $ frobert = "sad"
    show robert at lef
    with short
    r "Lena, how are you doing with your tables? Need some help?"
    "Robert came back after an hour or so, looking stressed out, like usual."
    l "So far, so good."
    r "OK, I need you to take care of VIP table number two. I'm barely able to handle all the other tables right now."
    "I wasn't short of work myself, but I couldn't refuse."
    l "Alright, I'll handle it."
    $ frobert = "smile"
    r "You're the best, have I told you already?"
    $ flena = "smile"
    l "Yeah, you did."
    r "You need to let me take you out for drinks to thank you for all the great work you do."
    "It wasn't the first time he proposed that. I hadn't taken him up on his offer yet..."
    l "Let's survive this week, first."
    $ lena_robert_agenda = True
    hide robert
    $ flena = "n"
    with short
    show lenawork at rig3
    with move
    "I picked up the menus and went to attend the VIP table."
    l "Good evening, welcome to Yunalesca Restaurant."
    l "May I recommend you our special Dom Pérignon..."
    stop music fadeout 2.0
    $ flena = "sad"
    $ fseymour = "n"
    $ faxel = "sad"
    show seymour at left
    show axel at centerlef
    with long
    "My voice failed me when I saw those blue eyes looking at me."
    x "Lena?"
    l "..."
    "I stood there, frozen like a statue for a few seconds. I didn't know what to do."
    l "I'm sorry."
    hide seymour
    hide axel
    with short
    show lenawork at right
    $ flena = "sad"
    with move
    "I turned around and walked away."
    "But he got up and followed me."
    show axel at centerlef
    with short
    x "Lena!"
    show axel at truecenter
    with move
    x "Lena, wait."
    $ flena = "mad"
    l "Don't talk to me."
    x "Wait, I haven't seen you in months, you blocked me and haven't returned my calls..."
    show axel at lef
    with move
    show axel
    "I pushed him away."
    l "Don't you think there's a reason for that?"
    x "Why don't you tell me?"
    l "I don't want to talk to you. That's the reason."
    x "Well, I do. You can't disappear on me like that..."
    l "Don't tell me what I can and can't do!"
    "Clients started to turn their heads, looking at us and wondering what was going on."
    $ flena = "worried"
    "I couldn't do this. Not here."
    show axel at truecenter
    with move
    "I turned around and tried to leave, but Axel held me back."
    $ flena = "mad"
    with vpunch
    l "Let go of me!"
    $ frobert = "serious"
    show robert at lef3
    $ flena = "worried"
    with short
    r "What's going on here?"
    "Axel turned around to look at Robert, distracted by him, and I used that opportunity to run away."
    hide robert
    hide axel
    with short
    $ flena = "worried"
    show lenawork at rig
    with move
    "I went to the back room, where only staff were allowed."
    l "Oh God..."
    "I felt my body trembling and my heart pounding in my chest."
    "Of all places, I had to stumble upon him here."
    play sound "sfx/door.mp3"
    $ frobert = "sad"
    show robert at lef
    with long
    "After a minute or so Robert came looking for me."
    r "What the hell was that about?"
    $ flena = "sad"
    l "It's... I'm sorry."
    l "He's my ex-boyfriend."
    $ lena_axel_agenda = True
    r "Oh. He is?"
    l "Yes..."
    r "I take it you're not too happy to see him?"
    l "Not at all. Things didn't end up well between us."
    r "I see... What are you gonna do?"
    l "I can't go back out there... Not with him there."
    r "Well, we can't kick him out."
    l "I know, I'm... I'm just gonna go home."
    r "That's a problem..."
    l "I can't work like this. He won't leave me alone."
    r "Of course, I get it..."
    $ frobert = "n"
    r "Look, let's do it this way."
    r "You get changed and go home... I'll put up a good word for you so the management doesn't get upset."
    r "But it's possible you'll get a pay cut for today, I don't know if I can help with that..."
    l "I don't care. I just wanna go home."
    r "Alright... Well, uh, take care."
    scene streetnight
    with long
    $ lena_look = 1
    $ flena = "sad"
    show lena
    with short
    "I left the restaurant without being noticed."
    "I wanted this to be a good day. Why did this have to happen?"
    "I thought I had put Axel behind me, but I guess I was just being naive..."
        
## FRIDAY #####################################################################################################################################################################################################################    
    $ day = "Friday"
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    $ flena = "sad"
    show lenabra
    with short
    "That night I didn't get much sleep."
    "My sudden encounter with Axel had left me shaken and anxious."
    "As Ivy said, it was almost half a year since we'd broken up, but I hadn't forgiven him."
    "And he hadn't given up on chasing after me, either..."
    "I didn't want to stay in bed stressing over those things, so I got up."
    "Today would be a long and intense day. At least it would keep me busy."
    if v1_ed_truth == False:
        "But I still hadn't found a way to get off work early..."
        "I hoped Molly would be back today, but I doubted that would be the case..."
    
    play music "music/normal_day.mp3" loop
    scene cafe
    $ flena = "n"
    show lena
    with long
    "I didn't want to stay at home and I ended up arriving at work a bit early."
    l "Good morning!"
    "Nobody answered."
    l "Mr. Van Dyke must be out shopping."    
    "I went to the backroom to get changed."
    hide lena
    with long
    $ lena_look = 2
    show lenabra
    with long
    "I got out of my clothes and I was about to put on my working outfit when somebody barged in unexpectedly."
    play sound "sfx/door.mp3"
    $ flena = "surprise"
    $ fed = "surprise"
    show ed at lef3
    with vpunch
    ed "Oh!"
    if v1_ed_truth:
        ed "Oh, sorry!"
        "He looked a bit flustered as he turned around and left the backroom."
        hide ed
        $ flena = "worried"
        with short
        l "It's OK, don't worry...!"
        
    else:
        "He looked at me with eyes and mouth wide open."
        ed "Oh, sorry!"
        menu:
            "Cover up":
                $ renpy.block_rollback()
                "I tried to cover myself out of instinct."
                "He looked flustered as he turned around and left the backroom."
                ed "I'm so sorry!"
                hide ed
                $ flena = "worried"
                with short
                l "It's OK, don't worry...!"
                
            "About leaving early today..." if v1_ed_truth == False:
                $ renpy.block_rollback()
                $ v1_ed_flirt = True
                "He was excusing himself, but his eyes were still glued to my body."
                "I instinctively knew that was the moment to strike."
                hide lenabra
                show lenabra2
                $ flena = "flirtshy"
                with short
                l "Um, excuse me, Mr. Van Dyke. I mean, Ed."
                $ fed = "sad"
                "He was about to leave the room, but he turned around and looked at me with caution."
                ed "Yes?"
                "I walked a few steps towards him."
                "I could feel how nervous it made him having me, just in my underwear, in front of him."
                l "About leaving a bit earlier today..."
                l "My friend really needs my help. He couldn't find anyone that could help him."
                ed "Is that so...?"
                "He sounded like he had a hard time focusing on the subject at hand. He seemed... distracted."
                l "Yes, and I would be so grateful to you if you'd let me off just a couple of hours earlier today to help him..."
                "He finally averted his eyes from me."
                l "Yes, just a couple of hours. I'll make up for it, I promise."
                ed "OK, OK. I understand it's important for you."
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
                l "Yay! Thank you so much!"
                l "Now let me finish getting changed and I'll get to work."
                ed "Of course."
                hide ed
                with short
                "I turned around and left."
                $ flena = "happy"
                l "Ha, got him!"
                "I finally managed to solve my problem. I could make it in time for the photo-shoot."
                $ flena = "n"
    
    hide lenabra
    hide lenabra2
    with long
    $ lena_look = 1
    show lenawork
    with long
    show lenawork at rig3
    with move
    $ fed = "n"
    show ed at lef3
    with short
    ed "Sorry about that, Lena. I didn't know you had arrived."
    if v1_ed_truth:
        l "It's nothing, don't worry about it."
        ed "I guess it's no big deal for you, since you are a nude model, huh?"
        l "Um... No big deal, no."
        ed "Good, good. Let's get everything ready, then."
    elif v1_ed_flirt:
        l "It's nothing, don't worry about it."
        ed "Let's get everything ready, then."
    else:
        l "It's OK, don't worry about it..."
        $ flena = "sad"
        l "But Mr. Van Dyke, I need to ask something of you..."
        ed "What is it, dear?"
        l "The friend I told you about yesterday has found somebody else to help him, but I have another problem."
        $ fed = "sad"
        l "You know my dad's health is not the best..."
        ed "Yes, my wife told me about it."
        l "So my mom also got sick, like Molly. And she needs me to take my Dad to chemotherapy..."
        l "So I still need to ask you to leave early, if that could be possible."
        l "I know it's bothersome since Molly's absent, but..."
        ed "Say no more. Family and health are the most important."
        ed "It will be just for today, so I'll manage."
        $ flena = "smile"
        play sound "sfx/xp.mp3"
        show wits_up
        $ lena_wits_xp += 1
        call screen skillsup
        l "Thank you so much, Mr. Van Dyke!"
        $ fed = "smile"
        ed "Don't mention it. And call me Ed, please."
        "I had had time to think of a better excuse. I felt bad using Dad's condition as an excuse, but I knew he wouldn't be able to refuse me this time."
        "I could make it in time for the photo-shoot."

    hide ed
    with long
    "Lunchtime came and I saw a familiar face walk into the café."
    $ ian_look = 1
    if v1_alisonlunch:
        $ fian = "smile"
        $ falison = "n"
        $ alison_look = 1
        show ian
        show alison at lef3
        with long
        if v1_name:
            "It was Ian. But he wasn't alone this time."
        else:
            "It was that boy. But he wasn't alone this time."
        "A tall, beautiful brunette was with him."
        $ flena = "smile"
        if v1_name:
            l "Welcome. Hi, Ian!"
            $ fian = "happy"
            i "Hello again."
            l "Having lunch today?"
            i "Yeah."
            l "Alright, take a seat over here."
            l "I'll be right back with the menu."
        else:
            l "Welcome. Hi again!"
            i "Hey... We've come for some lunch."
            $ flena = "n"
            l "Sure. Take a seat over here."
            l "I'll be right back with the menu."
            i "Thanks..."
        hide alison
        hide ian
        $ flena = "n"
        show lenawork at rig3
        with short
        if v1_name:
            "That girl seemed pretty close to Ian... The way she talked and smiled at him, and how close she was standing next to him..."
        else:
            "That girl seemed pretty close to him... The way she talked and smiled at him, and how close she was standing next to him..."
        "And he seemed to be enjoying her company very much, too."
        "She was probably his girlfriend..."
        "As I came back to their table with the menus, I overheard a bit of their conversation."
        $ fian = "happy"
        $ falison = "flirt"
        show ian
        show alison at lef3
        with short
        if v1_name:        
            a "Ohh, so that's why you wanted to come here?"
            $ fian = "insecure"
            i "No, that's not it... I like this place."
            i "I just talked with her once."
            a "Enough to know her name..."
        else:
            a "She's pretty cute... Do you know her?"
            $ fian = "insecure"
            i "No, not really."
            i "We just made some small talk the other day, that's all."
        $ fian = "n"
        $ falison = "n"
        l "Here's the menu. I'd recommend our eggs Benedict, they're delicious!"
        a "Thanks."
        "I took their orders and went back to Ed so he could cook them."
        hide ian
        hide alison
        $ flena = "sad"
        with short
        "I knew it... That girl was his girlfriend and she was demanding explanations on why I had greeted him in such a friendly way."
        "I hoped I hadn't gotten him in trouble..."
        "But looking at them, that didn't seem to be the case. They seemed to be having a great time, chatting and smiling."
        "Judging by the conversation I had with him the other day, I wouldn't have thought he'd have a girlfriend..."
        "I guess my intuition had failed me."
        "I didn't know why I cared about it, anyways. I had my own stuff to take care of."
        "When they were finished they came to pay at the counter."
        $ fian = "smile"
        show ian
        show alison at lef3
        show lenawork at rig3
        
        with short
        l "Did you like the food?"
        a "It was pretty good, yeah."
        i "Your recommendation was spot on."
        if v1_name_wits or v1_name_charisma:
            "I dispatched them quickly and politely."
            l "Glad to be of service. Have a nice day!"
            a "You too. Bye!"
            $ fian = "n"
            i "See you soon."
            l "Bye!"            
        else:
            "I dispatched them quickly and politely."
            l "Thank you. Have a good day!"
            a "Bye!"
            $ fian = "sad"
            i "Yeah, bye..."
        hide ian
        hide alison
        with long  
    else:
        $ fian = "smile"
        $ fholly = "n"
        show ian
        show holly at lef3
        with long
        if v1_name_wits or v1_name_charisma:
            "It was Ian. But he wasn't alone this time."
        else:
            "It was that boy. But he wasn't alone this time."
        "A short, cute girl was with him."
        if v1_name_wits or v1_name_charisma:
            l "Oh, hi Ian."
            i "Hey, hello again."
            i "How are you doing?"
        else:
            l "Oh, hello again."
            i "Hey... How are you doing?"
        l "Working hard, ha ha."
        i "We're going to give you a bit more trouble, then. We've come for some lunch."
        l "No trouble at all."
        l "Take a seat over here. I'll be right back with the menu."
        hide ian
        hide holly
        with short
        if v1_name_wits or v1_name_charisma:
            "The girl seemed so shy. She stayed quiet next to Ian the whole time."
        else:
            "The girl seemed so shy. She stayed quiet next to him the whole time."
        "Maybe she was his little sister?"
        show ian
        show holly at lef3
        with short
        l "Here's the menu, guys."
        l "I'd recommend our eggs Benedict, they're delicious!"
        i "Holly just told me the same thing before coming here."
        h "They're really good..."
        "I sent a reassuring smile her way."
        l "You have good taste."
        hide holly
        $ fholly = "shy"
        show holly3 at lef3
        with short
        h "T--{w=0.5}Thanks. You too."
        $ fholly = "blush"
        $ fian = "worried"
        $ flena = "worried"
        with short
        l "..."
        "She had blurted out quite an awkward reply."
        "The girl got flustered and her cheeks turned completely red."
        "Poor thing! She looked so shy and naive."
        $ fian = "smile"
        i "Did you know Holly is a professional writer?"
        $ flena = "smile"
        l "Really?"
        $ flena = "worried"
        $ fian = "worried"
        l "Wait..."
        "Now that he mentioned it, the girl's face looked familiar..."
        "I had seen her somewhere. Recently in fact."
        "It was in that amazing book..."
        $ flena = "surprise"
        l "You're Holly Watson?"
        l "The author of \"The Ice Flower\"?"
        h "Y--{w=0.5}Yes."
        $ flena = "happy"
        $ lena_holly_agenda = True
        "Wow, I couldn't believe it! How dumb I was not to figure it out just when I saw her?"
        "I had enjoyed reading her works a lot!"
        l "I love your books!"
        $ fholly = "n"
        i "So you know her?"
        l "Yes! I read your two books a few months ago and I was hooked."
        l "I knew we lived in the same city, but I can't believe you have been coming to this cafe all along."
        $ fian = "smile"
        i "It's such a coincidence. Holly and I work together at the magazine I told you about."
        l "That's cool. My name's Lena, by the way. I'm a fan."
        h "Nice to meet you, Lena."
        if v1_name_wits == False and v1_name_charisma == False:
            "I looked at the guy. I was fangirling over Holly and almost forgot about him for a second."
            l "Sorry, I still haven't asked your name..."
            i "I'm Ian."
            l "Cool. We finally can call each other by their actual names, ha ha."
        "I saw Ed signaling from the kitchen. Right, there was a lot of work to be done."
        l "Sorry, I have to take care of the other tables... And bring you your food!"
        i "Don't let us keep you."
        l "Maybe we can talk another time, when things are more calm."
        h "Sure... We come here often."
        l "I know."
        hide ian
        hide holly3
        $ flena = "smile"
        with short
        "So cool having fortuitously met the author of \"The Ice Flower\". It was a great book series and was gaining a lot of popularity."
        "Such bad luck not being able to talk to her right now, me and Ed being the only ones today at the café..."
        "But it seemed I would have the chance to do so some other time. She came here often, or so they said."
        if v1_name_wits == False and v1_name_charisma == False:
            $ v1_name = True
            "And I had also learned the boy's name. Ian."
            "I knew he had something interesting about him. He had to if he was close to a talented girl like Holly Watson."
        else:
            "I knew Ian had something interesting about him. He had to if he was close to a talented girl like Holly Watson."
        "When they were finished they came to pay at the counter."
        $ fian = "smile"
        $ fholly = "n"
        show ian
        show holly2 at lef3
        with short
        l "I hope you enjoyed the meal."
        i "Thanks for the recommendation. The eggs were amazing."
        l "Sorry to have bothered you before. I was just really surprised to learn who you really were, Holly."
        h "It's no bother at all... I'm so glad you liked my books."
        l "Maybe next time you can tell me a bit more about them? I have a few questions I would love to discuss directly with the author!"
        "Holly smiled at me."
        h "I would love that."
        if v1_name_wits or v1_name_charisma:
            "Then I turned to Ian."
            l "And we can keep discussing the sorry state of the book industry, Ian."
            i "Whenever you want."
        l "See you soon!"
        h "Bye!"
        hide ian
        hide holly2
        $ flena = "n"
        with short
        
    "Well, it was time for me to get ready for the photo-shoot..."
    $ fed = "smile"
    show ed at lef3
    with short
    l "Ed, I'm leaving. Is it alright?"
    ed "Yeah, go ahead. I'll take it from this point."
    l "Thank you! I'll make up for it, I promise."
    ed "Don't worry. Now go, don't be late!"
    stop music fadeout 2.0
    
## PHOTOSHOOT #################################################################################################################################################################################################################
    
    scene studio
    with long
    "Ivy had sent me the location of a photo studio that was for rent."
    "Photographers booked sessions there, where they had access to all kind of tools and materials for a few hours."    
    $ flena = "n"
    show lena2
    with long
    "This was where I had to meet Danny. He was waiting for me inside when I arrived."
    show lena2 at rig
    with move
    $ fdanny = "n"
    show danny at lef
    with long
    l "Hello!"
    dan "Oh, hi Lena! How are you doing?"
    "We kissed twice on the cheeks."
    l "Oh, you know, busy, working hard and stuff."
    dan "Still working at night at that restaurant? Ivy told me you had found a job at a café now."
    l "Well, yeah, I do both."
    "Him treating me like we were friends felt weird. I had to admit I barely even remembered anything about him."
    $ fdanny = "sad"
    dan "Wow, both at the same time? No wonder you're so busy!"
    $ fdanny = "smile"
    dan "Thank you for taking the time to work with me!"
    l "Thank you for giving me the chance."
    l "Shall we begin?"
    dan "Yeah, of course, whenever you feel comfortable."
    hide lena2
    show lenaunder at rig
    with long
    "I got into work mindset and did what I came here to do."
    "I started stripping down, baring my body for Danny's camera."
    dan "Must be hard working two waitressing jobs at once, huh?"
    l "It can get a bit tiresome, and shifts are a bit weird and not always fixed..."
    l "But it's OK."
    hide lenaunder
    show lenatopless at rig
    with long
    dan "So you're not working much as a model, then?"
    l "Not really, no... I've been too busy with other things."
    dan "It's a pity, you could earn well if you devoted more time to that! You're a wonderful model to work with."
    l "That's what Ivy tells me..."    
    hide lenatopless
    show lenanude2 at rig
    with long
    "The first time I had to strip like that in front of somebody I felt so uncomfortable."
    "Not that I was particularly shy, but the situation just felt weird."
    "Now I had gotten pretty used to it, though him talking to me all the time about my personal life made it a bit awkward."
    l "Done. Where do you want me?"
    dan "Here, in front of the backdrop... Yeah."
    l "Are you looking for something in particular?"
    dan "Right now I'm doing a series about posing and how it relates with the different art genres in model photography..."
    dan "And I thought you could perfectly represent the more sober and dignified style of high fashion."
    dan "Nobility, sensuality, but also youth and fragility."
    l "Um... OK."
    l "Let's see..."
    play music "music/sensual.mp3"
    scene studio
    show v1_pose1
    with long
    "I began with a very simple pose, something quite generic he could surely use."
    "I knew I had a beautiful backside that worked well in photography."
    dan "Oh, that's it! Exactly like that."
    dan "You got my idea perfectly!"
    play sound "sfx/camera.mp3"
    with flash
    "He began taking pictures."
    "Truth be told I hadn't figured out what his idea was exactly."
    "Dignified yet fragile? Sober and sensual?"
    dan "Now turn around, please..."
    scene studio
    show v1_pose2
    with long
    "I did as he asked, trying to find a new pose that he'd like."
    "Dignified but fragile. I covered my breasts while striking a sexy pose."
    dan "Excellent! That's beautiful..."
    "He searched for his optimal angle to shoot."
    play sound "sfx/camera.mp3"
    with flash
    dan "This one's really good!"
    play sound "sfx/camera.mp3"
    with flash
    "He seemed really happy with what I was giving him."
    "I had no real idea of what I was doing but he was loving it..."
    l "Let's go with this now..."
    scene studio
    show v1_pose3
    with long
    "With feline movements I laid on my side, relaxed but elegant, and held my stare directly into the camera."
    dan "Oh my God, yes, that's exactly it!"
    play sound "sfx/camera.mp3"
    with flash
    play sound "sfx/camera.mp3"
    with flash
    dan "I love the curve of your hip, and those eyes...!"
    "I was well aware of the power of the female stare, and I was quite good at using it."
    "Even though now I was playing the role of a nice girl, not overly assertive."
    dan "You look like a Cleopatra from the North..."
    dan "Oh, this is exactly what I was asking for. You're amazing."
    dan "Just one more..."
    play sound "sfx/camera.mp3"
    with flash
    dan "Let's try with a few more..."
    scene studio
    show v1_pose4
    with long
    "I was running out of ideas. I got an all fours trying to maintain the same mood as before."
    dan "Oh, you look beautiful... Let me see..."
    dan "Hmmm..."
    "He was struggling to find a good angle to shoot."
    dan "Hold it a bit longer... Maybe from here..."
    play sound "sfx/camera.mp3"
    with flash
    dan "OK, that'll do it."
    "We tried several more poses, as he searched for the perfect picture."
    "An hour or so later, when he was satisfied, he decided to call an end to the photo-shoot."
    scene studio
    $ fdanny = "smile"
    show danny at lef
    show lenanude2 at rig
    with long
    stop music fadeout 2.0
    dan "That was a wonderful photo-shoot Lena, best one of this whole project."
    l "Oh, thank you..."
    dan "I'm really happy with the pictures I got today."
    dan "The hard thing will be choosing the right ones..."
    dan "Do you want to check them out?"
    l "Of course, I want to see what we got."
    "He came closer and showed me his favorite pictures in his camera."
    dan "I love this one... And also this one... I don't know which one I should pick for the exhibition!"
    l "You're doing an expo?"
    dan "Yes, next week! This was the only set left to do. And I want it to be the centerpiece of the whole series!"
    l "Oh, wow."
    dan "That's why choosing this picture is so important... But I'm so in love with all of them my mind is cloudy!"
    dan "I trust your judgment. Which one do you think is best?"
    call screen v1chosepic
    if v1_choosepic == 1:
        l "I think this one's pretty good!"
        dan "This one, huh... Yeah, I guess it's a good one."
    if v1_choosepic == 2:
        l "I like this one a lot."
        dan "Yeah, this is one of my favorites, too!"
    if v1_choosepic == 3:
        l "I think this one's the best by far."
        dan "Hmm, I think so too! You have a really good eye!"
    if v1_choosepic == 4:
        l "I'd choose this one."
        dan "One of the last we did. Fair enough."
    dan "Thanks, Lena!"
    "After that I got dressed and ready to leave."
    scene studio
    $ fdanny = "n"
    show lena at rig
    show danny at lef
    with long
    dan "Well, it's been a real pleasure!"
    l "Same."
    dan "Here's your payment..."
    play sound "sfx/moneyup.mp3"
    show money_up
    $ lena_money += 1
    l "Awesome, thanks."
    dan "I hope we can work together more often!"
    dan "Oh, and by the way, you have to come to the expo's opening next week!"
    dan "Mine is not the only one opening, so it's bound to be full of photographers and other influential people in this industry."
    dan "You're an incredible model to work with, so I'm sure you'll find a ton of work there!"
    dan "Plus, you're the protagonist of my set. You can't miss it."
    l "When you put it like that I guess I really can't!"
    dan "Does that mean you'll be there?"
    $ flena = "smile"
    l "Yes, you can count on it."
    dan "Awesome! See you again next week then!"
    l "Bye, Danny."
    $ gallery_scene2 = True
    scene streetnight
    $ flena = "n"
    show lena
    with long
    
## V1 AXEL ########################################################################################################################################
    
    $ robert_look = 1
    "The photo-shoot had gone well. I was a bit nervous since I had never worked with Danny before, but he turned out to be pretty nice."
    l "Is he gay though, or is my radar broken?"
    l "I can't really tell."
    "And it seemed I was going to this opening next week. I had had no plans to do so, but..."
    "Danny was right. There I could meet interesting people if I wanted to do more photo-shoots."
    "I felt the bills that filled my pocket now."
    l "It sure is easy money... Way easier compared to my other jobs, that's for sure."
    "And now I had to clock into my job at the restaurant."
    "Being there was the last thing I wanted that day, considering what had happened last night. But work's work."
    $ frobert = "smile"
    show robert at rig3
    with short
    r "Hey, Lena."
    "I ran into Robert in front of the hotel just as we both arrived."
    r "How are you doing?"
    l "Well, you know... I'm good."
    l "By the way, I haven't thanked you for the other night. I was so upset I wasn't thinking straight."
    l "You offered to help me out and I didn't even say thanks. Sorry about that."
    r "Hey, don't worry, I'm just glad I could help..."
    "As we were going to get in, I noticed someone blocking the door."
    $ frobert = "sad"
    $ flena = "surprise"
    $ faxel = "sad"
    $ axel_look = 1
    show axel at lef3
    with long
    play music "music/danger.mp3" loop
    x "Lena."
    l "Axel!"
    $ flena = "mad"
    l "What the hell are you doing here?"
    x "Where else do you think I could find you? You won't answer my calls or messages."
    l "I told you the reason yesterday! And it's because I-{w=0.3}don't-{w=0.3}want-{w=0.3}to-{w=0.3}talk-{w=0.3}to-{w=0.3}you."
    $ faxel = "n"
    l "Have I made it clear this time?"
    x "Well, but I want to. And I need to."
    r "Dude, the lady has told you she doesn't want to speak to--"
    $ faxel = "furious"
    $ frobert = "sad"
    $ flena = "worried"
    with vpunch
    x "Nobody asked you anything, so shut the fuck up!!"
    r "Holy shit, dude...!"
    $ faxel = "mad"
    $ flena = "serious"
    "I faced him."
    l "Axel, get out of the door."
    x "Not until you agree to talk to me."
    l "I need to get to work and I don't want to talk to you. Step out of my way!"
    x "No. Not until you agree to talk to me."
    l "Get out!"
    play sound "sfx/punchgym.mp3"
    with vpunch
    "I tried pushing him, but he was much stronger and heavier than me, so he didn't even budge."
    $ frobert = "mad"
    "Robert saw how things were heating up and decided to step in."
    $ flena = "serious"
    show lena at rig3
    $ frobert = "mad"
    show robert at truecenter
    with move
    r "Hey dude, I don't know what your problem is but it's time you cut it off. Go the fuck away."
    x "I've told you to shut up. This is none of your concern."
    x "You shouldn't even be listening, so get going."
    r "Well, if you stepped out of the fucking door maybe we could!"
    play sound "sfx/punch.mp3"
    $ faxel = "furious"
    show axel at left
    with vpunch
    "Robert tried to push him away from the door. Big mistake."
    play sound "sfx/big_punch.mp3"
    pause 0.7
    $ flena = "surprise"
    show axel at lef3   
    hide robert
    with vpunch
    x "Get lost, clown!"
    "Axel punched him in the face to get him off himself."
    "The loud sound of bone hitting bone rang in my ears as Robert stumbled and fell to the floor."
    $ faxel = "mad"
    $ flena = "mad"
    l "Are you crazy!? What the hell are you doing!?"
    x "I told him to stop meddling!"
    l "You punched him, you crazy asshole!"
    $ faxel = "sad"
    x "That's because you won't talk to me!"
    x "I don't even know where you live now! I asked Ivy and you know what she told me?"
    x "That you had explicitly told her not to tell me if I asked!"
    l "You can surely understand why, seeing how you're behaving right now!"
    "Staff from the hotel rushed to the scene hearing the commotion."
    $ frobert = "sad"
    $ robert_hurt = 1
    show robert
    with short
    "Robert stumbled back to his feet, holding his face where the punch had landed."
    r "This motherfucker..."
    woman "What's going on here?"
    $ frobert = "mad"
    r "He punched me!"
    l "He's harassing me!"
    $ faxel = "sad"
    x "I'm not harassing you! I just want to talk to you!"
    x "Is that so much to ask? You can't even talk to me, for real?"
    $ frobert = "serious"
    man "Sir, I'm gonna have to ask you to leave or we'll call the police."
    x "Lena, please!"
    l "You've heard them. Leave!"
    "He looked at me with despair in his eyes."
    man "Sir, please. I won't warn you again."
    x "..."
    stop music fadeout 2.0
    hide axel
    with long
    "He finally gave up and turned around, leaving."
    $ flena = "sad"
    l "..."
    l "Oh my God..."
    "I had to answer the staff's questions as to what had happened."
    "I was so ashamed telling them that it had been my crazy ex-boyfriend that came to force me to speak with him..."
    "I caused so much trouble because of my fucked up personal life!"
    "After what had happened, they told Robert and me to go home. That night we wouldn't have to work."
    "If that would also be detracted from my pay, they didn't say. I really hoped not..."
    $ frobert = "serious"
    $ flena = "sad"
    show robert at lef
    show lena at rig
    with move
    r "Sheesh, I hope my face doesn't get all swollen... Your ex-boyfriend's a piece of shit, did you know that?"
    $ flena = "serious"
    l "Yes, I know. That's why he's my ex."
    $ frobert = "n"
    r "Well, it seems we get a night off... Wanna do something?"
    $ flena = "sad"
    l "What?"
    r "You know, grab a beer or something. I guess having somebody to talk to will do you good now."
    r "So, here I am."
    l "I'm sorry, Robert. I appreciate the gesture but I don't want to talk to anyone right now."
    l "I just want to get home and, I don't know, get into bed or something."
    r "Are you sure?"
    $ frobert = "sad"
    l "Yes. Sorry."
    "What was I even apologizing for?"
    l "Anyways, I'll get going."
    r "Let me at least walk you back home."
    l "I need to be alone with my thoughts. See you tomorrow."
    hide robert
    with short
    show lena at truecenter
    with move
    "I walked back home. Well, I almost ran."
    "I didn't want to stumble upon Axel again on my way back."
    
## V1 LENA FRIENDS ########################################################################################################################################################
    
    play sound "sfx/door_home.mp3"
    scene lenahomenight
    with long
    $ flena = "drama"
    show lena
    with short
    "I arrived home with my emotions still scrambled after the earthquake Axel had brought."
    l "I can't believe that just happened...!"
    "It was clear he couldn't let go of me. And he was in desperate need of me."
    "That frightened me."
    "And I could see how Axel was suffering. How he was pushed to act like that because of it."
    "I didn't want to go back to him. I just couldn't."
    "He had betrayed me and my trust. I knew what kind of guy he was and what I had to expect being next to him."
    "And I didn't want that."
    "But much like Axel himself, I couldn't get rid of my emotions just like that..."
    l "I'm a mess right now..."
    l "I should talk to somebody about this..."
    $ fstan = "surprise"
    $ stan_look = 1
    show stan2 at lef3
    with short
    st "Uh... Oh!"
    st "S--{w=0.3}sorry, I was just wanted to get some cookies from the kitchen..."
    menu:
        "Talk to Stan":
            $ renpy.block_rollback()
            $ v1_talk_stan = True
            l "Stan, this might sound weird, but... I need to talk to someone."
            st "A--{w=0.3}about what?"
            l "Something just happened to me."
            $ fstan = "blush"
            st "All right, but let me... put my pants on, first."
            l "Of course..."
            hide stan2
            show stan at lef3
            with short
            "Stan went to his room and covered himself, then met me at the living room again."
            show lena at rig
            show stan at lef
            with move
            $ flena = "sad"
            $ fstan = "sad"
            st "So... What happened?"
            l "Axel... My ex-boyfriend showed up."
            "I told Stan what had happened last night and just now. How Axel was demanding to speak to me and had flipped out and punched Robert."
            st "He punched a guy? Damn, that's... not good. Are you scared?"
            l "A bit, yeah."
            l "He knows where I work, what if he shows up there everyday until I speak to him?"
            st "Well then, you should call the police, just like the staff threatened to do."
            st "But... May I ask why you don't even want to talk with him?"
            $ flena = "serious"
            l "He betrayed me. I thought we were really in love, I was... But then I found out he had been taking me for a fool and cheating on me."
            l "Lying right to my face..."
            $ flena = "sad"
            l "And I was a fool and fell for it."
            st "That's... horrible..."
            st "I don't understand how he could do something like that to a wonderful girl like you..."
            st "But not all men are like that! You deserve someone who really values you and who would never betray or hurt you..."
            st "I'm sure you can find someone like that so... You should forget about that dude."
            l "I would if he left me alone."
            st "Next time he shows up just call the police, that way he won't dare bother you no more."
            l "To think we used to be together... And now I have to get the police involved?"
            l "It makes me so sad... I can see he still loves me. He looks desperate..."
            $ fstan = "serious"
            st "If he really did love you he would've never cheated on you! He would've treated you with the respect and devotion you deserve!"
            st "Instead he chose to act like a Chad... He deserves to lose you and you don't owe him anything!"
            "Stan seemed to be very opinionated, but I wasn't sure that was what I needed to hear..."
            l "Anyways, sorry for bothering you with my crap."
            play sound "sfx/friendup.mp3"
            show friend_up
            if lena_stan == 3:
                $ lena_stan += 2
            else:
                $ lena_stan += 1
            $ fstan = "shy"
            st "You're not bothering me... I'm honored you chose to talk to me about it..."
            st "If you need help with anything, no matter what... Please let me know..."
            l "Thanks, Stan. Goodnight."
            st "Goodnight..."
            
        "Talk to Louise":
            $ renpy.block_rollback()
            $ v1_talk_louise = True
            l "Uh, sure..."
            l "Is Louise home?"
            st "Yeah, she's in her room..."
            l "Alright."
            hide stan2
            with short
            "I knocked on Louise's bedroom door while Stan went back to his."
            play sound "sfx/door.mp3"
            $ louise_look = 2
            $ flouise = "n"
            show louisebra at lef3
            with short
            lo "Lena? What's up?"
            l "I need to talk to you. Can we go to my room?"
            lo "Sure..."
            play sound "sfx/door.mp3"
            scene lenaroomnight
            $ flena = "sad"
            $ flouise = "sad"
            show lena at rig
            show louisebra at lef
            with long
            lo "You don't look so good."
            l "Axel showed up."
            $ flouise = "surprise"
            lo "Really?"
            "I told Louise what had happened last night and just now. How Axel was demanding to speak to me and had flipped out and punched Robert."
            $ flouise = "sad"
            lo "Oh my... You must feel horrible right now."
            l "You have no idea..."
            l "What should I do? He knows where I work, what if he shows up there everyday until I speak to him?"
            lo "You think he'll do such a thing?"
            l "You've heard how he got today... It wouldn't surprise me."
            lo "Don't you think the staff scared him when they threatened to call the police? If he's as smart as you told me he is, he will steer clear from the hotel from now on."
            l "I hope so. But what if he doesn't?"
            lo "I know you don't want to have anything to do with him after what he did, but maybe you could talk to him."
            $ flena = "serious"
            l "You want me to give him what he wants?"
            lo "Maybe he'll get off your back if you do."
            l "But he'll ask me to get back with him."
            lo "You've made plenty clear that's not what you want. Just tell him the reasons clearly and ask him to move on."
            l "I doubt that'll get him to move on..."
            lo "If he sees you've moved on for good, he'll have no other option."
            $ flena = "sad"
            l "That's what I'm worried about... I don't know if I have moved on myself..."
            lo "What do you mean? You dumped him and you don't want to get back with him."
            l "That's true, but when he showed up... All my feelings resurfaced. I got very emotional and hot-headed."
            lo "That's normal! You're still furious with him."
            l "I don't know... I thought this was over, but it's clear it's not."
            l "It's far from over..."
            lo "Take it easy. You'll get through this. You went through the worst of it already."
            l "Thanks, Louise. You're a good friend."
            play sound "sfx/friendup.mp3"
            show friend_up
            if lena_louise == 4:
                $ lena_louise += 2
            else:
                $ lena_louise += 1
            lo "You know I'm here if you need me."
            l "Goodnight."
            hide louisebra
            with short
            "Louise went back to her room."
            "I was happy I could count on her as a friend, but there wasn't much she could do to help me."
            "At least it was nice having someone to talk to close at hand."
            
        "Call Ivy":
            $ renpy.block_rollback()
            $ v1_talk_ivy = True
            l "Uh, OK..."
            l "Good night, Stan."
            play sound "sfx/door.mp3"
            scene lenaroomnight
            $ flena = "sad"
            show lena
            with long
            "I went to my room, where I could speak to Ivy without being interrupted."
            $ flena = "worried"
            hide lena
            show lena_phone
            with short
            l "I hope she picks up..."
            l "..."
            show phone_ivy at lef3
            with short
            v "Hey, Lena! What's up? I'm about to get to work!"
            l "Hey Ivy... Sorry, but I just need a friend to talk to."
            hide phone_ivy
            show phone_ivy_sad at lef3
            v "You don't sound so good... What happened?"
            l "Axel showed up."
            hide phone_ivy_sad 
            show phone_ivy_surprise at lef3
            v "No way!"
            "I told Ivy what had happened last night and just now. How Axel was demanding to speak to me and had flipped out and punched Robert."
            hide phone_ivy_surprise
            show phone_ivy_sad at lef3
            v "Sheesh, that must have been really uncomfortable..."
            l "Way worse than uncomfortable. I'm really stressed out right now."
            l "He knows where I work, what if he shows up there everyday until I speak to him?"
            v "The staff threatened to call the police on him. He's a smart guy, I doubt he'll take that risk again."
            l "I don't know. Considering how he acted today, it wouldn't surprise me if he did..."
            hide phone_ivy_sad
            show phone_ivy at lef3
            v "Well then why don't you talk to him?"
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
            l "It doesn't sound like bad advice but... I'm not sure I will be able to do that."
            v "That's because you haven't really moved on! And I'm sure Axel sees it, too."
            l "What should I do then?"
            v "My advice? Fuck some guy already! You've been on a dry spell for months!"
            v "Come on girl, it's time to move on!"
            l "I don't know if that way of doing things will work for me..."
            v "Well, if you don't try it you'll never know! In any case, it's a win win situation."
            l "I'll think about it..."
            $ flena = "smile"
            l "Oh, and Ivy... Thanks for not telling Axel where I'm living now when he asked you."
            play sound "sfx/friendup.mp3"
            show friend_up
            if lena_ivy == 5:
                $ lena_ivy += 2
            else:
                $ lena_ivy += 1
            v "Of course, girl, you know you can trust me. I've got you."
            v "I've gotta get to work! Get some rest and don't stress so much over things!"
            v "Life's not so hard!"
            l "Good night."
            hide phone_ivy
            hide lena_phone
            $ flena = "n"
            show lena
            with short
            "She hung up."
            "Talking to Ivy had helped me relax a bit... I was happy I could count on her."
            "I had a lot to think about though..."
            
            
## SATURDAY ########################################################################################################################################################  
    $ day = "Saturday"
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    $ flena = "sad"
    show lenabra
    with short
    "That last night hadn't been a pleasant one, either."
    "I was too anxious to get any good sleep. Why was my life such a mess?"
    "At least I had all morning to myself on Saturdays, since I didn't work at the café during weekends."
    "I had to go to the life-drawing session this afternoon though, and go back to the restaurant at night..."
    "I hoped Axel would've gotten the message and given up once and for all."
    "In case he hadn't..."
    if v1_talk_stan:
        "Maybe I should do as Stan said and just call the cops as soon as I saw him approach me again."
        "I felt that was too extreme, but he had punched Robert... He was clearly unstable."
        "Then again, he was like that because I was making him suffer..."
    elif v1_talk_louise:
        "I wasn't sure what to do. Louise said maybe I could give him a chance and talk to him, try to reason with him."
        "He didn't seem reasonable at all though, with him punching Robert..."
        "But what was the other option? Calling the cops?"        
    elif v1_talk_ivy:
        "Maybe I should do as Ivy said and talk to him..."
        "Maybe it really was the best solution, but I also feared it could make things even worse."
        "I didn't want to call the cops on him, but if he forced me to..."
    l "I hope he just goes away and I don't need to make a choice."
    play sound "sfx/meow.mp3"
    play music "music/normal_day.mp3" loop
    show lola at lef3
    $ flena = "smile"
    with short
    l "Oh, hey Lola. Come here."
    "I lazed around without leaving my bed, trying to take the morning easy."
    $ flena = "n"
    "When was the last time I had time to write a song? I had been so busy lately."
    l "I really miss my guitar... I guess it's still at Axel's house, but I'm not going to ask him to give it back, that's for sure."
    "I petted Lola."
    play sound "sfx/purr.mp3"
    hide lola
    show lolahappy at lef3
    l "Not waitressing, not modeling, but writing and playing songs."
    l "That is what I'd really like to do with my life, you know that, right Lola?"
    "Just a distant dream, of course. Best I could do was taking it as a hobby."
    "A hobby I had barely had time for."
    l "I wish I had a guitar... With all that's going on, I feel like writing a song."
    "It was a great way of sorting out my feelings, putting them into words and melodies."
    l "I don't have a guitar, but I do have pen and paper... I can write the lyrics."
    "I was about to get a notebook when I got a text message."
    play sound "sfx/sms.mp3"
    l "It's from Danny..."
    dan "\"I'm sending you some of the pictures I've edited so far from yesterday's photo-shoot! I'm totally in love with them, Lena, and I hope you like them, too!\""
    dan "\"Can't wait to work with you again! See you next week at the exposition!\""
    $ flena = "smile"
    l "Oh, these are pretty good! What do you think, Lola?"
    "She ignored me, of course."
    l "He's a better photographer than I expected. His style is quite in tune with my own taste..."
    l "I guess I should update my Peoplegram profile with one of these."
    scene lenaroom
    show v1_peoplegram
    with long
    l "I guess I'll post this one..."
    "I had never been too thrilled about this social media stuff. I always felt people tried too hard to portray a perfect version of themselves that didn't really exist."
    l "I guess I'm guilty of that, too... But this is part of the business."
    "Ivy had insisted I needed to have a decent Peoplegram profile with my modeling work if I wanted to get work."
    "No photographer would work with a model that had no public page, and the more visibility I got the easier it would be to get new jobs."
    "In fact, this was the way the art gallery had contacted me and offered me to pose in those life-drawing sessions."
    l "I should write a caption with the picture..."
    menu:
        "Profound quote":
            $ renpy.block_rollback()
            $ v1_rss_quote += 1
            l "Let's go with something profound to make people think a bit..."
            show v1_peoplegram_a
            with long
            l "\"Life is not a problem to be solved, but a reality to be experienced\"."
            play sound "sfx/xp.mp3"
            show wits_up
            $ lena_wits_xp += 1
            call screen skillsup
            l "I wish I could see things this way myself, but sometimes it's just too hard."
            l "Anyways, it's the spirit that matters."            
            
        "Inspirational quote":
            $ renpy.block_rollback()
            $ v1_rss_quote += 2
            l "People like inspirational quotes. Let's see..."
            show v1_peoplegram_b
            with long
            l "\"Open your eyes, live and lie down with the satisfaction of having done it all\"."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ lena_charisma_xp += 1
            call screen skillsup
            l "That should do it. A cool picture needs a cool quote to go with it."
            
        "Flirty quote":
            $ renpy.block_rollback()
            $ v1_rss_quote += 3
            l "Let's write something a bit flirty to entice my followers..."
            show v1_peoplegram_c
            with long
            l "\"If you want to play with fire I can teach you\"."
            play sound "sfx/xp.mp3"
            show lust_up
            $ lena_lust_xp += 1
            call screen skillsup
            l "That sounds spicy without being dirty. Just what I was looking for."
    
    l "I hope people will like it."
    scene lenaroom
    with long
    "I spent the rest of the day at home until it was time to go to the drawing session."
    
    scene gallery2
    $ flena = "n"
    show lena2
    with long
    "It was only my second time posing as a drawing model. It was quite a different experience than posing for photographers."
    "As Ivy said, it wasn't as well paid as photo-shoots, but I was drawn to its artistic nature."
    "Also, the managers were really nice and I felt I was contributing to the cultural scene of the city."
    hide lena2
    show lenanude2
    with long
    "When the participants were ready on their seats, I stripped down backstage and walked to the podium."
    scene gallery2
    show v1_drawpose1
    with long
    "It was a bit nerve-wracking having so many eyes on me at once, since I was used to working one-on-one with a photographer..."
    "But the kind of people who attended these events were cultured and very respectful."
    "They were there to draw and create art, not to ogle creepily at a naked girl's body. Or so was the impression I got."
    "As I got into my first pose, I looked around, evaluating the crowd that would be drawing me today."
    "There were around fifteen people, and amongst those..."
    stop music fadeout 2.0
    scene gallery2
    show v1_drawpose2
    with short
    "I saw a familiar face staring at me with eyes wide open."
    scene gallery
    show v1_draw2
    if v1_fight:
        $ ian_hurt = 1
    if v1_fight:
        $ robert_hurt = 2
    if v1_fight:
        show v1_draw2_hurt
    with short
    if v1_name:
        "Ian!"
    else:
        "The guy from the café!"
        
    jump master_script
    
## V1 CHOOSE PHOTO #################################################################################

screen v1chosepic:
    imagebutton idle "v1_pic1_button.png" hover "v1_pic1_button_hover.png" focus_mask True action SetVariable("v1_choosepic", v1_choosepic +1) , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "v1_pic2_button.png" hover "v1_pic2_button_hover.png" focus_mask True action SetVariable("v1_choosepic", v1_choosepic +2) , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "v1_pic3_button.png" hover "v1_pic3_button_hover.png" focus_mask True action SetVariable("v1_choosepic", v1_choosepic +3) , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "v1_pic4_button.png" hover "v1_pic4_button_hover.png" focus_mask True action SetVariable("v1_choosepic", v1_choosepic +4) , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 

## V1 POOl GAME #################################################################################

screen v1poolgame:
    
    imagebutton idle "v1_pool_screen.png"
    imagebutton idle "v1_pool_screen1.png" hover "v1_pool_screen1_hover.png" focus_mask True action SetVariable("v1_hitball", v1_hitball+1) , [ Play ("ch_one", "sfx/cue.mp3") ] , Return at fade_in_skill 
    imagebutton idle "v1_pool_screen2.png" hover "v1_pool_screen2_hover.png" focus_mask True action SetVariable("v1_hitball", v1_hitball+2) , [ Play ("ch_one", "sfx/cue.mp3") ] , Return at fade_in_skill 
    imagebutton idle "v1_pool_screen3.png" hover "v1_pool_screen3_hover.png" focus_mask True action SetVariable("v1_hitball", v1_hitball+3) , [ Play ("ch_one", "sfx/cue.mp3") ] , Return at fade_in_skill 
