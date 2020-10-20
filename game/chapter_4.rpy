##################################################################################################################################################################################################################
############################################################### CHAPTER 4  ELASTIC HEARTS ###################################################################################################################################
##################################################################################################################################################################################################################

label chapter_four:
    $ save_name = "Lena: Chapter Four"
    
    show blackbg
    with long
    call screen chapter_title
    
##LENA FRIDAY ####################################################################################################################################################################

    $ day = "Friday"
    show active_lena
    with long
    pause 1.0
    scene blackbg
    with long
    pause 0.5 
    call screen calendar
    scene lenaroom
    with long
    $ lena_look = 1
    $ flena = "n"
    "I woke up quite early that Friday."    
    if v3_axel_call:
        $ flena = "sad"
        show lenabra
        with short
        "I had been thinking about Axel... I had decided to call him, and I was wondering when, and what to say."
        "I should take care of that as soon as possible and be done with it."
        if v3_seymour_date:
            $ flena = "n"
            show lenabra
            with short
            "My dinner with Seymour was also still fresh on my mind."
            if v3_seymour_reject:
                $ flena = "serious"
                "I didn't like his attitude nor his ideas. It was clear to see he thought himself to be above everyone else."
                "I didn't want to work for someone like that."
            else:
                "It had been an interesting evening, that was for sure..."
                "He was an intriguing man, and I was interested in knowing more about him."
                "Besides, I was in need of the work he was offering."
    elif v3_seymour_date:
        $ flena = "n"
        show lenabra
        with short
        "My dinner with Seymour was still fresh on my mind."
        if v3_seymour_reject:
            $ flena = "serious"
            "I didn't like his attitude nor his ideas. It was clear to see he thought himself to be above everyone else."
            "I didn't want to work for someone like that."
        else:
            "It had been an interesting evening, that was for sure..."
            "He was an intriguing man, and I was interested in knowing more about him."
            "Besides, I was in need of the work he was offering."
    else:
        $ flena = "n"
        show lenabra
        with short
    "Tonight I had to work at the restaurant again... My two free nights had gone by so quickly..."
    if lena_robert_sex:
        "Soon I would have plenty of free nights, and plenty less money too..."
        "But as long as I managed to get some extra income I should be able to manage. And I could surely use some free time."
    else:
        $ flena = "worried"
        "Soon all my nights would be free, though. And that was what I was worried about."
        "My finances would take a serious hit, being fired from the restaurant."
        "I had to force myself into seeing this as an opportunity to find a better job, though..."
    play sound "sfx/ring.mp3"
    "I hadn't even cleared my head completely when my phone rang."
    "I was pretty sure who it was, considering the time..."
    $ flena = "serious"
    "Indeed, it was Mom. She always liked to call early in the morning."
    "I took a deep breath and picked up."
    hide lenabra
    show lenabra_phone
    with short
    l "Hello."
    show phone_dad at lef3
    with short
    ld "Good morning, Pumpkin."
    $ flena = "worried"
    l "Oh, Dad... How are you? We haven't talked in a while..."
    ld "I'm fine, you don't need to worry about me. I'm taking good care of myself, and your mom is helping me."
    $ flena = "sad"
    l "I'm glad to hear..."
    ld "How have you been doing?"
    l "You know... Really busy with work and taking things one day at a time..."
    ld "Your mom has been keeping me updated. She also told me you had a big falling out."
    l "Yes... You can imagine why."
    ld "I do. But it's not her fault Axel came to visit us."
    $ flena = "serious"
    l "There was no need to invite him to have lunch, though. Nor to talk to him, really."
    ld "Did you want us to be rude to him?"
    l "Considering what he's done, yes. He really hurt me, but it seems Mom can't even consider that."
    ld "Your mom worries about you. I worry about you."
    if v3_talk_molly:
        $ flena = "sad"
        "That was exactly what Molly had told me..."
        l "I know, Dad. But I'm no longer a kid. I have my own life now."
        ld "We know... But you're still our daughter, and always will be. We want the best for you, and we want to know you're happy."
        l "I'm doing my best to make that happen. But Mom's not helping with that attitude."
        l "She thinks she knows better and that the only right way to do things is her own. She's always been that way."
        ld "You're right about that..."
        l "I know she worries about me. But her trying to impose her way of seeing things on me is not helping."
        l "It makes me feel she doesn't care about or respect my feelings. Like she doesn't want to understand me."
        l "Or that she even can't..."
        ld "But you know she loves you, right?"
        l "I do. I just wish she could support me instead of making things difficult for me."
        ld "She can be like that... I would know. I'll talk to her."
        l "Thanks, Dad..."        
    else:
        l "I'm a big girl now. I can take care of myself."
        l "It's time Mom got that idea in her head."
        ld "It's not easy letting a daughter go..."
        l "All I ask is for her to stop thinking she knows better! She thinks she has everything figured out, but she hasn't."
        l "She never listens to my opinions, like she wants to control my life. Well, I'm not a kid anymore, and she's wrong about many things."
        ld "I just hope you two could get along..."
        l "That's not gonna happen unless she changes her attitude."
        ld "We're a bit old to change, I'm afraid..."
    ld "Anyways, are you alright?"
    $ flena = "n"
    l "I am."
    ld "That's all I need to know. Well, that and..."
    ld "We were wondering if you'd be sending money our way this month, too."
    if lena_robert_sex:
        l "That's my plan, yeah. Don't worry."
        ld "That's not what worries me."
    else:
        $ flena = "sad"
        l "To be honest my budget is especially tight these days... But I will, if I can afford to."
    ld "You know you don't have to keep sending us money, right?"
    l "But I know you need it..."
    ld "We don't need it. It helps, of course, but you should take care of yourself first and foremost."
    l "Yes Dad, I know."
    ld "We miss you here. You should drop by one of these days."
    $ flena = "sad"
    l "I will. I've just been so busy..."
    ld "Take care of yourself first and foremost, and don't work too hard. You've always liked to."
    l "I'll try."
    ld "Bye, Pumpkin."
    l "Bye, Dad. Take care, I love you."
    hide phone_dad
    hide lenabra_phone
    show lenabra
    with short
    "I sighed."
    l "I wished things were easier for a change..."
    if v3_axel_call:
        $ flena = "worried"
        "And what I had to face now was even harder."
        play music "music/lenas_theme.mp3" loop
        "I felt this was the moment to call Axel."
        "I had the phone in my hand and this call had served as some kind of warm-up. This was probably the best moment to tackle this."
        "I took a very deep breath and exhaled."
        $ flena = "serious"
        l "OK Lena, you can do this."
        "I unblocked his number and dialed it..."
        hide lenabra
        show lenabra_phone
        with short
        play sound "sfx/ring.mp3"
        l "..."
        l "... ..."
        l "... ... ..."
        l "Come on, pick up..."
        show phone_axel_sad at lef3
        with short
        x "Lena?"
        l "Hello, Axel."
        x "I... I wasn't expecting you to call..."
        l "I wasn't planning to do it. But we need to talk."
        x "Yes, we do."
        l "I need to talk. So you will listen to what I have to say."
        x "Of course..."
        l "This has to stop. What you're doing. The way you're behaving."
        l "How dare you show up at my workplace and block my entrance? How dare you punch my co-worker?"
        x "Lena, I..."
        $ flena = "mad"
        l "How dare you show up at my parents' place? You have no right to involve them!"
        l "Have you any idea how fucking crazy you're acting? This is not normal, Axel!"
        x "I know... Believe me, I know."
        menu:
            "Let him explain himself":
                $ renpy.block_rollback()
                $ flena = "serious"
                "I tried to calm myself, remembering Ivy's advice."
                "Getting too emotional would only show Axel he still had a strong influence over my life."
                l "Why, Axel? Why are you doing this? Have you any idea how you're making me feel?"
                x "I... I can imagine. I'm really sorry."
                x "I feel ashamed of what I've done. All of it. I just couldn't stand this situation..."
                x "Especially knowing it's all my fault."
                $ lena_axel += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                "It was the first time I heard him admitting this so openly, so honestly."
                "That didn't change anything, though."
                hide friend_up
                
            "Double down":
                $ renpy.block_rollback()
                l "No, you don't!"
                l "You have no idea how that's making me feel! You probably don't care one bit!"
                x "That's not true..."
                l "Then stop it! Leave me alone, for fuck's sake!"
                x "But I can't stand how things ended between us... I can't stand this situation..."
                l "There's no situation! You and I are done, it's over. And it's you who caused it!"
                x "It's all my fault. Everything."
                "It was the first time I heard him admitting this."
                "It caught me by surprise, but it was too little, too late."
                
        l "Yes, it is."
        x "You don't deserve what I did to you. I was an asshole."
        l "That's the softest adjective you could use to describe it, but yeah, you were. You still are."
        x "I know... I just lost my mind... You know you have that power over me."
        "I was about to refute him, but he hastily added something else."
        x "But I don't want to make excuses. That's not my intention."
        l "Then what is it?"
        x "I..."
        x "I just wanted to apologize. Honestly."
        $ flena = "worried"
        x "I..."
        x "I know I hurt you... I know I lost you..."
        x "And I know I've been acting crazy and making it difficult for you..."
        x "I..."
        x "..."
        x "Fuck, it's hard for me to find the words."
        x "I know I don't have the right to ask you, but I would like to see you."
        x "I would like to be able to tell you this face to face."
        if lena_axel > 0:
            l "I don't think it's a good idea..."
        else:
            $ flena = "serious"
            l "But I don't want to see you."
        x "I know... But I want to put this past us, for real."
        x "I know you can't forgive me. I'm not asking you to..."
        x "But knowing that you hate me... I can't live with that. I can't live knowing I caused that."
        x "That's all I'm asking. The last thing I'll ever ask of you..."
        x "Besides, I still have your guitar at my place..."
        l "I've bought a new one."
        x "I also have your notebooks... The ones you wrote all those songs and poems into."
        x "I'd like to return them to you."
        x "Let's meet one last time, so I can give you my apology."
        x "Even if I know you can't forgive me."
        menu:
            "Meet with Axel":
                $ renpy.block_rollback()
                $ v4_axel_date = True
                $ flena = "sad"
                if lena_axel > 0:
                    "I hadn't heard him speak like that since we broke up... No, I had never heard him say such things."
                    "This situation also saddened me. This damned tragedy..."
                else:
                    "I was still on the fence... His words, though appropriate, weren't diminishing my anger."
                    "But I was tired of it. Of feeling angry like that."
                "I only wanted to put everything behind me once and for all."
                l "Alright. We can meet."
                l "Once."
                hide phone_axel_sad
                show phone_axel at lef3
                x "Thank you, Lena. I know it's more than I deserve, especially considering how I've been acting lately..."
                x "I promise you won't regret it."
                l "I hope not."
                x "When do you want to meet?"
                l "Sunday morning. I'll pick the place and let you know."
                play sound "sfx/xp.mp3"
                show charisma_up
                $ lena_charisma_xp += 1
                call screen skillsup
                x "Sure."
                x "See you on Sunday, then..."
                l "Bye, Axel."
                hide phone_axel
                hide lenabra_phone
                show lenabra
                with short
                "I hung up the phone."
                l "..."
                "I would be seeing Axel again, after all..."
                "I had the feeling he had finally accepted the situation and his guilt."
                l "I hope we can finally turn the page, both of us, and move on."
                l "I'm weary of all this drama... I need it to be over."
                "I wanted to be optimistic about it. But I would need to wait until Sunday to find out."
                
            "Shut him off":
                $ renpy.block_rollback()
                $ flena = "serious"
                l "No, Axel. I don't want to see you."
                l "I gave you what you wanted by calling you. You wanted us to talk, and we talked. It's more than you deserve."
                l " There's nothing more to say, so I hope you'll leave me alone now."
                x "Lena..."
                l "You're right. I'm not able to forgive you. I just want to forget about you."
                l "I suggest you do the same. Well, you can do whatever you want, but get out of my life."
                l "Don't show up at my work. Don't show up at my parents' place. Just leave me alone."
                l "This is what I want and I'm not gonna change my mind. Are we clear?"
                x "..."
                l "Are we clear?"
                x "Yes."
                l "Bye, Axel."
                hide phone_axel_sad
                hide lenabra_phone
                show lenabra
                with short
                "I hung up the phone."
                l "..."
                "I stayed still, quiet, my gaze lost on the wall."
                $ flena = "cry"
                "Two tears rolled down my cheeks without asking for my consent. A trembling gasp followed."
                "I felt I had finally severed a part of me. A part that had been festering for too long."
                "This would be the last time I cried for Axel."
                call screen willup
                $ flena = "n"
                "I wiped my tears off."        
    stop music fadeout 2.0    
    l "I should get ready for work..."
        
## FRIDAY WORK ############################################################################################################################################################################################
    
    play music "music/normal_day.mp3" loop
    scene cafe
    with long
    $ fmolly = "n"
    if v4_axel_date:
        $ flena = "sad"
    else:
        $ flena = "n"
    show lenawork
    with short
    "I spent part of the morning and afternoon working at the café, as always."
    "It was a pretty unremarkable day, with very few customers. I could take it easy and reflect on my current situation."
    "If only the Van Dykes could afford to pay a bit more... I wouldn't have to be so worried about it."
    "I doubted they could, but maybe I should consider asking them. Molly had always been so nice and understanding..."
    if v4_axel_date:
        $ flena = "worried"
        "Speaking of which..."
        show lenawork at lef
        with move
        show molly at rig
        with short
        l "Excuse me, Molly... I wanted to ask you something..."
        mo "Of course, Lena, you know you can ask me anything."
        l "Well, I should say I want to tell you something. It's a bit personal."
        mo "Go ahead, I'm listening."
        l "It's about my ex-boyfriend. We broke up several months ago, and it wasn't pretty..."
        $ fmolly = "sad"
        mo "Oh... I'm sorry."
        l "The thing is... I've decided to try ironing things out, if that's even possible."
        l "I'm meeting him on Sunday... And I think this would be the best place to do so."
        l "It's a place I know well and I feel... comfortable and safe, especially knowing you and Ed are here..."
        $ fmolly = "n"
        mo "Say no more. You can bring him here without worry."
        mo "Me and Ed will be discreet, but keep an eye on you should you need us."
        $ flena = "smile"
        l "Thank you, Molly. I feel at ease knowing you have my back."
        mo "I do! But I'm certain you won't need us."
        l "I hope not. But I just wanted to give you the heads up, just in case..."
        mo "As I said, don't worry about it. And thank you for trusting me with something like this!"
        l "No, not at all... Thank you, Molly."
        
    scene restaurant
    with short
    $ lena_look = 2
    $ flena = "n"
    $ robert_look = 2
    "After my shift at the café, I headed to the restaurant."
    show lenawork
    with short
    if lena_robert_sex:
        "I would be spending a lot less hours here from now on... For better and for worse."
    else:
        "I was only one week away of never having to return here... For better and for worse."
    if v3_seymour_date:
        $ frobert = "sad"
        show lenawork at rig
        with move
        show robert at lef
        with short
        "As soon as I stepped out of the changing room I saw Robert waiting for me. He had a troubled expression."
        if lena_robert_sex:
            l "Hey, Robert. What's the matter?"
            r "What do you mean, what's the matter?"
            r "What were you doing here last night, having dinner with the owner?"
        else:
            $ flena = "serious"
            l "What's with that face? I hope there's no more bad news concerning my job..."
            r "Bad news? What are you playing at, Lena?"
            l "Me? I'm not playing, far from it."
            r "Then what were you doing here last night, having dinner with the owner?"
        $ flena = "surprise"
        l "The owner?"
        r "Yeah. Mr. Ward."
        l "Wait, he's the owner of this restaurant?"
        r "The controlling shareholder, yeah."
        l "I... I had no idea!"
        r "Are you for real?"
        if lena_robert_sex:
            l "Of course! Why would I lie to you?"
            r "Then you're not trying to get back at the manager for reducing your working hours?"
        else:
            l "Of course! I have no reason to lie."
            r "The staff manager thinks you're trying to get back at her for firing you or something like that..."
        $ flena = "serious"
        l "That's not my intention. Seymour never told me he owned this place..."
        $ flena = "sad"
        l "Though now it makes sense why he brought me here..."
        r "He didn't know you work here?"
        if seymour_restaurant:
            l "I told him, but only when we were already here. He kept quiet about being the owner, though..."
        else:
            l "No, he doesn't know. I never told him... Same as he didn't tell me he owned the restaurant."
        r "And... How did you end up having a dinner date with him?"
        if lena_robert_sex:
            l "We met at an exhibition... He wanted to hire me as a model and asked me to have dinner with him."
            l "It was kind of a job interview."
            r "He wants to hire you as a model? Will you... work with him?"
            if v3_seymour_reject:
                l "No, I won't. I don't like him."
                r "You're at odds with the owner? That could be troublesome..."
                l "He looks like trouble, yeah... That's why I don't want to have anything to do with him."
                r "If you get on his bad side I won't be able to protect you..."
                $ flena = "n"
                l "Don't worry. I can take care of myself."
            else:
                $ flena = "n"
                l "Yes. I need the money."
                r "I see... So you will be posing for him or something like that?"
                l "That's what a modeling job is like, yeah."
                r "Does it cost a lot to hire you?"
                l "Why? You don't look like you need to hire a model."
                r "Um... Probably not..."
            l "Anyways, let's get to work."
        else:
            $ flena = "serious"
            l "We were talking business... But it's not like I need to give you an explanation."
            r "Business? With the boss?"
            l "Yes. But nothing you or the chief need to concern yourselves with."
            l "It was all just a big coincidence. Doesn't really matter, since I won't be here any longer."
            r "I see..."
            l "Can we get to work now?"
            r "Sure..."
    else:
        $ fseymour = "n"
        show lenawork at rig
        with move
        if lena_robert_sex:
            $ frobert = "smile"
            show robert at left 
            with short
            r "Hey, babe."
            l "Hi, Robert. Shall we get to work?"
            r "Wait, the owner has come to check on the restaurant. The staff chief wants us to be at the ready in case he wants anything."
            l "The owner of the restaurant?"
            $ frobert = "n"
            r "Yes. Look, there he comes."
        else:
            $ frobert = "n"
            show robert at left 
            with short
            r "Hey."
            l "..."
            r "I know you're mad about being fired, but try to put on a smile. The owner is here."
            l "The owner?"
            r "Yes, he's talking with the staff chief. She wants us to look professional and be at the ready in case he wants anything."
            r "Look, there he comes."
        show lenawork at rig3
        show robert at lef3
        with move
        $ flena = "surprise"
        show seymour 
        with short
        "I was surprised to see a familiar face walking towards us."
        "He didn't seem to recognize me, in fact he didn't even look at me twice. He talked to Robert."
        mr "So you're the head waiter?"
        r "Yes, sir."
        mr "I've heard you're doing a good job. Keep that up."
        $ flena = "worried"
        "Mr. Ward then turned to me."
        $ fseymour = "surprise"
        mr "Wait, you..."
        "It seems it took him a second to see through my uniform and recognize me."
        $ fseymour = "n"
        mr "Lena."
        $ frobert = "sad"
        l "Hello, Mr. Ward."
        "Robert looked at us, visibly confused, but didn't say anything."
        mr "What a surprise. I never knew you were one of my employees."
        "I then remembered it. I had seen Seymour Ward here before..."
        $ axel_look = 2
        $ faxel = "sad"
        scene restaurant
        show lenawork at rig3
        show axel 
        show seymour at lef3
        with long
        "He was the man having dinner with Axel that night..."
        "I was so shocked seeing my ex-boyfriend that I had barely paid attention to Seymour."
        "And it was clear he had paid zero attention to me. He would not remember a lowly waitress..."
        scene restaurant
        show lenawork at rig3
        show seymour
        show robert at lef3
        with long
        l "I never knew you owned this place."
        mr "Well, I'm the controlling shareholder. I don't involve myself other than in the financial aspect of the business..."
        mr "But this is the last place I was expecting to find you. I assumed you would have higher ambitions."
        if v3_seymour_call:
            "He looked at me and a smile appeared on his face."
            $ fseymour = "evil"
            mr "To think you rejected working with me and you have been working for me all along..."
            $ flena = "serious"
            mr "Oh, the irony."
            l "You should be equally satisfied, then."
            $ fseymour = "smile"
            mr "It's you who should feel dissatisfied. Note the difference in what I said before:"
            mr "I offered you to work {i}with{/i} me, yet you find yourself working {i}for{/i} me."
            mr "But I won't question your choices further. I trust you're clever enough to understand your mistake yourself."
            mr "Enjoy your table-waiting job."
        else:
            mr "You never called me. I have to assume you're not interested in working with me?"
            l "I'd say I'm already working for you, am I not?"
            mr "You're right about that. But I said working {i}with{/i} me, not {i}for{/i} me."
            l "I haven't really decided yet."
            mr "This is not an offer you can sit upon. I'm a man who doesn't like to be made to wait."
            $ flena = "serious"
            l "My apologies. But I have other priorities in my life right now."
            $ lena_seymour = 2
            play sound "sfx/frienddown.mp3"
            show friend_down
            mr "I see. I'll take it as a no, then."
            mr "It will be interesting seeing you come back asking about my offer. I'm not sure it will still be on the table."
            l "I'm sure I will manage without it."
            mr "I'm sure you will. Enjoy your table-waiting job."
        "He turned to Robert."
        mr "Keep up the good work."
        r "Yes, sir."
        hide seymour
        with short
        l "..."
        r "What the hell was that all about? You know the owner?"
        if lena_robert_sex:
            l "We met at an exhibition... He wanted to hire me as a model and asked me to have dinner with him."
            l "It was kind of a job interview."
            r "He wants to hire you as a model? And you said no?"
            l "I don't like him. And I choose who I work with."
            r "If you get on his bad side I won't be able to protect you..."
            l "Don't worry. I can take care of myself."
        else:
            l "Nothing you should concern yourself with."
            r "If you say so..."
            l "This is my last week here, after all."
        l "Let's get to work."
    
    hide robert
    with short
    show lenawork at truecenter
    with move
    "So Seymour was involved with the restaurant, too. Controlling shareholder, no less..."
    l "He really is an influential businessman... I wonder what other businesses he controls in the city."
    $ flena = "n"
    "I focused my attention on the job at hand. It was another busy night at the restaurant."
    "After several hours of hard work my shift ended and I could get back home and rest."
    stop music fadeout 2.0
    if lena_robert_sex:
        scene streetnight
        with long
        $ lena_look = 1
        $ robert_look = 1
        $ frobert = "smile"
        show lena
        with short
        "I got changed and left the hotel."
        r "Lena, wait!"
        show lena at lef
        with move
        show robert at rig
        with short
        l "What's up?"
        r "I was thinking I could keep you company tonight."
        r "Walk you home and, you know..."
        menu:
            "{image=icon_lust.png}Spend the night with Robert" if lena_lust > 2:
                $ renpy.block_rollback()
                $ v4_robert_sex = True
                l "Mhh..."
                "I could use some distraction that night."
                "I had been feeling pretty horny lately and Robert was offering me a release."
                l "Sounds good. Let's go."
                $ lena_robert += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                r "Nice!"
                jump v4fridayrobert
                
            "Not tonight":
                $ renpy.block_rollback()
                $ flena = "sad"
                l "Not tonight, Robert."
                $ frobert = "sad"
                r "Why not?"
                l "I'm just not feeling it tonight."
                $ lena_robert -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                r "But I thought you liked it..."
                l "It's not a matter of liking it or not. I'm just not in the mood."
                "It seemed like Robert was getting a bit too carried away. I had to make clear my position to him."
                l "Look, we slept together once..."
                if v3_robert_repeat:
                    r "Twice."
                    l "Yeah, twice, but it's the same."
                l "What I mean is that that doesn't mean we now have a stable relationship or anything like that."
                l "We can hook up from time to time, when we're both feeling it."
                $ frobert = "n"
                r "I see... Well then, let me know when you're in the mood again..."
                $ flena = "n"
                l "I will. Goodnight, Robert."
                hide robert
                with short
                "I could tell he wasn't too thrilled about it, but that's how it was."
                "I wasn't going to force myself into sleeping with him if I wasn't feeling like it, and I wasn't that night."
                "Another time, maybe."
                jump v4lenasaturday
                
            "End your relationship with Robert":
                $ renpy.block_rollback()
                $ lena_robert_over = True
                $ flena = "n"
                l "Look, Robert..."
                "I could see he was getting way too carried away. It was better if I put a stop to things now."
                $ frobert = "sad"
                r "What?"
                if v3_robert_repeat:
                    l "We slept together once..."
                    r "Twice."
                    l "Yeah, twice. Whatever."
                    l "It was nice, but it was a one-time thing... A two-time thing."
                else:
                    l "We slept together once... But it was a one-time thing."
                r "What? Since when?"
                l "I never said I wanted anything more."
                r "I know, but I hoped we could keep seeing each other..."
                l "As I said, it was nice, but I'm just not feeling it."
                l "If I'm being honest, I have no desire to do it again... Sorry."
                $ frobert = "serious"
                r "You could've told me sooner."
                l "I'm telling you right now. I couldn't have told you any sooner."
                r "What's the problem? You didn't like it?"
                menu:
                    "It was pretty bad":
                        $ renpy.block_rollback()
                        l "It was pretty bad, yeah."
                        $ frobert = "sad"
                        r "...!"
                        $ frobert = "mad"
                        $ lena_robert = 1
                        play sound "sfx/frienddown.mp3"
                        show friend_down
                        r "Well, I'm sorry for not satisfying your sky-high demands!"
                        $ flena = "n"
                        l "They're not sky-high. It just didn't do it for me."
                        l "We shared that experience and now it's time to let it go. That simple."
                        r "Sure. Super simple."
                    
                    "It didn't do it for me":
                        $ renpy.block_rollback()
                        "It had been far from the best sex of my life, but I didn't want to put it that bluntly."
                        $ flena = "n"
                        l "Again, it was... nice. Really. But it's just I'm not really feeling it."
                        $ frobert = "n"
                        r "I don't get it."
                        l "It's very simple. Look, we shared that experience, and now it's time to let it go."
                        $ frobert = "serious"
                        $ lena_robert = 3
                        play sound "sfx/frienddown.mp3"
                        show friend_down
                        r "OK. If you think it's that simple, then there's nothing I can say."
                        l "Thanks for understanding."                
                l "Well, I'm gonna go now... See you, Robert."
                hide robert
                with short
                "Robert wasn't pleased about my decision, of course..."
                "But that was how it was. He had no choice but to accept it."
                jump v4lenasaturday
        
    else:
        jump v4lenasaturday
    

## ROBERT SEX ############################################################################################################################################################################################
        
label v4fridayrobert:
    
    scene lenaroomnight
    with long
    $ flena = "flirt"
    $ frobert = "flirt"
    play sound "sfx/door.mp3" 
    show lena at rig3
    show robert at lef3
    with short
    l "Well, here we are again..."
    r "Yeah, baby..."
    play sound "sfx/meow.mp3" 
    show lola
    with short
    $ frobert = "serious"
    r "And your cat's here, too... I hope it won't try to scratch me again."
    "Lola looked at us for a moment, sitting on top of the bed."
    "She then jumped to the door, leaving us."
    hide lola
    with short
    $ lena_lola -= 1
    play sound "sfx/frienddown.mp3"
    show friend_down
    l "Seems she already knows what's up."
    $ frobert = "flirt"
    r "She's not the only one..."
    play music "music/sex.mp3" loop
    scene lenaroomnight
    show v2_robert2b
    with long
    "There was no need for any more words."
    "I hadn't brought Robert over to talk."
    "We began making out and taking our clothes off."
    scene v4_robert1
    with long
    "As soon as we were naked my hand reached down for Robert's cock."
    "I was pleased to find it hard and ready to go. I liked feeling how much he was turned on by me."
    "The hungry way he kissed me and how he groped my breasts attested to that, too."
    r "Mhhh, oh baby..."
    "His hands kneaded my boobs anxiously, gentleness forgotten in favor of primal desire."
    "What Robert lacked in subtlety he made up for in willingness... He was all over me, head over heels."
    "He had been like that for a long time, only now I was giving him the chance to act on it."
    "And he was super eager to do so. Good, it had been a long day and I didn't want to waste time."
    "I picked up a condom and put it on his cock myself."
    l "Let's do it..."
    scene v4_robert2
    with long
    "I lay down on the bed, spreading my legs and inviting him in."
    "Robert didn't make me wait. He got between them, grabbed his cock and pushed it into me."
    "His latex-covered manhood entered my moist pussy with ease and I felt that pleasurable shiver of the first penetration."
    l "Start slow..."
    r "OK."
    "Robert heeded my petition and began rocking his hips at a calm pace, giving my sex time to get used to it."
    "I took it upon myself to play with my boobs now, increasing my stimulation and excitement."
    "I caressed them, kneaded them softly, carefully pinched my nipples..."
    r "Fuck, baby..."
    "Robert seemed to love seeing me do it. And I also was getting into it more and more, giving something sexy to look at."
    "Robert's breathing started to get heavy and his thrusts gained speed. His erect cock slid in and out, faster, harder."
    "I saw the look of wonder and lust in his eyes. He was enjoying me so much..."
    r "Oh, Lena, fuck yes..."
    r "Do you like it? Can I go faster?"
    if lena_lust > 3:
        menu:
            "{image=icon_lust.png}Get on top":
                $ renpy.block_rollback()
                $ v4_robert_top = True
                l "Wait, I want to get on top."
                scene v4_robert3
                with long
                if v3_robert_repeat:
                    "Last time I enjoyed myself better in this position, taking control of the situation."
                else:
                    "I wanted to take control of the situation. And I had the feeling I would enjoy myself better in this position."
                r "Mhh, damn! Reverse cowgirl!"
                "That position would be ideal for what I had in mind. It obviously surprised Robert."
                "I guess he could enjoy a nice view of my ass bouncing up and down while I concentrated on achieving my orgasm."
                "I let all my weight fall on him, taking his cock balls-deep."
                play sound "sfx/mh1.mp3"
                l "Mhhh!"
                "It reached the spot."
                l "Move your hips, Robert! Fuck me!"
                "He granted my demands without a second thought."
                "He grabbed my ass and helped me move up and down while I added to my own pleasure with my fingers."
                "I rubbed my clit while Robert's dick slid in and out, stroking my sensitive insides."
                "Soon my legs began to tremble, not only because of the physical exertion, but because climax was near..."
                l "Just like that, don't stop, Robert!"
                "Robert heaved and struggled under me, but I wouldn't let him stop."
                r "Nghhh...!"
                l "Right there! I'm almost..."
                with vpunch
                play sound "sfx/ah1.mp3"
                l "Ahhhh!"
                "Finally the orgasm washed all over my body, bringing that fleeting but wonderful bliss."
                "It had been a good one."
                scene lenaroomnight
                with long
                $ frobert = "smile"
                $ flena = "flirt"
                show lenanude2 at rig
                show robertnude at lef
                with short
                r "Whew... That was intense."
                l "It was."
                r "I need a few minutes to catch my breath... But can we go for a second round?"
                r "I haven't cummed yet..."
                $ flena = "n"
                l "I'm dead tired, Robert... After that orgasm I feel my eyes closing by themselves..."
                $ frobert = "sad"
                r "Oh..."
                $ frobert = "smile"
                r "So you liked it that much."
                l "Yes, it was very good. Now I need to get some sleep."
                r "Sure babe, me too..."                
                jump v4fridayrobert3
                
            "Go faster":
                $ renpy.block_rollback()
                jump v4fridayrobert2
      
label v4fridayrobert2:
        "I was already moaning and panting, feeling pleasure building up in my crotch."
        "I decided we could try going for the finish line already."
        l "Yes, I do... Give it to me, Robert."
        "My words worked like a charm. All of a sudden he released all his pent up desire."
        r "Mhhh!"
        "He moved his hips as fast as he could, penetrating me, the sound of our flesh resounding in my room."
        "For a second I worried Stan or Louise could hear us. But I wanted to focus on another thing."
        l "I'm almost there... Don't stop, Robert!"
        r "I'm too..."
        with vpunch
        r "Nghhh!!"
        "He groaned as the climax overcame him."
        l "Don't stop, just a bit more...!"
        "He kept pumping his hips, gloating in his pleasure while I searched for mine."
        with vpunch
        l "Mhhhh!"
        "My orgasm followed his shortly."
        l "Ahh..."
        
label v4fridayrobert3:  
    stop music fadeout 2.0
    scene lenaroomnight
    with long
    "The deed was done, and we were tired."
    "It didn't take long for us to fall asleep."    
    

## LENA SATURDAY ############################################################################################################################################################################################

label v4lenasaturday: 
    $ panties_inv = 0
    $ p_inv1 = False
    $ p_inv2 = False
    $ p_inv3 = False
    $ p_inv4 = False
    
    $ day = "Saturday"
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    $ flena = "n"
    $ frobert = "flirt"
    if v4_robert_sex:
        "I woke up next to Robert the next day."
        show lenanude at rig
        show robertnude at lef
        with short
        l "Good morning."
        r "Mhhh... Good morning, babe."
        l "I'm gonna take a shower."
        r "Cool... Can I take one, too?"
        l "I'd rather not. My flatmates are here this morning and I don't want to disturb them."
        $ frobert = "n"
        r "I see."
        l "I think it's best if you get going."
        r "Sure, OK... Let me pick up my clothes."
        scene lenaroom
        with long
        "I sent Robert on his way and I took a long, relaxing shower."
    else:
        "First thing I did after waking up was taking a long, relaxing shower."
    "I had the morning off and I wanted to enjoy it."
    $ lena_look = 1
    scene lenahome
    with long
    show lena
    with short
    l "Ahh, I miss having normal weekends..."
    "When I stepped into the living room, I was greeted by Louise's shouting."
    play music "music/danger.mp3" loop
    $ flena = "surprise"
    $ flouise = "mad"
    $ louise_look = 1
    $ fstan =  "surprise"
    show louise at rig3
    show stan at lef3
    with short
    lo "Where are they? I know you took them!"
    st "N-{w=0.3}no I didn't!"
    lo "You're lying! I can tell by how shaky your voice is!"
    st "A-{w=0.3}anyone's voice would be shaky in a situation like this...!"
    $ flena = "worried"
    l "What's going on? Why are you fighting?"
    "Louise pointed an accusatory finger towards Stan."
    lo "It's him! I told you he was a creep!"
    menu:
        "I have no idea what you're talking about":
            $ renpy.block_rollback()
            l "I have no idea what you're talking about, Louise."
            l "You'll need to explain..."
            lo "Why don't you ask him? Tell Lena what you did!"
            st "I did nothing! I swear!"
            lo "You're still lying?"
            l "Will someone please explain to me what's going on?"
            
        "Calm down, please":
            $ renpy.block_rollback()
            l "Louise, calm down just a second, please."
            l "Tell me what's going on."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ lena_charisma_xp += 1
            call screen skillsup
            $ flouise = "serious"
            
        "Tell me what happened":
            $ renpy.block_rollback()
            l "Just hold on a second and tell me what happened, Louise."
            l "I need to understand what's going on."
            play sound "sfx/xp.mp3"
            show wits_up
            $ lena_wits_xp += 1
            call screen skillsup
            $ flouise = "serious"
        
        "{image=icon_mad.png}What did you do, you creep?" if lena_stan < 3:
            $ renpy.block_rollback()
            $ v4_accuse_stan = True
            $ v3_defend_stan = False
            $ flena = "mad"
            l "What did you do to Louise, you creep?"
            $ lena_stan = 0
            play sound "sfx/frienddown.mp3"
            show friend_down
            st "I'm no creep! I did nothing!"
            hide friend_down
            
    lo "He stole my panties!"
    l "What?"
    st "I'm telling you! I did not!"
    lo "No? And what were they doing in your room!?"
    st "I don't know! I didn't put them there!"
    if v4_accuse_stan:
        l "At least try coming up with a better excuse, creep."
        st "W-{w=0.3}why should I come up with an excuse? I swear, I did nothing..."
        l "That's all you have to say? The panties were in your room, and I believe Louise. I'm sure you took them!"
        lo "Do you think we haven't noticed how you ogle us when we walk around the house in comfy clothes?"
        st "W-{w=0.3}well, that's..."
        l "Yeah, the way you look at us is disgusting."
        st "...!"
        st "S-{w=0.3}still, that doesn't mean I'm an underwear thief..."
        l "What more proof do we need?"
    else:
        l "They were in your room, Stan?"
        st "Louise says so, but I never saw them there. I never took them, that's for sure!"
        lo "So they appeared there magically?"
        menu panties_investigation:
            "Where exactly did you find your panties?" if p_inv1 == False:
                $ renpy.block_rollback()
                $ p_inv1 = True
                $ panties_inv += 1
                l "Where did you find them? Did you go into Stan's room?"
                $ flouise = "serious"
                lo "No, I would never set foot into that room..."
                lo "But the door was halfway open and I saw them lying on the floor!"
                st "Why would I take your panties and leave them on the floor?"
                lo "Because that's what you do with everything! Your entire room is a mess!"
                st "..."
                "Stan kept quiet, admitting to at least that being true."
                jump panties_investigation
            
            "When did you notice your panties missing?" if p_inv2 == False:
                $ renpy.block_rollback()
                $ panties_inv += 1
                $ p_inv2 = True
                l "When did you notice your panties were missing?"
                $ flouise = "serious"
                lo "I didn't. I just saw them lying on the floor in this creep's room."
                l "So he could've taken them a long time ago?"
                lo "No, I just wore them yesterday. I didn't even get to wash them..."
                $ flouise = "mad"
                lo "Ugh, you disgusting pig! What were you doing with my used underwear!?"
                st "I was doing nothing! I'm telling you I have no idea how they ended up there!"
                st "Only you saw them!"
                jump panties_investigation
                
            "Why do you suspect Stan's guilty?" if p_inv3 == False:
                $ renpy.block_rollback()
                $ panties_inv += 1
                $ p_inv3 = True
                l "Louise, why do you think Stan's guilty?"
                $ flouise = "serious"
                lo "Really? Do I have to spell it out for you?"
                lo "The panties were in his room and he's a creep."
                st "Stop saying that! I've never given you reasons to think that about me..."
                lo "No? Just the other day I saw you creeping into my room!"
                st "I already told you! You left the door open and Lola snuck inside."
                st "And I know you don't like letting her in since that time she peed all over your bed..."
                l "Yeah, sorry about that..."
                "It was true, Louise, despite liking my cat, never let her into her room after that unfortunate and smelly accident."
                "I had to help her clean the mattress and the sheets..."
                lo "Well, that's a very convenient excuse."
                st "It's not an excuse, it's true, and you saw it!"
                jump panties_investigation
            
            "Did you do it, Stan?" if p_inv4 == False:
                $ renpy.block_rollback()
                $ panties_inv += 1
                $ p_inv4 = True
                l "Stan, did you really do it?"
                l "If that's the case, it's better to come clean now."
                $ lena_stan -=1
                play sound "sfx/frienddown.mp3"
                show friend_down
                $ fstan = "serious"
                st "No, I didn't! How many times do I have to repeat that?"
                lo "Say all you want, we won't believe you!"
                st "You just hate me for some reason!"
                lo "For some reason? Do you think I haven't noticed how you ogle me and Lena when we walk around the house in comfy clothes?"
                $ fstan = "surprise"
                st "W-{w=0.3}well, that's..."
                lo "That's true, isn't it? Lena has noticed it, too."
                st "...!"
                st "S-{w=0.3}still, that doesn't mean I'm an underwear thief..."
                hide friend_down
                jump panties_investigation
                
            "I've heard enough":
                $ renpy.block_rollback()
                $ flena = "serious"
                l "I've heard enough."
                lo "So, who do you believe?"
                lo "Me, or this creep?"
        
        menu:
            "{image=icon_mad.png}Accuse Stan" if lena_stan < 3:
                $ renpy.block_rollback()
                $ v4_accuse_stan = True
                $ v3_defend_stan = False
                $ flena = "mad"
                l "I think it's pretty clear you did it, Stan."
                $ lena_stan = 0
                play sound "sfx/frienddown.mp3"
                show friend_down
                st "What? No, I'm telling you..."
                l "Stop lying!"
                lo "You're not gonna fool us, we know you're a disgusting perv!"                
                
            "{image=icon_friend.png}Defend Stan" if lena_stan > 1:
                $ renpy.block_rollback()
                $ v4_defend_stan = True
                $ flena = "n"
                stop music fadeout 2.0
                l "I don't think Stan did it."
                $ flouise = "sad"
                lo "What?"
                $ lena_stan += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                $ fstan = "smile"
                st "Thanks, Lena."
                lo "But it's obvious he did!"
                lo "It doesn't make sense! How the hell did my panties end up in his room?"
                menu:
                    "{image=icon_wits}Lola did it" if lena_wits > 2 or panties_inv > 2:
                        $ renpy.block_rollback()
                        l "It was probably Lola."
                        lo "Lola?"
                        l "It wouldn't be the first time she's misplaced one of my socks. She likes to play with them."
                        l "If you left the door to your room open, it's possible she took them and left them in Stan's room."
                        l "That would explain why they were lying randomly on the floor."
                        lo "That sounds... Way too convenient."
                        l "It makes sense, though."
                    "I don't know":
                        $ renpy.block_rollback()
                        $ flena = "n"
                        l "I don't know... Maybe you dropped them when making laundry..."
                        $ flouise = "serious"
                        lo "In his room? How?"
                        l "As I said, I don't know... But I believe Stan."
                        if v3_defend_stan:
                            lo "I shouldn't be surprised. You already sided with him that other time..."
                        else:
                            lo "I don't understand why!"
                        l "I can see he's telling the truth. And he's never done anything of the sort."
                        $ lena_louise -= 1
                        play sound "sfx/frienddown.mp3"
                        show friend_down
                        lo "There's a first time for everything..."
                st "Look, I don't know what else to tell you... I've said nothing but the truth, and Lena sees it..."
                $ fstan = "sad"
                st "I'm sorry you think of me that way, Louise. All I can do is try to steer clear from you as much as possible from now on..."
                $ flouise = "n"
                lo "Yeah, do that."
                st "Well then... I'll be going to my room."
                play sound "sfx/door.mp3"
                hide stan
                with short
                lo "I can't believe how you defend him..."
                l "I just think he's innocent! I know you don't like him very much, but you should try keeping the peace..."
                lo "Whatever."
                 
            "It's a mystery":
                $ renpy.block_rollback()
                $ flena = "sad"
                l "I don't know what to tell you, guys... It's a mystery."
                lo "A mystery, how?"
                l "I don't think Stan did it... I mean, it would appear so, but I'm not convinced..."
                st "It wasn't me, I swear! I would admit it if I did, but I didn't!"
                lo "You really believe him, Lena?"
                l "I want to give him the benefit of the doubt..."
                lo "The situation's pretty clear to me."
                l "It's his word against yours. If you had any solid proof..."
                lo "I haven't installed cameras around the house, but maybe I should, having him around."
                st "I never did anything like that, but I don't know what else to tell you! You don't want to listen to me."
                st "All I can do is try to steer clear from you as much as possible from now on..."
                lo "Yes, keep yourself in your dirty room and avoid coming out as much as possible."
                l "More than you already do."
                st "Sure..."
                stop music fadeout 2.0
                play sound "sfx/door.mp3"
                hide stan
                with short
                lo "Ugh, I can't believe we have to share our place with that guy!"
                lo "You really believe him?"
                l "I can't be sure, but I'd say so... He's awkward and you could perfectly picture him being a creep, but..."
                if lena_stan > 3:
                    l "I don't think he's a bad guy."
                else:
                    l "Who knows. You could be right."
                $ flouise = "n"
                lo "Let's just be on our guard. I don't trust him."
        
    if v4_accuse_stan:
        "Stan looked desperate at this point."
        st "I don't know what else to tell you!"
        lo "Just say you will steer clear of us from now on."
        st "Yes, I will..."
        l "I hope so. And don't even dream coming close to our rooms!"
        st "I won't!"
        st "Can I go back to mine already?"
        lo "Yes, and avoid coming out as much as possible."
        l "More than you already do."
        stop music fadeout 2.0
        play sound "sfx/door.mp3"
        hide stan
        with short
        lo "Ugh, I can't believe we have to share our place with that guy!"
        $ flena = "sad"
        l "I know, it's far from ideal... But we can't afford anything better."
        $ flena = "n"
        l "At least we're living together, you and I."
        $ lena_louise += 1
        play sound "sfx/friendup.mp3"
        show friend_up
        $ flouise = "smile"
        lo "Yeah... I don’t know what I’d do without you being here with me."
        $ flouise = "n"
        lo "Let's hope this guy leaves sooner than later..."
        $ flena = "sad"
        l "I find it unlikely, since it's him who's renting us the rooms..."
   
    play sound "sfx/ring.mp3"
    l "Oh, wait, I'm getting a call."
    hide lena
    show lena_phone
    with short
    l "Yes?"
    show phone_ivy at lef3
    with short
    v "Hey, Lena! What are you doing this morning, are you home?"
    l "Yeah, I am."
    v "I'm in the area, and I want to see you! Meet me in five minutes!"
    menu:
        "Sure!":
            $ renpy.block_rollback()
            l "Sure! I want to see you, too."
            v "Cool! We need to do this more often! You can call me whenever, too."
            l "I know."
            v "Come on, move your ass and meet me outside! I'm almost to your place."
            l "I'm on my way."
           
        "Right now?":
            $ renpy.block_rollback()
            l "Right now?"
            v "Yeah, that's what I said!"
            l "This is unexpected."
            v "You know me, I'm full of surprises!"
            v "Come on, move your ass and meet me outside! I'm almost to your place."
            l "OK, I'll be on my way."
            
        "You should've warned me":
            $ renpy.block_rollback()
            l "You should've warned me you wanted to meet!"
            v "What are you, my friend or a doctor? Do I really need to make an appointment?"
            v "Besides, do you have anything better to do right now?"
            l "No, not really..."
            v "Then move your ass and meet me outside! I'm almost to your place."
            l "OK, OK. I'm going."
    
    hide lena_phone
    hide phone_ivy
    show lena
    with short
    lo "I still find it hard to believe you're friends with her, honestly."
    $ flena = "worried"
    lo "If I had a friend like her I wouldn't let her near my boyfriend at all. She looks like the kind of girl who would try to steal him."
    "Her comment reminded me of what I had learned just the other day."
    "Her boyfriend Jeremy was the same guy Ivy had been telling me about. That co-worker who had been flirting with her..."
    "Jeremy hadn't even tried to deny it. Quite the contrary..."
    "He even said he wasn't really Louise's boyfriend, but she thought he was."
    "Indeed, she was convinced about it. She had no idea of the games Jeremy was really playing behind her back."
    l "..."
    lo "What?"
    l "Oh... It's..."
    "Should I tell Louise about Jeremy's mischievousness?"
    "As far as I knew nothing had really happened between him and Ivy, but who knows what else he was doing and who else he was seeing..."
    "But I knew telling Louise would mean making her suffer. She took these kinds of things hard."
    "Not to mention she would probably get mad at Ivy. She never really liked her in the first place."
    "But, most of all, was it my place to get between Louise and her boyfriend?"
    "If I kept quiet, maybe they would figure things out by themselves and find happiness together, after all..."
    "But if I talked I was denying Louise that chance and most certainly dooming her relationship."
    menu:
        "Tell Louise about Jeremy":
            $ renpy.block_rollback()
            $ louise_jeremy = False
            $ flena = "sad"
            l "Louise... I need to tell you something about Jeremy."
            $ flouise = "sad"
            lo "About Jeremy? Is something wrong?"
            "I saw worry appear in Louise's expression. I was about to burst her bubble..."
            "But she deserved to know. I would like to, if it were me in her shoes."
            l "Actually, yes..."
            l "He's not as nice and respectful as he'd like you to believe."
            lo "Why are you saying that? You're scaring me, Lena."
            l "I've learned he's flirting with other girls."
            $ flouise = "surprise"
            lo "What!? That can't be true."
            l "Sadly, it is..."
            $ flouise = "serious"
            lo "How did you learn that?"
            l "I ran into Jeremy the other night at the gym... Turns out he's working with Ivy at the club."
            l "And it seems he's been trying to get into Ivy's panties..."
            $ flouise = "surprise"
            lo "He... He's been flirting with Ivy?"
            lo "Did something happen between the two?"
            l "No, it hasn't. At least that's what they told me."
            $ flouise = "mad"
            lo "That slut! I'm sure she's been trying to seduce him!"
            l "I think it's the other way around... In any case, Ivy didn't know Jeremy had a girlfriend."
            lo "She's lying! I'm sure she knew!"
            l "Listen to me, Louise, please. It's not Ivy's fault."
            l "Jeremy never told her about you. And when we confronted him about it, he..."
            l "Well, he said that he doesn't really consider you his girlfriend."
            $ flouise = "sad"
            lo "No, he didn't say that..."
            l "I'm sorry Louise, but Jeremy's not a trustworthy guy."
            $ flouise = "cry"
            lo "No, he wouldn't cheat on me... He wouldn't..."
            "Tears started rolling down Louise's cheeks and my heart sank."
            l "I'm sorry Louise, but I thought you deserved to know..."
            lo "Why? Why's he doing this to me?"
            l "He's an asshole... He doesn't deserve your tears..."
            lo "No, this can't be true... It can't..."
            play sound "sfx/door.mp3"
            hide louise
            with short
            "Louise suddenly turned around and disappeared into her room, closing the door behind her."
            l "I should leave her alone..."
            
        "Don't say anything":
            $ renpy.block_rollback()
            $ flena = "n"
            l "It's nothing."
            l "I gotta go!"
            $ flouise = "smile"
            lo "Sure, see you later!"
            
##IVY DATE #####################################################################################################################################################################

    play music "music/normal_day.mp3"
    scene street
    with long
    $ lena_look = 1
    show lena
    with short
    if louise_jeremy:
        "I finally decided against getting myself involved in Louise's relationship."
        "I didn't want to be the one to burst her bubble. It was not my place."
        "And maybe Jeremy would reconsider his attitude now and become a proper boyfriend."
        "Either that or he would come clean and talk about things with Louise himself. It was his responsibility, not mine."
        l "I hope I made the right choice..."
    else:
        l "That was really uncomfortable... But it had to be done."
        l "Though it's shitty she had to learn it from me..."
        "She would surely need comforting later. Now she needed time to grieve."
    $ ivy_look = 1
    $ fivy = "n"
    $ flena = "n"
    show lena at rig
    with move
    show ivy at lef
    with short
    "Ivy was waiting for me in the main street."
    v "There you are!"
    l "Hi Ivy. How come you're in the area this morning?"
    v "I want to do some shopping. When was the last time you and I did this together?"
    l "I don't even remember..."
    v "I always tell you we should find more time to hang out together!"
    l "I'll be way less busy next week..."
    l "So, what are you shopping for today? It's probably shoes, you can never have enough of those..."
    v "Not quite, though you're right about that, ha ha."
    l "Clothes?"
    v "Nope. You'll see."
    "We began walking down the street."
    l "By the way, how are things with Jeremy?"
    v "There is no \"thing\", not anymore. He didn't even speak to me last night at the club."
    v "I can see how ashamed he is. Come on boy, if you get caught at least deal with it!"
    if louise_jeremy:
        l "Do you think he will tell Louise?"
        v "How should I know? It's not like I care, either."
        l "I was thinking I should maybe tell her..."
        v "Don't. It's not your place. She should be smart enough to know what kind of guy she's dating."
        $ flena = "sad"
        l "We all make mistakes. We all can be fooled..."
        $ fivy = "sad"
        v "Yeah... Sorry about that."
        $ fivy = "n"
        v "What I mean is you should save yourself the trouble of getting involved."
        v "Besides, it's not like anything happened between him and me. Not really..."
        v "They will figure things out by themselves."
        $ flena = "n"
        l "Yeah, that's also my opinion."
    else:
        l "I just told Louise about his dirty deeds..."
        $ fivy = "surprise"
        v "You did?"
        $ flena = "n"
        l "Yeah... She deserved to know..."
        $ fivy = "serious"
        v "You shouldn't have gotten involved... That's only trouble."
        l "But I'm Louise's friend. I would like her to do the same for me."
        v "Ignorance is bliss, haven't you heard?"
        v "I'm sure she didn't take it well."
        l "She started crying..."
        "Ivy sighed."
        v "She's always been like that... I don't know her much, but I know I wouldn't have the patience to be friends with someone like her."
        v "And she never liked me either, I could tell that so clearly. I'm sure she blames me for this."
        l "I told her it wasn't your fault..."
        v "Because she blamed me right away, right?"
        l "Yeah..."
        $ fivy = "n"
        v "See? Anyways, it's not my problem."
        $ flena = "n"
    v "Such a shame Jeremy's a prick. I was about to give him a chance..."
    if lena_bdick > 0:
        l "I can see why..."
        $ fivy = "flirt"
        v "You can?"
        $ flena = "blush"
        l "Uh, I mean..."
        v "Could it be you like him, too?"
        if lena_jeremy > 3:
            l "He seems nice, or that's what I thought, but after seeing the kind of guy he is... But..."
        else:
            l "Not really, especially considering the kind of guy he is, but..."
        v "But?"
        l "I might've... seen his dick."
        v "Whaaat? You need to tell me about this!"
        l "I, uh..."
        "I confessed to Ivy that curiosity had taken the better of me and I had ended up spying on Jeremy and Louise."
        v "You naughty girl! I didn't know you were into that kind of thing, hee hee!"
        l "It's not like that..."
        $ flena = "flirt"
        l "Well, maybe just a bit. It was really fucking big."
        v "I know, I've seen it, too!"
        l "You have?"
        v "He sent me a pic, hee hee. I was curious about trying it, but oh well..."
    else:
        $ fivy = "flirt"
        v "You wouldn't believe how hung he is. Biggest I've ever seen, ha ha!"
        $ flena = "blush"
        l "You've seen his dick?"
        v "He sent me a picture. Wanna see?"
        l "No need!"
        if v3_spy:
            l "I might've... seen it too."
            v "Whaaat? You need to tell me about this!"
            l "I, uh..."
            "I confessed to Ivy that curiosity had taken the better of me and I had ended up spying on Jeremy and Louise."
            v "You naughty girl! I didn't know you were into that kind of thing, hee hee!"
            l "It's not like that..."
            v "So you saw it then. His cock is really fucking big, isn't it?"
            l "It's big, but I'm not fascinated by it or anything like that!"
            v "Not even a bit? I'm curious about it, I can tell you that much!"
            l "You know it's not my preference."
            v "That's true. You had problems with Axel..."
            l "Let's change the subject, shall we?"
            v "Sure, sure."
        else:
            v "Ha ha ha!"
    $ flena = "n"
    $ fivy = "smile"
    v "Look, here we are!"
    
    scene sexshop
    with long
    "Ivy had unexpectedly brought me to a sex shop."
    "It was far from the shady image one usually pictures in one's mind when thinking about a place like this."
    "It was clean and well-lit, welcoming and stocked full of toys, lingerie and other sex-related products..."
    show lena at rig
    show ivy at lef
    with short
    l "Oh, wow. I never knew this place existed."
    v "It's pretty new. Female-friendly, I'd say. No creepy or greasy guys around."
    v "And they even have a tattoo studio at the back!"
    l "Was it here where you got that navel piercing done?"
    v "Yeah! Come on, let's check it out. I need to buy a few things..."
    l "May I ask what for?"
    v "What do you think, silly?"
    menu:
        "To masturbate":
            $ renpy.block_rollback()
            l "To masturbate, I guess."
            l "Though I wouldn't think you need any of this, considering you always have a guy willing to sleep with you..."
            v "You need to use your imagination a bit more, Lena! There are a ton of things you can do."
            v "You don't need to be alone to use most of these toys... In fact, the best way to enjoy them is with someone else!"
            $ fivy = "flirt"
            v "Though I have thought about some special use I could give them solo..."
            v "People are asking for spicier content for my Stalkfap, so I'm thinking about giving it to them."
            l "I would use another word instead of \"spicier\", though."
            v "Use whatever word you wish, dirtier, sluttier..."
            
        "To spice things up":
            $ renpy.block_rollback()
            l "To spice things up with your partners, I guess."
            l "I doubt you need them to substitute having a willing guy to give you some loving, ha ha."
            if lena_lust < 5:
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
            $ fivy = "flirt"
            v "You're right, I have no shortage of guys to use these toys with!"
            v "But I've also thought about some special use I could give them solo..."
            v "People are asking for spicier content for my Stalkfap, so I'm thinking about giving it to them."
            l "I would use another word instead of \"spicier\", though."
            v "Use whatever word you wish, dirtier, sluttier..."
            
        "To make naughty content for Stalkfap" if v3_check_stalkfap:
            $ renpy.block_rollback()
            l "Let me guess... To make some naughty content for your Stalkfap."
            play sound "sfx/xp.mp3"
            show wits_up
            $ lena_wits_xp += 1
            call screen skillsup
            v "You've always been smart! You have a good eye for business, it seems." 
            $ fivy = "flirt"
            v "So yeah, that's one of the reasons. The other one is to enjoy myself, of course, hee hee!"
            l "I've seen the comments people leave on your Stalkfap... They are asking for pretty dirty stuff."
            
        "To play the drums":
            $ renpy.block_rollback()
            $ flena = "happy"
            l "To play the drums, obviously. I can totally picture you with one dildo in each hand..."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ lena_charisma_xp += 1
            call screen skillsup
            $ fivy = "flirt"
            v "Ha ha ha, you think of such strange things sometimes..." 
            l "That's why you like me so much."
            v "One of the many reasons! Sadly I don't know how to play the drums, so I will use those dildos for other stuff..."
            $ flena = "n"
            l "Such as?"
            v "To please myself... And to please my Stalkfap followers!"
            v "People are asking for spicier content, so I'm thinking about giving it to them."
            l "I would use another word instead of \"spicier\", though..."
            v "Use whatever word you wish, dirtier, sluttier..."
            
    v "You need to give the public what they're asking for, and their money will follow!"
    l "And are you really comfortable with that?"
    v "I'm past being ashamed of those kind of things. Though I've never done it before... Publicly, at least."
    l "You will be exposing yourself a lot..."
    v "A lot of girls do it and they seem to be doing alright."
    l "As long as you're comfortable with it..."
    if stalkfap:
        v "You're also using Stalkfap. People will ask this of you, too."
        l "Well, they can ask all they want... My plan is to use Stalkfap to post uncensored modeling pics, nothing more."
        v "That won't cut it. Stalkfap is better for selfies! It's what people really want."
        v "You should upload the professional pics to Peoplegram, they serve as bait."
        v "And those are the pics that will get you noticed by modeling agencies like Wildcats, and the real end goal."
        v "So it's important to have both, pro pics and selfies!"
        l "You're really knowledgeable about this stuff."
        v "Of course, I'm aiming to make it big! So listen to my tips!"
        $ fivy = "serious"
        v "There's a lot of competition, though... Girls are flooding that market and it's becoming difficult to stand out."
        $ fivy = "n"
        v "That's why I need to step up my game!"
        l "I should start by building up my Peoplegram, then."    
    elif v3_check_stalkfap:
        v "What about you? Have you thought about opening a Stalkfap account, too?"
        l "Yes, but it's not for me. I'm comfortable with uploading my modeling pics, but nothing more."
    else:
        v "It's no biggie."
        l "All I'm comfortable with is uploading my modeling pics, nothing more."
    v "In that case you should do more photo-shoots! Do you have any lined up?"
    if v3_seymour_reject:
        l "Not really."
        v "You should hit up Danny, I'm sure he would be happy to work with you again." 
    else:
        l "Yes, I actually do."
        v "Cool! You should hit up Danny, I'm sure he would be happy to work with you again." 
    $ fivy = "n"
    v "Anyways, let me see what I should pick..."
    "Ivy and I began browsing the store."
    "They had every kind of sex toy I could imagine... Some of them I didn't even know existed."
    v "I think I will take this one here... Oh, and maybe that one!"
    $ fivy = "flirt"
    v "By the way, Lena, have you been using the vibrator I gifted you?"
    if v3_use_dildo:
        $ flena = "shy"
        l "I have, actually."
        v "I'm glad to know you're enjoying my gift!"
        v "But don't use it as a substitute for guys!"
        if lena_robert_sex:
            if v3_ivy_chat:
                l "You know I'm not."
                v "True, true."
            else:
                l "I'm not."
                v "You're not?"
                l "Nope... I hooked up with Robert, the guy from work."
                $ fivy = "surprise"
                v "You slut! And you didn't tell me!?"
                $ fivy = "flirt"
                v "It was about time! And how was it?"
                if v3_robert_orgasm:
                    l "It was good!"
                    v "Good, but not great?"
                else:
                    l "It was... OK."
                    v "You don't sound too convinced."
                $ flena = "n"
                l "It wasn't the best sex of my life, but I wasn't expecting it either."
                l "It always takes time to get in sync with somebody new. And it had been quite a while for me..."
                v "Well, the important thing is to keep it swinging now that you've got it moving."
        else:
            v "You need to go out into the world and have some fun!"
            $ flena = "n"
            l "I know, I know..."
    else:
        l "I haven't, actually..."
        if v3_robert_repeat or lena_robert_sex_late:
            if v3_ivy_chat:
                v "Well, at least you're hooking up with that guy, Robert..."
                v "You could tell him to use the vibrator while you two are together!"
            else:
                v "Oh, come on. You're not getting any sex, so at least try pleasing yourself!"
                v "What's happened to you? I'm worried about you, girl!"
                l "I haven't used it because I hooked up with a guy. Robert, from work."
                $ fivy = "surprise"
                v "You slut! And you didn't tell me!?"
                $ fivy = "flirt"
                v "It was about time! And how was it?"
                if v3_robert_orgasm:
                    l "It was good!"
                    v "Good, but not great?"
                else:
                    l "It was... OK."
                    v "You don't sound too convinced."
                $ flena = "n"
                l "It wasn't the best sex of my life, but I wasn't expecting it either."
                l "It always takes time to get in sync with somebody new. And it had been quite a while for me..."
                v "Well, the important thing is to keep it swinging now that you've got it moving."            
        else:
            v "Oh, come on. You're not getting any sex, so at least try pleasing yourself!"
            v "What's happened to you? I'm worried about you, girl!"
            l "I just haven't been in the right mood, that's all."
            v "Nonsense. It's all about getting started. Put some effort into it!"
            l "I never thought one had to put effort into that kind of thing..."
            v "Then you're even more naive than I thought! Don't be a prude and just give it a try."
    if lena_robert_sex:
        if v3_ivy_chat:
            v "So how's it going with Robert?"
            if lena_robert_over:
                $ flena = "n"
                l "It's not \"going\". It's already over."
                $ fivy = "sad"
                v "What? Why?"
                l "This was never meant to be anything long-term. I was curious about him, decided to give it a go and now I'm satisfied."
                $ fivy = "n"
                v "I see, good choice. He wasn't that good in bed, so better to let him go."
                v "It's not like you'll have a shortage of options!"
            elif v3_robert_repeat or v4_robert_sex:
                $ flena = "shy"
                l "It's going good... We've slept together a few times now."
                v "You go girl! I hope he's getting better in bed, but in any case you should play the field a bit more."
                v "Don't get stuck with just this one guy."
                $ flena = "n"
                l "Yeah, I doubt this will be a long-term thing."
            else:
                l "I'm taking it slow."
                v "You're not too comfortable with him?"
                l "I guess. I just need to take things one step at a time. See where this is going."
                v "You already told me he wasn't boyfriend material."
                l "He isn't. And I doubt this will be a long-term thing. Still, I need to get back into the swing of things carefully."
                v "I understand. Then keep going at it until you feel comfortable with it and then ditch him!"
                v "It's not like you'll have a shortage of options, and now it's time for you to play the field and enjoy yourself!"
        else:
            if lena_robert_over:
                $ flena = "n"
                l "Well, about that... It's already over."
                $ fivy = "sad"
                v "What? Why?"
                l "This was never meant to be anything long-term. I was curious about him, decided to give it a go and now I'm satisfied."
                $ fivy = "n"
                v "I see, good choice. He wasn't that good in bed, so better to let him go."
                v "It's not like you'll have a shortage of options!"
            else:
                v "So what's the plan with this guy? I hope you're not thinking about dating him."
                l "No, not at all."
                v "Good. Last think you need right now is to get into another relationship!"
                v "It's time for you to be free, play the field and enjoy yourself."
                l "Could be. In any case I've never seen him as boyfriend material, and I doubt this will be a long-term thing."
                v "That's my girl."

    v "And what about Jeremy's friend, Ian? I never realized I had already met him..."
    if v2_kiss:
        l "Nothing new since that kiss..."        
    elif v3_ian_date:
        l "I met him with another friend of his last Wednesday, but nothing happened."
        v "That's disappointing... Maybe he's not interested?"
        if ian_lena > 6:
            l "I'd say he is..."
        else:
            l "I don't know... I'd say he is, but he's a bit unclear, I guess."
    elif v2_ian_date:
        l "We haven't met just the two of us since that time at the record store."
        v "That's disappointing... Maybe he's not interested?"
        l "I'm not really sure... He's not clear about it."
    else:
        l "Nothing new. We haven't met or anything."
        v "So nothing will come out of that."
        l "Probably not."
    v "The real question is, are you interested in him?"
    menu:
        "Yes" if ian_lena > 5:
            $ renpy.block_rollback()
            $ lena_go_ian += 2
            $ flena = "blush"
            l "Yeah, well... He's different. Different from most guys I've met..."
            v "And that's good?"
            l "Of course it is..."
            v "Then why don't you fuck him?"
            if lena_robert_sex:
                v "You're already fucking Robert, and you don't even like him that much."
                l "Maybe that's the reason I'm fucking him and not Ian."
                $ fivy = "sad"
                v "How does that make any sense?"
            l "I just... Don't want to botch it."
            v "That's dumb. When has sex ruined anything?"
            l "Plenty of times."
            $ fivy = "n"
            v "Actually..."
            v "OK, you're right. But you'll have to cross that bridge sooner or later if you're interested in him."
            l "When I feel the time's right... My life is pretty chaotic right now."    
            l "I don't want to drag him into it."
            v "I'm sure he wouldn't complain at all."
            
        "I don't know":
            $ renpy.block_rollback()
            $ lena_go_ian += 1
            $ flena = "sad"
            l "I don't really know... He's different, and I like that."
            l "But I don't know if now's the right time or if he's the right guy... My life is pretty chaotic right now."
            v "The right time and the right guy for what?"
            if lena_robert_sex:
                v "You're already fucking Robert. If you have doubts about fucking Ian you should probably get rid of him."
                l "It's not like that..."
                v "Then fuck him and clear your doubts. It's that simple."
            else:
                l "I don't know. For... everything."
                v "If you have so many doubts you should get rid of him."
                l "It's not like that..."
                v "Then fuck him and clear your doubts. It's that simple."
               
        "I don't think so" if ian_lena < 6:
            $ renpy.block_rollback()
            $ flena = "n"
            l "Honestly, I don't think so..."
            v "You seemed interested in him last time we spoke."
            l "He piqued my curiosity, yeah. But I don't know, I'm not sure it would work out."
            v "In bed?"
            l "Probably. I don't know if he's that kind of guy..."
            if lena_robert_sex:
                v "If you're fucking Robert and not him it must be for a reason."
                v "I'd say try it out with Ian to see how it goes, but if you don't feel any chemistry it doesn't make sense to force it." 
            else:
                v "I see."
                v "I'd say try it out with him to see how it goes, but if you don't feel any chemistry it doesn't make sense to force it."
            v "There's plenty of other guys available for you, should you want them!"
            l "I guess... And Ian hasn't really shown too much interest, I'd say."
            if lena_robert_sex:
                l "Unlike Robert."
                v "Yeah, and you already have him to scratch that itch, hee hee!"

    if lena_go_ian > 0:
        $ fivy = "flirt"
        v "In any case, if he doesn't make a move you should ditch him and find someone else." 
        if lena_robert_sex:
            v "You already have Robert to scratch that itch, after all."
        else:
            v "I'm sure there are a ton of guys who'd love to have you."
    $ fivy = "n"
    $ flena = "n"
    v "Oh, look at this!"
    "Ivy picked up something from a shelf, suddenly changing the subject."
    show lena at rig3
    show ivy at lef3
    with move
    show v4_anal_plug
    with short
    "It was an anal plug, or so it said on the box."
    v "Have you ever tried one of those?"
    l "Nope..."
    v "They're nice to have, especially if you're not used to anal sex..."
    v "You never really did it, did you?"
    $ flena = "blush"
    l "No... I tried a couple of times with Axel, but..."
    v "He was too big for you and it hurt too much. I remember you telling me."
    v "It's normal, it takes time getting used to it. For most people at least."
    $ fivy = "flirt"
    v "You should buy one of these!"
    if lena_lust > 2:
        $ flena = "n"
        l "You're right, I should try it. I'm curious about it."
    else:
        l "I don't know..."
        v "You need to start trying things, girl! You're missing out!"
    v "You should've tried it on your own first if you're ever going to do it with a guy."
    v "Take responsibility for your own sexuality!"
    l "Do you like it?"
    v "Anal? Yeah, it's pretty good!"
    l "Is it really pleasurable?"
    v "It is... Not for everybody, I guess, but I'm lucky in that sense."
    v "And it's a pretty big turn on, so you should give it a go if only for that reason!"
    if lena_lust > 2:
        $ flena = "flirt"
        l "OK, I'm more than convinced, ha ha."
    else:
        $ flena = "n"
        l "If you put it that way... I guess I can try it."
    l "I'll buy it."
    v "You'll need some lube, too."
    v "Let me get some sexy lingerie as well..."
    hide v4_anal_plug
    with short
    show lena at rig
    show ivy at lef
    with move
    $ flena = "n"
    $ fivy = "smile"
    "Ivy finished picking up her items and we paid at the counter."
    if lena_go_piercing == 2:
        l "Hey, before going I also want to check out the tattoo parlor on the back... I'd like to get a navel piercing like yours!"
        $ lena_ivy += 1
        play sound "sfx/friendup.mp3"
        show friend_up
        v "Oh, that's true! You told me you had been thinking about getting one."
        l "Yeah..."
        v "Let's take a look."
    elif lena_go_piercing == 1:
        v "Do you want to check out the tattoo parlor in the back, too?"
        v "You could get a sexy navel piercing like mine! I'm in love with it!"
        menu:
            "Not interested":
                $ renpy.block_rollback()
                l "I'm not interested."
                v "I think it would look good on you! But as you see fit."
                l "Let's go."
                jump v4ivydateend
                
            "Get a piercing":
                $ renpy.block_rollback()
                l "Mhh... Do you think I should get one?"
                v "I think it would look great on you! It looks great on me, after all!"
                l "I never really considered it, but maybe you're right."
                l "Why not, I'll get one done!"
                $ lena_ivy += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                v "Cool, let's take a look!"
    else:
        jump v4ivydateend
        
    "We went to the part of the store where the tattoo and piercing studio was located."
    "The wall was covered with tattoo designs and a selection of various piercings and earrings were on display at the counter."
    if lena_go_piercing == 2:
        "I was excited about getting my first piercing done. I had been considering it for quite some time, but never actually went through with it."
        "Now it was the perfect moment, and I couldn't wait to look sexier and more confident."
    else:
        "Getting this piercing done had been a sudden decision, and maybe because of that I was excited about it."
        "I had the feeling it would make me look sexy and confident."
    v "Which one are you going to pick?"
    hide ivy 
    hide lena
    with short
    call screen v4navelpiercing
    if lena_piercing1:
        show v4_navel1
        l "I'll get this one."
        v "It's like mine! Nice choice!"
    if lena_piercing2:
        show v4_navel2
        l "I like this one."
        v "That one's cute! It suits you, ha ha."
    $ flena = "sad"
    l "It's expensive, though... Buying that toy and also getting the piercing done will take some cash out of my pocket..."
    l "I'm not sure I can afford that now."
    v "Don't worry, I'll pay for it."
    $ flena = "worried"
    l "I can't ask you to do that!"
    v "Don't worry! It's not a lot of money by any means, and this month my finances are looking pretty great, ha ha."
    v "It's my treat."
    $ flena = "smile"
    l "Thank you, Ivy."
    v "That's what friends are for!"
    scene sexshop
    with long
    "It was quick and less painful than I had anticipated."
    "In a matter of minutes I had my first piercing done." 
        
label v4ivydateend: 
    scene street
    with long
    if lena_piercing1 or lena_piercing2:
        $ flena = "happy"
        $ fivy = "smile"
    show lena at rig
    show ivy at lef
    with short
    if lena_piercing1 or lena_piercing2:
        v "You look fabulous!"
        l "You think so? It's a small change, but I feel it makes quite a difference..."
        v "It does. You look even hotter, now. It seems my influence is finally doing something, ha ha!"
        l "I'm happy I got it, but I feel it might take some time for me to get used to it..."
        v "Nah, you'll get used to it in no time."
        v "Next step is for you to get some better clothes and maybe a cool tattoo!"
        $ flena = "n"
        l "Hey, what's wrong with my clothes?"
        v "Nothing... But you could do so much better! Don't waste your potential, girl!"
        "She pointed at the plastic bag I was carrying, with the plug and the lube."
        v "And I hope you enjoy your purchase, hee hee!"
    else:
        "We went out of the shop. I was carrying a small plastic bag with the plug and the lube."
        l "That was an interesting shop."
        v "It was, right? I hope you enjoy your purchase, hee hee!"
    l "Ivy..."
    if v3_axel_call:
        l "Oh, by the way... There's something I haven't told you yet."
        l "I called Axel yesterday."
        $ fivy = "n"
        v "Oh, you did? And how was it?"
        if v4_axel_date:
            $ flena = "sad"
            l "Well... He was very apologetic, and I believe he was being honest."
            l "I tried to do as you said, listening to him, not getting riled up..."
            v "So it went well?"
            l "I guess so. I'm meeting him tomorrow."
            $ fivy = "surprise"
            v "You are? How come?"
            l "He wanted to tell me his feelings and apologize face to face... And he has something of mine to give back."
            $ fivy = "n"
            v "I see. And how are you feeling about seeing him again?"
            l "I'm not sure... I don't know if I should've agreed."
            l "I'm a bit nervous."
            v "It's normal... Just try to keep your head cool and don't forget what it is that you want."
            v "As long as you have that clear things will play out as you want them to."
            $ flena = "n"
            l "Thanks."
            v "Be sure to tell me how that goes!"            
        else:
            l "I'm done with him. I listened to his excuses, I told him my feelings and asked him to leave me alone once and for all."
            l "It's time for us to move forward."
            v "And how did he react?"
            l "Better than I expected... He was very apologetic, in fact. And I believe he was honest..."
            l "But he wanted us to meet, and I said no. I'm sure he didn't like that, but that's how it is."
            v "You did more than enough. You talked to him, as he wanted, and now it is his turn to give you what you want."
            l "Exactly."
            
    v "Anyways, I loved hanging out with you today! Thanks for coming with me."
    l "It was great. Thanks for listening to me."
    v "Always! We need to hang out more!"
    v "You've never come to see me at the club! Why don't you come this weekend? You'll be free, right?"
    l "Yes... It will be my first free weekend in a long time."
    v "Let's celebrate together then!"
    v "Gotta go! See you at the gym!"
    
    scene lenahome
    with long
    show lena
    with short
    "I went back home and cooked myself some dinner."
    "The mood was weird after the fight Louise and Stan had had this morning."
    if louise_jeremy == False:
        "Even more so after I told Louise about Jeremy's behavior..."
    "None of them came out of their room during the whole afternoon."
    if v2_ian_date:
        play sound "sfx/sms.mp3"
        l "A message... Oh, it's Ian's."
        if v3_ian_date:
            i "{i}Hey Lena, what's up? I had a lot of fun last Wednesday.{/i}"
            i "{i}I was wondering if you'd like to meet again this week.{/i}"
        else:
            i "{i}Hey Lena, what's up? I'm sorry I couldn't come last Wednesday.{/i}"
            i "{i}I was wondering if you'd like to meet this week, maybe.{/i}"
        if lena_go_ian == 2:
            $ v4_ian_date = True
            $ flena = "smile"
            if v3_ian_date:     
                l "{i}I had a lot of fun, too! And yeah, that'd be cool. When is it OK for you?{/i}"
            else:
                l "{i}Don't worry about it... And yeah, that'd be cool. When is it OK for you?{/i}"
            i "{i}How about Wednesday again?{/i}"
            l "{i}Sound good to me!{/i}"
            i "{i}Cool. I'm eager to see you.{/i}"
            $ flena = "shy"
            l "Oh, he's eager to see me? How cute..."
            l "{i}Me, too. See you on Wednesday!{/i} {image=emoji_kiss.png}"
        else:
            menu:
                "Meet with Ian":
                    $ renpy.block_rollback()
                    $ v4_ian_date = True
                    "I decided it was worth going for a second date."
                    if v3_ian_date:     
                        l "{i}I had a lot of fun, too! And yeah, that'd be cool. When is it OK for you?{/i}"
                    else:
                        l "{i}Don't worry about it... And yeah, that'd be cool. When is it OK for you?{/i}"
                    i "{i}How about Wednesday again?{/i}"
                    l "{i}Sound good to me!{/i}"
                    i "{i}Cool. I'm eager to see you.{/i}"
                    $ flena = "shy"
                    l "Oh, he's eager to see me? How cute..."
                    l "{i}Me, too. See you on Wednesday!{/i}"
                    
                "Avoid him":
                    $ renpy.block_rollback()
                    $ lena_go_ian = 0
                    "I didn't really feel like going on another date with Ian..."
                    "Not at this moment, at least."
                    l "{i}Hey, Ian. Sorry, but I'm really busy this week.{/i}"
                    l "{i}There've been a lot of changes in my life and it's not really a good time right now...{/i}"
                    i "{i}I see. Don't worry then. I'll see you at the café.{/i}"
                    l "{i}Sure!{/i}"
                    l "So that's that..."
            
    "I relaxed a bit until it was time to go to work."
    "My last Saturday at the restaurant..."
    
## LENA SUNDAY - AXEL ################################################################################################################################################################################################################
    
    $ day = "Sunday"
    stop music fadeout 2.0
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    play music "music/normal_day.mp3" loop
    if v4_axel_date:
        $ flena = "worried"
        show lenabra
        with short
        "I got up pretty early next morning."
        "The night at the restaurant had been intense and I hadn't managed to get much sleep."
        "But the main reason I had trouble sleeping was the anxiety meeting Axel was causing me."
        l "I'm meeting him in just a few hours..."
        "I took a deep breath."
        l "I should get ready."
    else:
        "Last night at the restaurant had been intense and tiresome, but thankfully I could sleep in this morning."
        $ flena = "n"
        show lenabra 
        with short
        l "Mhhh... No more long and busy Sunday nights for me... It's kind of liberating."
        l "I have the whole day to myself..."
        "I had been in need of a day to do nothing and relax. I could laze around in bed, play some guitar..."
        l "But first, a shower and a hearty breakfast!"
    scene lenahome
    show lena
    with long
    if v4_axel_date:
        "I had still some time before meeting Axel at the café."
        "I tried to calm my mind by focusing on something else for a while... I decided to check my social media."
        $ flena = "n"
    else:
        "While I had breakfast I decided to check my social media."
    l "I haven't uploaded anything on Peoplegram for a while..."
    if v3_pg_ian:
        l "Last picture I posted was Ian's drawing... It received mixed reactions."
        if stalkfap:
            l "Maybe that's why I have so few subscribers on Stalkfap..."
            l "I guess I should post more stuff, both on Peoplegram and Stalkfap."
    elif v3_pg_danny:
        l "Last picture I posted was Danny's photo... People liked it very much."
        if stalkfap:
            $ flena = "happy"
            l "I've got a few more Stalkfap subscribers thanks to that..."
            l "Thanks to those I have some pocket money to spend!"
            $ lena_money += 1
            show money_up
            play sound "sfx/moneyup.mp3"
            l "I should keep posting stuff both on Peoplegram and on Stalkfap to keep this up..."
    "I thought about the advice Ivy had given me yesterday."
    $ flena = "worried"
    l "But I don't have anything good enough to post right now. No more pro pictures..."
    l "Maybe I could post a selfie, but I should get some more pics taken."
    l "I guess I should give Danny a call..."
    hide lena
    show lena_phone
    with short
    play sound "sfx/ring.mp3"
    l "..."
    show phone_danny at lef3
    with short
    dan "Hello, Lena! How are you?"
    l "Hi, Danny. I was thinking about our last time working together and how wonderful the pics you took are..."
    dan "I'm glad you liked it! We should work together again!"
    l "That's exactly why I'm calling. How about we do another photo-shoot soon?"
    hide phone_danny
    show phone_danny_sad at lef3
    dan "Soon, huh...?"
    $ flena = "sad"
    l "Is there a problem?"
    dan "I'm afraid I can't afford to pay you right now. Budget is quite tight..."
    dan "I spent all I had saved to hire you and other models for my last project, and I'm still waiting to get some return from that..."
    if v1_choosepic == 3:
        l "Didn't you say you had a high chance at winning the prize form that exhibition?"
        hide phone_danny_sad
        show phone_danny at lef3
        dan "Yes, in fact, I did!"
        $ flena = "n"
        l "Really? Congratulations!"
        l "Haven't you collected it yet?"
        dan "No, not yet... These things take some time."        
    if v1_choosepic == 2:
        l "Didn't you say you had a high chance at winning the prize form that exhibition?"
        dan "Yeah... I wasn't lucky in the end."
        l "Oh, I'm sorry..."
        dan "But I received really good critiques. That should ensure me some paid work."
    l "Will that take long? I'm in a bit of a hurry..."
    dan "You need those pictures for something?"
    l "I'd like to post them on my social media, to build up my personal brand..."
    dan "I see... You know, photographers normally pay models to pose for them because we hire you for our projects..."
    dan "But when it's a model who needs the photographer normally it's the other way around. We need to get paid, too..."
    l "Are you saying you could shoot me if I pay you?"
    dan "That's how it usually works, yeah."
    "Danny had a point. This time it was me who was in need of his services."
    "My budget was really tight too, though... Probably tighter than his was."
    menu:
        "{image=icon_charisma.png}Convince him to do it for free" if lena_charisma > 2 or v1_choosepic == 3:
            $ renpy.block_rollback()
            $ v4_danny_shoot = True
            $ flena = "n"
            if v1_choosepic == 3:
                l "I'm not asking you to pay me. I can't pay you either, but you'll be cashing in that prize soon!"
                dan "That's true."
            else:
                l "I can't pay you right now, my financial situation is complicated, too... But you said you loved working with me."
                l "I'm not asking you to pay me, though."
            l "We can just exchange services. I pose for you, you take pics for me."
            l "How does that sound?"
            dan "Someone has to pay for the photo studio... But I can't say no to you."
            $ flena = "happy"
            l "Thanks, Danny!"
            hide phone_danny_sad
            hide phone_danny
            show phone_danny at lef3
            dan "Let me check my schedule before agreeing on a day next week."
            l "Sure, no problem. Keep me posted!"
            dan "Bye, Lena!"
            hide lena_phone
            show lena 
            hide phone_danny
            hide phone_danny_sad
            with short
            $ flena = "n"
            l "Nice, I managed to convince him."
            
        "{image=icon_pay.png}Hire Danny" if lena_money > 0:
            $ renpy.block_rollback()
            $ v4_danny_shoot = True
            l "I really need those pics... OK, I'll hire you."
            hide phone_danny_sad
            hide phone_danny
            show phone_danny at lef3
            dan "Thanks, Lena. You know I'd shoot your for free, but renting the studio and the equipment takes money..."
            dan "And editing the pictures takes time, too, even though I don't mind that..."
            $ flena = "n"
            l "It's OK, I understand. You're a professional, same as me."
            l "We need to get paid."
            dan "I'm glad you understand. I'll charge you as little as possible."
            l "Thanks, Danny."
            $ lena_money -= 1
            show money_down
            play sound "sfx/moneydown.mp3"
            dan "Let me check my schedule before agreeing on a day next week."
            l "Sure, no problem. Keep me posted!"
            dan "Bye, Lena!"
            hide lena_phone
            show lena 
            hide phone_danny
            hide phone_danny_sad
            with short
            l "It will cost me money... But it's an investment. Though a risky one at that, especially considering my current situation."
            l "I hope I will get a good return. I really need it..."
            
        "{image=icon_friend}I can ask Stan instead..." if lena_stan > 4 and lena_stan_model_cash or lena_stan_model_free:
            $ renpy.block_rollback()
            $ v4_stan_shoot = True
            "A thought occurred to me: I could ask Stan to take the pictures instead..."
            "He wasn't a pro, but with some practice and guidance he could take some OK pictures..."
            "I could use those until Danny wanted to work with me again or I earned some money to pay him."
            l "I can't afford it right now, I'm sorry."
            hide phone_danny_sad
            hide phone_danny
            show phone_danny_sad at lef3
            dan "No, it's me who's sorry... You know I'd shoot you for free, but renting the studio and the equipment takes money..."
            dan "And editing the pictures takes time, too, even though I don't mind that..."
            $ flena = "n"
            l "It's OK, I understand. You're a professional, same as me."
            l "We need to get paid."
            dan "I'll give you a call as soon as I'm in need of hiring a model."
            dan "You're the first one I want to work with!"
            l "Thanks, Danny. Bye."
            hide lena_phone
            show lena 
            hide phone_danny
            hide phone_danny_sad
            with short
            l "I'll pitch my idea to Stan when I see him..."
            if lena_stan_model_cash:
                l "If I play my cards right I can even convince him to pay me for posing for him..."
        
        "I can't afford it":
            $ renpy.block_rollback()
            l "I can't afford it right now, I'm sorry."
            hide phone_danny_sad
            hide phone_danny
            show phone_danny_sad at lef3
            dan "No, it's me who's sorry... You know I'd shoot your for free, but renting the studio and the equipment takes money..."
            dan "And editing the pictures takes time too, even though I don't mind about that..."
            $ flena = "n"
            l "It's OK, I understand. You're a professional, same as me."
            l "We need to get paid."
            dan "I'll give you a call as soon as I'm in need of hiring a model."
            dan "You're the first one I want to work with!"
            l "Thanks, Danny. Bye."
            hide lena_phone
            show lena 
            hide phone_danny
            hide phone_danny_sad
            with short
            $ flena = "sad"
            l "Well, that's a no go..."
            l "I will need to get new pictures some other way."
   
    if v4_axel_date:
        stop music fadeout 2.0
        $ flena = "worried"
        l "Enough about that, now. I need to go and meet Axel..."
        "It was finally time. I got up and left for the café."
        jump v4axelcafe
        
    elif v4_seymour_date:
        stop music fadeout 2.0
        play sound "sfx/ring.mp3"
        "As soon as I put my phone down I got another call."
        l "It's Seymour."
        hide lena
        show lena_phone
        show phone_seymour at lef3
        with short
        l "Yes?"
        mr "Hello Lena. I wanted to inform you about that photo-shoot we agreed upon."
        l "The offer still stands?"
        mr "Oh, yes. I know we talked about it being next week, but I had to re-work my schedule."
        mr "It has to be this afternoon."
        l "Oh."
        mr "Is that a problem?"
        l "No... It's unexpected, but I can make it."
        mr "Excellent. I'll be waiting for you at the studio, then."
        mr "See you later, Lena."
        hide phone_seymour
        hide lena_phone
        show lena 
        with short
        l "Seems I won't get the whole day off, after all..."
        l "Well, it's OK. I was just in need of some new pictures, and of money."
        jump v4seymourshoot
        
    else:
        "I took the rest of the day easy, resting and gathering my thoughts."
        scene lenaroomnight
        show lena
        with long
        "I had almost forgotten how good it felt to do nothing all day..."
        "Sadly, I couldn't afford too many days like this one."
        stop music fadeout 2.0
        jump v4masturbation
        
## AXEL DATE ########################################################################################################################################################################################################
       
label v4axelcafe:
    
    scene street
    with long
    $ lena_look = 1
    show lena
    with short
    "As I walked to the café I tried to focus, remembering what Ivy had told me."
    "As long as I kept my head cool things would go like I wanted them to."
    "But what was the thing I wanted?"
    l "I guess I'm about to find out..."
    "I took a deep breath and entered the café."
    scene cafe
    with long
    show lena at rig
    with short
    "As soon as I went in I caught Molly's eyes."
    $ fmolly = "sad"
    show molly at lef3
    with short
    "Knowing she was concerned about me and that she had my back put me at ease, if only a bit."
    "She subtly pointed to a corner of the shop with her head, and I looked in that direction."
    hide molly
    with short
    play music "music/lenas_theme.mp3" loop
    $ axel_look = 1
    $ faxel = "sad"
    show axel at lef
    with short
    "There he was, sitting at a table and waiting for me."
    x "Lena..."
    "He stood up to greet me, but I sat down in front of him right away."
    "He looked at me briefly and sat down again."
    x "Hi, Lena..."
    menu:
        "Hello, Axel":
            $ renpy.block_rollback()
            l "Hello, Axel. How are you?"
            $ lena_axel += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            x "I'm... A mix of ashamed, thankful and relieved."  
            hide friend_up
        "Cut to the chase":
            $ renpy.block_rollback()
            $ flena = "serious"
            l "Cut to the chase, Axel..."
            l "I've come here to listen to you, so say what you need to say..."
    x "Thank you for showing up. I know it's more than I deserve."
    x "But I needed to see you... To tell you I'm sorry face to face."
    l "The way you've been acting lately doesn't make you look like you're sorry."
    x "I know, I'm... I'm so ashamed. About everything."
    x "When I saw you at the restaurant... I wasn't prepared. I had no idea you worked there."
    x "Stumbling upon you all of a sudden, it was a shock. It made me lose my cool."
    x "Only you have that effect on me, you know that..."
    l "I wish I didn't..."
    x "I know. I got desperate. After you had shut me off I couldn't resist. I had to talk to you."
    x "I felt that if I let that moment pass I would never get that chance ever again..."
    l "That's why you came looking for me the next day and acted like a psycho?"
    "He sighed."
    x "Yeah... I got crazy, I know. I'm so sorry for showing up at your parents' place."
    x "But I was losing my mind. I needed to talk to you."
    x "Not to ask you to come back to me. Not even to ask for your forgiveness..."
    x "I just wanted to say how sorry I am that I hurt you."
    menu:
        "You did more than hurting me":
            $ renpy.block_rollback()
            $ flena = "sad"
            l "You did more than just hurting me, Axel."
            l "You tricked me, you humiliated me, you broke my trust."
            l "You made me feel like a fool, like I was being used."
            l "Not only did you cheat on me for who knows how long, you brought her into our bed without me knowing..."
            l "I was supposed to be your girlfriend, the one you loved, and I trusted you enough to agree to that..."
            l "Yet I was the only one who did not know what was going on. I was the lamb and you two were the wolves."
            x "I... It hurts so much hearing you say those words, because I can see how much I hurt you."
            
        "You betrayed me!":
            $ renpy.block_rollback()
            $ flena = "serious"
            l "You betrayed me, fooled me, used me!"
            l "You cheated on me for who knows how long! And then you brought that girl into our bed!"
            l "I was stupid enough to agree to that, because I trusted you! But I was the only one who had no idea what was going on there."
            l "You two conspired behind my back and treated me like... Like I was your toy..."
            x "You know it wasn't like that..."
            if lena_axel > 0:
                $ lena_axel -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
            l "Don't tell me what it was like!"
            x "You're right. I understand you felt that way. You have plenty of reasons."
            x "Hearing it from you only makes me see myself in that light, and it's awful, but..."
            
    x "As I said, I'm not here to make excuses. I wish I had done things differently, but I was a fool."
    x "I never deserved you and it's just right that you hate me..."
    x "I don't think I can repair the damage done... All I can do is come before you and admit my guilt."
    $ flena = "sad"
    x "I was a complete asshole, and I'm so sorry."
    x "Thank you for allowing me the chance to apologize."
    x "The regret and remorse will not disappear... But I felt I wouldn't be able to move forward unless I did."
    menu:
        "Thank you for your apology":
            $ renpy.block_rollback()
            l "Thank you for your apology... I can see it's sincere."
            x "..."
            $ faxel = "smile"
            if lena_axel < 3:
                $ lena_axel += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            x "I don't even know what to say."
            l "I guess you've said it all..."
            x "Still, it feels like there are some things left unsaid, even if I can't find them." 
            l "There will always be, I suppose."
            hide friend_up
            
        "You have what you wanted":
            $ renpy.block_rollback()
            l "Well, you have what you wanted. I listened to you, so now what?"
            $ faxel = "smile"
            x "I don't know. This is as far as I had planned."
            
    x "I know you don't want me in your life, and I know you can't forgive me."
    x "I understand both. I just hope that now that we've talked, there's no need to run away or turn the head the other way around if by chance we meet again."
    l "We can be civil... As long as you don't start acting crazy again."
    x "It won't happen again, I promise. I got everything off my chest today."
    x "Oh, by the way..."
    "Axel picked up something from a bag and put it on the table."
    "My notebooks."
    x "Here. This belongs to you."
    l "Thanks... It's good to have them back."
    x "Do you still write songs?"
    menu:
        "I do":
            $ renpy.block_rollback()
            $ flena = "n"
            l "I do, sometimes."
            if lena_axel < 3:
                $ lena_axel += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            x "You had so much talent and a great sensibility... Your letters were true poetry."
            l "It's just a hobby..."
            x "You put too much passion in it to call it just a hobby. I'm glad you haven't lost that passion, and that you keep writing."
            l "What about you? How's your career as a photographer going?"
            x "I can't complain... I'm making important connections and there's no shortage of work."
            x "I'm really lucky in that regard..."
            l "You always knew how to achieve your goals."
            x "I don't know about that... I just kept trying and working hard."
            x "Anyways... I won't take more of your time."
            
        "This conversation is over":
            $ renpy.block_rollback()
            $ flena = "worried"
            l "Sorry, but I'm not in the mood to make small talk right now..."
            $ faxel = "n"
            x "Of course. I understand..."
            
    "Axel got up."
    x "Again, thanks for coming here today, Lena. And for listening to me."
    $ faxel = "smile"
    x "I'm glad to have seen you again, and to have talked. Please, take care."
    "He smiled at me one last time and left."
    stop music fadeout 2.0
    hide axel
    with short
    l "..."
    show molly at lef
    with short
    mo "How are you, Lena? It went well?"
    l "I guess it did... Not exactly how I expected."
    $ fmolly = "n"
    mo "That's good, isn't it?"
    $ flena = "n"
    l "Yes, it is. Thank you for worrying about me, Molly."
    mo "It's the least I can do..."
    l "I'm gonna go. I need to think about what was said..."
    mo "Of course. If you need to take the day off tomorrow just let me know."
    l "No, no. I will come, don't worry."
    l "See you tomorrow!"
    scene street
    with long
    show lena
    with short           
    if v4_seymour_date:
        play sound "sfx/ring.mp3"
        "As soon as I exited the café I got a phone call."
        l "It's Seymour..."
        hide lena
        show lena_phone
        show phone_seymour at lef3
        with short
        l "Yes?"
        mr "Hello Lena. I wanted to inform you about that photo-shoot we agreed upon."
        l "The offer still stands?"
        mr "Oh, yes. I know we talked about it being next week, but I had to re-work my schedule."
        mr "It has to be this afternoon."
        l "Oh."
        mr "Is that a problem?"
        l "No... It's unexpected, but I can make it."
        mr "Excellent. I'll be waiting for you at the studio, then."
        mr "See you later, Lena."
        hide phone_seymour
        hide lena_phone
        show lena 
        with short
        "I didn't feel especially ready for a photo-shoot after having just met Axel..."
        "My emotions had been stirred up and all I wanted was to go home, sit and think..."
        "But this was an appointment I couldn't afford to miss."
        jump v4seymourshoot
    else:
        "So, that was done..."
        "I had feared that encounter so much, and in the end it wasn't as bad as I had feared, not at all."
        "Still, meeting with Axel had stirred up my emotions..."
        "I decided to go home and take the rest of the day to think and relax."
        jump v4masturbation
        
## SEYMOUR PHOTOSHOOT ########################################################################################################################################################################################################
      
label v4seymourshoot:
    
    scene studio_black
    with long
    play music "music/flirty.mp3" loop
    $ flena = "n"
    $ seymour_look = 2
    $ fseymour = "n"
    show lena at rig
    with short
    "I arrived at the studio at the agreed-upon hour."
    "Seymour was already waiting for me."
    show seymour2 at lef
    with short
    mr "Ah, Lena. There you are, at last."
    l "I'm not late, am I?"
    mr "No, you're here at the expected hour. Let's not waste any time."
    mr "I want to shoot you in lingerie. You'll find a set and a pair of shoes I provided in the backroom, put them on."
    "His voice commanded authority and his words were direct and concise."
    "Down to business right away."
    l "Sure..."
    hide seymour2
    with short
    show lena at truecenter
    with move
    "I got into the small equipment room and picked up a bag that was sitting on a chair."
    $ flena = "surprise"
    "There was a big golden {i}B{/i} on the bag: the unmistakable logo of one of the most famous and fancy fashion brands in the world."
    l "Bellucci! These must be incredibly expensive...!"
    if lena_posh > 1:
        $ flena = "happy"
        l "Wow, these are so nice! Look at the quality of the fabric, and the embroidery..."
        l "And those shoes! They're amazing."
        l "I can't wait to wear this!"
    elif lena_posh > 0:
        l "Wow, I can tell the quality of the fabric, and the shoes are really nice..."
        l "No wonder they are that expensive, this feels like a luxury."
    else:
        $ flena = "worried"
        l "I can tell the quality of the fabric, and the shoes feel really comfortable..."
        $ flena = "worried"
        l "Still, not worth the sum of money they charge for these."
        l "I doubt I'll ever be wearing something like this outside the studio."
        $ flena = "n"
    l "Let's see how these fit me..."
    hide lena
    with short
    "I got out of my clothes and into the lingerie Seymour had brought."
    $ lena_look = "black_lingerie"
    if lena_posh > 1:
        $ flena = "shy"
    show lenabra
    with long
    if lena_posh > 1 or lena_lust > 2:
        l "It's perfect!"
        l "I know I shouldn't get so excited about this, but I really like lingerie!"
        l "This is by far the nicest set I've ever worn."
    else:
        l "It fits like a glove."
        l "I don't think I ever gave Seymour my measurements..."
        l "Either he found them somewhere himself or he has really good eye."
    show lenabra at rig
    with move
    $ fseymour = "smile"
    show seymour2 at lef
    with short
    mr "Oh, these look wonderful on you. Even better than expected."
    if lena_seymour < 6:
        $ lena_seymour = 6
        play sound "sfx/friendup.mp3"
        show friend_up
    "He seemed pleased. In fact, it was the first time I was seeing him smile since I had arrived."
    l "So... What do you want? You never told me what kind of photos you were looking to take."
    mr "I didn't? Well, I thought you could tell from our conversations..."
    mr "I'll be more clear."
    mr "I'm interested in portraying the sensuality and seduction of the muse."
    mr "That impetuous force only a female can possess, that magnetic {i}anima{/i} that draws men in, like a black hole."
    if lena_wits > 2:
        l "Sure."
        "That was just a fancy way of saying he wanted me in a sexy and provocative attitude."
        "It seems this was his way of being \"more clear\"..."
    elif lena_wits > 1:
        l "Um... OK."
        "If that was his way of being clear..."
        "Amongst his metaphors and fancy words I understood he wanted something on the sexier side."
    else:
        l "Um... OK."
        $ flena = "worried"
        "I wasn't sure I got what he was talking about..."
        "His metaphors and complicated words didn't convey the idea too clearly."
    stop music fadeout 2.0
    l "Do you have any other indications?"
    mr "Let me familiarize myself with you. Start by presenting yourself in a straightforward way."
    menu:
        "Elegant pose":
            $ renpy.block_rollback()
            play music "music/sensual.mp3" loop
            scene v4_seymour1
            if lena_piercing1:
                show v4_seymour1_p1
            elif lena_piercing2:
                show v4_seymour1_p2
            with long
            "I got in front of the backdrop and adopted a simple and elegant pose."
            "I wasn't going for a specific feeling or intention other than giving Mr. Ward a clear silhouette to shoot."
            play sound "sfx/camera.mp3"
            with flash
            mr "Mhh..."
            mr "That's good, but... I need a bit more."
            l "More?"
            mr "More intent. More pop."
            mr "You're not just being looked at. You're exhibiting yourself."
            l "Perhaps something like..."
            scene v4_seymour2
            if lena_piercing1:
                show v4_seymour2_p1
            elif lena_piercing2:
                show v4_seymour2_p2
            with long
            l "This?"
            mr "Yes. That's more like it. Good..."
            
        "Sultry pose":
            $ renpy.block_rollback()
            play music "music/sensual.mp3" loop
            $ seymour_shoot += 1
            scene v4_seymour2
            if lena_piercing1:
                show v4_seymour2_p1
            elif lena_piercing2:
                show v4_seymour2_p2
            with long
            "I got in front of the backdrop and went for a sultry pose right away."
            "It was a bit cliché, but he wanted something simple, so..."
            play sound "sfx/camera.mp3"
            with flash
            mr "Mhh... That's a good start."
            mr "That's more or less what I'm looking for... No shyness, no remorse."
            mr "You're not just being looked at. You're exhibiting yourself."
    if lena_piercing1 or lena_piercing2:
        mr "I wasn't sure about that navel piercing you've gotten..."
        mr "But it's really fitting for this mood. It enhances your appeal even more..."
        mr "Good choice."
        if seymour_shoot > 0:
            l "Thanks..."
        else:
            l "Thanks... I guess."
    play sound "sfx/camera.mp3"
    scene v4_seymour0
    with flash
    $ fseymour = "n"
    $ flena = "n"
    "Mr. Ward began taking pictures."
    "I continued to give him some easy and simple poses, as he had requested."
    "He sometimes gave me a small indications, but mostly he kept to himself, quietly."
    "His cold blue eyes looked at me with a strange sense of focus, like I was all he cared to pay attention to at that moment."
    "I could see a calculating intelligence behind them, sizing me up, studying me..."
    "It was a bit hard feeling comfortable under his scrutiny."
    "But that wasn't the real reason I felt a bit uneasy... Not the only reason, at least."
    "Mr. Ward had the eyes of a lion stalking his prey."
    scene studio_black
    show seymour2 at lef
    show lenabra2 at rig
    with long
    mr "OK, let's continue. Now I want you to remove the top."
    l "Oh, so you want to do a nude photo-shoot after all."
    mr "That was the deal, wasn't it?"
    l "Sure."
    "I began removing the bra, but Seymour stopped me."
    mr "Not like that. Slow. I want to shoot you while you do it."
    $ flena = "blush"
    l "Oh..."
    mr "This is an integral part of the seduction process. The teasing, the flaunting of a treasure..."
    menu:
        "{image=icon_lust.png}Inviting mood" if lena_lust > 3:
            $ renpy.block_rollback()
            $ seymour_shoot += 2
            scene v4_seymour3c
            if lena_piercing1:
                show v4_seymour3_p1
            elif lena_piercing2:
                show v4_seymour3_p2
            with long
            "I knew what he was asking for, and I decided to give it to him."
            "I stared directly into the lens of the camera, not averting my gaze at any moment."
            "I looked at it like it was my objective, the object of my desire..."
            "The object I wanted to be desired by."
            "At the same time I pulled down the cups of the bra, revealing my breasts."
            play sound "sfx/camera.mp3"
            with flash
            mr "That look in your eyes...! Yes, that's it, very good..."
            mr "Sometimes an image can say as much as a sentence, and often in a clearer way."
            mr "And this picture is saying without a doubt: \"come and get me\"."
            mr "That's the definition of sensuality!"
            
        "Calm mood":
            $ renpy.block_rollback()
            scene v4_seymour3
            if lena_piercing1:
                show v4_seymour3_p1
            elif lena_piercing2:
                show v4_seymour3_p2
            with long
            "I tried to keep that elegant and calm look I had been praised for so many times."
            "It was what I was best at and what photographers valued most about working with me as a model, or so I thought."
            "At the same time I pulled down the cups of the bra, revealing my breasts."
            play sound "sfx/camera.mp3"
            with flash
            mr "Beautiful..."
            mr "You natural appeal conveys desire effortlessly on your part..."
            mr "It's like second nature to you."
            
        "Playful mood":
            $ renpy.block_rollback()
            $ seymour_shoot += 1
            scene v4_seymour3b
            if lena_piercing1:
                show v4_seymour3_p1
            elif lena_piercing2:
                show v4_seymour3_p2
            with long
            "So he wanted me to play a game of teasing, huh...?"
            "I decided to give him what he wanted and play along."
            if lena_lust < 5:
                $ lena_lust_xp += 1
                play sound "sfx/xp.mp3"
                show lust_up
                call screen skillsup
            "As I pulled down the cups of the bra, revealing my breasts, I looked at the camera with a shy smile."
            "I noticed I wasn't able to avoid blushing... And I bit my lip."
            "I had never done anything like this on a photo-shoot..."
            play sound "sfx/camera.mp3"
            with flash
            mr "Magnificent..."
            mr "That vulnerable look in your eyes, yet your playful smile..."
            mr "A sight of femininity that's asking to be conquered..."
    
    "I felt a weird sensation during that moment."
    "I had become quite used to posing nude in front of a camera. But somehow wearing underwear made me feel more exposed than being naked..."
    "When I was wearing nothing at all I was just only me, natural and real. But wearing this lingerie, stripping slowly in front of Seymour..."
    "This had a clear sexual connotation. More so than baring my body right away."
    "I was slowly revealing my nakedness to him, engaging in a game of seduction, even if I was just posing."
    if seymour_shoot > 1:
        "And I was getting into it..."
    else:
        "I felt I should get into it to give him good results, but I was having trouble to do so..."
    "Flirting with the camera, drawing out my provocative and playful side..."
    play sound "sfx/camera.mp3"
    with flash
    "When I finished removing my bra he asked for a new pose."
    mr "Turn around for me."
    if seymour_shoot > 1:
        scene v4_seymour5
        with long
        "I did just that."
        "I turned around... for him."
        "I gave him a sexy pose, sticking my butt out, running my hands down my legs..."
        "I felt the silky texture of the stockings on the tip of my fingers as I turned my head to look back at the camera."
        play sound "sfx/camera.mp3"
        with flash
        mr "Excellent, Lena... This is exactly what I was looking for..."
        mr "Show yourself. Seduce the camera."
        mr "Seduce me."
        "I shifted the weight from one leg to the other, giving a sexy and unashamed view of my ass... and probably my crotch, too."
        play sound "sfx/camera.mp3"
        with flash
        "Each flash of the camera made me want to get even more into this..."
        if lena_lust < 4:
            $ lena_lust_xp += 1
            show lust_up
            play sound "sfx/xp.mp3"
            call screen skillsup
        "I was having fun."
    else:
        scene v4_seymour4
        with long
        "I did as he asked and gave him my back."
        "I rested my hand on my hip and looked back at the camera with a smile."
        "I tried to adopt a feminine pose and teasing attitude..."
        play sound "sfx/camera.mp3"
        with flash
        mr "Good... This is closer to what I was looking for..."
        mr "Show yourself. Seduce the camera."
        "I turned my body a bit, trying to give him a more interesting and sexy silhouette."
        "The curve of my breasts, the curve of my hips, the curve of my legs..."
        "Seymour was taking pictures of all of those with attention and intent."
        "I was easing a bit more into the role he was asking of me, but I couldn't completely shake off the feeling I was being scrutinized at all times..."
        "Like he wasn't only taking pictures, but also taking measures. My measure."
        
    play sound "sfx/camera.mp3"
    with flash
    mr "Alright. Now, let's finish with this."
    mr "Move to that couch over there..."
    scene v4_seymour6
    if lena_piercing1:
        show v4_seymour6_p1
    elif lena_piercing2:
        show v4_seymour6_p2
    with long
    mr "That's it, sit down, face the camera, look at it."
    mr "Spread your legs a bit more..."
    if seymour_shoot > 1:
        "Following his directions felt easy. I didn't hesitate and did as he asked."
        mr "Perfect..."
    else:
        "I gave him what he wanted, heeding his indications..."
        mr "A bit more still... Yes, like that."
    play sound "sfx/camera.mp3"
    with flash  
    "I tilted my head and looked at the camera, exposed to it."
    mr "That's it... You're a lover in waiting."
    mr "The seductress at the top of the mountain, desiring to be taken."
    mr "But if nobody's brave enough to take you, what're you going to do?"
    $ lena_look = "black_lingerie2"
    menu:
        "{image=icon_lust.png}Lure them in" if seymour_shoot > 1 and lena_lust > 2:
            $ renpy.block_rollback()
            $ seymour_shoot = 4
            l "Lure them in..."
            mr "And how would you do that?"
            "I had worked with several photographers, but none spoke to me like he did."
            "The way he was giving me directions was almost like he was making poetry of the moment."
            "I gave him the answer he wanted, but not in words."
            "He wasn't asking for my words."
            scene v4_seymour6b
            if lena_piercing1:
                show v4_seymour6_p1
            elif lena_piercing2:
                show v4_seymour6_p2
            with long
            "It was one of those moments when you think with your body, not with your mind."
            "My hand slid down along my hip and my thigh, until it reached my crotch."
            "I placed it there with a slow and deliberate motion, without averting my eyes from Seymour's camera."
            mr "Yes... Fan their fire... Feed the desire of their hearts."
            mr "That's the way of the seductress... That shining treasure all men want to conquer."
            mr "You offer the dangerous path to triumph, where only the most worthy can succeed."
            "His words were enticing me more than I was enticing his camera."
            "He pulled me towards his vision, his description of sensuality, of desire and of possession of its object..."
            "Before I realized my fingers began moving very slowly and very subtly, caressing my crotch."
            "My sex was demanding to be touched..."
            play sound "sfx/camera.mp3"
            with flash  
            "The flash and the shutter of the camera snapped me back from the haze that had enveloped me."
            $ flena = "blush"
            $ fseymour = "evil"
            scene studio_black
            show lenabra2 at rig
            show seymour2 at lef
            with long
            "I pulled back my hand and I could feel the blood rushing to my cheeks."
            "Thankfully, Seymour seemed satisfied enough with the pictures he had already taken."
            $ fseymour = "smile"
        
        "Wait":
            $ renpy.block_rollback()
            l "Wait... Wait for someone who does."
            mr "That's often the way of the seductress..."
            mr "Waiting for the man who can prove himself... Who's worthy of taking the treasure she offers."
            "I had worked with several photographers, but none spoke to me like he did."
            "I had no idea if he was giving me directions or was just making poetry of the moment."
            play sound "sfx/camera.mp3"
            with flash  
            "Seymour took several more pictures of me sitting on the couch, flirting with the camera."
            "After a few minutes, he seemed satisfied enough."
            $ fseymour = "smile"
            $ flena = "n"
            scene studio_black
            show lenabra2 at rig
            show seymour2 at lef
            with long
            
        "Stay silent":
            $ renpy.block_rollback()
            l "..."
            "I didn't know if he was expecting me to answer that question or it was just a figure of speech."
            "I decided to stay silent and focus on posing."
            play sound "sfx/camera.mp3"
            with flash  
            "Seymour took several more pictures of me sitting on the couch, flirting with the camera."
            "After a few minutes, he seemed satisfied enough."
            $ fseymour = "smile"
            $ flena = "n"
            scene studio_black
            show lenabra2 at rig
            show seymour2 at lef
            with long

    stop music fadeout 2.0
    mr "Good, I think that's everything."
    l "Are we done?"
    mr "Yes, it's getting late and I have enough material to revise."
    mr "I don't know if my skills as a photographer will produce any good results, but you were an excellent model."
    if seymour_shoot > 2:
        mr "Even better than I expected."
        if seymour_shoot == 4:
            mr "Way better."
            mr "I hope I managed to direct you properly during the shoot."
            l "You did..."
            "He directed too well, even. I got so much into it I almost lost myself."
            "But wasn't that the actual purpose of a good model? To embody what the artist asked of her?"
            "I had never felt so compelled to do so in any of my previous photo-shoots..."
            $ flena = "n"
            l "Yes, you did... Your descriptions were very colorful and passionate..."
            l "I enjoyed the experience."
        else:
            mr "I hope I managed to direct you properly during the shoot."
            l "Yes, you did... Your descriptions were very colorful and passionate..."
            l "I enjoyed the experience."
    elif seymour_shoot > 1:
        mr "As good as I expected."
        mr "I hope I managed to direct you properly during the shoot."
        l "You did. You were very colorful and detailed in your descriptions."
        l "They helped me get into the acting."
    else:
        mr "I haven't managed to fully connect with you yet, but that's to be expected."
        mr "I'll blame it on my inexperience."
        l "You were very colorful and detailed in your descriptions."
    mr "Once a writer, always a writer, I guess... Even if I stopped writing quite a long time ago."
    mr "But I'm glad you think it went well."
    mr "I'm in a bit of a hurry, so I'll be leaving while you change."
    l "What about the lingerie and the shoes?"
    mr "You can have them. I bought them for you, after all..."
    mr "And it wouldn't be fun using the same outfit with another model."
    if lena_posh > 1:
        $ flena = "happy"
        "I wasn't expecting that! I got to bring the lingerie home with me!"
        "This lingerie was really awesome and really expensive, probably more than what he was paying me for the photo-shoot!"
        $ flena = "n"
    else:
        "I wasn't expecting that... This lingerie was really expensive, probably more than what he was paying me for the photo-shoot."
    mr "I've left your payment on the table next to the door."
    if seymour_shoot > 2:
        mr "And I will throw in a little extra, since working with you was such a good experience."
    l "Before you go... Can I ask you something?"
    mr "Of course."
    l "Would you send me the pictures we've taken today? I'd like to post a few on my social media."
    $ fseymour = "n"
    mr "Mhh... I don't think I'm comfortable with exposing my work yet. I'm an amateur still, after all."
    mr "I'm not against sending them to you, but I don't want my artwork posted unless I'm completely happy with the results."
    l "Oh, I see... I understand."
    mr "Anyways, I'll talk to you soon, Lena. Bye."
    hide seymour2
    with short
    "I went to the table and picked up my payment."
    show lenabra2 at truecenter
    with move
    if seymour_shoot > 2:
        play sound "sfx/moneyup.mp3"
        show money_up
        $ lena_money += 2
        l "Great! This bonus will really help me at the end of this month."
        l "I knew he would be a generous employer..."
    else:
        play sound "sfx/moneyup.mp3"
        show money_up
        $ lena_money += 1
        l "Good, I need all I can get right now."
    scene studio_black
    with long
    "I changed back, put the shoes and the lingerie back in the bag, picked it up and went back home."
    
## LENA MASTURBATION ########################################################################################################################################################################################################
        
label v4masturbation:
     
    scene lenaroomnight
    with long
    $ lena_look = 1
    show lena2
    with short
    if v4_seymour_date:
        "Once home I cooked some dinner and I ate alone. Louise and Stan were still confined to their rooms."
        if seymour_shoot > 2:
            "The photo-shoot with Mr. Ward had been a very interesting experience..."
            "Different from what I was used to. I had enjoyed it."
            if seymour_shoot > 3:
                $ flena = "blush"
                "A bit too much, maybe..."
                l "I have no idea what got into me..."
                $ flena = "n"
                l "At least I got some extra money for it. And the lingerie."
            else:
                l "And I got some extra money for it! And the lingerie."
        elif seymour_shoot > 1:
            "I could say the photo-shoot with Mr. Ward had been an interesting experience, after all."
            "Different from what I was used to. I had enjoyed it."
            "And I had gotten some free lingerie."
        else:
            "The photo-shoot with Mr. Ward had been a weird experience... Interesting, maybe, but still weird."
            "It had been different from any of the previous photo-shoots I had done."
            "I had the lingerie to show for it."
    else:
        "The day went on and my free Sunday came to an end."
    hide lena2
    show lenaunder
    with short
    if lena_piercing1 or lena_piercing2: 
        "Before going to bed I made sure to take care of my piercing, cleaning and disinfecting it."
        "I was happy with my choice... It looked good on me."
    else:
        "I prepared to go to bed."
##AXEL PICS
    if v4_axel_date:
        "I thought about my meeting with Axel..."
        if lena_axel > 2:
            "It had been a weird sensation. Confronting him after all this time..."
            "It went better than expected, though. I felt his apology was sincere, and he didn't ask anything of me."
            "Maybe he was maturing..."
        elif lena_axel > 1:
            "I hadn't been sure about seeing him, but in the end it hadn't been as bad as I'd feared."
            "We could sit down and talk like adults. And he didn't ask anything of me."
        else:
            "I still wasn't sure giving him what he wanted was the right move... But it seemed to have gone well."
            "I hoped we managed to finally settle things."
        "I looked at the notebooks laying on top of my desk. My old notebooks..."
        "I picked one up. I had thought I would never see them again."
        "I flipped through the pages, reading some of the old songs I had written. Some were good, others not so much..."
        $ flena = "surprise"
        "Then I found something tucked between the pages."
        l "Those are...!"
        show lenaunder at right
        with move
        $ flena = "blush"
        show v4_polaroid4
        show v4_polaroid3
        show v4_polaroid2
        show v4_polaroid1
        with short
        l "Axel and I took these Polaroids on the day of his birthday..."
        l "What are they doing here? Did I put them into my notebook back then?"
        "Seeing these images all of a sudden was a shock. Memories rushed back, pleasant at the time, not so much now..."
        "I was wearing that collar Axel had bought for me... Back when I was devoted to him, back when I didn't know what he was doing behind my back."
        "I had been happy during those days... Easier days than the actual ones. Pleasant days..."
        menu:
            "Destroy the pictures":
                $ renpy.block_rollback()
                $ axel_pictures_destroy = True
                $ flena = "serious"
                "I shook my head."
                "I didn't want to get dragged into this. It was the opposite of what I wanted."
                "I wasn't sure how these pictures had ended up inside my notebook. Maybe I had left them there, or maybe Axel had put them intentionally..."
                "Either way, I did not want them. Those memories were not welcome."
                "They should remain a thing of the past."
                play sound "sfx/rip.mp3"
                hide v4_polaroid4
                hide v4_polaroid3
                hide v4_polaroid2
                hide v4_polaroid1
                with vpunch
                "I ripped them apart without even looking at them."
                call screen willup
                l "I won't be dragged into this."
                "I crumpled the pieces and threw them into the bin."
                show lenaunder at truecenter
                with move
                $ flena = "blush"
                "Seeing that one picture had stirred up my feelings again, though..."
                "I felt a strange mix of emotions inside me."
                l "I want to think about something else... Ease my mind a bit..."
                "My body provided me with the answer."
                
            "Look at another picture":
                $ renpy.block_rollback()
                "With trembling hands I revealed another one of the stacked Polaroids."
                play sound "sfx/paper_click.mp3"
                hide v4_polaroid1
                with moveoutleft
                play music "music/sensual.mp3" loop
                l "Oh, my..."
                "I remembered we had taken several pictures that day."
                "Both naked, in front of the mirror, spending the day together at Axel's place..."
                "The memories became clearer, brought forth by the picture."
                "Seeing both of us together again, his strong frame next to mine, his arm around my waist, claiming me as he liked to do..."
                if lena_lust < 4:
                    $ lena_lust_xp += 1
                    play sound "sfx/xp.mp3"
                    show lust_up
                    call screen skillsup
                "I felt my heart starting to race and my gut shrank. Why was I looking at these pictures?"
                "Remembering all that came with them was something I did not want, something I shouldn't want..." 
                menu:
                    "Destroy the pictures":
                        $ renpy.block_rollback()
                        $ axel_pictures_destroy = True
                        stop music fadeout 2.0
                        $ flena = "serious"
                        "I shook my head."
                        "I didn't want to get dragged into this. I had to control myself."
                        "Those were memories and feelings I did not want. They were not welcome..."
                        "They should remain a thing of the past."
                        play sound "sfx/rip.mp3"
                        hide v4_polaroid4
                        hide v4_polaroid3
                        hide v4_polaroid2
                        with vpunch
                        "I ripped them apart before I was dragged in by temptation."
                        call screen willup
                        "I crumpled the pieces and threw them into the bin."
                        show lenaunder at truecenter
                        with move
                        $ flena = "blush"
                        "Seeing those pictures had stirred up my feelings again, though..."
                        "I felt a strange mix of emotions inside me."
                        l "I want to think about something else... Ease my mind a bit..."
                        "My body provided me with the answer."
                        
                    "Look at the rest of the pictures":
                        $ renpy.block_rollback()
                        $ axel_pictures_watch = True
                        "I shouldn't, yet the blood pulsating in my veins demanded me to keep looking at these Polaroids."
                        "It was a need I couldn't contain..."
                        play sound "sfx/paper_click.mp3"
                        hide v4_polaroid2
                        with moveoutleft
                        l "Oh, my..."
                        "I knew what kind of pictures I was going to see, but having the actual image in front of me..."
                        "The memory of that day came back, clear as day."
                        "Me, kneeling in front of Axel, holding his hard cock in my hand..."
                        "Looking at us in the mirror while he took the pictures. Wearing that collar I felt completely his."
                        "That's why learning about his betrayal had been so painful. I thought I was his all, his everything..."
                        "At that moment, I was."
                        "A strong mix of emotions was brewing inside me, both negative and positive."
                        "An irresistible cocktail."
                        $ flena = "flirtshy"
                        play sound "sfx/paper_click.mp3"
                        hide v4_polaroid3
                        with moveoutleft
                        "I looked at the last Polaroid and my racing heart skipped a beat."
                        l "Oh, God..."
                        "That picture was..."
                        "My lips wrapped around his big, thick, hard cock..."
                        "I remembered its texture, its smell, its taste..."
                        "The weight of his manhood in my hand."
                        "The warm feeling of having him in my mouth."
                        "The sensation of having him inside me, both pleasurable and painful."
                        "The way he held me, the way he claimed me, the way he fucked me..."
                        if lena_lust < 6:
                            $ lena_lust_xp += 1
                            play sound "sfx/xp.mp3"
                            show lust_up
                            call screen skillsup
                        "All those memories got me so horny... I couldn't resist."
                        "I had to give myself to them."
                        hide v4_polaroid4
                        with short
                        show lenaunder at truecenter with move
        
## MAST        
    else:
        if seymour_shoot > 2:
            "For some reason I couldn't get the photo-shoot with Mr. Ward out of my mind."
            "My body was restless... It was telling me it was in need of some attention..."
            $ flena = "flirt"
            play music "music/sensual.mp3" loop
        else:
            "I lay down on the bed, but I knew I wouldn't fall asleep just yet."
            "It had been a relaxing day, but something was missing..."
            "My body spoke to me, letting me know it wanted me to give it some attention..."
            $ flena = "flirt"
            "That would put me to sleep like a baby, no doubt."            
            play music "music/sensual.mp3" loop
    
    hide lenaunder
    show lenanude2
    with short
    "I stripped down and lay down comfortably."
    "My body was hot..."            
    scene v4_solo1
    if lena_piercing1:
        show v4_solo1_p1
    if lena_piercing2:
        show v4_solo1_p2
    if axel_pictures_watch:
        show v4_solo1_pics
    with long
    if v3_robert_repeat == False and lena_robert_sex_late == False:
        "I had masturbated a few days ago, but I was eager to do it again."
        "I had been neglecting myself for far too long..."
    else:
        "When had been the last time I had masturbated?"
        "I had been neglecting myself for far too long..."
    if axel_pictures_watch:
        "And I needed this so much after seeing those pictures with Axel..."
        "I looked at them while my hand slid between my legs."
        play sound "sfx/mh1.mp3"
        l "Mhh..."
        "My fingers found my sex completely drenched..."
        l "Oh, no..."
        "I was more excited than I had anticipated, and my pussy was letting me know."
    else:
        "I should do this way more often..."
        play sound "sfx/mh1.mp3"
        l "Mhh..."
        "I slid my hand between my legs and found my pussy already moist."
        "I was hornier than usual lately..."
        "Not that it was a bad thing."
    "I began caressing my clit slowly, feeling the tingling sensation building up, spreading bit by bit from my crotch."
    "The moisture of my slit helped my fingers slide easily, rubbing my most sensitive spot with increasing pressure."
    if axel_pictures_watch:
        "I continued to look at Axel's pics while I reveled in the pleasure, that intimate, blissful sensation..."
    else:
        "I reveled in the pleasure, that intimate, blissful sensation..."
    "Every other thought evaporated from my mind as I enjoyed myself."
    if seymour_shoot == 4:
        "I had wanted to touch myself like I was doing now while Mr. Ward took pictures of me..."
        "Sitting on that couch, wearing sexy lingerie, my legs spread apart, my hand resting on my crotch..."
        "My fingers had begun moving while he watched..."
    "I caressed my body, feeling my own skin, soft and warm."
    "If only I had someone else's hands to do that for me..."
    
    if v3_robert_repeat and axel_pictures_watch == False or lena_robert_sex_late and axel_pictures_watch == False:
        menu:
            "Think about Ian" if v2_ian_date:
                $ renpy.block_rollback()
                $ v3_masturbate = "ian"
                $ fian = "smile"
                scene lenaroomnight
                $ ian_look = 1
                show ian
                with long
                "Ian's image appeared in my mind."
                "His amber eyes, his disheveled brown hair, his warm smile..."
                if v2_kiss:
                    scene recordstore
                    show v2_ian_kiss2
                    with long
                    "I remembered his kiss again, this time even more vividly."
                    "I could almost feel him. His lips..."
                    "I wanted to feel more of him. I wanted to make him vibrate like I was vibrating now..."
                elif v2_almost_kiss:
                    scene recordstore
                    show v2_ian_kiss1
                    with long
                    "I remembered the day at the record store."
                    "Our faces so close together, our eyes linked for a short but tense moment..."
                    "The tension I felt... I wanted it to explode between us..."
                "If he were with me tonight I wouldn't need to touch myself."
                "I would feel his fingers. His skin. His mouth."

            "Think about Holly" if v3_use_dildo == False:
                $ renpy.block_rollback()
                $ lena_go_holly += 1
                $ v3_masturbate = "holly"
                $ fholly = "flirt"
                scene lenaroomnight
                show holly
                with long
                "I didn't know why, but Holly came to mind."
                "Her cute face, her deep, steely eyes..."
                "Her sweet smell, her caramel laughter, her adorable softness..."
                "I wanted to hug her... To feel her..."
                if v2_kiss:
                    scene recordstore
                    show v2_ian_kiss2
                    with long
                    "I also remembered kissing Ian, so vividly..."
                    "I could almost feel him. His lips..."
                    "What would kissing Holly feel like?"
                    "I wanted to feel more of him. Of her. I wanted them to make me shiver like I was shivering now..."
                
            "Think about Robert" if lena_robert_sex:
                $ renpy.block_rollback()
                $ v3_masturbate = "robert"
                "I remembered what had happened in this bed the other day..."
                if v3_robert_orgasm:
                    scene v3_robert9b
                    with long
                    "Robert's naked body, his hands grabbing my flesh, his lips on my neck..."
                    "I shivered, as I imagined he was penetrating me again, rubbing my insides while I played with my clit, racing to orgasm..."
                else:
                    scene v3_robert7b
                    with long
                    "Robert's naked body, his hands grabbing my flesh, his hips hitting my butt..."
                    "I shivered as I imagined he was penetrating me again, fucking me..."
                
            "Think about Jeremy's cock" if lena_bdick > 0 and v3_use_dildo:
                $ renpy.block_rollback()
                $ v3_masturbate = "jeremy"
                $ lena_bdick += 1
                "I couldn't avoid thinking about what I had seen the other night."
                scene v3_louise1
                with long
                "Louise's boyfriend's enormous cock..."
                "So long and thick, dark and veiny..."
                "How Louise could barely fit it in her mouth..."            
                scene v3_louise3
                show v3_louise3cum
                with long
                "And then I saw it disappearing into her pussy, stretching it out to the limit..."
                "How Louise screamed... How that monster cock penetrated her..."
                "And he even came inside of her..."
                
            "Think about spying on Louise" if v3_spy:
                $ renpy.block_rollback()
                $ v3_masturbate = "spy"
                "I couldn't avoid thinking about what I had seen the other night."
                scene v3_louise2
                with long
                "I saw Louise pressed down against the bed, being penetrated by her boyfriend..."
                "Her expression and her moans were a mixture of pleasure and pain..."
                "Her red lips wide apart, her hands gripping the bed-sheets, her body being rocked back and forth with every thrust..."
                "It was so hot..."

            "Focus on your body":
                $ renpy.block_rollback()
                "I focused on my body, on the sensations..."
                "Pleasure was building up and I wasn't going to let it deflate."
                "The simple experience of pleasure was enough to turn me on..."
        scene v4_solo1
        if lena_piercing1:
            show v4_solo1_p1
        if lena_piercing2:
            show v4_solo1_p2
        with long
    
    else:
        if axel_pictures_watch:
            $ lena_bdick += 1
            "I looked at the picture where Axel was holding me with his strong, muscular arm."
            "I remembered how hard and powerful his chiseled body was..."
        elif v3_masturbate == "ian":
            "I thought of Ian. His hands... How would they feel?"
            "I was sure his touch was delicate. Or maybe he would be overtaken by passion?"
        elif v3_masturbate == "holly":
            "I wondered what Holly's hands would feel like..."
            "Her soft, small hands..."
        elif v3_masturbate == "robert":
            "I thought about Robert and what we had shared on this very same bed."
            "His naked body against mine, his cock inside of me, his grunts, his sweat..."
        elif v3_masturbate == "spy" or v3_masturbate == "jeremy":
            "I thought about the spectacle Louise and Jeremy had given me."
            "How she devoted herself to him, how he pounded her vigorously..."
            
    "I then thought about what Ivy had made me buy at the sex shop."
    "That anal plug and the bottle of lube... She had urged me to try it."
    "Was this the right moment?"
    menu:
        "Try the anal plug":
            $ renpy.block_rollback()
            $ lena_anal += 1
            "I might as well try it, since I had already bought it..."
            scene v4_solo2
            with long
            "I picked up the lube bottle and the plug and unboxed it."
            "As I smeared the cold and viscous substance over the plug and around my butt I felt my heart pounding with anticipation."
            l "Here we go..."
            "I laid back and slightly pressed the tip of the butt-plug against my anus."
            "I pushed it in very slowly, bit by bit..."
            scene v4_solo2_animation
            with long
            play sound "sfx/oh1.mp3"
            l "Ohh...!"
            "It suddenly slipped in thanks to the lube and inserted itself completely, making my body jump." 
            "That had been surprisingly easy..."
            l "Mhh..."
            "I tugged the plug a bit, investigating the sensations it produced."
            "I felt a weird pressure stretching my anus, but it wasn't unpleasant... Just a bit uncomfortable because I wasn't used to it."
            "I began sliding the plug in and out very slightly, exploring..."
            if lena_lust < 6:
                $ lena_lust_xp += 1
                play sound "sfx/xp.mp3"
                show lust_up
                call screen skillsup
            "It sent shivers up my spine... I began caressing my pussy too, adding to the sensation..."
            "It was pleasurable... Strange, but nice... And trying something new was turning me on."
            if axel_pictures_watch:
                "I had tried this with Axel, but it had been impossible due to his thick manhood..."
                "How would it have felt if he had managed to penetrate me?"
            elif v3_masturbate == "ian":
                "Would Ian be willing to do this with me?"
                "What was I thinking? We hadn't even slept together, yet..."
            elif v3_masturbate == "holly":
                "I wondered if Holly pleased herself, too..."
                "Did she do these kind of things when she was alone?"
            elif v3_masturbate == "robert":
                "I wondered if I could try anal with Robert..."
                "He would love to do it, that much was sure..."
            elif v3_masturbate == "spy" or v3_masturbate == "jeremy":
                "Did Louise do this with Jeremy, too?"
                "No, impossible... There was no way that massive cock would fit into her butt."
            
        "Continue masturbating":
            $ renpy.block_rollback()
            "I was enjoying myself too much. I didn't want to stop."
            "I continued rubbing my pussy, bringing myself closer to orgasm..."
    
    if axel_pictures_watch or v3_robert_repeat:
        if v3_use_dildo == False:
            $ v3_use_dildo = True
            "Last time I decided against using the vibrator, but this time I felt I needed it."
        else:
            if lena_anal > 0:
                "What if I added the vibrator to the mix?"
            else:
                "Using the vibrator again seemed like a good idea."
            "I had used it the other time and I had really enjoyed it..."
        if lena_anal > 0:
            "The combination with the anal plug could really be something, and I was so turned on...!"
        jump v4mastend
        
    elif lena_robert_sex_late:
        "Then something came to mind."
        "I remembered what I had stored in the back of a drawer. Something that could come in very handy right now..."
        scene v3_solo3
        if lena_piercing1:
            show v3_solo3_p1
        if lena_piercing2:
            show v3_solo3_p2
        if lena_anal > 0:
            show v3_plug
        with long
        "It was that vibrator Ivy had bought for my birthday a couple of years ago. She had asked me if I had been using it..."
        "I wasn't too used to using sex toys. I never really felt the need to."
        "But maybe now was the moment..."
        menu:
            "{image=icon_lust.png}Use it":
                $ renpy.block_rollback()
                $ v3_use_dildo = True
                scene v3_solo4_animation
                if lena_piercing1:
                    show v3_solo3_p1
                if lena_piercing2:
                    show v3_solo3_p2
                if lena_anal > 0:
                    show v3_plug
                with long
                "I pointed the vibrator towards my slit, turned it on and pushed it down slowly."
                play sound "sfx/ah3.mp3"
                "I felt it entering me, spreading my pussy while its vibrations did the same across my lower body."
                if lena_anal > 0:
                    "It pressed against the anal plug, trapping the wall of tissue that separated anus and pussy between the two toys."
                "I moved it back and forth, making room for it bit by bit."
                if lena_robert_sex:
                    "The feeling of Robert penetrating me came to mind..."
                else:
                    "It was the first thing penetrating my pussy in a long time..."
                "As the buzzing made my insides vibrate, I tried to concentrate on something that really turned me on..."
                jump v4mastend
                
            "Don't use it":
                $ renpy.block_rollback()
                if lena_anal > 0:
                    scene v4_solo2_animation
                    with long
                else:
                    scene v4_solo1
                    if lena_piercing1:
                        show v4_solo1_p1
                    if lena_piercing1:
                        show v4_solo1_p2
                    with long
                "I tossed it aside. I preferred the warmth of my fingers, the human touch."
                if lena_anal > 0:
                    "Besides, I was already using the butt plug. That was enough..."
                    "I just needed my mind and to use my imagination."
                else:
                    "I didn't need a toy to stimulate myself. I just needed my mind and to use my imagination..."
                "I continued to focus on what really turned me on..."
        
    "I could feel the climax approaching. I was almost there..."
    if seymour_shoot == 4:
        "I couldn't get today's photo-shoot out of my mind."
        "Had I really been turned on so much by posing for Mr. Ward?"
    if lena_anal > 0:
        "I rubbed my clit harder and increased the speed at which I was sliding the plug in and out."
        "Sensations mixed, increasing my pleasure until the release I was seeking came with an explosion."
    else:
        "I rubbed my clit faster and harder, feeling I was on the brink."
        "Finally the release I was seeking came with an explosion."
    play sound "sfx/ah5.mp3"
    if lena_anal > 0:
        show v4_solo2
    with vpunch
    jump v4mastend2
    
label v4mastend:
    scene v4_solo3_animation
    if lena_anal > 0:
        show v4_solo3_plug
    if axel_pictures_watch:
        show v4_solo3_pics
    with long
    if lena_robert_sex_late:
        "I rolled onto my belly so I could reach deeper with the vibrator."        
    else:
        "I did not hesitate. I got on my knees, picked up the vibrator and leaned forward."
        "I pointed the toy at my sex and slid it in. It entered so smoothly..."
        if lena_anal > 0:
            "It pressed against the anal plug, trapping the wall of tissue that separated anus and pussy between the two toys."
    if axel_pictures_watch:
        "My eyes found once more the Polaroids that were lying next to me."
        play sound "sfx/ah3.mp3"
        l "Ahhh... Axel..."
        "How I had loved giving myself to him... Pleasing him, obeying him..."
        "I loved the passion he had for me, how he desired me, how he dominated me..."
    if seymour_shoot == 4:
        if axel_pictures_watch:
            "And I also couldn't get today's photo-shoot out of my mind."
        else:
            "I couldn't get today's photo-shoot out of my mind."
        "Had I really been turned on so much by posing for Mr. Ward?"
    "Pleasing myself like this was pure bliss... All I could think about was how amazing I was feeling at that moment."
    "I should do this more often...!"
    if lena_anal > 0:
        "The vibrator sliding in and out of my pussy while my butt was filled by the plug had me about to burst."
        "The vibrations running through my body, the strangely pleasant and naughty sensation of my anus being dilated..."
        l "Fuck... Oh, fuck...!"
    else:
        "The vibrator sliding in and out of my pussy while vibrations ran through my body had me ready to burst."
        l "Oh God, ohhh..."
    play sound "sfx/ah5.mp3"
    scene v4_solo3
    if lena_anal > 0:
        show v4_solo3_plug
    if axel_pictures_watch:
        show v4_solo3_pics
    with vpunch
    pause 0.7
    with vpunch
    
label v4mastend2:
    l "Ahhh...! Ahh..."
    "My whole body shook, struck by a delightful orgasm."
    "How had I disregarded such wonderful sensations during these past few months?"
    "I could bring myself to cloud nine whenever I wanted. It was addictive."
    if lena_anal > 0:
        "And I had enjoyed this anal plug thing, more than I had anticipated..."
    stop music fadeout 2.0
    if axel_pictures_watch:
        $ flena = "blush"
        scene lenaroomnight
        show lenanude
        with long
        "When the orgasm died down and I finally came back to my senses, a weird sensation of guilt got a hold of me."
        l "Why did I do that? I shouldn't have..."
        "Thinking about Axel after all this time... I was supposed to have moved on. To want to move on."
        l "This changes nothing... I was just remembering the good old times, that's all."
        "I picked up the Polaroids and put them back into the notebook."
        "I convinced myself this hadn't been a big deal. Just a moment of nostalgia, a moment of weakness, perhaps."
        "Nothing more..."    
    else:
        scene lenaroomnight
        with long
        "The orgasm died out progressively, leaving me super relaxed."
        "I could fall asleep with ease after that..."
    
## LENA MONDAY ###########################################################################################################################################################################################################    
    
    $ day = "Monday"
    $ week = 4
    scene blackbg
    with long
    call screen calendar
    scene street
    with long  
    $ flena = "n"
    $ lena_look = 1
    with short
    "A new week began and I went to work at the café, like always."
    "A lot had happened last week... I hoped this one would be a bit calmer at least."
    scene cafe
    with long
    show lena at rig
    with short
    l "Good morning!"
    $ fed = "sad"
    show ed at lef
    with short
    ed "Hello, Lena..."
    $ flena = "sad"
    l "You don't sound too good, Ed... Don't tell me Molly is feeling under the weather today, too?"
    ed "A bit, yeah... I told her to take the day off and go to the doctor."
    ed "She began feeling ill during the weekend, but she pushed through, since it's when we get more clients and we don't have you to help."
    ed "She wanted to come today, too, but in the end she agreed to go get a check up."
    l "I can imagine, she's really devoted to this café..."
    ed "She is."
    l "Are you worried about her?"
    ed "I am... It's probably just her overworking herself, but she's not gonna get better if she doesn't take a rest! We're not young anymore."
    menu:
        "{image=icon_friend.png}You don't look old!" if ed_callout == False:
            $ renpy.block_rollback()
            $ flena = "smile"
            $ v4_compliment_ed = True
            l "You don't look old! You look strong and healthy for your age!"
            $ fed = "smile"
            if lena_ed < 6:
                $ lena_ed = 6
                play sound "sfx/friendup.mp3"
                show friend_up
            ed "You said it: for my age. But thanks, Lena."
            l "It's true. You work hard everyday and you always take care of Molly..."
            $ flena = "n"
            l "I can see you care deeply about her."
            $ fed = "n"
            ed "Of course. We've been together for so long..."
            ed "Who knows where I'd be if it wasn't for her."
            l "She's the kind of woman that makes you want to stay next to her."
            ed "Yes... You've put it into better words than I ever have!"
            if ed_callout == False:
                ed "That's something you and her have in common."
                l "Oh, thank you..."
            
        "I hope it's nothing":
            $ renpy.block_rollback()
            l "I hope it's nothing."
            ed "Don't worry, she's strong. Strongest woman I've ever met..."
            $ fed = "n"
            ed "That's why I'm with her, I suppose. Her drive is contagious, and she always stays positive, no matter how difficult the situation."
            $ flena = "n"
            l "Yes, she's a great woman... The kind of person that makes you want to stay next to her."
            ed "Yes... You've put it into better words than I ever have!"
            if ed_callout == False:
                ed "That's something you and her have in common. You also look very strong-willed."
                l "Oh, thank you..."
            ed "Thank you for caring, Lena."
            l "Of course..."
            
        "You care about her":
            $ renpy.block_rollback()
            $ flena = "smile"
            l "I can see you care deeply about her."
            $ fed = "n"
            ed "Of course. We've been together for so long..."
            ed "Who knows where I'd be if it wasn't for her."
            $ flena = "n"
            l "She's the kind of woman that makes you want to stay next to her."
            ed "Yes... You've put it into better words than I could ever have!"
            if ed_callout == False:
                ed "That's something you and her have in common."
                l "Oh, thank you..."
            
        "Getting old sucks":
            $ renpy.block_rollback()
            $ flena = "n"
            l "Getting old sucks, yeah."
            if lena_ed > 2:
                $ lena_ed -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
            ed "Thanks for reminding me of that, sweetheart."
            ed "But that's the way it is, I guess... Just don't say that in front of Molly, please."
            $ fed = "n"
            l "Sure..."
    
    if lena_ed > 2:
        ed "We've put so much into this café, Molly and I."
        ed "We started dating when we were really young... Even younger than you are."
        ed "And back then she already had this dream: having her own café, where she would prepare cakes and delicious coffee."
        ed "A cozy place for people to enjoy a bit of calm and peace..."
        menu:
            "She accomplished her dream":
                $ renpy.block_rollback()
                l "She managed to accomplish just that. With your help."
                ed "We did, yeah... This place hasn't always looked like this, though!"
                ed "We've always been a small business. We never wanted anything more... Just to have our little café and make people happy."
                ed "It worked for quite a few years... But at some point things began getting a bit more difficult."
                ed "We had saved up some money during the years, and we decided to invest most of it in renovating the place."
                ed "All you see now is pretty recent... We thought that way we could attract more clients again."
                l "You tried to go with the times."
                ed "Yes... And it worked, for a time. Sometimes I wonder if we made the right choice..."
                $ fed = "sad"
                ed "After all, the thing we could never have is kids. We would've loved to have a son or a daughter who would inherit our little café."
                ed "Now it's getting difficult for us to manage it ourselves... And well, you've noticed we don't have that many customers."
                ed "And that brings me to give you some bad news..."
                $ flena = "worried"
                l "Bad news? What bad news?"
                ed "I'm so sorry to have to tell you this, Lena, but..."
                
            "What was your dream, Ed?":
                $ renpy.block_rollback()
                l "And what about you? What was your dream, Ed?"
                ed "Hmm... I guess I never had a big dream to realize. I'm not a dreamer, unlike you or Molly."
                ed "I was just content seeing my wife and those around me happy, being happy myself... Proving myself useful, doing something people could enjoy."
                ed "That's why I like cooking!"
                ed "But I guess this café became my dream too, after all. We've always been a small business. We never wanted anything more..."
                ed "Just to have our little café and make people happy."
                ed "It worked for quite a few years... But at some point things began getting a bit more difficult."
                ed "We had saved up some money during the years, and we decided to invest most of it in renovating the place."
                ed "All you see now is pretty recent... We thought that way we could attract more clients again."
                l "You tried to go with the times."
                ed "Yes... And it worked, for a time. Sometimes I wonder if we made the right choice..."
                $ fed = "sad"
                ed "After all, the thing we could never have is kids. We would've loved to have a son or a daughter who would inherit our little café."
                ed "Now it's getting difficult for us to manage it ourselves... And well, you've noticed we don't have that many customers."
                ed "And that brings me to give you some bad news..."
                $ flena = "worried"
                l "Bad news? What bad news?"
                ed "I'm so sorry to have to tell you this, Lena, but..."
                
            "Why are you telling me this?":
                $ renpy.block_rollback()
                $ flena = "worried"
                l "Why are you telling me this?"
                ed "Oh... I guess you're not interested in this old man's stories, sorry."
                $ fed = "sad"
                ed "I guess I was just trying to work around giving you some bad news..."
                $ flena = "worried"
                l "Bad news? What bad news?"
    else:
        $ fed = "sad"
        ed "Anyways... I guess this is as good a moment as any to give you the bad news..."
        $ flena = "worried"
        l "Bad news? What bad news?"
    
    ed "I don't think we can afford to keep employing you."
    $ flena = "drama"
    l "What!?"
    ed "I'm sorry... We need you more than ever, considering Molly's health, but we're having trouble making ends meet..."
    "This was the worst possible news I could receive today."
    if lena_robert_sex:
        "I was losing half my wage from the restaurant, and now this?"
    else:
        "I was getting fired from the restaurant, and now this?"
    "How would I survive?"
    l "Isn't there something that can be done? I really need this job..."
    ed "I know... Molly's against this, and I don't like it either, but we can't fight the truth: we just don't make enough money."
    ed "It's not only that we can't afford to employ you... At this rate, we'll need to close up shop."
    $ flena = "sad"
    l "No way... Is it really that bad?"
    ed "I'm afraid it is..."
    l "But what will you do? You just said Molly can't keep working like she does, and if you fire me..."
    ed "I know. I would need to run the café mostly by myself. And I don't see how I'm going to do that, so..."
    ed "As things are, we'll need to shut off the caféeven sooner than I'm expecting."
    l "Isn't there anything that can be done?"
    ed "I have no idea. We tried everything we could, but it seems we only got ourselves in debt..."
    ed "Right now the only solution I see is finding someone to transfer the business to. Use that money to survive until we get our retirement pension..."
    "Ed and Molly's situation reminded me of my parent's. They had also struggled to keep the bakery open... and failed."
    ed "I don't like the idea, and Molly's against it, but I think it's what we should do..."
    ed "I need to make sure me and Molly can live our last years somewhat comfortably."
    menu:
        "{image=icon_friend.png}Can I do something to help?" if ed_callout == False or lena_molly > 8:
            $ renpy.block_rollback()
            $ cafe_help = True
            l "Can I do something to help?"
            ed "I don't know what could you do, aside from working for free, and I'm not going to ask you to do that."
            l "I don't know what we could do either, but there has to be something."
            l "Some way to get more customers to come, do some marketing or something like that..."
            ed "I have no idea about those things, but any help would be welcome."
            $ flena = "smile"
            l "Don't worry, I'll come up with something, you'll see!"
            call screen willup
            $ fed = "smile"
            ed "Thank you, Lena. You're such a darling."
            play sound "sfx/friendup.mp3"
            show friend_up
            $ lena_ed += 1
            $ flena = "n"
            l "We'll figure something out. Maybe you won't need to close after all."
            ed "And we'll keep employing you until we cannot do so anymore, or until we find someone who takes the business from us..."
            ed "Whatever happends first."
        
        "I understand...":
            $ renpy.block_rollback()
            l "I understand... It's a very difficult situation, and not too different from my family's..."
            ed "I'm so sorry, Lena. You've been a wonderful employee and I know Molly sees in you the daughter we never had."
            ed "We love having you with us, but we just need to assure our financial stability."
            l "So when are you going to close the shop?"
            if ed_callout:
                ed "I haven't found anybody who wants to take the café from us, but I'm searching. I know you need a two weeks' notice before laying off an employee, so..."
                ed "We will still employ you for half this next month and you will still get paid, even if it's just half..."
                $ fed = "n"
                ed "That way you'll have some time to find another job while we settle things here."
            else:
                ed "I haven't found anybody who wants to take the café from us, but I'm searching... I have no idea how long it can take me, though."
                $ fed = "n"
                ed "I'll keep you employed as long as I can until I find somebody to take over the business..."
                l "Thank you, Ed."
            if v1_ed_truth:
                ed "In any case, a beautiful model like you should aim higher than working at this humble café!"
                ed "I'm sure you'll find success in your modeling career."
            elif v1_ed_flirt:
                ed "In any case, I'm sure a charming and beautiful girl like you won't have any trouble finding a new job!"
                ed "You should aim higher than working at this humble café."
            ed "And in the worst case scenario you can ask the new owners to hire you. We will vouch for you."
            l "Nothing guarantees they will need to hire someone. They will probably run it themselves."
            ed "You never know...."
            
        "You're being unfair!":
            $ renpy.block_rollback()
            $ flena = "mad"
            l "But what about me? You're being unfair!"
            ed "I'm sorry, Lena. I hate doing this to you, believe me."
            ed "I'm the first one who wants this café to thrive, but I don't see any other way around the situation."
            l "But what will I do? I need the money!"
            $ flena = "drama"
            l "You can't just fire me like that...!"
            ed "I know you need a two weeks' notice before laying off an employee."
            ed "So we will still employ you for half this next month and you will still get paid, even if it's just half..."
            ed "That way you'll have some time to find another job while we settle things here."
            if v1_ed_truth:
                $ fed = "n"
                ed "Besides, a beautiful model like you should aim higher than working at this humble café!"
                ed "I'm sure you'll find success in your modeling career."
            elif v1_ed_flirt:
                $ fed = "n"
                ed "Besides, I'm sure a charming and beautiful girl like you won't have any trouble finding a new job!"
                ed "You should aim higher than working at this humble café."
            ed "And in the worst case scenario you can ask the new owners to hire you. We will vouch for you."
            l "That's if you find somebody who will take the business from you..."
            ed "I hope we will."
            
    ed "Anyways... Let's get to work."
    l "Yeah..."
    scene cafe
    with long
    $ flena = "sad"
    show lenawork
    with short
    "Needless to say it wasn't a cheerful shift. I couldn't believe my bad luck."
    "I felt sorry for Molly and Ed, who were struggling to keep their business open and make it to retirement... But that was also a big problem for me."
    "After what happened with my job at the restaurant I needed this one even more..."
    if ed_callout:
        "And now I found myself with two weeks to find something else or I would be without a stable job."
    else:
        "I wouldn't be fired immediately, but unless things took a turn I would be without a stable job sooner or later..."
        "Who knows how long it would take for Ed to find someone to transfer the business to?"
    "Thinking about it made me anxious and stressed..."
    l "I can't seem to catch a breath..."
    l "I will figure things out. Somehow, I will."
    
    play music "music/fancy.mp3" loop
    scene restaurant
    with long
    $ lena_look = 2
    $ frobert = "n"
    $ robert_look = 2
    show lenawork
    with short
    "My mood didn't improve when I got to the restaurant."
    if lena_robert_sex:
        "At least I would still keep this job, even if it was only a couple of days each week..."
        "Not nearly enough to pay the rent."
    else:
        "I had even been happy that this was my last week working here, but not after learning that I would be losing my job at the café, too..."
        "How would I pay the rent?"
    if v4_seymour_date:
        "Seymour Ward was interested in working with me again, but that was no stable job."
    if stalkfap:
        "I was trying to get some extra money with Stalkfap, but thus far it was a totally negligible amount."
    "Making money out of modeling didn't seem a reliable option, and earning a living making music was out of the question..."
    "At least today was a slow one. Not many customers on a Monday."
    show lenawork at rig
    with move
    show robert at lef
    with short
    if lena_robert_sex and lena_robert_over == False:
        r "Hey, Lena..."
        $ frobert = "sad"
        r "What's with the long face? Did something happen?"
        l "Yeah..."
        "I told him about the situation at the café."
        r "Damn, that's some bad luck..."
        l "Yeah... I'm pretty worried, as you can imagine. The only reliable source of income I have left is the one from the restaurant, and it's not much."
        l "Not much at all..."
        r "I wish I could help you... There's not much I can do, but if you have trouble finding a job for a while and need some help paying the rent..."
        r "Feel free to ask me."
        l "I won't ask money from you..."
        $ frobert = "n"
        r "Hey, it's me who's offering it to you. I don't earn that much myself, but I can spare to help you during a few months, if that's what you need."
        $ flena = "n"
        l "Thanks for the offer, Robert. It's really generous, but..."
        r "Don't think too much about it. Just know that, should you need some, I'm very willing to help."
        $ frobert = "smile"
        r "Anything for my sexy girl."
        l "Thank you..."
        $ frobert = "n"
        r "Anyways, I was going to tell you we have a very important client tonight."
    else:
        r "Hey, Lena. Pay attention, we have a very important client tonight."
        if lena_robert_over:
            "He was pissed after I'd told him I wasn't interested in seeing him again."
            "He didn't take my rejection graciously, but I expected that much. He wanted more of me than I had already given him, but that wouldn't happen."
        else:
            "I had grown accustomed to his cold and indifferent attitude towards me."
            "I didn't care, and I wouldn't be seeing him again in just a few days."
    $ flena = "n"
    l "Who's coming?"
    r "The Mayor himself."
    l "Oh, wow. We're having a political meeting at our restaurant tonight?"
    r "No, he's coming just with his family. But you can imagine the chef and the manager want us to provide them with perfect service."
    l "Of course. There's still classes in this world."
    if lena_robert_sex and lena_robert_over == False:
        r "Yeah... It's not like he's above us simple mortals, but since he's a VIP we need to treat him differently..."
        r "It's important for the reputation of the restaurant."
        l "I know, I know. I will treat the Mayor with the respect he deserves."
        r "I know you will. You're the best member of my team!"
    else:
        r "What?"
        l "Oh, nothing... I will treat the Mayor with the respect he deserves."
    r "Oh, here he comes."
    r "I'm gonna take them to their table and then you can take it from there. Go make sure the wine is cool and ready."
    l "Yes sir."
    hide robert
    with short
    show lenawork at rig3
    with move
    "I tried to shake my worries out of my head. I had to be focused on work tonight."
    if lena_robert_sex and lena_robert_over == False:
        "Robert's offer had eased my worries a bit though, even if I didn't want to take him up on it..."
        "But it was good knowing he had my back, just in case things went really South."
    "I walked to the VIP table to take our important clients' order."
    show mayor 
    show mayorwife at lef3
    with short
    l "Good evening and welcome to Yunalesca. We're happy to have you tonight, Mr. Vermeer."
    mayor "Thank you."
    l "Do you know what you'll be having? I can help you with some suggestions, if you'd like."
    mayor "No, we have already decided..."
    "He made his order and I wrote it down."
    l "That'll be all?"
    mwife "Wait a second, our son's in the bathroom..."
    mwife "Oh, here he comes."
    show lenawork at right
    show mayor at rig
    show mayorwife at centerlef
    with move
    $ fperry = "n"
    show perry at left
    with short
    $ flena = "surprise"
    p "Have you ordered the steak for me?"
    mayor "We were waiting for you to order it yourself."
    mwife "Have you washed your hands, Perry?"
    $ fperry = "meh"
    p "Of course, Mom."
    $ fperry = "n"
    $ flena = "worried"
    p "So, for me, the steak with green p--{w=0.5}pepper sauce..."
    $ fperry = "surprise"
    "Perry's eyes widened as he recognized me."
    p "Oh! You're L--{w=0.5}Lena, right? What are you doing here?"
    $ flena = "shy"
    l "I work here..."
    mwife "Oh, do you know each other?"
    $ fperry = "n"
    p "Yeah, we've met before... She's a friend of Ian's."
    mwife "Oh, I see."
    mayor "Leave the poor girl be. She's working and probably doesn't want to be disturbed."
    l "If that's all I'll go relay your order."
    mayor "Thanks."
    hide mayor
    hide mayorwife
    hide perry
    with short
    show lenawork at truecenter
    with move
    $ flena = "worried"
    $ lena_mayor_agenda = True
    $ ian_mayor_agenda = True
    $ lena_mayorswife_agenda = True
    $ ian_mayorswife_agenda = True
    "That was unexpected! So Perry was the son of Mayor Vermeer?"
    "I had never served people who had seen me naked before... I hoped he didn't tell his parents where he met me."
    "I'd rather they saw me just as a simple waitress and kept things professional."
    "When the first dishes came out I took them to their table."
    $ flena = "n"
    show lenawork at right
    with move
    $ fperry = "mad"
    show mayor at rig
    show mayorwife at centerlef
    show perry2 at left
    with short
    mwife "You could've dressed a bit nicer for this occasion, Perry. You knew we were coming to an expensive restaurant."
    p "I'm not a k--{w=0.5}kid anymore, Mom. I don't need you to tell me how to dress."
    mwife "It's obvious that you need me to tell you, considering what you're wearing."
    mayor "Let's not quarrel, please."
    $ fperry = "meh"
    l "Excuse me... Here you go."
    "I served them the dishes and gave the proper explanations."
    mayor "Thanks, Lena."
    l "You're welcome. I hope you enjoy them."
    hide mayor
    hide mayorwife
    hide perry2
    with short
    show lenawork at truecenter
    with move
    l "He called me by my name... I guess Perry did tell them about me, after all..."
    l "Anyways, they're just customers. I'll treat them as such."
    "I kept serving their table as the night went on."
    if lena_robert_sex and lena_robert_over == False:
        "When all that was left for them was dessert Robert approached me."
        $ frobert = "flirt"
        show lenawork at rig
        with move
        show robert at lef
        with short
        "He wrapped his hand around my waist and whispered in my ear."
        r "You're so beautiful tonight, Lena..."
        $ flena = "shy"
        l "Robert, what's up with you? Stop, they could see us..."
        r "Tell me, have you ever fantasized about doing it at work?"
        l "Doing what?"
        r "You know what..."
        l "There's no way we can do that here."
        r "Why not? I've always wanted to do it with you here..."
        r "It will be quick... Just a blowjob while they finish their meal..."
        l "You want me to give you a blowjob right now?"
        r "It's all I can think of. You drive me crazy, Lena..."
        r "Let's sneak into the changing room. Nobody will look for us there..."
        menu:
            "{image=icon_lust.png}Give Robert a blowjob" if lena_lust > 2 or v4_robert_sex:
                $ renpy.block_rollback()
                $ v4_robert_public = True
                jump v4lenarestaurantbj
                        
            "We can't do this":
                $ renpy.block_rollback()
                $ flena = "serious"
                "I freed myself of Robert's embrace."
                l "No, Robert. I won't do that, not at work."
                $ frobert = "sad"
                r "But... It will be just a moment... It's a fantasy I have..."
                l "It's a fantasy that will remain a fantasy. Don't ask me again."
                r "OK, OK... What a way to kill the mood..."
                $ flena = "n"
                l "Come on, you're all grown up. Stop acting like a kid and be responsible."
                $ frobert = "serious"
                $ lena_robert -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                r "Sure, whatever."
                l "Looks like the Mayor's done with his meal. I'm going back to work."
                
            "I'm not in the mood":
                $ renpy.block_rollback()
                $ flena = "sad"
                l "I'm sorry Robert, but I'm not in the mood... Not today."
                r "Are you sure? I thought a little game would cheer you up..."
                l "Not this kind of game. My mind isn't in the right place for that after what happened this morning."
                r "I see... OK, I understand..."
                r "Such a pity, though. That has always been a fantasy of mine..."
                $ flena = "n"
                l "We need to be responsible, especially you, head waiter."
                $ frobert = "n"
                r "I hate being responsible sometimes."
                l "Looks like the Mayor's done with his meal. I'm going back to work."
        
    else:
        "When they finally got up to leave, they seemed satisfied."
    show lenawork at right
    with move
    $ fperry = "smile"
    show mayor at rig
    show mayorwife at centerlef
    show perry at left
    with short
    l "I hope you enjoyed the dinner."
    mayor "We did. Thank you for your service. Here's a tip for you."
    $ lena_money += 1
    play sound "sfx/moneyup.mp3"
    show money_up
    $ flena = "surprise"
    l "That much? It's not necessary..."
    mwife "We insist."
    $ flena = "blush"
    l "Thank you so much..."
    p "It was really delicious! I'll tell Ian I saw you."
    $ flena = "smile"
    l "Say hello to him for me."
    p "Of course. You should drop by sometime and have a b--{w=0.5}beer with us."
    l "Thanks for the invitation!"
    mayor "Have a good night."
    hide mayor
    hide perry
    hide mayorwife
    with short
    show lenawork at truecenter
    with move
    "Something good happened today, finally..."
    "I wasn't expecting getting this huge tip... But I could really use it!"
    "All that was left now was cleaning up and going back home."
    stop music fadeout 2.0
    jump v4lenamondaynight
  
label v4lenarestaurantbj: 
    $ flena = "slutshy"
    if lena_bj < 3:
        $ lena_bj += 1
    "The idea was pretty arousing, to be honest..."
    l "Alright... I'm in."
    $ frobert = "smile"
    r "Nice! Come with me!"
    "Robert took my hand and led me to the changing room in the back."
    "With all the drama and worries that were piling up, this seemed like a good way to get my mind off of it."
    "Letting myself go and play this naughty little game with Robert... It was risqué and defiant..."
    "I felt the need to misbehave a bit tonight."
    play music "music/sex.mp3" loop
    play sound "sfx/door.mp3"
    scene v4_restaurant1
    with long
    "As soon as I closed the door behind me Robert unzipped his pants, revealing his already erect cock."
    r "Come on, we can't waste time..."
    "I got down on my knees and held his hard manhood."
    l "I see you're ready to go..."
    r "I'm so fucking excited right now... Ohhh!"
    "He groaned when I slid my tongue across the shaft, teasing him."
    r "Oh, baby... Do it, suck my dick..."
    if lena_bj > 1:
        "Feeling Robert's cock on my tongue was an immediate turn on for me. I liked it..."
    else:
        "If that's what he wanted, that's what I was gonna give him..."
        "I tried to let myself go, getting into the situation..."
    "I began licking Robert's cock, wetting it with my tongue and lips, sucking the tip..."
    menu:
        "Take your time":
            $ renpy.block_rollback()
            "I wanted to take my time and enjoy this. I couldn't stall too much, though..."
            scene v4_restaurant2
            with long
            "I ran my mouth down Robert's shaft until my lips reached his balls."
            r "Oh, Lena...!"
            play sound "sfx/bj1.mp3"
            "I began licking them, kissing and sucking..."
            r "Ah... That tickles..."
            l "Do you like it? Do you like having me sucking your balls at work?"
            r "Yes, keep doing it... And don't stop jerking me off..."
            "I did as Robert asked, stroking his cock with my hand while I used my mouth on his ball sack."
            "I could tell by how he was shivering that he was enjoying it... I felt his sex hard as a rod in my hand while I caressed it slowly..."
            r "Oh Lena, I can't believe we're doing this... This feels like a dream..."
            l "Enjoy it..."
            "I couldn't believe it either, but there I was, on my knees, pleasing Robert while at work..."
            if lena_lust < 6:
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
            "I felt naughty... I felt excited, brave and alive."
            r "I can't take it anymore... I need your mouth!"
            
        "Make him cum":
            $ renpy.block_rollback()
            "I couldn't afford to stall. We needed to end this quickly."
            l "Tell me how you want it. I want to make you cum."
            r "Oh, baby!"
    
    scene v4_robert_animation
    with long
    play sound "sfx/gag1.mp3"
    "Robert took control. He held my head and shoved his cock into my mouth."
    "He began moving his hips back and forth quickly, racing to orgasm."
    r "Oh shit, oh baby!"
    l "Mghh...!"
    "I took Robert's cock in my mouth as he fucked it."
    "He wasn't pushing it too deep, so it wasn't uncomfortable... His movements were short and fast."
    if lena_bj > 1:
        "This was so damn hot... The way he was using my mouth, trying to cum..."
    else:
        "This felt so naughty... Dirty, even. But I kinda liked it..."
    "I pressed my lips and tongue around his dick, giving him the friction he was looking for..."
    "It was my first time doing this kind of thing at work... In a public place..."
    "What if someone walked up on us? What if they saw me like this?"
    "My heart was racing and adrenaline was flooding my body... I was getting so turned on..."
    "And so was Robert."
    r "Shit, I'm almost there, I'm..." 
    scene v4_robert_animation2
    with long
    "Robert pulled back and began jerking off furiously."
    r "Open your mouth, baby! Here it comes...!"
    "I closed my eyes and prepared myself to receive Robert's load."
    l "Give it to me, Robert. Cum all over me!"
    "I was about to be covered by it, marked by it..."
    if axel_pictures_watch:
        "Marked as Axel used to mark me... How I loved that..."
    else:
        "I found myself wanting it, possessed by lust..."
    scene v4_restaurant4
    show v4_restaurant4_cum1
    with flash
    with vpunch
    r "Ahhhh!!"
    "Robert finally reached his climax."
    hide v4_restaurant4_cum1
    show v4_restaurant4_cum2
    with long
    r "Oh yes, fuck yes, baby! Nghh!"
    "Ropes of cum sprayed my mouth and face as he groaned and grunted."
    "He was anointing me with the symbol of his pleasure, his satisfaction, his desire for me..."
    "All of which I had granted him. It was a sexy and rewarding feeling..."
    r "Oh fuck, that's so hot..."
    r "Oh, babe..."
    stop music fadeout 2.0
    scene restaurant
    $ frobert = "flirt"
    $ flena = "slutshy"
    show robert at lef
    show lenawork at rig
    show lena_cum1 at rig
    with long
    "Robert wiped his cock and pulled up his pants."
    l "You were right, that didn't take long..."
    r "I told you... You know how to drive me crazy, Lena. And that was amazing!"
    l "I'm glad you liked it... Can you hand me a tissue?"
    r "Sure."
    hide lena_cum1
    with short
    $ flena = "smile"
    "I wiped Robert's cum off my face. Thankfully the uniform hadn't been stained."
    l "Do I look OK?"
    r "You do... But you looked much better with it on your face..."
    $ flena = "flirt"
    l "I didn't know you were so dirty..."
    r "You didn't?"
    l "Well... I had my suspicions. Plenty of them, actually."
    r "I never tried to hide it, ha ha."
    r "We should get back... We've been away long enough."
    "It had only taken us about five minutes, but that was a long time working at this restaurant..."
    "Thankfully there weren't many customers today."
    hide robert 
    with short
    show lenawork at right
    with move
    $ fperry = "smile"
    show mayor at rig
    show mayorwife at centerlef
    show perry at left
    with short
    "I went back to check on the Mayor's table. Someone else had brought them their desserts..."
    l "Is everything alright?"
    mayor "Yes, we're all but done."
    l "I hope you enjoyed the dinner."
    mayor "We did. Thanks for your service."
    p "It was really delicious! I'll tell Ian I saw you."
    $ flena = "smile"
    l "Say hello to him for me."
    p "Of course. You should drop by sometime and have a b--{w=0.5}beer with us."
    l "Thanks for the invitation!"
    mayor "Have a good night."
    hide mayor
    hide perry
    hide mayorwife
    with short
    show lenawork at truecenter
    with move
    "All that was left now was cleaning up and going back home."
    stop music fadeout 2.0
    jump v4lenamondaynight
 
label v4lenamondaynight:
    
    play sound "sfx/door_home.mp3"
    scene lenahomenight_dark
    with long
    $lena_look = 1
    $ flena = "n"
    show lena 
    with short
    "I finally got back home after a long day. And what a day..."
    "Ed's news was yet another burden on my back. Another pressing matter to solve..."
    if lena_robert_sex and lena_robert_over == False:
        "At least Robert had offered to help if I needed some extra money in the following months, but I didn't want to resort to that..."
    if v4_robert_public:
        "At least something fun had happened at work..."
        "I still was amazed at myself for doing something like that. I had liked it more than I'd thought I would..."
        "Too bad we didn't have time for more. That made me quite horny..."
    else:
        "At least I had gotten a really big tip from Mayor Vermeer."
        "To think he was Perry's father..."
    l "So Ian's flatmate is the Mayor's son... I would never have guessed he had those kinds of connections."
    l "He doesn't look like that kind of guy at all..."
    if louise_jeremy == False:
        $ flena = "sad"
        $ louise_look = 2
        $ flouise = "n"
        "I hadn't checked upon Louise yet after telling her about Jeremy..."
        l "I hope it's not too late to do it now..."
        "I walked to her room and softly knocked on the door."
        l "Louise...? Are you awake?"
        play sound "sfx/door.mp3"
        show lena at rig
        with move
        show louisebra at lef
        with short
        "She opened the door."
        lo "Yes. What's the matter?"
        l "I just... wanted to know how you're feeling. About Jeremy and all that..."
        lo "Oh, that..."
        lo "I called him. Talked to him. Asked for an explanation."
        l "And what did he tell you?"
        lo "He said that nothing happened between him and Ivy. And that he wasn't trying to get with her."
        $ flena = "worried"
        l "He said that?"
        lo "Yeah. Turns out it's Ivy who was flirting with him and trying to get into his pants."
        lo "He turned her down every time but he didn't want to be rude and she wasn't getting the message."
        menu:
            "That's not what happened":
                $ renpy.block_rollback()
                $ v4_confront_louise = True
                $ flena = "serious"
                l "That's not what happened."
                lo "That's what he told me."
                l "He's lying."
                $ flouise = "serious"
                $ lena_louise -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                lo "You're taking Ivy's side because you are her friend. But that girl is..."
                l "She can be many things, but she's not lying about this. Jeremy was trying to cheat on you."
                lo "That's his word against yours. And I'm willing to trust my boyfriend."
                $ flena = "sad"
                l "If that's what you want... It's your choice."
                l "I'm just saying this to you as a friend, I hope you know that..."
                $ flouise = "sad"
                lo "I know... But he's my boyfriend. I can't choose what you and Ivy are saying over his own word..."
                
            "Do you believe him?":
                $ renpy.block_rollback()
                l "And do you believe him?"
                lo "Yes... I want to. He's my boyfriend, after all."
                $ flouise = "serious"
                lo "I'll trust his word over that of Ivy, of that I'm sure."
                l "Then why didn't he tell her he had a girlfriend?"
                $ flouise = "sad"
                lo "That's..."
                $ flouise = "n"
                lo "That's none of her business. And she never asked him."
                l "I'd think it's his responsibility to tell her, if he thinks Ivy's flirting with him..."
                lo "She shouldn't have flirted in the first place. Lena..."
                
        lo "I don't want you to take this the wrong way, but I'd prefer it if you let me handle my relationship myself..."
        lo "You know I'm kinda insecure about these things... It's hard enough as it is."
        "She clearly didn't want to see the truth. I was Louise's friend, but it wasn't my responsibility to open her eyes..."
        "I had done more than enough. I had to let her discover the truth herself."
        "It would be way more painful for her when that happened..."
        $ flena = "n"
        l "OK, I'm glad to see you figured things out. I'm going to bed."
        lo "Goodnight, Lena."
        
    if v4_robert_public:
        play sound "sfx/door.mp3"
        scene lenaroomnight
        show lena
        with long
        $ flena = "sad"
        l "I'm not sleepy at all, even though I'm tired..."
        l "Doing that with Robert has excited me too much and now I'm a bit restless..."
        l "Ahh... Maybe I should've told Robert to come spend the night here..."
        "It was too late for that."
        $ flena = "flirtshy"
        "But I could always masturbate before going to sleep..."
    else:
        play sound "sfx/door.mp3"
        scene lenaroomnight
        show lena
        with long
        "I went straight to my room and got into bed."
        "I had many things to sleep on..."
        
################################################################################################################################################################################################################################
## IAN ##############################################################################################################################################################################################################################
################################################################################################################################################################################################################################
    
    $ lena_active = False
    $ ian_active = True
    $ save_name = "Ian: Chapter Four"
    $ day = "Sunday"
    $ week = 3
    scene blackbg
    with long
    show active_ian
    with long
    pause 1.0  
    scene blackbg
    with long
    call screen calendar
    play music "music/normal_day.mp3"
    scene ianroomnight
    with long
    $ fian = "n"
    $ ian_look = 2
    show ian
    with short
    $ v4_textscene_check = False
    "I stretched my back while sitting in front of the computer."
    "I had been writing the whole day, immersed in my book."
    "Another week had gone by..."
    if ian_switch_review or ian_honest_review:
        "A very crazy week. Things had taken a dramatic turn, especially at the magazine."
        "I was no longer working five days a week, and Minerva was looking for any excuse to finally kick me out..."
        "I should be more stressed about it, but for some reason I wasn't. Maybe because I didn't care about her or about that job."
        "All I wanted to do was finish my book... But I needed the money!"
    else:
        "Work at the magazine was as monotonous and boring as ever."
        "It only got in the way of me writing my book, but I needed the money..."
    if ian_go_holly > 0:
        "The only thing I really enjoyed about working at the magazine was Holly."
        "I had been talking and getting to know here more during this month, and I really liked her..."
        "She was cute and adorable, and, most importantly, shared my same passion."
        "I had never met a girl like her..."        
    if v3_cindy_date:
        "This weekend had been a lot calmer than last week's. I remembered my night out with Cindy, just the two of us..."
        "And the fight she had with Wade just moments before."
        if v3_cindy_dance_signs:
            "I wondered if that was the reason I felt like she was getting closer than usual to me..."
            "When we danced I felt some real chemistry between us, but maybe it was just my imagination, or wishful thinking..."
        elif v3_cindy_reject:
            "I had messed up trying to get too close and personal to Cindy, though."
            "What the hell had I been thinking? She was my friend's girl..."
        else:
            "It had been a fun night..."
        "And then that Axel guy showed up."
        "He really asked Cindy to pose for him... And she seemed very willing to accept."            
        if ian_cindy_model:
            "She seemed willing to show me the pictures too, though..."
            "I didn't know if to feel lucky or not about that. But those were some pictures I'd love to see, that much was clear..."
    if v3_ian_date:
        "I had had so much fun with Lena and Holly last Wednesday. I felt comfortable around them, and we could talk for hours."
        "I hoped we could meet like that again."
    else:
        "Also, I hadn't met Lena for a while..."
    if v2_ian_date:
        "I had texted Lena yesterday, asking if she wanted to meet."
        if v4_ian_date:
            $ fian = "smile"
            "She had agreed to it, and we had a date on Wednesday."
            if lena_go_ian == 2:
                "She even sent me a kiss emoji with a heart."
                if v2_kiss:
                    "I guessed we could continue what we had started at the record store..."
                else:
                    "That was promising..."
            i "I can't wait..."
        else:
            $ fian = "sad"
            "She had told me she was too busy and couldn't meet..."
            "She said her life was complicated and this was not the right time, so that was pretty much a way of saying she wasn't really interested in me after all." 
            "All I could do was wait and see if that changed, but I doubted it..."
            i "Such a pity.... It looked promising for a moment..."
    if ian_alison_sex:
        $ fian = "n"
        "I still felt weird about how my relationship with Alison had changed."
        if v3_alison_sex and v2_alison_home and v2_ian_limp == False:
            $ fian = "smile"
            "It had been twice that we had slept together already. And it had been pretty awesome..."
        elif v3_alison_sex and v2_ian_limp:
            "I had thought that after my screw-up last week she would be done with me, but it seemed she didn't mind."
            "We had tried again this week and this time it had actually worked... And it had been pretty awesome."
        elif v3_alison_sex == False:
            "We had slept together once and it seemed she wanted to do it again."
            "Sadly, I couldn't meet her last Wednesday, since I had to meet Lena and Holly. I hoped she didn't mind too much."
        "I had always found Alison attractive, but never thought we could actually end up together."
        "Well, together... It was more like we had added a new layer to our friendship."    
        "Neither of us was looking for a serious relationship... At least it seemed clear that wasn't her goal."
        "But that suited me just fine..."
    if ian_cherry_sex:
        "I thought about Cherry."
        "It had been more than a week since I met her... And slept with her."
        "I hadn't heard from her during this time, but it was to be expected."
        if ian_cherry_free:
            $ fian = "smile"
            "What we had had was a one night stand, casual sex at best. But I had liked it so much... And so did she, or at least it had looked that way."
            "I wondered if I should get in touch with her, let her know I was still around and interested..."
        else:
            $ fian = "worried"
            "And I didn't feel comfortable texting her after our conversation. She had seemed pretty uncomfortable when I had told her I expected us to be something more than a one night stand..."
            i "What the hell was I thinking? No wonder I creeped her out..."
            i "I should've played it cool. I'm sure she felt pressured and that's why she's not getting in touch."
    $ fian = "n"
    i "Ahhh..."
    "I got up from my chair and decided I had worked enough for today. My mind was distracted by other things."
    "I was waiting for Jeremy to come home. We had agreed to meet and watch the fights, as we did from time to time."
    menu:
        "Text Alison" if ian_alison_sex:
            $ renpy.block_rollback()
            $ v4_alison_sexting = True
            "I hadn't gotten in touch with Alison for a while. I decided to text her, see how she was doing."
            $ fian = "smile"
            i "{i}Hey Alison! How's your weekend been?{/i}"
            play sound "sfx/sms.mp3"
            "She texted back almost immediately."
            a "{i}Ian! It's been pretty awful. Taking care of things from work...They have an incredible mess in that office!{/i}"
            if ian_alison < 10:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_alison += 1
            jump v4alisontexting
            
        "Text Cherry" if ian_cherry_free:
            $ renpy.block_rollback()
            $ v4_cherry_sexting = True
            jump v4cherrytexting
            
        "Wait for Jeremy":
            $ renpy.block_rollback()
            "I decided to wait for Jeremy."
            i "He should be here any minute now."
            jump v4ianfriends            
            
label v4alisontexting:
    i "{i}You work on weekends, too?{/i}"
    a "{i}I shouldn't, but I do... And I also had to help my parents with some tax stuff{/i}."
    i "{i}That sounds like the most exciting weekend ever...{/i}"
    a "{i}Not nearly as exciting as hanging out with you {image=emoji_flirt.png} {image=emoji_kiss.png}{/i}"
    $ fian = "confident"
    i "{i}Very few things are as exciting as hanging out with me{/i}."
    if v3_ian_date:
        a "{i}Not even hanging out with that model of yours?{/i}"
        $ fian = "n"
        i "{i}What's that supposed to mean?{/i}"
        a "{i}Nothing, just that I know I can't compete with a Peoplegram model{/i}."
        i "{i}When did I say that? Just so you know I haven't even slept with her.{/i}"
        if alison_jeremy:
            i "{i}Besides, need I remind you who slept with Jeremy just the other day?{/i}"
            a "{i}That's right {image=emoji_ups.png}{/i}"
        else:
            a "{i}I'm not blaming you for wanting to {image=emoji_flirt.png}{/i}."
        a "{i}Anyways, have you missed me this weekend?{/i}."
    else:
        a "{i}Have you missed me this weekend?{/i}."
    i "{i}I sure did... {/i}"
    if v3_alison_boobjob:
        if ian_alison_gallery == False:
            $ ian_alison_gallery = True
        a "{i}You missed me, or you missed these?{/i}"
        play sound "sfx/sms.mp3"
        $ ian_alison_pics.append("v4_alison_selfie.png")
        show ian at left
        with move
        show v4_alison_selfie
        with short
        $ fian = "surprise"
        i "Wow!"
        $ fian = "shy"
        "Another unexpected selfie from Alison, and this time it was even naughtier!"
        "These kind of surprises really made my day..."
        i "{i}You think the only thing I miss about you are your boobs?{/i}"
        a "{i}Well, I could tell how much you liked them last time...{/i}"
        $ fian = "confident"
        i "{i}I loved them. But that's not the only thing to love about you{/i}."
        a "{i}I'd ask what else there is to love, but you also proved that to me {image=emoji_flirt.png}{/i}"
        i "{i}I will prove it as many times as needed{/i}."
        a "{i}Then I should find other ways to make you cum, too {image=emoji_cum.png}{image=emoji_love.png}{/i}."
        i "{i}I don't mind repeating what already worked{/i}."
        a "{i}So you want to use my boobs again? You're naughtier than I thought, Ian!{/i}"
        i "{i}Look who's talking{/i}."
        i "{i}Now I need to take a cold shower... Or maybe two {image=emoji_fire.png}{image=emoji_fire.png}{/i}"
        a "{i}A could shower? Wouldn't you rather do something else? Or is the pic I sent you not good enough?{/i}"
        "Was she suggesting I should jack off to her picture? I would do that for sure, but that was not something I could admit so openly..."
        i "{i}It's so damn hot {image=emoji_love.png}{/i}"
        a "{i}I'm glad you like it... {image=emoji_flirt.png}{/i}."
        hide v4_alison_selfie
        show ian at truecenter
        with move
    elif v2_alison_home and v2_ian_limp == False:
        a "{i}Really? I hope you enjoyed the picture I sent you, then...{/i}."
        "Was she asking if I had masturbated to the pic she sent me? Of course I did, but that was not something I could admit so openly..."
        i "{i}I had to take a cold shower or two because of it {image=emoji_fire.png}{/i}."
        a "{i}That's what you did? Wouldn't you rather do something else?{/i}."
        i "{i}You're right. Turning the shower hot and adding you as company sounds much better{/i}."
        a "{i}That's something we could do next time... {image=emoji_flirt.png}{/i}"
        i "{i}I'm down for that{/i}."
        a "{i}I'm sure you are... You're naughtier than I thought, Ian!{/i}"
        i "{i}Look who's talking{/i}."
    else:
        if ian_alison_gallery == False:
            $ ian_alison_gallery = True
        i "{i}I had to take a couple of cold showers thinking about you, ha ha {image=emoji_fire.png}{/i}"
        play sound "sfx/sms.mp3"
        a "{i}Speaking of showers... I just took one{/i}."
        $ ian_alison_pics.append("v3_alison_selfie.png")
        show ian at left
        with move
        show v3_alison_selfie
        with short
        $ fian = "surprise"
        i "Wow!"
        $ fian = "shy"
        "I looked at the selfie Alison had just sent me. I wasn't expecting that... But it was a very welcome surprise."
        i "{i}Damn... Now I need another cold shower. Maybe two {image=emoji_fire.png}{image=emoji_fire.png}{/i}"
        a "{i}Are you sure you want to take a cold shower? Wouldn't you rather do something else?{/i}"
        "Was she suggesting I should jack off to her picture? I would do that for sure, but that was not something I could admit so openly..."
        $ fian = "confident"
        i "{i}You're right. Turning the shower hot and adding you as company sounds much better{/i}."
        a "{i}That's something we could do next time... {image=emoji_flirt.png}{/i}"
        i "{i}I'm down for that{/i}."
        a "{i}I'm sure you are... You're naughtier than I thought, Ian!{/i}"
        i "{i}Look who's talking{/i}."
        hide v3_alison_selfie
        show ian at truecenter
        with move
    $ fian = "smile"
    a "{i}Anyways, it's dinner time and my parents are calling me {image=emoji_disgust.png}{/i}."
    a "{i}Seriously, don't ever go back to living with your parents!{/i}"
    i "{i}They don't want me there, ha ha{/i}."
    if v3_alison_boobjob:
        a "{i}Talk to you soon! Enjoy the picture {image=emoji_kiss.png}{/i}."
        i "{i}I will{/i}."
    elif v2_alison_home and v2_ian_limp == False:
        a "{i}Talk to you soon! {image=emoji_kiss.png}{/i}."
    else:
        a "{i}Talk to you soon! Enjoy the picture {image=emoji_kiss.png}{/i}."
        i "{i}I will{/i}."
    $ fian = "happy"
    i "Damn, that was awesome."
    i "She seems totally on board with this..."
    if v4_textscene_check == False:
        jump v4ianfriends
    else:
        jump v4ianmondayend
  
label v4cherrytexting:
    "It was about time I texted Cherry. I had let enough time pass so she wouldn't feel pressured." 
    i "{i}Hey Cherry, how's it going?{/i}."
    "She answered back just a couple of minutes later."
    ch "{i}Hi Ian! I'm fine, a bit stressed because the office is a mess these days!{/i}."
    i "{i}Alison told me about it. I guess that doesn't leave you too much free time{/i}."
    ch "{i}It's hard to come by, yeah{/i}."
    "It was time to test the waters, see if Cherry was interested in meeting again."
    i "{i}Can I borrow some of that free time? I'd like to hang out with you again{/i}."
    ch "{i}Sure, I'd like that, too{/i}."
    $ fian = "happy"
    i "Nice!"
    i "{i}Let me know when you have an available spot for me, then{/i}."
    ch "{i}Of course! That should be soon. I'll give you a call and we can do something{/i}."
    "I tried to probe her a little further."
    $ fian = "confident"
    i "{i}You have something in mind?{/i}"
    ch "{i}I will think of something{/i}."
    i "{i}Should I be excited? You're full of surprises...{/i}"
    ch "{i}Me? Why?{/i}"
    i "{i}Your Peoplegram, for example. I had no idea you were a model{/i}."
    ch "{i}I did some modeling, yeah. So that did surprise you{/i}?"
    i "{i}I should say not really, since I thought you looked like a model as soon as I saw you in that bar...{/i}"
    ch "{i}Ha ha, you did? {image=emoji_flirt.png}{/i}."
    i "{i}Don't act like you're surprised! But you never mentioned it during the night{/i}."
    ch "{i}It's not something I tell people unless it pops up during conversation... And I prefer being judged by who I am rather than by the fact that I have naked pictures on Peoplegram{/i}."
    i "{i}Well, you pass with flying colors on both accounts! I loved your pictures{/i}. Especially this one!"
    "I sent her a link to the picture from her profile I was referring to."
    ch "{i}That's one of my favorites, too {image=emoji_heart.png}{/i}"
    i "{i}I have good taste, as you should already know {image=emoji_flirt.png}{/i}."
    play sound "sfx/sms.mp3"
    $ ian_cherry_gallery = True
    $ ian_cherry_pics.append("v3_peoplegram_cherry2b.png")
    show ian at left
    with move
    show v3_peoplegram_cherry2b
    with short
    $ fian = "surprise"
    i "Oh!"
    $ fian = "shy"
    ch "{i}You deserve a gift for having such good taste {image=emoji_kiss.png}{/i}"
    "She unexpectedly sent me the picture I had told her I liked... Without the censorship."
    "I could finally see Cherry's unfiltered beauty. Her small breasts and perky nipples..."
    "I remembered how they felt to the touch, warm and hard... I wanted to play with them again..."
    i "{i}Damn, Cherry, you leave me speechless {image=emoji_love.png} {image=emoji_love.png}{/i}."
    $ fian = "confident"
    i "{i}Almost as speechless as you left me after we woke up...{/i}"
    ch "{i}You really liked that, huh? It was a very fun night, and a fun morning, too{/i}."
    i "{i}Too fun to do it just once, I'd say{/i}."
    ch "{i}And you'd be right{/i}."
    $ fian = "happy"
    "This was all the confirmation I needed... Cherry was down to sleep with me again!"
    hide v3_peoplegram_cherry2b
    with short
    show ian at truecenter
    with move
    ch "{i}I'm gonna go cook dinner! I'll get in touch as soon as I know when we can meet again{/i}."
    i "{i}I'll be waiting! Bye, Cherry{/i}."
    i "Awesome. That went better than I expected."
    i "I can't wait to meet Cherry again..."
    if v4_textscene_check == False:
        jump v4ianfriends
    else:
        "After that I went to sleep, trying to get some rest for tomorrow."
        jump v4iantuesday
    
label v4ianfriends:   
    
    $ v4_textscene_check = True
    stop music fadeout 2.0
    play sound "sfx/door_home.mp3"
    "I heard keys in the door and Perry arriving home. He wasn't alone."
    i "Is that voice... Wade's?"
    play sound "sfx/door.mp3"
    scene ianhomenight
    with long
    $ fian = "smile"
    $ fperry = "n"
    $ fwade = "n"
    show ian at lef3
    show perry 
    show wade at rig3
    with short
    i "Hey guys. What a surprise seeing you here, Wade."
    p "They were hosting a {i}Sorcery: the Assembly{/i} tournament in the shop and we went to play."
    i "I didn't know you still played card games, Wade."
    w "I hadn't for a long time... But I needed to spend some time outside this weekend."
    $ fian = "n"
    p "Yup, that's why we're gonna have some beers now. Want one?"
    i "Sure..."
    play sound "sfx/beer.mp3"
    "Perry grabbed some cans from the fridge and we sat down on the couch."
    i "So... I take it things haven't smoothed out yet with Cindy? That's why you're here with us today..."
    w "She's been pissed all week, man..."
    $ fperry = "meh"
    $ fian = "sad"
    p "She needs to get over it. She can't get mad at us for not wanting to go to that stupid bar."
    menu:
        "I understand why she's mad":
            $ renpy.block_rollback()
            i "Well, I can understand why she's mad..."            
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            i "It's only natural for a girl like her to want to go out and have fun."
            w "What do you mean by \"a girl like her\"?"
            i "A young and beautiful girl who's full of energy and wants to enjoy life..."
            $ fwade = "serious"
            w "Is that how you see Cindy? And you think she doesn't enjoy life with me?"
            $ ian_wade -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian = "worried"
            i "Hey, I didn't say that."
            w "I hope you didn't, because you and I are not so different. We like to go to the same places and do the same stuff."
            "Maybe before... But now I feared Wade and I had different outlooks and interests in life..."
            $ fwade = "n"
            w "In any case, the problem with Cindy is that she always has to get what she wants."
            w "Things have always to be the way she says." 
            hide friend_down
            
        "She's not very understanding":
            $ renpy.block_rollback()
            i "She's not very understanding, yeah... She's the kind of girl who always wants things done her way."
            $ ian_wade += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            w "That's it exactly, man. It's so hard to put up with it sometimes..."
            i "That said, maybe you two could try to reach an agreement. She has to get away with what she wants sometimes."
            w "Sometimes? She {i}always{/i} gets away with it!"
            hide friend_up
            
        "She's very selfish": 
            $ renpy.block_rollback()
            $ fian = "serious"
            i "You're right, she's very selfish, thinking only about what she wants to do."
            if v3_cindy_date:
                p "It's odd that you say this, since you went with her..."
                $ fian = "worried"
                i "Well, that's... I felt sorry for her and besides, that place is not that bad."
                p "Oh, c--{w=0.5}come on... If you hadn't played along she would've probably stayed. You encouraged her."
                i "I think she would've gone even if it had been on her own."
                w "You can't change her mind once she gets like that. It always has to be like she wants it to be."
            else:
                if ian_perry < 10:
                    $ ian_perry += 1
                    play sound "sfx/friendup.mp3"
                    show friend_up
                p "Exactly! Is it so hard to understand we don't like those kind of places?"
                p "She should know us b--{w=0.5}better. Especially Wade."
                w "Yeah... It always has to be like she wants it to be."
                w "It's so hard to put up with it sometimes..."
                hide friend_up
                
    $ fian = "n"
    i "I don't know, man, it's not my place to tell you how to go about your relationship."
    i "All I can say is I've noticed Cindy feels a bit... bored."
    $ fwade = "sad"
    $ fperry = "sad"
    w "Bored?"
    p "Y--{w=0.5}you mean she's bored of Wade?"
    $ fian = "worried"
    i "No, I didn't mean that...! I mean that she feels kind of stuck."
    w "Stuck?"
    p "She said she f--{w=0.5}feels stuck with Wade!?"
    i "No, not with Wade! It's more like she feels... kinda unsatisfied."
    $ fperry = "surprise"
    p "What the fuck? She told you Wade can't satisfy her in bed?!"
    i "What the--"
    $ fian = "mad"
    i "No, I didn't mean that! Will you shut up already?"
    $ fperry = "sad"
    if v3_cindy_date:
        w "Why do you think that? Has she said anything when you went to that bar?"
        $ fian = "worried"
        i "What? No, she hasn't..."
        p "It's true, how did it go with her? What did you two do?"
        $ fian = "worried"
        i "Uh, well, we had a couple of drinks at the bar, made some small talk..."
        p "Did she say something about Wade?"
        i "No, she didn't. She didn't want to talk about him, in fact."
        w "She didn't?"
        p "Why? W--{w=0.5}what did you ask her?"
        "I was digging myself an ever deeper hole here. Better to cut it off right now."
        i "Nothing, OK? I just asked about the fight that just happened and she didn't want to talk about it."
        i "We just had a few drinks, talked about this and that, boring stuff, and went back home after a while."
        p "I see..."
    else:
        w "Why do you think that? Has she said anything?"
        $ fian = "worried"
        i "No, she hasn't... It's just an idea based on what I see... I might be wrong!"
        i "Just... Never mind, I'm just talking shit."
    p "Women are too c--{w=0.5}complicated..."
    w "I still don't get what you were trying to say, Ian. What do you see, exactly?"
    menu:
        "You need to fight for Cindy":
            $ fian = "sad"
            $ wade_cindy += 1
            i "Maybe... Maybe just that you should try to pay a bit more attention to Cindy's needs."
            if v3_cindy_dance_signs or v3_cindy_reject:
                "It was a bit hypocritical of me saying that after having danced with Cindy while thinking how much I would like to have her..."
                "But in the end I was trying to do the right thing and be a good friend."                
            elif ian_go_cindy > 1:
                "It was a bit hypocritical of me saying that knowing how much I would like to have her for myself..."
                "But those were just harmless thoughts and now I was trying to do the right thing: be a good friend."  
            w "I always do that..."
            i "Doesn't matter. Even if you think you do it, push yourself to do it more, even if just a bit."
            i "You have to take care of a relationship, I would know... Sometimes you have to put in more time and energy during a period of time."
            i "But it will be worth it. I know you love Cindy, you don't want to lose her."
            w "Maybe you're right..."
    
        "I don't want to get involved":
            $ renpy.block_rollback()
            i "Look man, as I said, it's not my place to tell you what to do."
            i "You know Cindy better than I do, so anything I tell you is probably bullshit."
            w "But I'm asking you for your opinion here, man."
            i "What I said earlier will have to be enough. I just don't want to get involved."
            $ ian_wade -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            w "Such a friend you are..."
            hide friend_down
           
        "I don't know, man":
            $ renpy.block_rollback()
            if v3_cindy_date == False:
                i "I don't know, man. As I said, I was just talking out of my ass."
            else:
                i "I don't know, man."
            w "But you think something's wrong?"
            i "What would I know? As Perry said, women are too complicated. Nobody understands them."
            w "I guess you're right..."
    
    $ fwade = "n"
    w "Anyways, let's change the subject. I have plenty of this drama at home."
    $ fian = "n"
    $ fperry = "n"
    stop music fadeout 2.0
    play sound "sfx/doorbell.mp3"
    p "Uh? Who's coming?"
    i "It's Jeremy. He's coming to watch the fights."
    $ fwade = "happy"
    hide perry
    show perry2 
    hide wade
    show wade2 at rig3
    with short
    p "Oh, of course."
    "I got up to open the door for him."
    play music "music/perrys_theme.mp3" loop
    $ fjeremy = "happy"
    $ jeremy_look = 1
    $ fian = "smile"
    show wade2 at right
    show perry2 at rig
    show ian at left
    with move
    show jeremy at centerlef
    with short
    j "Hey, what's up my dudes!?"
    w "Hey Jeremy, long time no see, bro!"
    "Wade reached out with his arm from his seat and high-fived Jeremy."
    if ian_athletics > 1:
        "I guessed getting up was too much effort for him..."
    j "How are you doing, man? Glad to finally see you!"
    j "So you wanna watch the fights with us?"
    $ fwade = "smile"
    w "Why not."
    p "I guess so..."
    "The four of us sat down in the living room, drinking beer and watching the fights while we chatted."
    w "So, how's it going Jeremy? Ian told me you're working at a club or something like that."
    j "Yeah, I'm the bartender. Best job ever."
    w "Really? Working weekends, staying up all night with shit music and drunk people... I'd say it sucks."
    j "You sound just like Ian, man. You enjoyed clubbing back in the day, if I'm not mistaken!"
    w "I only enjoyed the booze and the chicks, ha ha."
    $ fjeremy = "happy"
    j "What do you think I'm there for? I'm in charge of the booze and it's full of hot chicks every night!"
    j "You should see some of those babes, the clothes they wear and the bodies they have..."
    p "Oh, yeah, what happened with that g--{w=0.5}girl you showed us the picture of? The go-go dancer."
    $ fjeremy = "sad"
    j "Eh... Actually, that girl..."
    $ fian = "n"
    i "Turns out Jeremy was caught dating two girls at the same time."
    j "It's not like that man, you know that."
    p "How it is, then?"
    "I told the guys the story of how we met Lena and Ivy when leaving the gym and how they found out Jeremy was actually dating Lena's flatmate."
    $ fperry = "happy"
    hide perry2
    show perry at rig
    with short
    p "No way! That sounds like the p--{w=0.5}plot of one of those stupid sitcoms, ha ha ha!"
    "Wade looked at Jeremy with a big grin on his face."
    $ fwade = "happy"
    w "Dude, you messed up big time."
    j "I never fucked Ivy. And Louise is not exactly my girlfriend..."
    i "Yeah, but \"she thinks she is\". What a thing to say in front of them, dude..."
    w "Wait, you said that? Ha ha ha dude, you're toast."
    "All of a sudden Perry began singing with a really convincing Jamaican accent."
    $ fian = "smile"
    $ fjeremy = "n"
    p "\"{i}To be a true player you have to know how to play, if she say a night, convince her say a day{/i}\"..."
    p "\"{i}Never admit to a word when she say, and if she claims, ah, you tell her, Baby, no way!{/i}\""
    menu:
        "{image=icon_charisma.png}Sing along":
            $ renpy.block_rollback()
            $ fian = "happy"
            "This was too good an opportunity to pass. Wade and I jumped on the chorus."
            pw "\"{i}But she caught me on the counter{/i}\"..."
            i "\"{i}It wasn't me{/i}\"."
            pw "\"{i}Saw me bangin' on the sofa{/i}\"..."
            i "\"{i}It wasn't me{/i}\"."
            pw "\"{i}I even had her in the shower{/i}\"..."
            i "\"{i}It wasn't me{/i}\"."
            pw "\"{i}She even caught me on camera{/i}\"..."
            i "\"{i}It wasn't me!{/i}\"." 
            j "OK, OK, I deserve it. I fucked up."
            if ian_perry < 10:
                $ ian_perry += 1
            $ ian_wade += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            "The three of us laughed for a few seconds still before getting somewhat serious again."
            hide friend_up
            
        "Let them rip on Jeremy":
            $ renpy.block_rollback()
            "Wade jumped on the chorus."
            p "\"{i}But she caught me on the counter{/i}\"..."
            w "\"{i}It wasn't me{/i}\"."
            p "\"{i}Saw me bangin' on the sofa{/i}\"..."
            w "\"{i}It wasn't me{/i}\"."
            p "\"{i}I even had her in the shower{/i}\"..."
            w "\"{i}It wasn't me{/i}\"."
            p "\"{i}She even caught me on camera{/i}\"..."
            w "\"{i}It wasn't me!{/i}\"."
            j "OK, OK, I deserve it. I fucked up."
            "Perry and Wade still laughed for a few seconds before we could get somewhat serious again."
            "That had been pretty funny. It was hard not to at least smile."
            
        "Spare Jeremy the humiliation":
            $ renpy.block_rollback()
            "That was pretty funny, but I decided to spare Jeremy the humiliation."
            "I stopped Perry before he continued to sing. I could see Wade was about to jump in, too."
            i "OK guys, that's enough... I think he got the point."
            j "Yeah, I did."
            $ fjeremy = "smile"
            j "Thanks, bro."
            $ ian_jeremy += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            w "Just as it was getting funny..."
            $ fperry = "meh"
            p "What a way to ruin it."
            hide friend_up
            
    $ fian = "n"
    $ fwade = "n"
    $ fperry = "n"
    $ fjeremy = "n"
    i "So, what will you do about that?"
    if louise_jeremy:
        j "As long as nobody says anything there's nothing I should do."
        i "So you're counting on Lena not telling Louise about you flirting with her friend? That doesn't sound too likely..."
        $ fjeremy = "smile"
        j "So far Louise is acting like always, so it seems Lena hasn't told her."
        j "And if she hasn't done it by now, I'm assuming she won't do it later, either."
        i "Well, seems you won't have problems with your not-girlfriend, but what about Ivy?"
        i "I think you have complicated things with her now, bro."
    else:
        $ fjeremy = "serious"
        j "Well, I wouldn't have to do anything if your girlfriend hadn't told Louise about what happened!"
        i "She's not my girlfriend."
        p "Of course, dude. What did you expect would h--{w=0.5}happen?"
        j "I guess the gentlemen code doesn't apply to women..."
        $ fwade = "smile"
        w "I don't think you can talk about  that gentleman stuff too much, dude, ha ha."
        j "All I'm saying is  that if I found some dude trying to score with a couple of chicks at the same time I wouldn't go telling the other one."
        p "That's because you're a dude."
        i "So, your not-girlfriend knows that you were trying to bone another girl."
        $ fjeremy = "n"
        j "Yeah... She called me the other day, crying and shit. I had to calm her down..."
        p "By telling her a l--{w=0.5}lie?"
        j "By telling her something that would calm her down."
        w "A lie."
        "Perry started singing again."
        p "\"{i}It wasn't me{/i}\"..."
        $ fjeremy = "serious"
        j "Shut up."
        $ fjeremy = "n"
        j "Yeah, I told her what anyone would've told her."
        j "That nothing happened between us, that it was just some harmless flirting, no harm done..."
        j "Assured her nothing will happen. That sort of thing."
        p "All lies."
        i "Not all. I think you have complicated things with Ivy now, bro."
    $ fjeremy = "sad"
    j "Yeah man, that's eating at me...! I was so fucking close!"
    $ fian = "smile"
    i "If I remember correctly, you said you would chop your balls off if you failed to get with her..."
    j "I say a lot of bullshit."
    p "We agree on something, f--{w=0.5}for once."
    w "Why keep this other girl, Louise? I mean, seems that go-go dancer was the girl you really wanted to fuck."
    w "Why waste your time with this Louise?"
    if ian_jeremy > 4:
        $ fjeremy = "flirt"
        j "Do you want me to show you the reason?"
        "Jeremy pulled up his phone and showed us a picture."
        show wade2 at right5
        show ian at left5
        show perry at rig3
        show jeremy at lef3
        with move
        $ fian = "surprise"
        $ fperry = "surprise"
        $ fwade = "surprise"
        show v4_louise_selfie1 with short
        j "Look, this is her."
        $ fperry = "flirt"
        p "Holy shit!"
        $ fwade = "happy"
        w "She's pretty hot, congrats, dude."
        $ fian = "blush"
        i "So this is Lena's flatmate..."
        "Even though she wasn't as pretty or hot as Lena, she was such turn on, that couldn't be denied..."
        "She was slender and sexy, and she had something special about her looks..."        
        hide v4_louise_selfie1
        show v4_louise_selfie2 
        with short
        "Jeremy swiped and showed another pic."
        j "Look, her boobs aren't that great but she has a tight ass."
        p "She sent you these pics?"
        j "Better. She let me take them myself."
        $ fwade = "n"
        w "Damn, I'd love it if Cindy let me take pictures like that..."
        w "But you'll get in trouble if this girl finds out you're showing her sexy pictures around, man."
        j "I'm just showing you because you're my bros. I know I can trust you."
        "He swiped again."        
        hide v4_louise_selfie2
        show v4_louise_selfie3 
        with vpunch
        $ fian = "surprise"
        $ fperry = "surprise"
        $ fwade = "happy"
        $ fjeremy = "surprise"
        i "Dude!"
        j "Oops!"
        hide v4_louise_selfie3
        with short
        show wade2 at right
        show ian at left
        show perry at rig
        show jeremy at centerlef
        with move
        $ fjeremy = "happy"
        j "Sorry, I didn't intend to show you my cock, ha ha."
        $ fian = "disgusted"
        $ fperry = "sad"
        p "That was your f--{w=0.5}fucking cock?"
        j "What, are you impressed?"
        w "What impresses me is that you were trying to stuff that thing into that poor girl's mouth."
        j "Hey, she wasn't complaining, ha ha."
        j "Sex with Louise is pretty hot. She's one of those goth chicks who like it rough..."
        j "She lets me do whatever I want, it's super awesome."
        $ fjeremy = "happy"
        j "So, did I answer your question? Do you get why I want to keep her around?"
        $ fwade = "smile"
        w "Yeah, sure."
        if ian_jeremy > 5:
            menu:
                "{image=icon_friend.png}Send them to me" if ian_jeremy > 5:
                    $ renpy.block_rollback()
                    $ fian = "shy"
                    i "Hey, can you send me the pics? She's pretty hot alright..."
                    $ fjeremy = "evil"
                    j "What, you want to stroke one out to her, is that it?"
                    i "Well, no, I mean..."
                    $ fjeremy = "happy"
                    j "I'm just breaking your balls. I'm happy to share."
                    j "Feel free to stroke out as many as you want, I do it all the time, too!"
                    j "Be sure to keep those pics to yourself, though. I'm trusting you here, bro."
                    $ fian = "smile"
                    i "Sure."
                    play sound "sfx/sms.mp3"
                    $ ian_louise_gallery = True
                    $ ian_jeremy_gallery = True
                    $ ian_louise_pics.append("v4_louise_selfie1.png")
                    $ ian_louise_pics.append("v4_louise_selfie2.png")
                    $ ian_louise_pics.append("v4_louise_selfie3.png")
                    $ ian_jeremy_pics.append("v4_louise_selfie3.png")
                    j "There, sent. Don't show anybody, especially Perry."
                    $ fperry = "meh"
                    p "Hey."
                    i "Of course."
                    $ fperry = "n"
                
                "We've seen enough":
                    $ renpy.block_rollback()
                    i "OK, we get it. We've seen enough."
                    $ fperry = "n"
                    p "Y--{w=0.5}yeah, we have..."
        else:
            $ fian = "n"
            i "OK, we get it. We've seen enough."
            $ fperry = "n"
            p "Y--{w=0.5}yeah, we have..."
        
    else:
        $ fjeremy = "smile"
        j "Fucking chicks is never a waste of time, dude! And I also like Louise, sex with her is pretty hot."
        $ fjeremy = "flirt"
        j "She's one of those goth chicks who like it rough... She lets me do whatever I want, it's pretty awesome."
    w "Not gonna lie, seems you have it good, man... That girl seems to have everything a guy like you could ask for."
    w "That's why I don't get why you need to go messing around. You could lose her."
    w "If I found a girl I really liked I'd be satisfied with being only with her. It's what I did with Cindy, in fact."
    $ fjeremy = "smile"
    j "I'm not one to settle, not yet. If that works for you, go for it..."
    j "But there's still so much pussy I want to crush!"
    if alison_jeremy:
        $ fperry = "meh"
        p "Including Alison's."
        $ fian = "n"
        j "Again with that? Dude, you're not even that close to her. Why does it bother you so much?"
        p "You know what I think about h--{w=0.5}hooking up with people from the inner circle..."
        j "Come on, we all know you'd like to hook up with Emma. Stop it with the hypocrisy."
        $ fperry = "meh"
        hide perry
        show perry2 at rig
        with short
        j "If you want it grow a pair and go for it. We're not judging you."
        p "We weren't t--{w=0.5}talking about Em--{w=0.5}Emma. We were talking about Alison..."
        if v3_alison_sex:
            $ fian = "n"
            "I had something to confess, and this seemed like the moment to do it..."
            i "Jeremy, has Alison said anything about me?"
            j "No, she hasn't. Something like what?"
            i "Well, she called me to go have dinner last Wednesday..."
            j "So?"
            i "We ended up sleeping together, too."
            $ fperry = "surprise"
            $ fwade = "happy"
            p "What? Dude!"
            w "You two are eskimo brothers now, ha ha!"
            i "I suppose she hadn't told you, so that's why I thought I should come clean..."
            j "Good for you, bro. She's got amazing boobs, right?"
            i "Wait, aren't you upset?"
            j "Why should I?"
            i "You hooked up with her before me..."
            j "She's not my girlfriend, bro. She can do whatever she wants with whoever she wants, the same as I do."
            j "I don't have any problem with it... Unless you have it..."
            i "No, I mean... I don't know what kind of relationship you two have."
        else:
            $ fian = "n"
            i "So what kind of relationship do you two have?"
        j "Fuck buddies, nothing more."
        i "But you will keep seeing each other?"
        $ fjeremy = "flirt"
        j "Yes, I guess so. We've hooked up a couple of times already."
        if alison_no_voyeur:
            $ fjeremy = "smile"
            j "But I know you don't want to hear about that, so let's change the subject."
        elif alison_voyeur:
            $ fjeremy = "evil"
            j "I'll show you something good later, in private..."
            i "Oh, OK..."
        else:
            j "Later I'll tell you the details if you're interested... In private."            
    else:
        p "You even had to go for Alison..."
        j "Again with that? Dude, you're not even that close to her. Why does it bother you so much?"
        $ fjeremy = "happy"
        j "Besides, if you wanna give shit to somebody, give it to Ian!"
        j "He's the one who ended up fucking her!"
        $ fian = "shy"
        p "Yeah, and I don't like that either..."
        p "You know what I think about h--{w=0.5}hooking up with people from the inner circle..."
        j "Come on, we all know you'd like to hook up with Emma. Stop it with the hypocrisy."
        $ fperry = "meh"
        hide perry
        show perry2 at rig
        with short
        j "If you want it grow a pair and go for it. We're not judging you."
        p "We weren't t--{w=0.5}talking about Em--{w=0.5}Emma. We were talking about Alison..."
        i "Stop making a big deal out of it."
        if v3_alison_sex:
            p "You brought her home again on Wednesday, right?"
            i "You weren't asleep?"
            p "I heard you getting home with someone... I assumed it would be Alison."
            $ fjeremy = "happy"
            "Jeremy help up his hand, asking for a high-five."
            j "Nice bro, you're slaying it!"
            $ fian = "smile"
            i "I'm trying."
            j "Alison's a great catch, top stuff! I'd love to get a taste of those boobs!"
            j "Hopefully she'll let me soon..."
            $ fian = "worried"
            i "Wait, what?"
        else:
            j "Yeah, man."
            p "You only take Ian's side because you want to fuck her, too."
            j "Of course! And I know she wants it, too."
            j "I saw her this Wednesday, in fact..."
            $ fian = "worried"
            i "Wait, what?"
            j "Yeah, she called me all of a sudden asking if I wanted to have dinner with her that same Wednesday."
            "She had called me to have dinner on Wednesday, too, but that had been the day prior..."
            "So when I said no she decided to call Jeremy instead?"
            i "And did something happen?"
            j "No, she said she had to get up early and go to work the next morning..."
            j "But if it had been Friday I would've fucked her for sure. I can see our sexual tension so clearly."
            p "Wait dude, what are you doing?"
            j "What?"            
        p "You s--{w=0.5}still want to get it on with Alison?"
        j "Of course dude, I already told you guys I wanted to fuck her."
        w "Yes dude, but now Ian's claimed that land."
        $ fjeremy = "smile"
        j "Really? You guys are a couple of self-conscious dinosaurs..."
        j "You see it that way too, Ian? I'm forbidden to try my luck with Alison because you got to her first?"
        menu:
            "Alison's only mine":
                $ renpy.block_rollback()
                $ alison_jeremy_block = True
                $ fian = "serious"
                i "Yes dude, I'm fucking her already. You don't step into another dude's relationship."
                $ fjeremy = "n"
                j "Relationship? What relationship? Are you two dating?"
                $ fian = "n"
                i "No."
                j "You have some sort of special arrangement I should know of?"
                i "No..."
                j "So what's the fucking deal?"
                i "Dude, it's basic etiquette. You don't try to sleep with your friend's hookups."
                w "The bro code, dude."
                j "That line isn't in my bro code, man. That's some self-conscious old-fashioned bullshit."
                j "She's an adult woman and has no formal relationship. If she wants the D that's game for me."
                $ fian = "serious"
                i "I don't see it that way, dude. I'm serious."
                $ ian_jeremy = 3
                play sound "sfx/frienddown.mp3"
                show friend_down
                j "Well, then let's agree to disagree."
                p "So are you s--{w=0.5}still gonna try to fuck her?"
                j "If she wants to..."
                j "Look, if she was your girlfriend it would be different. I do respect that."
                j "But the way I see it you're just fuck buddies with no strings attached."
                $ fjeremy = "smile"
                if v3_alison_sex == False:
                    j "Besides, it was her who called me. And if she wants to have some fun I'm not gonna say no..."
                    j "And you're also trying to hook up with other girls, right? Lena, for example."
                else:
                    j "Besides, you're also trying to hook up with other girls, right? Lena, for example."
                j "Also, if you keep Alison entertained she won't come looking for me, and I have other pussy to chase, too. It's not like I'm hounding her."
                i "That's not the point..."
                j "Dude, as I said, I'm not trying to see who can piss further. That's self-conscious bullshit."
                j "I don't care that you're also sleeping with Alison. Go ahead, have fun! You can also try your luck with Ivy, for all I care!"
                j "Just let everyone do what they want to do. If Alison wants it, who am I to say no to her?"
                $ fian = "n"
                "He had a point, but that didn't make me feel less affronted."
                "Seems like Jeremy was right: all we could do was agree to disagree on this..."
                
            "It makes me uncomfortable": 
                $ renpy.block_rollback()
                $ alison_jeremy_doubt = True
                $ fian = "disgusted"
                i "It actually makes me kind of uncomfortable..."
                $ fjeremy = "n"
                j "Really, dude? {i}Uncomfortable{/i}? Only chicks speak like that..."
                $ fwade = "happy"
                w "I understand him perfectly, ha ha."
                i "Is it so weird for me not to want you to fuck a girl I'm actually fucking myself? Even more so with that girl being Alison."
                j "What has that to do with anything? You two are not dating, are you?"
                $ fian = "n"
                i "Nope..."
                j "Besides, you're also trying to get with other girls, aren't you? Lena, for example."
                i "Yeah, but still..."
                $ fjeremy = "smile"
                j "If she was your girlfriend it would be different, but she's just a friend and a grown woman."
                j "She can make her own decisions and if she wants what she wants she has no boyfriend she would be cheating on, so..." 
                if v3_alison_sex == False:
                    j "I mean, it was her who called me. And if she wants to have some fun I'm not gonna say no to her..."
                    j "Maybe if you keep her entertained she won't come looking for me, and I have other pussy to chase, too. It's not like I'm hounding her."
                else:
                    j "Besides, if you give her what she's looking for she won't have time for me. And I have other pussy to chase, too. It's not like I'm hounding her."
                $ fwade = "n"
                w "It makes sense when you put it that way."
                j "You're welcome to try your luck with Ivy, if you want!"
                j "And if you want Alison just for yourself, you know... put a ring on it!"
               
            "You're welcome to try":
                $ renpy.block_rollback()
                $ fian = "n"
                i "You're welcome to try... She's not my girlfriend nor a kid."
                i "She can make her own choices and I'm not gonna tell her to be with only me..."
                i "I intend to do the same."
                play sound "sfx/xp.mp3"
                show charisma_up
                $ ian_charisma_xp += 1
                call screen skillsup
                j "See? That's how a real man talks!"
                j "You're a real bro, Ian."
                $ ian = "confident"
                i "If I give her all the attention she wants I doubt she'll give you a chance, though!"
                if v3_alison_sex == False:
                    i "She only called you on Wednesday because I canceled on her first!"
                $ fjeremy = "flirt"
                j "I see you're very confident, huh?"
                j "In any case, I have plenty of pussy to pursue other than Alison. I won't go hungry!"
                $ ian_jeremy += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                p "I c--{w=0.5}can't believe these two..."
                w "Let them have their fun..."
  
    $ fjeremy = "smile"
    $ fian = "smile"
    $ fperry = "n"
    $ fwade = "n"
    "Then Wade got up."
    w "Anyways, guys. The fight's over and it's getting late."
    w "I'm calling it a night."
    p "So soon?"
    j "It's a good hour. I'll be leaving, too."
    i "OK."
    stop music fadeout 2.0
    scene ianhomenight
    with long
    "We said goodbye to our friends and went back to our own bedrooms."
    if alison_no_voyeur or alison_jeremy == False:
        jump v4ianmonday
        
## ALISON JEREMY PIC ##########

    play sound "sfx/door.mp3"
    scene ianroomnight
    show ian
    with long
    "I sat in front of the computer again."
    "I didn't want to keep writing today, so I started to procrastinate a bit before going to sleep..."
    play sound "sfx/sms.mp3"
    "Fifteen minutes or so later I got a text."
    "It was Jeremy's."
    j "{i}Wassup bro? Remember I told you I would share something with you in private?{/i}"
    j "{i}It's a picture I took of Alison while she gave me a boob job!{/i}"
    if alison_voyeur:
        j "{i}Since last time you wanted me to tell you the details I thought you might want to see it {image=emoji_devil.png}{/i}"
    else:
        j "{i}Wanna see it? {image=emoji_devil.png}{/i}"
    menu:
        "Show it to me!":
            $ renpy.block_rollback()
            $ alison_voyeur = True
            $ fian = "shy"
            i "{i}OK, show it to me.{/i}"
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            "I knew I was doing something I shouldn't, but I couldn't refuse Jeremy's offer."
            "Some kind of morbid curiosity made we want to take a look at Jeremy's and Alison's sexual intimacy..."
            
        "That's private":
            $ renpy.block_rollback()
            $ alison_no_voyeur = True
            i "{i}No, dude... That's something private between you and her.{/i}"
            i "{i}I shouldn't see it and you shouldn't offer to show it to me.{/i}" 
            if alison_voyeur:
                j "{i}Oh, OK, I thought you didn't see things this way when we last talked. I respect that!{/i}"
            else:
                j "{i}OK, man! I just wanted to share it with you since you're my bro.{/i}"
            j "{i}See you at the gym!{/i}"
            i "What a guy..."
            "After that I wasted some more time on the Internet and went to sleep."
            $ alison_voyeur = False
            jump v4ianmonday
            
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
    i "That motherfucker is hung like a horse. It's not even normal..."
    i "And how the hell did he take this picture? Judging by Alison's mouth, she seems to be a lot into it..."
    $ fian = "worried"
    i "{i}When did you take this?{/i}"    
    if v3_alison_sex:
        j "{i}This Friday. I met with her before going to work.{/i}"
        "Seems like Alison hadn't had enough with me on Wednesday..."
        if alison_satisfaction == 2:
            "She had a bigger libido than I thought... Because I knew for a fact I had left her satisfied."
        elif alison_satisfaction == 1:
            "I was pretty sure she was satisfied with me, but who knows..."
            "Maybe she just had a big libido."
        else:
            "Maybe I hadn't satisfied her as much as I thought?"
    else:
        j "{i}Last Wednesday, I took her to my place after dinner.{/i}"
        "Wednesday... The day Alison asked to meet with me..."
    i "{i}And how did you take it? You asked her and she let you?{/i}"
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
    "I went back to procrastinating for a while before going to sleep."
    jump v4ianmonday
    
##IAN MODAY #######################################################################################################################################################################################################################

label v4ianmonday:    
    $ day = "Monday"
    $ week = 4
    scene blackbg
    with long
    call screen calendar
    play music "music/normal_day.mp3" loop
    scene magazine
    with long
    $ fholly = "n"
    $ ian_look = 1
    $ fian = "n"
    show ian
    with short
    "Another Monday, another morning at the magazine."
    if ian_honest_review or ian_switch_review:
        "The mood at the office had been quite tense after my fight with Minerva. She tried to treat everyone else normally, but you could tell she was on edge."
        "Me, she just ignored, except for some hateful glances she sent my way from time to time when she stepped out of her office."
        "And now she was doing just that, ready to assign the new book reviews."
        $ fminerva ="mad"
    else:
        "Business as usual: mundane and boring tasks, like editing texts and sending e-mails..."
        "Minerva stepped out of her office to assign the new book reviews."
        $ fminerva = "n"
    show ian at lef3
    with move
    show minerva
    show holly2 at rig3
    with short
    mi "Gather everyone, I'm going to hand out this week's books."
    "She began handing out the assignments."
    if ian_honest_review or ian_switch_review:
        "She left me for last, but when my turn came she just frowned and skipped me."
        mi "I have another book due to review, but since Ian can't be trusted with it I will need to ask somebody else to take care of it."
        mi "Holly, I wouldn't ask you if it wasn't completely necessary, but could you take care of it?"
        h "Sure..."
        $ fminerva = "n"
        mi "Thank you, sunshine. You don't need to finish it by Monday, but I would like to ask you to do it as soon as you're able."
        mi "I know you're busy with your own book, but this one should be pretty straightforward to read and review."
    else:
        mi "This one's for you Holly... And this one..."
        mi "\"Competition of Hearts\", this one's for you, Ian. It's an easy one, so be sure to do a good job."
        i "Sure."
    mi "That'll be all."
    hide minerva
    with short
    i "Jeez..."
    if ian_honest_review or ian_switch_review:
        show ian at lef
        show holly2 at rig
        with move
        i "Hey... I'm sorry you're getting extra work because of me."
        h "Don't worry... It's no big trouble... It looks like a pretty short and simple book."
        i "What did you get?"
        h "It's called \"Competition of Hearts\"..."
        "I took the book and read the synopsis on the back cover."
        "\"Amber Clover is a normal young girl who suddenly gets dragged into the revolution to overthrow the despotic tyranny of Pander...\""
        "\"But leading the rebellion will not be her only concern, since she finds herself trapped in a love triangle between a mysterious vampire and a brooding werewolf...\""
        i "Oh, for fuck's sake..."
        if ian_honest_review:
            $ fian = "smile"
            "Then I got an idea."
            i "Hey, why don't you lend me the book while you work on the other review? I can help you with it."
            h "It's not necessary..."
            i "Don't worry. I'll read it for you and write some notes you can use."
            $ fholly = "happy"
            h "Thank you, Ian."
            i "You're welcome."
            hide holly2
            with short
            show ian at truecenter
            with move
            "I would help Holly, but the real reason I wanted that book was different."
            $ fian = "evil"
            "I would write another review like the one I did for \"Poker Love\" and post it online."
            "People at the office had had a blast with it, so I might as well keep doing it... and get some new audience while I was at it."
            "I sat on my desk and decided it was time for the whole world to read what I had to say."
            play sound "sfx/keyboard.mp3"
            "There wasn't too much work today, so I took the time to create a social media account and a blog where I would post my honest reviews bashing the crap publishers were selling."
            "It was the best way I could think of to blow off some steam... the only way."
            "Minerva could censor me in the magazine, but not on the Internet."
            "I took the rest of the shift to set those up and publish my first review..."
        else:
            h "Just another generic teenage romance novel, I guess."
            i "When will they get tired of pumping these out?"
            h "As long as they sell... Anyways, I should get back to work."
            i "Hey, why don't you lend me the book while you work on the other review? I can help you with it."
            h "It's not necessary..."
            i "Don't worry. I'll read it for you and write some notes you can use."
            $ fholly = "happy"
            h "Thank you, Ian."
            i "You're welcome."
            hide holly2
            with short
            show ian at truecenter 
            with move  
            "I sat down at my desk again. There wasn't too much work to do that day..."
            "Then I realized the review for \"The Fall of Delbaeth\" should've been published already! I went to the magazine web page to see people's reaction."
            $ fian = "smile"
            "I scrolled down to the comments and read them. Some of them were really good!"
            "\"I had high hopes for this book and this review confirms them! I can't wait to read it!\""
            "\"If the book is as good and as entertaining to read as this review, it will be an instant classic, no doubt\"."
            "\"Another great review by Holly Watson! Everything she does is gold!\""
            $ fian = "worried"
            i "Wait, what?"
            "I scrolled back up and read the title."
            i "\"The Fall of Delbaeth. Review by Holly Watson\"."
            $ fian = "mad"
            i "What the fuck?!"
            "That bitch! Minerva knew it was me who had written that!"
            "She had credited Holly just to spite me?"
            "I got up and was about to storm into her office and demand an explanation, but I knew how that would turn out."
            "She was looking for an excuse to fire me, and I needed to keep this job right now..."
            "But my blood was boiling. Another of her blatant injustices with me..."
            "If only I could make her pay for it some day..."
    else:
        hide holly2
        with short
        show ian at truecenter 
        with move
        "I looked at the back cover of the book and read the synopsis."
        "\"Amber Clover is a normal young girl who suddenly gets dragged into the revolution to overthrow the despotic tyranny of Pander...\""
        "\"But leading the rebellion will not be her only concern, since she finds herself trapped in a love triangle between a mysterious vampire and a brooding werewolf...\""
        i "Oh, for fuck's sake..."
        i "At least the book is pretty short..."
        "I had to write another bland and praising review Minerva would like, but that was how things were. There was no way around that."
    
    $ v4chatmuseum = False    
    scene ianroom
    with long
    $ ian_look = 2
    $ fian = "n"
    show ian 
    with short
    "I arrived home at the afternoon and decided to do something productive."
    if ian_honest_review or ian_switch_review:
        "I felt like I was wasting my time at the magazine and I still had to find a solution to my money problems."
        "At least I had more free time to invest in productive stuff now... But I had to work on those."
    else:
        "I felt like I was wasting my time at the magazine. I hoped to make a break soon..."
    i "First things first. I need to finish my book."
    if v3_cindy_date and v3_cindy_reject == False and ian_cindy > 3:
        "I was about to get started when I got a call."
        play sound "sfx/ring.mp3"
        i "Who's this?"
        $ fian = "smile"
        i "Cindy?"
        hide ian
        show ian_phone
        show phone_cindy at lef3
        with short
        i "Hey, what's up?"
        c "Hey, Ian! Look, I know it's kinda unexpected, but I learned there's an exhibition in this art gallery and I want to go."
        c "Wanna come with me?"
        i "When, right now?"
        c "Yeah."
        menu cindymuseum:
            "I'm in":
                $ renpy.block_rollback()
                $ v4_cindy_date = True
                if ian_go_cindy == 0:
                    $ ian_go_cindy = 1
                elif ian_go_cindy == 1:
                    $ ian_go_cindy = 2
                $ fian = "happy"
                i "I'm in!"
                c "Cool! Let's meet there at six."
                i "See you in a bit."
                hide phone_cindy
                hide ian_phone
                show ian
                with short
                jump v4cindymuseum
                
            "What about Wade?" if v4chatmuseum == False:
                $ renpy.block_rollback()
                $ v4chatmuseum = True
                $ fian = "sad"
                i "What about Wade?"
                hide phone_cindy
                show phone_cindy_serious at lef3
                c "What about him?"
                i "Have you asked him to go with you?"
                c "Why would I? I'm sure he'll say it's boring and a waste of time."
                i "Are you guys still at odds?"
                if wade_cindy > 0:
                    c "We talked and he apologized... But I haven't called you to talk about that."
                else:
                    c "I haven't called you to talk about that."
                hide phone_cindy_serious
                show phone_cindy at lef3
                jump cindymuseum
                
            "{image=icon_friend.png}You should ask Wade instead" if v4chatmuseum and wade_cindy > 0:
                $ renpy.block_rollback()
                $ wade_cindy += 1
                $ fian = "n"
                i "You should ask Wade instead of me."
                hide phone_cindy
                show phone_cindy_sad at lef3
                c "I've already told you, he will say no..."
                $ fian = "smile"
                i "Try him. You won't know unless you give him a chance."
                if v3_cindy_dance_signs:
                    c "But I was hoping to go with you..."
                else:
                    "She sighed."
                c "I guess you're right. I'll see if he's willing to get off the couch and put down his video games for a bit."
                i "I'm sure he will."
                i "See you, Cindy."
                hide phone_cindy_sad
                hide ian_phone
                show ian
                with short
                $ fian = "n"
                if ian_go_cindy > 2:
                    i "Damn... I wanted to go... But I have to be a good friend to Wade."
                    i "I can't be lusting over his girlfriend..."
                elif ian_go_cindy > 1:
                    i "I would've liked to go... But Cindy was Wade's girlfriend, not mine."
                i "Alright... Where was I?"
                i "Oh, yeah, time to write."
                
            "I'll pass":
                $ renpy.block_rollback()
                $ fian = "n"
                i "I'll have to pass... I was going to work on my book right now."
                hide phone_cindy
                show phone_cindy_sad at lef3
                c "Can't you do that later?"
                i "I can't... You know how important this is to me, and there's still a lot of work to be done."
                play sound "sfx/frienddown.mp3"
                show friend_down
                $ ian_cindy -= 1
                c "Alright... I'll go alone then."
                i "See you, Cindy."
                hide phone_cindy_sad
                hide ian_phone
                show ian
                with short
                if ian_go_cindy > 1:
                    i "I would've liked to go... But Cindy was Wade's girlfriend, not mine."
                i "Alright... Where was I?"
                i "Oh, yeah, time to write."
                
    scene ianroom
    show v2_ianwrite
    with long
    jump v4writing
         
         
##CINDY MUSEUM #########################################################################################################################################################################################################         
               
label v4cindymuseum:    
    stop music fadeout 2.0
    if ian_go_cindy > 2:
        i "Nice!"
        "I wasn't expecting this sudden call, but I was so hyped."
        "I had been thinking about Cindy and our night together... Fearing it had been a one-time thing."
        "But we would have some alone time again, and it was her who asked me..."        
    elif ian_go_cindy > 0:
        "I wasn't expecting this sudden call, but I was pleased by it."
        "I was looking forward to have Cindy's company..."
    scene street
    with long
    $ fian = "smile"
    $ ian_look = 1
    $ fcindy = "smile"
    show ian at lef
    with short
    "I left home right away and met Cindy in front of the gallery."
    play music "music/flirty.mp3" loop
    show cindy2 at rig
    with short
    c "Hey Ian! There you are. Thanks for coming."
    i "I wouldn't miss it. But I'm a bit surprised, how come you called me all of a sudden?"
    $ fcindy = "n"
    c "You know stuff about art and after our conversation the other night I figured out you'd be the right person to go to the gallery with."
    menu:
        "You made the right choice":
            $ renpy.block_rollback()
            i "Wise choice indeed, ha ha."
            c "I still don't know if I made the right choice. I hope you don't prove me wrong!"
            i "We're not even in yet and you're already flooding me with demands! If you want to enjoy this, listen to this suggestion:"
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            i "Just relax, have fun and keep your mind open."
            c "Alright, master."
            if ian_go_cindy > 1:
                i "Master... I like the sound of that."
                $ fcindy = "shy"
                c "Shut up! Who are you and what have you done with Ian?"
                i "Ha ha ha! Come on, let's go."
            else:
                i "Come on, let's go."
            
        "You just want a free tour guide":
            $ renpy.block_rollback()
            i "You just want a free tour guide, don't you?"
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            c "I could use your artistic insight to get more enjoyment of this experience, ha ha."
            i "Oh, so that's it? I feel like I'm being used..."
            c "Oh, come on, I thought you'd like feeling useful..."
            if ian_go_cindy > 1:
                i "And this is the best use you have for me? How disappointing."
                $ fcindy = "flirt"
                c "What were you expecting? I could make you carry my bags when I go shopping, too, if you want me to use you for other things as well."
                i "Bah, forget it. Your ideas are awful."
            i "Come on, let's go."
        
        "You missed my company?":
            $ renpy.block_rollback()
            i "Oh, so you missed my company already?" 
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            i "I never knew you were so fond of me..."
            $ fcindy = "shy"
            c "Don't be an idiot. I just thought you'd tell me stuff I don't know while watching the paintings and stuff."
            i "Oh, so you just wanted a free tour guide? You're the worst."
            c "Nooo, it's not that, idiot!"
            i "Then what?"
            c "I just thought it could be cool visiting the museum with you."
            if ian_go_cindy > 1:
                i "That's what I wanted to hear."
                c "Oh my God, who are you and what have you done with Ian?"
            i "Come on, let's go."
    
    scene gallery
    with long
    $ fcindy = "n"
    $ fian = "smile"
    show ian at lef
    show cindy2 at rig
    with short
    "I had no idea what I was going to see in this gallery, but contemplating art wasn't the reason I was there..."
    "The only other time I had come to this place was because of a girl, too... Though I had had no idea that girl would be Lena."
    "Now I was there with Cindy, and I had no real idea of what I was expecting out of all of this."
    if ian_go_cindy > 1:
        "I shouldn't expect anything out of a friend, but... It was hard forgetting about how attractive Cindy was to me..."
    else:
        "I shouldn't expect anything, though. We were just two friends hanging out."
    "We took a walk around the gallery, looking at the paintings on the walls."
    "The oil paintings were depicting landscapes and architecture, still lifes and a few portraits." 
    c "Mhhh..."
    c "Have you ever painted a picture?"
    i "Once or twice, during my high-school years. I drew way more than I painted."
    c "Is there a big difference?"
    i "Obviously."
    c "I don't know much about art. I like it, but I feel I could appreciate it a lot more if I had a deeper understanding of it."
    i "That's true for all things."
    c "That's what I brought you here for! Teach me something!"
    i "You'll have to be a bit more specific..."
    c "I don't know! Something about art!"
    menu:
        "{image=icon_wits.png}Talk about being creative" if ian_wits > 2:
            $ renpy.block_rollback()
            i "Well, my field is writing, so I'm no expert when it comes to pictures, but I think all artists draw from the same place."
            i "Most people feel art is an expression of self. That's why art is valuable..."
            i "In all of these paintings you can sense the artists' perspective on the world they experience. The way they chose to portray the person, the colors they chose for the landscape..."
            c "Really? I must admit it's hard for me to see beyond the colors and brushstrokes..."
            i "Not everyone connects with the same kind of art. We all have the medium and artists which speak to us."
            i "I love stories the most, that's why I like to read and write. You just have to find your own sensibility."
            c "My own sensibility... Mhh..."
            if ian_cindy < 10:
                $ ian_cindy += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            $ fcindy = "smile"
            c "Interesting! Wade could've never taught me something like that."
            
        "{image=icon_charisma.png}Make something up" if ian_charisma > 2:
            $ renpy.block_rollback()
            i "Uh, well... Art lies in the eye of the beholder, you know?"
            c "What do you mean?"
            i "I mean... Art is inside of you, and a good artist can draw it out of you with his work."
            c "So if I'm looking at some of these pictures and not feeling anything special it's because the artist is bad?"
            i "That can be one reason, yeah... Art is all about feeling."
            i "If something doesn't spark up inside, then you're not connecting with that piece of art and the artist."
            c "Then maybe paintings are not my thing..."
            if ian_cindy < 10:
                $ ian_cindy += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            c "But what you said is very interesting! I could've never learned that with Wade."
            
        "I don't know what to tell you":
            $ renpy.block_rollback()
            $ fian = "n"
            i "Um... I don't know what to tell you, really."
            $ fcindy = "serious"
            c "I thought you'd be able to provide me with some insight."
            i "You're seeing the same pictures as I'm seeing. You can draw the same conclusions..."
            $ ian_cindy -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            c "How boring. I'm kinda glad I didn't drag Wade here..."
            
        "I'm no expert":
            $ renpy.block_rollback()
            i "Well, I'm no expert by any means..."
            c "But you have some artistic sensibility, don't you?"
            i "I hope I do, or my writing career is doomed!"
            i "I guess all art is similar, books or paintings, in that you have to connect with it."
            i "There's no clear reason why you like something or you are indifferent to it. It depends on your own personal sensibilities."
            c "I guess my sensibilities are not very aligned with these paintings, because I find them a bit boring..."
            c "I'm kinda glad I didn't drag Wade here."
    
    $ fian = "n"
    $ fcindy = "n"
    hide friend_down
    hide friend_up
    c "By the way, you saw Wade yesterday, right?"
    i "Yeah, he was at my place with Perry."
    c "Did he say something?"
    i "Something about what?"
    $ fcindy = "serious"
    c "About the current situation... Things have been rather tense, and he never speaks about his emotions."
    c "I don't know if it's a guy thing or he's just too lazy to make the effort..."
    menu:
        "He said you're selfish":
            $ renpy.block_rollback()
            $ wade_cindy = 0
            i "Well... He said he thinks you're a bit selfish and that things always have to be the way you want them."
            $ fcindy = "mad"
            c "He said that, huh? Funny he's accusing me of being selfish when he's even worse!"
            c "It's him who never wants to do anything! We can only do things when he's not feeling lazy, he only cleans up when it's convenient for him..."
            c "And if I suggest he should get his ass out of his comfort zone he gets mad!"
            
        "I shouldn't get involved":
            $ renpy.block_rollback()
            $ fian = "sad"
            i "Cindy, I don't think if I should get involved like this..."
            c "You're my friend, aren't you? I'm asking your help to understand him better..."
            i "You're both my friends, and I don't want to snitch information for either side."
            c "Mhh... OK, if that's how you want it..."
            $ fcindy = "sad"
            c "It's just that it's hard figuring Wade out. Sometimes I don't know what's up with him, if he's bored of our relationship or what..."
    
    if wade_cindy > 0:
        $ fcindy = "sad"
        c "Don't get me wrong, it's not all bad, of course, but..."
    else:
        i "Is it that bad?"
        $ fcindy = "sad"
        c "There are good things, too, of course, but..."
    c "I don't know, I guess I thought I'd get more from life. The future was always full of promises..."
    if ian_cindy > 1:
        i "I know that feeling very well... You don't have it that bad, though..."
    else:
        i "I know that feeling very well... But you don't have it that bad. You can be happy with what you have..."
    c "That's how I tell myself I should feel like, but I can't avoid seeing things this way. I think I already told you the other night..."
    c "But where can I go from here? I have a stable job, I'm living with my boyfriend..."
    i "Life can take unexpected turns..."
    c "And sometimes I wished that'd happen. I feel I'm full of energy and motivation! I want to enjoy life as much as I can!"
    c "But I can't see that hunger for life in Wade at all. I'm beginning to question if he ever had it to begin with..."
    i "I'd say he already has everything he wants from life."
    c "Yes, so it seems... I feel guilty for not having enough with what I have so far..."
    c "Is it my fault not being able to feel satisfied with the life I currently have?"
    if wade_cindy > 0:
        i "I don't think trying to figure out who's at fault is helpful. Maybe you should bring this up to Wade."
        i "Discuss what you'd like to change to feel more satisfied..."
    else:
        i "I don't think it's your fault. It's normal to feel dissatisfied if you're not living the life you want for yourself..."
    i "But what is it that you actually want?"
    c "That's the problem... I'm not sure..."
    c "I see some girls on Peoplegram and they seem to have it all. Sometimes I envy their lives..."
    menu:
        "You could be one of those girls":
            $ renpy.block_rollback()
            if ian_go_cindy < 2:
                $ ian_go_cindy += 1
            $ fian = "smile"
            i "You could be one of those girls, if you wanted it."
            $ fcindy = "shy"
            c "You think so?"
            i "I mean, I have no idea how one becomes an influencer, but you look the part without a doubt."
            i "You're young, beautiful, and look at that smile..."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            $ fcindy = "shy"
            c "Ian...!"
            i "You have to work a bit on that personality of yours, though."
            c "Ha ha, you idiot."
            if ian_cindy < 10:
                $ ian_cindy += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            c "It's good to see you believe in me to such extent."
            
        "Don't let that influence you":
            $ renpy.block_rollback()
            $ fian = "n"
            i "Don't let that influence you. What you see on Peoplegram is not real life."
            i "Behind those perfectly edited photos they are normal people, just like you and me."
            c "I don't know about that. Normal people like us never spend the summer at a tropical beach, sailing on a ship or going to the best clubs and restaurants..."
            i "Is that what you really want?"
            c "Who would say no to that? Influencers even get free stuff from brands all the time!"
            i "I'm sure you'd love that..."
         
        "You're searching for yourself":
            $ renpy.block_rollback()
            $ fian = "smile"
            i "You're searching for yourself, Cindy. Trying to figure out what's your calling in life, what you enjoy..."
            c "Anyone would think I should've figured that out by now. You're super clear about what your calling is."
            i "Don't mind what others think. My passion has always been very clear to me, but I still have doubts sometimes."
            i "Everyone takes a different time to figure it out. And a lot of people never find their passion."
            i "Don't kick yourself in the teeth for not having figured it out yet."
            i "You're searching, and that's what makes the difference between those who discover their passion and those who don't."
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            $ fcindy = "smile"
            c "Those are wise words! I'll try to remember them."
            if ian_cindy < 10:
                $ ian_cindy += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            c "Thank you, Ian."
            
        "All you see on Peoplegram is fake":
            $ renpy.block_rollback()
            $ fian = "n"
            i "All you see on Peoplegram is fake. A doctored portrait of those people's lives."
            i "They only upload the best highlights of their life, but you don't know what's happening behind the cameras..."
            i "It's all an act and they're full of hypocrisy."
            $ fcindy = "n"
            c "I would still love to have those fake highlights in my life."
            c "Traveling, spending the summer, sailing on a boat, going to the best clubs and restaurants, getting free stuff from brands all the time..."
            c "Maybe it's fake, but I'm sure it's way more enjoyable than my actual life."
    
    hide friend_up
    "We continued to walk through the gallery as we talked."
    "We were now in an area were photographs were exhibited instead of paintings."
    "And then we saw it."
    $ fian = "surprise"
    $ fcindy = "surprise"
    show ian at left
    show cindy2 at right
    with move
    if v1_choosepic == 1:
        show v2_frame1
        with short
    if v1_choosepic == 2:
        show v2_frame2
        with short
    if v1_choosepic == 3:
        show v2_frame3 behind cindy2, ian
        with short
    if v1_choosepic == 4:
        show v2_frame4 behind cindy2, ian
        with short
    c "Hey, isn't this girl the one you talked to me about?"
    "She was. Lena."
    $ fian = "worried"
    i "Yeah..."
    "It seemed destiny wanted me to find her unexpectedly all the time. Her, or her image in this case."
    $ fcindy = "blush"
    c "Wow, look at her, she's so beautiful..."
    if v1_choosepic == 1:
        c "You showed me this picture on your phone, but seeing it like this is even more impressive..."
    else:
        c "You showed me a picture on your phone, but here she looks even more impressive..."
    "It was. And seeing her in the flesh was even better."
    c "She's a work of art."
    c "Hmm... I'm too skinny compared to her..."
    $ fian = "sad"
    "I looked at Cindy. What was up with her, suddenly expressing her self-consciousness out loud?"
    menu:
        "{image=icon_lust.png}You're hotter than she is" if ian_lust > 1 and ian_go_cindy > 0:
            $ renpy.block_rollback()
            if ian_go_cindy < 3:
                $ ian_go_cindy = 3
            $ fian = "confident"
            i "Really? I think you're hotter than she is."
            i "I'd prefer if it was you in that picture, to be honest."
            $ fcindy = "flirt"
            "She playfully punched me on the arm."
            c "You would like that, wouldn't you? Ha ha ha."
            i "What can I say? I'm sure it'd be a glorious sight to behold."
            c "Are you trying to convince me with those fancy words of yours?"
            i "It isn't working?"
            c "I think you need to keep trying a bit more..."
            if ian_cindy < 10:
                $ ian_cindy += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            i "Well, if it's only a bit..."
            
        "{image=icon_charisma.png}You're as beautiful as she is" if ian_charisma > 1:
            $ renpy.block_rollback()
            if ian_go_cindy < 3:
                $ ian_go_cindy += 1
            $ fian = "smile"
            i "You're as beautiful as she is."
            c "That's not true..."
            i "Well, I can't change the way you see yourself, but I can tell you the way I see you."
            i "And I know almost everyone shares my view on that."
            i "It could perfectly be you in that picture, and it would be stunning, too."
            $ fcindy = "shy"
            c "You really believe that?"
            i "I'm not trying to make you feel better. Well, I do, but not by lying to you."
            i "Hundred percent honest, I swear."
            c "You're so cute sometimes."
            if ian_cindy < 10:
                $ ian_cindy += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            
        "Don't compare yourself to her":
            $ renpy.block_rollback()
            $ fian = "n"
            i "Don't compare yourself to her."
            $ fcindy = "sad"
            c "It's hard not to. Look at her, she's being exhibited in a gallery like a work of art. Meanwhile, I..."
            i "Comparing yourself to others is the best route to unhappiness."
            c "Seems there are many routes to unhappiness! Too many."
            
        "You could eat more":
            $ renpy.block_rollback()
            $ fian = "happy"
            i "You're a bit bony, yeah. You could eat a bit more."
            $ fcindy = "serious"
            c "Thanks, that's exactly what I needed to hear."
            i "Hey, I'm not saying it in a bad way! You can eat all you want and it will be good for you..."
            i "Do you know how many people would kill to be in that position?"
            c "So should I start stuffing my mouth full of chocolate doughnuts?"
            i "I'm sure that would cheer you up."
            $ fcindy = "n"
            c "I doubt that's the solution."
    hide v2_frame1
    hide v2_frame2
    hide v2_frame3
    hide v2_frame4
    with short
    show ian at lef
    show cindy2 at rig
    with move
    $ fian = "n"
    i "By the way, I haven't asked yet, but..."
    i "What's up with that guy we met at the bar? Are you gonna take him up on his offer?"
    $ fcindy = "sad"
    c "Axel? I've been thinking about it..."
    c "I want to, but I'm still somewhat undecided..."
    i "Why?"
    c "I've never done anything like that, and I don't really know what kind of guy Axel is."
    c "I have no idea if it's a situation I will feel comfortable in... But I wanna do it."
    i "So you've made your choice already."
    c "I guess so..."
    $ fcindy = "n"
    if ian_cindy_model:
        c "Now that I think of it, you said you wanted to see my work as a model."
        $ fian = "shy"
        i "I did, yeah."
    if ian_cindy_model or ian_cindy > 5:
        c "I have an idea. Why don't you come with me to the photo-shoot?"
        $ fian = "surprise"
        i "Me?"
        c "Yeah... I'd be more comfortable with someone I can trust. I don't want to be alone with the photographer on my first time posing."
        menu:
            "I'll go with you":
                $ renpy.block_rollback()
                $ v5_cindy_shoot = True
                $ ian_go_cindy = 3
                $ fian = "smile"
                i "Sure, I'll go with you."
                $ fcindy = "smile"
                c "You will? Cool!"
                i "When will it be?"
                c "I don't know, I haven't even accepted yet."
                c "I'll text Axel and let you know."
                            
            "{image=icon_friend}You should bring Wade" if wade_cindy > 0:
                $ renpy.block_rollback()
                $ fian = "n"
                $ wade_cindy = 2
                if ian_go_cindy > 1:
                    $ ian_go_cindy = 1
                i "Don't you think you should bring Wade instead?"
                $ fcindy = "sad"
                c "I don't know about that..."
                i "You haven't told him about the photo-shoot yet, have you? And if he learns you went without telling him and brought someone else he'll get mad for sure."
                i "If you really want to go and need someone to keep you safe, you should tell Wade. He's your boyfriend after all."
                c "I guess you're right..."
                
            "I don't think it's a good idea":
                $ renpy.block_rollback()
                if ian_go_cindy > 1:
                    $ ian_go_cindy = 1
                $ fian = "sad"
                i "I don't think it's a good idea..."
                $ fcindy = "sad"
                c "Why not?"
                i "I don't think I'm the right person to go with you. You should ask someone else..."
                i "One of your girl friends. Or Wade, maybe."
                i "I don't want him to get mad at me for going with you, especially when he knows nothing about it."
                c "If that's what you want... I'll try to find someone else to keep me company."
             
    $ fcindy = "n"
    c "Well, we've seen everything there is to see here already, haven't we?"
    $ fian = "smile"
    i "Seems so. Time to go."
    stop music fadeout 2.0   
    scene streetnight
    with long
    show ian at lef
    show cindy at rig
    with short
    c "Thanks for coming with me today. It's been fun!"
    i "Thanks you for thinking about me and calling."
    if ian_cindy > 6 and ian_go_cindy == 3:
        c "Of course I thought about you. We should do this more often!"
        i "Anytime."
        c "See you soon! Bye!"
        hide cindy
        with short
        i "I don't think this could've gone any better... She said she thinks about me..."
    elif ian_cindy > 6 and ian_go_cindy == 2:
        c "You were my first option! It's fun hanging out with you."
        i "Good to know."
        c "See you soon! Bye!"
        hide cindy
        with short
        i "Seems like she really enjoyed my company..."
    else:
        c "Anyways, see you soon! Bye!"
        hide cindy
        with short
        i "I'd say we get along pretty nicely, Cindy and me..."
    i "Well, time to go home and do some writing."
    scene ianroomnight
    with long 
    $ fian = "smile"
    $ ian_look = 2
    play music "music/normal_day.mp3" loop
    show ian
    with short
    "I arrived home a bit before dinner time, but I wasn't hungry."
    if v5_cindy_shoot:
        "I couldn't believe Cindy had invited me to go with her to her first photo-shoot..."
        "I would get the chance to see something sexy, I was sure. The situation was a bit weird and made me nervous, but I couldn't wait!"
        i "Anyways..."
    "I sat in front of the computer and tried to focus on the task at hand."
    scene ianroomnight
    show v2_ianwrite
    with long
    
##IAN WRITE ################################################################################################################################################################################################################

label v4writing:
    "I had already chosen the genre of my book and its call to adventure."
    "Now I had to define another basic aspect, and a very important one: who was the antagonist?"
    i "They say a story is only as good as its villain. I need to pick one that's interesting and fitting..."
    if book_scifi:
        "What kind of antagonist could work with my {color=#3FB305}Science Fiction{/color} novel?"
    if book_fantasy:
        "What kind of antagonist could work with my {color=#B30505}Fantasy{/color} novel?"
    if book_historical:
        "What kind of antagonist could work with my {color=#D1B402}Historical{/color} novel?"
label v4_writebookchoice:
    call screen book_screen_3
    if book_card2 == "dark_lord":
        i "I will write a Dark Lord as the enemy."
        i "The incarnation of evil, a powerful figure that's hellbent on domination and destruction."
        i "A terrifying force that seems impossible to overcome..."
        menu:
            "Choose this card":
                $ renpy.block_rollback()
                if book_scifi:
                    i "Mhh... A Dark Lord in a sci-fi book? Sure, why not? It could work."
                    i "It can be a space conqueror or some sort of evil cosmic entity..."
                if book_fantasy:
                    i "What's a fantasy book without a Dark Lord? It's true and tested."
                    i "All great fantasy stories have one... I should have one, too."        
                if book_historical:
                    i "You could easily say someone like Hitler or Stalin were real-life Dark Lords..."
                    i "I'm sure I can find other examples in History."
                        
            "Try something else":
                $ renpy.block_rollback()
                jump v4_writebookchoice

    if book_card2 == "villain":
        i "The bad guy in this story will be a credible villain."
        i "Not someone who's evil for the sake of being evil, but a real human being with his own goals and motivations."
        i "A dangerous and morally reprehensible one at that, though. Someone you can understand and hate at the same time."
        menu:
            "Choose this card":
                $ renpy.block_rollback()
                if book_scifi:
                    i "A treacherous and violent antagonist can fit in my sci-fi book."
                    i "Someone evil who's hellbent on destroying anyone who gets between him and his selfish goals..."
                if book_fantasy:
                    i "I think using this kind of antagonist will work best in my fantasy book."
                    i "Writing an enemy who's grounded and gritty, far from fantasy's tropes."        
                if book_historical:
                    i "History is full of villains, people with selfish and seedy interests that stepped on everyone else..."
                    i "Treachery, tyranny, murder... All that sounds pretty villainous."
                                
            "Try something else":
                $ renpy.block_rollback()
                jump v4_writebookchoice
        
    if book_card2 == "relativistic":
        i "I want to try with a relativistic antagonist."
        i "Someone who the reader can't truly figure out whether he is good or bad. Someone who fights for his own interests, someone you can understand and even side with..."
        i "Even if he does awful things during the story. They will be justified from his point of view..."
        menu:
            "Choose this card":
                $ renpy.block_rollback()
                if book_scifi:
                    i "Sci-fi is the perfect space for grays: no absolute goodness or evilness."
                    i "Questioning morality is questioning culture and society itself, so it will work perfectly."
                if book_fantasy:
                    i "Someone who's neither good nor bad, someone chaotic with his own interests..."
                    i "It could work in a fantasy setting."
                if book_historical:
                    i "Nothing's black or white in History. It's all a conflict of interests."
                    i "Everyone's the hero in their own eyes, making the other the bad guy... It's an interesting insight."
                
            "Try something else":
                $ renpy.block_rollback()
                jump v4_writebookchoice
                
    if v4_cindy_date:
        "I was so engrossed with writing that I even skipped dinner."
    else:
        scene ianroomnight
        show v2_ianwrite
        with long
        "I was so engrossed with writing that I continued to write all afternoon and even skipped dinner."
    play sound "sfx/keyboard.mp3"
    "I felt the ideas and the words flowing through my fingers, the characters coming alive as my fingers danced over the keyboard..."
    if ian_alison_sex and v4_alison_sexting == False:
        $ v4_alison_sexting = True
        play sound "sfx/sms.mp3"
        scene ianroomnight
        show ian
        with long
        "Then the buzz of my phone brought me out of the zone and back to the real life."
        i "Who's texting at this hour?"
        i "Oh, it's Alison..."
        a "{i}Hey! How are you doing? Haven't heard from you in a while!{/i}" 
        i "{i}Hey Alison. I've been busy writing, in fact it's what I was doing just now{/i}."
        a "{i}Working hard on your book as always, huh? Maybe I'll read it when you're done!{/i}"
        i "{i}Still a long way to go for that. So, how was your weekend?{/i}."
        a "{i}Oof, it's been pretty awful. Taking care of things from work...They have an incredible mess in that office!{/i}"
        jump v4alisontexting 
    else:
        scene ianroomnight
        show ian
        with long
label v4ianmondayend:
    stop music fadeout 2.0
    $ fian = "n"
    play sound "sfx/door_home.mp3"
    "I heard the front door. Someone had just arrived."
    "Perry, at this hour?"
    play sound "sfx/door.mp3"
    $ fperry = "n"
    scene ianhomenight
    show ian at lef
    show perry at rig
    with long
    i "Hey, here you are. Where were you?"
    "Truth be told I hadn't even noticed he was gone, engrossed as I was in my writing."
    p "Hey. Today was my f--{w=0.5}father's birthday, so we went to a nice restaurant to celebrate."
    i "Oh, that's true. He always takes you out to expensive places... Must be nice being the son of the Mayor."
    $ fperry = "meh"
    hide perry
    show perry2 at rig
    with short
    p "It wasn't always like that. He's only been the Mayor for four years."
    i "You seem bothered by it."
    p "You know I don't like being dragged into p--{w=0.5}political arguments and all that stuff. I don't want to have anything to do with that."
    p "That's why my parents are always giving me a h--{w=0.5}hard time. They would like me to be the perfect tie-wearing son."
    i "I don't think they want you to wear a tie. But you could've gotten a college degree or at least a job..."
    p "That's what I'm saying, they would've l--{w=0.5}liked me to be different. You should understand me, your parents are the same."
    p "They never liked you wanting to be a w--{w=0.5}writer."
    $ fian = "sad"
    i "Yeah... They wish I would've studied something different, finances or something like that."
    i "\"Wasted potential\", my father called it..."
    hide perry2
    show perry at rig
    with short
    $ fperry = "n"
    p "Anyways, guess who was w--{w=0.5}working at this restaurant we went to tonight."
    i "Who?"
    p "Lena."
    $ fian = "surprise"
    i "Lena, really?"
    p "Yup."
    $ fian = "worried"
    i "Seems like she's everywhere... So she's a waitress at this restaurant?"
    p "Yes. It's at the top floor of this hotel and man, the food's delicious..."
    if v4_robert_public:
        p "The service was not stellar, though... We had to call for another waiter to bring our desserts, since Lena disappeared for a while."
        i "I guess it's a very busy job. She must've been caught up with other customers."
        p "I don't know, but she was nowhere in sight."
    else:
        p "She was really nice and I told my dad to tip her generously."
        i "I'm sure she was happy about getting a big tip from the Mayor."
    i "Anyways, did she say something?"
    p "Yeah, she t--{w=0.5}told me to say hello to you, and I told her she should come have some beers with us."
    i "Where, here?"
    p "Yeah, why not?"
    i "I see..."
    p "Anyways, I'm going to bed. It's late."
    i "Yeah, I should do that, too."
    if ian_cherry_free and v4_cherry_sexting == False:
        play sound "sfx/door.mp3"
        scene ianroomnight
        show ian
        with long
        "I went back to my room. I was a bit tired and could go to bed, but..."
        "Maybe now was the right moment to text Cherry."
        menu:
            "Text Cherry" if ian_cherry_free:
                $ renpy.block_rollback()
                $ v4_cherry_sexting = True
                jump v4cherrytexting
            
            "Go to bed":
                $ renpy.block_rollback() 
                i "Nah... Better leave it as it is."
                "I left my phone on the table and went to sleep."
                jump v4iantuesday
    
##IAN TUESDAY #########################################################################################################################################################################################################

label v4iantuesday:   
    $ day = "Tuesday"
    scene blackbg
    with long
    call screen calendar
    scene magazine
    with long
    play music "music/normal_day.mp3" loop
    $ fian = "n"
    $ ian_look = 1
    show ian with short
    "I went to work first thing in the morning."
    if ian_switch_review or ian_honest_review:
        "This week would be very short, though. Since my fight with Minerva I only had to go to the office from Monday to Wednesday."
    else:
        "It was only Tuesday and I was already wishing for the week to be over..."
    if ian_switch_review:
        $ fholly = "sad"
        show ian at lef
        with move
        show holly3 at rig
        with short
        h "Hey, Ian... I..."
        h "I just found out about the review. I know they published it under my name instead of yours..."
        h "I'm so sorry..."
        i "It's not your fault. You don't have anything to apologize for, Holly."
        h "Still, it's so unfair. Have you told Minerva?"
        i "What good would that do? She won't listen to me."
        h "I will speak with her..."
        i "I don't want you to get into trouble. She hates it that I dragged you into this trick I pulled on her."
        i "Last thing you want is to get on her bad side, too..."
        show ian at lef3
        show holly3 at rig3
        with move
        $ fminerva = "n"
        $ fholly = "n"
        show minerva
        hide holly3
        show holly2 at rig3
        with short
        i "Speaking of her..."
    else:
        $ fholly = "n"
        $ fminerva  = "n"
        show ian at lef3 with move
        show minerva
        show holly2 at rig3
        with short
        "Just before lunch Minerva came out of her office to give an announcement."
    mi "Please, listen everybody. I have great news."
    mi "You all know who Seymour Ward is, CEO of Hierofant publishing, amongst other business, and a big philanthropist."
    mi "He will be paying us a visit this next Friday!"
    $ fian = "surprise"
    "Murmuring spread across the whole office after hearing that announcement."
    "Hierofant was  one of the top publishers in the country, and Seymour Ward a very important individual."
    $ fian = "n"
    i "Why is he coming here?"
    $ fminerva = "mad"
    if ian_switch_review or ian_honest_review:
        mi "The exact reasons of his visit are for him to disclose, and in any case, it doesn't concern you."
        mi "He's coming on Friday, and you're not working that day, as you might've remembered."
        mi "So I don't want to see you in here."
        $ fian = "serious"
        "She was openly kicking me out in front of the whole office. I felt ashamed and furious."
        mi "Anyways, I don't need to tell you how important this visit is."
        mi "We have been working closely with Hierofant for quite some time and I want to make Mr. Ward feel welcome and to show how professional we are."
        mi "I won't tolerate any rude or inappropriate behavior, is that clear?"
        "She looked at me after saying that sentence, and held her stare for a few, menacing seconds."
        "I forced myself to remain silent. Arguing with her would only cause further trouble."
        "But Minerva was barring me from one very big opportunity, and she knew that."
        $ fian = "worried"
        "Seymour Ward was a really big fish in the literary world. If I could do some networking with him..."
        "Maybe I could give him a draft of my book to see if he was interested. If I managed to catch his eye that could open me the doors to becoming a professional writer once and for all."
        "I wouldn't even need to win the literary contest to become a published author!"
        "Just the shortcut I was hoping for, sinc eI knew winning that contest was naerly impossible..."
        "But Minerva was standing right in front of my dream, denying it."
        "If I could only show Mr. Ward my work, maybe..."
    else:
        mi "He's taken interest in our magazine, since we've been working closely with Hierofant for quite some time."
        mi "The exact reasons of his visit are for him to disclose, but I don't need to tell you how important this visit is."
        mi "We want to make him feel welcome and to show him how professional we are."
        mi "I won't tolerate any rude or inappropriate behavior, is that clear?"
        "She said that while looking at me."
        "I decided to just remain silent. Answering back wouldn't have been a good idea."
        $ fian = "worried"
        "I had something in mind that Minerva would consider inappropriate for sure, though."
        "Seymour Ward was a really big fish in the literary world. If I could do some networking with him..."
        "Maybe I could give him a draft of my book to see if he was interested. If I managed to catch his eye that could open me the doors to becoming a professional writer once and for all."
        "I wouldn't even need to win the literary contest to become a published author!"
        "Just the shortcut I was hoping for, sinc eI knew winning that contest was naerly impossible..."
        "But if I did that, Minerva would get mad for sure. Maybe I could do it without her noticing?"
    "In any case, if I wanted to do that, I had to work my ass off to create a good synopsis and polish the two or three first chapters of the book to make sure they were perfect."
    "I had to hand him my best material, one that would make him consider betting on me as a writer..."
    "It was a chance I wasn't sure I could afford to lose."
    hide minerva
    with short
    $ fian = "n"
    show ian at lef
    show holly2 at rig
    with move
    "After my shift ended Holly approached me."
    $ fholly = "blush"
    hide holly2
    show holly3 at rig
    with short
    h "Hey... I was wondering if it's not too much trouble and you don't have anything else to do, maybe..."
    h "We could get a coffee together if that's OK..."
    $ fian = "smile"
    i "I have an hour or so before going to the gym. We can go, of course."
    $ fholly = "happyshy"
    h "Cool."
    
    $ v4_proposeholly = False
    $ flena = "smile"
    $ lena_look = 1
    scene cafe
    with long
    $ fholly = "smile"
    show ian 
    show holly at lef3
    with short
    "We went straight to the café and Lena greeted us."
    show lenawork at rig3
    with short
    "It was the first time I had seen her after our unexpected meeting at the gym."
    l "Hey guys! Nice to see you here! What can I get you?"
    h "Matcha latte for me."
    i "For me a coffee with a shot of brandy."
    l "Oh, wow, you're going strong today!"
    $ fian = "n"
    i "I'm going to the gym right after this. And I had a rough day at the office..."
    $ flena = "sad"
    $ fholly = "sad"
    l "What happened?"
    if ian_switch_review or ian_honest_review:
        "I told Lena about Seymour Ward's visit and how Minerva was forbidding my attendance, barring me from a great opportunity."
    else:
        "I told Lena about how Minerva continued to under-value me and the dilemma of handing Mr. Ward my book proposal or not, risking angering Minerva."
    $ flena = "worried"
    l "Wait, Mr. Ward? You mean Seymour Ward?"
    i "Yes."
    l "I know him."
    $ fholly = "n"
    i "He's a very important figure in the industry."
    l "No, I mean I personally know him."
    $ fian = "surprise"
    i "You do?"
    if v4_seymour_date:
        $ flena = "n"
        l "Yeah, I worked for him very recently. As a model."
        i "No way! Did you pose for him?"
        l "We've only worked together just once so far, but it seems he's interested in keeping to collaborate."
        $ fian = "sad"
        i "He's also a photographer?"
        l "An amateur."
        h "It seems he's a man of many talents, or so they say. I've never met him myself but he's very much talked about."
        i "Damn, you're well connected, Lena..."
    elif v3_seymour_date:
        $ flena = "serious"
        l "He wanted me to pose for him and took me out to dinner..."
        i "What? Out to dinner? No way! Did you work with him?"
        l "No. I didn't like the offer he was making... He's not a man I would trust. I don't like his vibe at all."
        $ fian = "sad"
        i "Really? I never knew..."
        h "I've heard he can be a bit intimidating. I've never met him myself but he's very much talked about."
        i "Damn, you're well connected, Lena..."
        $ flena = "n"
        l "There are some connections that are better not made."
    else:
        $ flena = "serious"
        l "I met him at an exhibition... He wanted to hire me as a model."
        $ fian = "surprise"
        i "No way! Did you work with him?"
        l "No. I didn't like the offer he was making... He's not a man I would trust. I don't like his vibe at all."
        $ fian = "sad"
        i "Really? I never knew..."
        h "I've heard he can be a bit intimidating. I've never met him myself but he's very much talked about."
        i "Damn, you're well connected, Lena..."
        $ flena = "n"
        l "There are some connections that are better not made."
    menu decidev4proposal:
        
        "I will hand him my proposal myself":
            $ renpy.block_rollback()
            $ v5_hand_proposal = True
            $ fian = "serious"
            i "I will hand Mr. Ward my proposal myself, even if Minerva doesn't like it."
            h "Are you sure about that...?"
            i "Yes, I won't let this chance slip. And it's not something I should ask anyone else to do."
            i "I'll take full responsibility of it myself, and of its consequences."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            l "That's really brave. I hope everything turns out alright."
            
        "Ask Lena to hand your proposal to Seymour" if v4_seymour_date and ian_lena > 5:
            $ renpy.block_rollback()
            $ v5_hand_proposal_lena = True
            i "Um, Lena... I hate to ask this of you, but do you think you'd be able to hand Mr. Ward my proposal in my place?"
            l "I don't see why not."
            $ fian = "smile"
            i "Really? You'll do that?"
            l "It's no big deal for me. I will give it to him and ask him to read it."
            i "Thank you, Lena! This could be a big chance for me."
            l "I hope it is!"
            if v4_proposeholly == False and ian_switch_review or v4_proposeholly == False and ian_honest_review:
                h "I'd offer my help, too, but this Friday I'm not at the office..."
                h "I have a meeting with my editor to check on how the new book is coming along..."
                i "Don't worry, it's already solved."
            i "I'll give you a copy when I've written the synopsis and all that stuff, Lena."
            
        "Ask Holly to hand your proposal to Seymour" if v4_proposeholly == False and ian_honest_review or v4_proposeholly == False and ian_switch_review:
            $ renpy.block_rollback()
            $ v4_proposeholly = True
            i "Holly... I hate asking this of you, but could you hand Mr. Ward my proposal instead of me?"
            i "Since Minerva won't let me show myself at the office that day..."
            h "I would like to help you, but this Friday I'm not at the office..."
            h "I have a meeting with my editor to check on how the new book is coming along..."
            i "Oh, I see... Sorry that I asked."
            h "It's OK..."
            jump decidev4proposal
            
        "Forget about contacting Seymour":
            $ renpy.block_rollback()
            i "Bah, I should forget about it."
            if v4_proposeholly == False and ian_switch_review or v4_proposeholly == False and ian_honest_review:
                h "I would like to help you, but this Friday I'm not at the office..."
                h "I have a meeting with my editor to check on how the new book is coming along..."
                i "Don't worry, I wouldn't ask you to bear that responsibility either way."
            if ian_lena > 5 and v4_seymour_date:
                l "Do you want me to help you? I could give it to him and ask him to read it."
                i "You'd do that?"
                l "Sure, it's no big deal for me."
                menu:
                    "Accept Lena's help":
                        $ renpy.block_rollback()
                        $ v5_hand_proposal_lena = True
                        i "I don't like asking this of you, but... OK, I'll take your help."
                        l "You're not asking, I'm offering, so don't feel bad about it."
                        $ fian = "smile"
                        i "Thank you so much, Lena."
                        i "I'll give you a copy when I've written the synopsis and all that stuff."
                        
                    "Decline Lena's help":
                        $ renpy.block_rollback()
                        i "Never mind, it's OK like this."
                        i "I'll find another way to reach my goals..."
                        l "If that's how you want it..."
            else:
                l "I'd like to help..."
                i "Don't worry. I'll find another way to reach my goals..."
    $ fian = "n"
    $ fholly = "n"
    i "Anyways, enough about me. How are you doing, Lena?"
    $ flena = "sad"
    l "Well... It's a difficult moment."
    $ fholly = "sad"
    $ fian = "sad"
    if lena_robert_sex:
        l "I'm getting a lot of hours cut from my work at the restaurant beginning next week."
        i "The one where Perry saw you?"
        l "Yeah... Turns out they want to optimize expenses and are looking for ways to save on salaries."
        l "I could've been fired, but a friend vouched for me and I still get some work..."
    else:
        l "A couple of weeks ago I learned I'm being laid off from the restaurant where I worked at nights..."
        i "The one where Perry saw you?"
        l "Yeah..."
    l "And just yesterday I found out the café isn't doing so well and they'll be forced to shut it down, too..."
    h "Oh, no, that's terrible!"
    i "This place doesn't seem to be doing that badly..."
    l "The owners are getting old and their investment in this business isn't paying off as it should... They are considering selling."
    h "Oh no! That would be so sad...!"
    i "You're right, it's such a shame..."
    $ flena = "n"
    l "Anyways, I don't want to bore you with my problems."
    l "I will survive. I'm already searching for alternatives." 
    $ fian = "smile"
    $ fholly = "n"
    hide holly
    hide holly3
    show holly2 at lef3
    with short
    if v4_axel_date:
        $ flena = "happy"
        l "On a good note, I got my old notebooks back!"
        h "The ones where you wrote your songs?"
        l "Yeah!"
        $ fian = "worried"
        $ fholly = "sad"
        if v3_ian_date:
            i "How did you get them? I thought you said your ex-boyfriend had them..."
        else:
            h "But didn't you say your ex-boyfriend had them?"
        if axel_pictures_watch:
            $ flena = "blush"
        else:
            $ flena = "worried"
        l "Oh, yeah... I saw him on Sunday and he gave them back."
        i "Oh...I see..."
        $ flena = "n"
    l "Anyways, I haven't brought you your coffees yet! I'll be right back!"
    hide lenawork
    with short
    $ fian = "n"
    $ fholly = "n"
    h "Seems like she's having a hard time..."
    i "Yeah... I don't know what I would do if I was in her situation."
    if ian_switch_review or ian_honest_review:
        i "Although mine may be not so different in the near future..."
    $ flena = "smile"
    show lenawork at rig3
    with short
    l "Here you go!"
    i "Thanks."
    "We continued to chat while we drank our coffees. There weren't many customers, so Lena could take the time to participate in our conversation."
    h "It's so sad thinking that this café could end up closing..."
    h "I really love this place, and even if it's just been a few weeks, we've made some good memories here..."
    $ fholly = "blush"
    hide holly2
    show holly3 at lef3
    with short
    h "At least I did..."
    l "They say what's important is the people, not the place. We can still hang out together!"
    h "But coming here has this feeling of routine... It's a cozy place where I know we can meet each other casually..."
    l "If it's a sense of routine you're looking for, why don't we do some activity together?"
    l "I'm already going to my friend's pole dancing lessons on Monday and Wednesday, why don't you join us?"
    h "P-{w=0.3}pole dancing? There's no way I will be able to do that...!"
    l "It takes practice, like all things. But it's fun and good exercise!"
    l "I think it could be good for you. And that way we would do something together every week."
    h "I can't see myself doing it..."
    i "Why not? Give it a try, Holly!"
    l "That's right, if you don't like it you don't have to force yourself to do it. But it's always cool to try new things!"
    h "I haven't exercised since my high school days, but... I guess I can give it a try..."
    "I looked at the time and got up."
    i "Speaking of exercising, it's time for me to go to the gym."
    l "OK! See you, Ian."
    stop music fadeout 2.0
     
## IAN GYM #########################################################################################################################################################################################################
# new text
    scene gym
    with long
    play music "music/jeremys_theme.mp3" loop
    $ fian = "n"
    $ ian_look = 7
    show ian at lef
    with short
    $ fjeremy = "smile"
    $ jeremy_look = 2
    "I got changed and I stepped on the mat."
    show jeremy at rig
    with short
    if jiujitsu > 0:
        j "Hey dude! I see you're not wearing those white pajamas today!"
        j "Are you tired of Jiu Jitsu already?"
        i "Nope. Last time we were just giving it a try. I haven't decided what I'll do yet."
        if alison_jeremy_block:
            "I was still stingy with Jeremy after what he'd said about Alison."
            "Even when I told him I didn't like him trying to get close to her he ignored it..."
            "He was right about her not being my girlfriend or anything, but it still made me feel uncomfortable. He didn't seem to care too much about that, though."
        elif alison_jeremy_doubt:
            "I was still awkward with Jeremy after what he'd said about Alison."
            "He didn't care that I had been sleeping with her, he wanted to try his luck, too..."
            "Granted I had no exclusive relationship with her or anything, but still, it made me feel uncomfortable..."
        show ian at lef3
        show jeremy at rig3
        with move
        show wensmile
        with short
        wen "Buf if you're clever you'll join the team, ha ha."
        yuri "Trying to poach my students, Wen?"
    else:
        j "Hey, you came."
        i "Of course."
        if alison_jeremy_block:
            "I was still stingy with Jeremy after what he'd said about Alison."
            "Even when I told him I didn't like him trying to get close to her he ignored it..."
            "He was right about her not being my girlfriend or anything, but it still made me feel uncomfortable. He didn't seem to care too much about that, though."
        elif alison_jeremy_doubt:
            "I was still awkward with Jeremy after what he'd said about Alison."
            "He didn't care that I had been sleeping with her, he wanted to try his luck, too..."
            "Granted I had no exclusive relationship with her or anything, but still, it made me feel uncomfortable..."
        j "I've been wanting to try a spinning elbow technique I saw the other day... Put your headgear on!"
        show ian at lef3
        show jeremy at rig3
        with move
        show wen
        with short  
        wen "Stop using Ian as a punching bag."
        $ fjeremy = "n"
        j "Oh, I guess you're in charge of the class today too."
        yuri "No, it's in my hands again."
    $ ian_yuri_agenda = True
    $ fjeremy = "happy"
    hide wen
    hide wensmile
    show wen
    show jeremy at centerlef
    show ian at left
    show wen at right
    with move
    show yuri at rig with short
    j "Hey, Yuri! Back from Thaildand already?"
    yuri "Yeah, I just got back a few days ago. Sorry for the long absence, it took longer than usual."
    j "Don't worry, we've been just fine, taking care of business!"
    i "Or rather, Wen has been taking care of us."
    yuri "Yeah, I have to thank you for that."
    wen "Don't mention it. You know I have fun with it."
    "Yuri looked at me."
    yuri "What was your name again?"
    $ fian = "smile"
    i "Ian."
    yuri "That's right, Ian. We haven't worked together that much yet."
    yuri "Let's see what he's taught you. Put on the boxing gloves..."
    wen "Come on Jeremy, you're with me today."
    $ fjeremy = "n"
    j "OK..."
    scene gym
    with long
    "For a moment there I thought he was going to make me spar him, but thankfully that wasn't the case."
    "He put on the pads and tried some drills with me."
    scene v5_pads
    with long
    yuri "OK, let's start with the basics, give me two straight jabs."
    play sound "sfx/punchgym.mp3"
    yuri "Alright, now add a cross!"
    if kickboxing > 0:
        play sound "sfx/punch.mp3"
        with vpunch
        yuri "Good!"
        "He drilled me through several basic combos for a while. I was managing to follow along pretty consistently."
        yuri "Now let's add some kicks!"
        scene v5_pads2
        "He changed the way he held the mitts and began asking for different kicks."
        yuri "Front kick! Roundhouse to the body! Now high!"
        if kickboxing > 1:
            play sound "sfx/strongpunch.mp3"
            with vpunch
            yuri "Nice kicks!"
            yuri "Now let's add them to the combos!"
            yuri "Left hook, cross, roundhouse to the body!"
            play sound "sfx/punch.mp3"
            with vpunch
            yuri "Again!"
            $ ian_athletics_xp += 1
            play sound "sfx/xp.mp3"
            show athletics_up
            call screen skillsup
        else:
            play sound "sfx/punchgym.mp3"
            "My kicks didn't land with too much power or I failed to maintain balance while throwing them."
            yuri "Mhh, your kicks lack a bit of finesse. We'll have to work on those."
            yuri "OK, try again. Left hook, cross, roundhouse to the body!"
    else:
        "I did what he asked but I missed the punch."
        yuri "Straighten your arm, drive with your shoulder. Try again!"
        yuri "Double jab, cross!"
        "I did it again, this time with only slightly better results."
        "I tried a few combos as Yuri ran me through the basics."
        "The results where rather... Underwhelming."
        scene gym
        show ian at lef
        show yuri at rig
        with short
        yuri "Well... You still have to work on your basics."
        yuri "Work a lot."
        i "I know, I know."
        scene v5_pads
        with long
        yuri "Ok, let's start from the beginning again!"
        play sound "sfx/punchgym.mp3"
        yuri "Jab, jab, cross!"
        
    "Yuri kept working with me during most of the class."
    "I had begun sharp, but this was way more tiresome than I had expected!"
    "After ten minutes I was sweating and panting heavily, and after twenty I was ready to call it quits."
    "I didn't know how I managed to do thirty minutes of that, but somehow I did."
    $ ian_athletics_xp += 1
    play sound "sfx/xp.mp3"
    show athletics_up
    call screen skillsup
    scene gym
    $ fian = "disgusted"
    show ian at lef
    show yurismile at rig
    with long
    "Needless to say, at the end I was fucking exhausted. I needed a few minutes to get back up from lying on the floor."
    i "Whew! That was killer!"
    yuri "Like all good training sessions are!"
    yuri "You have nice technique, but you have to learn not to tense up so much, and to breathe with the strikes."
    i "Also a bit more cardio wouldn't hurt..."
    yuri "That never does!"
    $ fian = "n"
    $ fjeremy = "smile"
    show yuri at rig
    show ian at left
    with move
    show jeremy at centerlef
    show wen at right
    with short       
    j "I see he put you through the grinder!"
    i "I barely made it."
    if kickboxing > 1:
        w "Well, I'd say you did pretty well!"
        yuri "He moves rather well, yeah."
        j "See? I make for a great coach, too."
        i "I'd say Wen helped more than a bit, too."
        yuri "That sounds more believable, ha ha."
    elif kickboxing > 0:
        w "You didn't do too bad."
        yuri "You can get decent at this if you train a bit more."
        i "I hope so."
        yuri "Let's keep working on the basics for a time."
    else:
        w "How did he do?"
        yuri "Like a newbie."
        i "Damn."
        yuri "Don't worry, I wasn't expecting more. To be honest, I was positively surprised."
        yuri "You don't have bad attributes, you can get decent at this with proper training."
        i "I hope so."
        yuri "Let's keep working on the basics for a time."
    j "With Yuri, you're gonna learn from the best! What was your professional record?"
    yuri "Twenty-three fights, nineteen wins and twelve knockouts."
    i "Damn, that's impressive."
    yuri "That was a few years ago, though. Now I'm just a humble coach."
    wen "You could still beat a lot of fighters in the professional scene."
    yuri "Maybe, but I'm done with that. Too much sacrifice, and I'm getting old!"
    yuri "Anyways, are you two training Ian for the interclub tournament?"
    i "A tournament?"
    wen "Oh, yeah... I'm not sure you're ready, so I didn't say anything yet."
    wen "Starting next month several gyms in the city are hosting an amateur MMA tournament."
    $ fjeremy = "happy"
    j "That sounds awesome!"
    i "What's the tournament like?"
    yuri "You fight once a month against someone on your weight class from a different gym. You fight in a bracket, so even if you lose a fight you can make it to the top three if you win the other ones."
    yuri " There's a small money prize for the winner and finalists."
    j "Nice, you can even get paid! I'm in!"
    yuri "There's an entry fee, too, but it's not much."
    j "Whatever, sign me in! What about you, Ian? Are you in?"
    menu:
        "Sounds interesting":
            $ renpy.block_rollback()
            $ tournament = True
            $ fian = "smile"
            i "It sounds interesting, yeah..."
            i "But I'm not sure I'm skilled enough to enter."
            yuri "It's an amateur tournament, so don't worry. Most importantly, it makes for a good way to rack up some real experience."
            i "I like the idea, but Wen said he's not sure I'm ready..."
            if kickboxing > 1:
                wen "Your striking is pretty good for an amateur, so maybe you'll do OK."
                if jiujitsu > 1:
                    wen "And you seem to be learning Jiu Jitsu fast, so that's a plus!"
                elif jiujitsu > 0:
                    wen "And I can teach you some Jiu Jitsu, too."
                else:
                    wen "Your grappling skills is what worries me..."
            elif kickboxing > 0:
                wen "You should be able to sharpen your striking with some more training."
                if jiujitsu > 1:
                    wen "And you seem to be learning Jiu Jitsu fast, so that's a plus!"
                elif jiujitsu > 0:
                    wen "And I can teach you some Jiu Jitsu, too."
                else:
                    wen "Your grappling skills is what worries me..."
            else:
                wen "Let's just say your striking is a bit lacking... You should really put some effort into it."
                if jiujitsu > 1:
                    wen "Your Jiu Jitsu game could become pretty good rather fast, though!"
                elif jiujitsu > 0:
                    wen "And I can teach you some Jiu Jitsu, too. You'll need it."
                else:
                    wen "Your grappling skills is also really weak..."
            yuri "There's still some time to prepare yourself. If you're really willing to enter the tournament, train hard these following weeks."
              
        "I'll pass":
            $ renpy.block_rollback()
            i "Nah, it's not for me. I'll pass."
            $ fjeremy = "sad"
            j "Really? Come on, man."
            yuri "You have to train hard for this tournament. It might be amateur, but it's no joke. You could get hurt."
            i "Exactly. Getting hurt is very low on my list os priorities, so not for me."
            i "I'm just doing this as a hobby."
            yuri "That's good too." 
            $ fjeremy = "smile"
    
    if jiujitsu> 0:
        j "But what are you going to stick with, Ian? Kick boxing or Jiu Jitsu?"
        yuri "Both aspects are equally important, but since you're not devoting a hundred percent of your time to training, you should focus on one."
        i "Yeah, I have a life outside of the gym..."
        i "I'll think about it."
    yuri "We're done for today. See you next week, guys."
    
    stop music fadeout 2.0
    scene streetnight
    with long
    $ fian = "n"
    $ ian_look = 1
    $ jeremy_look = 3
    show ian at lef
    show jeremy at rig
    with short
    "We took a shower and left the gym."
    i "I thought last time was bad, but I'm dead tired today too..."
    j "Sleep it off tomorrow."
    if v4_ian_date:
        i "I can't. I have a nine-to-five job, unlike you... Besides, I have a date with Len, too."
        j "Nice! Will you finally bang her?"
        i "That's not my goal..."
        j "Don't lie to me, man, or to yourself."
        $ fian = "blush"
        i "I mean, of course I'd like to... I meant it's not my short-term goal."
        j "Short-term, long-term... The only difference is how long it takes you to get there."
    else:
        i "I can't. I have a nine-to-five job, unlike you..."
        i "But I'll be sitting in front of a computer all day, so at least I have that going for me."
        j "You don't have any plans? You could ask Lena to meet..."
        if v2_ian_date == False:
            i "I haven't really hung out with her yet..."
            if v3_ian_date:
                i "I mean, I met her and Holly, but I never really asked for a date, just the two of us..."
            j "Then it's about time you did it! Girls don't like to wait for too long."
            j "If she thinks you're not interested your window of opportunity will close."
        else:
            $ fian = "sad"
            i "I asked her already, but she said she was too busy... That she's having a tough time lately and now's not the best moment..."
            $ fjeremy = "n"
            j "Damn, dude... That sounds like she's politely telling you that she's not interested."
            i "That's my feeling as well... But I guess we can still be friends."
            $ fjeremy = "smile"
            j "Yeah, keep her close and who knows, maybe when the time is actually right you'll get to score with her!"        
    $ fian = "n"
    if louise_jeremy == False:
        i "What about you? How are things with your \"girlfriend\"?"
        $ fjeremy = "flirt"
        j "We've straightened things out. I met her the other day and she was still stingy, but she got over it after I gave her a good dicking."
        j "In the end, as long as you keep them happy girls won't give you too much trouble."
    else:
        i "Are things with your \"girlfriend\" still OK?"
        j "Yeah, seems like Lena has decided to keep quiet about me and Ivy. I should thank her."
        i "You're lucky beyond what you deserve."
        j "Don't hate me, ha ha."
    if alison_jeremy_block or alison_jeremy_doubt:
        i "Speaking of that, about Alison..."
        $ fjeremy = "smile"
        j "Come on, man, don't be like that... You can't get mad at me for wanting to score with her."
        j "She's not anyone's property."
        i "I'm not saying she is. Just that there are some boundaries."
        j "I think so too, but they're not in play now. She's not your girlfriend, so..."
        i "Still, can't you understand why it makes me uncomfortable?"
        $ fjeremy = "n"
        j "I can, but I don't want to be rude, man..."
        i "What do you mean?"
        j "It makes you uncomfortable because you're insecure... But I'm not trying to steal anything away from you."
        j "Bros before hoes. She shouldn't be something that gets in between us. If you want to enjoy her, go ahead! I'm happy for you, honest."
        j "But don't get mad with me for wanting the same as you do..."
        $ fjeremy = "smile"
        j "And man, as I said, if she's more than a fuck buddy for you, you should ask her out. Make her your girlfriend."
        i "She said she's not looking for a serious relationship."
        j "Then don't think of your relationship with her as serious! Carpe diem, my man."
        j "We should enjoy these things together, not get jealous and shit! I need to take you out partying, so we can score with some bitches!"
        "Jeremy had a very clear outlook on things. I wasn't gonna change his mind..."
    elif alison_jeremy:
        j "I'm keeping Alison happy, too, it seems... She wants to hang out with me soon."
        if alison_voyeur:
            j "Did you like the picture I sent you?"
            $ fian = "blush"
            i "I'm amazed she let you take it..."
            j "I'll try and convince her to take more. I'll show you if she lets me."
            i "OK, ha ha..."
    $ fjeremy = "smile"
    $ fian = "n"
    i "Anyways, I'll be on my way home. All I want is to eat something and go to bed..."
    j "See you, man!"    
    
    if v2_ian_date == False and v4_ian_date == False:
        hide jeremy
        with short
        show ian at truecenter
        with move
        "As I walked back home I thought about what Jeremy had said regarding Lena."
        "If I wanted to get closer to her I had to make a move before it was too late."
        "I had been postponing it and now I felt it could be my last chance..."
        menu:
            "{image=icon_friend.png}Ask Lena for a date" if ian_lena > 4:
                $ renpy.block_rollback()
                i "I will do it. I will text her..."
                if v3_ian_date:
                    i "{i}Hey Lena, what's up? I had a lot of fun last Wednesday.{/i}"
                    i "{i}I was wondering if you'd like to meet again this week, just the two of us.{/i}"
                else:
                    i "{i}Hey Lena, what's up? It was nice chatting with you at the café today.{/i}"
                    i "{i}I was wondering if you'd like to hang out someday, just the two of us.{/i}"
                "It was pretty straightforward, but I had to be at this point..."
                "Her response arrived before I got home."
                play sound "sfx/sms.mp3"
                if lena_go_ian > 0:
                    $ v4_ian_date = True
                    l "{i}Hey! Sure, I'd like that {image=emoji_smile.png}{/i}"
                    $ fian = "smile"
                    l "{i}I'm free tomorrow night, is that OK with you?{/i}"
                    i "{i}Sure! We can go grab a beer or something.{/i}"
                    l "{i}Cool! Sounds like a plan. See you tomorrow!{/i}"
                    i "Nice! She agreed!"
                    i "Maybe I had a chance after all..."
                else:
                    l "{i}Hey, Ian. Sorry, but I'm really busy this week.{/i}"
                    l "{i}There's been a lot of changes in my life and it's not really a good time right now...{/i}"
                    $ fian = "worried"
                    i "{i}I see. Don't worry then. I'll see you at the café.{/i}"
                    l "{i}Sure!{/i}"
                    i "Damn... That was a polite way of rejecting me."
                    i "I should've known... Fuck."
                    i "Well, at least I tried..."
                    
            "Forget it":
                $ renpy.block_rollback()
                i "Nah... It's not worth the trouble."
                i "She's probably not interested and I'd prefer to save us the trouble and uncomfortable situation."
                i "She's out of my league, anyways... Better to just keep things friendly."



## CALL DAD ######################################################################################################################################################################################################
     
    scene ianroomnight
    with long
    $ fian = "n"
    $ ian_look = 2
    show ian 
    with short
    "After cooking something simple for dinner I went to my room and collapsed on the bed."
    i "Man, I'm beat... I'll go to sleep early, today."
    if ian_switch_review or ian_honest_review:
        "I was a bit anxious and I couldn't relax, though. I had money problems to solve..."
    play sound "sfx/ring.mp3"
    "I was considering just that when when my phone rang."
    $ fian = "worried"
    i "Damn, it's Dad..."
    hide ian
    show ian_phone
    show phone_iandad at lef3
    with short
    i "Hi, Dad."
    ld "Hello, son. How are you doing?"
    i "I'm fine, same as ever, you know..."
    ld "We haven't heard from you in quite some time, so I thought to ask."
    "It had been weeks since I spoke to my parents, probably two months. I hadn't called, but neither had them."
    i "No news is good news, right?"
    ld "So says your mother, but I thought I'd check up on you. Are you receiving our stipend regularly?"
    i "Yeah, I get the money each month. Thanks, Dad."
    ld "And I take it you're still working at that magazine?"
    i "Yes."
    ld "Any progress on that? Have you managed to climb the corporate ladder, even if it's only one step?"
    "Again with that climbing the ladder thing..."
    if ian_switch_review or ian_honest_review:
        "He had a point, though. Instead of climbing the ladder I was one step closer to being fired."
        "Minerva wanted me out of that office and my salary had been cut in half. What a way to progress..."
        "Right now my financial problems were very real and the only feasible way to solve them was to ask Dad to send me more money..."
        "Either that or ask Perry to hold off my rent and promise him to pay the money once I made a break."
        "A break I wasn't sure would ever come..."
        menu:
            "{image=icon_money.png}Ask Dad for more money":
                $ renpy.block_rollback()
                $ ian_stipend = 2
                $ fian = "sad"
                i "Actually... There's been a problem with my contract and I'm getting less working hours."
                ld "And less pay."
                i "Yeah... I earned enough to cover for most expenses, but now I'm in a difficult position."
                i "I need some extra money and I don't have a way to earn it quickly, so..."
                i "Could you send me a bit more money at the end of the month?"
                "I hear him sigh."
                ld "OK, Ian. But this situation can't go on much longer."
                
            "Don't mention it":
                $ renpy.block_rollback()
                $ fian = "serious"
                "I couldn't ask Dad for money, though. I wouldn't."
                "I was a grown man and I could solve my own problems."
                "I had to."
                ld "Ian, are you still there?"
                i "Yeah, yeah."
    else:
        i "Everything's the same."
        ld "That's not good. You're going to be twenty-eight this month, sufficient age to have figured things out and start to settle."
        i "I'm doing everything I can."
        "That was never enough for him, though. I knew that very well."
    ld "You know, it's still not too late to re-configure things. You can still get a productive career. We'll support you financially while you're studying."
    $ fian = "serious"
    i "I've already chosen my career. You know I won't be happy becoming a lawyer or an engineer..."
    ld "You'd do even better as an architect at this point."
    i "That's not what I want."
    ld "Yeah, I know, you want to be happy. But are you happy with your situation right now?"
    if ian_switch_review or ian_honest_review:
        ld "I'd say it's obvious that you're not."
    i "I'm happier than I would be following the paths you want me to follow."
    ld "I don't believe that. I know you're a clever boy, Ian. You're my son, after all."
    ld "I see so much wasted potential. If you only had a bigger will to push hard..."
    i "Me not getting the results you want doesn't mean I'm not working hard."
    ld "Then work smarter. More efficiently."
    i "Life's not all about efficiency. Art is not all about efficiency."
    ld "We won't ever see eye to eye on this, will we?"
    ld "You can do whatever you want, Ian. But you should stop needing your parents' financial support at some point."
    ld "I'm just trying to push you in that direction."
    if ian_stipend == 2:
        ld "Instead, you're asking me to increase your stipend... You can see why I'm worried."
        $ fian = "worried"
        "Fuck... He knew how to make me feel humiliated and ashamed of myself. He was right, though..."
    else:
        i "You don't have to keep sending me money if that's a problem."
        ld "Money's not the problem. Your life's situation is."
        $ fian = "worried"
        "Fuck... Again with that. He knew how to make me feel humiliated and ashamed of myself."
    i "Anyways... How's Mom?"
    ld "She's fine. You know her, she keeps herself busy with her hobbies, her travels and her friends."
    i "Good to know."
    i "Well, nice talking to you, Dad. I'm going to bed now."
    ld "Good night, son."
    hide phone_iandad
    hide ian_phone
    show ian
    with short
    $ fian = "serious"
    i "Talk to you again in two months."
    if ian_switch_review and ian_stipend == 1 or ian_honest_review and ian_stipend == 1:
        $ fian = "n"
        "At least I had the dignity not to ask Dad for extra money at the end of the month."
        "He had a sorry image of his son, and that would've only served to make it even worse."
        "I wouldn't give him more reasons to patronize me."
        call screen willup
    elif ian_stipend == 2:
        $ fian = "sad"
        "I had to ask Dad for more money, though... Even if it felt humiliating and I gave him even more reasons to patronize me."
        "I had to make a break at some point, show my family they were wrong about me..."
    else:
        $ fian = "sad"
        "He always found a way to patronize me. I wish I could make him see he was wrong about me."
    "I had to find a way to achieve my goals."
    if v4_ian_date:
        jump v4ianlenadate
    else:
        jump v4lenawednesday
        
##IAN LENA DATE findme ############################################################################################################################################################################################################ 
     
label v4ianlenadate:
     
    $ v4ld_1 = False
    $ v4ld_2 = False
    $ v4ld_3 = False
    $ v4ld_4 = False
    $ day = "Wednesday"
    scene blackbg
    with long
    call screen calendar
    scene ianroom
    with long
    $ ian_look = 2
    $ fian = "n"
    show ian
    with short
    "I arrived home after my work at the magazine was done."
    "I had been wishing for it to be over: meeting Lena was the only thing I really wanted to do today."
    "I had to prepare for the date. We were meeting for drinks after dinner, and I hadn't decided where to take her yet..."
    "Only two reasonable ideas popped up in my head. I could take her to the Fortress, the bar where me and my friends always met."
    "Or I could take her to that cocktail place, Shine."
    i "I wonder what's best for tonight's date... What will she like most?"
    i "And where will I feel more comfortable...?"
    menu:
        "Take Lena to the Fortress":
            $ renpy.block_rollback()
            $ fian = "smile"
            $ v4_place = "fortress"
            i "I will take her to the Fortress."
            i "I know the place and I think we can have fun there."
            if lena_metal > 1:
                i "She said she liked rock music, even heavy metal, so she'll like the place."
            else:
                i "She said she liked rock music, after all. Even if metal's not her thing."
            
        "Take Lena to Shine":
            $ renpy.block_rollback()
            $ fian = "smile"
            $ v4_place = "shine"
            i "I will take her to the Shine."
            i "It's the most appropriate place for a date with a girl."
            i "She will probably like the cocktails and music."
            
    i "I'll text Lena to tell her where we'll be meeting."
    play sound "sfx/sms.mp3"
    i "There, done."
    i "I'll entertain myself before the date..."
    scene ianroomnight
    with long
    $ fian = "n"
    $ ian_look = 3
    "I cooked some dinner and I got myself ready."
    show ian
    with short
    "I was more nervous than I expected."
    if v2_ian_date:
        "It wasn't the first time Lena and I went on a date, but this time it felt different."
        "It felt more serious. Like this one was The Date."
    else:
        "It wouldn't be the first time hanging out with Lena, but it did feel like the first date."
        "A real date."
    "Should I go for it? Take the step to be more than just friends?"
    if v2_kiss:
        "We had already taken that step before, when we kissed at the record store, right?"
        i "Well, kinda..."
        "That step had not really yet been claimed. More than a week had gone by since that kiss and nothing in our relationship had changed."
        i "That step still needed to be fully taken."
    else:
        "I wasn't sure that was what Lena wanted..."
        "She was really nice to me, but so she was to everybody else. Holly and her bosses loved her for a reason..."
        "I could very well be mistaken in my interpretations of her feelings towards me..."
        i "I guess there's only one way to really find out..."
    
    if v4_place == "fortress":
        $ lena_look = 4
        scene street2night
    else:
        $ lena_look = 3
        scene streetnight
    with long
    "I waited for Lena in front of the bar at the agreed-upon hour."
    show ian 
    with short
    if v2_ian_date:
        i "Good, I'm on time, just like last time."
        if v2_robert_bj:
            "Lena had been late on our last date... But that night she showed up on time."
        else:
            "She arrived just a minute later."
    else:
        i "Good, I'm on time."
        "She arrived just a minute later."
    show ian at lef
    with move
    $ fian = "happy"
    $ flena = "smile"
    show lena at rig
    with short
    if v2_ian_date:
        if v2_robert_bj:
            l "Dammit, you beat me to it! I wanted to be first this time since I made you wait the other day."
            i "Don't worry, I arrived just a second ago."
        else:
            l "Dammit, you beat me to it again! You sure are punctual!"
            i "Only when the situation requires it, ha ha."
    else:
        l "Oh, you beat me to it. You sure are punctual!"
        i "Only when the situation requires it, ha ha."
    if v4_place == "fortress":
        "I looked at her. She was stunning in those short jeans and sneakers."
        "Casual, cute and sexy."
    else:
        "I looked at her. She was stunning in that skirt and black heels."
        "Fashionable, elegant and sexy."
    menu:
        "Say hello":
            $ renpy.block_rollback()
            $ fian = "smile"
            i "Hello, by the way."
            "She smiled."
            l "Hi."
            
        "Compliment": 
            $ renpy.block_rollback()
            i "You're looking stunning, Lena."
            $ flena = "shy"
            l "Oh, thank you for your bold compliment."
            $ fian = "smile"
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            i "It's not bold at all. Just stating the obvious."
            $ flena = "smile"
            l "Glad to know you see me with such favorable eyes."
                                                
        "Joke":
            $ renpy.block_rollback()
            i "Who are you and what have you done with the girl who brings me coffee?"
            $ flena = "happy"
            l "She said she couldn't come and sent someone who would look the part tonight."
            i "You surely do look the part... Tell her that she should've warned me so I could have sent someone of equal standing."
            i "I'm afraid I look like a fool next to this beauty."
            $ flena = "shy"
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            l "Ha ha ha, if you were trying to break the ice you surely managed to do it." 
            $ fian = "smile"
            i "Off to a good start, then."
            $ flena = "smile"
         
        "Whistle":
            $ renpy.block_rollback()
            play sound "sfx/whistle.mp3"
            $ fian = "confident"
            "I looked at her while looking at her from head to toe."
            $ flena = "shy"
            $ fian = "smile"
            i "Wow, you're looking stunning, Lena."
            l "Wow, what am I supposed to answer to that?"
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            i "Nothing, take it for what it is: a very honest compliment."
            $ flena = "smile"
            l "Thanks, ha ha. You're not looking bad either..."
    
    l "Shall we go in?"
    if ian_charisma > 1:
        i "Sure. Ladies first."
    else:
        i "Sure..."
    if v4_place == "fortress":
        play music "music/rock_bar.mp3" loop
        scene rockbar
    else:
        play music "music/nice_place.mp3" loop
        scene cocktailbar
    with long 
    show lena at rig
    show ian at lef
    with short
    
    if v4_place == "fortress":
        l "So this is the rock bar you told me about..."
        i "Yes. I know it's not much to look at, but me and my friends have been coming here for quite a few years."
        i "I wanted to share that with you."
        play sound "sfx/xp.mp3"
        show wits_up
        $ ian_wits_xp += 1
        call screen skillsup
        if lena_posh > 1:
            $ flena = "worried"
            l "Yeah, it's uh... very peculiar."
            l "Reminds me of the places where I used to go when I was like sixteen."
            if ian_lena > 2:
                play sound "sfx/frienddown.mp3"
                show friend_down
                $ ian_lena -= 1
            i "Uh... Let's get something to drink. I hope you like beer."
            l "I can do with it."
        else:
            l "I see... That's cool!"
            l "I like the place, it looks really authentic! Not many places like this left..."
            if lena_posh == 0 and ian_lena < 10:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_lena += 1
            i "Sadly not. Let's get some beer."
            l "OK!"
        
    else:
        i "Here we are. I hope you're in the mood for a cocktail!"
        l "I've been needing one, in fact!"
        play sound "sfx/xp.mp3"
        show charisma_up
        $ ian_charisma_xp += 1
        call screen skillsup
        i "Did you know this place?"
        if v2_robert_date:
            l "I came here before once, with a colleague from work."
            l "Other than that, I haven't been going out much lately..."
        else:
            l "Nope, my first time here..."
            l "I haven't been going out much lately."
        if lena_posh > 1:
            l "But I really like the place! It's right up my alley."
            if ian_lena < 10:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_lena += 1
            i "I'm glad to hear that!"
            
        if lena_posh == 0 :
            $ flena = "n"
            l "This place looks a bit too fancy for my wallet, though..."
            if ian_lena > 2:
                play sound "sfx/frienddown.mp3"
                show friend_down
                $ ian_lena -= 1
            $ fian = "n"
            i "Oh, no, it's not that expensive..."
            l "Probably not! It just looks more fancy than what I'm used to."
            
    $ fian = "smile"
    $ flena = "n"
    "We grabbed a couple of drinks at the bar and took a seat."
    "The lighting was dim enough to be intimate and music played in the background."
    i "So, finally we find a moment to hang out together."
    l "Yeah... These last couple of weeks have been pretty chaotic for me. And the coming ones promise to be the same way..."
    $ fian = "n"
    i "I'm sorry you're going through so much with your jobs right now."
    l "It is what it is, you shouldn't be sorry. As I said, I will survive."
    l "Besides, you don't have it exactly easy at your job, either!"
    $ fian = "smile"
    i "Another thing we share, then."
    l "But yeah, you're right. It's good that we finally pick a date to meet!"
    l "Seems like lately we've only been stumbling across each other!"
    i "That happened a surprising amount of times. I'm not counting the café, since everybody has to meet somewhere for the first time..."
    i "But also the art gallery and outside the gym!"
    l "Yeah, and turns out your friend is my flat-mate's so-called boyfriend. And I also met Perry at the restaurant!"
    i "I know, he told me..."
    menu v4lenadate1:
        "Talk about Jeremy" if v4ld_1 == False:
            $ renpy.block_rollback()
            $ v4ld_1 = True
            $ fian = "n"
            i "I'm sorry that Jeremy caused so much trouble."
            l "That's another thing you shouldn't be sorry about. It's not your fault!"
            $ fian = "smile"
            i "Sometimes you just feel you have to take some responsibility for your friends' screw-ups."
            i "He's not a bad guy, but he's..."
            l "A meat head?"
            i "Yeah, I guess that sums it up pretty well, ha ha."            
            if louise_jeremy:
                $ flena = "sad"
                l "I haven't told Louise about what he did with Ivy since I don't want to cause her trouble..."
                l "But you should tell your friend to come clean or start behaving from now on."
            else:
                $ flena = "serious"
                l "There's nothing wrong about that, but he outright lied to Louise's face."
                $ fian = "sad"
                l "I told her what he did with Ivy and he denied everything until Louise accepted it."
                i "Hard to defend him on that."
                l "If he's not willing to come clean at least he should start behaving from now on. You should tell him that."
            $ flena = "n"
            l "That's as much responsibility as you should bear."
            $ fian = "smile"
            i "I will."
            jump v4lenadate1
                
        "Talk about Perry" if v4ld_2 == False:
            $ renpy.block_rollback()
            $ v4ld_2 = True
            $ flena = "smile"
            l "So, your flatmate is the son of Mayor Vermeer, huh? You have friends in high places..."
            i "My relationship with Perry is hardly political, believe me."
            i "He hates the topic and doesn't even want it discussed around him."
            $ flena = "n"
            l "Really? How unbecoming of the Mayor's son."
            $ fian = "n"
            i "Oh, and if you meet him, try not to call him that."
            l "Noted. I guess his relationship with his father is not that good?"
            i "I wouldn't say it's bad, but I guess Perry's parents aren't too fond of his general disinterest."
            l "He's not working or studying?"
            i "Nope, not right now."
            l "I guess he can afford not to, having a well-positioned father."
            $ fian = "smile"
            i "He doesn't live in luxury, I can assure you. I live with him."
            jump v4lenadate1
            
        "Talk about Ivy" if v4ld_3 == False:
            $ renpy.block_rollback()
            $ v4ld_3 = True
            i "I'm curious, are you and Ivy close friends?"
            l "Yes, I'd say she's my closest friend. The one I've known the longest, at least."
            l "We were classmates during high school and we've been friends ever since, even if we don't see each other as much as we used to."
            i "I see..."
            l "Why were you curious about it?"
            i "I had the impression you two were very different. Opposites don't tend to mix well."
            l "We're not opposites, but I guess it's true we're quite different. But I don't judge people on their life-style or stuff like that."
            l "All I care about is if they are good people, and Ivy is. Though she can be a bit chaotic and brash sometimes!"
            i "You two are an interesting duo, no doubt."
            jump v4lenadate1
            
        "Comment on Lena's new piercing" if lena_piercing1 and v4ld_4 == False or lena_piercing2 and v4ld_4 == False:
            $ renpy.block_rollback()
            $ v4ld_4 = True
            i "That navel piercing is new, right? I hadn't seen it before..."
            l "Yes, it is. I had it done just the other day. Do you like it?"
            $ fian = "shy"
            i "Navel piercings are always sexy..."
            l "I'll take that as a yes."
            $ fian = "smile"
            i "It is, ha ha. It looks great on you, but I guess anything would."
            l "Even a mohawk?"
            $ fian = "happy"
            i "I would need to see it to be sure, but... Maybe you should give it a try, ha ha!"
            $ flena = "happy"
            l "I think I'll stick with the piercing for now!"
            $ fian = "smile"
            $ flena = "smile"
            jump v4lenadate1
        
        "Do you believe in destiny?":
            $ renpy.block_rollback()
            i "Tell me something... Do you believe in destiny?"
            $ flena = "happy"
            l "Wow, that question came out of the blue. I wasn't expecting to discuss such things tonight!"
            i "Sorry about that, ha ha."
            i "I just thought about it since we've been stumbling across each other and experiencing so many coincidences..."
            $ flena = "smile"
            l "It's a small world, isn't it? It surprised me too, but it's kind of funny."
            l "I don't know if such a thing as destiny exists, if everything that happens to us is already determined beforehand..."
            l "I like to think that it's our choices that take us where we find ourselves at."
            i "I like to think that, too. But there's just so many things that escape our control..." 
            i "And they say coincidences don't exist."
            l "So you think your choices aren't yours?"
            $ fian = "n"
            i "I sure hope they are! Though sometimes it feels life would be easier if someone else chose for you..."
            $ flena = "n"
            l "I know that feeling... The anxiety of not knowing if you're making the right choice or a mistake..."
            l "But even if your choices are your own or not, a decision's being made. That's all we can be sure about!"
            $ fian = "smile"
            i "Then let's keep our fingers crossed and hope that the right decisions are made."
            
    if v4_place == "fortress":
        i "And speaking about decisions... How about we play a game of pool?"
        $ flena = "smile"
        l "I've only played once in my life, and I was pretty awful at it!"
        i "Don't worry, I'm pretty bad at it, too..."
        if v1_poolwadewin and v3_pool_win or v1_poolcindywin and v3_pool_win:
            i "Though lately it seems I'm getting the hang of it. I've won my two last games!"
            l "You're gonna destroy me in that case!"
        elif v1_poolwadewin or v1_poolcindywin or v3_pool_win:
            i "I'm still getting the hang of it. I've won some and lost some."
            l "Then this'll be another victory for you!"
        else:
            i "I've lost all the games I ever played."
            l "Well, in that case I don't feel so outclassed!"
        i "Winning or losing is not the point. Just having fun."
        l "I can get behind that. But you need to teach me!"
        i "No problem."
        scene v4_lenadate1
        with long
        "We got up and moved to the pool table."
        "After I set everything up I gave a cue to Lena."
        i "Are you familiar with the rules?"
        l "I forgot most of it. I know you have to hit the white ball..."
        "I refreshed her memory and gave her a few tips on how to strike the ball."
        if ian_athletics > 1:
            "Her first shots weren't very successful. I sank three balls and she hadn't scored a single one yet."
        else:
            "Her first shots weren't very successful. Mine weren't that good either, but I managed to sink two balls before she could score a single one."
        l "Ahh, you're chewing me up! That's not fair."
        i "Wait, let me help you..."
        "I got behind Lena and placed one hand on her hip and the other one on her arm, guiding her position."
        i "There, keep your hand steady and drive your arm forward in a straight line... Try not to hit the ball too low or you'll send the ball flying."
        "I felt Lena's warmth on my chest. My fingers touched the soft skin of her hand, and her sweet scent almost overwhelmed me."
        "Being like this with her was so nice..."
        play sound "sfx/cue.mp3"
        with vpunch
        "Lena followed my advice and managed to sink her first ball."
        l "It worked! Thank, you, Ian!"
        play sound "sfx/xp.mp3"
        show athletics_up
        $ ian_athletics_xp += 1
        call screen skillsup
        if v2_ian_date:
            "She turned to thank me. She was so close to me, her bright blue eyes right in front of mine, just like that day at the record store..."
        else:
            "She turned to thank me. She was so close to me, her bright blue eyes right in front of mine... It was the first time she was so close to me."
        "My hand still rested on her hip. All I had to do was pull her closer, just a few centimeters, and kiss her..."
        "I moved forward just a bit, still undecided, but about to take the step..."
        $ flena = "sad"
        $ fian = "worried"
        scene rockbar
        show ian at lef
        show lena2 at rig
        with long
        "But she took a step backwards."
        $ flena = "n"
        "She handed me the cue."
        l "It's your turn."
        $ fian = "n"
        i "Sure..."
        play sound "sfx/cue.mp3"
        "We continued to play, but her reaction when I tried to get close jarred me."
        "Had I done something wrong? Was she uncomfortable? I had been having the opposite impression..."
        if v2_lena_kiss:
            "And it had been her who had kissed me last time! Why would she be hesitant now?"
            "Maybe I was imagining things?"
        elif v2_ian_kiss:
            "I had already kissed her once, and she had seemed OK with it. Why hesitate now?"
            "Had she changed her mind? Or maybe I was just imagining things?"
        elif v2_almost_kiss:
            "We had almost kissed at our last date. I had had the impression she had wanted it, or had been waiting for it to happen at least."
            "I couldn't be sure, but I was pretty certain she had just avoided me. Maybe she saw me just as a friend?"
        else:
            "Maybe she never intended for anything to happen between us, seeing me just as a friend."
            "I couldn't be sure, but I was pretty certain she had just avoided me. And I couldn't really pinpoint the reason."
        "We finished the game and left the table to grab another beer."
        $ flena = "smile"
        l "You beat me, just as expected."
        $ fian = "smile"
        i "You didn't do that badly..."
        l "Don't patronize me! I'm horrible at this."
        i "You'll need to take a few more classes, yeah, ha ha."
        l "It was fun, though. Thanks for showing me this place. It's like you're showing me a part of yourself..."
        i "And what do you think about it?"
        l "I think it suits you! It's very underground and alternative."
        i "So that's how you see me? Underground and alternative... Ha ha."
        l "Well, you don't seem to be the kind of guy who likes mainstream things too much."
        l "I guess that's why you're a writer. That's pretty alternative in itself."
        $ fian = "n"
        i "Sadly... But I guess only people who are not comfortable in the mainstream search for the alternative."
        i "If you've never suffered a day in your life you won't find any need to deviate from the mainstream."
        l "So you think having it hard is necessary to break free from mainstream culture?"
        $ fian = "smile"
        i "Don't quote me on that, but alternative people tend to be quite edgy, ha ha."
        $ flena = "flirt"
        l "Really? I still have to see that edge of yours, I guess."
        
    else:
        l "How about we dance? Feeling like it would be a good decision?"
        i "I might accidentally stomp on your toes, but other than that it seems a pretty good choice."
        $ flena = "happy"
        l "It's a risk I'm willing to take!"
        scene v4_lenadate2
        with long
        "Lena took my hand and took me to the dance floor."
        "The music wasn't too loud and only a few people were dancing, which made me feel quite exposed..."
        if ian_charisma > 1:
            "Thankfully I had been learning to be less self-conscious and let go a bit."
        else:
            "I always felt so self-conscious when I had to dance..."
        i "I'm not very good at this... You'll need to teach me a bit!"
        l "No problem! Let me guide you."
        "Lena held my hands while dancing on the spot. I couldn't avoid to shiver slightly at the touch of her soft skin."
        "I began following her steps. They were simple enough."
        "When she saw I had synced to her rhythm she added some more flair to her moves, letting herself go with the music."
        "Her red skirt fluttered around her long legs with each step, following the movements of her hips."
        if v3_cindy_dance:
            "She danced so effortlessly, much like Cindy... They both seemed to have a natural ability to move to the rhythm."
        else:
            "She danced so effortlessly, having a natural ability to move to the rhythm."
            "Her black hair flowed with her movements as she smiled at me and guided me with her hands. My feet followed."
        l "That's it, you've got this! You're not as bad a dancer as you tried to make me believe!"
        "I held her hand up and made her do a twirl before pulling her towards me and catching her again."
        i "I know a couple of moves."
        "Her smile got wider. She was clearly amused."
        play sound "sfx/xp.mp3"
        show lust_up
        $ ian_lust_xp += 1
        call screen skillsup
        if v2_ian_date:
            "She was so close to me, her bright blue eyes right in front of mine, just like that day at the record store..."
        else:
            "She was so close to me, her bright blue eyes right in front of mine... It was the first time she was so close to me."
        "My hand rested on her hip and we were practically chest to chest. All I had to do was pull her a bit closer, just a few centimeters, and kiss her..."
        "This had to be the moment..."
        "I moved forward just a bit, about to take the step..."
        $ flena = "sad"
        $ fian = "worried"
        scene cocktailbar
        show ian at lef
        show lena at rig
        with long
        "But she took a step backwards."
        $ flena = "n"
        l "I'm thirsty! Let's get another cocktail."
        $ fian = "n"
        i "Sure."
        "Had I done something wrong? Was she uncomfortable? I had been having the opposite impression..."
        if v2_lena_kiss:
            "And it had been her who had kissed me last time! Why would she be hesitant now?"
            "Maybe I was imagining things?"
        elif v2_ian_kiss:
            "I had already kissed her once, and she had seemed OK with it. Why hesitate now?"
            "Had she changed her mind? Or maybe I was just imagining things?"
        elif v2_almost_kiss:
            "We had almost kissed at our last date. I had had the impression she had wanted it, or had been waiting for it to happen at least."
            "I couldn't be sure, but I was pretty certain she had just avoided me. Maybe she saw me just as a friend?"
        else:
            "Maybe she never intended for anything to happen between us, seeing me just as a friend."
            "I couldn't be sure, but I was pretty certain she had just avoided me. And I couldn't really pinpoint the reason."
        "We asked for another drink at the bar and took a seat."
        $ flena = "smile"
        l "See, you didn't step on my toes a single time." 
        $ fian = "smile"
        i "I think all the merit belongs to you. I can see you're a very good dancer. You must've practiced a lot."
        l "Can you believe I haven't been out dancing for almost a year? I can barely remember when the last time was..."
        i "I'm glad I brought you here, then."
        l "You did it because of me?"
        i "I thought you'd like it, yeah."
        l "You don't seem like a regular to this kind of place..."
        i "I don't?"
        l "Maybe I'm mistaken, but I picture you in another kind of ambiance... Something less mainstream."
        i "You're not wrong, ha ha... There's this rock bar me and my friends usually go to... But these places are cool, too, I like it here."
        i "I guess mainstream stuff is not that bad, after all..."
        if lena_posh > 1:
            l "Definitely! But not everybody feels comfortable with the mainstream."
        elif lena_posh > 0:
            l "I guess so, too. But not everybody feels comfortable with the mainstream."
        else:
            l "It depends. Not everybody feels comfortable with the mainstream."
        $ fian = "n"
        i "Quite often, you can be made to feel less than welcome if you don't conform to what they tell you you should be."
        i "If you're a bit different, if you're a geek, if you're shy... It can be difficult fitting in."
        $ fian = "smile"
        i "But I guess it's just a matter of learning how to let loose and just go with it."
        $ flena = "flirt"
        l "It would be fun to see you really letting loose, no doubt."
        
    $ fian = "n"
    "I could see she was being playful. But then why avoid my previous attempt to kiss her?"
    "I couldn't really figure out what she wanted. What she was expecting..."
    menu:
        "{image=icon_charisma.png}Kiss her" if v2_kiss and ian_charisma > 1 or ian_charisma > 2:
            $ renpy.block_rollback()
            $ v4_ian_kiss = True
            stop music fadeout 2.0
            "It had to be now. This was the moment."  
            play music "music/main_menu.mp3"
            if v4_place == "fortress":
                scene v4_lenadate3
            else:
                scene v4_lenadate3b
            with long
            "I didn't give her the chance to back away this time."
            "I leaned forward and kissed her, rolling the dice."
            "For a second my fate was up in the air. Acceptance or denial waiting to befall me."
            "But all that anxiety vanished when I felt Lena answering to my kiss."
            if ian_lena < 10:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_lena += 1
            "It felt like a change in the breeze, like entering a bath of warm water. She accepted my feelings and revealed her own."
            "The way we kissed, deep and slow, making the moment last, told me all I had been wanting to find out."
            $ fian = "shy"
            $ flena = "shy"
            if v4_place == "fortress":
                scene rockbar
            else:
                scene cocktailbar
            show ian at lef
            show lena at rig
            with long
            "When our kiss ended both of us felt a bit awkward."
            i "Sorry, that was a bit sudden..."
            l "No, I... I was expecting it to happen."
            $ fian = "smile"
            i "Glad to know that's the case, then. I wasn't sure..."
            l "I hope I have dispelled your doubts..."
            menu:
                "Yes, you have":
                    $ renpy.block_rollback()
                    i "Yeah, you have... But maybe you need to reassure me again, just in case."
                    play sound "sfx/xp.mp3"
                    show charisma_up
                    $ ian_charisma_xp += 1
                    call screen skillsup
                    $ flena = "happy"
                    l "Is that so?"
                    if v4_place == "fortress":
                        scene v4_lenadate3
                    else:
                        scene v4_lenadate3b
                    with long
                    "She leaned forward and kissed me again."
                    "I rested my hands on Lena's hips and pulled her towards me gently, our lips meeting again."
                    "Certainly, this time there wasn't any doubt: she liked me and wanted me."
                    "I was having trouble believing my luck, but I wasn't gonna question it at that moment."
                    "I just closed my eyes and enjoyed Lena's lips and tongue..."
                    "We kept making out for a long time, until we decided it was time to call it a night."
                    
                "Kiss her again":
                    $ renpy.block_rollback()
                    if v4_place == "fortress":
                        scene v4_lenadate3
                    else:
                        scene v4_lenadate3b
                    with long
                    "The best answer I could give her was another kiss."
                    "I rested my hands on Lena's hips and pulled her towards me gently, our lips meeting again."
                    "I felt her leaning against my chest, kissing me deeply, her tongue searching for mine."
                    "Words were unnecessary, we were communicating much more clearly through our bodies."
                    "I could finally let her know my desire for her, and she was showing me her desire for me."                    
                    play sound "sfx/xp.mp3"
                    show lust_up
                    $ ian_lust_xp += 1
                    call screen skillsup
                    "It was hard to believe, but it was real. She wanted me."
                    "We kept making out for a long time, until we decided it was time to call it a night."
        
        "Play it safe":
            $ renpy.block_rollback()
            "I decided I should play it safe. I didn't want to mess it up..."
            $ flena = "n"
            "Without being clear on what Lena really wanted I didn't feel confident enough to really go for it."
            if v2_kiss:
                "Even if we had already kissed before, that didn't mean anything."
            if v4_place == "fortress":
                "Her reaction while we were playing pool had sowed doubt in me..."
            else:
                "Her reaction while we were dancing had sowed doubt in me..."
            "I didn't want to overstep my bounds or make her feel uncomfortable around me."
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            "I would wait for a better chance... A clearer one."
            $ fian = "smile"
            i "Anyways..."
            "We continued to chat while we finished our drinks."
            "The conversation flowed without hindrances. Lena and I always hit it off really well."
            "I felt comfortable around her and I had the feeling she felt the same."
            "That's why her earlier reaction was bugging me, but I didn't want to think about that anymore."
            "I focused on enjoying myself and we had a really good time together until we decided to call it a night."
            stop music fadeout 2.0
            
    if v4_place == "fortress":
        scene street2night
    else:
        scene streetnight
    with long
    if v4_ian_kiss:
        $ fian = "shy"
        $ flena = "shy"
    else:
        $ fian = "smile"
        $ flena = "smile"
    show ian at lef
    show lena at rig
    with short
    if v4_ian_kiss:
        i "Well... It's been an interesting night..."
        l "Interesting is one way to describe it, yeah... Ha ha."
        $ fian = "smile"
        i "I'm glad we met tonight. Really."
        $ flena = "smile"
        l "Me too. I enjoyed this very much."
        l "I hope to see you again soon, Ian."
        i "Whenever you want, or can."
        $ flena = "shy"
        l "It will be very soon, if that's the case. Goodnight."
        "She kissed me briefly on the lips before waving her hand and leaving with a smile."
        stop music fadeout 2.0
        hide lena
        with short
        i "..."
        $ fian = "happy"
        i "Hell yes! It's on!"
        "I almost had to control my desire to jump."
        "I couldn't have asked for a better result than this. She liked me and wanted to see me very soon."
        i "I can't wait..."
        $ fian = "n"
        i "I wonder if I should've invited her home... Or offered to walk her home..."
        i "Maybe the night could've ended up even better..."
        i "But no, she didn't give me the option. She said goodbye right away..."
        i "Well, it's OK. It was my intention from the beginning to let her set the pace."
        "Having to wait didn't matter. What did was that I was feeling butterflies in my stomach for the first time in ages..."
        i "Lena..."
        "I knew she would be special since the day I first spoke to her..."
        
    else:
        l "I had so much fun tonight, Ian. You have no idea how much I was in need of something like this."
        i "I'm glad. We can do it again whenever you want."
        l "I would like you to want it, too."
        $ fian = "happy"
        i "Isn't that sufficiently clear? I thought it was..."
        $ flena = "happy"
        l "If it wasn't until now, you've made it clear. Thanks again, Ian."
        $ fian = "n"
        l "See you really soon."
        i "Good night, Lena."
        if v2_kiss:
            "She kissed me briefly on the lips before waving her hand and leaving with a smile." 
        else:
            "She kissed me on the cheek before waving her hand and leaving with a smile."
        hide lena
        with short
        $ fian = "n"
        i "..."
        if v2_kiss:
            i "She kissed me again... But it was just a smooch..."
            i "Damn, I'm confused now. Maybe it's just that she wants to take things really slowly?"
            $ fian = "smile"
            i "Well, if that's the case, I have no problem with it. It was my intention from the beginning to let her set the pace."
            i "I'd say it's clear she likes me, so I shouldn't worry about that... Just work to bring us closer..."
            "It was a very appealing prospect. I was feeling butterflies in my stomach for the first time in ages..."
            i "Lena..."
            "I knew she would be special since the day I first spoke to her..."
        else:
            i "I'd say that went well, but..."
            i "She kissed me on the cheek. That means she sees me only as a friend?"
            i "But I'm pretty sure I felt tension between us... My gut tells me she likes me, but I could be mistaken..."
            i "I guess I will need to keep looking for signs. I'm pretty sure I should see them soon..."
            $ fian = "smile"
            i "This is looking good. I can do this."
            "Were those butterflies that I felt in my stomach?"
   
    jump v4lenawednesday
    

##LENA HOLLY GYM ###########################################################################################################################################################################################################

label v4lenawednesday:
    
    $ ian_active= False
    $ lena_active = True
    $ save_name = "Lena: Chapter Four"
    $ day = "Wednesday"
    scene blackbg
    with long
    show active_lena
    with long
    pause 1.0  
    scene blackbg
    with long
    call screen calendar
    play music "music/normal_day.mp3"
    scene cafe
    with long
    $ flena = "n"
    $ lena_look = 1
    $ fmolly = "sad"
    show lena at rig
    with short
    "I entered the café to begin Wednesday's shift."
    "I was happy to see Molly was back after being absent the past two days."
    show molly at lef
    with short
    l "Good morning, Molly! How are you feeling?"
    mo "Oh, Lena... I'm fine, don't worry."
    mo "Ed told me he spoke to you. I'm so sorry about the situation..."
    $ flena = "sad"
    l "I understand..."
    mo "I didn't want him to tell you about our problems yet. I was hoping we could figure something out..."
    if ed_callout:
        l "What can you do, if the situation is so difficult?"
        $ fmolly = "serious"
        mo "Well, for starters, we're not going to fire you in two weeks."
        l "But Ed said he was giving me the notice..."
        mo "What Ed said was a mistake. We're going to keep employing you until we can't afford to keep this café open."
        $ fmolly = "sad"
        mo "You've been such a great help, especially now that I've been feeling a bit under the weather..."
        $ flena = "n"
        l "Thank you so much, Molly."
        mo "I know it's not much... I can't guarantee you a stable salary, but still..."
        $ flena = "sad"
    else:
        $ flena = "n"
        l "Ed told me you wouldn't be firing me right away, so..."
        mo "We will keep you employed as long as we can, but still... This is not what we promised you."
    mo "I don't want to give up... Ed says the only reasonable choice is to sell the business and live with that money until retirement, but..."
    l "He told me about how much you invested in this café and how important it is to you..."
    if cafe_help:
        l "That's why I told him I want to help keep this place afloat."
        $ fmolly = "smile"
        mo "Ed told me. You're such a kind hearted person, Lena."
        l "It's you who's a really kind hearted person. You deserve to have things go your way."
        l "I still have no idea how I can help you, but I'll try to think about something."
        mo "Thank you, Lena."
        $ fmolly = "sad"
        mo "It would break my heart having to close up shop. I want to avoid it, but I don't know how..."
        mo "I don't want to lose faith, not yet at least."
    else:
        mo "Yes... It breaks my heart having to close up shop. I want to avoid it, but I don't know how..."
        mo "I don't want to lose faith, not yet at least."
    $ flena = "n"
    l "Something will turn up, you'll see."
    $ fmolly = "sad"
    mo "And I hate putting you in this situation just as much."
    l "Don't worry... I'm young, I will find a way to make ends meet!"
    $ fmolly = "n"
    mo "You're a very strong girl. You should be proud of yourself."
    l "Thank you, Molly. I'm gonna get changed and start working."
    mo "Sure."
    hide molly
    with short
    show lena at truecenter
    with move
    $ flena = "sad"
    "I had said that, but I was struggling... I had no idea how I would set up things going forward."
    "I had a few options, but nothing safe..."
    hide lena
    show lenawork
    with short
    "I changed into my working clothes and did my job as the day went by."
    if cafe_help == False:
        "When my shift was ending I counted the cash drawer to make sure everything checked out."
        "As I counted the money and put it in an envelope for Molly and Ed, a thought appeared in my head..."
        $ flena = "worried"
        "What if..."
        "What if I took a couple of bills for myself?"
        menu:
            "Put the money back where it belongs":
                $ renpy.block_rollback()
                $ flena = "serious"
                l "What the hell am I even thinking? Am I really that desperate?"
                "I put the money back in the envelope feeling disgusted at myself for even considering something like that."
                "I wasn't that kind of person. I wouldn't steal from Molly and Ed, especially knowing how dire their situation was."
                "Doing something like that would be incredibly despicable."
                call screen willup
                $ flena = "n"
            "{image=icon_money.png}Steal from the drawer":
                $ renpy.block_rollback()
                $ cafe_steal = True
                "I looked around to make sure nobody was watching and slipped a few bills into my pocket."
                play sound "sfx/moneyup.mp3"
                show money_up
                $ lena_money += 1
                "I knew what I was doing was wrong, but I needed the money... And my time in this café was running out."
                "If I could steal a couple of bills each day Molly and Ed wouldn't notice, and I would earn a bit of extra cash."
                "I wasn't proud of what I was doing, but desperate times call for desperate means... And my troubles were bigger than Ed's and Molly's."
                "They were close to retirement and I had a whole life in front of me..."
            
    show lenawork at rig
    with move
    show molly at lef
    with short
    mo "Are you done?"
    if cafe_steal:
        l "Y-{w=0.3}yes! Done for today."
    else:
        l "Yes, done for today."
    mo "Then don't waste any more time and go home! You deserve some rest."
    l "Thanks, Molly. See you tomorrow..."
    
    scene street
    with long
    $ fholly = "n"
    $ flena = "n"
    show lena at rig
    with short
    "Holly was waiting for me in front of the café."
    show holly2 at lef
    with short
    "I had convinced her to come with me to the gym this afternoon."
    h "Hi..."
    l "Hello, Holly! Are you ready?"
    h "As ready as I'll ever be, I guess..."
    l "Come on then, let's go!"
    stop music fadeout 2.0
    
    scene polegym
    with long
    play music "music/jeremys_theme.mp3" loop
    $ flena = "smile"
    $ fholly = "blush"
    $ lena_look = 2
    $ holly_look = 3
    $ ivy_look = 2
    $ fivy = "smile"
    $ holly_glasses = False
    "I took Holly to the gym and we changed into our workout clothes."
    show holly3 at lef
    show lena at rig
    with short
    l "Come, it's this way."
    h "Um... OK..."
    l "I'll introduce you to Ivy, the teacher. She's a very good friend of mine!"
    l "Look, there she is."
    show lena at rig3
    show holly3 at lef3
    with move
    show ivy2
    with short
    v "Hi, Lena! Glad to see you made it today!"
    l "You know I always come if possible."
    l "Look, this is Holly, a friend of mine. It's her first time trying pole dancing."
    v "Oh, hello there. My name's Ivy!"
    h "N-{w=0.3}nice to meet you..."
    v "You know anything about pole dancing?"
    h "No... Not at all, to be honest..."
    v "I figured as much. Don't worry, we'll start with the basics!"
    v "Let me get the class started, first..."
    hide ivy2
    with short
    "Ivy went to talk to the other girls and indicated to them the routine they should follow."
    l "She's nice, isn't she?"
    h "She's... I'm not used to being around people like her."
    l "People like her? What do you mean?"
    h "She's so sexy and full of confidence... It's like she's the polar opposite of me."
    l "Don't think about it that way! Ivy is just a normal girl, like you and me."
    hide holly3
    show holly2 at lef3
    with short
    l "I know she can look a bit intimidating at first, but she's a sweetheart, you'll see."
    h "OK..."
    $ fivy = "n"
    show ivy
    with short
    v "I'm back. OK, Holly, right?"
    h "Yes..."
    v "Come, let's get you started. Pole dancing is just like any other dance, but the athletic element is very important in the mix."
    v "It's great to build up strength, flexibility and fitness... But it's better if you see it yourself."
    v "Lena, why don't you show her what you've learned so far?"
    l "Me? Well, OK."
    l "I'm a newbie at this, too, so don't expect much, Holly!"
    v "That's why I want her to use you as an example! Come on."
    scene v1_pole1
    with long
    "I jumped on the pole and performed the first figure Ivy had taught me."
    "I spun around as I held myself up, using mostly my legs instead of my arms."
    v "Good, you have this one down!"
    v "Move to the next one."
    scene v2_pole1
    with long
    "I maneuvered my body to change positions while spinning."
    "I had practiced this one before, and managed to get it right easier than I expected."
    play sound "sfx/xp.mp3"
    show athletics_up
    $ lena_athletics_xp += 1
    call screen skillsup
    v "Just like that! Remember to use your core strength..."
    "I did as she said, straightening my body, arms and legs as much as possible."
    h "Oh, wow... That's beautiful..."    
    if lena_athletics > 2:
        v "You're doing great! Try with the posture I was teaching on the last class!"
        scene v4_gym_lena
        with long
        "I hadn't tried that one before, but I felt confident enough to give it a shot."
        "I clasped my hands tightly around the pole and used my abdominal strength to launch my legs upwards, getting my body upside down."
        "I locked my legs as I had seen Ivy and the other girls do and let go of my hands, extending them to the sides as my body kept spinning slowly."
        v "Awesome! Well done, Lena, you got it on your first try!"
        h "Oh, wow...!"
        "I held the pose as long as I felt comfortable with and then got back down on my feet as gracefully as I could."
    scene polegym
    $ fholly = "shy"
    $ flena = "n"
    show holly2 at lef3
    show ivy
    show lena at rig3
    with long
    l "Whew! That's about it."
    if lena_athletics > 2:
        h "That was amazing..."
        l "It went better than expected!"
        v "Those are some nice improvements! Oh, I'm such a good teacher."
        v "See, Holly? You can learn fast if you apply yourself to it!"
    else:
        h "That was impressive..."
        l "Not at all. I still have a ton to improve."
        v "And you will, thanks to this great teacher here, ha ha!"
        v "See, Holly? Step by step, no need to rush it."
    v "Give it a try."
    $ fholly = "blush"
    hide holly2
    show holly3 at lef3
    with short
    h "B-{w=0.3}but I don't even know where to start..."
    v "Do as Lena did, jump on the pole and try to hold yourself on it."
    v "You don't need to do anything else, just hold on and spin a bit. Get yourself familiar with it."
    h "I'll try..."
    hide lena
    hide ivy
    with short
    show holly3 at truecenter
    with short
    "Holly stood in front of the pole during a few seconds, not daring to jump on it."
    h "..."
    l "Come on, Holly, you can do it!"
    scene v4_gym_holly1
    with long
    "She took a deep breath, held the pole with her hands and jumped."
    "She squeezed her legs together, trying to hold on as the pole began spinning with her inertia."
    l "That's it, just like that..."
    scene v4_gym_holly2
    with short
    h "..."
    scene v4_gym_holly3
    with short
    "She immediately began sliding down the pole until her knees reached the floor."
    h "..."
    $ flena = "sad"
    $ fholly = "blush"
    scene polegym
    show holly2
    show lena at rig3
    show ivy at lef3
    with short
    h "It's... It's no use. I can't..."
    v "Don't worry, it's normal! You're not used to it, you need to build up some strength!"
    v "And do you know how to do that? By trying over and over again!"
    $ flena = "smile"
    l "That's it!"
    h "I don't see how I could do it, even in a million years..."
    v "That's because you haven't tried for a single day! Keep working at it, OK? Don't be afraid to fail every time, it's only your first class."
    v "We'll let you work, OK? I'll check on you in a while."
    h "OK..."
    $ flena = "n"
    hide holly2
    with short
    show lena at rig
    show ivy at lef
    with move
    "We left Holly to it and moved to another spot."
    v "Where did you get this poor thing from?"
    l "I met her at the café... I think I told you about her."
    v "She looks like a helpless puppy. I can't but feel pity for her!"
    l "She's a very nice girl... But she had a hard time growing up and is so timid..."
    v "I'm not bashing on her, just stating the obvious. It's been a long time since I had someone like her around."
    v "But it's typical for you to offer your hand to the poor and wretched souls, isn't it?"
    $ flena = "smile"
    l "I guess it is. I offered you my hand, didn't I?"
    $ fivy = "flirt"
    v "You bitch! But you're right, you were my only friend back in high school. You like helping lost causes!"
    l "It's not going so badly for yourself, so maybe we can still make something out of you!"
    v "I'm not losing hope either, ha ha. But it will take a ton of work to make something out of Holly..."
    l "She's already a great gal. She only needs some confidence to make her worth shine."
    v "I can see that... Well, let's see if she sticks around and has the will to do just that."
    l "I hope she does. It would benefit her greatly."
    v "Anyways, if you're done with your good act of the day, start training a bit yourself!"
    l "Right on it, ma'am."
    stop music fadeout 2.0
    scene polegym
    with long
    "We continued to work until the class was dismissed, and went to the locker rooms to take a shower and change."
    $ flena = "n"
    $ fholly = "sad"
    $ holly_look = 1
    show lenabra at rig
    show hollybra at lef
    with short
    l "So Holly, how was your first experience? Did you like it?"
    h "Um... I don't know... It was hard."
    h "I didn't manage to even stay on the pole... It's too challenging for me."
    l "It is now, but if you keep at it you'll get better, you'll see."
    h "I don't think I can. This is not for me."
    menu:
        "Encourage her":
            $ renpy.block_rollback()
            $ encourage_holly = 3
            $ holly_gym = True
            l "That's not true. Thinking like that will make it true, though."
            h "But you've seen how badly I did..."
            l "Yeah, that's because it's challenging. You said it yourself."
            l "Challenges can be really hard, but you shouldn't run away from them."
            l "I mean, if you don't like pole dancing, you don't have to force yourself to do it, of course."
            l "But if the reason you're giving up is because you're afraid to take on a challenge, then that's not good."
            l "It can be pole dancing, or anything else in life..."
            h "You're right... But it seems like any challenge is too big for me."
            
        "Agree with her":
            $ renpy.block_rollback()
            if encourage_holly > 0:
                $ encourage_holly -= 1
            $ flena = "sad"
            l "If that's how you feel, maybe that's the way it is..."
            l "Not everybody's cut for the same stuff."
            h "Yeah... I can write well, but that's about it..."
            l "Oh, come on, you have other virtues..."

    h "I mean, it's hard for me not to be aware of my own inadequacy..."
    h "Look at you, for example. You're so beautiful, and tall, and charming..."
    h "And look at me, I'm small, and plain, and flabby..."
    l "You're neither plain nor flabby!"
    "Holly poked herself on the stomach."
    h "Look at how soft it is. And I'm flat as a board and..."
    h "Ian would never notice someone like me. Not while having someone like you around."
    $ flena = "sad"
    "So that was the gist of the matter..."
    if lena_go_ian > 0:
        "She had probably noticed some chemistry between me and Ian. And it was so painfully obvious she liked him..."
    else:
        "It was so painfully obvious she liked him..."
    "I was making her feel bad, or threatened? That was a position I didn't want to be in..."
    l "So... You like Ian?"
    $ fholly = "blush"
    hide hollybra
    show hollybra3 at lef
    with short
    h "Well, yeah, I mean... It's hard not to..."
    if lena_go_ian > 0:
        h "But I know he prefers you, and who wouldn't...?"
    else:
        h "But he doesn't see me like that. Who could?"
    l "Don't say that! It's not like that..."
    menu:
        "{image=icon_friend.png}You're lovely" if lena_holly > 4 or lena_go_holly > 0:
            $ renpy.block_rollback()
            if lena_go_holly == 0:
                $ lena_go_holly = 1
            $ flena = "shy"
            l "Actually, I think you're really lovely, Holly. In a lot of ways."
            h "Y-{w=0.3}you think I am?"
            l "Of course... You're clever, very cute and one of the most good-hearted people I've ever met."
            l "What's not to love about you?"
            "Her face turned completely red."
            h "I... I don't know what to say."
            h "Thank you..."
            $ flena = "smile"
            l "Love yourself a little more, OK?"
            
        "You're OK":
            $ renpy.block_rollback()
            $ flena = "n"
            l "You're OK, Holly. There's nothing wrong with you."
            l "You need to stop believing that and maybe you'll be able to see yourself from a different perspective."
            l "I assure you a lot of people see you with those eyes, too."
            h "I wish I knew how..."
            l "You'll figure it out, but you need to push yourself out of your comfort zone a little bit..."
            
        "You'll find someone":
            $ renpy.block_rollback()
            l "There are a lot of fish in the sea. Even if Ian doesn't see you that way, you'll find someone who will..."
            h "I... My experience tells me otherwise."
            h "But let's not talk about that, now..."
            l "OK... All I'm trying to say is you should be a bit kinder to yourself. Don't bash yourself so much."

    h "I'll try..."
    scene streetnight
    with long
    $ holly_glasses = True
    $ lena_look = 1
    $ flena = "n"
    $ fholly = "n"
    $ holly_look = 1
    "We finished changing and left the gym."
    show lena at rig
    show holly at lef
    with short
    h "My arms feel weird... It's like I have no strength left in them."
    l "You'll probably be really sore tomorrow, but don't worry. It happened to me at first, too."
    h "Thank you for inviting me today... I really appreciate it."
    l "Of course! You know I like spending time with you."
    h "I do, too..."
    l "See you at the café soon?"
    $ fholly = "smile"
    h "Yeah. Good night, Lena."
    hide holly
    with short
    if lena_go_holly > 0:
        l "She's so cute... I really like her..."
    else:
        l "She's so cute."
    if v4_ian_date:
        $ flena = "sad"
        show lena at truecenter 
        with move
        "And now I had to go home and get ready to meet Ian..."
        "But what should I do after what Holly had confessed?"
        "I had already known she liked him in some kind of way, but it seemed she was really into him..."
        "What if something happened between Ian and me? That would hurt Holly for sure."
        "If we started dating, or even just hooked up, she would probably distance herself from us."
        if v2_kiss:
            "And we had already kissed once, but Holly didn't know about that..."
        "Last thing I wanted was to make Holly feel bad..."
        "I was making a lot of assumptions, though. I had no idea how the date would go."
        $ flena = "n"
        l "Stop stressing yourself out, Lena. Try to enjoy yourself tonight..."
    else:
        l "Time for me to go home, too."
    jump v4lenaafterdate

    
##AFTER DATE #################################################################################################################################################################################################################
label v4lenaafterdate:
    
    if v4_ian_date:
        scene blackbg
        with long
        call screen v4afterdate
        scene lenaroomnight
        with long
        $ flena = "n"
        $ lena_look = 2
        show lenabra at rig
        with short
        "I arrived home after saying goodbye to Ian."
        play sound "sfx/meow.mp3"
        show lola at lef
        with short
        "As I changed Lola jumped on the bed to greet me and asked to be petted."
        l "Hey, baby girl..."
        play sound "sfx/purr.mp3"
        hide lola
        show lolahappy at lef
        l "Do you want to know how the date went?"
        if v4_ian_kiss:
            $ flena = "shy"
            l "It went great... At first I was a bit hesitant because of what Holly had told me, but..."
            l "We ended up making out in the middle of the bar!"
            l "And the guy knows how to properly kiss a girl... I got so much into it."
            l "If we had been in someone's bedroom things would've escalated for sure..."
        else:
            l "It went really good. I had a lot of fun with him."
            l "It's clear he really likes me... I think he even tried to kiss me, but I hesitated because of what Holly had just told me..."
            l "I wonder if I did the right thing. He seemed a bit confused. No wonder he didn't try again..."
            l "I like him, but I feel I need a bit more time. I don't want to ruin things by acting without proper consideration..."
        if v4_ian_kiss:
            l "I wonder if I should hold back... I feel I want to be with Ian, sleep with him..."
            l "And I know he wants it, too. But he's being respectful, letting me set the pace."
            l "And that's what I'm wondering. What pace should we move at? Is it too soon?"
            l "Is tonight the right moment to take the next step?"
            menu:
                "{image=icon_lust.png}Invite Ian over" if v4_ian_kiss and lena_lust > 3:
                    $ renpy.block_rollback()
                    $ ian_lena_sex = True
                    $ v4_ian_lena_sex = True
                    "I made up my mind and decided to call him."
                    l "No need to keep postponing things..."
                    $ flena = "flirtshy"
                    "I really wanted to have sex with him."
                    "I had been thinking about it the whole night. I wanted to know what I would feel with him in bed..."
                    "I was horny and I wanted to be with him right now. We both wanted it."
                    jump v4iansex                
                    
                "{image=icon_love.png}Invite Robert over" if lena_robert_sex and lena_robert_over == False:
                    $ renpy.block_rollback()
                    "I didn't want to call Ian tonight. It was too soon for that."
                    l "It's better if I take things slow with Ian. I really like him and I don't want to mess things up."
                    if v4_ian_kiss:
                        $ flena = "sad"
                        l "Besides, I have to be mindful of Holly... Though it's a bit late for that. We already made out..."
                        l "It's clear there's something between Ian and me."
                    else:
                        l "Besides, I have to be mindful of Holly... That's why I didn't kiss Ian tonight."
                    $ flena = "flirt"
                    l "It's a shame ending a night like this one alone, after such a perfect date..."
                    l "But I have Robert for moments like these!"
                    play sound "sfx/meow.mp3"
                    hide lolahappy
                    show lola at lef
                    "Lola looked at me, almost as if she was questioning me."
                    l "I know you don't like him that much but I'm gonna call him... I could use someone's company tonight."
                    l "Sex is always a good remedy to forget about my frustrations, even if just for a while... And I need that now."
                    jump v4callrobertwed
                        
                "Go to sleep":
                    $ renpy.block_rollback()
                    $ flena = "n"
                    l "It's too soon for that... I don't want to mess this up."
                    l "It's better if I take things slow with Ian. I really like him..."
                    $ flena = "sad"
                    if v4_ian_kiss:
                        l "And I also have to be mindful of Holly... Though it's a bit late for that. We already made out..."
                        l "It's clear there's something between Ian and me."
                    else:
                        l "And I also have to be mindful of Holly... That's why I didn't kiss Ian tonight."
                    l "Anyways... Time to go to sleep."
                    scene lenaroomnight
                    with short
                    "I got into bed and Lola snuggled next to me."
                    "She was all the company I needed that night."
                    jump master_script
        
        elif lena_robert_sex and lena_robert_over == False:
            $ flena = "sad"
            l "It's a shame ending a night like this one alone..."
            l "It would've been the icing on the cake for a perfect date."
            jump v4ianrobert
        else:
            l "Anyways, I'm pretty happy with how things are so far..."
            l "I'm excited to see how they evolve."
            l "Time to go to bed, now!"
            jump master_script
          
    elif lena_robert_sex and lena_robert_over == False:
        $ lena_go_ian = 0
        scene lenaroomnight
        with long
        $ flena = "n"
        $ lena_look = 1
        show lenabra at rig
        with short
        "I cooked myself some dinner and after that went to my room to relax."
        play sound "sfx/meow.mp3"
        show lola at lef
        with short
        "Lola jumped on the bed and asked to be petted."
        l "Hey, baby girl..."
        play sound "sfx/purr.mp3"
        hide lola
        show lolahappy at lef
        if cafe_steal:
            $ flena = "sad"
            l "If you knew what I did today... Stealing from the Van Dykes..."
            l "You probably wouldn't be asking for my affection. I'm a bad person."
            l "But I need to survive."
            l "At least I did something good by bringing Holly to the gym. I think she needs it."
        else:
            l "Today's been a good day... In both good and bad ways."
            l "I'm worried about my future with all that's happening..."
            l "But I made a new friend. Holly seemed happy that I brought her to the gym today."
        $ flena = "sad"
        l "Don't take this the wrong way, Lola, but I feel a bit alone today..."
        if louise_jeremy == False:
            l "My flatmates are at odds and things with Louise are a bit weird since I told her about Jeremy."
        l "I wonder if I should've gone to that date with Ian..."
        l "But I guess he's not really my type. Or maybe he is but he's not the right guy for this moment in my life. Who knows."    
        menu v4ianrobert:
            "{image=icon_love.png}Call Robert" if lena_robert_sex and lena_robert_over == False:
                $ renpy.block_rollback()
                $ flena = "flirt"
                l "I have Robert, though."
                hide lolahappy
                show lola at lef
                l "I know you don't like him that much but I'm gonna call him... I could use his company tonight."
                l "Sex is always a good remedy to forget about my frustrations, even if just for a while..."
                jump v4callrobertwed
                    
            "Go to sleep":
                $ renpy.block_rollback()
                $ flena = "n"
                l "Time to go to sleep."
                scene lenaroomnight
                with short
                "I got into bed and Lola snuggled next to me."
                "She was all the company I needed that night."
                jump master_script
        
    else:
        $ lena_go_ian = 0
    jump master_script
    
    
##ROBERT SEX 2 ################################################################################################################################################################################################################    
    
label v4callrobertwed:   
    $ v4_robert_repeat = True
    hide lola
    with short
    show lenabra at truecenter with move
    hide lenabra
    show lenabra_phone
    with short
    l "..."
    show phone_robert_smile at lef3
    with short
    r "Hey, Lena!"
    l "What's up, Robert? Are you off from work?"
    r "Just leaving, yeah. Why?"
    l "Do you want to come over?"
    r "You know I do!"
    l "Cool. I'll be waiting."
    r "Already on my way!"
    hide lenabra_phone
    show lenabra
    hide phone_robert_smile 
    with short
    l "I knew he'd be willing."
    "He didn't keep me waiting for long. Fifteen minutes later I was opening the door for him and welcoming him to my room."
    $ frobert = "flirt"
    $ robert_look = 1
    show lenabra at rig
    with move
    play sound "sfx/door.mp3"
    show robert at lef
    with short
    r "Hey, babe. So you wanted to see me?"
    l "If that wasn't the case I wouldn't have called."
    r "And what's that you want from me, huh?"
    $ flena = "slut"
    l "You know very well what I want."
    play music "music/sex.mp3"
    hide lenabra
    show lenanude2 at rig
    with short
    "I didn't need words to make him understand that. I stripped my clothes off, teasing him."
    "I knew Robert didn't need too much encouragement, though."
    "He was all over me in a matter of seconds."
    scene v4_robert1
    if lena_piercing1:
        show v4_robert1_p1
    if lena_piercing2:
        show v4_robert1_p2
    with long
    r "Mhhh...!"
    "He glued his lips to mine and his hands to my boobs."
    "As we made out I helped Robert get rid of his clothes."
    "I was happy to find his cock already hard and ready for action. I enjoyed how effortless it was for me to turn Robert on!"
    if lena_piercing1 or lena_piercing2:
        r "Holy shit, babe... I just noticed that belly piercing..."
        l "Mhh... You like it?"
        r "Fuck, you were sexy before, but now I can barely take it..."
        r "I want to fuck you so badly..."
    else:
        "He groaned when I wrapped my hand around the shaft and began stroking it."
        r "Mhhh, baby... I can't wait to fuck you..."
    scene v4_robert4b
    with long
    l "Is that so?"
    "I got on all fours on top of the bed and smiled at him invitingly."
    l "Then come and take me."
    "I loved the look on his face. He was barely able to control himself while searching for a condom and putting it on."
    "He couldn't take his eyes off of me... which made putting on the condom a difficult task."
    l "Come on, I'm waiting."
    "I wiggled my ass playfully."
    r "Holy fuck!"
    if lena_lust < 6:
        play sound "sfx/xp.mp3"
        show lust_up
        $ lena_lust_xp += 1
        call screen skillsup
    scene v4_robert4
    with long
    "I teased Robert beyond what he could take."
    "He shoved his cock into my slit right away, diving into what I was offering him."
    play sound "sfx/oh1.mp3"
    l "Ohh!"
    r "Fuck, babe! Fuck!"
    "He held my hips in place as he slammed his forward, penetrating me savagely right from the start."
    "A quick and passionate fuck, just what I was in need of."
    "I began playing with my pussy, adding to the pleasure of Robert's ravenous cadence."
    l "Mhh, yes, keep it up!"
    "I heard Robert grunting and wheezing behind me as he kept fucking me with all his energy."
    "I normally preferred another style of love-making, but right now I was enjoying this so much."
    "I had an itch that needed to be scratched, a desire to be satisfied without preambles, and I had the power to get just what I wanted."
    "A simple call and a few minutes later the loneliness of my night had turned into wild sexual satisfaction."
    "I loved having Robert inside me, pounding at me, bending to my wishes..."
    "It turned me on so much and and it was driving me closer to climax at great speed."
    l "I'm almost there, don't stop now, Robert!"
    r "Ughh!"
    "My words encouraged him to give everything he had left while I rubbed my clit fast and intensely."
    l "Yes, yes, yes...!"
    play sound "sfx/orgasm1.mp3"
    with vpunch
    l "Oaahhh!!"
    "I was sure my flatmates would've heard that moan, but I didn't care at this point."
    scene lenaroomnight
    with long
    stop music fadeout 2.0
    "Robert's orgasm followed shortly after. I fell asleep right after that, my needs already satisfied."
    jump master_script
    
## IAN SEX ################################################################################################################################################################################################################    

label v4iansex:
    
    play sound "sfx/meow.mp3"
    hide lolahappy
    show lola at lef
    l "Yes, I'm gonna call him... I shouldn't be afraid of taking what I want!"
    hide lenabra
    show lenabra_phone at rig
    with short
    l "..."
    show phone_ian_worried at lef3
    with short
    i "Yes? Lena?"
    l "Hi..."
    i "Is everything alright?"
    l "Yes, it is. I just wanted to ask..."
    l "Are you home yet?"
    hide phone_ian_worried
    show phone_ian at lef3
    i "No, not yet... I'm halfway there. Why?"
    l "I was wondering if... If you'd like to have one last drink at my place."
    hide phone_ian
    show phone_ian_surprise at lef3
    l "I know it's a bit late, but... I'd really like to."
    i "Uh, sure...! One last drink sounds cool...!"
    l "Alright. I'll text you the address. It shouldn't be too far away from where you're now..."
    hide phone_ian_surprise
    show phone_ian_shy at lef3
    i "I'm on my way."
    hide phone_ian_shy
    hide lenabra_phone
    show lenabra at rig
    with short
    "I bit my lip."
    l "He's really coming... Now I'm nervous!"
    "Fifteen minutes later Ian was waiting at the door."
    scene lenahomenight_dark
    with long
    $ lena_look = 1
    $ flena = "shy"
    $ fian = "shy"
    "I covered up a bit with a t-shirt before greeting him."
    play sound "sfx/door_home.mp3"
    show lenabra at rig
    show ian at lef
    with short
    l "Hey..."
    if v3_ian_date:
        i "Hi... Here I am, again."
    else:
        i "Hi... So this is your place?"
    l "Yes, come on in... Let's go directly to my room, I don't want to disturb my flatmates."
    i "Sure."
    play sound "sfx/door.mp3"
    scene lenaroomnight
    show ian at lef3
    show lenabra at rig3
    with long
    if v3_ian_date:
        l "Sorry, I know my room's bit small, but..."
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
        l "And this is my room. It's a bit small, but it's all I need..."
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
    l "Yes, she is..."
    "And she was stealing Ian's attention. I wanted those caresses to be for me..."
    "I wanted him to make me purr..."
    l "OK, that's enough."
    hide lolahappy
    with short
    "I nudged Lola and made her jump off the bed and leave the room."
    i "Oh, poor thing..."
    $ flena = "slut"
    hide lenabra
    show lenaunder at rig3
    with short
    $ fian = "surprise"
    "I closed the door behind Lola and took off my t-shirt."
    $ fian = "shy"
    l "How about you pay some attention to me, now?"
    i "That's why I came..."
    play music "music/ourredstring.mp3" loop
    scene v4_lena1
    if lena_piercing1:
        show v4_lena1_p1
    if lena_piercing2:
        show v4_lena1_p2
    with long
    "I embraced him and searched his mouth with mine. My lips were hungry for his kisses."
    "This time I felt his hands directly on my naked skin, as his fingers descended down my back and held my hips, pulling me towards him."
    "I wanted to feel him, too. I took off his shirt, revealing his torso."
    "His body was so incredibly warm... I felt I was about to start sweating just by making out."
    "His tongue entangled with mine performing a wet and luscious dance. Our desires had been set free and were mixing together..."
    "However, his hands never ventured outside the safe zone. It seemed like Ian was hesitant to extend his caresses to my ass or breasts."
    "That was his lovely awkwardness at work... It was to be expected for him to be a bit shy."
    "It fell to me to lead the action. It's what I had already decided to do from the moment I invited Ian over."
    "I had no need to keep up appearances."
    scene v4_lena2
    with long
    i "Uh..."
    "I pushed Ian down to the bed, took off my panties with a playful smile and climbed on top of him."
    "Our lips met again in a deep and passionate kiss while my hands slid down his chest and torso, feeling Ian's build."
    "He was lean and quite athletic and had broad shoulders. He was handsome, too... I found everything about him attractive."
    if lena_bdick > 1:
        "I wondered what he would be hiding under his pants... I hoped I wouldn't be disappointed..."
    "Ian began letting loose as he felt my unrestrained passion."
    "His hands became bolder, exploring my body slowly, thoroughly, attentively..."
    "He dug his fingers into my butt cheeks and ran them down my thighs, making me shiver."
    "My pussy was already soaking and my hips wanted to move on their own..."
    "As we kissed I began grinding on top of him, pressing my crotch down on his."
    "I could feel the bulge under his pants, and I knew I wouldn't be disappointed..."
    menu:
        "Suck him off":
            $ renpy.block_rollback()
            if lena_bj < 3:
                $ lena_bj += 1
            "I had no rush... I wanted to enjoy him, to enjoy the moment..."
            "I wanted him to enjoy me."
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
            else:
                if lena_robert_sex:
                    "It was just a bit longer than Robert's, but noticeably thicker."
                else:
                    "He was well endowed, that much was true..."
            play sound "sfx/bj1.mp3"
            "I took my time kissing and licking his manhood, getting to know it, its shape, its taste..."
            "Noticing Ian's reactions depending on where and how I licked him, the way he tensed his body, how his breathing changed, when he sighed..."
            "I spent several minutes with it, and each time I felt more excited, more willing to be taken by Ian..."
            "And this time it wasn't me who decided to take the lead."
            i "Lena, that's enough. I can't wait anymore, I want to be inside of you..."
            l "Just what I wanted to hear..."
            "I reached out and grabbed a condom from the drawer."
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
            else:
                "He was well endowed, that much was true..."
                if lena_robert_sex:
                    "It was just a bit longer than Robert's, but noticeably thicker."
               
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
            if lena_lust < 6:
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
            "I could feel her trembling, at the brink of orgasm..."
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


    
screen book_screen_3:
    
    imagebutton idle "card3_darklord.png" hover "card3_darklord_hover.png" focus_mask True action SetVariable("book_card2", "dark_lord") , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "card3_villain.png" hover "card3_villain_hover.png" focus_mask True action SetVariable("book_card2", "villain")  , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "card3_relativistic.png" hover "card3_relativistic_hover.png" focus_mask True action SetVariable("book_card2", "relativistic") , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
        
    
screen v4navelpiercing:
    
    imagebutton idle "v4_navel1.png" hover "v4_navel1_hover.png" focus_mask True action SetVariable("lena_piercing1", True) , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "v4_navel2.png" hover "v4_navel2_hover.png" focus_mask True action SetVariable("lena_piercing2", True)  , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    
screen v4afterdate:
    
    imagebutton idle "blackbg1.png" action Null, Return at fade_in_skill
    
    vbox:
        xcenter 0.5
        ypos 430
        text "{font=peach_pen.ttf}{size=120}After the date ended..."