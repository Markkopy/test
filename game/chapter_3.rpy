################################################################################################################################################## 
###################################################### CHAPTER 3 KNOTS #################################################################################
################################################################################################################################################## 
label chapter_three:
    
    $ lena_active = True
    $ ian_active = False
    $ save_name = "Lena: Chapter Three"
    
    show blackbg
    with long
    call screen chapter_title

## LENA SATURDAY ###########################################################################################################################################################################################
    $ lena_jeremy = 3
    $ robert_hurt = 0
    $ day = "Saturday"
    show active_lena
    with long
    pause 1.0
    scene blackbg
    with long
    pause 0.5 
    call screen calendar
    scene restaurant
    with long
    $ lena_look = 2
    $ flena = "worried"
    show lenawork
    with short
    "To most people, Saturday night meant meeting friends, partying, relaxing, going to the cinema..."
    "For me it only meant work."
    "It was me who was serving all those people who were out enjoying their weekend. The restaurant was really busy tonight."
    "But I had almost gotten used to that. Almost."
    "What had me in agony was the fact that they had changed my shifts for this week."
    "I normally had my days off on Sunday and Wednesday, and half of the month's Mondays."
    "But they had asked me to work from Thursday to Tuesday because one of the staff members was ill or something."
    "I would be working six nights in a row!"
    l "{i}*Sigh...*{/i} I'd really hoped I could rest Sunday night..."
    "At least I was getting Wednesday and Thursday nights off, but it was too little, and too late."
    l "I'm starting to really hate this job..."
    if v2_robert_date:
        "And I didn't even know if I was going to get fired at the end of the month!"
        if v2_robert_reject:
            "Robert said he'd speak with the boss on my behalf, so it should be fine."
        else:
            "I trusted Robert would speak to the boss on my behalf, so I shouldn't worry too much."
    hide lenawork
    with short
    "I kept serving tables until the last customer left and after cleaning up I was finally free."
    $ lena_look = 1
    $ flena = "sad"
    stop music fadeout 2.0
    scene street2night
    with long
    show lena 
    with short
    l "Tonight's been intense... I left so late today."
    l "At least I get to rest tomorrow morning."
    if v3_robert_date:
        play sound "sfx/ring.mp3"
        "As I made my way back home, my phone buzzed."
        "Robert was calling me. What could he want at this hour?"
        menu:
            "Pick up":
                $ renpy.block_rollback()
                hide lena
                show lena_phone
                with short
                $ flena = "n"
                l "Yes?"
                show phone_robert_smile at lef3
                with short
                r "Hi, Lena! Have you left work already?"
                "He was speaking loudly and seemed in a good mood. A lot of voices and faint music could be heard in the background."
                l "Yes, why? Where are you?"
                r "I was partying with the boys but we're going to call it a night."
                l "You went partying again? You did that on Tuesday, too, right?"
                r "Yes, this was a long weekend, so we had to take advantage of it!"
                l "Lucky you... I'm working every single night."
                if v2_robert_home:
                    r "Well, you're not working now! I was thinking... Maybe we could end the night together."
                    $ flena = "sad"
                    l "Oh..."
                    l "Right now I'm beat, Robert. All I want is to get home and get some sleep. You know I'm working six nights straight this week."
                    hide phone_robert_smile
                    show phone_robert at lef3
                    r "Yeah, I know... But I'm dying to see you..."
                    hide phone_robert
                    show phone_robert_flirt at lef3
                    r "We have some unfinished business, you and I, after all!"
                    $ flena = "shy"
                    l "That's true..."
                    l "How about we meet tomorrow?"
                    r "Tomorrow afternoon sounds fine! Around five?"
                    $ flena = "n"
                    "It was as good as any other moment to meet Robert again. Maybe the best moment, considering my awful schedule this week."
                    l "Alright."
                    r "Cool! See you tomorrow babe!"
                else:
                    r "Well, you're free during the day and the afternoon, aren't you?"
                    l "Yeah."
                    if v2_robert_chance:
                        r "You said you would meet me again during the weekend."
                    else:
                        r "I'm dying to see you again."
                    r "Let's meet tomorrow afternoon!"
                    "It was as good as any other moment to meet Robert again. Maybe the best moment, considering my awful schedule this week."
                    l "Alright, tomorrow at five."
                    r "Cool, cool. See you tomorrow then!"
                hide phone_robert_smile
                hide phone_robert_flirt
                hide lena_phone
                show lena
                with short
                "This situation with Robert had me wondering."
                if v2_robert_home:
                    "I would've had sex with him by now, if it hadn't been for that hiccup with the condom..."
                    "It had been a while since I had slept with someone. But I was probably overthinking things."
                    "What was so wrong about sleeping around with someone? As Ivy said, I should just do it and stop fretting about it."
                    "Besides, Robert seemed like the perfect guy to do just that. I found him quite attractive and he liked me a lot."
                    "Taking that step with him would help me turn the page once and for all. I couldn't keep sulking about my breakup."
                elif v2_robert_kiss:
                    "He was the first guy I had kissed in quite some time. The first since Axel..."
                    "Robert was interested in me, those cards were up on the table. But I still was on the fence about how to play things."
                    "What was so wrong about sleeping around with someone? As Ivy said, I should just do it and stop fretting about it."
                    "Besides, Robert could be just the perfect guy to do that. I found him quite attractive and he liked me a lot."
                    "Taking that step with him would help me turn the page once and for all. I couldn't keep sulking about my breakup."
                elif v2_robert_chance:
                    "Robert was interested in me, those cards were up on the table. But I still was on the fence about how I felt about him."
                    "I had given him a second chance despite rejecting his advances on our first date. I wasn't sure why I'd done it."
                    "Maybe I just needed some more time to warm up to things. Take one step at a time."
                    "What was so wrong about sleeping around with someone? As Ivy said, I should just do it and stop fretting about it."
                    "Robert was offering me that chance. I found him somewhat attractive and it was clear he liked me a lot."
                    "Taking that step with him would help me turn the page once and for all. I couldn't keep sulking about my breakup."
                $ flena = "sad"
                if v2_ian_date:
                    "Then again, things weren't so simple. Robert was not the only guy I was considering getting close to..."
                    if v2_kiss:
                        "That kiss Ian and me had shared had made clear the attraction we felt for each other."
                        "I was still getting to know him, but I was really liking what I had seen so far."
                        "It was too early to get any ideas, though. Still, it made me wonder if fooling around with Robert was something I should be doing..."
                    else:
                        "I had really enjoyed my date with Ian, but I wasn't sure about what the deal was with him."
                        "Was he really interested in me? Was I?"
                        if v2_almost_kiss:
                            "Though we had almost kissed, or so it felt to me... What seemed clear was that there was some kind of tension between us."
                            "What I wasn't clear about was if that was a tension I should explore."
                        "He was an interesting guy, and pretty nice. But maybe I shouldn't expect things to progress further than a good friendship."
                        "There was no reason to feel bad about fooling around with Robert, right?"                        
                "I wanted to move on, that much was clear. But Axel was still haunting me, and not just in memory."
                "My last argument with Mom was still fresh on my mind..."
                "What the hell was Axel doing showing up at my parents' place? Maybe I really should talk to him, just to tell him to stop it for good!"
                l "Ahhh, why can't I get a break? I just want to have it easy for a while!"
                                
            "Ignore him":
                $ renpy.block_rollback()
                $ v3_robert_ignore = True
                "I was too tired and all I wanted was to get home and get into bed."
                l "Sorry, but I'm offline today."
                "I ignored his call and let the phone buzzing die down."
                "Anything he had to tell me he could do tomorrow morning."
    
## LENA SUNDAY ###########################################################################################################################################################################################
    
    $ v3sundaypeoplegram = False
    $ v3sundaystalkfap = False
    $ v3sundayseymour = False
    $ louise_look = 1
    $ day = "Sunday"
    scene blackbg
    with long
    call screen calendar
    show lenaroom
    with long
    if v2_lena_stan_model_shirt:
        $ lena_look = 2 
    else:
        $ lena_look = 1
    $ flena = "n"
    show lenabra
    with short
    "I got up pretty late next day."
    l "Ahh... I needed some rest."
    play sound "sfx/meow.mp3"
    show lola at lef3
    with short
    l "Good morning, Lola... Or should I say good afternoon? It's almost lunch time!"
    l "You're hungry, aren't you?"
    "I got up and went to the kitchen to feed her."
    play music "music/normal_day.mp3" loop
    $ flouise = "happy"
    play sound "sfx/door.mp3"
    scene lenahome
    show lenabra 
    show lola_b at lef3
    with short
    show louise at rig3
    with short
    lo "Look who's getting up!"
    l "Good morning Louise. You look cheerful today!"
    lo "Yeah, I'm meeting my boyfriend this afternoon! We'll go to the cinema and then we'll have dinner at a Japanese restaurant that I heard is really good!"
    l "I'm glad."
    "I poured some cat food into Lola's bowl and she began eating eagerly."
    hide lola_b
    with short
    if v2_lena_stan_model_shirt:
        $ flouise = "sad"
        lo "By the way... Shouldn't you put a shirt on or something at least?"
        lo "Stan could walk out any minute now and see you like this!"
        l "Oh... I don't really mind."
        lo "You don't?"
        l "It's not different to wearing a bikini, if you think about it. And you know it's not a big deal for me."
        lo "I know, I know, you're a model and all that. But context is important... We're not at the beach and, well..."
        lo "Stan's just a creep."
        menu:
            "{image=icon_friend.png}He's not like that" if lena_stan > 4:
                $ renpy.block_rollback()
                $ v3_defend_stan = True
                l "Come on, don't say that. He's alright."
                $ flouise = "serious"
                lo "Are you serious?"
                play sound "sfx/frienddown.mp3"
                $ lena_louise -= 1
                show friend_down
                $ flena = "serious"
                l "I don't know why you're so against him. He's never done anything bad or caused trouble."
                lo "Aren't you troubled by the creepy way he looks at us? I know I am..."
                l "He's been nothing but nice to me so far."
                lo "That's because he wants to get in your panties!"
                l "So must I assume any guy who's nice to me does it just because he wants to get a piece of me?"
                $ flouise = "sad"
                lo "I didn't say that... But you know how guys are..."
                $ flena = "n"
                l "I have nothing against Stan, and I'm not gonna treat him badly or think ill of him."
                lo "Alright, alright... I'm sorry if my comment bothered you."
                hide friend_down
                
            "Why do you think so?":
                $ renpy.block_rollback()
                $ flena = "sad"
                l "Why do you think so?"
                $ flena = "serious"
                lo "Do you really need to ask? You've seen him."
                lo "A geek like him has probably never even been with a girl. I'm sure he's horny as a dog!"
                l "We should feel sorry for him, if anything..."
                lo "Not a chance. If those are his circumstances it's his own fault. If he stopped being fat and ugly and creepy..."
                l "It's not like we can choose exactly who we want to be, Louise..."
                lo "Alright, I'm being unfair. But that's just because he gives me the creeps. The way he stares at us..."
                lo "Come on, you've surely noticed!"
                $ flena = "n"
                l "Maybe, I don't know... I mean, it's not like finding us attractive makes him a bad person."
                $ flouise = "n"
                lo "I think you're too nice, but I guess you've got a point... I just don't like him, that's all."
                
            "Maybe you're right":
                $ renpy.block_rollback()
                $ flena = "worried"
                l "You think so?"
                lo "Come on, you can't be that naive... He's not getting any action, that's clear to see, so I'm sure he's horny as a dog!"
                l "Maybe you're right..."
                lo "I'm telling you, the only thing I don't like about living in this flat is having to share it with him."
                lo "I feel like I'm living with a creep in the room next to mine. I'm sure he's a Peeping Tom or even worse..."
                "Maybe it had been a mistake posing for Stan after all."
                l "I don't know... So far he's never caused trouble, right?"
                lo "Aren't you troubled by the creepy way he looks at us? I know I am..."
                $ lena_stan -= 1
                $ flena = "n"
            
    lo "Anyways, I'm gonna get some work done before my date. I'm almost done with my Master's degree!"
    l "You've been working so hard on your thesis lately."
    lo "Yeah, I can't wait to be done with it!"
    $ flouise = "happy"
    lo "We must go out once I'm finished. And I'll introduce you to my boyfriend!"
    l "I'd like that."
    hide louise
    with short
    l "Well... I have a few hours to myself today. What should I do?"
    "A lot of things had happened these past few days. A lot of stuff to think about."
    
    if v3_robert_ignore and v3_robert_date:
        "As I was about to make a choice, my phone rang."
        play sound "sfx/ring.mp3"
        "It was Robert again."
        hide lenabra
        show lenabra_phone
        with short
        l "Hi Robert. What's up?"
        show phone_robert at lef3
        with short
        r "Hey, you finally pick up! I called you yesterday but you ignored me..."
        l "I was probably sleeping when you called me. I was dead tired last night."
        r "I thought you'd call me back after seeing my missed call..."
        $ lena_robert -= 1
        show friend_down
        play sound "sfx/frienddown.mp3"
        l "I just woke up, Robert. What did you need? Is it something important?"
        hide phone_robert
        show phone_robert_smile at lef3
        r "It is. I want to see you!"
        r "You told me we could meet during the weekend, and it's already Sunday, so I guess we're meeting today!"
        l "You know I have to work tonight. They gave me six nights in a row..."
        r "I know, but we can still spend the afternoon together, even if it's just a few hours."
        if v2_robert_chance:
            r "You said you wanted to meet me again, didn't you?"
        elif v2_robert_home:
            hide phone_robert_smile
            show phone_robert_flirt at lef3
            r "We have some unfinished business, you and I, after all!"
            $ flena = "blush"
            l "That's true..."
        else:
            r "We had such a good time the other night, and I've been wanting to hang out with you again."
        r "Or do you have other plans already?"
        $ flena = "n"
        l "Not really..."
        r "It's settled then! I'll pick you up at five!"
        "It was as good as any other moment to meet Robert again. Maybe the best moment, considering my awful schedule this week."
        if v2_robert_chance:
            "And I had told him I was giving him another chance, after all."
        elif v2_robert_home:
            "And that night things were left unfinished, after all. Things had happened a bit too quickly, but this could be a good chance to see how things flowed between us now."
        else:
            "And after what happened that night it was in order meeting him again, seeing how things flowed between us."
        l "Alright, I'll see you at five."
        r "Awesome. See you later, babe!"
        hide lenabra_phone
        show lenabra
        hide phone_robert_smile
        hide phone_robert_flirt
        with short
        "This situation with Robert had me wondering."
        if v2_robert_home:
            "I would've had sex with him by now, if it hadn't been for that hiccup with the condom..."
            "It had been a while since I had slept with someone. But I was probably overthinking things."
            "What was so wrong about sleeping around with someone? As Ivy said, I should just do it and stop fretting about it."
            "Besides, Robert seemed like the perfect guy to do just that. I found him quite attractive and he liked me a lot."
            "Taking that step with him would help me turn the page once and for all. I couldn't keep sulking about my breakup."
        elif v2_robert_kiss:
            "He was the first guy I had kissed in quite some time. The first since Axel..."
            "Robert was interested in me, those cards were up on the table. But I still was on the fence about how to play things."
            "What was so wrong about sleeping around with someone? As Ivy said, I should just do it and stop fretting about it."
            "Besides, Robert could be just the perfect guy to do that. I found him quite attractive and he liked me a lot."
            "Taking that step with him would help me turn the page once and for all. I couldn't keep sulking about my breakup."
        elif v2_robert_chance:
            "Robert was interested in me, those cards were up on the table. But I still was on the fence about how I felt about him."
            "I had given him a second chance despite rejecting his advances on our first date. I wasn't sure why I'd done it."
            "Maybe I just needed some more time to warm up to things. Take one step at a time."
            "What was so wrong about sleeping around with someone? As Ivy said, I should just do it and stop fretting about it."
            "Robert was offering me that chance. I found him somewhat attractive and it was clear he liked me a lot."
            "Taking that step with him would help me turn the page once and for all. I couldn't keep sulking about my breakup."
        $ flena = "sad"
        if v2_ian_date:
            "Then again, things weren't so simple. Robert was not the only guy I was considering getting close to..."
            if v2_kiss:
                "That kiss Ian and me had shared had made clear the attraction we felt for each other."
                "I was still getting to know him, but I was really liking what I had seen so far."
                "It was too early to get any ideas, though. Still, it made me wonder if fooling around with Robert was something I should be doing..."
            else:
                "I had really enjoyed my date with Ian, but I wasn't sure about what the deal was with him."
                "Was he really interested in me? Was I?"
                if v2_almost_kiss:
                    "Though we had almost kissed, or so it felt to me... What seemed clear was that there was some kind of tension between us."
                    "What I wasn't clear about was if that was a tension I should explore."
                "He was an interesting guy, and pretty nice. But maybe I shouldn't expect things to progress further than a good friendship."
                "There was no reason to feel bad about fooling around with Robert, right?"                        
        "I wanted to move on, that much was clear. But Axel was still haunting me, and not just in memory."
        "My last argument with Mom was still fresh on my mind..."
        "What the hell was Axel doing showing up at my parents' place? Maybe I really should talk to him, just to tell him to stop it for good!"
        l "Ahhh, why can't I get a break? I just want to have it easy for a while!"        
        l "Agh, enough overthinking that stuff! I don't want to stress out during my free time!"
        l "I have plenty of things to think about as it is. A lot has happened during these past few days..."
        $ flena = "n"
        l "What should I do?"
        
    menu v3sunday:
        "Post to Peoplegram" if v3sundaypeoplegram == False:
            $ renpy.block_rollback()
            $ v3sundaypeoplegram = True
            "I hadn't uploaded anything to my Peoplegram since that last pic from Danny's photo-shoot."
            "I should keep it updated. As Ivy said, doing so was good business."
            "If I wanted to give a professional image I should put some effort into it."
            l "I don't have anything new to upload, though. My last photo-shoot was the one with Danny, so..."
            l "I guess I should pick another picture from the ones he sent me."
            if v2_photo_draw:
                "As I was looking through my phone I saw another picture I had taken."
                "It was the drawing Ian had made of me. It was pretty good..."
                "I had never posted something like that, but it felt quite in line with the artistic vibe I wanted my Peoplegram to have."
                l "I wonder if I should post this instead of a picture of myself..."
                menu:
                    "Post Ian's drawing":
                        $ renpy.block_rollback()
                        $ v3_pg_ian = True
                        "I liked the idea of posting something like that. Something different and artistic."
                        show lenabra at right
                        with move
                        show v3_peoplegram2
                        with short
                        l "I just have to crop it a bit and apply some filter... There."
                        "The nice thing about posting a drawing instead of a photo was that I didn't need to censor it."
                        "Having to paint over nipples in photos reminded me of those people painting over Michelangelo's work in the Sistine Chapel, covering the genitalia of all the figures..."
                        "Close-minded people and censorship had ruined so many great works of art. It all seemed so absurd."
                        if v3_check_stalkfap:
                            "I didn't need to do that in my Stalkfap account, though."
                        l "Morality is such a weird thing. A drawing is OK, but not a photo... Anyways."
                        l "There, posted."
                        l "I wonder if people will like it. I bet they will."
                        
                    "Post Danny's picture":
                        $ renpy.block_rollback()
                        $ v3_pg_danny = True
                        l "I think it's best to go with Danny's picture. It keeps things consistent... Besides, I don't have Ian's permission to use his drawing."
                        "People wanted to see my pictures, not drawings, after all."
                        show lenabra at right
                        with move
                        show v3_peoplegram1
                        with short
                        l "I guess I'll post this one. It's the one I like the most."
                        if v1_choosepic == 3:
                            l "And it is the one that got Danny so many good critiques at the gallery!"
                        l "I just have to edit it to censor my nipples..."
                        "Editing Danny's picture like that felt a bit like ruining his work."
                        "It reminded me of those people painting over Michelangelo's work in the Sistine Chapel, covering the genitalia of all the figures..."
                        "Close-minded people and censorship had ruined so many great works of art. It all seemed so absurd."
                        if v3_check_stalkfap:
                            "I was doing the same thing now, but I didn't need to in my Stalkfap account."
                        else:
                            "I was doing the same thing now, but it also served to protect my intimacy, somehow."
                        l "There, posted."
                        l "I hope people will like it."
            else:
                show lenabra at rig3
                with move
                show v3_peoplegram1
                with short
                $ v3_pg_danny = True
                l "I guess I'll post this one. It's the one I like the most."
                if v1_choosepic == 3:
                    l "And it is the one that got Danny so many good critiques at the gallery!"
                l "I just have to edit it to censor my nipples..."
                "Editing Danny's picture like that felt a bit like ruining his work."
                "It reminded me of those people painting over Michelangelo's work in the Sistine Chapel, covering the genitalia of all the figures..."
                "Close-minded people and censorship had ruined so many great works of art. It all seemed so absurd."
                if v3_check_stalkfap:
                    "I was doing the same thing now, but I didn't need to in my Stalkfap account."
                else:
                    "I was doing the same thing now, but it also served to protect my intimacy, somehow."
                l "There, posted."
                l "I hope people will like it."
            hide v3_peoplegram1
            hide v3_peoplegram2
            with short
            show lenabra at truecenter
            with move
            jump v3sunday
            
        "Check out Stalkfap" if v3_check_stalkfap == False:
            $ renpy.block_rollback()
            $ v3_check_stalkfap = True
            l "I guess it's time for me to really check out this Stalkfap thing..."
            "Ivy had sent me a link granting me free access to her content, but I had to create an account of my own first."
            "I did that."
            l "User name... \"Bluenightsky\", same as my Peoplegram nickname. There, it's done."
            "Logged into my own account I opened Ivy's profile and browsed through it."
            show lenabra at right
            with move
            show v3_stalkfap1
            with short
            "She had uploaded some uncensored pictures from her photo-shoots, but mostly sexy selfies."
            l "Seems like an easy way to earn money, that's for sure..."
            "I checked some of the comments on her last picture."
            $ flena = "worried"
            "\"{i}That booty! Has it seen a lot of action lately?{/i}\""
            "\"{i}O-la-la those are very nice tattoos. Any piercings in interesting places? I would love to play with them :P {/i}\"   "
            l "Oh my God, these are some really raunchy comments!"
            "The ones that followed were not mild either."
            "\"{i}Holy shiiit, you make me so hard babe{/i}\""
            "\"{i}Words can’t even begin to describe how badly I want to fuck you{/i}\""
            $ flena = "blush"
            l "Damn, they're horny and they're not hiding it..."
            "\"{i}You're fucking hot, but I'm not paying for stuff I could have seen on Peoplegram. Step it up!{/i}\""
            l "And demanding, too!"
            "\"{i}OMG can we see your pussy next??{/i}\""
            "\"{i}plz bb show butthole{/i}\""
            l "This one barely looks literate!"
            $ flena = "worried"            
            l "These are in a totally different tone than the ones my followers leave on Peoplegram..."
            l "Ivy's content is quite different from mine, though. I don't think I'd get that same kind of followers, or so I hope..."
            l "She's insisting on me getting on board with this Stalkfap thing, but I'm on the fence about it..."
            l "On one hand, it's not so different from what I already have on Peoplegram. I can keep posting my artistic nudes... Just uncensored."
            l "I've always said I'm not ashamed of my body and my art, after all."
            l "But I wonder if I'll feel comfortable exposing myself to that degree. I know people can be very judgmental... And horny."
            l "And this doesn't feel too \"artistic\", rather just... erotic."
            if lena_lust > 2:
                l "Not that there's anything wrong with that, of course."
            else:
                l "I guess there's nothing wrong with that, but... I'm not sure it's my thing..."
            l "What should I do?"
            menu:
                "Give it a try":
                    $ renpy.block_rollback()
                    $ stalkfap = True
                    $ flena = "n"
                    l "I could give it a try, why not?"
                    l "I'll be basically posting the same content that's on my Peoplegram. Just tasteful artistic nudes."
                    l "Let people think or say what they will, that only shows how close-minded they are."
                    hide v3_stalkfap1
                    show v3_stalkfap2
                    with short
                    if v3sundaypeoplegram:
                        if v3_pg_danny:
                            l "I'll post the same picture I just uploaded to Peoplegram..."
                            l "Only this time I don't have to censor it and ruin Danny's work."
                        else:
                            l "I'll post here the picture I was thinking about uploading to Peoplegram before."
                            l "Here I don't have to censor it... Doing so feels a bit like ruining Danny's work."
                    else:
                        l "I'll post this picture from Danny's photo-shoot."
                        l "Here I don't have to censor it... Doing so feels a bit like ruining Danny's work."
                    l "Now I need to let people know I have set up this account. I should post a link in my Peoplegram bio..."
                    l "{i}\"To see the unedited pictures subscribe to my Stalkfap account\"{/i}."
                    hide v3_stalkfap2
                    with short
                    show lenabra at truecenter
                    with move
                    l "There, all done."
                    l "Let's see how this goes. I can always delete it if I don't like the experience."
                    
                "I don't like it":
                    $ renpy.block_rollback()
                    l "I don't think this is for me..."
                    hide v3_stalkfap1
                    with short
                    show lenabra at truecenter
                    with move
                    l "I don't want to expose myself like that, monetizing my sex appeal."
                    $ flena = "n"
                    l "It's something better left to girls like Ivy. She owns it and takes good advantage of it."
            jump v3sunday            
            
        "Mr. Ward's proposal" if v3sundayseymour == False:
            $ renpy.block_rollback()
            $ v3sundayseymour = True
            "I thought about Friday's exhibition and the man I had met there, Seymour Ward."
            "He had expressed interest in working with me as a model, since he was getting into photography."
            "He was just doing it as a hobby though, and I didn't really like working with amateurs..."
            if lena_stan_model_free or lena_stan_model_cash:
                "I had made an exception with Stan, but just because he was a flatmate and a friend..."
            $ flena = "serious"
            "And it was quite typical: older men with money who are bored, buy an expensive camera and get into model photography."
            "But all they are truly after is getting close to young naked girls. It was quite a common phenomenon."
            "The pictures they took never saw the light of day, remaining a private trophy for them to stroke their ego to. And probably their dick, too."
            $ flena = "sad"
            "That man, though... Seymour Ward was someone intriguing. His presence couldn't be ignored, that was for sure."
            "But he had something rather unnerving about him. I couldn't put my finger on it, but being in front of him made me feel like..."
            "It was hard to describe. It was like something that feels somewhat dangerous but draws your attention at the same time."
            "Something... Thrilling?"
            $ flena = "n"
            "He had given me his card and told me to contact him if I was interested in his offer."
            "Should I do it?"
            menu:
                "Accept Seymour's offer":
                    $ renpy.block_rollback()
                    $ v3_seymour_call = True
                    l "Sure, why not? Work's work, and that's the reason I went to that exhibition, to find work."
                    l "Besides, he's supposed to be someone important and wealthy... I'm sure he pays good."
                    "I pulled out his card and looked up his contact info."
                    l "I guess I'll give him a call. It's Sunday, so he shouldn't be working."
                    hide lenabra
                    show lenabra_phone
                    with short
                    l "..."
                    $ flena = "sad"
                    l "... ..."
                    l "... ... ..."
                    "Just when I thought he wouldn't pick up, I heard his voice."
                    show phone_seymour at lef3
                    with short
                    mr "Yes? Who's this?"
                    l "Uh, it's me, Lena. We met this Friday at the exhibition."
                    hide phone_seymour
                    show phone_seymour_smile at lef3
                    mr "Oh, Lena, of course. I was expecting your call."
                    $ flena = "n"
                    mr "I take it you're interested in my offer?"
                    l "Yes, I am."
                    mr "Good. Let's schedule a meeting, then. When are you available?"
                    l "Let's see, this week... I'm free on Wednesday or Thursday afternoon."
                    mr "Lets make it Thursday, but at night."
                    $ flena = "worried"
                    l "At night? Isn't that a bit late for a photo-shoot?"
                    hide phone_seymour_smile
                    show phone_seymour at lef3
                    mr "I wasn't thinking about a photo-shoot. I'm very picky when it comes to the people I choose to work with."
                    mr "You gave me a good impression on Friday, but I want to know more about you before hiring you as a model."
                    mr "I want to make sure you're the right person for what I have in mind."
                    "What was he talking about? Make sure I was the right one?"
                    "He was just an amateur but he was acting like he was such a high-profile and important photographer."
                    l "So you want us to talk or...?"
                    mr "Let's meet for dinner. That way we'll be able to have some informal conversation and see if we can work together."
                    menu:
                        "Accept":
                            $ renpy.block_rollback()
                            $ v3_seymour_date = True
                            "It was the first time someone asked me to do a job interview to pose for them..."
                            $ flena = "n"
                            l "Alright, I guess..."
                            hide phone_seymour
                            show phone_seymour_smile at lef3
                            mr "Thursday night it is, then. You live in the city, right?"
                            l "Yeah, pretty close to the downtown area."
                            mr "Perfect, since I wanted us to meet there. I'm picking the restaurant."
                            mr "See you on Thursday. Thanks for your interest, Lena."
                            l "No, thank you."
                            hide phone_seymour_smile
                            hide lenabra_phone
                            show lenabra
                            with short
                            "So he wanted us to have dinner... That was unexpected, and unusual."
                            "I was well aware some men that hired models thought they were buying more than just a photo-shoot, but I hoped that wasn't the case..."
                            "Seymour didn't sound like someone so simple-minded, though that didn't guarantee anything. Cultured men could be big creeps, too."
                            "In any case I was intrigued. I had my doubts about his moral character, but one thing was sure: he was an intelligent and interesting man."
                            "He was arrogant and authoritative, too. Wanting to evaluate me..."
                            "Well, this dinner would serve me too as well. I would get the chance to know what kind of man he really was, and maybe then I would be the one not interested in working with him."
                            l "We'll see how that goes... It will be an interesting experience either way, it seems."
                            
                        "Refuse":
                            $ renpy.block_rollback()
                            $ flena = "serious"
                            $ v3_seymour_reject = True  
                            l "I'm sorry, but that's not how I work."
                            l "I thought you had already decided you wanted to work with me, but it's not my job to convince you if you're uncertain about that."
                            l "If you want me as a model I can give you references so you can judge the quality of my work, but I don't do dinners, or job interviews."
                            hide phone_seymour
                            show phone_seymour_serious at lef3
                            mr "Is that so? I thought you called me because you were interested in working with me."
                            l "I called to respond to your request, Mr. Ward."
                            l "And I'm sorry, but I'm not interested in doing business with you."
                            $ lena_seymour = 2
                            play sound "sfx/frienddown.mp3"
                            show friend_down
                            mr "So be it! I don't need to tell you how dumb it is to let this chance pass."
                            mr "I have the feeling you'll come to realize your mistake, and you'll come back to me on your knees."
                            l "Nice dream. Too bad it won't happen."
                            l "Have a good Sunday, Mr. Ward."
                            hide phone_seymour_serious
                            hide lenabra_phone
                            show lenabra
                            with short
                            "I hung up."
                            "I didn't know what he was expecting, but I didn't like his arrogance at all."
                            "It was clear he was used to everybody playing by his rules. But I wouldn't."
                            "I didn't want to have dinner with him. Too many men like him thought they were buying more than just a photo-shoot."
                            "I was a model, not an escort girl. He'd have to find someone else for that."
                            $ flena = "n"
                    
                "Ignore it":
                    $ renpy.block_rollback()
                    l "I don't think it's a good idea... I didn't really feel comfortable around him."
                    l "He'll have to find himself another model."
            
            jump v3sunday
        
        "Play guitar":
            $ renpy.block_rollback()
            "I didn't want to concern myself with anything else."
            "Ignoring everything and just spending my afternoon playing music sounded like a good plan..."
            if v3_robert_date:
                l "I have to meet Robert, so I should make good use of my time."
            menu:
                "Practice guitar":
                    $ renpy.block_rollback()
                    l "I'll do that!"
                    scene lenaroom
                    with long
                    "I got dressed, had a quick lunch and sat on the bed with my new guitar."
                    show lena_guitar1
                    with short
                    play sound "sfx/guitar.mp3"
                    "I strummed the strings and began going over the song I had written the other day, polishing it."
                    "My fingers remembered how to flow around the instrument the more I played."
                    "I was no great musician, but I was getting the melodies I wanted out of the guitar."
                    "All in all, I was having a great time, immersed in my own world of song and poetry, getting more comfortable in it."
                    play sound "sfx/xp.mp3"
                    show wits_up
                    $ lena_wits_xp += 1
                    call screen skillsup
                    if v3_robert_date:
                        "I would've spent even more time playing, but it was time for me to meet Robert."
                        jump v3robertsundayscene
                    else:
                        "When I looked at the clock again it was almost time for me to go to the restaurant again!"
                        jump v3iansundayscene
                "I should do something else first...":
                    $ renpy.block_rollback()
                    l "I'd like to do that, but I should take care of some other stuff first."
                    jump v3sunday
                    
        "Relax and rest":
            $ renpy.block_rollback()
            "I didn't want to concern myself with anything else."
            "Ignoring everything and just spending my afternoon resting, maybe even taking a long, relaxing bath..."
            if v3_robert_date:
                l "Before meeting Robert, that is."
            menu:
                "Take a bath":
                    $ renpy.block_rollback()
                    l "A bath sound like a great idea..."
                    hide lenabra
                    show lenanude2
                    with short
                    "I went to the bathroom, I latched the door and filled the bathtub with hot water."
                    l "I wish I had a few candles I could light... And one of those aromatic bath bombs!"
                    "I didn't have any of those fancy stuff, so a simple warm bath should do."
                    "I created some foam, put on some music on my phone and submerged myself, closing my eyes."
                    l "Ahhh... This is just what I needed!"
                    "These night shifts were quite stressful, and combining my work at the restaurant with the one at the café felt taxing for sure."
                    "Going to Ivy's classes was good to keep my body healthy, but so was making sure I gave it the rest it needed!"
                    play sound "sfx/xp.mp3"
                    show athletics_up
                    $ lena_athletics_xp += 1
                    call screen skillsup
                    "This way I would be full of energy to tackle tonight's work."
                    if v3_robert_date:
                        "I lingered in the bath until the water turned cold. When I got out it was almost time for me to meet Robert."
                        jump v3robertsundayscene
                    else:
                        "I lingered in the bath until the water turned cold. After that I felt so relaxed I decided to take it easy the rest of the afternoon before having to go to work."
                        jump v3iansundayscene
                        
                "I should do something else first...":
                    $ renpy.block_rollback()
                    l "I'd like to do that, but I should take care of some other stuff first."
                    jump v3sunday
    
##SUNDAY ROBERT DATE ##########################################################################################################################################################################################################    

## DATE

label v3robertsundayscene:
    
    $ v3robconvo1 = False
    $ v3robconvo2 = False
    $ v3robconvo3 = False
    
    stop music fadeout 2.0
    scene street2
    with long
    $ flena = "n"
    $ lena_look = 1
    $ frobert = "smile"
    $ robert_look = 1
    show lena at lef
    show robert at rig
    with short
    "Robert was waiting for me in the street, next to my place."
    play music "music/flirty.mp3" loop
    if v2_robert_home:
        scene street2
        show v2_robert2
        with long
        $ flena = "blush"
        $ frobert = "flirt"
        "He greeted me with a kiss on the lips."
        scene street2
        show lena at lef
        show robert at rig
        with short
        l "Oh."
        r "How are you, babe?"
        $ flena = "smile"
        l "Great, thanks..."
        $ frobert = "smile"
    else:
        r "Hey, there you are."
        l "Here I am, indeed."
    r "So, what you wanna do?"
    l "I haven't thought about anything... To be honest I don't have time for much."
    r "Hmm, I see... Well, let's just take a stroll and see if anything comes up. We can chat that way, too."
    l "Sure."
    "We started walking down the street towards the downtown area."
    r "How's your Sunday going so far?"
    l "I can't complain, I guess. Took care of a few things, relaxed..."
    r "Cool, cool. Mine's cool, so far. I woke up just recently, though. It was a bit crazy last night, ha ha."
    l "I got up pretty late today, too... Work was pretty intense."
    r "I see, yeah, weekends are always harder..."
    if v2_robert_kiss and v2_robert_reject == False:
        "The conversation was rather plain... Were we feeling awkward after the other night?"
        "I decided to make it a bit more interesting."
    else:
        "The conversation couldn't be more mundane and irrelevant... I had to bring up something interesting to talk about."
    menu v3robconvo:
        "What's your passion?" if v3robconvo1 == False:
            $ renpy.block_rollback()
            $ v3robconvo1 = True
            l "I have a question for you. What would you say is your passion?"
            $ frobert = "n"
            r "My passion? Huh, what a deep question... I need to think about it..."
            r "I don't know, I guess I like hanging out with the dudes, going out... Having fun and enjoying life in general."
            l "But what kind of fun are you passionate about?"
            r "I like partying, going to bars and clubs. Just hanging out with the dudes, as I said."
            r "Oh, and I also like traveling! I'm going on vacation in a few weeks!"
            l "Oh, really? Where to?"
            r "To a beach resort, with a friend of mine. To relax and have a good time."
            l "I would need that, too..."
            $ frobert = "smile"
            r "We can go together sometime. I like spending time with you, too, of course."
            r "You could say you're one of my passions, ha ha!"
            jump v3robconvo
            
        "Tell me about your dating life" if v3robconvo2 == False:
            $ renpy.block_rollback()
            $ v3robconvo2 = True
            l "So, Robert, tell me about your dating life."
            $ frobert = "sad"
            r "My dating life?"
            l "Yeah. Or does the subject make you uncomfortable?"
            r "Well, it's a strange question to ask... What do you want to know?"
            l "Have you had any serious girlfriends?"
            $ frobert = "n"
            r "A couple, yeah."
            l "For how long?"
            r "The first one around one year, but it was a long time ago. The second one lasted around six months or so... And we broke up almost a year ago."
            l "What happened?"
            r "We were in different points of the relationship, you know. She had her needs, I had mine... It was just not working out."
            l "I see. It's important to recognize when that's the case."
            r "Yeah. She's still resentful, though, but we stopped seeing each other long ago."
            l "So nothing serious during this last year?"
            r "No, not really... Just some sporadic things, you know how it goes..."
            l "And what are you looking for?"
            $ frobert = "sad"
            r "This is turning into a pretty serious interrogation, Lena..."
            l "You're right, I'm sorry. I was just curious."
            $ frobert = "n"
            jump v3robconvo
        
        "Do you know anything about my job's situation?" if v3robconvo3 == False:
            $ renpy.block_rollback()
            $ v3robconvo3 = True
            $ flena = "worried"
            l "Is there any news about that situation you told me about? About my job..."
            $ frobert = "n"
            r "Oh, that. No, not yet."
            r "I think the brass wants to have a reunion tomorrow. If they do I'll get summoned and I'll let you know about it."
            l "Alright... I've been a bit worried about it."
            $ frobert = "smile"
            r "I told you not to worry. I will make sure they don't fire you. I'm the head waiter, they'll listen to my opinion."
            $ flena = "n"
            l "Thanks, Robert."
            jump v3robconvo
            
        "Keep walking":
            if v3robconvo1 or v3robconvo2 or v3robconvo3:
                "Nothing else of interest came to mind..."
            else:
                "But nothing worth my interest came to mind."
            $ frobert = "n"
            $ flena = "n"
            $ renpy.block_rollback()
    
    scene street
    show lena at lef
    show robert at rig
    with short
    "We kept with our aimless stroll around downtown, making some small talk." 
    "We stopped at a red light, and I felt Robert's hand sliding across my hip."
    scene street
    show v2_robert2
    with long
    "I turned my head to look at him and I was met with a kiss."
    if v2_robert_chance:
        "That was unexpected...!"
        "He grabbed me with both hands and pulled me towards him, chest to chest, as he kissed me deeper."
        menu:
            "Kiss him back":
                $ renpy.block_rollback()
                "I wasn't completely sure if this was still a bit too soon for me but... Why not just give it a try?"
                "I was tired of feeling anxious and restless... I didn't want to keep resisting the situation."
                jump v3robertsundaykiss
                
            "Stop him":
                $ renpy.block_rollback()
                $ v3_robert_reject = True
                $ flena = "sad"
                $ robert = "sad"
                hide v2_robert2
                show lena at rig
                show robert at lef
                with short
                show robert at lef3
                with move
                with vpunch
                l "Robert, stop."
                "I pushed him away gently but decisively."
                $ frobert = "serious"
                r "What? I don't get you, Lena!"
                r "You told me to go slow last night, and I did."
                l "This is your idea of going slow?"
                r "Really? I'm not even allowed to kiss you? It's not like I'm asking you to have sex, it's just a simple kiss!"
                l "You don't really get it, that's true. That's exactly what \"going slow\" means!"
                r "That slow? Come on, I never imagined you'd be one of those!"
                $ flena = "mad"
                l "What do you mean \"one of those\"?"
                $ frobert =  "sad"
                r "Uh, I mean, one of those old-fashioned nuns that..."
                l "That won't put up on the first or second date just because you're horny?"
                l "If that's the case, yeah, I'm old-fashioned. Though I prefer to call that \"not letting myself be pushed around\"."
                $ frobert = "serious"
                r "Jeez, girl, you don't have to get worked up like that. That was not my intention."
                r "It's just a stupid kiss, let's not make a big deal out of it."
                l "If it's so stupid, I hope you don't mind not getting one. Ever."
                $ frobert = "mad"
                r "...!"
                r "You're right, I don't mind. Coming here today was a mistake."
                l "It sure was. Bye, Robert."
                r "Bye."
                hide robert 
                with short
                l "That guy...! Who does he think he is?"
                jump v3robertsundaywork
           
    else:
        "It was unexpected, but not unwelcome."
        "He grabbed me with both hands and pulled me towards him, chest to chest, as he kissed me deeper."
        jump v3robertsundaykiss
    
## KISS   
    
label v3robertsundaykiss:
    
    "I leaned my back against the wall while embraced by Robert, responding to his kisses."
    "We began making out for a few minutes right there in the middle of the street."
    "Robert's kisses became deeper, his breathing heavier, and his hands groped my flesh with desire."
    "He grabbed my ass as his tongue went crazy around my mouth."
    "He pressed me towards him, our bodies as close as they could be."
    "I could feel him moving his hips back and forth slightly and the hard bulge under his pants rubbing against my thigh..."
    if lena_lust > 1:
        "Things were getting really hot, and so was I..."
    else:
        "Things were getting really hot..."
    r "Lena, I want you..."
    stop music fadeout 2.0
    if v2_robert_home:
        $ frobert = "flirt"
        $ flena = "blush"
        scene street
        show robert at rig
        show lena at lef
        with long
        r "Hey... You still have an hour or so before needing to go to work, right?"
        "I took a look at the clock."
        l "Around forty-five minutes."
        r "I've made sure to buy some condoms this time, so..."
        r "Why don't we go up to your place and finish what we couldn't last night?"
        "He wanted to have sex now? Considering how little time I had we would need to rush it quite a bit..."
        menu:
            "Let's wait till we have more time":
                $ renpy.block_rollback()
                $ lena_robert_sex_late = True
                $ flena = "sad"
                l "Sorry, but not today, Robert."
                $ frobert = "sad"
                $ lena_robert -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                r "You don't want to? What's the problem?"
                l "I want to do it, but I don't want to rush it. Let's wait until we have more time."
                r "Oh, of course... I understand. And when will that be?"
                l "The soonest I'm free is Wednesday night..."
                r "You are, but I'm working Wednesday. Unless you don't mind waiting for me to get out, then I can come to your place again..."
                $ flena = "n"
                l "We can do that."
                r "I'd rather do it now, though... I'm afraid I'll be a bit tired right after work."
                l "You didn't seem tired at all last time."
                $ frobert = "smile"
                r "Yeah, that's true... You're so sexy I forget about being tired, ha ha."
                $ flena = "flirtshy"
                l "So, Wednesday night then."
                $ frobert = "flirt"
                r "I can't wait!"
                "We kept taking a stroll and chatting until it was time for me to go to work."
                jump v3robertsundaywork
                
            "{image=icon_lust.png}OK, let's do it" if lena_lust > 2:
                $ renpy.block_rollback()
                $ lena_robert_sex = True
                $ lena_robert_sex_early = True
                "I had very little time, but I was feeling quite horny..."
                "And I would've had sex with Robert already if it wasn't for us missing condoms. That problem was solved now, though."
                "I wanted to know what would've happened if we had done it that night."
                $ flena = "flirtshy"
                l "Alright, let's do it... But we'll have to be quick about it."
                "Robert grabbed my hand and put it on his crotch. I felt the bulge of his cock under his pants."
                r "Don't worry, I'm ready to go right away."
                $ flena = "flirt"
                l "Oh..."
                l "Let's go to my place, then..."
                jump v3robertsundaysex
                
    else:
        $ frobert = "flirt"
        $ flena = "blush"
        scene street
        show robert at rig
        show lena at lef
        with long
        menu:
            "You're going too fast!":
                $ renpy.block_rollback()
                $ v3_robert_reject = True
                "I retreated slightly."
                l "Wait, you're going too fast, Robert..."
                r "What's the matter? I'm noticing you're feeling the same as me..."
                l "I like you Robert, but I'm not sure to what extent yet..."
                r "Then why not discover it? Let's do it, Lena."
                "He pulled me towards him again. He was so fired up."
                "And I wasn't comfortable with it."
                $ flena = "serious"
                $ frobert = "sad"
                play sound "sfx/punchgym.mp3"
                with vpunch
                show robert at rig3
                with move
                l "Robert, stop."
                "I pushed him away gently but decisively."
                r "What? I don't get you, Lena!"
                r "You told me to go slow last night, and I did."
                l "This is your idea of going slow? Having sex on the second date instead of the first?"
                r "Come on, I never imagined you'd be one of those!"
                $ flena = "mad"
                l "What do you mean \"one of those\"?"
                $ frobert =  "sad"
                r "Uh, I mean, one of those old-fashioned nuns that..."
                l "That won't put up on the first or second date just because you're horny?"
                l "If that's the case, yeah, I'm old-fashioned. Though I prefer to call that \"not letting myself be pushed around\"."
                r "So that's how you see it? Like you'd be doing me a favor by having sex with me or something?"
                l "Right now, yes. Because you're the only one of us who wants it."
                r "If you don't want it then why the hell are you making out with me just now!?"
                l "To find out if there's any possibility I'd want to. And I just got my answer."
                r "And what's that answer?"
                l "Do you really need me to spell it out for you?"
                l "N{w=0.3}O{w=0.3}. Not a chance."
                $ frobert = "mad"
                r "It's clear coming here today was a mistake."
                l "It sure was. Bye, Robert."
                r "Bye."
                hide robert 
                with short
                l "That guy...! Who does he think he is?"
                jump v3robertsundaywork
                
            "I want you too":
                $ renpy.block_rollback()
                $ lena_robert_sex_late = True
                l "I want you too, Robert... But it's a bit too soon."
                $ frobert = "sad"
                r "Why? We both want it, so there shouldn't be any problem."
                l "It's just... I don't wanna rush it. I barely have fifty minutes before having to get to work."
                l "I need a more comfortable context, less pressure, you know...?"
                $ frobert = "n"
                r "But you want to do it?"
                l "Yes, I wanna try it..."
                $ frobert = "smile"
                r "Alright! Let's agree on a day then, OK?"
                r "When are you free? Wednesday?"
                l "Yes."
                $ frobert = "sad"
                r "Damn, I'm working Wednesday."
                $ frobert = "flirt"
                r "But I can come over once I finish. I'll try to get off as early as possible, so it won't be too late."
                $ flena = "shy"
                l "Wednesday... OK, that sounds good."
                r "Cool! That's a promise. I can't wait!"
                "We kept taking a stroll and chatting until it was time for me to go to work."
                jump v3robertsundaywork
                
## SEX

label v3robertsundaysex:
    stop music fadeout 2.0
    play sound "sfx/door_home.mp3"
    scene lenahome
    show lena at lef
    show robert at rig
    with long
    "We went upstairs and entered my flat, then went right to my bedroom."
    hide robert
    show robertunder at rig
    with short
    "Robert was so eager he started taking off his shirt even before getting there."
    r "Oh baby! This is gonna be great!"
    play music "music/sensual.mp3" loop
    play sound "sfx/door.mp3"
    scene lenaroom
    show lena at lef
    show robertunder at rig
    with short
    "Robert followed me into my room and closed the door behind us."
    hide lena
    show lenaunder at lef
    with short
    "I began taking off my clothes, too."
    $ frobert = "evil"
    "Robert directed a lascivious look my way and licked his lips before coming over and helping me remove my underwear."
    r "Yeah, take everything off..."
    hide lenaunder
    show lenanude2 at lef
    with short
    "Robert took out his wallet and a condom from a pocket before throwing his pants away."
    hide robertunder
    show robertnude at rig
    with short
    r "Mhh, here we go..."
    l "Come over here."
    scene lenaroom
    show v3_robert1
    with long
    $ flena = "flirt"
    $ frobert = "flirt"
    "We embraced and kissed again."
    "Our lips and tongues slid over each other's with wet passion as Robert's desirous hands squeezed my bare ass."
    "I felt his skin against mine, the heat of his body bleeding into mine..."
    "My sensitive nipples rubbed against his chest, sending tingles up my spine. And his erect cock also did, but against my belly."
    "His manhood was pressed against my body, trapped between our pubes. It was sliding back and forth slightly, pushed by Robert's hip movements."
    "I felt the head of his dick rub over my labia, trying to spread it, as our wet kissing continued..."    
    scene lenaroom
    show lenanude2 at lef
    show robertnude at rig
    with long
    "Robert cracked the condom open. His cock was as hard as it could possibly be, and he was eager to bury it inside of me."
    r "Ooof, baby, here we go..."
    menu:
        "{image=icon_lust.png}Just fuck me!" if lena_lust > 1:
            $ renpy.block_rollback()
            $ flena = "slut"
            "I was so damn horny at that point...!"
            "I hadn't had sex for months, and when I tried to we lacked condoms..."
            "But I was finally going to get it."
            "I looked Robert in the eye and licked my lips."
            l "Come on, fuck me already..."
            r "Damn!"
            jump v3sundaysexfast
            
        "{image=icon_lust.png}Let me suck you off" if lena_lust > 1 and v2_robert_bj:
            $ renpy.block_rollback()
            $ flena = "slutshy"
            $ v3_robert_bj = True
            $ lena_bj += 1
            l "Wait, let me suck you off before putting that on."
            $ frobert = "smile"
            r "Oh, really? Yes, of course, go ahead!"
            $ lena_robert += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            scene lenaroom
            show v3_robert3
            with long
            "I made Robert lay on the bed and I got between his legs."
            "His hard tool was eager and ready for my attentions."
            play sound "sfx/bj4.mp3"
            "When I slid my tongue up the shaft I felt Robert shiver."
            r "Oh, baby!"
            "I wanted to have sex with him but I felt I wasn't wet enough yet."
            "Last time I got pretty horny while sucking him off, and I felt like doing it again."
            "I enjoyed it."
            l "Mhhh.. Ahh..."
            r "Fuck baby, your mouth is crazy good."
            "As I kept sucking and savoring his dick I felt my excitement and the heat in my lower belly grow."
            "Robert was more than pleased with my blowjob, of course."
            "But we hadn't come here just for that."
            l "Let's do it, now..."
            r "Hell yeah. Get up."
            jump v3sundaysexfast
        
        "Let's do it slowly...":
            $ renpy.block_rollback()
            $ flena = "blush"
            l "OK, but let's go slowly..."
            r "Yes, of course, let me take care of it..."
            jump v3sundaysexslow
            
            
label v3sundaysexfast:
    scene lenaroom
    show v3_robert5
    show v3_robert5_slut
    with long
    "Robert positioned me on top of the bed to his liking."
    r "Yes, get on all fours..."
    "If that's how he wanted it that's how I was gonna give it to him. I was just so eager to feel his manhood inside of me!"
    "He finished adjusting the condom and slid the tip of his cock across my slit."
    l "Mhhh!"
    r "Oh yeah baby, I'm so hard...!"
    scene lenaroom
    show v3_robert6
    show v3_robert5_slut
    with long
    r "Hmmm, you're tight!"
    play sound "sfx/ah3.mp3"
    "I was, but I also was really wet, so his cock slid in without too much trouble."
    "I felt it pressing onward, filling me in a single motion."
    l "Ohhh..."
    r "Damn, baby... You're really excited, aren't you?"
    l "Fuck yeah..."
    "Finally, I had broken my dry spell... I was having sex for the first time since my breakup with Axel."
    "He began moving his hips back and forth at a light pace, taking it somewhat slow."
    l "Mh, yes... Just like that..."
    "Bit by bit my insides turned more comfortable for Robert, welcoming him and making room for his cock." 
    jump v3sundaysexend
    
label v3sundaysexslow:            
    scene lenaroom
    show v3_robert5
    with long       
    r "Here, get like this... yeah."
    "Robert put me on all fours on top of the bed and got behind me while finishing adjusting the rubber."
    l "What, like this...?"
    r "Yeah, this way it will be easier, trust me."
    "He slid the tip of his cock across my slit, preparing it."
    "It was finally going to happen. I was about to have sex for the first time since my breakup with Axel..." 
    scene lenaroom
    show v3_robert6
    with long
    "Robert began pushing it in slowly."
    play sound "sfx/ah3.mp3"
    r "Hmmm, you're tight...!"
    "I was a lot more excited and eager than last night, but I was somewhat hesitant, still..."
    "I wasn't as lubricated as I would've liked to, and that was making Robert's job a bit more difficult."
    l "Just a bit more, slowly..."
    r "Yeah..."
    "Thankfully he was taking his time and being considerate about it."
    "I felt his manhood penetrate me bit by bit, gaining half an inch of terrain with each thrust."
    r "Ahh, there, finally..."
    jump v3sundaysexend
    
label v3sundaysexend:
    scene lenaroom
    show v3_robert7
    with long
    "Robert began getting carried away, giving it to me faster each time."
    r "Oh Lena, oh yes..."
    r "I've wanted to do this since the first time I saw you at the restaurant...!"
    play sound "sfx/mh1.mp3"
    l "Mhhh...!"
    "His thrusts became harder as he pumped his hips hastily."
    "He fucked me fast and eagerly, his passion for me unbridled."
    "He was claiming my body, penetrating my sex, enjoying me..."
    "Having me on all fours at the end of his dick made Robert feel like he was in heaven, or so his groans told me..."
    r "Oh baby, oh baby, I'll cum any minute now!"
    "Right on time. If I wanted to be on time at work, we had to finish this business just about now."
    "But I hadn't gotten to cum yet..."        
    menu:
        "Hold on a bit longer!":
            $ renpy.block_rollback()
            $ v3_robert_orgasm = True
            "I hadn't gotten this far to be left unsatisfied."
            l "No, hold on a bit longer!"
            l "I don't want you to cum just yet."
            r "Alright baby... How do you want it?"
            scene lenaroom
            show v3_robert9
            with long
            "I made Robert change posture. He was now spooning me, our lower bodies still connected."
            "I felt his warm, sweaty chest on my back, his heavy breathing on my ear."
            r "You drive me crazy, Lena..."
            "His whisper made me shiver and fanned my fire. That's how I liked it..."
            "Robert kept pumping his hips, but this posture made him go at a slower pace. I liked it better..."
            l "Just like that... Ahh, don't go faster..."
            r "I don't need to... I'll cum like this, too..."
            "I wanted to cum, too! I wasn't gonna let this chance slip my hands, so I used them."
            scene lenaroom
            show v3_robert10
            with short
            $ lena_lust_xp += 1
            play sound "sfx/xp.mp3"
            show lust_up
            call screen skillsup
            "I moved my hand to my pussy, and caressed it."
            "My fingers quickly found my clit and began rubbing it."
            "A new and intense source of pleasure added to the sensation of Robert's cock penetrating me."
            "That could do it..."
            l "Don't stop Robert, keep that rhythm!"
            r "This is how you like it, babe? You touching yourself is so damn hot...!"
            "I kept masturbating myself while Robert gave it to me from behind. Pleasure was building up and beginning to overflow..."
            l "Yeah...! Mhhh!"
            "I was almost there...! Just a bit more...!"
            "I stimulated my clit at the right speed, with the right pressure, giving myself just what I needed."
            "That, plus the hot sensation of Robert's cock sliding in and out of my pussy, was enough to finally drive me to climax."
            play sound "sfx/orgasm1.mp3"
            l "Ahhh!"
            with vpunch
            "My hips and legs trembled as the orgasm shook me."
            r "You're cumming?"
            l "Y..{w=0.3}yes!"
            r "That's so hot! Oh God!"
            "Robert felt like he had no need to hold back anymore."
            "He let himself loose, penetrating me fast and hard."
            "His climax followed within seconds."
            r "Ohhhh! Oh, yeah!"
            with flash
            with vpunch
            "He grunted and tensed behind me as he ejaculated inside the condom."
            l "Ahhh..."
            "I tried to relax while I felt the orgasm wash over my body before fading."
            "I had done it."
            "I had finally fucked another guy. I feared it could've been terrible, but I ended up getting into it enough to even cum..."
            $ flena = "flirt"
            $ frobert = "smile"
            scene lenaroom
            show robertnude at rig
            show lenanude2 at lef
            with long
            stop music fadeout 2.0
            r "Whew... That was great... You liked it too, didn't you?"
            l "Yes, it was good..."
            $ flena = "surprise"
            l "Oh no, look at the hour! I'm already late!"
            r "We got a bit carried away back there, ha ha."
            $ flena = "n"
            "I picked up my clothes and began getting dressed."
            l "Quick, I should've left like ten or fifteen minutes ago!"
            r "I'm going, I'm going..."            
        "OK, cum!":
            $ renpy.block_rollback()
            "I hadn't gotten to cum, but it happening didn't seem likely, so..."
            "Better to get this over with and avoid being late to work!"
            l "Alright, cum!"
            r "Oh yes! Oh yes, baby!"
            "He let himself loose, penetrating me fast and hard."
            "His climax followed within seconds."
            r "Ohhhh! Oh, yeah!"
            with flash
            with vpunch
            "He grunted and tensed behind me as he ejaculated inside the condom."
            r "Ahhh..."
            "I had done it. I had finally fucked another guy."
            "I wasn't feeling completely comfortable with it yet, though... That was probably why I hadn't been able to relax and reach climax..."
            "I was kind of expecting it, to be honest."
            $ flena = "blush"
            $ frobert = "smile"
            scene lenaroom
            show robertnude at rig
            show lenanude2 at lef
            with long
            stop music fadeout 2.0
            r "Whew... That was great... Did you like it?"
            l "Yeah, it was... good."
            "Robert was too happy and satisfied to notice I was just being polite."
            r "We finally did it... This should've happened way earlier."
            l "It did when it did. Now let's get dressed... I will be late if we stall."
            r "I'm going, I'm going..."
    
## WORK

label v3robertsundaywork:
    stop music fadeout 2.0
    scene restaurant
    with long
    $ lena_look = 2
    show lenawork 
    with short
    if v3_robert_orgasm:
        $ flena = "drama"
        "I arrived almost half an hour late and I got scolded because of it."
        "There were a few minutes left before we opened to the public, but the other staff had to take care of setting up the tables in my place."
        "It wasn't a good track record, after the scene Axel caused last week..."
        $ flena = "sad"
        l "Well... Let's get to work..."
    else:
        $ flena = "n"
        "Once I arrived at the hotel I got changed and ready for another long night of work."
    if lena_robert_sex:
        $ flena = "blush"
        "I was left with a strange sensation after having just slept with Robert."
        "Not only because it had been my first time in a long time, but because it felt quite rushed."
        "I liked being able to stay in bed and relax with my partner after having sex. Share a quiet moment together, feeling close after the release..."
        "But I had to rush to work as soon as we finished fucking. I felt I was missing something."
        if v3_robert_orgasm == False:
            "Aside from an orgasm, of course..."
        "But it was done. Robert and I had taken our relationship to the physical level, this time for good."
        "I still wasn't sure how I felt about it... I didn't see him as a potential boyfriend, at least not yet. That much was sure..."
        "But I was interested enough to see how things unfolded. You could never know..."
    elif v3_robert_reject:
        $ flena = "serious"
        "Thinking about what had just happened with Robert made me frown."
        l "That asshole...!"
        l "I should never have agreed to go on a date with him. I had already had the feeling we wouldn't get along."
        l "Well, live and learn."
        "I had given it a try, but he was not the right guy, that much was clear."
        "The only thing that worried me was having to keep working with him..."        
    else:
        "As I got down to business I thought about Robert and how our relationship was evolving."
        "I felt I still barely knew him as a person, but I was interested in doing so."
        $ flena = "shy"
        "And I was interested in sleeping with him..."
        "My feelings for Robert weren't much more than a tentative interest at that point. I didn't see him as a potential boyfriend, at least not yet. Far from that..."
        "But we were close enough for me to explore my sexuality with him. To put an end to the dry spell I had been having since breaking up with Axel."
        "I wondered how I would feel... But I was eager to have sex once more."
        l "What's wrong with me, I'm even getting nervous... I'm not a teenager anymore!"
    jump v3lenasundaynight
    
##SUNDAY IAN TEXT ########################################################################################################################################################################################################## 

label v3iansundayscene:
    
    stop music fadeout 2.0
    scene streetnight
    with long
    $ flena = "sad"
    $ lena_look = 1
    show lena 
    with short
    "I made my way to the restaurant."
    l "Ahh... I wish I could stay home."
    if v2_ian_date:
        play sound "sfx/sms.mp3"
        $ flena = "smile"
        l "A message... Oh, it's Ian's."
        play music "music/date.mp3" loop
        i "{i}Hey, how's it going? Have you tried that new guitar yet? You looked pretty happy to get it!{/i}"
        "How nice. He had noticed my enthusiasm."
        if v2_lena_gohome:
            l "{i}Yes, I've been playing it quite a lot! Getting the hang of it again.{/i}"
        else:
            l "{i}Yes, I've been trying it out! Getting the hang of it again.{/i}"
        i "{i}I never asked you, but what kind of music do you like to play?{/i}"
        l "{i}Several styles... But I guess I mostly enjoy rock, especially indie, pop and blues... The softer styles, ha ha.{/i}"
        i "{i}So no heavy metal then, ha ha.{/i}"
        menu:
            "Depends on the style!":
                $ renpy.block_rollback()
                $ lena_metal = 2
                $ flena = "smile"
                l "{i}Well, you'd be surprised! It depends on the style, though.{/i}"
                l "{i}I'm not into the death metal stuff, but I like listening to progressive, and classic heavy metal is not bad.{/i}"
                l "{i}And when I was a teenager I loved gothic, ha ha...{/i}"
                i "{i}No way, you like progressive? It's my favorite style!{/i}"
                l "{i}I'm no expert or anything like that, but I listen to it from time to time.{/i}"
                i "{i}Wow, that's so cool. Most girls don't like metal for some reason, even though there are a lot of different and cool songs.{/i}"
                l "{i}People think metal is all noise and screaming... Though that still beats what they play in clubs and on TV. That music is really awful!{/i}"
                
            "Not really...":
                $ renpy.block_rollback()
                $ lena_metal = 1
                $ flena = "sad"
                l "{i}Not really... I like some songs, though, especially the classics and the ballads.{/i}"
                i "{i}That's cool! There aren't many girls who enjoy heavy metal, for some reason. Even if it's just the softer stuff.{/i}"
                $ flena = "n"
                l "{i}There are great songs to enjoy in every genre!{/i}"
                l "{i}Well, not in every genre... Most of the music they play in clubs and on TV is awful!{/i}"
               
            "Not at all":
                $ renpy.block_rollback()
                $ flena = "serious"
                l "{i}No, not at all! I can't listen to it.{/i}"
                i "{i}I thought so. Not many girls like metal, for some reason.{/i}"
                l "{i}Too loud and noisy and frantic! I don't like it at all.{/i}"
                i "{i}Such a shame... There's plenty of awesome songs!{/i}"
                $ flena = "n"
                l "{i}I'll let others enjoy those. Though I'd rather listen to metal than to the music they play in clubs and on TV. That one is really awful!{/i}"
                
        i "{i}I know, right? I hate commercial music nowadays... A few years ago it used to be good.{/i}"
        l "{i}You sound like an old man!{/i}"
        i "{i}I'm getting there, ha ha.{/i}"        
        if v3_pg_ian:
            i "{i}By the way, I saw your last post on Peoplegram.{/i}"
            $ flena = "shy"
            l "{i}Oh! Sorry about that, I should've asked your permission, right?{/i}"
            i "{i}No, not at all! If anything I'm surprised you decided to post it! The drawing wasn't that good to be honest.{/i}"
            l "{i}I liked it.{/i}"
            $ ian_lena += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            i "{i}I'm glad you did. Makes me wanna get into it again!{/i}"
            $ flena = "smile"
            l "{i}It's never too late, right?{/i}"
            i "{i}Sometimes it is... But I can try and practice some more!{/i}"
            l "{i}I'll let you know when I go back to one of those life drawing sessions if you want.{/i}"
            i "{i}Please do.{/i}"
        "I finally arrived at the hotel."
        l "{i}Ian, I'm gonna start my shift now, so I'm putting my phone away.{/i}"
        i "{i}Working on a Sunday night?{/i}"
        l "{i}Yeah... It sucks, I know.{/i}"
        i "{i}Stay strong! And let's hang out again soon.{/i}"
        l "{i}Yes! I'm super busy these days, but I'll let you know as soon as I have some free time.{/i}"
        i "{i}I'd like that.{/i}"
        stop music fadeout 2.0
        scene restaurant
        with long
        $ lena_look = 2
        $ flena = "smile"
        show lenawork 
        with short
        "That little unexpected chat had put a smile on my face."
        "Getting to work felt a bit less cumbersome that night."
        "I still wished I could've stayed home, or texted with Ian for a while longer..."
        jump v3lenasundaynight
        
    else:
        "There was no helping it, though. Sadly money didn't grow on trees."
        scene restaurant
        with long
        $ lena_look = 2
        show lenawork 
        with short
        "Once I arrived at the hotel I got changed and ready for another long night of work."
        jump v3lenasundaynight
        
##LENA NIGHT LOUISE ########################################################################################################################################################################################################## 

label v3lenasundaynight:
    
    $ flena = "sad"
    "This Sunday's night was almost as busy as Saturday's."
    "Thankfully tomorrow was Monday, so most people had to get up to go to work and they left a bit earlier."
    scene restaurant 
    with long
    $ lena_look = 1
    "After sending off the last customer I cleaned up and finally ended my shift."
    show lena
    with short
    l "Another day in the bag... Two more to go and I will be able to rest."    
    if v3_robert_date and v2_ian_date:
        "I pulled out my phone to look at the hour and I saw I had a text message from Ian."
        l "Oh! When was this...?"
        i "{i}Hey, how's it going? Have you tried that new guitar yet? You looked pretty happy to get it!{/i}"
        l "He wrote to me at half past seven in the afternoon. I was with Robert so I didn't see it..."
        "He had sent a second text at ten, while I was at work."
        i "{i}I never asked you, but what kind of music do you like to play?{/i}"
        "Both were unanswered, of course."
        l "He must think I'm ignoring him...! I'll write a quick reply..."
        l "{i}Hey Ian! Sorry, I've been caught up all afternoon and I'm just leaving work!{/i}"
        l "{i}I'm a mess, sorry! And yes, I'm loving the guitar! That visit at the record store only brought good things!{/i}"
        l "There..."
    l "Let's go home."
    scene street2night
    with long
    $ flena = "n"
    "I walked my way home, as I always did."
    show lena
    with short
    "All I wanted was to get into my bed and rest...!"
    $ flena = "surprise"
    show lena at rig
    with move
    show hobo at lef
    with short
    play music "music/danger.mp3"
    bum "Excuse me ma'am."
    "From the shadow of a corner this man suddenly planted himself in front of me."
    "My heart almost skipped a beat, startled by his approach. The night was silent and the streets lonely."
    $ flena = "worried"
    bum "Can you give me some spare change, please?"
    "He was clearly a bum. And he reeked of alcohol and other things I couldn't name."
    menu:
        "Run away!":
            $ renpy.block_rollback()
            $ lena_posh += 1
            "I stepped back. I didn't like the look of things. There was no way a man like that could have good intentions at this hour."
            "Better get away from that situation as quickly as possible!"
            show lena at right
            with move
            hide hobo
            with short
            "I avoided him and ran across the street, dashing to my home."
            "The bum looked surprised, but didn't make any effort of pursuing me."
            "I stopped running when I saw he wasn't following, but I kept a steady place until I reached my house."   
            
        "No, sorry":
            $ renpy.block_rollback()
            $ help_bum += 1
            $ flena = "sad"
            l "No, sorry..."
            "It seems like my answer didn't satisfy him enough to step aside."
            bum "Not a single coin? Come on, you must have something."
            l "I said no, so..."
            bum "I don't believe you."
            $ flena = "drama"
            l "Sir, I'm sorry, but I just want to get home now."
            "I tried to walk around him but he moved to block my path. I started to get really frightened."
            bum "You don't have to lie, you can just say you don't want to give anything to a rat like me."
            l "I... I just don't want to give you anything, I'm sorry."
            show lena at right
            with move
            hide hobo
            with short
            "This time he didn't try to stop me when I dashed past him and he didn't follow when I kept walking, almost running, until I got to my place."
            
        "Give him a few dollars.":
            $ renpy.block_rollback()
            $ help_bum += 2
            $ flena = "n"
            "I decided giving him what he wanted was the best thing to do. What were a couple of dollars, after all?"
            "And it was clear he needed them more than I did..."
            l "Here you go."
            "I put a couple of bills in his hand and he looked at them, then at me, then back at them."
            bum "..."
            hide hobo
            with short
            $ flena = "sad"
            "He turned around without saying a word and walked away. It seemed like my my contribution had worsened his mood instead of making him thankful..."
            if lena_wits > 2:
                "It would've been so petty of me expecting him to show happiness, though."
                "Who could feel happy having to beg for a couple of dollars in the street at this time of night?"
                l "Though saying \"thank you\" never hurts."
            elif lena_posh > 1:
                "Was he expecting more? He should be thankful I decided to give him anything..."
            else:
                "Maybe he was expecting more? But I gave him even more than he asked for..."
            "I also turned around and went back to my place."
            
    stop music fadeout 2.0
    scene lenahomenight_dark
    with long
    play sound "sfx/door_home.mp3"
    show lena
    with short
    if help_bum == 2:
        l "That was sad..."
    else:
        l "That was scary!"
    $ flena = "sad"
    l "I see more people like that in the streets each day."
    l "They say the city's economy, and the country's for that matter, is in bad shape."
    l "And homeless people like him are the tragic product of that..."
    "As I walked past Louise's room I heard a faint sound."
    $ flena = "worried"
    play sound "sfx/mh1.mp3"
    lo "Mh..."
    menu:
        "Go straight to your room":
            $ renpy.block_rollback()
            "Whatever was happening in that room, and I was pretty certain what it was, was none of my business."
            "Louise was entitled to her privacy and I was not going to violate it."
            jump v3lenasundaynightend

        "Get closer":
            $ renpy.block_rollback()
            "I just wanted to make sure. Could be that Louise was in pain, puking or something, and needed some help!"
            "I knew her periods could get really painful for her."
            "I moved closer to her door."
            
    scene v3_louise0
    with long
    "It was left ajar and I got to see a clear stripe, barely lit by the light from the living room, that revealed the action that was going on inside."
    "It was only a glimpse, some forms in movement I couldn't really recognize."
    "But what I did recognize was the motion itself, as well as the sounds."
    play music "music/sensual.mp3"
    "Louise was having sex with her mysterious boyfriend."
    "I then heard some faint words, whispered in a raspy voice."
    guy "Yeah, you know how I like it, baby..."
    lo "Yes, I do... Mhhh...!"
    menu:
        "Take a peek":
            $ renpy.block_rollback()
            $ v3_spy = True
            $ lena_lust_xp += 1
            play sound "sfx/xp.mp3"
            show lust_up
            call screen skillsup
            "My heart was racing in my chest. Its pulse pulled me closer and closer, until I couldn't bear to be kept in the dark."
            scene v3_louise1
            show v3_louise_door2
            with long
            "I pushed the door very slightly and got a peek of what was going on there."
            play sound "sfx/dp2.mp3"
            lo "Mhhh... Naahhh..."
            guy "Oh fuck, baby."
            "Louise was on top of the bed, on all fours, her mouth stuffed with a massive dick!"
            menu:
                "Focus on Louise":
                    $ renpy.block_rollback()
                    "I watched Louise's red lips spread to perfectly fit her lover's cock as she slid them across the shaft."
                    "Her naked, slender body in a submissive position, her boyfriend's hand on her head, guiding her motion..."
                    "It was like the scene of a porn, and my friend Louise was starring in it, shining with lust and beauty in front of her sexual partner." 
                    
                "Focus on that big dick!":
                    $ renpy.block_rollback()
                    $ lena_bdick += 1
                    "My eyes got locked on that big lump of hard meat. Probably the biggest I had ever seen."
                    "And I had seen big."
                    "It was long, thick and veiny, and its dark skin glistened with Louise's saliva."
                    "How greedily she devoured it."
                    
            "Before I realized my eyes got locked on that scene, my mind trapped and amazed at its sight."
            scene lenahomenight
            show v3_louise2_animation
            show v3_louise_door2
            with long
            "Louise's partner took the lead when he felt satisfied with her blowjob." 
            "He pushed Louise down to the bed, got behind her and penetrated her, all in fluid motion, without wasting time."
            play sound "sfx/oh1.mp3"
            lo "Ohhh!" with vpunch
            "I got startled by Louise's scream. It had been loud enough for everyone in the house to hear it."
            if lena_bdick > 0:
                "She couldn't contain her voice at all when her lover's enormous dick penetrated her. No wonder...!"
                "Before I could regain my senses, its sight captivated me against all reason once again."
                "That mammoth cock sliding in and out of Louise... How was she able to take all of that?"
                "I bit my lip."
                $ lena_lust_xp += 1
                play sound "sfx/xp.mp3"
                show lust_up
                call screen skillsup
                $ v3_spy_full = True
                "I couldn't help but keep watching, enthralled as I was."
            else:
                "She couldn't contain her voice at all when her lover's dick penetrated her."
                "I regained my senses. What the hell was I doing?"
                "I was spying on my flatmate having sex with her boyfriend!"
                "I was invading her privacy! I was acting like a creep!"
                menu:
                    "Keep watching":
                        $ renpy.block_rollback()
                        $ lena_lust_xp += 1
                        play sound "sfx/xp.mp3"
                        show lust_up
                        call screen skillsup
                        $ v3_spy_full = True
                        "But I just couldn't avert my sight."
                        "What was playing before my eyes had me captivated, enthralled."
                        
                    "Go to your room":
                        $ renpy.block_rollback()
                        stop music fadeout 2.0
                        scene lenahomenight_dark
                        $ flena = "blush"
                        show lena2
                        with short
                        "I backed away. What I was doing was wrong."
                        "I shouldn't be peeping on Louise like that. I was acting like a total creep!"
                        "If she caught me I couldn't look her in the eye anymore..."
                        "I decided to sneakily go to my room and leave them to their business."
                        "Too little, too late, though... My eyes had seen plenty and I had succumbed to temptation."
                        jump v3lenasundaynightend
            
            "Louise's boyfriend pressed his body down on hers, sinking Louise on the bed each time he pounded her."
            "Her delicate hands grasped the bed sheets in a tight clench as she endured his thrusts, her mouth wide open."
            "By the moans she was letting out I couldn't tell if she was in pain or pleasure. Probably a mix of both."
            "The guy's breathing mixed with Louise's as he began to pant, a sound punctuated by the slaps of his hips against Louise's flesh."
            "I was pretty sure I would've have heard them perfectly even if I was in my room. They were barely holding back."
            "Finally Louise's boyfriend tired himself out in that position and instructed her to change."
            guy "Come here, baby."
            scene lenahomenight
            show v3_louise3_animation
            show v3_louise_door2
            with long
            "Louise followed eagerly. In a heartbeat she was on top now, her lover's cock sliding into her."
            play sound "sfx/ah5.mp3"
            if lena_bdick > 0:
                "I couldn't believe my eyes. Her pussy dilating and making way for that big black dick..."
                "That gargantuan lump of meat that was penetrating her..."
                "The only way to describe how Louise was taking that thing in was to say she was devouring it."
                "I couldn't avert my eyes from that sight, following with my pupils the back and forth motion of that massive dick..." 
                "The way he penetrated my friend, the lewd sounds she was making... I was seeing and hearing everything."
            else:
                "Oh no! I had the most explicit angle possible in that position!"
                "I shouldn't be seeing that! Yet I was...!"
                "Louise's most private parts, her butt cheeks spread apart giving way to her boyfriend's cock...!"
                "The raunchy motion of her hips and the lewd sounds she was making... I was seeing and hearing them all."
            "I was violating Louise's utmost privacy yet I couldn't make myself look away."
            guy "Fuck baby, keep moving like that and I'll cum!"
            lo "Yes!"
            "Her yes sounded wild and hungry."
            lo "Yes baby, cum for me!"
            "I became aware of that fact only then: they were doing it bareback!"
            "The voice of the guy tensed."
            guy "Yes baby, I'm almost there...!"
            lo "Yes, give it to me baby! Give it to me, please!"
            play sound "sfx/ah4.mp3"
            lo "Ahhhh!!{w=1}{nw}"
            scene v3_louise3
            show v3_louise3cum
            with flash
            with vpunch
            pause 0.5
            with vpunch
            pause 0.5
            with vpunch
            pause 0.5
            "He grunted loudly and I could see how he arched his back and pushed his hips upwards, staying like that while trembling."
            "Unloading inside her."
            if lena_bdick > 0:
                "What a thick and plentiful cum a cock like that had to have...!"
                "And indeed, it did. Streaks of jizz gushed out of Louise's pussy, sliding down that thick shaft."   
            else:
                "Streaks of sperm gushed out of Louise's pussy, sliding down the shaft." 
            l "Oh my God..."
            "I couldn't avoid a whisper while seeing that scene. Thankfully those two were way too riled up to be able to hear anything."
            lo "Oh yes, oh yes baby... Give me everything..."
            "He grunted again."
            guy "{i}\*Uhhn...\*{/i} Oh, man..."
            stop music fadeout 2.0
            scene lenahomenight_dark
            $ flena = "blush"
            show lena2
            with short
            "I saw Louise jump off the bed and I backed away."
            "Was she going to the toilet for towels right now?"
            "My heart skipped a beat. What if she opened the door and saw me peeping?"
            "I had to get out of there!"
            show lena2 at left
            with move
            "Being less stealthy than one should I jolted towards my room and hid in the darkness, but leaving my door open."
            play sound "sfx/door.mp3"
            $ flousie = "flirt"
            hide lena2
            show louisenude
            with short
            l "So close...!"
            "I had been wise to trust my instincts there. If I had been caught..."
            "I couldn't have looked Louise in the eye anymore!"
            scene lenahomenight_dark
            with long
            "When she went back to the room and closed the door, I also closed mine, slowly, trying not to make any sound."
            jump v3lenamonday
            
        "Go to your room":
            $ renpy.block_rollback()
            stop music fadeout 2.0
            "Peeping would mean violating Louise's utmost intimacy."
            "She was having some private time with her boyfriend and I had no right to dig my nose into that."
            "I wouldn't act like a creep!"
            "I turned around and went to my room, feeling I was doing the right thing."
            "But the temptation had been real, and the curiosity was still there..."
            jump v3lenasundaynightend
            
label v3lenasundaynightend:

    stop music fadeout 2.0
    scene lenaroomnight
    if v3_spy:
        $ flena = "blush"
    else:
        $ flena = "worried"
    with long
    play sound "sfx/door.mp3"
    show lena
    with short
    "I closed the door to my room and decided to go to sleep."
    hide lena2
    show lenabra
    with short
    play sound "sfx/meow.mp3"
    show lola at lef
    with short
    "Lola jumped on the bed as I got in, eager to cuddle next to me."
    l "Yeah, don't be impatient..."
    play sound "sfx/oh1.mp3"
    with vpunch
    lo "Ohhh!"
    $ flena = "blush"
    "I got startled by Louise's scream. It had been loud enough for me to clearly hear it from my room."
    "I could hear the faint noise of moans and flesh slapping against flesh."
    l "Oh, God... They're not holding back, are they?"
    "By the moans Louise was letting out I couldn't tell if she was in pain or pleasure."
    l "I guess I'm using earplugs tonight..."
    jump v3lenamonday
    

##LENA MONDAY ########################################################################################################################################################################################################## 

label v3lenamonday:
    
    $ day = "Monday"
    $ week = 3
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    if v2_lena_stan_model_shirt:
        $ lena_look = 2 
    else:
        $ lena_look = 1
    $ flena = "n"
    show lenabra 
    with short
    if v3_spy:
        $ flena = "sad"
        "I didn't know how I would face Louise after what I had done last night..."
        "Fortunately she had no idea, so I should just try to play it cool."
        "And luckily it was Monday and she always left early to go to class and work on finishing her thesis."
        $ flena = "n"
    else:
        "I didn't know how to face Louise today after what I had heard last night..."
        "Luckily it was Monday and she always left early to go to class and work on finishing her thesis."
    "I could go to the kitchen and make some breakfast peacefully."
    play music "music/normal_day.mp3" loop
    play sound "sfx/door.mp3"
    scene lenahome
    show lenabra
    with short
    "I got out of bed and went to make myself a coffee and some toast."
    show lenabra at rig3
    with move
    l "..."
    $ jeremy_look = 2
    $ fjeremy = "smile"
    show jeremynude at lef3
    with short
    guy "Hey, good morning."
    $ flena = "surprise"
    with vpunch
    l "Oh!"
    "I got startled seeing a stranger appear in my living room all of a sudden."
    guy "Oh, sorry, I scared you! I'm Louise's boyfriend, Jeremy."
    $ lena_jeremy_agenda = True
    $ flena = "worried"
    "He extended a hand and I shook it."
    if v2_lena_stan_model_shirt:
        "He didn't seem to be acknowledging or reacting to me being only in my underwear."
        "Maybe I should cover up... But cover up with what?"
    l "I wasn't expecting anybody to be here at this hour... I mean, Louise already left, didn't she?"
    j "Yeah, she told me I could sleep in and help myself to some breakfast before leaving."
    show jeremynude at lef
    with move
    j "So, if you don't mind... Can you hand me a cup?"
    j "And do you have any avocado? I can make you a toast, if you make me a coffee."
    menu:
        "OK, make me a toast":
            $ renpy.block_rollback()
            $ v3_breakfast_jeremy = True
            $ flena = "smile"
            l "Sure, make one for me. Here."
            "I hurled him an avocado and he caught it."
            $ fjeremy = "happy"
            $ lena_jeremy += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            j "Cool!"
            show lenabra at rig
            with move
            "We began preparing breakfast one next to the other."
            "So this was Louise's boyfriend I had been hearing about so much. Jeremy..."
            "He was tall, with broad shoulders and long arms. And didn't seem to find it necessary to wear a shirt."   
            if v3_spy:
                $ flena = "blush"
                "I had seen much more of him last night, of course..."
                "I couldn't avoid blushing remembering it."
                j "What's up?"
                l "O-{w=0.3}oh, no, nothing. The coffee's almost done..."
            else:
                "He didn't seem shy at all."
            $ flena = "n"
            $ fjeremy = "smile"
            j "Here, I hope you enjoy my famous avocado toasts! Nothing better to start a day healthy and with energy!"
            l "They can not be so famous if I haven't heard about them before..."
            j "Hey, you just did. And now you know about them, and are about to taste them. Famous enough for me!"
            $ flena = "smile"
            l "Ha ha. Thanks."
            "We began having breakfast."
            
        "We don't have avocado":
            $ renpy.block_rollback()
            "So this was Louise's boyfriend I had been hearing about so much. Jeremy..."
            "He was tall, with broad shoulders and long arms. And didn't seem to find it necessary to wear a shirt."   
            if v3_spy:
                $ flena = "blush"
                "I had seen much more of him last night, of course..."
                "I couldn't avoid blushing remembering it."
                j "What's up? Am I bothering you?"
                l "N-{w=0.3}no. I'll just wait for this coffee to be done and I'll take it to my room..."
                j "Don't worry about me, I'll be done and out in a flash."
            else:
                j "Oh, sorry, am I bothering you?"
                "I tried to be polite."
                l "No... I'll just wait for this coffee to be done and I'll take it to my room."
                j "Don't worry about me, I'll be done and out in a flash."
        
    if lena_jeremy > 3:
        j "So you're Louise's flatmate. Are you friends?"
        l "Yeah, we met at college before living together."
        j "I see, I see. And there's also a dude living here, right?"
        l "Yes, Stan."
        j "Louise, Stan... I know everyone's name but yours! You haven't told me yet."
        l "You haven't asked."
        j "Come on, don't make me beg for it."
        l "I'm Lena."
        j "Nice to meet you, Lena..."
        
    if v2_showlena_jeremy:
        if lena_jeremy > 3:
            $ fjeremy = "n"
            j "..."
            $ flena = "worried"
            j "Lena, huh..."
            l "What?"
        else:
            $ fjeremy = "n"
            "Just as I picked up my coffee and I began walking to my room he called me out."
            j "Wait, uhm..."
            l "Lena. Do you need something?"            
        j "You look familiar..."
        l "What, me?"
        j "Yeah, I've been having that feeling for a few minutes now... Where have I seen you?"
        l "Well, we've never met before, so maybe you saw me on Peoplegram or..."
        $ fjeremy = "happy"
        j "Yes, that's it! Peoplegram!"
        j "You're that model Ian told me about!"
        $ flena = "surprise"
        l "What? You know Ian? And he told you about me?"
        j "Yeah, we're buddies! He told me he had met a stunning model and showed me your Peoplegram!"
        $ flena = "n"
        l "Oh. I see. Small world, isn't it...?"
        j "Yes, it is. To think you are Louise's flatmate, what a crazy coincidence! Ian won't believe me when I tell him."
        $ flena = "serious"
        "So Ian told Jeremy he had met a \"stunning model\" and even showed him my Peoplegram... Why? To boast?"
        if ian_lena > 2:
            $ ian_lena -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
        "Was that how he saw me, like a \"model\" he had met?"
        $ flena = "n"
        if lena_jeremy < 4:
           l "Anyways, I'm going to my room. Enjoy your breakfast."
           j "Thanks!"
            
    if lena_jeremy > 3:
        j "Well, thanks for the breakfast and for the chat. I should get going."
        l "Yeah, I have to go to work soon, too."
        j "You're such a nice girl, Lena! It's been a pleasure to meet you. See you around!"
        l "Bye!"
        hide jeremynude
        with short
        "He went back to Louise's room, picked up his things and left."
        "What a curious individual Louise's boyfriend was..."
    else:
        scene lenaroom
        show lenabra
        with short
        "I went back to my room and I left Jeremy to his own devices."
        "What a curious individual Louise's boyfriend was..."
        "He finished his breakfast quick enough and I heard him leave the house. Soon after I left for work myself."
        
## CAFE
    stop music fadeout 2.0
    scene street
    with long
    $ flena = "n"
    $ lena_look = 1
    show lena
    with short
    "While I was walking to the café my phone rang."
    play sound "sfx/ring.mp3"
    $ flena = "serious"
    "It was Mom."
    "I was still mad at her and the last thing I wanted or needed was to argue with her on the phone right before work."
    "I had no desire to pick up, so I let it ring until it stopped."
    "I would need to talk to her at some point, but not today."
    if v3_robert_date:
        play sound "sfx/sms.mp3"
        $ flena = "n"
        "I still had the phone in my hand when I received a text message from Ian."
        "He was answering the text I had sent him at night."
        i "{i}Working on a Sunday night? That really sucks!{/i}"
        l "{i}Yeah, I know. And now I'm heading to the café...{/i}"
        i "{i}I was going to ask you if you wanted to hang out soon, but I don't know if I should seeing how busy you are!{/i}"
        l "{i}Sorry, I'm super busy these days! But let's hang out, I'll let you know as soon as I have some free time.{/i}"
        if v3_pg_ian:
            i "{i}By the way, I saw your last post on Peoplegram.{/i}"
            $ flena = "shy"
            l "{i}Oh! Sorry about that, I should've asked your permission, right?{/i}"
            i "{i}No, not at all! If anything I'm surprised you decided to post it! The drawing wasn't that good to be honest.{/i}"
            l "{i}I liked it.{/i}"
            $ ian_lena += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            i "{i}I'm glad you did. Makes me wanna get into it again!{/i}"
            $ flena = "smile"
            l "{i}It's never too late, right?{/i}"
            i "{i}Sometimes it is... But I can try and practice some more!{/i}"
            l "{i}I'll let you know when I go back to one of those life drawing sessions if you want.{/i}"
            i "{i}Please do.{/i}"
            i "{i}Anyways, good luck with your day today!{/i}"
        else:
            i "{i}That'll be cool. Good luck with your day today!{/i}"
        l "{i}Talk to you soon!{/i}"
    
    scene cafe
    with long
    show lena at rig
    with short
    l "Good morning."
    show molly at lef
    with short
    mo "Good morning, Lena."
    $ flena = "smile"
    l "Oh, Molly! You're feeling OK again?"
    mo "Yeah, I think so. Sorry for making you take care of all the work these days..."
    l "Don't apologize! It's not your fault, and taking care of your health is the most important thing. Are you sure you're fit to work?"
    mo "Yes, I'm fine! It's just the ailments of age, you know."
    mo "Ah, youth, such divine treasure! Be sure to enjoy it now that you have it!"
    $ flena = "sad"
    l "I'm trying..."
    $ fmolly = "sad"
    mo "I can tell by looking at you that you seem to be going through a difficult moment."
    mo "In fact, I had that feeling since we hired you..."
    l "Oh..."
    mo "Maybe it's none of my business, but if you need someone to talk to I'm here, Lena."
    $ fmolly = "n"
    mo "I don't know if I can help you, but I'd be happy to listen to you if you feel the need to share your burden."
    menu:
        "Tell her about your problems":
            $ renpy.block_rollback()
            $ v3_talk_molly = True
            "Ms. Van Dyke was so lovely and nice. I felt she was being sincere and that I could talk to her."
            l "Well, a lot has been happening lately. And a few days ago I got in a fight with my mom..."
            $ fmolly = "sad"
            "I told her about my situation with Axel, the recent developments and my phonecall with Mom."
            mo "I see... Relationships can be very complicated. I'm sorry you're having to go through this."
            $ flena = "serious"
            l "Yeah, and my mother seems unable to understand that."
            mo "What she did was wrong, but you have to understand she doesn't see it that way."
            l "I understand that, the one who has trouble understanding me is her!"
            mo "It's hard when the child is wiser than the parent... I've never had children, but I know what a mother's love is like."
            $ flena = "sad"
            mo "You must know she loves you and only wants the best for her daughter."
            l "Sometimes it doesn't seem like it..."
            mo "That's because she's very worried about you and wants to protect you. But she only knows how to do it that way."
            mo "It seems she's very set on her ways and has trouble seeing things from your perspective."
            l "Yes, that's it exactly...! She thinks the only right way to go about things is her own!"
            mo "That's a mistake she's guilty of, yes. But do you know what causes it?"
            l "What?"
            mo "Fear."
            mo "She's very worried about you, being so young, living on your own, working so hard..."
            mo "If you could make her feel at ease, communicate better with her, maybe she would relax and you'd have an easier time making her see things your way."
            l "That sounds like really wise advice... But I don't know if I can do that..."
            $ fmolly = "n"
            mo "It's worth trying at least, don't you think?"
            play sound "sfx/friendup.mp3"
            show friend_up
            $ lena_molly += 1
            $ flena = "smile"
            l "Thanks, Molly. I really appreciate what you've told me."
            l "I can't believe you never had children, because you're an amazing mom."
            mo "I'm glad I was able to help you a bit. You're a great girl, Lena. You deserve to be cared for."
            "I couldn't avoid giving Molly a hug. She was so tender and lovely!"
            $ flena = "n"
            l "Thank you so much. Well, shall we get to work?"
            mo "Sure!"
            
        "Avoid talking about it":
            $ renpy.block_rollback()
            $ flena = "n"
            l "Don't worry, I'm OK."
            mo "Alright. I don't want to bother you..."
            l "I appreciate your gesture, thanks, Molly. But I'm here to work, so let's get to it."
            $ fmolly = "n"
            mo "Sure."
    play music "music/normal_day.mp3"
    scene cafe
    show lenawork
    with long
    "It was another slow day at the café."
    "Good thing was it was much more relaxed than my night job at the restaurant. The place was much cozier and work much less stressful."
    "If I could get by with just this job it would be great... But things weren't so easy."
    "Early in the afternoon a familiar face came to visit."
    show lenawork at rig
    with move
    $ fholly = "smile"
    $ flena = "smile"
    show holly2 at lef
    with short
    l "Nice to see you, Holly!"
    h "Hi, Lena. Could I get a coffee?"
    l "Of course, I'll bring it to you right away."
    "Holly took a seat and put a couple of notebooks on top of the table."
    l "Here you go. Have you come here to write again today?"
    h "Yeah, I like it here. It's really peaceful."
    l "I won't bother you then."
    $ fholly = "shy"
    hide holly2
    show holly3 at lef
    with short
    h "Oh, you don't bother me at all... I like talking with you."
    l "Oh, really?"
    h "Yeah, you are very kind and I feel at ease talking with you. And that doesn't happen often..."
    $ flena = "shy"
    l "I'm flattered..."
    h "It's just that... As you can see I'm not too good with people. They are generally nice to me, but for some reason I just can't get along with them..."
    $ flena = "n"
    l "Sometimes it is difficult finding people you can feel comfortable around of, especially if you're shy."
    if v1_alisonlunch == False:
        l "You seem to get along with Ian pretty well, though!"
        $ fholly = "blush"
        h "Uh, w-{w=0.3}well that's..."
        "She got visibly flustered."
        if v2_kiss:
            l "He's really nice, isn't he?"
            $ fholly = "shy"
            h "Yes, he is."
        h "He's different from most people."
        $ flena = "smile"
        l "Yeah, he gives that impression alright."
        h "I mean, from most people at the magazine..."
    else:
        h "I thought maybe I could meet people like that at the magazine, but it seems it hasn't been the case..."
        h "The boss seems to love me, and there's this guy who I think is pretty nice, but still..."
        $ flena = "surprise"
        l "Wait, you work at a magazine? A literature one just around the corner?"
        $ fholly = "n"
        h "Yes. You know about it?"
        l "I know someone who works there. His name's Ian, do you know him?"
        $ fholly = "blush"
        h "I... I do, yeah..."
        $ flena = "smile"
        h "You two are friends?"
        "I told her how I had met Ian a couple of weeks ago."
        $ fholly = "n"
        h "Oh, I see... What a coincidence."
        l "You have no idea... I just found out this morning my flat mate's boyfriend is also a friend of his..."
        l "Seems like everybody in this town knows him!"
    $ flena = "n"
    l "So how's work at the magazine? Ian tells me he doesn't really like it..."
    $ fholly = "sad"
    h "Oh, that... He and the boss don't really get along."
    if ian_switch_review or ian_honest_review:
        h "In fact they just had a big fight at the office... It was pretty horrible."
        $ flena = "worried"
        l "Really? What happened?"
        h "There were some... irregularities regarding Ian's review."
        if ian_switch_review:
            $ fholly = "blush"
            h "And I have to admit I was involved in them."
        $ flena = "sad"
        l "Oh."
        $ fholly = "sad"
        h "But you should ask him, he'll tell you the story..."
    else:
        h "He says she has something personal against him..."
        l "Does she?"
        h "I'm not sure, but I'm starting to think he really has a point..."
        l "Poor Ian..."
    $ fholly = "smile"
    h "Anyways, don't let me keep you from your duties!"
    l "It's me who's keeping you from writing! Sorry."
    $ fholly = "blush"
    h "Not at all..."
    h "I told you I like talking to you..."
    h "T-{w=0.3}that's one of the reasons I came here, too..."
    $ flena = "shy"
    "Oh, she was so cute!"
    "Poor thing. It was clear she'd love to ask me to hang out but was so shy she wouldn't dare." 
    "I decided to make it easier for her."
    $ flena = "happy"
    l "I feel flattered! I enjoy talking to you, too, as you might've noticed."
    if v2_holly_song:
        l "And I told you I would show you one of my songs, right?"        
    else:
        l "And I already asked you to meet some time for you to tell me about your books and stuff, right?"
    l "I'd say we have a date."
    $ fholly = "happyshy"
    h "Y-{w=0.3}yes, that's true."
    l "When is it good for you?"
    h "Maybe... Wednesday afternoon?"
    l "That's perfect. It's finally my day off, so let's meet when I'm done with my shift at the café."
    h "Alright. I'll wait for you at the door."
    $ flena = "smile"
    if v2_ian_date:
        $ v3_ian_date = True
        l "Do you think we should tell Ian to join us?"
        $ fholly = "n"
        h "Oh... Yeah, of course."
        "She seemed a bit nervous all of a sudden."
        l "OK, I'll text him later."
    else:
        menu:
            "Tell Ian to join in":
                $ renpy.block_rollback()
                $ v3_ian_date = True
                l "Do you think we should tell Ian to join us?"
                $ fholly = "n"
                h "Oh... Yeah, of course."
                "She seemed a bit nervous all of a sudden."
                l "OK, I'll text him later."
                
            "Don't bring Ian":
                $ renpy.block_rollback()
                "I felt it would be better if Holly and me met without Ian."
                "I was curious to spend some time just with her, and she'd probably feel more comfortable opening up."

    l "Well, I'll leave you to your writing! We'll talk more on Wednesday!"
    $ fholly = "happyshy"
    h "Yes."
    stop music fadeout 2.0
    scene cafe
    with long
    "I ended my shift and got ready for another night at the restaurant."

# RESTAURANT

    scene restaurant
    $ flena = "n"
    $ lena_look = 2
    $ robert_look = 2
    with long
    show lenawork at rig
    with short
    l "Come on Lena, just two more nights and then you're free."
    if v3_robert_reject:
        $ frobert = "serious"
        show robert at lef
        with short
        "Robert didn't even talk to me the whole night."
        "Better that way, I had no desire to have him close after Sunday's disastrous date."
        hide robert
        with short
    elif v3_robert_date:
        $ frobert = "smile"
        show robert at lef
        with short
        r "Hey baby."
        "Robert appeared from behind and put his hand on my waist."
        l "Hey, Robert."
        if lena_robert_sex:
            $ flena = "blush"
            r "Yesterday was amazing. I can't wait to have you again."
            "He kissed me lightly on the neck and continued with his work."
            hide robert
            with short
            if v3_robert_orgasm:
                $ flena = "shy"
                "It had been enjoyable, yeah... I saw no reason not to do it again..."
            else:
                "It hadn't been great, but it was to be expected..."
                "The thing was, did I want to try it again?"
        else:
            r "I can't wait till Wednesday."
            "He kissed me lightly on the neck and continued with his work."
            hide robert
            with short
            l "That's right. We're going to sleep together soon..."
    elif v2_robert_reject:
        $ frobert = "n"
        show robert at lef
        with short
        r "Lena, make sure the glasses are ready and the wine's getting oxygenated. You got VIP table one and two tonight."
        l "Got it."
        hide robert
        with short
        "My relationship with Robert was back to the way it had always been. He kept his distance now, though."
        "Keeping it strictly professional, just like I wanted."
    scene restaurant
    with long
    $ flena = "n"
    $ lena_look = 1
    "I spent the next five hours serving tables and cleaning up stuff."
    if v3_robert_reject == False and v3_robert_date:
        show lena at rig
        show robert at lef
        with short
        "Before leaving, Robert approached me."
        r "The brass told me to come earlier tomorrow to have a meeting. I guess they're gonna discuss that issue with me..."
        l "I see... I hope they listen to you!"
        r "They will, don't worry. See you tomorrow, baby."
    else:
        "Finally, I got changed and went back home to get some sleep."


##LENA TUESDAY ####################################################################################################################################################################################################################

    $ day = "Tuesday"
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    if v2_lena_stan_model_shirt:
        $ lena_look = 2 
    else:
        $ lena_look = 1
    $ flena = "worried"
    play sound "sfx/meow.mp3"
    show lola at rig3
    with short
    l "Oh, Lola..."
    show lenabra
    with short
    l "Yes, I'll feed you some breakfast..."
    l "Good morning, by the way."
    play sound "sfx/purr.mp3"
    hide lola
    show lolahappy at rig3
    l "You could've let me sleep for a while longer... Ah, I'm still tired..."
    "I got up and stretched."
    $ flena = "n"
    l "Well, last night of the six in a row today! I'm almost done."
    play sound "sfx/ring.mp3"
    l "Who's this? Oh, Ivy."
    hide lenabra
    show lenabra_phone
    show phone_ivy at lef3
    hide lolahappy
    with short
    l "Good morning."
    v "There you are, you bitch! Why didn't you come yesterday? I missed you!"
    l "Oh, sorry, I forgot to tell you. They changed my shifts at the restaurant this week."
    v "Are you coming tomorrow, at least?"
    $ flena = "sad"
    l "Oh... I already made plans for Wednesday, sorry..."
    hide phone_ivy 
    show phone_ivy_sad at lef3
    v "What? You don't tell me anything! That's not good, where's our communication?"
    l "I'm sorry, these days have been crazy..."
    hide phone_ivy_sad 
    show phone_ivy_smile at lef3
    v "That means you have a ton to tell me!"
    l "A few things, yeah... Can I go to your Thursday's class this week?"
    v "Of course! And don't bail on me! I miss you!"
    l "I miss you, too, Ivy. Thanks for calling."
    v "Bye!"
    hide lenabra_phone
    show lenabra
    hide phone_ivy_smile
    with short
    l "Seems I have my free time completely scheduled already..."
    if v3_ian_date:
        "Tomorrow afternoon I was meeting Holly and Ian."
    else:
        "Tomorrow afternoon I was meeting Holly."
    if lena_robert_sex_late:
        "And at night Robert would come to my place once he got out of work..."
    "And it seems Thursday I would be going to the gym after working at the café!"
    if v3_seymour_date:
        "I would need to be quick about it, since I was meeting Mr. Ward for dinner that same day."
        "I hoped I wasn't too tired..."
    if v3_pg_ian or v3_pg_danny:
        $ flena = "n"
        "Since I already had my phone in my hand, I decided to check how my last picture was doing."
        show lenabra at right
        with move
        if v3_pg_ian:
            show v3_peoplegram2
        else:
            show v3_peoplegram1
        with short
        if v3_pg_ian:
            "It had less likes and comments than my previous post..."
            l "Let's see what people wrote..."
            "\"{i}Very nice drawing! It’s amazing to see how your modeling inspires others to bring out the artist within themselves{/i}\""
            "\"{i}Considering the source material, any drawing depicting you will turn out great!{/i}\""
            $ flena = "smile"
            l "Seems like they liked it."
            "\"{i}I'd love you to pose for me. Where do I send my business inquiry?{/i}\""
            l "He looks like some random guy... I'll pass."
            "\"{i}Nice drawing, but I prefer your pictures! You're really beautiful {image=emoji_kiss.png}{/i}\""
            $ flena = "sad"
            "\"{i}Why are you posting this? We don’t care about some random guy’s drawing of you{/i}\""
            l "Look like not everybody's happy with the post..."
            $ flena = "n"
            l "Whatever, it's my profile and I post what I want."
        else:
            "It had received even more likes and comments than my previous upload."
            "I read some."
            "\"{i}Wow, spectacular! You really have it all: unparalleled beauty, a body sculpted by the Gods and a confidence that radiates through every photo{/i}\""
            "\"{i}I hope you are going to work more with @danny_photography, because IMHO he truly captured your voluptuous beauty. Can't wait to see more of you!{/i}\""
            $ flena = "smile"
            l "They're really nice! I love these comments..."
            "\"{i}Shame about the censorship. Nice work by @danny_photography though. Please do more!{/i}\""
            "\"{i}Very sensual and sexy pose. {color=#1F5898}\#freethenips{/color}{/i}\""
            $ flena = "n"
            "\"{i}Magnificent picture, although this really makes me wish Peoplegram would allow nipples {image=emoji_disgust.png}{/i}\""
            if stalkfap:
                l "A lot of people are complaining about the censorship... Well, that's what I created that Stalkfap account for!"
            else:
                l "A lot of people are complaining about the censorship... Well, those are the rules."
            if v1_ed_truth or v1_ed_flirt:
                if ed_callout == False:
                    $ flena = "worried"
                    l "Seems like Ed commented again..."
                    "\"{i}You look like one of those Greek statues made out of marble! So beautiful! {image=emoji_kiss.png} {image=emoji_cum.png}{/i}\""
                    l "The comment is really nice, but those emojis..."
                    $ flena = "n"
                    l "Well, it's not something I should worry about. Ed's always been polite and respectful."
                    l "I should stop thinking ill about him!"
        hide v3_peoplegram2
        hide v3_peoplegram1
        with short
        if stalkfap:
            "I should also check that Stalkfap account I made..."
            "I had almost forgotten about it."
        else:
            show lenabra at truecenter
            with move
    elif stalkfap:
        "Since I already had my phone in my hand, I decided to check that Stalkfap account I made..."
        "I had almost forgotten about it."
        show lenabra at right
        with move
    if stalkfap:
        show v3_stalkfap2
        show v3_stalkfap3
        with short
        l "Hm... It seems three people signed up so far."
        l "Not much, but it's only been a couple of days since I set this up..."
        l "Look, one of them even left a comment."
        "\"{i}It's wonderful to finally be able to see your art and beauty without that stupid censorship!{/i}\""
        l "Well, let's see how people respond in the following days..."
        hide v3_stalkfap2
        hide v3_stalkfap3
        with short
        show lenabra at truecenter
        with move
    if v3_ian_date:
        "Last thing to do before starting the day was to tell Ian about my plans with Holly on Wednesday."
        "I decided to give him a call, but realized I didn't have his number. Just his Peoplegram."
        l "I guess I'll have to text him..."
        l "{i}Good morning Ian! I don't know if Holly already told you, but she and I are hanging out on Wednesday!{/i}"
        if v1_alisonlunch:
            l "{i}It surprised me discovering you and her know each other and work together!{/i}"
        l "{i}It would be cool if you decided to join us!{/i}"
        "His response arrived immediately."
        play sound "sfx/sms.mp3"
        if v1_alisonlunch:
            i "{i}You and Holly are friends? No way!{/i}"
        i "{i}Of course, I'd love to! Wednesday afternoon?{/i}"
        l "{i}Yes, in front of the café. By the way, we should exchange phone numbers!{/i}"
        i "{i}Of course.{/i}"
        "He texted me his number and I added him to my agenda."
        l "Alright, everything's set up now."
    "I stretched once more before getting up and tackling the day."
    "I took a shower, had some breakfast and headed to work."
    
    scene cafe
    with long
    $ lena_look = 1
    "Just as I was about to enter the café I saw Ed and Molly talking to each other."
    $ fmolly = "sad"
    $ fed = "sad"
    show ed at rig3
    show molly at lef3
    with short
    "Their faces had a look of concern..."
    mo "You know I don't like it."
    ed "I don't either, but..."
    $ flena = "sad"
    show lena
    with short
    l "Good morning..."
    $ fmolly = "n"
    mo "Oh, good morning Lena! Ready for today?"
    $ flena = "n"
    l "Yeah."
    mo "Let's get to it, then!"
    scene cafe
    show lenawork
    with short
    "Molly greeted me with her usual enthusiasm. I couldn't be sure if there was something going on..."  
    $ flena = "worried"
    if ed_callout:
        "I worried it could have something to do with me calling out Ed on his behavior..."
        "Maybe he had complained to Molly or maybe she was reprimanding him..."
        "I hoped I hadn't caused a fight between them..."
        "But I guess if it had anything to do with me they would've brought it up. It was probably something personal between them."
    elif v1_ed_flirt:
        "I wondered if it could have something to do with what happened with Ed and the trick I used on him to get off work earlier..."
        "Or maybe she had seen the comments Ed had left on my Peoplegram and was upset..."
        "I hoped not... If Molly thought there was something weird or inappropriate going on I would die of shame..."
        "But I guess if it had anything to do with me they would've brought it up. It was probably something personal between them."
    elif v1_ed_truth:
        "I wondered if it had something to do with the comments Ed had left on my Peoplegram..."
        "Maybe Molly had seen them and was upset?"
        "I hoped not... If Molly thought there was something weird or inappropriate going on I would die of shame..."
        "But I guess if it had anything to do with me they would've brought it up. It was probably something personal between them."
    else:
        "I hoped everything was OK between them..."
    "I had other things to worry about."
    if v3_talk_molly:
        "I had been thinking about my situation with Mom and Axel over and over these past few days."
        "Molly had given me something to consider regarding my relationship with Mom, but about Axel..."
    else:
        "I had been thinking about my situation with Axel over and over these past few days."
    "What should I really do?"
    if lena_robert_sex_early:
        "I had decided to turn the page, I even had sex with Robert already."
        if v2_kiss:
            "And I was also getting to know Ian, and he was someone I really liked..."
            "I had no idea how that would go, or if I really wanted it, but at least he was interesting."
        "I wasn't chained to Axel anymore."        
    elif lena_robert_sex_late:
        "I had decided to turn the page. I even hooked up with Robert and we would have sex very soon..."
        if v2_kiss:
            "And I was also getting to know Ian, and he was someone I really liked..."
            "I had no idea how that would go, or if I really wanted it, but at least he was interesting."
        "I wasn't chained to Axel anymore."        
    elif v2_kiss:
        "I was trying to turn the page. I had decided to do so."
        "I was getting to know Ian, and he was someone I really liked..."
        "I had no idea how that would go, or if I really wanted it, but at least he was interesting."
    elif v2_ian_date:
        "I had decided to turn the page. I was trying to, at least."
        "I was getting to know Ian, too... I had no idea how that would go, or what I wanted, but at least he was interesting."
    else:
        "I had decided to turn the page. I was trying to, at least."
    "I couldn't keep dragging the past along. But it wasn't so easy."
    "Axel didn't see things as I did and he was causing trouble in my life. Uncontrolled, I feared he would cause havoc."
    "He showed up at my workplace, then he went to visit my parents..."
    "What could be next? What unpleasant surprise would be the next one?"
    "Maybe I should do as Ivy advised and talk to him, just to make things clear and make sure he would stop pestering me."
    menu:
        "I should call him":
            $ renpy.block_rollback()
            $ v3_axel_call = True
            $ flena = "sad"
            l "I guess I should call him..."
            $ flena = "serious"
            l "If only to tell him to stop acting out and pestering me."
            l "If he wants to talk I'll talk to him... But I'll make things crystal clear for him."
            l "Maybe if I give him that he'll finally accept we're no longer together and let me go."
            $ flena = "sad"
            l "It won't be an easy talk though, that's for sure... I'll need to be ready mentally and emotionally before calling him."
            
        "I don't want to speak to him":
            $ renpy.block_rollback()
            $ flena = "serious"
            l "No, I don't want to speak to him or have anything to do with him."
            "Talking with him was giving him exactly what he wanted."
            l "If he's not getting the message it's clear he's the one who has a problem, not me."
            l "He must assume that he had lost me and move on."
            l "And leave me the fuck alone!"
    
# RESTAURANT
    stop music fadeout 2.0
    scene restaurant
    with long
    $ lena_look = 2
    $ flena = "n"
    $ robert_look = 2
    $ frobert = "n"
    show lenawork
    with short
    "After my shift at the café ended the one at the restaurant began."
    l "Come on Lena, last night... I'm in need of some rest already!"
    show lenawork at rig
    with move
    show robert at lef
    with short
    r "Lena, I have to talk to you..."
    if lena_robert_sex_early or lena_robert_sex_late:
        l "You have news about my job's situation?"
        $ frobert = "smile"
        r "Yes, we just had the meeting."
        l "So?"
        r "Well, there's good news and bad news."
        $ flena = "worried"
        l "Bad news?"
        r "The good news is that they won't fire you."
        l "And the bad ones?"
        $ frobert = "n"
        r "Your working hours are being reduced starting next month."
        "That meant my paycheck was being cut, too."
        $ flena = "drama"
        l "What? Why?"
        r "The situation was more serious than I thought... They wanted to kick someone out and reduce the shift of someone else to save some money."
        r "They wanted to lay you off and reduce Samantha's contract, since she's been working here for longer than you and well... No crazy ex-boyfriend of hers has been causing trouble around here."
        r "But I told them I need you on the team and that I'd rather have you, even if it's less hours, instead of Samantha."
        l "I see... It's not what I was expecting but..."
        r "Sorry, it's the best I could manage."
        $ flena = "sad"
        l "Thanks, I guess..."
        hide robert
        with short
        show lenawork at truecenter
        with move
        "I went back to work a bit discouraged."
        "I was keeping the job, yeah, but with a reduced schedule it wouldn't be enough to make ends meet..."
        hide lenawork
        $ frobert = "sad"
        show robert
        with short
        "I heard Samantha screaming at the other end of the room."
        "Robert had just told her that she was being fired and she was going off on him, complaining about me staying and she being laid off even though she had more experience."
        "She was furious... Robert had really done me a favor and he was taking the heat now."
        "I should've thanked him properly..."
        
    else:
        if v2_robert_date:
            $ flena = "worried"
            l "It's about that thing you told me?"
            r "Yes."
            "I didn't like his serious expression and tone."
            l "Is there a problem?"
        else:
            l "What about?"
            r "About your contract."
            $ flena = "worried"
            l "My contract? Is there a problem with it?"
        r "Your contract is not being renewed. We're gonna let you go at the end of the month."
        $ flena = "surprise"
        l "What?"
        if v2_robert_date:
            l "But you told me you were going to put in a good word on my behalf..."
            r "I would've, but that topic was never on the table."
        $ flena = "drama"
        r "We needed to let someone go, and the decision was between you and Samantha."
        r "She's been working here for two years already, so she's the more experienced."
        l "Samantha's been here longer, but she's a bit clueless, you know that!"
        r "She's not getting laid off, but her workdays are being reduced, so she's being affected by this too. That's the situation."
        l "Still, I'm way more efficient than she is!"
        r "That's not how the brass see it. Besides, her personal life doesn't cause trouble at the workplace."
        l "If you're talking about what happened with Axel, you know that's not my fault...!"
        "He answered with the same serious and monotone voice."
        r "The decision has been made. It wasn't me who took it, I hope you understand that."
        r "So next week will be the last one you'll be working with us. I'm sorry, Lena."
        hide robert
        with short
        "He ended the conversation and went back to work."
        "I was left there, feeling like a bucket of cold water had just been poured on me."
        if v2_robert_date:
            "I was losing my job at the restaurant, after all..."
        else:
            "I was losing my job at the restaurant all of a sudden!"
        show lenawork at truecenter
        with move
        "I went back to work quite discouraged."
        "What now? Without this job I would need to come up with something else to make ends meet."
        if v3_robert_reject:
            "I wondered if this was Robert's vengeance for what had happened on Sunday?"
            "If that was the case, it was unbelievably petty...!"
        elif v2_robert_reject:
            "I wondered if me rejecting Robert's advances had something to do with this..."
            "If that was the case, it was unbelievably petty...!"
        else:
            "It was a very unexpected blow."
        "I would need to think how to re-organize my life now..."
    jump v3ianfriday
    
################################################################################################################################################## 
##IAN #################################################################################
################################################################################################################################################## 

label v3ianfriday:
    
    $ week = 2
    $ lena_active = False
    $ ian_active = True
    $ save_name = "Ian: Chapter Three"
    
    $ day = "Friday"
    scene blackbg
    with long
    show active_ian
    with long
    pause 1.0  
    scene blackbg
    with long
    call screen calendar
    scene ianroom
    with long
    
## CHERRY
    if ian_cherry_sex:
        $ ian_look = 2
        $ know_cherry_model = True
        $ fperry = "meh"
        $ perry_glasses = False
        i "..."
        i "Mhhh..."
        "I opened my eyes slowly. I was feeling a tingly sensation down there..."
        play music "music/sensual.mp3" loop
        scene v3_cherry1
        with long
        with vpunch
        i "...!"
        ch "Good morning."
        play sound "sfx/bj1.mp3"
        "It took me a few seconds to understand what was going on. I was not dreaming..."
        "I had fallen asleep next to Cherry after having sex... And now she was between my legs with my erect cock between her hands."
        i "Cherry...! That's..."
        "She kissed the tip and a shiver ran across my spine."
        i "Mhh!"
        ch "\"It\" got up before you, and seeing how hard it was and since you didn't get to cum last night..."
        ch "I thought I could wake you up while making it up to you."
        "No complaints there. I was barely awake and I was having my dick sucked..."
        scene v3_cherry2_animation
        with long
        play sound "sfx/bj2.mp3"
        ch "Mhph..."
        i "Ohh...!"
        "She suddenly stopped with the teasing and swallowed my cock."
        "I felt her full lips enveloping it, her wet and soft tongue pressing down on the shaft."
        "The warmth of her mouth radiated through my cock, stimulated by its slippery strokes."
        "Soon I felt pleasure building up, pushing the boundaries of climaxing release."
        i "Oh God, Cherry..."
        play sound "sfx/dp2.mp3"
        "Hearing my moans only encouraged her more."
        scene v3_cherry2_animation2
        with long
        "She sucked faster and rougher, helping the motion with her hand."
        "I closed my eyes and I felt it coming. What had been eluding me last night was being finally brought forth."
        i "Cherry, I'll cum...!"
        "I gripped the bed sheets as I felt my body tense."
        scene v3_cherry2
        show v3_cherry2cum
        with flash
        with vpunch
        i "Ahhh!!"
        "I did it. My mind went blank."
        "For a moment, I just felt the sensation that invaded my body."
        "I felt Cherry's hot mouth enveloping my cock as I orgasmed and shot my load inside it."
        scene v3_cherry1
        show v3_cherry1cum
        with long
        "I still convulsed a few more times before the orgasmic pleasure dissipated."
        "I opened my eyes and saw Cherry smiling at me from behind my cock."
        "Her dark and fleshy lips became glazed by my cum, sticky and shiny, as she caressed my cock with them."
        ch "See? I knew you could cum."
        stop music fadeout 2.0
        i "Oh, Cherry..."
        "I was still breathing heavy."
        ch "You just were too tense..."
        "She climbed up to my level after her job down there was done."
        $ fian = "smile"
        scene ianroom
        show iannude at lef
        show cherrynude at rig
        show cherry_cum  at rig
        with short
        "I could finally get my bearings back and smiled at her."
        i "Good morning indeed."
        ch "I'm glad you liked it."
        ch "Do you have a tissue?"
        i "Oh yeah, wait a second..."
        hide cherry_cum
        with long
        "I gave her one and she wiped the cum from her face."
        i "I certainly wasn't expecting to wake up like this when I went to sleep last night..."
        ch "I couldn't leave without repaying you."
        i "I feel I'm the one indebted to you now. It was so good..."
        ch "Stop it, or you'll make me blush, ha ha."
        ch" Well, now that I'm satisfied with my job I'll get going."
        $ fian = "n"
        i "Oh, sure... Let me see you out."
        hide iannude
        hide cherrynude
        with short
        "We got dressed and I walked Cherry to the door."
        play sound "sfx/door.mp3"
        scene ianhome
        $ fian = "smile"
        $ fcherry = "smile"
        show ian at lef
        show cherry at rig
        with short
        i "Well..."
        ch "Thanks, Ian. It's been fun."
        "She gave me a kiss... on the cheek."
        $ fian = "worried"
        i "Oh..."
        $ fcherry = "sad"
        "It was obvious she saw the disappointment in my eyes, because she felt the need to add something before leaving."
        ch "I don't know how to say this without sounding obnoxious, but..."
        ch "I really had fun with you, but this is all this was. Just fun."
        menu:
            "I thought we could be more":
                $ renpy.block_rollback()
                i "I thought we could, uh, maybe, try becoming something more?"
                i "You're a really awesome girl and I like you a lot..."
                ch "I like you too, Ian. That's why I came to your place last night."
                $ ian_cherry -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                ch "But I'm at a complicated stage in my life right now and I'm not looking to get into a relationship or anything like that at this moment..."
                ch "I'd hate to cause trouble for someone who had other expectations, so that's why I wanted to make it clear from the start."
                i "Oh, I see... Of course, it's not like I'm looking for a girlfriend right now or anything like that!"
                i "It's just that I'd like to keep in touch with you and meet some other time..."
                ch "Maybe, who knows. And only as long as you're not expecting anything more of me."
                ch "I'm sorry to be like this, I know it comes across as cold but... I'd rather be honest about it."
                i "Of, course, I understand."
                $ fian = "n"
                i "Don't worry... I'm not head-over-heels for you."
                $ fcherry = "smile"
                ch "Good to know. See you around."
                i "Oh, wait, can I add you on Peoplegram at least?"
                ch "Sure... It's \"{i}@cherryblossom{/i}\", without spaces."
                i "Cool. Bye, then."
                hide cherry
                with short
                $ fian = "sad"
                i "Damn... I'm such an idiot."
                show perry2 at right
                with short
                p "Yeah, that wasn't too smooth."
                $ fian = "surprise"
                i "Jesus! Where are you popping out from?"
                show perry2 at rig
                with move
                p "I was in the kitchen making some c--{w=0.5}coffee... Oh man, this headache..."
                $ fian = "n"
                i "So how much of that did you hear?"
                p "Almost everything? You should've given her some sa--{w=0.5}space."
                i "Yeah, you're a big expert on these things..."
                p "Hey man, it's just my opinion. If you don't wanna hear it, it's not my fault."
                hide friend_down
                
            "I see it that way too":
                $ renpy.block_rollback()
                $ ian_cherry_free = True
                $ fian = "n"
                i "Oh, yeah, yeah, of course. I see it the same way."
                ch "That's the impression I got, that's why I thought it would be nice to do it."
                ch "I'm at a complicated stage in my life right now and I'm not looking to get into a relationship or anything like that at this moment..."
                ch "I'd hate to cause trouble for someone who had other expectations, so that's why I wanted to make it clear from the start."
                $ fian = "smile"
                i "Don't worry, we're on the same page. Being in a complicated stage in life included."
                $ fcherry = "happy"
                ch "Good to know."
                $ fcherry = "blush"
                ch "Oh, and please, don't think I do this kind of thing often..."
                ch "I just thought you were really nice and I felt comfortable with you, that's why I decided to come to your place."
                i "Oh... Thank you, I really appreciate it. You're awesome too."
                "I bumped my fist against her shoulder in a friendly and playful way."
                $ fcherry = "happy"
                play sound "sfx/xp.mp3"
                show charisma_up
                $ ian_charisma_xp += 1
                call screen skillsup
                ch "I think you get me. Thanks!"
                ch "Oh, and you can add me on Peoplegram, it's \"{i}@cherryblossom{/i}\", without spaces."
                ch "See you around!"
                i "Bye!"
                hide cherry
                with short
                show perry2 at right
                with short
                p "Well, that went well."
                $ fian = "surprise"
                i "Jesus! Where are you popping out from?"
                show perry2 at rig
                with move
                p "I was in the kitchen making some c--{w=0.5}coffee... Oh man, this headache..."
                $ fian = "n"
                i "So how much of that did you hear?"
                p "Almost everything? Well played, dude."
        $ fperry = "sad"   
        p "Uhhh, this headache..."
        "Perry sat on the couch and sipped his coffee."
        i "I'm surprised you're up so early, considering how wasted you got..."
        p "Ugh, yeah... This is o--{w=0.5}one of those hangovers that will take the entire day to wear off..."
        p "Sorry for making you and C--{w=0.5}Cherry drag me home..."
        $ fperry = "meh"
        p "So how was it? With Cherry."
        menu:
            "Tell him":
                $ renpy.block_rollback()
                "I sat next to him."
                $ fian = "smile"
                i "It was pretty great, actually."
                p "How did you manage that?"
                i "Manage what? Getting her into my bed?"
                p "Yeah."
                i "I have no idea. I wouldn't say I \"managed to\"... It was more like she wanted to get into my bed."
                i "I just... Made way for it to happen, I guess!"
                p "Lucky b--{w=0.5}bastard! So was she... you know, good in bed?"
                i "I'd say she was..."
                p "You'd say? You have doubts?"
                i "She had an amazing body and was not shy in bed. And those lips, oh man..."
                p "So what's the p--{w=0.5}problem?"
                $ fian = "n" 
                i "I just couldn't cum. Well, at night at least."
                $ fperry = "surprise"
                p "Shit, so you did it in the morning, too?"
                i "I'm already telling too much..."
                $ fperry = "meh"
                i "In any case she said it was because I'm too tense."
                p "Yeah, your cock must've been extremely t--{w=0.5}tense with a hottie like her..."
                i "Could you please not speak about my cock and its state?"
                p "Whatever. Let's check her Peoplegram, then."
                
            "It's none of your business":
                $ renpy.block_rollback()
                $ fian = "serious"
                i "That's none of your business."
                $ fperry = "mad"
                p "Hey, I'm just asking because y--{w=0.5}you're my friend. You don't need to get like that."
                $ ian_perry -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                p "It's not like I'm wanting to hear the d--{w=0.5}details to jerk off or something."
                i "I hadn't even thought about that possibility until you brought it up. So yeah, I'm better not telling you."
                $ fperry = "meh"
                p "Whatever dude... I'm not even that interested to be honest."  
                p "Let's at least check her Peoplegram."
        i "OK..."
        show perry2 at right
        show ian at left
        with move
        show v3_peoplegram_cherry1
        with short
        "I pulled out my phone and searched for Cherry's profile."
        $ fian = "surprise"
        $ fperry = "surprise"
        "What I found surprised both me and Perry."
        p "Oh, wow. Looks like she's a model!"
        $ fperry = "flirt"
        $ fian = "worried"
        "Indeed, she had a variety of pictures on her profile and some looked like professional photo-shoots."
        i "It doesn't look like she's a professional though..."
        p "Of course she's not. She w--{w=0.5}works with Alison..."
        i "But why did she avoid mentioning it?"
        hide v3_peoplegram_cherry1
        show v3_peoplegram_cherry2
        with short
        "I kept scrolling as we talked."
        i "Damn."
        p "This one's amazing... T--{w=0.5}too bad there's censorship!"
        p "I'd love to see her nipples...!"
        i "Maybe that's the reason she failed to tell us she did this kind of modeling. To avoid pervs like you..."
        p "Easy for you to say. You've seen them."        
        $ fian = "smile"
        i "Oh yeah. And more than just seeing them."
        $ fperry = "n"
        p "Shut up. I don't know how you're d--{w=0.5}doing it, man."
        p "This is the second model you charm. You have discovered some illegal pheromones or something?"
        if v2_kiss:
            i "Well, now that you say it... It's kind of baffling, actually."
        else:
            i "I wouldn't say I have charmed Lena..."
        p "Anyways, I'm h--{w=0.5}happy for you, man."
        hide v3_peoplegram_cherry2
        with short
        show ian at lef
        show perry2 at rig
        with move
                                                                                                             
## ALISON
    elif ian_alison_sex:
        $ ian_look = 2
        $ fperry = "meh"
        $ perry_glasses = False
        $ falison = "n"
        $ fian = "worried"
        i "..."
        "I woke up next morning feeling someone moving in my bed."
        show iannude2 at lef
        show alisonbra at rig
        with short
        "Alison was finishing putting on her underwear."
        i "Uh... Good morning."
        a "Oh, sorry, I didn't want to wake you up. I have some stuff to take care of today so that's why I'm leaving so early."
        menu:
            "Go back to sleep":
                $ renpy.block_rollback()
                $ fian = "n"
                i "Oh, OK."
                scene ianroom
                with long
                "I turned around and covered myself with the blanket."
                "Alison kissed me on the cheek before getting dressed and leaving."
                "I slept for an hour or so before deciding to finally get up."
                show ianunder 
                with short
                "I had a slight head-ache that morning."
                if v2_cocktail == 1:
                    i "Those Bloody Marys seem to be taking a bit of a toll on me..."
                if v2_cocktail == 2:
                    i "Those Margaritas seem to be taking a bit of a toll on me..."
                if v2_cocktail == 3:
                    i "Those Tequila Sunrises seem to be taking a bit of a toll on me..."
                i "Also, those shots sure helped, too."
                "I got up and went to get something to drink."
                i "Some coffee will help clear my head..."
                play sound "sfx/door.mp3"
                scene ianhome
                with short
                $ ian_look = 2
                show ian at lef
                with short
                $ perry_glasses = False
                $ fperry = "meh"
                show perry2 at rig
                with short
                p "Hey."
                i "Hey."
                "I found Perry on the couch, drinking a cup of coffee in a much sorrier state than I was in."
                
            "Get up":
                $ renpy.block_rollback()
                $ fian = "n"
                i "I can't let you leave like that. Let me see you to the door at least."
                $ falison = "smile"
                "She smiled."
                play sound "sfx/xp.mp3"
                show charisma_up
                $ ian_charisma_xp += 1
                call screen skillsup
                a "Such a gentleman."
                "I got up and searched for my clothes."
                $ falison = "n"
                "Alison looked pretty lively first thing in the morning. Instead, I had a slight head-ache."
                if v2_cocktail == 1:
                    i "Those Bloody Marys seem to be taking a bit of a toll on me..."
                if v2_cocktail == 2:
                    i "Those Margaritas seem to be taking a bit of a toll on me..."
                if v2_cocktail == 3:
                    i "Those Tequila Sunrises seem to be taking a bit of a toll on me..."
                i "Also, those shots sure helped, too. Don't you have a headache?"
                a "I can take alcohol pretty well. I think I trained my body plenty when I was a teen, ha ha."        
                play sound "sfx/door.mp3"
                scene ianhome
                show ian at lef
                show alison at rig
                with short
                "We got dressed and I walked Alison to the door."
                "I still wasn't sure how to act around Alison after what had just happened last night. We really had sex..."
                "She was acting like she always had though, like nothing had changed. Maybe it really hadn't..."
                i "Um... So I guess I'll see you soon?"
                a "Of course."
                "She smiled and pinched my cheek as she used to do."
                a "Gotta run. Let's talk soon. Bye!"
                "She kissed me on the cheek before turning around and leaving for good."
                hide alison
                with short
                i "..."
                "Why did I feel so awkward? Was I expecting a different attitude from her, perhaps?"
                $ perry_glasses = False
                $ fperry = "meh"
                show perry2 at rig
                with short
                p "So she stayed over at the end."
                $ fian = "surprise"
                i "Jesus! Where are you popping out from?"
                show perry2 at rig
                with move
                p "I was in the kitchen making some c--{w=0.5}coffee... Oh man, this headache..."
                $ fian = "n"
                "Perry sat on the couch and sipped his coffee."
                
        i "I'm surprised you're up so early, considering how wasted you got..."
        p "Ugh, yeah... This is o--{w=0.5}one of those hang-overs that will take the entire day to wear off..."
        if perry_cherry < 2:
            $fperry = "mad"
            p "So you went ahead and really did it... with Alison."
            "It looked like he was still mad at me for having left him hanging with Cherry."
        else:
            p "So you went ahead and really did it... with Alison."
        p "Even when I told you it could get c--{w=0.5}complicated."
        i "Stop acting like some kind of doomsday prophet. So far it's going pretty good."
        p "Really? Then why don't you look too hyped?"
        i "I'm hyped. Last night was amazing. It's just that this morning felt..."
        p "S--{w=0.5}strange?"
        i "..."
        i "Yeah, a bit."
        p "Told you so."
        i "But not in a bad way! The first time is always awkward."
        p "So you'll be doing it with her again?"
        i "I don't know, I guess... We haven't talked about that..."
        p "I just hope you k--{w=0.5}know what you're doing."
        i "Yeah, yeah. Thanks for your concern."
        hide perry2
        show perry at rig
        with short
        p "So did you like it, at least? Was she, you know... good?"
        menu:
            "Tell him":
                $ renpy.block_rollback()
                "I sat next to him."
                i "Yeah, I'd say she was..."
                p "You'd say? You have doubts?"
                i "No, I mean... She's beautiful and has an amazing body. And she was not shy in bed..."
                p "So what's the p--{w=0.5}problem?"
                i "I just couldn't cum."
                $ fperry = "meh"
                p "Did you use a condom?"
                i "Yeah, of course."
                p "Maybe it's because of that. It's harder with a r--{w=0.5}rubber."
                i "I don't know. It was never an issue in the past."
                p "Maybe it's because of the alcohol? Or maybe you j--{w=0.5}just don't like her that much..."
                i "I could blame the alcohol, but not not liking her enough. I was really excited..."
                i "Though at one point... I almost fucked up. Down there, you know..."
                p "Your little soldier didn't want to stand firm?"
                i "Don't call it \"little soldier\", for fuck's sake. But yeah, for a second there I thought it would betray me."
                i "I managed to make it work in the end, though."
                p "That's probably because you were fucking a f--{w=0.5}friend... You must've felt weird about it."
                i "I don't think that was the case. Anyway, at the end we had quite some fun."
                p "I'm glad for you, then..."
                
            "It's none of your business":
                $ renpy.block_rollback()
                $ fian = "serious"
                i "That's none of your business."
                $ fperry = "mad"
                p "Hey, I'm just asking because y--{w=0.5}you're my friend."
                if ian_perry > 2:
                    $ ian_perry -= 1
                    play sound "sfx/frienddown.mp3"
                    show friend_down
                p "It's not like I'm wanting to hear the d--{w=0.5}details to jerk off or something."
                i "I hadn't even thought about that possibility until you brought it up. So yeah, I'm better not telling you."
                $ fperry = "meh"
                p "Whatever dude... I'm not even that interested to be honest."                  
        
## ALONE        
    else:
        $ ian_look = 3
        "I woke up with a slight head-ache that morning."
        $ fian = "disgusted"
        show ianunder
        with short
        if v2_cocktail == 1:
            i "Those Bloody Marys are taking a toll on me today..."
        if v2_cocktail == 2:
            i "Those Margaritas are taking a toll on me today..."
        if v2_cocktail == 3:
            i "Those Tequila Sunrises are taking a toll on me today..."
        "Also, those shots sure helped, too..."
        if v2_cherry_home:
            "That was not the only thing that was making me feel sick, though."
            "What had happened after that was much worse."
            $ fian = "sad"
            i "How the hell could I go soft with Cherry?"
            i "I had her right here, in my room, completely nude and willing..."
            i "Shit, man..."
        elif v2_alison_home:
            "That was not the only thing that was making me feel sick, though."
            "What had happened after that was much worse."
            $ fian = "sad"
            i "How the hell could I go soft with Alison?"
            i "I had her right here, in my room, completely nude and willing..."
            i "Shit, man..."
        else:
            $ fian = "n"
            "Last night... It had been an interesting one."
            "I wondered what Alison and Jeremy did at the end.."   
        "I got up and went to get something to drink."
        i "Some coffee will help clear my head..."
        play sound "sfx/door.mp3"
        scene ianhome
        show ianunder at lef
        with long
        $ perry_glasses = False
        if v2_cherry_home:
            $ fperry = "sad"
        else:
            $ fperry = "meh"
        show perry at rig
        with short
        p "Hey."
        i "Hey."
        if v2_cherry_home:
            "Perry was on the couch, drinking a cup of coffee in a sorrier state than I was in."
            i "I'm surprised you're up already, after how hammered you got last night!"
            p "Ugh, yeah... This is o--{w=0.5}one of those hang-overs that will take the entire day to wear off..."
            p "Sorry for making you and C--{w=0.5}Cherry drag me home..."
            $ fperry = "meh"
            p "By the way, what h--{w=0.5}happened with her in the end?"
            i "What do you mean \"what happened with her\"?"
            p "Dude, you were f--{w=0.5}flirting with her all night long... And I remember she came to our house..."
            p "Did something happen? Or did she l--{w=0.5}leave?"
            $ fian = "depress"
            i "..."
            "I sighed and collapsed on the sofa next to Perry. It was time to confess my shameful failure."
            i "I fucked up."
            p "What do you mean \"you f--{w=0.5}fucked up\"?"
            i "We were about to have sex, and then... I just couldn't get it up."
            $ fperry = "sad"
            p "No way."
            i "Yeah, dude... It was so fucking embarrassing."
            p "I'm sorry man, that sucks... What happened, you got n--{w=0.5}nervous?"
            i "Yes, I freaked out a bit. Maybe it's because I had drunk a bit too much, I don't know..."
            p "It's hard to get it up when y--{w=0.5}you're drunk."
            i "I wasn't like that. I was really hard, but then when it was time to put on the condom I just..."
            i "I started to think about how long it's been since I last had sex and I got afraid of not being good enough."
            i "I have been dumped once already, after all..."
            p "Dude, you need to avoid thinking like that!"
            i "I know that! Easier said than done, though."
            p "Did she get mad?"
            i "No... She was quite understanding... But she was visibly frustrated, that I could tell."
            p "And she left?"
            i "Yeah..."
            p "Well, at least she didn't y--{w=0.5}yell at you or something like that... Maybe you should write to her and apologize."
            $ fian = "sad"
            i "I already apologized too much yesterday."
            p "I'm sorry that happened to you, man. She was so fucking h--{w=0.5}hot."
            i "I know..."
            $ fperry = "n"
            p "Well, look at the bright side of things. You managed to get such a hot girl to want to sleep with you."
            i "I guess... Though the way you phrased it makes it feel like I conned her or something..."
            $ fperry = "meh"
            p "I'm just trying to boost your confidence."
            i "Thanks... I guess that's something I can take away from this experience, at least."
            
        elif v2_alison_home:
            "Perry was on the couch, drinking a cup of coffee."
            p "So, how did last night end?"
            i "Oh, you know, it was... fine."
            $ fperry = "mad"
            p "Wasn't fine for me. I told you not to leave me alone with Cherry!"
            i "I'm not your babysitter, dude. You're old enough to fend for yourself."
            p "You know it's n--{w=0.5}not so easy for me!"
            i "Get over it already."
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_perry -= 2  
            p "Such a friend you are."
            i "Dude, I'm not in the mood right now..."
            $ fperry = "meh"
            p "Why? Did something happen?"
            i "It's..."
            "I sighed and collapsed on the sofa next to Perry. It was time to confess my shameful failure."
            i "I fucked up."
            p "What do you mean \"you f--{w=0.5}fucked up\"?"
            i "With Alison..."
            p "I told you you shouldn't have tried to flirt with her. She's your friend..."
            i "We were about to have sex, and then... I just couldn't get it up."
            $ fperry = "sad"
            p "No way."
            i "Yeah, dude... It was so fucking embarrassing."
            p "I'm sorry man, that sucks... I guess you felt weird having sex with a friend, right?"
            i "No, it wasn't that. I was excited and eager to go, but then when it was time to put on the condom I just..."
            i "I started to think about how long it's been since I last had sex and I got afraid of not being good enough."
            i "I have been dumped once already, after all... And I didn't want to disappoint Alison..."
            p "Dude, you need to avoid thinking like that!"
            i "I know that! Easier said than done, though."
            p "Did she get mad?"            
            i "I wouldn't say she got mad, just... frustrated, I guess."
            p "And she left?"
            i "Yeah..."
            p "And what did she say?"
            $ fian = "sad"
            i "I don't really remember... She said \"I guess these things can happen\" and \"some other time, then?\""
            p "Some other time?"
            i "Yes... But I don't know if she really meant it."
            $ fperry = "n"
            p "Who knows... I want to say \"I told you so\" but what's done is done."
            p "I just hope things don't get w--{w=0.5}weird as I warned you they could."
            i "I hope so too."
            
        else:
            p "Hang-over much?"
            i "A bit. I'm gonna get some coffee..."
            "Perry was already drinking one."
            p "I made plenty. I knew you'd be needing it after drinking those c--{w=0.5}crappy cocktails."
            p "Help yourself."
            i "Thanks, man."
            "I poured myself some and sat next to Perry."
        "Perry looked at me."
        p "You could put on some pants at least, man."
        i "Shut up."
    if alison_jeremy:
        $ fperry = "meh"
        p "What about Jeremy and Alison? Do you think they f--{w=0.5}fucked?"
        $ fian = "n"
        i "If I had to bet I'd say yes..."
        p "Yeah, I'd say that, too. He was hounding her like a dog that won't let go of a bone."
        i "He came with a clear intention in his head and went for it."
        p "In his h--{w=0.5}head? In his dick rather."
        $ fian= "smile"
        i "Heh, yeah... You know how he is."
        i "If anything happened between them we'll get to hear it from him, don't worry."
        p "Oh, I'm sure we will, even if we don't ever ask him..."        
    if perry_cherry > 1 and v2_cherry_home == False:
        $ know_cherry_model = True
        i "So what about you and Cherry? I had the feeling you were hitting it off pretty well..."
        $ fperry = "smile"
        p "Oh, yeah. She's p--{w=0.5}pretty cool."
        i "Do you think there's any possibility that you and her..."
        $ fperry = "n"
        p "No, it's not like that. A man and a woman can be just friends, you know? That we got along doesn't mean we should end up f--{w=0.5}fucking."
        p "That's how Jeremy thinks."
        i "I didn't say that... But don't tell me you wouldn't like sleeping with her!"
        p "I wouldn't mind, of course... But that's not my goal..."
        $ fperry = "happy"
        p "Anyways, look at this! She gave me her number and today I added her on Peoplegram..."
        if ian_alison_sex:
            show ian at left
        else:
            show ianunder at left
        show perry at right
        with move
        show v3_peoplegram_cherry1
        with short
        "Perry pulled up his phone and showed me Cherry's profile."
        $ fian = "surprise"
        i "Oh, wow. Looks like she's a model, too!"
        $ fperry = "flirt"
        p "She's not a pro, but it looks like she's done some m--{w=0.5}modeling, yeah."
        p "Can you believe it? A model gave me her number!"
        p "And she's the second one we've met in just a couple of weeks!"
        i "Yeah..."
        "I kept scrolling through her profile. She had a variety of pictures and only some looked like actual photo-shoots."
        hide v3_peoplegram_cherry1
        show v3_peoplegram_cherry2
        with short
        i "Damn."
        p "Yeah, this one's amazing... T--{w=0.5}too bad there's censorship!"
        p "I'd love to see her nipples...!"
        $ fian = "smile"
        i "What happened to that \"just being friends\" thing?"
        p "Hey, I can be her friend and still want t--{w=0.5}to see her boobs... That doesn't mean I'll try to fuck her or anything."
        i "I see. So you're just a voyeur."
        p "Shut up. Don't tell me you wouldn't love to see them, either!"
        if ian_lust > 1:
            i "Sure, why not..."
        else:
            i "Who knows..."
        i "I'm surprised she's a model, too. She didn't say anything last night."
        $ fperry = "n"
        p "She probably didn't want to be judged by you and Jeremy. You were acting like t--{w=0.5}total pervs."
        i "Look who's talking! The voyeur master!"
        p "At least I'm like this in private and I don't creep girls out!"
        $ fian = "smile"
        i "That's just because they don't know you as I do..."
        hide v3_peoplegram_cherry2
        with short
        if ian_alison_sex:
            show ian at lef
        else:
            show ianunder at lef
        show perry at rig
        with move
            
    $ fian = "n"
    i "Well... I'm gonna try and do something productive today. I still need to write that book review..."
    p "OK."

##IAN WRITING
    play music "music/normal_day.mp3" loop
    play sound "sfx/door.mp3"
    scene ianroom
    with long
    $ fian = "n"
    $ ian_look = 2
    show ian
    with short
    if ian_switch_review:
        "I sat down at my desk and picked up \"The Fall of Delbaeth\"."
        "I had been reading it these past few days and it was amazing. It had been a long time since a read had me that hooked."
        "It was long, so I hadn't finished it yet. I needed to get that done during the weekend, so I applied myself thoroughly."
        "I continued to read while taking notes and planning the review in my head."
        play sound "sfx/xp.mp3"
        show wits_up
        $ ian_wits_xp += 1
        call screen skillsup
        scene ianroomnight
        with long
        "Before I noticed almost the whole day went by and it was dinner time."
        $ fian = "smile"
        show ian
        with short
        "I had been having fun with an assignment for the first time in... For the first time ever, in fact."
        i "I should ask Holly for her opinion when I'm done, just to make sure I'm doing a good job with this review..."
    elif ian_honest_review:
        "I sat down at my desk and picked up \"Poker Love\"."
        "I had been reading it these past few days and it was every bit as awful as I had anticipated."
        i "I can't believe they are publishing this thing... But I'm going to enjoy tearing it apart."
        scene ianroom
        show v2_ianwrite
        with short
        "I began checking my notes and writing the review."
        play sound "sfx/keyboard.mp3"
        i "{i}This book throws all the tropes present in teenage literature into the mixer and blends them mindlessly, like a kid who mixes all colors believing he will get a better one.{/i}"
        i "{i}The results are the same: brown and bland like the content of that kid's diaper.{/i}"
        "I smiled."
        i "Hah, that sounds just about right..."
        play sound "sfx/xp.mp3"
        show charisma_up
        $ ian_charisma_xp += 1
        call screen skillsup
        scene ianroomnight
        with long
        "I kept working on the review until it was almost dinner time. I had a surprising amount of fun with it and I tried to make it something worth reading."
        $ fian = "confident"
        show ian
        with short
        "When I was done I had the feeling I had written something that people could love and that Minerva would really hate. I was even proud of my job."
        i "Maybe I could show it to Holly to get an honest opinion about it, since I know what Minerva will say..."
    else:
        "I sat down at my desk and picked up \"Poker Love\"."
        "I had been reading it these past few days and it was every bit as awful as I anticipated."
        play sound "sfx/keyboard.mp3"
        scene ianroom
        show v2_ianwrite
        with short
        "I began checking my notes and writing the review. I had to make sure to write something to Minerva's standards this time..."
        scene ianroomnight
        with long
        "I slugged through the writing as almost the whole day went by."
        $ fian = "disgusted"
        show ian
        with short
        "What a miserable way to spend a holiday."
        i "I'm sick of this... But it's finally done, and I think I've made a good job."
        $ fian = "n"
        i "I should consult with Holly to make sure Minerva will be OK with this. I tried to follow Holly's instructions on how to write it, after all."
    
    menu:
        "Meet with Holly":
            $ renpy.block_rollback()
            $ v3_holly_date = True
            $ fian = "smile"
            "I texted her."
            i "{i}Hey Holly! I've been working on the review and I'd love to have your opinion.{/i}"
            i "{i}Would you like to meet before Monday so you can take a look at it?{/i}"
            play sound "sfx/sms.mp3"
            if ian_switch_review:
                h "{i}Yes, of course! When is it OK for you?{/i}"
                i "{i}I haven't finished it yet, but I should have it done by Sunday...{/i}"
                h "{i}Maybe we could meet Sunday morning in the café, then?{/i}"
                i "{i}Sound good to me! Thanks Holly, I'll see you on Sunday then. Coffee's on me.{/i}"
                play sound "sfx/sms.mp3"
                h "{i}Alright {image=emoji_smile.png}{/i}"
                i "Nice. I must finish the review before Sunday, though."
            else:
                h "{i}Yes, of course! But I'm still working on mine, the book is pretty long.{/i}"
                h "{i}Maybe we could meet Sunday morning in the café?{/i}"
                i "{i}Sound good to me! Thanks Holly, I'll see you on Sunday then. Coffee's on me.{/i}"
                play sound "sfx/sms.mp3"
                h "{i}Alright {image=emoji_smile.png}{/i}"
                i "Nice. I wonder what Holly will think about my review..."
            "I got a text from someone else."
            
        "E-mail it to Holly":
            $ renpy.block_rollback()
            $ fian = "n"
            "I decided to e-mail her the review so she could give me her opinion."
            i "That should be enough."
            "My phone vibrated with a text message."
    play sound "sfx/sms.mp3"
    i "Oh. It's Cindy's. Weird, she rarely texts me..."
    i "Let's see what she's saying."
    c "{i}Hey, look at what I found!{/i}"
    "She was attaching a file. It was a video."
    $ ian_ian_gallery = True
    $ ian_ian_pics.append("v3_memory.png")
    hide ian
    show v3_memory
    with short
    i "Oh, damn!"
    "It was a video of one of the performances we had made during our high school years."
    "I hadn't seen pictures or videos from that time in ages..."
    "I didn't know if to feel ashamed or laugh. I did both."
    i "{i}That's hilarious. Where did you get that?{/i}"
    play sound "sfx/sms.mp3"
    c "{i}I found it on an old hard-drive Wade had lying around.{/i}"
    i "{i}Well, you said you wanted to see us play... What do you think?{/i}"
    c "{i}It's the best thing I've seen in a long time. I can't stop laughing.{/i}"
    i "{i}Hey, we weren't that bad!{/i}"
    c "{i}You were surprisingly good! I can't get over Perry singing! And the looks you guys had, OMG.{/i}"
    i "{i}Everybody has a dark past... I'd like to see you when you were sixteen!{/i}"
    c "{i}I was already fabulous, ha ha.{/i}"
    $ fian = "smile"
    c "{i}By the way, are you guys doing anything tomorrow night? It's Saturday, we could do something.{/i}"
    i "{i}Sure. Me and Perry don't have plans yet... I'll go tell him.{/i}"
    $ fperry = "n"
    $ perry_glasses = True
    play sound "sfx/door.mp3"
    scene ianhomenight
    show ian at lef
    show perry at rig
    with short
    i "Hey. Cindy just asked if we wanna do something tomorrow night."
    p "Oh, sure. But this time we're going to our usual bar."
    i "Yeah, yeah."
    p "I was just texting with Emma. I'll tell her to come, too..."
    p "..."
    $ fperry = "happy"
    p "She says she's in."
    i "Nice."
    "I got back to Cindy and let her know we were on with her plan."
    play sound "sfx/sms.mp3"
    c "{i}Cool! See you guys tomorrow at the bar!{/i}"
    stop music fadeout 2.0

##IAN SATURDAY ####################################################################################################################################################################################################################

    $ day = "Saturday"
    scene blackbg
    with long
    call screen calendar
    scene ianroom
    with long
    
    $ v3_write_check = False
    show ianroom
    show v2_ianwrite
    with long
    if ian_switch_review:
        "I spent the whole day working on my book review."
        play sound "sfx/keyboard.mp3"
        "I wanted to make the best job I had ever done. And I was enjoying it, too."
        "I would show Minerva how talented I really was and how full of shit she actually was."
        scene ianroomnight
        show v2_ianwrite
        with long
        "Just before dinner time I finally finished the review."
        i "Right on time!"
        jump v3iansaturdayafternoon
    else:
        jump v3writebook
        
label v3writebook:        
    "Since I had already finished my book review I could concentrate again on my book."
    "That was my main goal, after all... The work at the magazine was just getting in the way in the end."
    "And the deadline to submit my book at the contest was getting closer..."
    if book_scifi:
        "I had decided to write a {color=#3FB305}Science Fiction{/color} book, a very cool but complicated genre that opened the door to being original and creative, but while keeping things coherent."
    if book_fantasy:
        "I had decided to write a {color=#B30505}Fantasy{/color} book, a genre that was perfect to explore adventure and drama with freedom and creativity."
    if book_historical:
        "I had decided to write an {color=#D1B402}Historical{/color} book, a genre very familiar to the public but that needed to be well researched and grounded."
    "I had a general idea of the plot and themes, but I still had to define some key elements of the story."
    i "First, I need a compelling reason to kick-start the action. A call to adventure for the main character..."
    i "The reason he's in this."
    i "I should choose a call to adventure that fits with the type of book I'm writing..."
    if ian_wits > 0:
        "I should try to find some original combination that you don't see often but that could work with the genre."
    if ian_wits > 1:
        i "Bust most of all I should to avoid clichés."
    
label v3_writebookchoice:
    call screen book_screen_2
    if book_card1 == "vengeance":
        i "A vengeance story is always money. The character has a personal grudge to settle with the antagonist or the world itself..."
        i "That's the best possible fuel for a thrilling adventure."
        menu:
            "Choose this card":
                $ renpy.block_rollback()
                if book_scifi:
                    i "Yes, let's go with this."
                    i "It will give my sci-fi book a dark and gruesome tone that will work really well."
                if book_fantasy:
                    i "Yes, let's go with this." 
                    i "It will give my fantasy book a dark and gruesome tone that will be really cool."
                if book_historical:
                    i "Yes, let's go with this."
                    i "I will need to find some interesting rivalry or grudge in History, though."
                        
            "Try something else":
                $ renpy.block_rollback()
                jump v3_writebookchoice
                
    if book_card1 == "call_of_duty":
        i "A call of duty is a good way to get the main character into the conflict. Conscripted by the army, or being part of some special organization..."
        menu:
            "Choose this card":
                $ renpy.block_rollback()
                if book_scifi:
                    i "Making the hero fight for something bigger than himself will make my sci-fi story more relatable and epic."
                    i "And maybe the cause that sets him on his adventure isn't as rigtheous as it seems at first glance..."
                if book_fantasy:
                    i "The call of duty has kickstarted so many classic adventure stories. The hero has to fight for something bigger than himself..."
                    i "It'll work like a charm."
                if book_historical:
                    i "The call of duty has kickstarted so many adventures in History. Wars, conquests, sacrifices..."
                    i "People have been very patriotic during History, dying to protect something they believed bigger than themselves."
                        
            "Try something else":
                $ renpy.block_rollback()
                jump v3_writebookchoice
                
    if book_card1 == "chosen_one":
        i "The Chosen One... I'm I really willing to use this trope?"
        menu:
            "Choose this card":
                $ renpy.block_rollback()
                if book_scifi:
                    i "A Chosen One in a sci-fi novel? I'm not sure I have seen that before..."
                    i "Maybe I can give reason to that pre-destined thing using some deterministic physics or causal loops in space-time!"
                    i "Yeah, that sounds pretty awesome..."
                if book_fantasy:
                    i "A fantasy story needs a Chosen One, right?"
                    i "That should be easy to write..."
                if book_historical:
                    i "A Chosen One in an historical setting? I wonder how I will justify that..."
                    i "History is already written though, so one can argue it was bound to happen that way."
                        
            "Try something else":
                $ renpy.block_rollback()
                jump v3_writebookchoice
        
    play sound "sfx/keyboard.mp3"
    "The book was finally starting to take shape as I began writing the first chapters."
    "There was still a long way to go, but I had a good feeling about this..."
    if v3_write_check:
        jump v3endiansunday
    else:
        scene ianroomnight
        show v2_ianwrite
        with long
        "I spent the whole day writing, so focused I almost lost sight of time."
        i "Enough for today... Time to get back to the real world."
        jump v3iansaturdayafternoon
        
label v3iansaturdayafternoon:
    $ v3_write_check = True
    $ ian_look = 1
    $ fian = "n"
    $ fperry = "n"
    play music "music/perrys_theme.mp3" loop
    i "Now to eat something and get ready for tonight..."
    scene ianhomenight
    show ian at lef
    show perry at rig
    with long
    p "Hey, I finally see your f--{w=0.5}face today."
    i "I was very busy. Have you cooked something for dinner?"
    p "Why should I've cooked something? I'm not your mom."
    i "But you always say you like to cook and brag about how good of a cook you are..."
    p "If you want to ask for s--{w=0.5}something just do it, man."
    $ fian = "smile"
    i "How about one of your delicious home-made pizzas? I bought all the necessary ingredients last week."
    p "You like those, huh? Alright."
    hide perry
    with short
    $ fian = "n"
    show ian at truecenter
    with move
    "I sat on the sofa to relax while Perry cooked. Having him as a flatmate had its pros, too."
    "I decided to waste some time on Peoplegram while I waited for dinner."
    "As I scrolled mindlessly I thought about all that had been happening..."
    if ian_alison_sex:
        "I had really slept with Alison the other night..."
        "I had been so focused on my writing I had barely had time to reflect on that."
        if v2_ian_date:
            "Sleeping with Alison wasn't something I had been really considering, especially since my mind had been quite focused on Lena..."
            i "Lena..."
            if v2_kiss:
                "We had kissed, but I didn't know if that really meant anything."
                i "It has to, though..."
                "But if there really existed something between us... What should I make of what happened with Alison?"
            else:
                "I had the feeling I should feel bad for sleeping with Alison, but there was nothing between me and Lena..."
                "Not yet, at least."
        "I still didn't know what to do with what had happened with Alison. She had been very clear about her not wanting a relationship at the moment."
        "I guess that meant she had no intention of changing the way she saw me. When she said goodbye I felt like nothing had changed between us."
        "I wondered if it had been a one time thing or... To be honest, I had no idea what was on Alison's mind at the moment."
    elif ian_cherry_sex:
        "I had really slept with Cherry the other night..."
        "I had been so focused on my writing I had barely had time to reflect on that."
        if v2_ian_date:
            "It had been so unexpected, especially considering my mind had been quite focused on Lena..."
            i "Lena..."
            if v2_kiss:
                "We had kissed, but I didn't know if that really meant anything."
                i "It has to, though..."
                "But if there really existed something between us... What should I make of what happened with Cherry?"
            else:
                "I had the feeling I should feel bad for sleeping with Cherry, but there was nothing between me and Lena..."
                "Not yet, at least."
            "Besides, Cherry had said she wasn't looking for anything serious. It was just a night of fun."
        else:
            i "I should just be happy it happened and not dwell on it too much."
            i "After all, she said she wasn't looking for anything serious. It was just a night of fun."
        "I wondered if I would find myself in bed with Cherry another time..."
    elif v2_kiss:
        "When I met Lena I never expected I would go on a date with her, let alone kiss her..."
        "I had no idea what to think about that kiss. Did it mean something? It had to..."
    else:
        "I had been meeting people and making progress, something that had been missing in my life for quite some time..."
    if v2_ian_limp:
        "If only I hadn't gone limp that night... Fuck, just thinking about it made me feel so embarrassed."
        if v2_alison_home:
            "I didn't know how I should act in front of Alison next time I saw her..."
        elif v2_cherry_home:
            "Probably I wouldn't see Cherry again, but what if she told Alison? She would probably tell her, wouldn't she?"
        i "I need to get myself together..."
    $ fian = "surprise"
    "My attention was suddenly pulled to a picture that appeared on my feed."
    show ian at left
    with move
    show v3_cindy_peoplegram
    with short
    $ fian = "blush"
    "It was a picture Cindy had posted just yesterday."
    "I couldn't avoid being struck by it."
    "Her blonde and silky hair glistened under the sun of the afternoon, and her green eyes looked bright and deep."
    "She was really beautiful, there was no denying that."
    menu:
        "Comment the picture":
            $ renpy.block_rollback()
            $ ian_go_cindy += 2
            $ fian = "shy"
            "I felt the need to like and comment her picture. It was remarkable like that."
            "I had no idea what to write, though."
            "Should I praise her? Be funny or maybe insightful?"
            menu:
                "{image=icon_wits.png}Insightful comment" if ian_wits > 1:
                    $ renpy.block_rollback()
                    $ v3_cindy_comment = "wits"
                    $ fian = "smile"
                    i "Let's go with witty. That's my specialty."
                    i "{i}I see you can't wait for Summer and Summer probably can't wait for you either!{/i}"
                    i "Something like that..."
                
                "{image=icon_charisma.png}Funny comment" if ian_charisma > 1:
                    $ renpy.block_rollback()
                    $ v3_cindy_comment = "charisma"
                    $ fian = "smile"
                    i "Being charismatic is the best option."
                    i "{i}You really love being lazy! Watch out for sunburns... and voyeurs! {image=emoji_glasses.png}{/i}"
                    i "I enjoy teasing her a bit..."
                
                "{image=icon_lust.png}Praising comment" if ian_lust > 1:
                    $ renpy.block_rollback()
                    $ v3_cindy_comment = "lust"
                    i "She deserves to be praised."
                    i "{i}Looking really beautiful Cindy! {image=emoji_wink.png}{/i}"
                    i "Maybe it's a tad straightforward... But it conveys my feeling."
               
                "Emoji comment":
                    $ renpy.block_rollback()
                    $ v3_cindy_comment = "n"
                    $ fian = "n"
                    i "I don't know what to write... A few emojis will do the trick."
                    i "{image=emoji_100.png} {image=emoji_100.png} {image=emoji_100.png}"
                    i "There. No need to complicate things."
            hide v3_cindy_peoplegram
            with short
            $ fian = "n"
            show ian at truecenter
            with move
        "Like the picture":
            $ renpy.block_rollback()
            $ ian_go_cindy += 1
            "I tapped the screen twice and liked her picture."
            $ fian = "smile"
            i "It's a really good picture... Least she deserves is a like."
            "I wasn't sure what I was trying to accomplish by doing that, if anything at all."
            i "I guess she posted it to get likes, so... I suppose she'll be happy."
            hide v3_cindy_peoplegram
            with short
            $ fian = "n"
            show ian at truecenter
            with move
        "Ignore the picture":
            $ renpy.block_rollback()
            hide v3_cindy_peoplegram
            with short
            $ fian = "n"
            show ian at truecenter
            with move
            "I decided to ignore the picture and keep scrolling."
            "Cindy was beautiful, yeah, but so were many other girls. And she was Wade's girlfriend."
            "There was no reason for me to see her as anything else than a friend, and I stood to gain nothing by liking or commenting her pic."
            "I was going to meet them both in about an hour anyways."
    p "Pizza's almost ready!"
    i "Oh, cool."
    stop music fadeout 2.0
    scene ianhomenight
    with long
    "I had dinner with Perry and went to the bar when it was time."
    
## BAR POOL Game ####################################################################################################################################################################################################################
    
    play music "music/rock_bar.mp3" loop
    scene rockbar
    with long
    $ fian = "smile"
    $ fperry = "n"
    $ fcindy = "n"
    $ femma = "n"
    show ian at lef3
    show perry 
    with short
    i "Here we are again, another night."
    p "This is the place to be. Much better than the other bar."
    p "Oh, there's Emma."
    show emma at rig3
    with short
    e "Hi guys!"
    if v2_ian_date:
        p "So this is the tattoo Ian told me about..."
        e "Oh, yeah. Do you like it?"
        p "Yeah. I think it suits you. Congratulations on getting that job at the record store, by the way."
        e "I see Ian has you up to speed!"
    else:
        p "W--{w=0.5}what's that? You got a tattoo!"
        e "Oh, yeah! Just the other day... I made a bet with a friend that I would get one if I got a job!"
        e "And they just hired me, so..."
        i "So you got a job?"
        e "Yes, at the record store!"
        p "That's so cool! We should go and pay you a visit, then."
        i "Yeah, you were struggling to find a job... Congratulations!"
        i "I would've picked a more significant reason to get a tattoo, though..."
        e "Why? It's not a big deal. It's just skin."
        e "Besides, I had been thinking if I should get one. This was as good an excuse as any other."
        p "I like it."
        e "Thanks!"
    show emma at right
    show perry at rig
    show ian at centerlef
    with move
    show cindy at left
    with short
    c "Hey, there you are!"
    i "Hey, Cindy."
    p "W--{w=0.5}where's Wade?"
    $ fcindy = "serious"
    c "He had some very important game to finish. He'll be joining us later."
    $ fian = "n"
    i "He stayed at home playing video games?"
    p "He was taking part in an on-line championship this weekend. He was very serious about it."
    c "It's so friggin' stupid. There's not even a prize for winning!"
    p "There's the p--{w=0.5}pride of winning."
    c "Nonsense."
    e "Boys will be boys! Let's get some beers!"
    $ fian = "smile"
    $ fcindy = "n"
    "We went to the bar and got some drinks. It turned out Emma knew the barman and she got hers for free."
    $ fperry = "surprise"
    p "How come he gave it to you for free?"
    e "We know each other from the popular assembly."
    $ fperry = "n"
    c "Popular assembly? You're into politics?"
    e "Yeah! I think we the people should take an active role in our city's politics!"
    menu:
        "So you're a political activist?":
            $ renpy.block_rollback()
            i "You've always been into that kind of things, but I didn't know you had become a political activist."
            $ ian_emma += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            $ femma = "serious"
            e "It's hard to keep ignoring the situation... A lot of business owners have joined the assembly since politicians are not protecting people as they should."
            $ fperry = "meh"
            $ fian = "n"
            hide perry
            show perry2 at rig
            with short
            c "I don't know much about politics... What's the situation, exactly?"
            e "The economy's been bad for a few years, but now it's taking a real toll on the citizens. A lot of small businesses have had to close, and most are struggling..."
            e "Look at this place, for example."
            c "Yeah, it's pretty empty..."
            i "It used to be filled to the brim with people."
            e "While local-owned businesses are closing, wealthy businessmen are injecting money into new commercial establishments. But that kind of gentrification only benefits them!"
            e "If you want to run your own business you're forced to shut it down and need to end up working for a measly salary in one of those fancy new places..."
            e "That's if you can even get a job. I got mine at the record store because the owner is a member of the assembly, too..."
            p "Can we p--{w=0.5}please talk about something other than politics?"
            e "Oh, yeah, sorry. I know you don't like the subject."
            $ femma = "n"
            $ fperry = "n"
            $ fian = "smile"
            hide friend_up
            hide perry2
            show perry at rig
            with short
            
        "Let's not talk politics":
            $ renpy.block_rollback()
            $ fian = "n"
            i "Let's not talk politics, please. We're here to have fun."
            p "My t--{w=0.5}thoughts exactly."
            e "Sure."
            $ fian = "smile"
            
    $ fcindy = "flirt"        
    c "Who's in for a game of pool?"
    e "I feel like playing today!"
    p "Alright then..."
    if v1_teamcindy:
        if v1_poolcindywin:
            $ fcindy = "smile"
            c "Ian, you're on my team!"
            i "Oh, OK, sure."
            c "Last time we worked well together and we won, so I'm trusting you!"
            if v1_poolpoints > 2:
                c "You made some really good shots!"
                i "Let's see if I can make it happen again."
        else:
            p "Do you wanna team up with me, Emma?"
            e "Sure!"
            $ fcindy = "serious" 
            c "Then it's you and me, Ian..."
            c "You were pretty awful last time... Don't mess up again, I don't want to lose twice in a row because of you!"
            i "Hey, we're a team... Our victory depends on you, too."
            c "I know, it depends almost exclusively on me! Just don't drag me down with you!"
            $ fian = "sad"
            i "Jeez... You know how to cheer a teammate..."
    if v1_teamwade:
        if v1_poolwadewin:
            $ fcindy = "serious"
            c "Last time you and Wade beat me, so this time you're teaming up with me, Ian."
            i "Oh, OK, sure. You want to be on the winning side."
            $ fcindy = "flirt"
            c "Always."
        else:
            p "Do you wanna team up with me, Emma?"
            e "Sure!"
            $ fcindy = "serious" 
            c "Then it's you and me, Ian..."
            c "You were pretty awful last time... I just hope you don't bring me down as you did with Wade..."
            $ fian = "n"
            i "I'm sure your ability will compensate my lack of it."

## POOL GAME
    $ v1_poolpoints = 0
    $ v1_hitball = 0
    "We moved to the pool table."
    $ fcindy = "n"
    c "Hey, do you wanna bet? To make things more interesting..."
    p "Not a chance."
    c "Too bad... Well, Ian and I will be starting!"
    hide perry
    hide perry2
    show perry2 at rig 
    with short
    $ fperry = "serious"
    p "Why?"
    c "Because it was me who proposed we play."
    p "Since when is that a reason to go first? Let's flip a coin or something..."
    $ fian = "smile"
    i "Don't argue with her, ha ha."
    c "Do you have coins, Ian? I don't have any."
    $ fian = "n"
    i "Yeah..."
    $ fperry = "n"
    "I put some money in the coin slot and the balls rolled out. Cindy set them up and Emma brought us the cue sticks."
    scene v1_pool_bg
    show v1_pool_base
    show v1_pool_cindy1
    show v1_pool_ian1
    with long
    c "Ian, you get the break shot since you put down the coins."
    i "Alright..."
    hide v1_pool_ian1
    show v1_pool_ian2
    with short
    "I aimed down the cue ball and prepared my stroke."
    menu:
        "Hard break":
            $ renpy.block_rollback()
            $ v1_poolpoints += 1
            "A break has to be strong and direct."
            play sound "sfx/cue.mp3"
            "I hit the cue ball hard and sent the frozen balls spiraling across the table in all directions."
            c "You sank a striped one!"
            p "But you also sank a spotted one!"
            c "We'll be playing stripes, then."
            e "Spots for us in that case. Our turn!" 
            
        "Controlled break":
            $ renpy.block_rollback()
            if ian_athletics > 1:
                $ v1_poolpoints += 2
                play sound "sfx/cue.mp3"
                "I was looking for a controlled but determined break, and I got it."
                "I hit the cue ball with enough energy for it to send the frozen balls spiraling across the table and I sank a striped one."
                c "Good shot!"
                e "Seems like we'll be playing spots. Our turn!"                
            else:
                "I tried to be moderate in my break."
                play sound "sfx/cue.mp3"
                "But it turned out too weak and I didn't sink in any of the frozen balls."
                c "What the hell was that? You need to put some energy in it!"
                hide v1_pool_ian2
                show v1_pool_ian1
                with short
                i "Calm down..."
                e "Our turn!"
            
        "Soft break":
            $ renpy.block_rollback()
            "I tried to hit the ball carefully so I wouldn't lose control..."
            play sound "sfx/cue.mp3"
            "My break was too weak and I didn't sink in any of the frozen balls."
            c "What the hell was that? You need to put some energy in it!"
            hide v1_pool_ian2
            show v1_pool_ian1
            with short
            i "Calm down..."
            e "Our turn!"
    scene rockbar
    show emma at right
    show perry at rig
    show ian at centerlef
    show cindy at left
    with short
    play sound "sfx/cue.mp3"
    if v1_poolpoints == 2:
        "Emma took a shot and sank one of her balls."
        p "Nice!"
        e "We're off to a good start!"
        c "We can't let them catch up to us!"
    if v1_poolpoints == 1:
        "Emma took a shot and sank one of her balls."
        p "Nice!"
        e "We're off to a good start!"
        c "We can't let them take the lead like this!"
    else:
        "Emma took a shot and sank a spotted ball."
        p "Nice!"
        c "We're playing stripes, then. Come on, we need to catch up to them!"
    c "My turn now..."
    scene v1_pool_bg
    show v1_pool_base
    show v1_pool_cindy2
    show v1_pool_ian1
    with short
    c "Let's see..."
    play sound "sfx/cue.mp3"
    p "You missed!"
    hide v1_pool_cindy2
    show v1_pool_cindy1
    with short
    c "Shut up! It was a tricky shot! You would've missed it too..."
    "We continued playing until it was my turn again."
    hide v1_pool_ian1
    show v1_pool_ian2
    with short
    i "Let's see..."
    show v3_poolshot1
    with long
    "There were three good candidates for me to strike."
    c "Think, Ian!"
    i "The blue ball seems kinda difficult..."
    if ian_wits > 1:
        i "But maybe I can try a trick shot."
    i "I'm not sure about the yellow one... But I have a good feeling about the red."
    if ian_wits > 1 and ian_athletics < 2:
        "But I would need to hit the ball at a tricky angle, and I wasn't sure I had the skills for that..."
    "Which one should I try to sink in?"
    call screen v3poolgame1
    $ renpy.block_rollback()
    if v1_hitball == 3:
        $ v1_poolpoints += 1
        hide v3_poolshot1
        show v3_poolshot1_c
        with short
        "I calculated the trajectory correctly and managed to sink the ball with a neat cannon."
        i "Yes!"
        c "Great shot, Ian!"
        $ fian = "smile"
        $ fcindy = "smile"
        scene rockbar
        show emma at right
        show perry2 at rig
        show ian at centerlef
        show cindy at left
        with short
        jump v3sankball
    if v1_hitball == 2:
        hide v3_poolshot1
        show v3_poolshot1_b
        with short
        "I tried to go for the yellow ball, but the angle wasn't good and I missed."
        i "Damn!"
        $ fian = "serious"
        $ fcindy = "serious"
        scene rockbar
        show emma at right
        show perry at rig
        show ian at centerlef
        show cindy at left
        with short
        c "You missed! You should've gone for another ball!"
        i "I know, you don't have to point it out."
        c "We're not gonna win if you keep missing..."
        i "Hey, you missed too!"
        c "Shut up..."
        jump v3gamecontinue
        
    if v1_hitball == 1:
        if ian_athletics  > 1:
            $ v1_poolpoints += 1
            hide v3_poolshot1
            show v3_poolshot1_a
            with short
            "I managed to hit the ball at the right angle and sank it."
            i "Yes!"
            c "Nice shot, Ian!"
            $ fian = "smile"
            $ fcindy = "smile"
            scene rockbar
            show emma at right
            show perry2 at rig
            show ian at centerlef
            show cindy at left
            with short
            jump v3sankball
        else:
            hide v3_poolshot1
            show v3_poolshot1_ab
            with short
            $ fian = "serious"
            $ fcindy = "serious"
            scene rockbar
            show emma at right
            show perry at rig
            show ian at centerlef
            show cindy at left
            with short
            c "You missed! How could you miss that one? It was so easy!"
            i "It wasn't as easy as it seemed..."
            c "We're not gonna win if you keep missing..."
            i "Hey, you missed too!"
            c "Shut up..."
            jump v3gamecontinue
    
    menu v3sankball:
        "It's too soon to celebrate":
            $ renpy.block_rollback()
            $ fian = "n"
            i "It's too soon to celebrate... The game's still on, and it's very close."
            c "I'm just trying to be hopeful!"
            p "Hope won't save you!"
          
        "I wont let you down":
            $ renpy.block_rollback()
            $ fian = "happy"
            i "I'm on fire today! Don't worry, I won't let you down, we're gonna win this."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            "Cindy high-fived me."
            c "I trust you! Let's go!"
            if ian_cindy < 10:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_cindy += 1
            p "Don't be so cocky! You're not a pro, so don't act like one."
            i "I'm not gonna stop sinking balls, if that's what you're asking!"
            p "We'll see if your luck continues..."
            
        "I've got this":
            $ renpy.block_rollback()
            $ fian = "confident"
            i "I've got this figured out. Don't worry, I see the table and I'm several moves ahead."
            i "Our balls are in the perfect position... We'll win this."
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            "Cindy patted me on the back."
            c "You sound confident! I'll trust you."
            if ian_cindy < 10:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_cindy += 1
            p "You're just being arrogant. This is pool, not chess! It's not like you can plan your moves ahead of time."
            i "That's what you think."
            p "We'll see. It all depends on where the cue ball is, and you can't control that, so..."
        
        "Make a sexual innuendo" if ian_go_cindy > 0:
            $ renpy.block_rollback()
            $ fian = "confident"
            $ ian_go_cindy = 3
            i "I know how to slide it in properly..."
            i "A determined, strong thrust is necessary."
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            $ fcindy = "flirt"
            c "That's one way to do it, indeed. But don't get too carried away and overdo it, or you will miss your shot."
            i "Of course. I'm a civilized man, I know technique beats brute strength."
            i "And I know the importance of planning the shot before executing it."
            c "Glad to see you're aware of the recipe for success..."
            if ian_cindy < 10:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_cindy += 1
    
label v3gamecontinue:        
    $ fian = "smile"
    $ fcindy = "n"
    "We continued on with the game."
    play sound "sfx/cue.mp3"      
    "Perry made his move and he sank another ball in."
    $ fperry = "smile"
    p "Hell yeah! I'm the boss!"
    $ femma = "smile"
    e "Good job!"
    "They were playing really well..."
    "It was Cindy's turn again. She got into position, took aim and..."
    play sound "sfx/cue.mp3"
    $ fcindy = "surprise"
    $ fian = "worried"
    c "No!"
    p "Ha ha, you missed again! And that was a very easy shot!"
    $ fcindy = "sad"
    c "I don't know what's going on with me tonight..."
    $ fian = "n"
    if v1_poolpoints == 3:
        i "Don't worry... We can still take this."
        play sound "sfx/cue.mp3"
        "Emma sank yet another ball in and it was my turn again."
        "I had to make this shot count, or they would catch up to us. I needed to score..."
    elif v1_poolpoints > 0:
        i "We can still take this..."
        play sound "sfx/cue.mp3"
        "Emma sank yet another ball in and it was my turn again."
        "I had to make this shot count, or we were doomed. If I failed there was no way we could catch up with them..."
    else:
        i "I don't see us winning this... But it's just a game, so let's play."
        play sound "sfx/cue.mp3"
        "Emma sank yet another ball in and it was my turn again."
        "Even if I made this shot count I doubted we could catch up with them..."
    scene v1_pool_bg
    show v1_pool_base
    show v1_pool_cindy1
    show v1_pool_ian2
    with short
    "I chalked the cue stick and took aim."
    show v3_poolshot2
    with short
    "Perry and Emma had just one ball into play. After sinking that one they could go and try to finish the game."
    "Cindy and I were not done yet. We had a couple of balls to take care of before going for the eight-ball..."
    c "The green ball is almost in, but we have a spotted ball blocking the way..."
    i "Their only ball left..."
    p "You can do us a favor and put it in for us!"
    i "I could try and go for the purple ball, since we're gonna need to sink that one too eventually..."
    $ v1_hitball = 0
    call screen v3poolgame2
    $ renpy.block_rollback()
    if v1_hitball == 1:
        $ v1_poolpoints -= 1
        hide v3_poolshot2
        show v3_poolshot2_a
        with short
        "I tried to go for the purple ball, but I wasn't really sure of what I was trying."
        "I hit the ball, but didn't do anything useful with it."
        c "No! That was terrible!"
        i "I'm doing what I can!"
    if v1_hitball == 2:
        $ v1_poolpoints += 1
        hide v3_poolshot2
        show v3_poolshot2_b
        with short
        "I made a bet, trying to hit the green ball while avoiding the spotted one... And it paid off!"
        c "Awesome!"
        p "How the hell did you pull that off?"
        e "I thought you weren't too good at this, Ian!"
        i "Maybe I'm better than I thought."        
    if v1_hitball == 3:
        hide v3_poolshot2
        show v3_poolshot2_c
        with short
        "I decided to go for the guaranteed scoring and I took the direct path."
        "I made sure to sink our ball in, but I also sank the spotted one..."
        p "Nice! Thanks, dude."
        c "Was that really necessary, Ian?"
        i "I didn't see any other way. At least I sank one of ours, too."
    $ fperry = "n"
    $ femma = "n"
    scene rockbar
    show emma at right
    show perry at rig
    show ian at centerlef
    show cindy at left
    with short
    "The game was almost ending."
    if v1_poolpoints == 4:
        $ v3_pool_win = True
        "We managed to be one step ahead and ended up beating Perry and Emma."
    elif v1_poolpoints == 3:
        $ v3_pool_win = True
        "It was a very close call, but we ended up beating Perry and Emma."
    else:
        "Finally Perry and Emma got the victory."
        $ fperry = "smile"
        $ femma = "smile"
    if v3_pool_win:
        $ fcindy = "smile"
        $ fian = "happy"
        $ fperry = "meh"
        hide perry
        show perry2 at rig
        with short
        c "Yes! We did it!"
        c "Well played, Ian!"
        "She held up her fist."
        menu:
            "{image=icon_charisma.png}Exploding fist bump!" if ian_charisma > 1:
                $ renpy.block_rollback()
                "That victory deserved an exploding fist bump!"
                "I bumped her knuckles and opened my fingers with a dramatic effect."
                $ fcindy = "flirt"
                with vpunch
                ic "Boom!"
                if ian_cindy < 10:
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    $ ian_cindy += 1
                "Seems like Cindy had been thinking the same, since we did it at the same time!"
                $ fcindy = "smile"
                c "That was fun!"                
            
            "Fist bump":
                $ renpy.block_rollback()
                "I bumped Cindy's knuckles, but then she followed up openeing her fingers with a dramatic effect."
                c "Boom..."
                $ fcindy = "blush"
                $ fian = "worried"
                "I failed to do the same."
                c "Oh, I thought we were doing the exploding fist bump."
                c "This victory deserved it..."
                i "Oh, yeah..."
                $ fperry = "smile"
                p "He left you hanging, ha ha."
                $ fcindy = "serious"
                c "No, he didn't."
                $ fian = "smile"
                i "It was just a miscommunication, ha ha. We still won!"
                $ fcindy = "n"
                c "Yeah."
                
            "Leave her hanging":
                $ renpy.block_rollback()
                $ fian = "n"
                i "You didn't play too well today. We won mainly because of me."
                $ fcindy = "sad"
                "I turned around left her hanging."
                play sound "sfx/frienddown.mp3"
                show friend_down
                $ ian_cindy -= 1
                $ fcindy = "serious"
                c "Jackass."
                
        $ fperry = "n"
        hide perry2
        show perry at rig
        with short
    
    else:
        $ fian = "sad"
        $ fperry = "happy"
        $ femma = "smile"
        $ fcindy = "mad"
        p "Ha! We got you!"
        if v1_teamcindy and v1_poolcindywin == False:
            c "Fuck! We lost again!"
        else:
            c "Fuck! We lost!"
        c "You're awful at this, Ian!"
        play sound "sfx/frienddown.mp3"
        show friend_down
        $ ian_cindy -= 1
        $ fian = "serious"
        i "Hey, don't blame just me. You played like crap, too."
        c "Shit..."
        e "Don't get mad, it's just a game!"
        c "Easy to say when you're the winner..."
        i "She's right you know...?"
        c "Whatever."
        hide friend_down
        
## WADE ARRIVES    
    scene rockbar
    show perry at rig5b
    show ian at truecenter
    show emma at right5
    show cindy at lef5
    with move
    $ fwade = "n"
    show wade at left5
    with short
    w "Hey."
    $ fian = "n"
    $ fcindy = "n"
    c "Oh, look who decided to finally show up..."
    p "How was the t--{w=0.5}tournament? Did you win?"
    w "Nah... Some guys are just too good. All they do is play all day long, there's no way of beating them."
    c "Considering you spend most of the day playing, too, I'm surprised you're unable to."
    w "I have a job, too, you know? Though it would be a dream getting paid for playing video games..."
    c "Well, yeah, keep dreaming."
    $ fian = "smile"
    $ fcindy = "n"
    i "We just finished a game of pool. Let's get another beer."
    $ fwade = "smile"
    w "Sure, that's why I came here."
    $ fperry = "n"
    $ femma = "n"
    "We grabbed some more drinks and sat to chat."
    w "Hey, nice tattoo Emma. It's cool."
    e "Thanks!"
    c "Ian, have you shown them the video I sent you yesterday?"
    i "Oh, no. Do you guys want to take a trip down memory lane?"
    scene rockbar
    show v3_memory
    with short
    e "Oh my!"
    p "Where did you get this?"
    w "It was stored on an old hard-drive of mine... Cindy was poking around and found it."
    i "So you expressly searched for it?"
    c "Yeah, I wanted to see you guys playing back in the day!"
    e "That's so funny, ha ha! Look at your hair guys!"
    i "We had some manes on our heads, yeah..."
    c "Except Perry. Look at you, singing so full of energy..."
    p "Well, yeah... I had fun with it. Those were other t--{w=0.5}times."
    e "You look good with shorter hair."
    c "And with less belly, ha ha."
    p "Hey!"
    e "Look at you Ian, you look so much like an angsty teenager! Head and shoulders down and staring at the floor all the time..."
    i "That's because I was an angsty teenager, don't you remember? And Wade already had a beard at sixteen, ha ha."    
    scene rockbar
    show perry at rig5b
    show ian at truecenter
    show emma at right5
    show cindy at lef5
    show wade at left5
    with short
    c "You guys changed so much..."
    i "For the better, I hope."
    w "Of course. Except Perry, ha ha."
    p "S--{w=0.5}shut up already."
    c "Looking at you now it's hard to believe you four played in a rock band."
    i "The good old times. We were just trying to find what our passion was."
    $ fian = "sad"
    "Looking at us now, though... It was hard not to see how none of those passions had been fulfilled."
    "All that youthful energy seemed to have been gone to waste. Neither Emma nor Perry, Wade or me had achieved our dreams."
    "Well, maybe Wade... But his life didn't seem too full of passion. Emma and I were still struggling, and Perry, well... He was a whole other story."
    "Could it possibly be that we had grown up to be a bunch of losers...?"
    "Cindy noticed something was wrong with me."
    c "What's with the long face all of a sudden?"
    "I shook those thoughts from my head."
    $ fian = "smile"
    i "Oh. It's nothing."
    if v1_alisonlunch:
        w "So Jeremy is not coming today either? What about Alison?"
    else:
        w "So Alison and Jeremy are not coming today either?"
    p "We saw them on Thursday."
    c "Oh, yeah?"
    i "Yeah, we went with Alison and a friend of hers to this cocktail bar called Shine."
    c "You didn't tell us anything!"
    p "We thought you wouldn't be interested."
    w "You thought right."
    c "Talk for yourself. So, a cocktail bar?"
    if ian_chad == 2:
        i "Yeah, it was pretty cool! I liked it, and we had fun."
    elif ian_chad == 1:
        i "Yeah, a bit on the expensive side, but it was cool. We had fun."
    else:
        i "Yeah, a bit too posh for my taste, but we had fun nonetheless."
    "We told them a bit about our night."
    if perry_cherry > 1:
        $ fperry = "smile"
        p "We met this really cool girl, Cherry. She's Alison's co-worker and also super beautiful..."
    else:
        p "There was this girl named Cherry, Alison's co-worker..."
    i "And we ended the night with a couple of rounds of tequila shots."
    if alison_jeremy:
        $ fperry = "meh"
        p "Well, Alison and Jeremy ended the night in another way, probably..."
        $ fcindy = "surprise"
        $ femma = "surprise"
        $ fian = "n"
        w "Jeremy and Alison? No way."
        p "Yup."
        i "We still don't know for sure... But it's most probable, yeah."
        c "That guy can't keep it in his pants, can he?"
        $ femma = "n"
        e "He wasn't like that before."
        $ fcindy = "n"
        i "People change."
        w "Good for him. He seems to be enjoying himself."
        i "He sure is..."
    if ian_alison_sex:
        $ fperry = "flirt"
        p "Ian and Alison got along in a very close way, you could say."
        $ fian = "serious"
        play sound "sfx/punchgym.mp3"
        with vpunch
        "I elbowed Perry to make him shut up."
        $ fperry = "meh"
        $ fwade = "happy"
        $ fcindy = "surprise"
        w "You and Alison? For real?"
        $ fian = "blush"
        i "Is it that strange?"
        e "I don't think it is. I always thought you two clicked so well together back in high school."
        i "Really?"
        w "You always had a good relationship, that's true."
        i "I don't know, a lot of time has passed since then. We're different people now."
        w "You seem to get along better than before, ha ha."
        i "OK guys, that's enough about that..."
    elif ian_cherry_sex:
        $ fperry = "flirt"
        if alison_jeremy:
            p "Jeremy was not the only one who scored, though..."
        p "Ian and Cherry got along really well."
        $ fian = "shy"
        $ fwade = "happy"
        w "You scored with Alison's friend?"
        if v2_ian_date == False:
            p "And turns out Cherry's a model..."
            $ fcindy = "surprise"
            w "Really? Dude, what the hell? You're on fire!"
            $ fcindy = "serious"
            e "So you're getting intimate with models now, Ian?"
            i "Shut up guys, it's not like that... We just saw some pictures on her Peoplegram, she's probably an amateur..."
            p "Still, she's so damn hot. An ebony beauty!"
        else:
            i "Yeah... It seems we had chemistry, so... It just happened."
            e "Good for you!"
            p "Good for him? He's a lucky bastard."
            p "She's so damn hot! An ebony beauty!"
            w "Nice!"
            $ fcindy = "serious"
        i "OK guys, that's enough about that..."
    $ fian = "n"
    $ fcindy = "n"
    $ fwade = "n"
    c "Sounds like you had fun alright..."
    $ fperry = "n"
    $ fian = "n"
    if v2_ian_date:
        $ femma = "smile"
        e "So Ian, will you tell me who that girl was you came with to the record store?"
        $ fian = "blush"
        w "A girl?"
        e "Yeah, a very beautiful, dark-haired girl... I'd say you two were on a date!"
        i "It wasn't a date... Not exactly."
        $ fian = "n"
        i "Her name's Lena. I met her a couple of weeks ago at the café..."
        "I told them my story with Lena, aided by Perry."
        $ fwade = "happy"
        w "So she's a model? Good going, dude!"
        if ian_cherry_sex:
            p "Turns out Cherry's also a model..."
            $ fian = "shy"
            w "Dude, what the hell? You're on fire!"
            $ fcindy = "serious"
            e "Look at Ian, he's becoming a true women magnet!"
            i "Shut up guys, you know it's not like that..."
            $ fcindy = "n"
        c "So is there something between you two?"
        if v2_kiss:
            i "No, I mean... Seems like we like each other, yeah, but it's too soon to be sure about anything..."
            p "It's obvious there's some ch--{w=0.5}chemistry though."
        else:
            i "No, nothing happened. We're just getting to know each other."
            i "It's too soon to be sure about anything..."
        w "At this rate even Jeremy will get jealous of you, ha ha."
        i "I'm the first one to be surprised about all of this."
        e "You shouldn't. You're a cool guy, it's not that weird that girls like to be around you."
        $ fian = "blush"
        i "Oh... Thanks, Emma."
        if ian_alison_sex:
            $ fcindy = "flirt"
            c "So, Alison and then this model... Don't tell me you've become a womanizer, Ian."
            i "It's not like that!"
            c "If you say so..."
            $ fcindy = "n"
        elif ian_cherry_sex:
            $ fcindy = "flirt"
            c "So, this girl named Cherry and then this other model... Don't tell me you've become a womanizer, Ian."
            i "It's not like that!"
            c "If you say so..."
            $ fcindy = "n"
    $ fian = "n"
    $ fwade = "n"
    i "Can we stop talking about my personal life now? I feel it's all we talk about recently..."
    e "That's because it's pretty interesting!"
    $ fian = "smile"
    i "Oh, if that's the case... I still haven't told you guys about the book review I had to write for my bitchy boss..."
    "We kept chatting as we drank some more beer."
    "The spirits were high and as we finished the second round Cindy made a proposal."
    $ fcindy = "smile"
    c "Hey guys, I was thinking... That bar you went to with Alison, Shine, it sounded pretty cool."
    c "Why don't we go there some time? In fact, we could end the night there. I fancy a cocktail!"
    w "No way."
    $ fcindy = "serious"
    c "Why not?"
    w "I have no interest in going to such a place."
    c "Well, I do."
    w "You have some really stupid interests sometimes..."
    $ fcindy = "mad"
    c "Says the one who's only interested in his dumb video-games!"
    $ fian = "worried"
    $ fperry = "meh"
    $ femma = "sad"
    $ fwade = "serious"
    c "I'm getting a bit tired of having to drag you off the couch, you know?"
    w "I just don't like those kind of bars, is that my fault?"
    c "Yes, it is."
    p "I'm on Wade's side here, we're much more c--{w=0.5}comfortable in here. There's no reason to move..."
    $ fian = "serious"
    play sound "sfx/punchgym.mp3"
    with vpunch
    if ian_alison_sex:
        "I elbowed Perry again. He was so clueless and such a blabbermouth sometimes..."
    else:
        "I elbowed Perry to make him shut up. He was so clueless and such a blabbermouth sometimes."
    $ fperry = "serious"
    hide perry
    show perry2 at rig5b 
    with short
    $ fcindy = "serious"
    c "I'm not asking for you to love these kind of places, just to stop complaining and go along with something I enjoy for once."
    $ fian = "sad"
    w "Well, I'm sorry, I just don't enjoy those shitty places!"
    c "Gosh! Sometimes I feel like I'm actually dating Perry!"
    p "Hey, what's that s--{w=0.5}supposed to mean?"
    "Nobody paid attention to his complaint."
    $ fcindy = "mad"
    c "I want to go to that bar tonight, and I will."
    w "You're free to go, but you'll be going alone."
    c "I don't care! I will, if I have to!"
    "She looked at us."
    c "Guys, is anybody up for it?"
    p "Not a chance."
    e "I can't... I have an assembly meeting early in the morning tomorrow. I was just about to call it a night, in fact."
    "Cindy looked at me. I was the only one left."
    menu:
        "{image=icon_friend.png}I'll go with you" if ian_cindy > 3:
            $ renpy.block_rollback()
            $ v3_cindy_date = True
            $ fian = "smile"
            i "Alright, I'll go with you."
            $ fcindy = "n"
            c "Good!"
            p "Really, dude?"
            $ fian = "n"
            i "We can't leave her alone..."
            p "It's her who's hellbent on going. If she wants to go so badly..."
            w "It's OK, let them go."           
            c "Let's go, Ian!"
            i "I'm coming... Bye, guys."
            stop music fadeout 2.0
            jump v3iancindydate
            
        "I'll pass":
            $ renpy.block_rollback()
            $ ian = "worried"
            i "I'm sorry Cindy, but I'll pass, too..."
            if v3_holly_date:
                i "I'm meeting a colleague tomorrow morning to work on that book review I told you about..."
            else:
                i "I'm not really feeling it..."
            i "And honestly I'm not sure we're in the best mood to enjoy it right now..."
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_cindy = 2
            c "What do you know about my mood?"
            c "Whatever, I don't need you guys to come with me."
            e "I'd go with you but I really can't..."
            c "It's OK, Emma. I said I didn't mind going alone and I don't!"
            "Wade answered her in a dismissive tone."
            w "Have fun."
            c "I will."
            hide cindy
            with short
            i "..."
            $ fperry = "sad"
            p "That was t--{w=0.5}tense."
            w "She's so fucking stubborn sometimes!"
            i "You're stubborn as an ox, too, dude."
            w "Whatever. She'll come around. It's not the first time we fight."
            $ fwade = "n"
            w "I'm going home."
            e "Yeah, me too."
            i "Let's call it a night, then..."
            stop music fadeout 2.0
            jump v3iansunday
            

##CINDY NIGHT DATE ####################################################################################################################################################################################################################

label v3iancindydate:
    $ axel_look = 2
    $ faxel = "n"
    scene street2night
    with long
    $ fcindy = "serious"
    "I followed Cindy out of the bar."
    show ian at lef
    show cindy at rig
    with long
    c "Where's that place?"
    i "It's not too far from here. We can go by foot."
    $ fcindy = "n"
    c "OK, lead the way."
    "I wasn't sure if this had been a good idea after all."
    "Cindy and Wade had just had a pretty big argument and going with her to the bar could look like I was taking sides."
    "And the mood was kinda tense after that..."
    play music "music/edm.mp3"
    scene cocktailbar
    with long
    $ fcindy = "smile"
    "The first thing I noticed when we arrived at Shine was the music. It was different from last time."
    "That night the atmosphere was more festive and even more crowded. People drank and danced to the loud music."
    show cindy2 at rig
    show ian at lef
    with short
    c "So this is the place! I like it!"
    c "Let's get a drink!"
    "We made our way through the crowd until we reached the bar. We asked for a couple of cocktails and leaned on the bar to drink them."
    "I had no idea what Cindy's mood was like at that moment, so I decided to test the waters." 
    i "How are you feeling?"
    c "What?"
    "The music was loud, so I had to lean closer to hear and raise my voice."
    i "How are you feeling after what happened at the bar?"
    $ fcindy = "n"
    c "Well... I'm pissed, but I don't want to let that sour my night!"
    menu:
        "{image=icon_wits.png}I'm concerned about Wade" if ian_wits > 1:
            $ renpy.block_rollback()
            i "You know... I'm a bit concerned about Wade."
            c "What do you mean?"
            i "His attitude... He barely wants to go out with us anymore or any other stuff. It's like he's lost his fire."
            $ fcindy = "sad"
            c "Yeah... He wasn't like that when I met him."
            i "Well, he was always a bit like that. Chill, taking things easy, never trying too hard..."
            c "Yeah, but I kind of liked that about him. He was cool, I guess. But he used to be more active."
            i "Something happened to him?"
            c "I wouldn't say so... I mean, I know he's not exactly thrilled with his job, but it's not like he's depressed or anything..."
            c "It's just that he's not interested in doing anything anymore! Just staying home, playing his video games, maybe going out with me once or twice a week..."
            c "It's pretty drab, to be honest!"
            i "I wish I knew what to tell you, but you know him better than I at this point."
            c "I guess... Whatever."
            
        "Are things OK with Wade?":
            $ renpy.block_rollback()
            i "Are things with Wade... OK?"
            $ fcindy = "serious"
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_cindy -= 1
            c "I don't want to talk about that now, OK?"
            c "Thinking about how stupid he is sometimes will only piss me off, and I'm trying to have fun."
            i "Sure, OK. Sorry."
            hide friend_down
            
        "Drop the subject":
            $ renpy.block_rollback()
            i "Let's not talk about it, then."
            c "Yeah, that'll be better."
            
    if ian_alison_sex:
        $ fcindy = "flirt"
        c "Let's talk about you! So you and Alison are more than just friends now..."
        $ fian = "worried"
        i "I wouldn't say that... At least that's not the feeling I got..."
        $ fcindy = "n"
        c "So it didn't go well?"
        i "Oh no, it did. But it's just... I know she's not looking for a relationship, and I guess neither am I."
        c "I wasn't saying that you had become a couple. Maybe just colorful friends."
        i "\"Colorful friends\"?"
        c "It means friends with benefits. Fuck buddies!"
        i "Yeah, yeah, I got that. I don't know. It just happened that once and we haven't talked over it yet."
        c "I see... It doesn't surprise me that it happened, though."
        $ fian = "n"
        i "It doesn't?"
        c "Nope. I always thought you had good chemistry..."
        if v2_ian_date:
            c "But you really are a player! Seems you don't have enough with just one girl..."
    elif ian_cherry_sex:
        $ fcindy = "flirt"
        c "Let's talk about you! So you got with Alison's friend... What does she think of it?"
        i "Alison? I don't know. She didn't say anything. She was busy herself with Jeremy."
        $ fcindy = "n"
        c "Alison and Jeremy... I don't know them that much, but they look like an odd couple to me."
        c "I never saw them having much in common."
        i "I don't know about that... But they're not looking for a serious relationship, I can tell you that."
        c "Even those two becoming friends with benefits looks odd to me, but I guess I can kind of see it if it was just a one-night stand."
        i "I have no idea about that."
        $ fcindy = "flirt"
        c "But we were not talking about them. Tell me about that girl, Cherry. She's a model?"
        i "Judging by some of her pictures it seems she's done some modeling, yeah..."
        c "I see... So it was the first time you were meeting her and she ended up at your place? I didn't know you were such a player, Ian!"
        $ fian = "smile"
        i "How's that being a player? You could say she was the one taking the initiative, to be honest."
        c "Oh, so she threw herself at your neck?"
        i "Not like that, dummy. But yeah, seems like she liked me and decided she wanted a taste, ha ha."
        c "So are you going to see her again or...?"
        i "I don't know, maybe. It was a pretty great experience."
        c "Hmmm..."
        if v2_ian_date:
            c "You really are a player! Seems you don't have enough with just one girl..."
    elif alison_jeremy:
        c "So Alison and Jeremy, huh...? I don't know them that much, but they look like an odd couple to me."
        c "I never saw them having much in common."
        i "I don't know about that... But they're not looking for a serious relationship, I can tell you that."
        c "Even those two becoming friends with benefits looks odd to me, but I guess I can kind of see it if it was just a one-night stand."
        i "I have no idea about that."
        if v2_ian_date:
            c "Well, they're not the only ones having fun, are they?"
    if v2_ian_date:
        $ fcindy = "flirt"
        c "Tell me more about that girl you met at the café! Her name's Lena, right?"
        i "Yeah. What do you want me to tell?"
        $ fcindy = "flirt"
        c "So she's a nude model?"
    else:
        $ fcindy = "n"
        if ian_alison_sex or ian_cherry_sex:
            c "So, any other girl-related stories to tell?"
        else:
            c "What about you? Any other girl-related stories to tell?"
        i "Not really, I guess..."
        if v2_alison_home:
            "I didn't want to tell her about my disastrous night with Alison. Thankfully Perry hadn't brought up the subject while we were with the others."
        elif v2_cherry_home:
            "I didn't want to tell her about my disastrous night with Alison. Thankfully Perry hadn't brought up the subject while we were with the others."
        i "I met a girl recently, but we're just friends. She's pretty cool, though."
        c "Really? Who's she?"
        "I told her about Lena and our spontaneous meetings."
        $ fcindy = "flirt"
        c "I see! So she's a nude model?"
    c "No wonder you're interested in her..."
    $ fian = "n"
    if v2_ian_date:
        i "You think that's the only reason?"
        c "Don't tell me you don't like it."
    else:
        i "I never said I was interested in her..."
        c "Come on, don't tell me you're not interested in a girl who does nude modeling..."
    menu:
        "I love it":
            $ renpy.block_rollback()
            $ fian = "happy"
            i "Of course, I love it. It's super sexy."
            play sound "sfx/xp.mp3"
            show lust_up
            $ ian_lust_xp += 1
            call screen skillsup
            c "I knew it... So you think it's sexy? Come on, show me! I want to see her pictures."
            
        "It's cool":
            $ renpy.block_rollback()
            $ fian = "smile"
            i "Sure, I think it's cool. It's artistic and beautiful, and out of the ordinary, that's for sure."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            c "Artistic and beautiful? Come on, I know how you guys really think..."
            c "Show me! I want to see her pictures."
            
        "I don't really like it":
            $ renpy.block_rollback()
            i "I don't have anything against it, but it's something a bit out of my comfort zone."
            $ fcindy = "n"
            c "Why? Are you intimidated by it?"
            i "I don't know if that's the case. It's just something I'm not used to. And I guess I wouldn't feel comfortable doing it if it was me."
            c "I'm curious now. Show me! I want to see her pictures."
            
    "I guessed there was no harm in showing her."
    i "Wait, I'll show you her Peoplegram..."
    show ian at left
    show cindy2 at right
    with move
    show v1_peoplegram
    if v1_rss_quote == 1:
        show v1_peoplegram_a
    elif v1_rss_quote == 2:
        show v1_peoplegram_b
    elif v1_rss_quote == 3:
        show v1_peoplegram_c
    with short
    $ fcindy = "surprise"
    c "She's so beautiful! Oh my God!"
    $ fian = "smile"
    "She scrolled and looked as some of Lena's pics. She didn't have many anyways."
    $ fcindy = "n"
    c "I love those pictures... they look really professional."
    hide v1_peoplegram
    hide v1_peoplegram_a
    hide v1_peoplegram_b
    hide v1_peoplegram_c
    with short
    show ian at lef
    show cindy2 at rig
    with move
    c "Quite a lot of girls do this nowadays... Becoming Peoplegram models..."
    i "You sound like you have thought about it, too."
    c "I don't know. I'm not sure if it's for me."
    c "Though I would like to have some pictures like that... They look super pretty."
    hide friend_up
    if ian_go_cindy > 0:
        hide friend_up
        i "I'd say you like posing, considering your last Peoplegram pic."
        if v3_cindy_comment == "lust":
            $ fcindy = "flirt"            
            c "Oh yeah, you commented that I was looking beautiful..."
            $ fian = "confident"
            i "You really were."
            c "So I'm only beautiful in my pictures?"
            i "You're looking pretty good right now."
            $ cindy= "smile"
            if ian_cindy < 10:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_cindy += 1
            c "Good to know."
            $ fian = "smile"
            hide friend_up
        elif v3_cindy_comment == "wits":
            c "Oh yeah, you commented something about Summer not waiting for me or something? I didn't really understand..."
            $ fian = "n"
            i "I was just trying to be kinda poetic, or something like that."
            c "I didn't get it. Thanks for the like and the comment anyways!"
        elif v3_cindy_comment == "charisma":
            i "Maybe you're looking for voyeurs after all..."
            $ fcindy = "smile"
            c "Ha ha ha, don't be silly! Your comment made me laugh. But I'm not lazy!"
            "She punched me playfully on the arm."
            if ian_cindy < 10:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_cindy += 1
        elif v3_cindy_comment == "n":
            c "Oh yeah, thanks for the emojis."
            i "You deserved all of them, ha ha."
        else:
            c "Oh, so you liked it?"
            i "Yeah, you looked pretty stunning."
            c "Thanks!"
    hide friend_up
    c "Let's get another drink!"
    i "You finished that one fast!"
    "I drank up what was left of my cocktail and Cindy asked for two more."
    "I had had my doubts about going out with Cindy tonight, but I was having fun after all."
    "Though she seemed very keen on asking about my life..."
    $ fcindy = "n"
    c "Say, Ian, back at the bar, what had you looking so sad?"
    $ fian = "n"
    i "Huh? What are you talking about?"
    c "After watching the video you stayed quiet for a moment, like you were far from there... What was going through your mind?"
    i "You have a really keen eye, you know that?"
    c "I do. I know how to read people."
    i "It was nothing. Nostalgia, maybe."
    i "Seeing everyone so young, so naive..."
    i "And I guess I couldn't avoid comparing our teenage selves with who are now. And that comparison got a bit bleak."
    $ fcindy = "sad"
    c "Why?"
    i "I just got assaulted by the thought that we're all still struggling... None of us has made it big, none of us has achieved their dreams yet."
    i "It's like we're still chasing the same train we chased when we were sixteen."
    i "And I wondered if we're still on time to get on board."
    c "Oh..."
    $ fian = "smile"
    i "But don't mind me! Sometimes I'm just pessimistic like that, but I get over it."
    $ fcindy = "n"
    c "Don't worry, it's a thought we all have. I think the same, too."
    c "Life's not as my sixteen-year-old-self pictured it, I guess."
    i "How did you picture it?"
    c "To be honest, I never had a clear picture in my head. I guess I just wanted to have fun, feel fulfilled and all that jazz..."
    $ fcindy = "sad"
    c "But I don't know. I'm twenty-five now, working a nine-to-five at my father's company and living with my boyfriend... Seems like I'm already set up."
    c "But I still feel I'm not sure what I really want..."
    $ fcindy = "n"
    c "That's something I really envy you for, Ian."
    i "Me? How so?"
    c "You're very clear on what your passion is. I can see it when you talk about writing your book and all that art-related stuff."
    c "Even if it's hard and you're not having much luck with it, you never thought of quitting. Or at least, you never did quit."
    c "For you writing is not just a hobby. It's something that kinda drives your whole life, isn't it?"
    $ fcindy = "sad"
    c "I don't feel I have something like that... Sometimes I just feel I don't have a passion."
    i "It's often the case that you just need to try different things until you find it... But I'm sure there's something you'd like to do."
    c "Sometimes I thought I would like to do something artistic. It looks so glamorous and cool..."
    c " But I don't know much about art, and I can't draw, or paint, or sing, or even write..."
    c "I'd like to be creative like you, Perry or Emma, but I guess I'm just not. So I'm just stuck not knowing what to do."
    menu:
        "{image=icon_wits.png}+{image=icon_charisma.png}Don't give up!" if ian_wits > 0 and ian_charisma > 1:
            $ renpy.block_rollback()
            i "Don't give up! I've had that feeling many times. Feeling that I'm not good enough at what I like..."
            i "That I don't have the talent, so I should just quit. But that's nonsense."
            i "When you have a passion you pursue it for the sake of it. Because you enjoy it, and because you can't just stop."
            i "Maybe you haven't found your calling yet, but don't shy away from things. Even if you're not too good at them the only thing that matters is that you enjoy doing them."
            i "So find whatever it is you feel like doing and just do it. Becoming good at it will come naturally."
            $ fcindy = "smile"
            if ian_cindy < 10:
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_cindy += 1
            c "You're right. Thanks for the pep talk, that really cheered me up! Now let's do something more fun!"
            c "I feel like dancing, so let's pay for these drinks and jump on the dance floor!"
            hide friend_up
        "Find something else":
            $ renpy.block_rollback()
            i "Find something else. There's a lot of stuff you can be passionate about."
            i "Cooking, traveling, animals, movies... I don't know."
            $ fcindy = "n"
            i "There's a whole big world out there for you to explore. You'll find something."
            c "I guess I will. Thanks for the pep talk! Now let's do something more fun!"
            c "I feel like dancing, so let's pay for these drinks and jump on the dance floor!"
        "Art isn't worth it":
            $ renpy.block_rollback()
            $ fian = "n"
            i "Honestly, art isn't worth it, Cindy."
            i "It's nice to have as a hobby, but if you try living out of it you're gonna have a bad time."
            i "You can find passion in your hobbies, too. Nothing wrong with that."
            c "I guess... Anyways, let's change the subject. I want to have fun!"
            c "In fact, I feel like dancing! Let's pay for these drinks and jump on the dance floor!"
    "Cindy called the barman and asked for the bill. When she took out her wallet she frowned."
    $ fcindy = "n"
    c "Hmm. I was counting on Wade paying for tonight's drinks, so I just brought enough cash for the taxi back home."
    $ fian = "n"
    c "You don't mind if the drinks are on you tonight, right?"
    "Cindy had the habit of asking for stuff... That wouldn't be bad if it wasn't because she was also quite stingy when it came to money."
    "Perry always hated it when she asked for beers while she never brought some herself."
    menu:
        "{image=icon_pay.png}Pay for the drinks":
            $ renpy.block_rollback()
            "I was having a great time with Cindy and I didn't want to spoil it."
            $ fian = "smile"
            i "Sure, no worries. I got you."
            $ ian_money -= 1
            play sound "sfx/moneydown.mp3"
            show money_down
            $ fcindy = "smile"
            c "Thanks!"
            jump v3cindydatedance
             
        "Refuse to pay":
            $ renpy.block_rollback()
            "I didn't want to indulge her. She always did the same."
            i "You have enough money."
            $ fcindy = "serious"
            c "Not for both the drinks and the taxi!"
            i "You can take the bus."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            c "Ugh, really? You're gonna be this cheap?"
            i "I'm just saying there's no need for you to take a taxi having the bus at hand..."
            c "You want me to take the bus, at night? You know the creeps one can find there?"
            $ ian_cindy -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            c "It's not like I'm asking anything crazy, I'm sure you can afford to pay for some extra drinks..."
            i "I'm not rich, you know?"
            stop music fadeout 2.0
            show ian at lef3
            show cindy2 at truecenter
            with move
            show axel at rig3
            with short
            x "I'll pay."
            $ fian = "worried"
            $ fcindy = "blush"
            "Only then we noticed the guy standing next to us on the bar."
            "He was tall and muscular, well dressed and handsome. He looked like he came right out of a TV spot or something..."
            "He didn't look too cheerful, though."
            c "It's not necessary..."
            x "I don't mind. It's just a cocktail."
            $ faxel = "smile"
            "He then looked at Cindy and finally smiled."
            x "My name's Axel."
            $ ian_axel_agenda = True
            $ fcindy = "blush"
            c "I'm Cindy, nice to meet you. And this is my friend Ian."
            x "I see. Nice to meet you too, Ian."
            $ fcindy = "n"
            hide friend_down
            menu:
                "{image=icon_charisma.png}You look like a lone wolf" if ian_charisma > 2:
                    $ renpy.block_rollback()
                    $ fian = "n"
                    i "Are you drinking alone?"
                    x "Yeah, I am..."
                    i "You're like a lone wolf from the movies, drinking whiskey alone at the bar."
                    play sound "sfx/friendup.mp3"
                    show friend_up
                    $ ian_axel += 1
                    x "Yeah, ha ha, but instead of whiskey I'm having a Long Island Ice Tea. Not so badass."
                    x "Let me pay for your drink too, dude."
                    i "Thanks man."
                    c "So you decided to go out on your own?"
                    
                "She's with me":
                    $ renpy.block_rollback()
                    $ fian = "serious"
                    i "She's with me, dude."
                    $ fcindy = "serious"
                    $ faxel = "happy"
                    x "I'm sure she is."
                    "Cindy gave me a sour look."
                    play sound "sfx/frienddown.mp3"
                    show friend_down
                    $ ian_cindy -= 1
                    $ fian = "sad"
                    c "What was that for?"
                    i "I just, huh... Thought he might be bothering you..."
                    c "Well, he's not."
                    $ faxel = "smile"
                    x "Don't worry man. I'm just trying to be polite with her, since you aren't."
                    "Axel paid for Cindy's drinks and I paid mine."
                    i "So... Where are your friends? Or are you here all by yourself?"
                    
                "Nice to meet you too":
                    $ renpy.block_rollback()
                    $ fian = "n"
                    i "Yeah... Nice to meet you too."
                    "Axel paid for Cindy's drinks and I paid mine."
                    i "So... Where are your friends? Or are you here all by yourself?"
    
            x "Yeah... I know it sounds lame, but I didn't feel like staying at home tonight."
            x "No one was available, but I needed to get a drink and clear my head, so I thought \"why the hell not\"?"
            c "I was feeling the same! I would've come here alone tonight too, if it wasn't for Ian."
            x "That's the second thing we have in common."
            c "What's the first one?"
            $ faxel = "happy"
            x "Well, you're blonde. And beautiful."
            $ fian = "n"
            $ fcindy = "shy"
            c "Ha ha ha!"
            "Had he gone out by himself to clear his head or to score with some chicks...?"
            "How confident and smooth he was made it clear to me that he was very used to flirting with beautiful girls."
            "And Cindy was right, if I hadn't come with her tonight this guy would've found her all by herself..."
            "Considering how much attention she was giving him I had reasons to be worried."
            if ian_go_cindy > 0:
                "For a moment I thought she was having a great time with me..."
                "Maybe she was pissed at Wade and was just looking for attention elsewhere. And I was acting like a jackass."
            else:
                "She was pissed at Wade and was looking for attention elsewhere."
            hide friend_down
            jump v3cindydateend

label v3cindydatedance:
    
    "Cindy grabbed my hand and dragged me to the area of the bar that served as a dance floor."
    scene v3_dance1
    with long
    "We found a space amongst the crowd and began dancing one in front of the other."
    "I had never been a very good dancer, and always felt quite embarrassed, but the alcohol was probably helping."
    if ian_athletics > 1:
        "I felt comfortable enough to put some pop in my moves, enjoying the moment."
        "Cindy looked at me and smiled."
        c "Nice moves!"
    else:
        "I had no real idea of what I was doing, but at least I was moving. And I was having fun."
        "Cindy seemed to be enjoying herself, too."
    "She moved with that kind of ease some girls have, like dancing was second nature to her."
    "Her movements were fluid and sultry, as easy to her as walking."
    "Her golden hair flashed when she moved her head, hit by the lights of the bar."
    if ian_go_cindy > 0:
        "She was a thing of beauty... I found myself unable to take my eyes off of her."
        "And I wasn't the only one. I could see other guys turning their gazes to her."
    else:
        "She soon grabbed the attention of nearby guys, turning their gazes to her. No wonder..."
    "Cindy seemed to be oblivious of it all. She just danced and enjoyed herself."
    menu:
        "{image=icon_charisma}+{image=icon_athletics}Dance together" if ian_athletics > 1 and ian_charisma > 1:
            $ renpy.block_rollback()
            $ v3_cindy_dance = True
            if ian_go_cindy < 3:
                $ ian_go_cindy += 1
            "I wanted to dance with her, get closer to her."
            scene v3_dance2
            with long
            "I took her hand and pulled her towards me."
            "She looked at me and smiled, accepting my invitation to dance together."
            "She focused her attention on me, same as I had mine focused on her. We were sharing that moment, just her and I."
            "I felt the smoothness and warmth of her hand, her delicate fingers intertwined with mine..."
            menu:
                "Let her lead":
                    $ renpy.block_rollback()
                    $ v3_cindy_dance_signs = True
                    "I followed Cindy's moves, letting her guide the dance."
                    "I wanted to make her comfortable and in control of what was happening."
                    "I wanted to be as close as possible, of course, but I was also aware of our situation. She was Wade's girlfriend, after all..."
                    "I knew this could be deemed inappropriate by some, but at that moment it just felt so right."
                    "Cindy and me dancing together, a smile on her beautiful lips, her shiny green eyes locked with mine..."
                    "I was having a blast, and so was she, or so it seemed to me."
                    "Cindy had never given signs of finding me attractive, and I had never expected her to. But at that moment I couldn't help feeling that there was some real tension between us."
                    if ian_cindy < 10:
                        play sound "sfx/friendup.mp3"
                        show friend_up
                        $ ian_cindy += 1
                    "She leaned forward, her chest on mine, and talked to my ear."
                    c "I didn't know you were such a good dancer!"
                    i "You think I am? Cool, I managed to fool you, ha ha!"
                    c "You are, compared to Wade at least!"
                    "We danced together for a few minutes, until Cindy spoke again."
                    c "I need to go pee!"
                    i "Yeah, me too..."
                    "After having spent the night drinking it was only normal that we needed to."
                    scene cocktailbar
                    with long
                    "We left the dance floor and went to take care of our biological needs."
                    
                "Get physical":
                    $ renpy.block_rollback()
                    $ v3_cindy_reject = True
                    "She was so hot... I was getting so turned on dancing with her..."
                    play sound "sfx/xp.mp3"
                    show lust_up
                    $ ian_lust_xp += 1
                    call screen skillsup
                    "I grabbed her hips and pulled her closer to me. Our pelvis' made contact, and our faces were just inches away..."
                    $ fcindy = "sad"
                    $ fian = "worried"
                    scene cocktailbar
                    show ian at lef
                    show cindy2 at rig
                    with short
                    "But then Cindy leaned back and escaped my embrace."
                    "She looked uncomfortable and I knew I had messed up."
                    play sound "sfx/frienddown.mp3"
                    show friend_down
                    $ ian_cindy -= 2
                    c "Um... I need to go to the bathroom."
                    i "Yeah, me too..."
                    hide cindy2
                    with short
                    i "..."
                    $ fian = "disgusted"
                    i "Fuck, what the hell's wrong with me? I creeped her out..."
                    "No wonder. She was Wade's girlfriend! I shouldn't have gotten so touchy..."
                    "I went to the bathroom to pee and clear my head."
                    hide ian
                    with short
                    $ fian = "sad"
                    "How should I act now, what should I say? Should I apologize?"
                    "That would make it even more uncomfortable..."
                    
                "Stop dancing":
                    $ renpy.block_rollback()
                    "After a while I felt I had danced enough."
                    "I had dared to get closer to Cindy, but I still wasn't completely comfortable with it. She was Wade's girlfriend, after all..."
                    "I wondered if he'd get mad knowing I had been dancing with his girl. I didn't do anything inappropriate, though."
                    i "Hey, I need to go to the bathroom..."
                    c "Yeah, me too! Let's go."
                    scene cocktailbar
                    with long
                    "We left the dance floor and went to take care of our biological needs."
            
        "Keep dancing separately":
            $ renpy.block_rollback()
            "I kept dancing in front of Cindy, together but separately at the same time."
            if ian_go_cindy > 0:
                "I didn't dare to get any closer... She was Wade's girlfriend, after all."
                "Doing more could be considered inappropriate... And Cindy didn't seem to have any special desire to get more physical with me."
                "No, this was enough. We were having a great night, as friends."
                "Even though it was hard not to like her..."
            else:
                "I was having a great night with my friend."
            "I couldn't believe Wade refused to party with her."
            "After a few songs Cindy leaned forward and talked to my ear."
            c "I need to go pee!"
            i "Yeah, me too..."
            "After having spent the night drinking it was only normal that we needed to."
            scene cocktailbar
            with long
            "We left the dance floor and went to take care of our biological needs."
            
        "Stop dancing":
            $ renpy.block_rollback()
            "After a short while I had enough. Dancing was not my thing, after all."
            "I found an excuse to get off the dance floor."
            i "Cindy, I'm going to the bathroom."
            c "OK! I'll be here!"
            scene cocktailbar
            with long
            "I left the dance floor and went to take care of my biological needs."
    stop music fadeout 2.0        
    "Surprisingly, I had to wait in line to get into the bathroom. After I was done I went back and looked for Cindy."
    $ fcindy = "smile"
    show ian at lef3
    with short
    i "Where's she...?"
    "It took me a couple of minutes to finally see her."
    i "Oh, there she is..."
    show cindy2 
    with short
    i "Hey, Cindy..."
    $ fian = "worried"
    $ faxel = "smile"
    show axel at rig3
    with short
    "Then I saw she was speaking to a guy." 
    $ fian = "n"
    i "Hey."
    c "Oh, hey Ian. This is Axel."
    $ ian_axel_agenda = True
    x "Hello."
    i "A friend of yours?"
    c "No, we just met!"
    i "Of course..."
    "I left her alone for two minutes and some guy was already hitting on her."
    "And not just any guy. He was tall and muscular, well dressed and handsome. He looked like he came right out of a TV spot or something..."
    if ian_go_cindy > 0:
        "Sadly for him Cindy was not alone. Not so easy flirting with a girl when her guy friend is next to her..."
    else:
        "He probably wasn't expecting having me around, though. Not so easy flirting with a girl when her guy friend is next to her..."
    "If my presence bothered him he concealed it very well, though."
    i "My name's Ian. What were you talking about?"
    c "You know, the typical stuff..."
    x "Just getting to know her a little bit. I was asking Cindy what brought her here tonight."
    menu:
        "{image=icon_charisma.png}The night took us here" if ian_charisma > 2:
            $ renpy.block_rollback()
            $ fian = "smile"
            i "Oh, the night took us here. Things weren't going as expected and we decided to go on a little adventure."
            c "That pretty much sums it up, yeah!"
            play sound "sfx/friendup.mp3"
            show friend_up
            $ ian_axel += 1
            x "I see. You guys look like fun."
            x "So are you two dating or something?"
            c "No, not at all!"
            if ian_go_cindy > 0:
                $ fian = "n"
                "The way Cindy denied it rubbed me the wrong way for some reason... Though she was telling the truth."
            else:
                i "No, we're just friends."
            i "Why do you ask?"
            x "I got the impression that could be the case, and I wouldn't want to get in the way of your night."
            c "Don't worry!"
            "She seemed eager to talk to him..."
        
        "She's with me":
            $ renpy.block_rollback()
            $ fian = "serious"
            i "She's with me, dude."
            $ fcindy = "serious"
            $ faxel = "happy"
            x "I'm sure she is."
            "Cindy gave me a sour look."
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_cindy -= 1
            $ fian = "sad"
            c "What was that for?"
            i "I just, huh... Thought he might be bothering you..."
            c "Well, he's not."
            $ faxel = "smile"
            x "Don't worry man, I'll be very polite with your friend."
            
        "We're just hanging out":
            $ renpy.block_rollback()
            i "Well, we're just hanging out."
            x "I can see that. Just the two of you?"
            c "Yeah, our friends bailed on us. Only Ian was cool enough to join me."
    $ fcindy = "n"        
    i "What about you? Axel, right? You're here on your own?"
    x "Yeah... I know it sounds lame, but I didn't feel like staying at home tonight."
    x "No one was available, but I needed to get a drink and clear my head, so I thought \"why the hell not\"?"
    c "I was feeling the same! I would've come here alone tonight, too, if it wasn't for Ian."
    x "That's the second thing we have in common."
    c "What's the first one?"
    $ faxel = "happy"
    x "Well, you're blonde. And beautiful."
    $ fian = "n"
    $ fcindy = "shy"
    c "Ha ha ha!"
    "Had he gone out by himself to clear his head or to score with some chicks...?"
    "How confident and smooth he was made it clear to me that he was very used to flirting with beautiful girls."
    "And Cindy was right, if I hadn't come with her tonight this guy would've found her all by herself..."
    "Considering how much attention she was giving to him I had reasons to be worried."
    if ian_go_cindy > 0:
        "And to think she was giving that attention to me a moment ago..."
        "Now it seemed like that amazing feeling had dissipated like a smoke screen, and I hated it."
        "Maybe she was pissed at Wade and was just looking for attention elsewhere. And I was acting like a jackass."
    else:
        "She was pissed at Wade and was looking for attention elsewhere."

label v3cindydateend:
    $ faxel = "smile"
    x "So what do you guys do for a living?"
    c "Nothing really fascinating... I'm just an accountant at my father's business, it's pretty boring."
    $ fcindy = "n"
    c "Ian's a writer, though. That's pretty cool."
    x "A writer, huh?"
    i "Well, not really... I like to write, but I haven't published anything yet... I'm working at a literature magazine right now."
    x "I see, so you're a man of culture as well, ha ha."
    i "You write, too?"
    x "No, I'm mainly a photographer and videographer."
    i "Mainly?"
    x "I'm a man of many talents."
    c "And what kind of pictures do you take?"
    x "My specialty is shooting models. Fashion and artistic nudes mostly."
    $ fcindy = "smile"
    $ fian = "worried"
    c "Really? We were just talking about that before!"
    x "Is that so? So you're interested in photography?"
    i "Not reall--{w=0.1}{nw}"
    c "Yes!"
    x "Have you done some modeling before, Cindy?"
    c "Who, me? Not at all!"
    x "Really? That's weird. You'd be perfect as a model, it's unbelievable that nobody has asked you to pose before."
    $ fcindy = "blush"
    c "Who, me?"
    x "I don't see any other perfectly slender, green-eyed blonde beauty in here."
    $ fcindy = "shy"
    $ fian = "surprise"
    x "I can't image a more perfect model. I'd love to shoot you."
    "That guy did not beat around the bush!"
    $ fian = "worried"
    "And it seemed Cindy was really buying it..."
    if ian_go_cindy > 0:
        "I wanted to intervene, but trying to cock-block that guy would only make me look like a jealous asshole."
        "And it wasn't my place to control what Cindy did. Wade should be here instead of me..."
    else:
        "I wanted to intervene, but it wasn't my place to control what Cindy did. Wade should be here instead of me."
    x "Have you ever thought about trying it?"
    c "Not really, but I would be lying if I said I wasn't curious!"
    c "It seems like a really cool experience... But I don't know if it's for me..."
    x "I can't imagine anything that would suit you better."
    x "If you want to I'd be happy to shoot you. For free, of course."
    "That was the final nail in the coffin. If there was something Cindy could not resist it was the words \"for free\"."
    c "In that case... Yeah, I think I'd like that!"
    x "Let's exchange numbers so we can find a day that's good for both of us."
    c "Sure."
    "I watched as they added each other's phone numbers. That guy got what he had been aiming for and he made it look so fucking easy and effortlessly..."
    x "Well, it's getting late and as I said today I'm not in the most reveling of moods..."
    x "I went out to clear my head and I'm going back home with more than I bargained for!"
    c "We'll be leaving now, too."
    x "It's been a pleasure meeting you, Cindy."
    if ian_axel == 4:
        x "You too, Ian. I hope you're lucky with your book."
        $ fian = "n"
        i "Thanks."
        "Axel shook my hand and left."
        hide axel with short
    else:
        hide axel
        with short
        "He left without even saying goodbye to me. It was like I had ceased to exist while they were having their conversation."
    show ian at lef
    show cindy2 at rig
    with move
    $ fcindy = "smile"
    c "That was so cool!"
    i "Are you really gonna pose for him?"
    $ fcindy = "n"
    c "Sure, why not? He offered to shoot me for free..."
    menu:
        "{image=icon_friend}I'd love to see your pictures" if ian_go_cindy > 0 and ian_cindy > 4:
            $ renpy.block_rollback()
            $ ian_cindy_model = True
            $ fian = "smile"
            i "Well, if you do, I'd love to see your pictures."
            $ fcindy = "blush"
            c "You would?"
            i "Yeah. I think what that guy said is true. You'd look wonderful as a model and I'd love to see your artistic side."
            $ cindy = "blush"
            c "Oh... Thanks, Ian."
            $ fcindy = "shy"
            c "I'll show you the results if I decide to do it!"
            $ fcindy = "n"
            c "By the way... Don't tell Wade about this. Not yet."
            $ fian = "n"
            i "You don't want him to know?"
            c "I do, but I want him to learn it from me and when the time's right."
            c "I know him and after the fight we had today the last thing I want is for him to get all jealous and worked up again."
            c "So please keep this secret for me."
            i "Alright, if that's what you want."
            
        "If that's what you want":
            $ renpy.block_rollback()
            $ fian = "n"
            i "Well, if that's what you want, go ahead."
            c "I think it can be interesting. It's something I haven't tried before, and it's artistic!"
            c "It's like what we were saying before about passions and stuff..."
            i "I guess."
            $ fcindy = "n"
            c "Anyways, please don't tell Wade."
            i "Why not? If you feel like you're not doing anything wrong..."
            c "I'm not. But I know him and after the fight we had today the last thing I want is for him to get all jealous and worked up again."
            c "I'll tell him, but when I think the time's right. And I want him to learn it from me, so keep quiet!"
        
        "Be careful":
            $ renpy.block_rollback()
            $ fian = "worried"
            i "You should be careful... You know what they say about some photographers..."
            $ fcindy = "serious"
            c "I'm a big girl and I can defend myself. I know what I'm doing."
            c "Axel looked really nice, but if it turns out he's not I know how to stop a guy in his tracks."
            if v3_cindy_reject:
                "Yeah, like she just did with me before..."
            c "Anyways, please don't tell Wade."
            i "Why not? If you feel like you're not doing anything wrong..."
            c "I'm not. But I know him and after the fight we had today the last thing I want is for him to get all jealous and worked up again."
            c "I'll tell him, but when I think the time's right. And I want him to learn it from me, so keep quiet!"
        
        "Wade won't like it":
            $ renpy.block_rollback()
            $ fian = "serious"
            i "Wade won't like that."
            $ fcindy = "serious"
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ ian_cindy -= 1
            c "So? What, have you come just to keep an eye on me for him?"
            $ fian = "sad"
            i "What? No..."
            c "Wade's not my owner and I don't have to ask him permission to do stuff."
            c "Besides, I'm not doing anything wrong."
            i "I'm just saying you should consider how he will feel about it..."
            c "If he feels anything other than happy for me then he's being completely egotistical once again!"
            c "Now don't you go running and tell him about this. I want to tell him myself, when I feel I want him to know."
            c "Are we clear?"
            i "Yes..."
   
    scene streetnight
    with long
    "After that Cindy called a cab and I walked back to my place."
    "That had been a really weird night, once again..."

##IAN SUNDAY ####################################################################################################################################################################################################################

label v3iansunday:
    
    $ day = "Sunday"
    scene blackbg
    with long
    call screen calendar
    $ ian_look = 3
    $ fian = "n"
    if v3_cindy_date:
        scene ianroom
        with long
        i "Nhhh..."
        show ianunder
        with short
        "I woke up late the next morning. It had been a longer night than I had expected..."
        if v3_holly_date:
            $ fian = "surprise"
            with vpunch
            i "Oh, shit! I had to meet Holly this morning!"
            i "What time it is?"
            $ fian = "worried"
            i "Damn, I'm already late!"
            "I jumped out of the bed, got dressed as quickly as I could and I left without having breakfast or even a glass of water."
            jump v3sundayholly
        else:
            "I thought about Cindy and all that had happened..."
            if v3_cindy_reject:
                "I had messed up... I had felt things were flowing so smoothly between her and me and I had been too forward."
                i "What would Wade do if he knew how I behaved? He'd probably punch me in the face, and I can't say I wouldn't deserve it..."
                "Cindy didn't seem as concerned about keeping the distance with that other guy, Axel."
                "He swooped in and charmed her like it was nothing... And he wanted to take photos of her."
                i "That sly bastard..."
            elif v3_cindy_dance:
                "It had been the first time we hung out just the two of us, and I liked it quite a lot."
                "I even felt comfortable enough to dance with her, and that wasn't something that usually happened..." 
                if v3_cindy_dance_signs:
                    "And during that dance I had felt some kind of special connection with her."
                    "I considered myself quite clueless when it came to these kind of things, so for me to notice it it must've been pretty obvious, right?"
                "This was probably just in my head, though. I doubted it meant anything for Cindy..."
                "Her attitude towards me had nothing to do with how she reacted when that guy, Axel, showed up." 
                "He charmed her like it was nothing... And he wanted to take photos of her."
                i "That sly bastard..."
            else:
                "It had been the first time we hung out just the two of us, and I liked it quite a lot."
                "But then that dude, Axel, showed up and charmed Cindy like it was nothing... And he wanted to take photos of her."
            "She had asked me not to tell Wade about it..."
            "I wondered what that meant. Did she feel she was actually doing something wrong?"
            "Did Cindy actually have any intention of doing something she shouldn't...?"
            i "It's not something I should worry about. It's none of my business actually..."
            i "I need to take care of my own problems. The book review, to begin with."
    else:
        if v3_holly_date:
            jump v3sundayholly
        else:
            scene ianroom
            with long
            i "Nhhh..."
            "I had no rush to get up that morning."
            $ ian_look = 2
            show ian
            with short
            "When I felt I had slept enough I got up. I could enjoy my Sunday."
            "Last night had been really fun, until Wade and Cindy fought..."
            i "That was pretty awkward..."
    "I checked my e-mail to see if Holly had answered to my request."
    $ fian = "n"
    i "She has! Let's see what she thinks of the book review I wrote..."
    if ian_switch_review:
        "Holly's opinion was incredibly positive."
        "She said she really loved my analysis and that it was one of the best reviews she had ever read."
        "She thought it was perfect and she had nothing to really point out, except a couple of nitpicks."
        i "That's some big praise... If Holly likes it I'm sure I did a good job!"
        scene ianroom
        show v2_ianwrite
        with long
        jump v3writebook
    if ian_honest_review:
        "Holly was worried. On one hand, she thought this was one of the most acid and funny reviews she had ever read."
        "On the other one, she was certain Minerva would hate it."
        "That was my intention, after all. This would be my protest to her."
        "The choice was already made. I didn't want to worry about it, so I decided to enjoy my Sunday and relax."
    if ian_minerva_review:
        "She said I had done a good job following Minerva's guidelines."
        "She pointed out a couple of things I could tweak to make sure she was really pleased."
        "All in all, Holly herself could've been the author of my review, or so she said, since the style was so similar."
        i "I'll change what Holly pointed out. This way Minerva won't have any reason not to praise me."
        "Other than that, I had the rest of the day to myself."
    jump v3endiansunday
    
##HOLLY

label v3sundayholly:    
    $ ian_look = 1
    scene street
    with long
    if v3_cindy_date:
        $ fian = "worried"
        show ian
        with short
        "As I ran to the café I thought about Cindy and all that had happened..."
        if v3_cindy_reject:
            "I had messed up... I had felt things were flowing so smoothly between her and me and I had been too forward."
            i "What would Wade do if he knew how I behaved? He'd probably punch me in the face, and I can't say I wouldn't deserve it..."
            "Cindy didn't seem as concerned about keeping the distance with that other guy, Axel."
            "He swooped in and charmed her like it was nothing... And he wanted to take photos of her."
            i "That sly bastard..."
        elif v3_cindy_dance:
            "It had been the first time we hung out just the two of us, and I liked it quite a lot."
            "I even felt comfortable enough to dance with her, and that's not something that usually happens..." 
            if v3_cindy_dance_signs:
                "And during that dance I had felt some kind of special connection with her."
                "I considered myself quite clueless when it came to these kind of things, so for me to notice it it must've been pretty obvious, right?"
            "This was probably just in my head, though. I doubted it meant anything for Cindy..."
            "Her attitude towards me had nothing to do with how she reacted when that guy, Axel, showed up." 
            "He charmed her like it was nothing... And he wanted to take photos of her."
            i "That sly bastard..."
        else:
            "It had been the first time we hung out just the two of us, and I liked it quite a lot."
            "But then that dude, Axel, showed up and charmed Cindy like it was nothing... And he wanted to take photos of her."
        "She had asked me not to tell Wade about it..."
        "I wondered what that meant. Did she feel she was actually doing something wrong?"
        "Did Cindy actually have any intention of doing something she shouldn't...?"
        i "It's not something I should worry about. It's none of my business actually..."
        play music "music/date.mp3" loop
        scene cafe
        with long
        show ian at lef
        with short
        "I finally arrived at the café. I tried to steady my breathing, but I was panting after rushing there."
        "I looked at the time. I was almost an hour late."
        i "Damn..."
        $ fholly = "sad"
        show holly2 at rig
        with short
        i "Hi...! I'm sorry for the delay!"
        h "It's OK..."
        i "No, I'm really sorry. Last night I went out with my friends and things dragged on longer that I expected, so..."
        $ ian_holly -= 1
        play sound "sfx/frienddown.mp3"
        show friend_down
        h "You don't need to tell me... I already know you probably had some important things to take care of..."
        i "This is more important... You agreed to help me and I made you wait..."
        if v1_alisonlunch == False:
            i "Have you seen Lena?"
            h "No, she's not working on Sundays."
            i "I figured as much."
        else:
            "I looked around. Lena was nowhere to be seen, so I assumed she wasn't working on Sundays. Just as I expected."
        $ fholly = "n"
        h "So... Shall I read your review?"
        i "Sure."
    else:
        $ fian = "smile"
        $ fholly = "shy"
        show ian
        with short
        "I made my way to the café, where I had to meet Holly."
        play music "music/date.mp3" loop
        scene cafe
        with long
        show ian at lef
        show holly3 at rig
        with short
        i "Good morning!"
        h "Good morning..."
        i "Have you been waiting for long?"
        h "No, I just got here..."
        if v1_alisonlunch == False:
            i "Have you seen Lena?"
            h "No, she's not working on Sundays."
            i "I figured as much."
        else:
            "I looked around. Lena was nowhere to be seen, so I assumed she wasn't working on Sundays. Just as I expected."
        i "Well, let's take a seat and get some coffee. And some breakfast!"
        i "As I said, it's my treat."
        h "It's not necessary..."
        i "It's the least I can do since you're willing to help me!"
        $ fholly = "smile"
        hide holly3
        show holly2 at rig
        with short
        h "In that case, I won't argue. Do you want me to take a look at your review now?"
        i "Sure."
    $ fholly = "n"
    $ fian = "n"
    "I handed Holly the papers and I watched a bit nervously as she read my review."
    if ian_switch_review:
        "After a few minutes of silence during which she seemed to consider a few things, she gave me her verdict."
        $ fholly = "happy"
        h "It's great, Ian!"
        $ fian = "happy"
        i "Really?"
        h "Yes, I'm surprised, honestly... I mean, I know you can write, but this is really good."
        h "I love your analysis, it's very nuanced and poignant, and the way you wrote it makes it fun to read."
        h "I don't think I could've done a better job myself, honestly. And I really want to read \"The Fall of Delbaeth\" now!"
        "Holly's opinion was incredibly positive."
        $ fian = "shy"
        i "Wow, that's some really big praise coming from someone like you..."
        $ fian = "smile"
        i "Thanks a lot, Holly. If you like it so much I'm confident I've done a good job."
    if ian_honest_review:
        $ fholly = "surprise"
        "Holly's eyes widened as she read."
        h "Oh my god."
        $ fian = "happy"
        $ fholly = "happy"
        "A chuckle escaped her as she continued."
        h "Ian! I can't believe you wrote this..."
        "She laughed again before finishing the review."
        h "Oh my God, that was the most acidic and brutal review I have ever read!"
        i "Seems like you found it funny!"
        h "I did...!"
        $ fholly = "sad"
        hide holly2
        show holly3 at rig
        with short
        h "But are you really going to hand this to Minerva?"
        $ fian = "smile"
        i "That's the idea."
        h "Isn't that a bit... kamikaze?"
        i "Maybe... But I'm too fed up with this situation. I tried to do things her way and she still treats me like dirt."
        i "This will be my protest, one that won't leave her indifferent."
        h "No, it won't... Be careful, Ian."
        i "Thanks for worrying about me, Holly. And for your opinion about the review."
    if ian_minerva_review:
        "After a few minutes of silence during which she seemed to consider a few things, she gave me her verdict."
        $ fholly = "smile"
        h "It's great!"
        $ fian = "n"
        i "You think so?"
        h "Yes, I think you understood exactly what Minerva wants. The way you wrote it is almost as if I had written this myself!"
        "We took a few minutes to correct a couple of things Holly pointed out to get the perfect review Minerva would love."
        i "Thanks a lot, Holly."
    $ fholly = "shy"
    h "It's nothing..."
    $ fian = "n"
    i "I kinda feel bad making you read all my reviews... Meanwhile, I have to admit I haven't read any of your books..."
    $ fholly = "n"
    hide holly2
    show holly3 at rig
    with short
    h "Oh... Well, you're not missing out on anything great."
    menu:
        "{image=icon_wits.png}Stop putting yourself down" if ian_wits > 1:
            $ renpy.block_rollback()
            $ encourage_holly += 2
            $ fian = "n"
            i "Holly, you need to stop putting yourself down."
            $ fholly = "sad"
            i "Every time I tell you how amazing you are you say that's not a big deal or that you're not that good..."
            $ fian = "smile"
            i "Well, you are to me! I admire you achievements and so should you!"
            $ ian_holly += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            $ fholly = "happyshy"
            h "Thanks, Ian... Those are wise words."
            h "I'll try to believe in them."
            hide friend_up
            
        "People think they're good":
            $ renpy.block_rollback()
            $ encourage_holly += 1
            i "Well, people like them. Some even love them!"
            h "People like a lot of stuff... Some of it isn't even good."
            i "So you think your books are bad?"
            $ fholly = "blush"
            h "N-{w=0.3}no, I think they're OK...But they're far from great."
            i "Hey, nobody's asking you to be great. Being OK is good enough, you're just starting!"
            $ fholly = "smile"
            h "I guess so."
            
        "If you say so":
            $ renpy.block_rollback()
            i "If you say so..."
            i "If I wasn't so busy I'd think about giving them a read to see for myself."
            h "It's OK, you probably wouldn't like them anyways..."
            
    i "In any case, if I get my hands on one of your books I'll put them on my to-read pile."
    if encourage_holly > 1:
        i "At the top spot."
        h "Oh..."
    $ fholly = "blush"
    h "I could get you one..."
    i "One of your books?"
    h "Yeah. I have a ton of them at home."
    i "Oh, that would be awesome! Thanks, Holly."
    $ fholly = "n"
    h "What about you? You told me you were writing a book of your own..."
    $ fian = "n"
    i "Oh yeah, I've been quite motivated lately..."
    $ fholly = "smile"
    h "What's it about?"
    $ fian = "smile"
    if book_scifi:
        i "It's a sci-fi novel!"
        h "Really? That's so cool! They say it's the most complicated genre to write about, and I think I agree..."
        i "It's also the most deep and thrilling, in my opinion, of course."
    if book_fantasy:
        i "It's a fantasy novel!"
        h "I see! So you're a fantasy writer like myself!"  
        i "Yeah, those have always been my favorite kind of story."
    if book_historical: 
        i "It's an historical novel."
        h "Oh, so you like History!"
        i "Yes, a lot!"
    h "So you're aiming at the literay contest for new voices?"
    i "Yeah... Winning it would be awesome for my career. The break-through I've been needing..."
    if ian_holly > 4 :
        menu:
            "{image=icon_friend.png}Ask Holly for advice on writing":
                $ renpy.block_rollback()
                i "Say, Holly... You won last year's contest. Can I ask you for advice as a writer?"
                h "Yeah, of course..."
                if book_scifi:
                    h "Sci-fi tends to be a darker genre that explores moral and societal issues..."
                    h "I'd say stay away from a more whimsical approach and try to make things intense and shocking."
                    h "Maybe try to even go beyond hard-science and explore more metaphysical or philosophical themes..."
                    i "Yeah, that makes a lot of sense!"
                    h "I don't know, I'm no expert..."
                    i "What you said will be of great help. Thanks, Holly."
                if book_fantasy:
                    i "You're a fantasy writer, too, after all!"
                    h "My main advice is to avoid clichés like the plague!"
                    $ fholly = "shy"
                    h "Oh, and I just spouted one, ha ha..."
                    i "Avoid clichés. Noted."
                    $ fholly = "smile"
                    h "Yeah. Think about the typical fantasy stories, with elves, dragons, a dark lord... That's been done so many times."
                    h "Fantasy readers want something a bit more original, something new."
                    i "I'll try to remember that. Thanks, Holly."
                if book_historical:
                    h "I'm no expert, but my advice would be to keep to the proven path."
                    h "Use the elements that make an historical novel work. Be coherent with them and don't try whacky or unorthodox stuff."
                    h "I think the story would suffer and readers won't like it as much."
                    i "Noted. I'll try to remember that. Thanks, Holly."
                play sound "sfx/xp.mp3"
                show wits_up
                $ ian_wits_xp += 1
                call screen skillsup
                
            "I don't need advice":
                $ renpy.block_rollback()
                i "I have faith in my chances of winning."
    else:
        i "I have faith in my chances of winning."
    h "I hope you're successful with your book!"
    i "Who knows... I doubt it, but maybe if I get lucky I will become famous like you!"
    h "Stop it, I told you already, I'm far from famous..."
    i "Stop lying, ha ha! You have a lot of fans... You must receive love letters all the time!"
    $ fholly = "blush"
    h "No... Not at all..."
    i "I don't believe it. You must be one of the cutest female writers out there."
    hide holly2
    show holly3 at rig
    with short
    h "..."
    if ian_holly > 5:
        h "Do you... think I'm cute?"
        menu:
            "Very cute":
                $ renpy.block_rollback()
                $ ian_go_holly +=2
                $ ian_holly += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                $ fian = "confident"
                i "I do. I think you're very cute."
                with vpunch
                h "...!"
                h "Uh. I..."
                $ fian = "smile"
                h "Thank you."
                i "Don't get so flustered. I just said something really obvious."
                i "You're cute, Holly."
                $ fholly = "shy"
                h "Ha ha, stop it, I heard you..."
                i "OK. Just wanted to make sure."
                
            "I do":
                $ renpy.block_rollback()
                $ ian_go_holly +=1
                i "I do. I think you're cute."
                h "..."
                h "Really?"
                i "Sure! Why would I lie to you?"
                $ fholly = "shy"
                h "I don't know..."
                i "Then don't be so distrustful!"
                h "Oh, ha ha..."
                
            "I didn't mean it that way...":
                $ renpy.block_rollback()
                $ fian = "worried"
                i "Oh, I'm sorry, I didn't mean it like that...!"
                i "I mean, I didn't want it to sound inappropriate or something like that."
                h "Don't worry. It's not..."
                i "Oh, OK. I just wanted to make sure I didn't make you feel uncomfortable or..."
                h "No, no, it's OK! Forget it."
                
        h "I just, uh, need to get going so..."
        i "Sure, let me pay for our coffees... And thanks for helping me out, Holly. Really."
        if ian_go_holly > 0 and encourage_holly > 0:
            h "No, thank you... I enjoyed this."
            $ fholly = "happyshy"
            h "A lot."
        else:
            h "Oh, not at all... I was glad."
    else:
        h "Thanks..."
        i "Well, I should get going."
        h "Yeah, me too."
        i "Thanks a lot, Holly."
        if encourage_holly > 0:
            h "No, thank you... I enjoyed this."
            if encourage_holly > 1 and ian_holly > 4:
                $ fholly = "shy"
                h "A lot."
        else:
            h "Never mind..."
    stop music fadeout 2.0
    if ian_switch_review:
        scene ianroom
        with long
        $ ian_look = 2
        "After my date with Holly I went back home and decided to do something productive."
        show v2_ianwrite
        with short
        jump v3writebook
    else:
        jump v3endiansunday

        
## SUNDAY END

label v3endiansunday: 
    
    scene ianroomnight
    with long
    $ian_look = 2
    $ fian = "n"
    if v3_holly_date and ian_switch_review == False:
        "Back at home I decided to relax and enjoy my Sunday"
    show ian
    with short
    i "It's getting late..."
    if v2_ian_date:
        i "I haven't heard from Lena this whole weekend... Maybe I should've written to her."
        i "I don't want to be bothersome, though..."
        "I decided to check her Peoplegram, see if she had posted something about her weekend."
        show ian at left
        with move
        if v3_pg_ian:
            show v3_peoplegram2
        else:
            show v3_peoplegram1
        with short
        if v3_pg_ian:
            $ fian = "surprise"
            i "Hey, that's my drawing!"
            $ fian = "blush"
            i "Now that I remember it, she took a picture... But I never expected her to upload it to her Peoplegram."
            $ fian = "shy"
            i "I feel special now. I should text her..."            
        else:
            i "She's stunning..."
            i "I should text her."
        hide v3_peoplegram1
        hide v3_peoplegram2
        with short
        show ian at truecenter
        with move
        $ fian = "n"
        i "How should I open up? Man, these things are hard."
        i "Oh, yeah, let's go with a callback from our last meeting..."
        i "{i}Hey, how's it going? Have you tried that new guitar yet? You looked pretty happy to get it!{/i}"    
        if v3_robert_date:
            i "..."
            $ fian = "sad"
            i "She's not answering..."
            i "She must be busy. She'll text me back later."
            $ fian = "n"
        else:
            play sound "sfx/sms.mp3"
            "The buzz of the notification made me smile. She answered right away."
            play music "music/date.mp3"
            $ fian = "smile"
            if v2_lena_gohome:
                l "{i}Yes, I've been playing it quite a lot! Getting the hang of it again.{/i}"
            else:
                l "{i}Yes, I've been trying it out! Getting the hang of it again.{/i}"
            i "Now I need to follow up with something interesting... I want to learn some relevant stuff about her!"
            i "{i}I never asked you, but what kind of music do you like to play?{/i}"
            l "{i}Several styles... But I guess I mostly enjoy rock, especially indie, pop and blues... The softer styles, ha ha.{/i}"
            i "{i}So no heavy metal then, ha ha.{/i}"
            if lena_metal == 2:
                l "{i}Well, you'd be surprised! It depends on the style, though.{/i}"
                l "{i}I'm not into the death metal stuff, but I like listening to progressive, and classic heavy metal is not bad.{/i}"
                $ fian = "surprise"
                l "{i}And when I was a teenager I loved gothic, ha ha...{/i}"
                "I wasn't expecting that! So she liked metal? And progressive? That was my favorite stuff!"
                "It was hard finding people who liked that kind of music, even more a girl who did!"
                $ fian = "happy"
                $ ian_lena += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                i "{i}No way, you like progressive? It's my favorite style!{/i}"
                l "{i}I'm no expert or anything like that, but I listen to it from time to time.{/i}"
                i "{i}Wow, that's so cool. Most girls don't like metal for some reason, even though there are a lot of different and cool songs.{/i}"
                l "{i}People think metal is all noise and screaming... Though that still beats what they play in clubs and on TV. That music is really awful!{/i}"
            elif lena_metal == 1:
                l "{i}Not really... I like some songs, though, especially the classics and the ballads.{/i}"
                i "Oh, not as bad as I thought. She has some musical culture."
                i "{i}That's cool! There aren't many girls who enjoy heavy metal, for some reason. Even if it's just the softer stuff.{/i}"
                l "{i}There are great songs to enjoy in every genre!{/i}"
                l "{i}Well, not in every genre... Most of the music they play in clubs and on TV is awful!{/i}"
            else:
                l "{i}No, not at all! I can't listen to it.{/i}"
                $ fian = "n"
                i "Such a shame. But it was to be expected."
                i "{i}I thought so. Not many girls like metal, for some reason.{/i}"
                l "{i}Too loud and noisy and frantic! I don't like it at all.{/i}"
                i "{i}Such a shame... There's plenty of awesome songs!{/i}"
                l "{i}I'll let others enjoy those. Though I'd rather listen to metal than to the music they play in clubs and on TV. That one is really awful!{/i}"
            i "{i}I know, right? I hate commercial music nowadays... A few years ago it used to be good.{/i}"
            l "{i}You sound like an old man!{/i}"
            $ fian = "smile"
            "She wasn't wrong."
            i "{i}I'm getting there, ha ha.{/i}"        
            if v3_pg_ian:
                "It was time to ask her about the drawing... I had to bring that up."
                i "{i}By the way, I saw your last post on Peoplegram.{/i}"
                l "{i}Oh! Sorry about that, I should've asked your permission, right?{/i}"
                i "{i}No, not at all! If anything I'm surprised you decided to post it! The drawing wasn't that good to be honest.{/i}"
                l "{i}I liked it.{/i}"
                i "{i}I'm glad you did. Makes me wanna get into it again!{/i}"
                l "{i}It's never too late, right?{/i}"
                i "{i}Sometimes it is... But I can try and practice some more!{/i}"
                l "{i}I'll let you know when I go back to one of those life drawing sessions if you want.{/i}"
                i "{i}Please do.{/i}"
                "I felt that the conversation was going really well."
            l "{i}Ian, I'm gonna start my shift now, so I'm putting my phone away.{/i}"
            i "{i}Working on a Sunday night?{/i}"
            l "{i}Yeah... It sucks, I know.{/i}"
            i "{i}Stay strong! And let's hang out again soon.{/i}"
            l "{i}Yes! I'm super busy these days, but I'll let you know as soon as I have some free time.{/i}"
            i "{i}I'd like that.{/i}"
            stop music fadeout 2.0
            "I lay down on the bed."
            $ fian = "shy"
            i "Ahhh, Lena..."
            i "She's so nice."
            if v2_kiss:
                i "I still can't believe I kissed her."
                i "I feel almost like a teenager again, ha ha..."
                i "I wonder if we'll get somewhere, her and me..."
            else:
                i "I wonder if something will ever happen between us. I'd say things seem to indicate so, but I don't want to jump to conclusions..."
            $ fian = "n"
            
    ## decide train jiu
    
    i "Well, I guess I'll get some more writing done."
    play sound "sfx/keyboard.mp3"
    scene ianroomnight
    show v2_ianwrite
    with long
    "I continued to work on my book, developing the ideas I had been working on and finishing the second chapter."
    if v2_ian_date and v3_robert_date:
        $ fian = "sad"
        scene ianroomnight
        show ian
        with short
        i "..."
        "Lena hadn't answered back yet and it was past dinner time."
        i "Maybe I should write her again just in case..."
        i "{i}I never asked you, but what kind of music do you like to play?{/i}"
        i "..."
        if ian_lena > 2:
            $ ian_lena -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
        i "Nothing, she's probably still busy."
        i "I wonder what's keeping her so completely busy on a Sunday afternoon."
        i "Anyways, I should try to write a bit more before going to bed..."
        "I didn't take much longer to go to sleep, though."
    else:
        "I worked until it was time to go to bed."
    "I had to be ready for tomorrow..."

##IAN MONDAY #####################################################################################################################################################################################################################
    
    $ week = 3
    $ day = "Monday"
    scene blackbg
    with long
    call screen calendar
    $ ian_look = 1
    $ fian = "n"
    $ minerva_look = 1
    play music "music/normal_day.mp3" loop
    scene magazine
    with long
    "Monday had finally arrived."
    show ian
    with short
    if v2_ian_date and v3_robert_date:
        "When I woke up that morning Lena had answered my texts. It seemed that she had been working despite it being Sunday."
        if v3_pg_ian:
            "We texted a bit and I asked about the drawing. I also asked her about hanging out soon but she said she was super busy."
            "But she promised to let me know when she was free."
        else:
            "I had asked her about hanging out soon but she said she was super busy. She'd let me know when she had time."
    if ian_honest_review:
        "We had delivered the reviews first thing in the morning and now I was expecting the outrage to ensue."
        "Minerva had been reading and editing them in her office, as usual. Only this time she would find a surprise."
        stop music fadeout 2.0
        show ian at lef3
        with move
        $ fminerva = "furious"
        play sound "sfx/door.mp3"
        show minerva
        with short
        play music "music/danger.mp3" loop
        "I wasn't surprised at all when she stormed out looking for me with anger painted on her face."
        with vpunch
        mi "What the hell is this!?"
        "She brandished a bunch of papers in my face, practically screaming at me. Of course, that got the attention of the whole office."
        $ fholly = "sad"
        show holly2 at rig3
        with short
        "Everybody got quiet and looked at the scene that was about to play out."
        i "What's the problem?"
        mi "You know full well what the problem is! What kind of nonsense is this?"
        i "It's an honest review of the book you assigned me. I don't see where the problem is."
        mi "Is this some kind of joke to you?"
        $ fminerva = "mad"
        "Minerva looked at the papers and read one of my sentences aloud."
        mi "\"{i}The fact that a forty-nine year old writer came up with this makes \"Poker Love\" seem like your drunk uncle trying to act hip and cool to a group of fifteen-year old girls{/i}\"."
        mi "\"{i}It's deeply embarrassing and very close to being illegal{/i}\"."
        "Someone had to hold back his laughter, but everyone heard it. Minerva scanned the room like a hound in search of the perpetrator, but I diverted her attention back to me."
        i "Look, there's some serious technical analysis, too, just as you asked."
        "I took my own copy of the review and read another paragraph."
        $ fminerva = "furious"
        i "\"{i}You get your typical love triangle, blank slate main character who's the most special person in the galaxy, your cookie-cutter evil villain and so on...{/i}\""
        i "\"{i}The book's most notorious achievement might be that it could hold the record for the most clichés ever in a single story. And that's no joke{/i}\"."
        mi "You think you're funny? Well, you're not!"
        mi "You're just being incredibly disrespectful with this potty humor!"
        i "I don't see how. I just did what was asked of me, I analyzed a book and did a comprehensive review of it."
        mi "You don't see how? Let me show you how!"
        "Minerva read the closing sentences of my review."
        mi "\"{i}I found there's two ways one can enjoy this book:{/i}\""
        mi "\"{i}Either you like those \"so bad, they're good\" things, or you're not able to tell when you're being treated like a brain-dead imbecile{/i}\"."
        mi "\"{i}Otherwise, use your time and money to support authors who really deserve it. Those are rarely shoved into our faces by greedy corporations{/i}\"."
        "At this point several people couldn't keep holding their laughter and they became clearly audible."
        girl "Shh, shut up idiot! Hee hee!"
        guy "Oh my God."
        "Minerva looked at me like she was about to lose it."
        mi "This is utter mockery and disrespect! Do you think we can publish this!?"
        $ fian = "mad"
        i "So, what is it that you want? A real book review or an advertising pamphlet?"
        i "If it's the second, at least be honest with what you're asking of us! And if that's what you really want, assign me an actually good book I can honestly praise!"
        mi "We've already talked about that when--!"
        i "No, you're just putting my work down for some reason I can't understand! Let me do some work I can be proud of!" 
        $ ian_minerva = 0
        play sound "sfx/frienddown.mp3"
        show friend_down
        with vpunch
        mi "Enough!!"
        $ fian = "serious"
        mi "I want a normal review that doesn't look as if it's written by a crazy man-child on my desk tomorrow, first thing in the morning!"
        "I had never seen her screaming like that. I had really managed to push her off the rails."
        mi "If I don't see it when I open the door to my office you can consider yourself fired, are we clear!?"
        "She turned around and slammed the door to her office shut."
        stop music fadeout 2.0
        play sound "sfx/door.mp3"
        hide minerva
        with vpunch
        "The room was left in silence, no more laughter could be heard. Everybody was shocked with what had just happened."
        "I had managed to show them Minerva's true colors."
        call screen willup
        
    if ian_switch_review:
        "We had delivered the reviews first thing in the morning and Minerva had been reading and editing them in her office, as usual."
        $ fminerva = "smile"
        show ian at lef3
        with move
        show minerva
        with short
        "After lunch she came out of her office with a smile on her face."
        mi "Everybody, gather round! I'm going to assign the new reads for this week..."
        $ fholly = "n"
        show holly2 at rig3
        with short
        mi "But before that I want to praise Holly. Your reviews are always fantastic, but this one..."
        mi "It's incredible!"
        $ fholly = "blush"
        hide holly2
        show holly3 at rig3
        with short
        mi "I showed it to the publisher and they really loved it."
        mi "\"The Fall of Delbaeth\" is one of the most important fantasy books of our times and you captured its essence perfectly. I'm sure a lot of books will be sold thanks to your review!"        
        i "I wrote it."
        $ fminerva = "n"
        mi "What?"
        i "I wrote that review, not Holly."
        $ fminerva = "mad"
        i "I asked if she didn't mind switching our assignments, since I really wanted to review \"The Fall of Delbaeth\"."
        mi "Wh--{w=0.3}You mean that..."
        "Her brain was so scrambled she couldn't even blurt out a coherent sentence."
        "I had gotten her good."
        mi "Is this some kind of game?"
        $ fian = "serious"
        i "This is no game. It's a job well done."
        i "No matter what I do you keep complaining about my reviews, even when I made sure to do it as you wanted."
        i "You kept pushing me down and wouldn't let me review anything significant because you said I was bad at my job."
        i "Well, I just proved to you you were being unfair with me. I wrote a very good review and you loved it."
        call screen willup
        mi "Holly, is this true? Did you switch reviews with Ian?"
        h "..."
        h "Yes."
        $ fminerva = "sad"
        mi "..."
        $ fminerva = "furious"
        mi "I see."
        "Minerva turned her sight to me, and if stares could kill I would've been dead on the spot."
        $ ian_minerva = 0
        play sound "sfx/frienddown.mp3"
        show friend_down
        "Yet she didn't say anything. She couldn't."
        "After a tense silence that filled the whole room, she turned around and went back to her office."
        play sound "sfx/door.mp3"
        hide minerva
        with short
        "After she left, whispering began to spread throughout the magazine about what had just happened."
        "I had showed everybody how full of shit Minerva was and how she had been mistreating me."
        "I had beaten her at her own game."

    if ian_minerva_review:
        "I had delivered the review first thing in the morning and Minerva had been reading and editing them in her office, as usual."
        $ fminerva = "smile"
        show ian at lef3
        with move
        show minerva
        with short
        "After lunch she came out of her office to assign the new reads."
        mi "OK, interns, gather round..."
        $ fholly = "n"
        show holly2 at rig3
        with short
        mi "Oh, Holly. Your review was really really good! \"The Fall of Delbaeth\" is a complicated book, but I knew you'd do a wonderful job."
        hide holly2
        show holly3 at rig3
        with short
        h "Thanks..."
        i "What about mine?"
        $ fminerva ="n"
        mi "Huh?"
        i "My review on \"Poker Love\". Do you think it's good?"
        mi "It's passable this time."
        $ fian = "worried"
        i "Just passable?"
        $ fminerva = "mad"
        mi "What do you want to hear, Ian?"
        mi "You were barely able to write a comprehensive review last week. Do you expect to improve this fast? That's not how things work."
        mi "This time I got a review I can use, but this should be the norm, not the exception!"
        "She turned around and went back to her office."        
        play sound "sfx/door.mp3"
        hide minerva
        with short
        $ fian = "mad"
        i "I can't believe this woman...!"
        show ian at lef
        show holly3 at rig
        with move
        $ fian = "serious"
        h "Hey..."
        $ fian = "sad"
        i "Hey, Holly."
        h "I know you must be feeling frustrated... But this time she didn't complain about your review."
        i "Of course not, she has no reason to! You said it yourself, it could've passed for one of yours..."
        h "I'm sorry... It really seems like Minerva doesn't appreciate you, but you should avoid getting on her bad side..."
        h "Maybe if you keep doing what she expects of you you'll get into her good graces..."
        i "I guess I will need to keep doing these awful reviews..."
        i "Well, a job's a job, and I need the money. As long as I get paid, I'll do it."
        i "This is only temporary, after all... Hopefully when I publish my book I won't need to keep doing this."
            
    scene street
    with long
    show ian
    with short
    if ian_honest_review:
        i "Well... It's done. I had my confrontation with Minerva, finally."
        "And now I had to spend the afternoon writing a bullshit review about that book, or she would fire me..."
        "But at least I had made my point. What this would imply, I still had no idea..."      
    else:
        if ian_switch_review:
            i "Well... It's done. I had my confrontation with Minerva, finally."
            "I had dismantled all her excuses. She couldn't keep hiding behind them to treat me unfairly."
        if ian_minerva_review:
            "I left the office feeling a bit defeated. There was no way of pleasing Minerva..."
        "I went back home to continue writing my book."
        
##IAN TUESDAY #####################################################################################################################################################################################################################
    
    $ jiulesson1_error = 0
    stop music fadeout 2.0
    
    $ day = "Tuesday"
    scene blackbg
    with long
    call screen calendar
    $ ian_look = 1
    $ fian = "n"
    scene magazine
    with long
    $ fian = "n"
    show ian
    with short
    if ian_switch_review or ian_honest_review:
        "The next morning I didn't see Minerva in the office."
        "Maybe she was too afraid to show her face? In any case, I felt like I had won the war."
        "Finally something to be proud of."
        if ian_honest_review:
            $ fian = "smile"
            "Other interns asked me to let them read my review. Everyone in the magazine was talking about it."
            "People loved it and thought it was super hilarious and praised me not only for having written it, but for having the balls to present it to Minerva."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
    else:
        "The next day at the magazine was like any other."
        "I did the tasks that were required of me and got a new boring book to review."
        "I didn't intend on putting too much effort into things, just doing enough to get by and don't upset Minerva."
    if v3_ian_date:
        "During the morning I had received another text from Lena."
        $ fian = "smile"
        "She told me her and Holly were meeting tomorrow afternoon, and she invited me to join them."
        if v1_alisonlunch:
            show ian at lef
            with move
            $ fholly = "n"
            show holly at rig
            with short
            i "Hey, Holly! I wasn't aware you also knew Lena!"
            h "Oh, so she already told you about tomorrow?"
            i "Yeah. Did you meet her at the café, too?"
            hide holly
            show holly3 at rig
            with short
            h "Yes, she had read my books and recognized me..."
            i "So she's a fan of yours! What a coincidence..."
        else:
            "I agreed, of course."
    scene magazine
    with long
    "The day went on without any hiccups and it was finally time for me to go the gym."
    
    if ian_lowkick:
        $ kickboxing += 1
    scene gym
    with long
    play music "music/jeremys_theme.mp3" loop
    $ fian = "n"
    if jiujitsu > 0:
        $ ian_look = "gi"
    else:
        $ ian_look = 7
    show ian at lef
    with short
    $ fjeremy = "smile"
## JIUJITSU
    if jiujitsu > 0:
        i "I think the belt is tied like this... Mhh..."
        show jeremy at rig
        with short
        j "Hey, dude!"
        $ fjeremy = "n"
        j "What are you wearing? Don't tell me you really let Wen convince you!"
        i "Yeah, I thought I should give it a try..."
        if v1_fight_kick:
            j "Really? I thought those low kicks worked wonders for you in that fight!"
            i "They did, but I'm curious about Jiu Jitsu. I think I might like it."
        elif v1_fight_grappling:
            j "Come one, you tried it at that street fight and it didn't do shit!"
            i "That's why I want to learn more!"
        else:
            j "Come on, you know striking is much more fun!"
        show ian at lef3
        show jeremy at rig3
        with move
        show wen
        with short
        wen "I see you bought a {i}gi{/i}, so I guess you want me to teach you some grappling!"
        play sound "sfx/friendup.mp3"
        show friend_up
        $ ian_wen += 1
        $ fian = "n"
        i "Yeah."
        wen "Are you sure you don't want to join too, Jeremy?"
        $ fjeremy = "smile"
        j "No, thank you. I'll go work the heavy bag."
        j "You know where to find me when you get bored, Ian!"
        if ian_cherry_sex:
            j "You need to tell me about Thursday night!"
        hide jeremy
        with short
        $ fian = "n"
        if alison_jeremy:
            "I still hadn't asked about Alison... I'd talk to him later."
        show ian at lef
        show wen at rig
        with move
        "Wen came closer and adjusted my belt."
        wen "So, now that I'm gonna teach you a bit of Jiu Jitsu, what would you say is the main difference between grappling and striking?"
        menu:
            "{image=icon_wits.png}Mentality" if ian_wits > 1:
                $ renpy.block_rollback()
                i "I'd say the biggest difference is in the mentality used to approach the fight..."
                i "Striking relies on explosive power, but Jiu Jitsu seems more like a chess match where control is the most important thing..."
                hide wen
                show wensmile at rig
                wen "You're a smart one! Good, that will benefit you a lot in Jiu Jitsu."
                wen "You're right, this is all about strategy. Knowing the techniques and how to set up your attack."
            
            "Technique":
                $ renpy.block_rollback()
                i "Obviously technique, right? Punches and kicks versus throws and submissions."
                wen "Of course, that's true. But I was referring to something a bit deeper."
                wen "Jiu Jitsu is all about strategy, knowing the techniques and how to set up your attack."
             
            "Physical contact":
                $ renpy.block_rollback()
                i "I'd say physical contact. There's a lot more touching and hugging in grappling..."
                wen "You sound like Jeremy, but you're not wrong... On a superficial level."
                wen "In grappling we employ throws and submissions rather than punches and kicks."
                wen "Jiu Jitsu is all about strategy, knowing the techniques and how to set up your attack."
                
            "I don't know":
                $ renpy.block_rollback()
                i "I have no idea."
                wen "Well, it's kind of obvious."
                wen "In grappling we employ throws and submissions rather than punches and kicks."
                wen "Jiu Jitsu is all about strategy, knowing the techniques and how to set up your attack."

        wen "You have to deceive your opponent, lure him into your trap and at the same time read his intentions so you can defend and avoid his threats."
        wen "It's a physical and intellectual battle where you're trying to dictate where the fight goes!"
        i "Isn't striking a bit like that, too?"
        wen "Sure, and there's levels to this thing... But when punches start flying, anything can happen. Even if you're a noob you can get lucky and nail someone."
        wen "That just doesn't happen in Jiu Jitsu. If someone trained grapples someone who doesn't know Jiu Jitsu, the result will always be the same."
        wen "Here, technique is everything. Though strength is important, too..."
        hide wen
        show wensmile at rig
        wen "Especially when it's time to squeeze!"
        "The smile he had on his face when he said \"squeeze\" had me worried..."
        if v1_fight_grappling:
            i "So, are you gonna finish teaching me that technique? You said it was incomplete."
            wen "Oh, yeah. That was the gateway to this. Listen."
        else:
            i "So, what's the first thing you're gonna teach me?"
        wen "The first thing a Jiu Jitsu fighter has to do is take control of the range and bring the fight to where he wants it."
        i "To the floor."
        wen "Right. And that means avoiding strikes and taking down the opponent. So, do you remember how that technique goes?"
        i "Yeah, I try to punch you..."
        scene gym
        show v3_jiu1
        with long
        wen "Come at me."
        "I threw a punch at Wen and he parried it, like he had done with Jeremy when he showed me this technique the first time."
        show v3_jiu2
        with short
        "Like before, too, he closed the distance."
        "But this time he didn't lock his arms around my neck, he drove all his body weight forward, putting me off balance..."
        show v3_jiu3
        with short
        "Next thing I knew, my feet were swept from under me and my body was being accelerated through the air!"
        "I tensed up, feeling the floor disappearing from under my feet and watching the room fly in front of my eyes."
        "But the one flying was me."
        play sound "sfx/throw.mp3"
        show v3_jiu4
        with vpunch
        i "Ooof!"
        "And then, suddenly, my back hit the floor."
        "The shock spread through my body and left me out of breath."
        i "Holy shit!"
        play sound "sfx/xp.mp3"
        show athletics_up
        $ ian_athletics_xp += 1
        call screen skillsup
        $ fian = "surprise"
        scene gym
        show ian at lef
        show wensmile at rig
        with short
        "Wen helped me up."
        "My heart was racing in my chest after that sudden fall's impact."
        wen "That's the first thing you need to learn. It takes practice, though!"
        $ fian = "n"
        wen "Come on, try doing it to me! Or do you want me to show you a second time?"
        menu:
            "Let's try it!":
                $ renpy.block_rollback()
                hide wensmile
                show wen at rig
            "Show me again":
                $ renpy.block_rollback()
                "Wen performed the technique again."
                scene gym
                show v3_jiu1
                with long
                "I threw a punch..."
                show v3_jiu2
                with short
                "He made me lose balance..."
                show v3_jiu3
                with short
                "He kicked my legs from under me..."
                show v3_jiu4
                with vpunch
                "And I hit the mat!"
                scene gym
                show ian at lef
                show wen at rig
                with short
                wen "Got it? Now it's your turn."
        wen "OK, let's go over it! If I punch you, what's the first thing you have to do?"
        $ timeout_label = "jiulessontime"

        menu jiulesson1:
            "Block!":
                $ renpy.block_rollback()
                $ jiulesson1_error += 1
                i "Block!"
                wen "No, you can't just block, you need to close the distance, too!"
                jump jiulesson1
            
            "{image=icon_wits.png}Parry!" if ian_wits >1:
                $ renpy.block_rollback()
                show v3_jiu1
                with short
                i "Parry!"
                wen "Exactly, first the parry, then..."
            
            "Parry!" if ian_wits < 2:
                $ renpy.block_rollback()
                show v3_jiu1
                with short
                i "Parry!"
                wen "Exactly, first the parry, then..."
                
            "Evade!":
                $ renpy.block_rollback()
                $ jiulesson1_error += 1
                i "Evade!"
                wen "No, you can't go backwards! You need to get into close quarters!"
                jump jiulesson1
        
        menu jiulesson2:
            "Hug him!":
                $ renpy.block_rollback()
                $ jiulesson1_error += 1
                i "I need to hug you..."
                wen "What? Have you been paying attention?"
                i "I mean, I need to get chest to chest..."
                wen "Yeah, but what for? What's the purpose?"
                jump jiulesson2
            
            "Kick the legs!":
                $ renpy.block_rollback()
                $ jiulesson1_error += 1
                i "I need to kick your legs from under you!"
                wen "No, not yet! There's a very important step before that!"
                jump jiulesson2
                
            "{image=icon_wits.png}Make him lose his balance" if ian_wits > 1:
                $ renpy.block_rollback()
                show v3_jiu2
                with short
                i "I need to drive my body weight forward and make you lose your balance!"
                wen "Exactly! Don't forget this step, it's crucial!"    
                wen "Now what?"
            
            "Make him lose his balance" if ian_wits < 2:
                $ renpy.block_rollback()
                show v3_jiu2
                with short
                i "I need to drive my body weight forward and make you lose your balance!"
                wen "Exactly! Don't forget this step, it's crucial!"
                wen "Now what?"
        
        menu jiulesson3:
            "Kick the legs!":
                $ renpy.block_rollback()
                show v3_jiu3
                with short
                i "Kick the legs while I keep driving my body forward!"
                wen "Exactly! Use the imbalance you've created to sweep your enemy's feet!"
                show v3_jiu4
                with short
                wen "Then just let gravity do the rest of the work!"
                
            "Pull him up!":
                $ renpy.block_rollback()
                $ jiulesson1_error += 1
                i "Pull him up, and..."
                wen "Think. Pulling him up is the opposite of what you want. You're trying to put him on the floor!"
                jump jiulesson3
            
            "Push him down":
                $ renpy.block_rollback()
                $ jiulesson1_error += 1
                i "Push him down!"
                wen "No, that's not enough! Unless your opponent is completely out of balance, he won't fall like that."
                jump jiulesson3
        $ timeout_label = None
        if jiulesson1_error == 0:
            $ jiujitsu = 2
            play sound "sfx/xp.mp3"
            show athletics_up
            $ ian_athletics_xp += 1
            call screen skillsup
            wen "I knew you were clever! Good job, you'll get the hang of this quicker than I thought."
        elif jiulesson1_error > 1:
            wen "You need to pay attention! Use your head, Ian!"
        else:
            wen "You'll get the hang of this."
        wen "Now's time to practice!"
        scene gym
        with long
        "I spent the next forty-five minutes trying to throw Wen..."
        play sound "sfx/throw.mp3"
        with vpunch
        "And being thrown by him."
        "It was harder than I thought!"
        "By the end I had hit the floor so many times I had the feeling my whole body would be covered by hematomas the next day."
        $ fian = "worried"
        scene gym
        show wensmile at rig
        show ian at lef
        with long
        wen "So, how did you like that?"
        menu:
            "It was great":
                $ renpy.block_rollback()
                $ fian = "smile"
                i "I thought it was great! I really liked the mental aspect of the technique."
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_wen += 1
                wen "Good to hear! You'll love the complete technique, then."
                
            "It was OK":
                $ renpy.block_rollback()
                i "It was OK. Exhausting and a bit repetitive, but OK."
                wen "Practice is key. This is still an incomplete technique, mind you!"

            "Passable":
                $ renpy.block_rollback()
                i "Uh... Passable. A bit too repetitive for my taste..."
                i "And my body is all banged up!"
                wen "Don't be weak, or I won't be able to teach you the complete technique!"

        i "It's still incomplete?"
        wen "Yeah, there's the final piece still missing! But before I teach you that you need to get good at this!"
        wen "I told you Jiu Jitsu needs some time to learn... But once you get a hold of the basics you'll progress fast."
        wen "See you next day!"
        hide wensmile
        with short
        show jeremy at rig
        with short
        j "So, you're done throwing each other around like sacks of potatoes?"
        i "Yeah."
        
## KICKBOXING
    else:
        $ ian_grappling = False
        "I changed into my workout clothes and stepped onto the mat."
        show jeremy at rig
        with short
        j "Hey, dude! Are you ready?"
        i "Let me warm up a bit..."
        if alison_jeremy :
            i "How was it with Alison on Thursday?"
            $ fjeremy = "happy"
            j "Oh man, it was great. I'll tell you about it after the workout."
            if v2_cherry_home:
                j "And you have to tell me about your night, too!"
        elif v2_cherry_home or v2_alison_home:
            j "You need to tell me about Thursday night!"
            i "Sure, when we're done with the workout..."
        j "Put your head gear on, let's do some sparring!"
        menu:                
            "OK, let's spar":
                $ renpy.block_rollback()
                i "Alright, let's spar."
                j "Cool! That's the fun part!"
                play sound "sfx/friendup.mp3"
                show friend_up
                $ ian_jeremy += 1
                scene gym
                show v1_kickboxing1
                with long
                "We did some light sparring that day."
                "I tried to get the best of Jeremy, but to no avail..."
                play sound "sfx/punchgym.mp3"
                scene gym
                show v1_kickboxing2
                with vpunch
                "As always I struggled to get past his long arms and I got hit ten times for every strike I managed to connect."
                "I felt like a fish out of the water..."
                if ian_lowkick:
                    scene gym
                    show v1_kickboxing3
                    with short
                    "I managed to land a few low kicks. That was the most effective weapon I had found so far."
                    play sound "sfx/punchgym.mp3"
                    scene gym
                    show v1_kickboxing2
                    with vpunch
                    i "Oof!"
                    "I was still getting lit up by Jeremy, though."
                "Our skill levels were still too far apart for me to put up a decent fight."
                $ fjeremy = "smile"
                $ fian = "worried"
                scene gym
                show jeremy at rig
                show ian at lef
                show headgear at lef
                with long
                i "Alright... Enough for today."  
            
            "I want to work on technique":
                $ renpy.block_rollback()
                $ kickboxing += 1
                i "I should focus on technique before doing any more sparring, as Wen said."
                $ fjeremy = "n"
                i "Let's work the heavy bag. I should practice fundamentals."
                j "Hm, OK... Sparring's the fun part, though."
                i "It is, but I won't be much of a match if I don't get good technique first!"
                j "That's right. Let's go."
                play sound "sfx/punching_bag.mp3" 
                scene gym
                show v2_box
                with long
                "I practiced combos and proper technique on the heavy bag."
                "I also used the opportunity to vent out all my frustration with Minerva!"
                "It was incredibly tiring and by the end of it my shoulders ached and I was even dizzy, but it had been an awesome workout!"
                play sound "sfx/xp.mp3"
                show athletics_up
                $ ian_athletics_xp += 1
                call screen skillsup
                $ fjeremy = "smile"
                $ fian = "n"
                scene gym
                show jeremy at rig
                show ian at lef
                with long
                i "Whew, I'm beat!"
                j "You went at it really hard today!"
                i "I needed to..."

    i "Come on, let's hit the showers."
    stop music fadeout 2.0
    scene streetnight
    with long
    $ fian = "n"
    $ ian_look = 1
    $ jeremy_look = 3
    show ian at lef
    show jeremy at rig
    with short
    "Once outside, Jeremy got two cans of isotonic drinks and gave me one."
    j "Here, catch. Good to rehydrate after a good workout."
    play sound "sfx/beer.mp3"
    i "Thanks."
    if v2_cherry_home:
        $ fjeremy = "happy"
        j "So, you need to tell me what happened with Cherry! You two were on fire that night!"
        i "Did you notice?"
        j "It was clear to see, I've got an expert eye my friend... So, did you fuck her?"    
        if ian_cherry_sex:
            $ fian = "smile"
            i "Yeah... She spent the night at my place."
            j "Nice!"
            "Jeremy held up his hand and I gave him the high-five he wanted."
            j "She was smoking hot! If I didn't have Alison ripe and ready for the taking I would've tried to go after her!"
            j "That tight booty, and those lips... Damn!"
            $ fian = "shy"
            i "She was pretty amazing, yeah."
            j "I'm jealous, man!"
            $ fian = "n"
            i "Hey, it's not like you have scarcity when it comes to women... Alison included."
            j "Ha ha, yeah!"            
        else:
            $ fian = "insecure"
    elif v2_alison_home:
        $ fjeremy = "happy"
        j "So, tell me what happened with Alison! Did you fuck her?"        
        if ian_alison_sex:
            $ fian = "smile"
            i "Yeah... She spent the night at my place."
            j "Nice!"
            "Jeremy held up his hand and I gave him the high-five he wanted."
            j "Alison was ripe for the taking that night... If you hadn't done it I would have!"
            $ fian = "worried"
            i "She was quite... receptive, yeah."
            j "So, are her tits as nice as they seem to be?"
            $ fian = "shy"
            i "They're pretty nice, yeah..."
            j "Lucky guy! I wish I got to taste them... But it seems she preferred you!"
            $ fian = "smile"
            i "It's not like you have scarcity when it comes to women... I'm sure you can live with one preferring me over you."
            j "It's all cool, bro, ha ha."
        else:
            $ fian = "insecure"
    if v2_ian_limp:
            i "Uh... Not really..."
            $ fjeremy = "n"
            "I told Jeremy the shameful story of that night."
            j "Shit dude, that's not good... Girls don't like it when you go limp on them..."
            i "Has it ever happened to you?"
            j "Yeah, I've been through that, too, tough that was long in the past."
            j "I've got that shit under control now."
            i "How do you do it?"
            $ fjeremy = "happy"
            j "Being a horny motherfucker, and hooking up with hot girls, ha ha!"
            $ fjeremy = "smile"
            j "No, but seriously, it's all about confidence, man. You just need to build that up..."
            j "Get some real field experience! Once you've conquered several beds you will have conquered yourself, too!"
            
    if alison_jeremy:
        "It was time to ask Jeremy about what had really happened on Thursday night."
        $ fian = "n"
        i "So, about you and Alison... Did you..."
        $ fjeremy = "happy"
        j "You can bet your ass I did!"
        menu:
            "Tell me the details!":
                $ renpy.block_rollback()
                $ alison_voyeur = True
                $ fian = "shy"
                i "Really? Tell me the details...!"
                $ fjeremy = "flirt"
                j "Oh, so you wanna know the good stuff, huh?"
                j "Well, Alison's way freakier in bed than I expected! She was all over me right after we got to my place."
                j "She began sucking my cock without me even asking her to, and of course I used those mighty tits of hers to get a nice boob job!"
                i "So she let you stick your cock between her tits?"
                j "Of course man, she loved doing it! And then I crushed her pussy all night!"
                j "She was screaming like a bitch in heat, asking me to give her more. It was awesome."
                i "Damn..."
                $ fian = "smile"
                i "So are you two gonna repeat it?"
                $ fjeremy = "smile"
                j "I'm sure we will. She had a really good time, so it would be strange for her not to come back asking for more."
                i "I see..."
                
            "Good for you":
                $ renpy.block_rollback()
                $ fian = "n"
                i "Good for you, man."
                j "It was pretty awesome. Alison's hornier than she looks!"
                j "It was an intense night alright, heh heh!"
                i "So are you two gonna repeat it?"
                j "We haven't talked about it, but I'd say we will! I want to, at least!"
                j "Those were some mighty tits to enjoy only once! And she had a really good time, so it would be strange for her not to come back asking for more."
                i "I see..."
                
            "I don't wanna hear about it":
                $ renpy.block_rollback()
                $ alison_no_voyeur = True
                $ fian = "serious"
                i "I prefer not to hear about it, honestly."
                $ fjeremy = "n"
                j "Then why did you ask?"
                $ fian = "sad"
                i "To know if there was anything to tell. And since there is, I'd rather not hear about it..."
                j "OK, if that's how you feel..."
        
    if v2_showlena_jeremy:
        $ fjeremy = "happy"
        j "Oh, by the way, I need to tell you something funny!"
        i "Something funny? What is it?"
        j "That girl you told me about, the model..."
        $ fian = "n"
        i "Lena?"
        j "Yes! I met her the other day!"
        $ fian = "worried"
        i "You did? How?"
        j "You remember I told you about a girl I've been dating for a while? The one that was giving me shit lately..."
        i "Yes."
        j "Turns out she's her flatmate! I spent the night this Sunday and I met her the next morning."
        $ fian = "surprise"
        i "Really? That's quite the coincidence...!"
        j "That's what I thought myself! Small world."
        if v3_breakfast_jeremy:
            j "She's a super nice and friendly girl."
            $ fian = "n"
            i "Yeah, she is..."
            j "We had breakfast together and chatted a bit."
        else:
            j "She was kind of cold, though. She doesn't look like the friendliest girl in the world..."
            $ fian = "n"
            i "She is, at least to me."
            j "Maybe I rubbed her the wrong way..."
        if v2_lena_stan_model_shirt:
            $ fjeremy = "flirt"
            j "She's quite shameless, though. She was walking around only in her underwear."
            $ fian = "blush"
            j "I guess it's to be expected from a model, she's used to showing off her body..."
            j "And damn, what a bangable body! She's one of the hottest girls I've ever seen!"
        else:
            $ fjeremy = "smile"
            if v3_breakfast_jeremy:
                j "And she's really pretty! Lovely hair and lovely legs..."
            else:
                j "But she's really pretty! Lovely hair and lovely legs..."
        j "You've found yourself a ten! Don't let her slip!"
        if v2_ian_date:
            i "I hope she won't."
        else:
            i "We'll see what happens."    
    j "Well, I'm gonna get going! See you on Thursday!"
    i "Bye, dude."
    
    play sound "sfx/door_home.mp3"
    scene ianhomenight
    with long
    $ fian = "n"
    $ fperry = "meh"
    "I finally got back to my place."
    show ian at lef
    with short
    i "I'm home."
    show perry at rig
    with short
    p "Hey, dude."
    "Perry, as always, was playing video games in the living room."
    "I sat down next to him and exhaled deeply."
    p "Tough day?"
    i "Pretty much, yeah."
    p "What happened with those book reviews?"
    if alison_jeremy:
        "I told Perry about my day and confrontation with Minerva, the training session and the confirmation of Jeremy and Alison hooking up."
    else:
         "I told Perry about my day and confrontation with Minerva and the training session."
    if v2_showlena_jeremy:
        i "Oh, and turns out Jeremy has met Lena, too."
        $ fperry = "surprise"
        p "He has? How?"
        "I also told him about Jeremy's girl being Lena's flatmate."
        $ fperry = "meh"
        p "It's like having a wolf in the hen house..."
        if ian_jeremy > 4:
            i "Don't say that..."
        else:
            i "I hope not!"
    play sound "sfx/sms.mp3"
    "While we talked I got a text message."
    "I pulled out my phone and looked at it. It was Alison's..."
    if v2_alison_home:
        a "{i}Hey! How are you doing?{/i}"
        i "{i}Surviving. Tough day at the office today.{/i}"
        a "{i}Yeah, me too. It's been a rough start of the week.{/i}"
        a "{i}I just took a long and relaxing shower.{/i}"
        if ian_alison_sex:
            play sound "sfx/sms.mp3"
            $ ian_alison_pics.append("v3_alison_selfie.png")
            show ian at left
            show perry at right
            with move
            show v3_alison_selfie
            with short
            $ fian = "surprise"
            i "Holy--!"
            p "What?"
            "I turned the phone screen to me to hide it from Perry's eyes."
            $ fian = "worried"
            i "No, it's nothing..."
            $ fian = "shy"
            "I looked at the selfie Alison had just sent me. I wasn't expecting that... But it was a very welcome surprise."
            i "{i}Looks like the shower worked for you, because you're looking mighty good.{/i}"
            a "{i}Thanks! I got the impression you liked looking at me last night, so...{/i}"
            i "{i}You have no idea how much I liked it.{/i}"
            a "{i}Oh, I did get an idea {image=emoji_flirt.png}{/i}"
            hide v3_alison_selfie
            show ian at lef
            show perry at rig
            with move
            p "Who are you talking to?"
            $ fian = "smile"
            i "Alison."
            p "Oh."
        a "{i}I had so much fun Thursday at the bar. We should hang out again soon!{/i}"
        i "{i}Yeah, we definitely should.{/i}"
        a "{i}How about tomorrow? This week's being awful, I really need it!{/i}"
        if v2_ian_limp:
            "I thought after my awful performance she wouldn't want to meet me again, but it seemed like she didn't care..."
            "Well, maybe she just wanted to meet as friends and nothing more, but I wasn't getting that vibe..."
            if v3_ian_date:
                "This could be my chance to make up for my failure last time, but...!"
            else:
                "This could be my chance to make up for my failure last time...!"
    else:
        a "{i}Hey, how are you doing?{/i}"
        "I wasn't expecting her to text me all of a sudden."
        i "{i}Surviving. Tough day at the office today.{/i}"
        a "{i}Yeah, me too. It's been a rough start of the week.{/i}"
        a "{i}I miss you!{/i}"
        "I wasn't expecting that either! She missed me? Since when?"
        a "{i}We should meet tomorrow! This week's being awful, I really need a distraction!{/i}"
        "Why was she asking me instead of Jeremy? If she was in need of a distraction I assumed she would ask him..."
    if v3_ian_date:
        "I had already made plans with Lena and Holly tomorrow afternoon..."
        "If I wanted to meet Alison I would need to cancel with them."
        menu:
            "Meet Lena and Holly":
                $ renpy.block_rollback()
                $ fian = "n"
                "I was really looking forward to hanging out with Lena and Holly. They took priority over Alison."
                i "{i}I can't, I already have plans.{/i}"
                a "{i}Really? What are you doing?{/i}"
                i "{i}I'm hanging out with Lena and Holly, a co-worker of mine.{/i}"
                if v2_alison_home:
                    $ ian_alison -= 2
                else:
                    $ ian_alison -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                a "{i}Oh, I see. I can't compete with those girls, especially if one's a model.{/i}"
                a "{i}See you some other day, then!{/i}"
                i "{i}Sure. Let's find another date to meet.{/i}"
                a "{i}I'm pretty busy, but yeah. Some other time!{/i}"
            "Meet Alison instead":
                $ renpy.block_rollback()
                $ v3_alison_date = True
                $ fian = "smile"      
                i "{i}Alright, let's meet tomorrow afternoon.{/i}"
                if ian_alison_sex:
                    "It felt wrong leaving her hanging after what we had shared last night."
                elif v2_ian_limp:
                    "Alison and I had unfinished business, and that had to be resolved."
                else:
                    "I was curious to see what she wanted of me..."
                a "{i}OK! See you at eight, is that cool?{/i}"
                i "{i}Yeah, sounds good.{/i}"
                a "{i}See you tomorrow then {image=emoji_kiss.png}{/i}"
                "Now I had to send a message to Lena to tell her I wouldn't be able to make it tomorrow."
                "I was looking forward to hanging out with her and Holly, but Alison took priority."
                i "{i}Hey Lena, something came up and I won't be able to join you and Holly tomorrow. I'm sorry!{/i}"
                play sound "sfx/sms.mp3"
                l "{i}Oh, that's too bad... {image=emoji_sad.png} Well, I hope to see you soon!{/i}"
                i "{i}Yeah, me too.{/i}"
    else:
        i "{i}What do you wanna do?{/i}"
        a "{i}I don't know, take a walk, maybe we can have dinner or something like that.{/i}"
        menu:
            "Meet Alison":
                $ renpy.block_rollback()
                $ v3_alison_date = True
                if ian_alison_sex:
                    "Of course I wanted to meet her after what happened last night."
                elif v2_ian_limp:
                    "Alison and I had unfinished business, and that had to be resolved."
                else:
                    "I was curious to see what she wanted of me..."
                $ fian = "smile"
                i "{i}Alright, let's meet tomorrow afternoon.{/i}"
                a "{i}OK! See you at eight, is that cool?{/i}"
                i "{i}Yeah, sounds good.{/i}"
                a "{i}See you tomorrow then {image=emoji_kiss.png}{/i}"
                
            "I can't":
                $ renpy.block_rollback()
                $ fian = "n"
                if v2_ian_limp:
                    "I honestly didn't want to face her again, not so soon at least, after what had happened."
                    "I felt too ashamed."                    
                elif ian_alison_sex:
                    "I felt kinda bad refusing to see her after what had happened between us last time, but..."
                    "Maybe it was because of that, in fact. I didn't want Alison to get any ideas about us..."
                else:
                    "I just didn't feel like hanging out with her."
                    if ian_alison_interest > 1:
                        "It was not my responsibility to distract her from her problems. She had Jeremy for that."
                i "{i}Sorry Alison, but I can't.{/i}"
                if v2_alison_home:
                    $ ian_alison -= 2
                else:
                    $ ian_alison -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                a "{i}Why not? You're busy?{/i}"
                i "{i}Yeah, I have a lot to do...{/i}"
                a "{i}Oh, I see. Too bad, I wanted to see you.{/i}"
                if alison_jeremy:
                    i "{i}I'm sure you'll find someone else to distract you.{/i}"
                    a "{i}Yeah. See you next time!{/i}"
    scene ianroomnight
    with long
    $ fian = "n"
    "After that I went to my room to write a bit more before going to sleep."
 
##IAN WEDNESDAY #####################################################################################################################################################################################################################
    $ fholly = "n"
    $ day = "Wednesday"
    scene blackbg
    with long
    call screen calendar
    scene magazine
    with long
    show ian 
    with short
    "It was another day at the office."
    if ian_switch_review:
        $ fian = "smile"
        "People were still talking about what had happened on Monday and some showed interest in reading my review."
        "I decided to print a few copies to let them read it and give me their opinion."
    elif ian_honest_review:
        $ fian = "smile"
        "People were still coming up to me to tell me how funny and outrageous they found my review."
        "It seems like copies had been circulating around the magazine, and somebody even told me I should publish it somewhere."
        "That was a really good idea, actually..."
    else:
        "Everything was as usual. Nothing had changed, and I continued to take care of the menial tasks I was assigned."
    show ian at lef3
    with move
    show holly2 at rig3
    with short
    $ fian = "smile"
    if v3_ian_date and v3_alison_date:
        i "Hey Holly. I won't be able to come this afternoon..."
        $ fholly = "sad"
        h "Oh, is that so?"
        i "Yeah, something came up... I'm sorry, I was looking forward to hanging out with you and Lena."
        h "Yeah, me too..."
        i "I'm sure you two will have fun, though!"        
    elif v3_ian_date:
        i "Good morning, Holly."
        $ fholly = "smile"
        h "Hi, Ian. We're still meeting this afternoon after work, right?"
        i "Of course!"
        $ fholly = "shy"
        h "I'm looking forward to it..."
    else:
        i "Good morning, Holly."
        h "Hi, Ian."
        i "How's your Wednesday looking?"
        h "I'd say it's looking pretty good..."
        if v1_alisonlunch:
            h "Oh, I haven't told you yet!"
            h "I'm hanging out with Lena this afternoon. She told me you know each other."
            $ fian = "surprise"
            i "Oh, you're friends with Lena?"
            h "We met at the café, just like you two... Turns out she had read my books and recognized me..."
            "I was surprised by this revelation, but it made sense, actually. Holly frequented that café, too, and Lena had talked to me when she saw me reading..."
            "No wonder she had made conversation with Holly, too, especially if she knew her work!"
            $ fian = "smile"
            i "So she's a fan of yours! What a coincidence..."
        else:
            h "I'm hanging out with Lena this afternoon."
            i "Oh, you are? It seems you two are getting along pretty nicely."
        h "Yes, she's really nice..."
        i "She is, yeah."
        
    if ian_switch_review or ian_honest_review:
        play music "music/danger.mp3"
        $ fminerva = "mad"
        show minerva
        with short
        $ fian = "worried"
        $ fholly = "sad"
        "As I was talking with Holly Minerva appeared in front of me."
        "Of course, she didn't look too happy."
        mi "Ian. To my office, now. We need to talk."
        "I looked at Holly before getting up and following Minerva."
        hide holly2
        with short
        play sound "sfx/door.mp3"
        show ian at lef
        show minerva at rig 
        with move
        $ fian = "n"
        "She closed the door and sat behind her desk."
        mi "Take a seat."
        menu:
            "Take a seat":
                $ renpy.block_rollback()
                "I sat down in front of her."
                "Better to do this as she asked and not upset her any more. This seemed serious."
                play sound "sfx/xp.mp3"
                show wits_up
                $ ian_wits_xp += 1
                call screen skillsup
                mi "Good."
                
            "Stay standing":
                $ renpy.block_rollback()
                $ fian = "serious"
                i "I'll stand."
                play sound "sfx/xp.mp3"
                show charisma_up
                $ ian_charisma_xp += 1
                call screen skillsup
                mi "You won't drop your confrontational attitude, I see."
                mi "Have it your way."
        
        mi "I won't beat around the bush: I don't know who or where you think you are, but your behavior is completely unacceptable."
        $ fian = "serious"
        i "Is that so? I thought I..."
        $ fminerva = "furious"
        mi "Let me finish!" with vpunch
        $ fminerva = "mad"
        mi "I won't tolerate that behavior. You're here to work, not to play games!"
        mi "This is a serious literary magazine, not a schoolyard!"
        mi "Your actions are disrupting the working environment and are hurting the magazine. That's why I'm reducing your contract."
        mi "You'll only be working from Monday to Wednesday from now on."
        $ fian = "mad"
        i "What? You can't do that!"
        $ fminerva = "furious"
        mi "Sure I can! Haven't you read the contract? You're here on a temporary internship!"
        $ fminerva = "mad"
        mi "I find your performance lacking and I can cut working hours off it, with the corresponding pay cut, of course."
        i "You're just being fucking unfair again!"
        mi "Watch your language! And be thankful I'm not firing you right away!"
        i "If you aren't doing it it's probably because you can't."
        mi "Keep giving me reasons to and I'll be more than happy to do it!"
        if ian_switch_review:
            mi "I'd love be rid of you, believe me, after what you pulled off."
            mi "Did you enjoy tricking me in front of the whole magazine? Did your little game give you satisfaction?"
            $ fminerva = "furious"
            mi "You even turned Holly against me!"
            mi "How could you manipulate such a naive and innocent girl? You're despicable."
            i "I didn't manipulate her! I just asked for help because she knows as well as I do that you've been treating me unfairly!"
            mi "What would you know about fairness?"
            i "I know some things. I'm not a stupid kid anymore."
            mi "Then stop acting like one!"
            i "Me? Who's acting like a kid here? I proved to you I'm good at my job! You said it yourself, that review was amazing!"
            i "You only said that because you thought Holly wrote it, of course. You won't ever admit I've done a good job and I have no idea why!"
        if ian_honest_review:
            mi "You think you can take my assignments as a joke?"
            i "They are a joke! This is no literary magazine!"
            i "You don't want reviews, you want ads for the crap that those publishers are pumping out!"
            i "People deserve real, honest reviews! The literary industry is in shambles and this magazine is part of the problem!"
            $ fminerva = "furious"
            mi "And you've come to save us all? How arrogant can you be?"
            mi "You'll do as you're told! And if you don't like it you're welcome to leave!"
            mi "But don't worry, you won't be reviewing anything else from now on."
            i "How much are they paying you to protect them like this? I hope you're selling your integrity at a high price, at least."
            mi "Enough!" with vpunch
            mi "Watch your words and what you're implying, young man!"        
        $ fminerva = "mad"
        mi "I'm tired of this conversation. I have nothing else to say and I hope I made myself clear."
        mi "Any more shenanigans from you and I'll kick you out from this magazine so quick you won't ever know what happened!"
        $ fminerva = "furious"
        mi "Are we clear?"  with vpunch
        i "...!"
        $ fminerva = "mad"
        "I clenched my fists in anger. I had nothing to fight back at that moment."
        $ fian = "serious"
        i "Sure."
        stop music fadeout 2.0
        play sound "sfx/door.mp3"
        hide minerva
        with short
        "I got out of Minerva's office and closed the door trying to control my anger."
        "This was so fucked up... I would quit this job if I could, but I needed the money..."
        "In fact, with a pay cut, I wouldn't get enough to cover all my monthly expenses... And my position in this magazine was doomed."
        "Minerva would fire me as soon as she got the chance. I still had a few months left on my contract, but still..."
        "I wasn't wanted here. She couldn't have made it more clear."
        i "Fuck..."
        
    else:
        i "Well, I'll get back to work..."
        if v3_ian_date and v3_alison_date == False:
            i "We'll talk later!"
            $ fholly = "smile"
            h "Yeah!"
        else:
            i "Say hi to Lena on my behalf!"
            h "I will."
        scene magazine
        with long
        
    if v3_alison_date:
        jump v3datealison
        
    else:
        scene street
        show ian
        with long
        if ian_minerva_review:
            "I wasn't too thrilled about things after another boring day at the magazine."
            if v3_ian_date:
                i "I hope hanging out with Lena and Holly will cheer me up a bit."
            else:
                "I went back home, where I could focus on something that could make me feel some joy..."
        else:
            "I was furious and worried. My victory on Monday had been completely turned around by Minerva."
            if ian_honest_review:
                i "Though I don't know what I was expecting, honestly..."
                i "Maybe writing that honest review wasn't such a good idea. Maybe if it hadn't been *{i}that{/i}* honest..."
            else:
                "Least I expected was to be recognized for my work, but not even that seemed possible..."
                i "Oh God, how I hate her..."
            i "And I have to think on where to get the money from I'm missing after this pay cut..."
            i "At least I hope to get close to full pay this month, but after that..."
            i "I don't want to think about that now..."
            if v3_ian_date:
                "I was about to meet Lena and Holly and I didn't want to be in a sour mood."
                i "I'll worry about it later..."
            else:
                "I went home and tried to forget about it."
        jump v3lenawednesday        
        
## ALISON DATE ####################################################################################################################################################################################################################
label v3datealison:    
    scene ianroomnight
    with long
    show ian
    with short
    if ian_minerva_review:
        "I wasn't too thrilled about things after another boring day at the magazine."
        $ fian = "n"
        "Hopefully hanging out with Alison would make my day a bit brighter."
    else:
        "I was furious and worried. My victory on Monday had been completely turned around by Minerva."
        if ian_honest_review:
            i "Though I don't know what I was expecting, honestly..."
            i "Maybe writing that honest review wasn't such a good idea. Maybe if it hadn't been *{i}that{/i}* honest..."
        else:
            "Least I expected was to be recognized for my work, but not even that seemed possible..."
            i "Oh God, how I hate her..."
        i "And I have to think on where to get the money from I'm missing after this pay cut..."
        i "At least I hope to get close to full pay this month, but after that..."
        i "I don't want to think about that now..."
        i "I'm meeting Alison and I don't want to be in a sour mood."
        $ fian = "n"
        i "I'll worry about it later..."
    "I thought about what to wear."
    "Last time Alison was dressing quite fashionably... I should try and match her a bit."
    hide ian
    with short
    $ ian_look = 3
    "I searched a bit in my wardrobe, between shirts, hoodies and sweatshirts, some of which I had for almost ten years."
    i "Maybe this one..."
    show ian
    with short
    i "Hm, yeah, I guess this'll do."
    i "Let's go."
    $ falison = "smile"
    if alison_sexy:
        $ alison_look = 2  
    else:
        $ alison_look = 1
    scene streetnight
    with long
    show ian at lef
    with short
    "I met Alison on the street, at the spot we had agreed on."
    play music "music/flirty.mp3" loop
    show alison at rig
    with short
    a "Hey, there you are!"
    if alison_sexy:
        if ian_alison_sex:
            $ fian = "shy"
            i "Oh, you're looking sexy!" 
        else:
            $ fian = "blush"
            i "Oh... You're looking... nice."
        $ falison = "flirt"
        a "Well, you said this style suited me the other night so... I listened."
        $ fian = "smile"
        i "It does, it really suits you."
        a "I'm glad you think that way!"
        a "I like your shirt, too, by the way."
        i "Thanks!"
    else:
        $ fian = "smile"
        i "Hey, Alison."
        a "Nice shirt!"
        i "Thanks."
    $ falison = "n"
    a "So, where do you wanna go?"
    i "We can go to the Fortress. It's close by and they make pretty good burgers before ten."
    a "Sure, why not."
    scene rockbar
    with long
    "Last night the bar wasn't crowded at all, but on a Wednesday, at this early hour, it was practically empty."
    $ fian = "sad"
    $ falison = "n"
    show ian at lef
    show alison at rig
    with short
    i "Damn, this place has seen better days..."
    a "It's a curious place to have dinner, but sure, let's try it."
    $ fian = "smile"
    i "You've never eaten here? I think it's good."
    a "It's dark."
    if ian_alison_sex:
        $ fian = "confident"
        i "Sounds like a plus to me."
        $ falison = "smile"
        a "Seen from a certain perspective, I guess it is, ha ha."
        $ falison = "n"
    else:
        i "Yeah, a bit, ha ha..."
    "We took a seat and we ordered a few hamburgers, beers and some fries."
    a "Sometimes I feel I'm back in my teenage years when I'm out with you!"
    $ fian = "worried"
    "Was she calling me immature?"
    "Granted, this kind of dinner felt more like one a teenager would have on a night out rather than one a twenty-seven-years-old would."
    "Though I couldn't be spending money in expensive restaurants in my current situation..."
    if ian_honest_review or ian_switch_review:
        "Even less right now!"
    a "So, how's your week going?"
    if ian_honest_review or ian_switch_review:
        $ fian = "n"
        i "Oh boy, let me tell you about what happened at work..."
        $ falison = "surprise"
        "I told Alison about my fight with Minerva."
        a "That's not good!"
        i "No, it's not. But I had to do something, I couldn't keep eating dirt day after day in that job..."
        $ falison = "flirt"
        a "You've always been a rebel, but you've gotten even worse with age!"
        $ fian = "smile"
        i "Ha, that's one way to see it..."
    else:
        i "Pretty boring actually... Working at my job, trying to write the book..."
    if v2_cherry_home:
        $ falison = "flirt"
        a "So, you need to tell me about Cherry! You're a sly one, using me to meet girls and seducing them."
        $ fian = "blush"
        i "Hey, it's not like that..."
        a "I never expected that to happen. I thought you and Cherry wouldn't have anything in common."
        $ fian = "smile"
        i "Well, it seems we did."
        a "Yeah, yeah, I can see that... So did you enjoy yourselves?"
        if ian_cherry_sex:
            $ fian = "shy"
            i "Yeah, we did."
            a "She said you were pretty good..."
            $ fian = "surprise"
            i "Me? What the hell did you two talk about?"
            a "Oh, you know, I just wanted to know how her night had been... She didn't give me the details though."
            $ fian = "smile"
            i "And I won't either... But I'm glad to see my performance was appreciated, ha ha."
            a "She told me she wasn't looking for a boyfriend, though."
            i "I know. She told me, too."
            a "And aren't you disappointed?"
            if ian_cherry_free:
                i "Me? Not at all, I wasn't looking for a relationship either."
            else:
                i "No, no... I've known her for just a night. It's not like I wanted to make her my girlfriend or anything."
            a "I see."
        else:
            $ fian = "insecure"
            i "Uh... Not really."
            $ falison = "surprise"
            a "So nothing happened?"
            i "Nope... Well, yeah, something happened. Just a bit."
            a "Just a bit?"
            i "I mean, we made out a bit and something more, but we didn't fuck."
            a "What? How come? If you two were making out already..."
            "I wanted to drop that subject as quickly as possible."
            i "The mood just wasn't right, I don't know. Can we talk about something else?"
            $ falison = "n"
            a "Sure, sure."
            $ fian = "n"

    a "So, let me tell you about my awful week so far!"
    $ fian = "n"
    i "Of course."
    $ falison = "sad"
    a "Well, not just the week... It's been pretty shitty for quite some time!"
    a "I broke up with my boyfriend so I couldn't keep living with him, but I had also just lost my job and they owe me a ton of money."
    a "So I had to go back to living with my parents!"
    i "You moved out a few years ago... You must've gotten pretty used to living by yourself."
    a "Yes, I can't stand being back at my parents' home. It's like I've been sent back to the past and I'm stuck there."
    a "They treat me like I was a kid who can't tell left from right and right from wrong. Well, I have two master degrees!"
    a "My parents just don't care. They still act like I had no idea of what I'm doing with my life."
    a "Though seeing how things are going for me, maybe they're not entirely wrong..."
    a "I'm overqualified for my new job, yet I can barely keep up thanks to the pile of work they're dumping on me."
    a "They're short on staff and money. It's almost like I have to thank them for giving me a job..."
    a "But considering how the city's economy is looking lately, having a job is starting to feel like a luxury."
    "Alison went on and on and on complaining about her life's situation."
    a "Still, it's not my fault that my boss was a crook! And it's not my fault my ex-boyfriend was a whack!"
    a "Things should be going good for me, but it's like the world is conspiring against me!"
    menu:
        "{image=icon_charisma.png}You're tough" if ian_charisma > 1:
            $ renpy.block_rollback()
            $ fian = "smile"
            i "I'm not worried about you. You're one of toughest people I know."
            $ ian_alison += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            $ falison = "n"
            a "I know. I just like to complain to take it out of my system, but I'm alright."
            a "I don't give up and I'm hard-working, so I'm keeping my faith still."
            a "At least until I turn thirty!"
            i "I have faith in you, too."
            
        "It will get better":
            $ renpy.block_rollback()
            i "I know it's what people always say, but it will get better..."
            a "I hope it will, that's what I'm working my ass off for!"
            a "I just hope it would get better now and not in like, two years, when I'm already thirty!"
            $ falison = "n"
            a "In any case, \"it\" won't get better by itself. I'll have to force it to!"
            
        "I don't know what to tell you":
            $ renpy.block_rollback()
            $ fian = "sad"
            i "I don't know what to tell you, Alison..."
            a "I'm not looking for answers in other people's opinion."
            $ falison = "serious"
            a "Everybody knows exactly what I should do and how I should feel, but they preach from a sinking ship."
            a "Their life is no better than mine!"
            $ falison = "n"
            a "Whatever, I just like to complain."
   
    if alison_jeremy:
        $ fian = "n"
        if v2_cherry_home:
            "Alison had talked about a lot of things, my relationship with Cherry included, but she hadn't mentioned anything about Jeremy..."
        else:
            "Alison had talked about a lot of things but she hadn't mentioned anything about Jeremy..."
        "He had already told me what happened that night, but it felt weird that Alison was avoiding the subject."
        "I felt the need to ask."
        i "So... How did things end up with Jeremy?"
        $ falison = "n"
        a "Oh, it went well. We had a nice time."
        i "I was quite... surprised, to be honest."
        a "Surprised? Why?"
        i "I never knew you and Jeremy had a thing for each other."
        a "I didn't either... But he made it very clear he was interested in me."
        menu:
            "So that's all it takes?":
                $ renpy.block_rollback()
                a "So that's all it takes?"
                $ falison = "serious"
                a "What do you mean by that?"
                i "I mean, if he hadn't shown interest in you you wouldn't have tried anything with him?"
                $ falison = "n"
                a "Oh. No, I don't think so. I'm tired of fighting losing battles."
                a "I won't try to force myself on someone who's not interested in me."
                i "I see. So it's not like you were pursuing Jeremy..."
                a "It was the other way around. But since he raised the game I thought it could be interesting playing it."
                a "It's not like he was my first option. But at least he wanted to play..."
                a "After all he's a good looking guy, tall and charming... And he made it very clear what he wanted, so..."
                a "We girls like that. It's nice feeling desired, you know."
                i "Yeah, of course..."
                if ian_alison_interest > 0:
                    jump v3alisondatekiss
                else:
                    jump v3alisondateend
                
            "I'd say the interest was mutual":
                $ renpy.block_rollback()
                i "I'd say the interest was mutual..."
                a "Well, he's a good looking guy, tall and charming... And he made it very clear what he wanted, so..."
                a "We girls like that. It's nice feeling desired, you know."
                i "Yeah, of course..."
                a "In any case, it was him who raised the game. If he hadn't I wouldn't have played."
                a "Is it wrong for me to want to have some harmless fun?"
                i "No, I'm not saying that..."
                a "It's not like he was my first option. But at least he wanted to play..."
                if ian_alison_interest > 0:
                    jump v3alisondatekiss
                else:
                    jump v3alisondateend
                
            "You shouldn't have done it":
                $ renpy.block_rollback()
                i "You shouldn't have done it..."
                $ falison = "serious"
                a "You have an objection?"
                $ fian = "sad"
                i "I mean, it's never wise to mix friendships and sex..."
                $ ian_alison -= 1
                play sound "sfx/frienddown.mp3"
                show friend_down
                a "I already have my new boss and my parents on my back. I don't need anybody else telling me what I should and shouldn't do."
                a "We're not kids in high school anymore. We're responsible adults with our own lives. I hadn't seen Jeremy in a long time, so I don't think I'm being disruptive."
                a "Besides, if that's how you think, you should tell that to him, too, not just me."
                i "I also did..."
                if ian_cherry_sex:
                    a "Whatever. You had sex with Cherry and I'm not complaining to you about sleeping with my friends."
                else:
                    a "Whatever."
                i "Sorry. I didn't intend to judge."
                $ falison = "n"
                a "You did, but it's OK."
                jump v3alisondateend
    
    if ian_alison_sex:
        "We were talking like we always used to, like nothing had changed... But I couldn't see her just as my friend anymore."
        "My eyes and my thoughts kept getting lost in her body..."
        "In her deep brown eyes, her beautiful lips, her clean jawline, her smooth collarbone, her lavish cleavage..."
        $ falison = "flirt"
        "I was being more obvious than I intended, because she noticed."
        a "What? Seeing something you like?"
        $ fian = "shy"
        i "Indeed."
        a "Have you even been listening to me?"
        i "Yeah, of course."
        $ fian = "confident"
        i "It's just hard to avoid admiring you. Especially after that selfie you sent me..."
        a "Oh, you liked that one, didn't you?"
        i "Do you need to ask?"
        a "I don't know. I'd ask if you prefer seeing me on pictures or maybe you want to see me live again..."
        i "Pics are cool, but nothing beats a live performance."
        a "I see we're on the same page, then..."
        scene rockbar
        show v3_alison1
        if alison_sexy:
            show v3_alison1_red
        else:
            show v3_alison1_green
        show v3_alison1_shirt
        with long
        "There was no reason to keep holding back."
        "I leaned forward and kissed Alison's warm lips. She accepted my kiss more than willingly, responding with her own."
        "It still felt somewhat weird, tasting her, feeling her tongue on mine, her hands on my hair..."
        "It felt weird, but awesome."
        "As we made out I could clearly feel her growing passion. I would've never imagined Alison could feel this way about me..."
        "We were both hungry for each other."
        $ fian = "confident"
        $ falison = "slut"
        scene rockbar
        show ian at lef
        show alison at rig
        with long
        a "Say... Can we go to your place?"
        i "Of course. I was about to invite you over..."
        a "Then I'd say we're done here... Let's go!"
        stop music fadeout 2.0
        jump v3alisondatesex
        
    if v2_alison_home and v2_ian_limp:
        "The conversation had been going well. I was able to forget about the shame I felt after failing to perform the other night..."
        "That was until Alison tackled the subject head on."
        $ falison = "n"
        a "So, about last night, what happened..."
        $ fian = "worried"
        i "Um, that... I'm sorry, I know I messed up. It's very embarrassing."
        a "It's OK... I was really liking how things were playing out before that..."
        a "And well... I'm still curious to know how it would've continued."
        a "So, do you think we can give it another go?"
        $ fian = "surprise"
        "She was still willing to try it with me, despite my fuck-up?"
        "I wasn't really understanding why or how, but I was getting another chance..."
        menu:
            "{image=icon_lust.png}I want you, Alison" if ian_lust > 1:
                $ renpy.block_rollback()
                $ fian = "n"
                "Backing down now would be a pussy move! I had to step up to the circumstances."
                "Alison still wanted me. And I wanted her, too."
                $ fian = "confident"
                i "I really want you, Alison. I want to do it with you."
                $ falison = "flirt"
                a "I was hoping to hear that."
                
            "{image=icon_wits.png}+{image=icon_charisma.png}This time it will work" if ian_wits > 0 and ian_charisma > 1:
                $ renpy.block_rollback()
                $ fian = "n"
                "She still wanted me, even after my shameful performance..."
                "It was time to erase that awful moment and show Alison I was capable of giving her a good time."
                $ fian = "confident"
                i "I'm curious about it, too. I wanted to know so badly... And I still want to."
                $ falison = "flirt"
                a "I was hoping to hear that."
                
            "Let's better not":
                $ renpy.block_rollback()
                $ fian = "sad"
                i "I think we should better not..."
                $ falison = "sad"
                a "Oh."
                "I wasn't finding the confidence I needed. I felt I would only disappoint her again, and I wouldn't have that."
                i "I think it's better if we forget about this... thing and go back to just being plain, regular friends."
                $ ian_alison -= 2
                play sound "sfx/frienddown.mp3"
                show friend_down
                a "Sure, if that's how you see it..."
                a "I guess we shouldn't even have tried in the first place, right?"
                i "Maybe..."
                a "Well, never mind. Another disappointment, but I'm used to it by now."
                jump v3alisondateend
         
        scene rockbar
        show v3_alison1
        if alison_sexy:
            show v3_alison1_red
        else:
            show v3_alison1_green
        show v3_alison1_shirt
        with long
        "I leaned forward and kissed Alison's warm lips. She accepted my kiss more than willingly, responding with her own."
        "It still felt somewhat weird, tasting her, feeling her tongue on mine, her hands on my hair..."
        "It felt weird, but awesome. This time, for sure, it would work."
        "As we made out I could clearly feel her growing passion. I would've never imagined Alison could feel this way about me..."
        "We were both hungry for each other. Feeling that her passion was still there gave me the confidence I lacked the other night."
        $ fian = "confident"
        $ falison = "slut"
        scene rockbar
        show ian at lef
        show alison at rig
        with long
        a "Say... Can we go to your place?"
        i "Of course. I was about to invite you over..."
        a "Then I'd say we're done here... Let's go!"
        stop music fadeout 2.0
        jump v3alisondatesex
            
label v3alisondatekiss: 
    $ fian = "n"
    $ falison = "n"
    "We were done with dinner and it was about time to get going."
    "As we got up I thought about what Alison had just told me."
    "So what she had been looking after was feeling desired?"
    "And the reason why Jeremy had taken her was because he wasn't afraid to show his desire for her?"
    if ian_wits > 1:
        "She had said Jeremy hadn't been her first option... What did she really mean by that?"
    "What would've happened if I had shown a clear interest in Alison that night?"
    "Did I really want to find out?"
    menu:
        "{image=icon_will.png}Kiss Alison" if ian_will > 0:
            $ renpy.block_rollback()
            "Yes, yes I did."
            $ ian_will -=1
            show will_down
            play sound "sfx/willdown.mp3"
            scene rockbar
            show v3_alison1
            if alison_sexy:
                show v3_alison1_red
            else:
                show v3_alison1_green
            show v3_alison1_shirt
            with long
            "Somehow I managed to push my doubts and insecurities to the back of my mind and acted without even thinking."
            "I leaned forward and kissed Alison's warm lips."
            "I noticed her surprise, but it only lasted a second. She accepted my kiss more than willingly, responding with her own."
            "It was happening. I was kissing her and she was kissing me back..."
            "It felt weird, but awesome."
            "As we made out I could clearly feel her growing passion. I suspected Alison could feel this way about me, even if it was hard to believe..."
            "Seems like her hooking up with Jeremy had been of no real significance. I felt Alison's honest hunger for me, her passion and desire..."
            if v2_cherry_home:
                a "You're awful... You don't have enough with Cherry and want me, too?"
                "Despite her saying that she didn't seem against it at all..."
                "I kissed her again, and she welcomed my lips and my tongue."
            $ fian = "confident"
            $ falison = "flirt"
            scene rockbar
            show ian at lef
            show alison at rig
            with long
            a "What's up with this sudden fit of passion, Ian?"
            i "Don't play dumb... You can't tell me you're surprised."
            a "I am... But it's a very nice surprise..."
            if v2_cherry_home:
                i "I should've done this the other night..."
                a "You were too busy with Cherry..."
                i "And you were too busy with Jeremy!"
                a "Well, if you had been a bit more obvious about what you really wanted, instead of flirting with my friend all night..."
            else:
                i "I should've done this the other night... But you were too busy with Jeremy."
                a "If you had been a bit more obvious about what you really wanted..."
            i "Well, I'm being plenty obvious now."
            i "Say... Do you want to have one final beer at my place?"
            a "I was hoping you'd offer..."
            i "Then I'd say we're done here... Let's go!"
            stop music fadeout 2.0
            jump v3alisondatesex
         
        "Leave things as they are":
            $ renpy.block_rollback()
            "I decided it was better to leave things as they were."
            if ian_alison_interest > 1:
                "I found Alison really attractive, but she was first and foremost my friend."
            else:
                "Alison was attractive, but she was first and foremost my friend."
            "I didn't want to make things more complicated than they needed to be."
            "Besides, she and Jeremy already had something going on, didn't they?"
            if v2_cherry_home:
                "Not to mention I had hooked up with Alison's friend, too..."            
            jump v3alisondateend

label v3alisondateend:
    $ fian = "n"
    $ falison = "n"
    a "Well, I guess I should get going. Tomorrow I have to get to work early..."
    i "Yeah, me too."
    "She smiled and pinched my cheek."
    a "It's been nice hanging out with you. I always enjoy it."
    $ fian = "smile"
    i "Anytime."
    a "See you!"
    jump v3lenawednesday
    
## ALISON  SEX

label v3alisondatesex:
    stop music fadeout 2.0
    play sound "sfx/door_home.mp3"
    scene ianhomenight_dark
    with long
    $ fian = "confident"
    $ falison = "flirt"
    "When we arrived at my place the lights were out. Perry was in his room, maybe sleeping."
    "Perfect."
    if v2_alison_home == False:
        a "So this is your new place... You never invited me here before."
        i "I just found the best reason possible to do so."
        a "How about you show me your room, next?"
        i "Of course."
    else:
        a "Here we are again..."
        i "Let's go to my room. We don't want to be disturbed..."
    play music "music/sensual.mp3" loop
    scene ianroomnight
    show v3_alison1
    if alison_sexy:
        show v3_alison1_red
    else:
        show v3_alison1_green
    show v3_alison1_shirt
    with long
    "As soon as we got into my room we began making out again."
    "Alison wrapped her arms around my neck as she kissed me deeply."
    "Her taste and sweet smell overwhelmed my senses, our bodies rubbing against each other with growing need."    
    scene ianroomnight
    show v3_alison1
    with long
    if v2_alison_home:
        "Soon our hands, eager to explore each other's bodies a second time, stripped us of our clothes."
    else:
        "Soon our hands, eager to explore each other's bodies, stripped us of our clothes."
    "The touch of her naked skin on mine made me shiver, her soft boobs pressed against my chest made by blood boil..."
    "And of course my cock got hard as an iron rod, aroused by Alison's uncovered sensuality."
    if ian_alison_sex:
        "Alison reached down and grasped my shaft with her fingers, smiling."
        a "You're so hard down there... I love it."
        scene v3_alison4
        with long
        "She then got on her knees and my heart skipped a beat, seeing what was about to come."
        "Her lips brushed the tip of my cock while her hand stroked the shaft slowly."
        i "Mhh, Alison..."
        "She teased me, jerking me off without haste, playing with her lips."
        "She was taking her time, like she enjoyed having me shivering, at the end of my wits."
        play sound "sfx/bj1.mp3"
        "She finally used her tongue, and its wet contact with my sex made me groan."
        i "Ohhh..."
        a "I'd swear you're even harder than last time..."
        i "That's the effect you have on me..."
        "She was turning me on so much...! I felt I could cum in no time if she kept that up..."
        menu:
            "{image=icon_lust.png}Ask for a boob job" if ian_lust > 1:
                $ renpy.block_rollback()
                $ v3_alison_boobjob = True
                "I looked at Alison, on her knees before me, her naked and exuberant bust under my cock..."
                "I wanted to feel them... If I was to cum, I wanted it to happen between those wonderful tits."
                "And I was so horny I couldn't restrain myself from asking."
                i "Alison... I want you to use your boobs."
                a "Oh! Naughty boy..."
                scene v3_alison5_animation
                with long
                a "So you're the kind of guy who likes this stuff, huh?"
                "She granted my request with a lustful smile on her face."
                "We found the right position and I rested my cock on her chest."
                "She then squeezed her boobs together, sandwiching my manhood between them."
                "A dream come true...!"
                "I began moving my hips back and forth as she tried to mimic my movement."
                i "Oh God..."
                "The excitement was growing more and more, taking hold of my reason. So did the pleasure."
                i "Alison, this is great..."
                a "I can see you're enjoying it... Don't tell me you'll cum from this!"
                i "I very well might..."
                "I thought she would tell me to hold back, but she did the opposite."
                scene v3_alison6_animation
                with long
                a "Do it! Cum for me, Ian!"
                "She held her mouth open, like she was begging for it."
                i "Fuck!"
                "There was no way I could hold it in seeing her like that!"
                "I took hold of my dick and began jerking off myself. I was so close to the finish line, and it was time to cross it."
                a "Yes, I can see you're almost there...!"
                i "Alison...! Uhhh!"
                play sound "sfx/bj4.mp3"
                scene v3_alison6
                show v3_alison6cum1
                with flash
                with vpunch
                a "Oh, yes!"
                i "Mhhhh!!"
                "I clenched my teeth trying not to moan aloud, struck by climax."
                scene v3_alison6
                show v3_alison6cum2
                with short
                "I trembled as I shot all my load over Alison's welcoming body."
                "My jizz hit the mark, splashing her tongue and chin, then dripping down her chest."
                "My mind went blank for a few seconds, and as pleasure died down I recovered my senses."
                "I couldn't believe what I just did. I really came all over Alison..."
                "And she seemed to love it."
                $ fian = "shy"
                $ falison = "slut"
                scene ianroomnight
                show iannude at lef
                show alisonnude at rig
                show alison_cum1 at rig
                show alison_cum2 at rig
                with long
                a "Oh my! You came a lot!"
                i "Oh, wow... That was... Amazing."
                a "I knew I could make you cum... I guess all of this is what you had saved up from last time!"
                $ fian = "smile"
                i "I wasn't expecting to cum so fast, especially after how hard it was last time..."
                i "But you just turned me on so fucking much!"
                a "I'm glad, hee hee... But now the one who's super turned on is me!"
                $ fian = "confident"
                i "Let me return the favor, then!"
                
            "Return the favor":
                $ renpy.block_rollback()
                "I wanted to make this last. And she deserved me to return the favor."
                i "Come here."
                "I picked her up and drove her to the bed."
                
            "Fuck her!":
                $ renpy.block_rollback()
                "I couldn't wait to stick it inside of her again!"
                i "I want you, Alison!"
                scene ianroomnight
                with long
                "I picked her up and drove her to the bed."
                a "Oh, such passion!"
                "I put on a condom as fast as I could."
                jump v3alisonsexfuck
        
    else:
        scene v2_alison3
        with long
        "Alison reached down and grasped my shaft with her fingers, still kissing me."
        a "You're so hard down there..."
        if v2_alison_home:
            "This time it would work. I was too much into it to be distracted by random thoughts..."
            "I grabbed a condom and gave it to Alison."
            i "Put it on me."
            "She smiled."
            a "Gladly..."
            "Once she finished putting it on I knew everything would go as it should."
        else:
            i "How could I not be? You're so sexy..."
            a "Do you have a condom?"
            i "Sure..."
            $ fian = "worried"
            $ falison = "slut"
            scene ianroomnight
            show iannude at lef
            show alisonnude at rig
            with long
            "I searched in the drawer and took out a condom, cracked it open and put it on my cock."
            "I felt my erection die down a bit. The break to put on the rubber often had that effect on me..."
            "I knew how to pump blood to my cock again, though."
        if v2_alison_home == False or v2_ian_limp:
            scene v2_alison4
            with long
            i "Come here."
            "I made Alison sit down on my bed as I continued to make out with her."
            "Slowly, I ran my hand down her chest and her abdomen, reaching down between her legs..."
            play sound "sfx/mh1.mp3"
            a "Mhh... Oh..."
            "I slid the tips of my fingers very lightly over Alison's sex, making her shiver a bit."
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
        
    if v3_alison_boobjob == False:
        scene v3_alison2
        with long
        "I kissed her on the lips and began descending, smooching her neck, her collarbone, her chest..."
        "My lips and tongue caressed her skin until I reached her boobs, her nipples..."
        play sound "sfx/mh1.mp3"
        "She moaned when I teased them, brushing my lips subtly, making them get progressively hard."
        "I slid my tongue over them, pressing down, making circles, and feeling how Alison's breathing became heavier and heavier."
        "She began swaying her hips, rubbing her legs together."
        "It was obvious she was desiring me to go even lower..."
    $ v3_alison_cunnilingus = True
    $ alison_satisfaction += 1
    scene v3_alison3
    if v3_alison_boobjob:
        show v3_alison3cum
    with long
    if v3_alison_boobjob:
        "I didn't even give her the chance to wipe off the cum on her skin."
    "I ran my hands down Alison's belly, reaching her thighs, and I spread them apart."
    "She looked at me with desire as she opened her legs, helping me get access to her pussy."
    "I slid my tongue across her sex, watching her moan and shiver."
    $ ian_lust_xp += 1
    play sound "sfx/xp.mp3"
    show lust_up
    call screen skillsup
    a "Oh, Ian..."
    "She was dying for me to shove my head between her legs and eat her out, I could tell."
    "I gave her what she wanted."    
    play sound "sfx/ah1.mp3"
    a "Ahhh... Oh, yes..."
    "I tasted the flesh of her sex, warm and moist. Her acrid juices told me how much she was into this."
    "As I began using my tongue, exploring her slit and playing with her clit, Alison moaned and surrendered herself to the sensations I was making her feel."
    "Her hand caressed my hair, inviting me to increase the intensity of the cunnilingus."
    "I kept eating her out, trying to find her most sensitive spots, until she had enough."
    a "Ian, I want you inside of me now! Fuck me!"
    
label v3alisonsexfuck:
    
    scene v3_alison7
    if v3_alison_boobjob:
        show v3_alison7cum
    with long
    if v3_alison_boobjob:
        "After taking this break and devoting myself to Alison's enjoyment, my cock was hard as a rock again, ready to go."
        "I put on a condom without wasting time and got on top of her."
    elif v3_alison_cunnilingus:
        "It was a demand I had no intent of rejecting."
    if ian_alison_sex:
        "Doing it with Alison had been great, and this second time was being even better..."
    else:
        "I was going to do it... I was going to have sex with Alison, for real.."
    "She was looking at me, legs spread apart, inviting..."
    "I pressed my cock into her slit, introducing it into her slowly..."
    "She bit her lip and began rubbing her clit as I penetrated her completely."
    play sound "sfx/mh1.mp3"
    scene v3_alison7_animation
    if v3_alison_boobjob:
        show v3_alison7cum_animation
    a "Mhhh, yeah..."
    if ian_alison_sex:
        "A few days ago I never imagined I would get to have this kind of relationship with Alison, and now I was having sex with her again..."
    elif v2_ian_limp:
        "Finally...! This time I wasn't going to botch it!"
    "I began rocking my hips back and forth, and Alison moaned with a smile on her face."
    "Damn, she was so hot and turned me on so much!"
    if ian_cherry_sex:
        "I had slept with Cherry and just a few days after that I got to do it with Alison... I couldn't believe how lucky I was."
    if alison_jeremy:
        "Then the thought occurred to me: Jeremy had been with Alison just a few days ago."
        "He had been doing to her what I was doing now... Alison had been sharing with him what she was sharing with me at this moment."
        "But that did not matter... She was here with me now."
        "I was the one having sex with her. I was the one she was wanting, the one giving her pleasure..."
        "And I should better give it to her!"
    if ian_alison_sex == False:
        scene v2_alison6b_animation
        with long
        "I pulled her legs up and dove right between them. I felt her slippery pussy giving way to my cock as I pushed it in."
        play sound "sfx/oh1.mp3"
        a "Ian! Oh, yes...!"
        play sound "sfx/xp.mp3"
        show lust_up
        $ ian_lust_xp += 1
        call screen skillsup   
        "She held her own legs up as I began moving my hips back and forth, penetrating her at a lively pace."
        "I kissed her on the mouth, on the neck, on her collarbone..."
        a "Oh, this angle is nice... Keep doing it... Do me, Ian!"
        "I supported all my body weight with my arms as I focused on giving Alison what she was asking for."
        "I wanted her to enjoy this. I wanted her to feel happy that she decided to have sex with me."
        scene v2_alison6b_animation2
        with long
        "I tensed my body, penetrating her with my cock in that angle she seemed to like so much, increasing my speed more and more..."
        "I was straining my body, concentrating on Alison's pleasure instead of mine. At this rate I wouldn't get to cum, but it didn't matter..."
        a "Ohhh, don't stop! Yes, Ian, yes...!"
        play sound "sfx/orgasm1.mp3"
        scene v2_alison6b
        with vpunch
        a "Ohhhh! Yeees!!"
        "Alison moaned and I felt her hips and legs trembling... I had accomplished it!"
        i "*{i}Gasp{/i}*..."
        "I let myself fall next to her, panting and sweating, exhausted as I was."
        
    else:
        scene v3_alison8_animation
        if v3_alison_boobjob:
            show v3_alison7cum_animation
        with long
        "As I gave it to Alison her breasts hypnotically bounced up and down. It was pleasure both for my eyes and body." 
        if v3_alison_boobjob:
            "I had just came a few minutes before though, so there was no way I would cum again."
            "But that wasn't my goal. I was straining my body, concentrating on Alison's pleasure instead of mine."
        else:
            "I was straining my body, concentrating on Alison's pleasure instead of mine. At this rate I wouldn't get to cum, but it didn't matter..."
        "All I wanted was to see her cum again, like the other night."
        "I wanted to show her that that had been no fluke. I was man enough to satisfy her."
        "I increased the pulse of my hips, driving them into her harder."
        "Her fingers also began caressing her pussy faster, her moans and breathing became more intense..."
        if v3_alison_boobjob:
            "Alison's chin and breasts were shiny with my cum while I fucked her."
        "It was so hot seeing her like that... And I could tell she was getting close!"
        "As I put all my energy into my thrusts, sweat beginning to run down my forehead."
        a "Fuck, Ian! Don't stop now!"
        if ian_athletics > 1:
            $ alison_satisfaction += 1
            "I gritted my teeth and tensed my abs to maintain that rhythm. I wouldn't let her down!"
            a "Yes, yes, yes...!"
            play sound "sfx/orgasm1.mp3"
            scene v3_alison8
            if v3_alison_boobjob:
                show v3_alison7cum
            with vpunch
            a "Ian! Ooohhh!!"
            "Her entire body trembled, ravaged by the orgasm. I wondered if Perry would've heard us..."
            "Mission accomplished."
            a "Ohhh..."
            "It took her a few seconds to recover."
        else:
            "I couldn't maintain that rhythm! I was holding my breath and I started getting dizzy..."
            "I had to slow down to catch my breath back. Alison's fingers didn't slow down, though."
            a "Mmmhhh...!"
            "She continued masturbating while I slid my cock in and out at a much slower pace."
            a "Almost there..."
            play sound "sfx/ah1.mp3"
            scene v3_alison8
            if v3_alison_boobjob:
                show v3_alison7cum
            a "Ahhh..."
            "It seems she finally came."
            
    stop music fadeout 2.0
    $ fian = "smile"
    $ falison = "slut"
    scene ianroomnight
    show iannude at lef
    show alisonnude at rig
    if v3_alison_boobjob:
        show alison_cum1 at rig
        show alison_cum2 at rig
    with long
    if ian_alison_sex:
        if alison_satisfaction == 2:
            a "God, that was pretty amazing."            
        else:
            a "Mhhh... That was nice."
        i "I'm glad you liked it."
        if v3_alison_boobjob:
            $ falison = "flirt"
            a "And this time you got to cum, too. Look at the mess you made!"
            hide alison_cum1
            hide alison_cum2
            with short
            "She wiped the jizz off her skin."
            i "That was pretty amazing, yeah."
            $ falison = "n"
            a "Next time it would be cool if we could cum together..."
            "So she was counting on there being a \"next time\"... Nice!"
            i "Maybe next time, then."
        else:
            $ falison = "sad"
            a "You didn't get to cum, though. Again..."
            i "I already told you not to worry about it..."
            a "You don't enjoy it?"
            i "I do, of course I do."
            $ falison = "n"
            a "If you say it, I'll believe you."
        i "Do you want to stay the night again?"
    else:
        a "Mhhh... That was so nice..."
        i "*{i}Whew{/i}*... I'm glad you've enjoyed it."
        $ falison = "n"
        a "What about you? You didn't get to cum yet."
        i "Don't worry about it. Besides, I'm completely beat!"
        i "I couldn't keep going even if I wanted to..."
        a "Alright. I'm dead tired, too..."
        i "Do you want to stay the night perhaps?"
    a "I'd love to, but tomorrow I need to get up early."
    i "I'll call you a taxi then. It's the least I can do."
    "She pinched my cheek."
    a "Aww, so nice. thanks, Ian."
    $ ian_look = 3
    hide iannude
    show ianunder at lef
    hide alisonnude
    show alison at rig
    with short
    "The taxi was around the corner. Alison had just enough time to get dressed and say goodbye."
    if ian_alison_sex:
        "This time she didn't part with just a kiss on the cheek."
        scene ianhomenight_dark
        show v3_alison1
        if alison_sexy:
            show v3_alison1_red
        else:
            show v3_alison1_green
        with long
        "She planted a nice kiss on my lips and lingered a couple of seconds before finally leaving."
    else:
        scene ianhomenight_dark
        show alison at rig
        show ianunder at lef
        with long
        "I walked Alison to the door."
        $ fian = "n"
        "I wasn't sure how to act around her after what had just happened. We really had sex..."
        i "Um... So I guess I'll see you soon?"
        a "Of course."
        "She smiled and pinched my cheek as she used to do."
        "For some reason that just didn't feel right."
        scene ianhomenight_dark
        show v3_alison1
        if alison_sexy:
            show v3_alison1_red
        else:
            show v3_alison1_green
        with long
        "I kissed her goodbye. It seemed like she wasn't expecting it, but kissed me back immediately."
        "After that short, final kiss, she finally left, leaving me to contemplate on what had just happened..."
        scene ianhomenight_dark
        with long
        
    $ v3_alison_sex = True
    if ian_alison_sex == False:
        $ ian_alison_sex = True
    jump v3lenawednesday
    
##LENA WEDNESDAY ####################################################################################################################################################################################################################

label v3lenawednesday:
    stop music fadeout 2.0
    $ ian_active = False
    $ lena_active = True
    $ save_name = "Lena: Chapter Three"
    $ lena_look = 1
    $ flena = "n"
    $ fholly = "n"
    $ ian_look = 3
    $ fian = "smile"
    $ day = "Wednesday"
    scene blackbg
    with long
    show active_lena
    with long
    pause 1.0  
    scene blackbg
    with long
    call screen calendar
    scene cafe
    with long
    show lenawork
    with short
    "I finished checking the cash register and made sure not a single cent was missing. My shift at the café was over and it was time for me to leave."
    if v3_ian_date and v3_alison_date == False:
        "I was meeting Holly and Ian in just a few minutes."
    elif v3_ian_date:
        "I was meeting Holly in just a few minutes."
        $ flena = "sad"
        "Ian had planned to come, too, but he canceled last night..."
        if ian_lena > 2:
            $ ian_lena -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
        "I wondered what he had to do that was that important."
    else:
        "I was meeting Holly in just a few minutes."
    show lenawork at rig
    with move
    show molly at lef
    with short
    l "I'm done! I just checked the register and everything tallies."
    mo "Thanks, Lena! Get changed and be on your way, we'll finish cleaning up."
    l "Thanks, Molly!"
    scene street
    with long
    show lena at rig
    show holly2 at lef
    with short
    "Holly was already waiting for me at the door."
    l "Hi!"
    $ fholly = "shy"
    h "Hello, Lena..."
    l "How was your day?"
    h "Same as usual, I can't complain..."
    if v3_ian_date and v3_alison_date == False:
        show lena at rig3
        show holly2 at truecenter
        with move
        show ian at lef3
        with short
        i "Hello, girls."
        l "Hey Ian! That's all of us. Shall we go?"
    else:
        l "Tell me more while we walk!"
    h "Where do you want to go?"
    l "I feel like taking a stroll in the park. There's a kiosk in there that sells popcorn and I fancy some!"
    $ fholly = "n"
    if v3_ian_date and v3_alison_date == False:
        i "Sounds good! Let's go."
    else:
        h "Oh, that sounds nice. Let's go."
    play music "music/date.mp3" loop
    scene park
    with long
    "The park was nearby."
    "It was by far the biggest green area in the city and had beautiful views of the river."
    "It was pretty quiet and a nice place to relax, except on weekends, where a lot of people practiced all kinds of sports, from running to rowing boats down the river."
        
## IAN + HOLLY ##########

    if v3_ian_date and v3_alison_date == False:
        show ian at lef3
        show holly3
        show lena2 at rig3
        with short
        h "I've always liked this park... Sometimes I came here to wander when I needed to think about ideas for my book."
        l "Yes, it's a really nice place... I haven't spent too much time here, though, since I used to live in the outskirts."
        i "So you didn't grow up in the city?"
        l "No, in a small town a couple of hours away. That's where my parents always lived."
        l "I moved to the big city after quitting college, two years ago, to find a job."
        h "You quit college?"
        l "Yeah, I had to..."
        "I told them about my family's situation and my father's health."
        $ fian = "worried"
        $ fholly = "sad"
        i "I had no idea..."
        l "It's not something fun to go telling people! But I'm fine, and my father's fine, don't worry about it."
        h "I'm glad he's getting better. My grandfather died from cancer... I know how hard it can get."
        $ flena = "sad"
        l "Oh... I'm sorry about that..."
        $ fholly = "blush"
        h "But that was long ago! I'm sorry, I'm talking about depressing things and I'm ruining the mood."
        $ fian = "smile"
        i "Don't be sorry! We're just sharing stuff, sometimes it's good and sometimes it's bad... That's life."
        $ flena = "n"
        "Ian was a nice guy. He knew how awkward and shy Holly was and was trying to make her feel at ease."
        "I liked that about him."
        l "Exactly! You can talk about anything you want, Holly. We'll be happy to listen."
        $ fholly = "n"
        h "OK..."
        if ian_honest_review or ian_switch_review:
            l "That reminds me, Ian, Holly told me you had a fight with your boss at the magazine..."
            $ fian = "serious"
            i "Oh, yeah."
            "He told me what had happened with his book review, and how Holly had helped him."
            if ian_honest_review:
                $ flena = "surprise"
                l "That was a very bold move! No wonder your boss got so mad!"
                i "What was I to do? I had tried everything to please her... I was so fed up."
                $ fian = "sad"
                i "It got me into trouble though, that's true. Minerva's halved my working hours, and my paycheck."
            if ian_switch_review:
                l "That was a very clever strategy! Sad to hear it didn't get you anywhere..."
                $ fian = "sad"
                i "It did. Minerva's halved my working hours, and my paycheck."
            $ flena = "worried"
            $ fholly = "sad"
            l "Oh, no!"
            h "That's horrible..."
            i "What's horrible is having to work under her... At least I'll have some more free time now."
            if lena_robert_sex_early or lena_robert_sex_late:
                "My job at the restaurant had been in jeopardy too, but thanks to Robert I didn't have to suffer a situation similar to Ian's."
            else:
                "I had troubles with my job, too, but I didn't want to bring that up."
                "I still didn't know what to do about it, but I didn't want to think about it at that moment."
        $ fian = "n"
        $ flena = "smile"
        l "So, Holly! You were supposed to tell me about your books!"
        $ fholly = "shy"
        h "Oh, that's true..."
        l "I hope you don't mind me turning into a fangirl and asking you a few questions, ha ha."
        $ fholly = "smile"
        h "Of course not..."
        i "I'd love to listen, too. Though I don't want to hear spoilers..."
        $ flena = "happy"
        l "You haven't read Holly's books? Such a friend you are, ha ha!"
        i "I didn't get the chance yet, but Holly said she'd give me one so I can read it!"
        l "You're such a freeloader!"
        $ fian = "happy"
        i "Hey, I won't turn down such a generous gift! That would be rude."
        h "I can give some to you, too, Lena. I have plenty of copies at home."
        l "I already bought them, like a good reader should! But I'd love you to sign them for me!"
        h "Of course."
        $ fian = "smile"
        $ flena = "smile"
        l "So, how does it feel to be a successful writer? You must feel so proud of yourself!"
        $ fholly = "blush"
        h "You guys keep asking me that..."
        h "Most people tell me I should feel like that, but I don't know, I'm afraid I don't..."
        $ fian = "worried"
        $ flena = "sad"
        i "Why not? You have plenty of reasons..."
        menu:
            "{image=icon_wits.png}Only you can decide how to feel" if lena_wits > 1:
                $ renpy.block_rollback()
                $ encourage_holly = 2
                $ flena = "n"
                l "Only you should decide how to feel, Holly. No matter what other people say."
                l "You don't have to believe us if you don't want to... But then don't believe the negative stuff other people said."
                h "Uh, well..."
                l "I have the feeling people have put you down in the past and that's why you don't feel good enough..."
                l "But regardless of that, look at what you accomplished and think if you're happy you did."
                l "Because you did it, nobody else."
                play sound "sfx/friendup.mp3"
                show friend_up
                $ lena_holly += 2
                $ fholly = "shy"
                $ fian = "smile"
                h "Thanks, Lena..."
                "Ian looked at me and smiled, pleased with how I managed things. I winked at him in complicity."
                h "But you're right, I'm used to people putting me down..."     
            
            "Ian's right":
                $ renpy.block_rollback()
                $ flena = "n"
                l "Ian's right, you know? You should be happy!"
                l "You managed to create stories and characters that people really love!"
                h "I feel the merit is on the book itself, not on me..."
                i "But you wrote those books..."
                h "Maybe, but I'm nothing like the characters in them... They are brave and special. They have friends and people who value them..."
                $ flena = "sad"
                l "And you don't?"
                h "Well..."
                
            "Sometimes it's complicated":
                $ renpy.block_rollback()
                if encourage_holly < 2:
                    $ encourage_holly += 1
                l "Sometimes things are more complicated than just that..."
                l "Even though people tell you you should feel good about something, if you don't love it you just can't..."
                i "You don't love writing?"
                h "Yes, I do... Of course I do. But..."
                l "But probably someone made you believe you as a person weren't good enough. Even if what you write is great..."
                $ fholly = "blush"
                h "Well, that's, um..."
                $ flena = "n"
                l "You don't have to listen to people when they say you should feel good. But don't listen to them when they say you should feel bad!"
                play sound "sfx/friendup.mp3"
                show friend_up
                $ lena_holly += 1
                h "That makes sense... But it's complicated."

        $ fian = "n"
        $ flena = "sad"
        $ fholly = "n"
        h "I've never been too popular... Especially during high school."
        h "No, in fact, I think I didn't have any real friends even when I was a kid..."
        i "I understand that feeling. I was never too popular either, and spent most of my time alone, living in the fantasy worlds I created for myself."
        h "Yes, that's right..."
        $ flena = "n"
        l "Is that so? You told me you were in a rock band..."
        $ fian = "smile"
        i "Yeah, but we never were the cool kids, not at all!"
        i "We were a group of misfits that happened to be lucky enough to meet each other at the right time."
        i "If it weren't for them, I would've felt all alone during my high school years." 
        $ fholly = "n"
        hide holly3
        show holly2 
        with short
        h "Yeah... The school I went to, well... I couldn't really find kids who liked the same things I did."
        l "We all had a hard time in school... During those years you're trapped in there, and it seems the world is so small... It can feel like a jail."
        i "That's pretty well put."
        $ flena = "smile"
        l "But now we're out of that jail! We're free to find who we want to spend our time with."
        l "And right now I'd say we're spending time with the best people possible, don't you agree?"
        $ fian = "happy"
        $ fholly = "shy"
        h "Y-{w=0.3}yes."
        i "You two are really cool people in my book."
        l "Oh look, there's that kiosk! Let's grab some popcorn!"
        $ fian = "smile"
        $ fholly = "smile"
        $ flena = "smile"       
        "We sat down on a bench facing the river to eat our popcorn."
        if v2_showlena_jeremy:
            l "Oh, Ian, I met this guy who's supposed to be a friend of yours..."
            $ fian = "n"
            i "Jeremy, yeah. He told me. He's seeing your flatmate, huh?"
            l "Yes, she's his girlfriend."
            $ fian = "worried"
            i "His girlfriend?"
            l "Yes."
            i "Uh, I see..."
            $ fian = "smile"
        "We talked animatedly about many things, from day to day stuff to pop culture or even art History."
        "Both Ian and Holly had keen minds and an eye for art, and I also thought they shared many sensibilities."
        "Holly was visibly shy and a scaredy-cat, afraid of the world but in need of a big, warm hug."
        "Ian, in comparison, was a pretty forthcoming guy. But I could see something in him, something I had seen from the very first time, when watching him write at the café."
        "That insecurity that spills from a wounded heart, an insecurity he always tried his very best to hide."
        "But my eyes saw."
        scene park
        with long
        scene parknight
        with long
        "We sat there talking until night came, hiding the sun and making the lamps light the park in a warm, orange light."
        show ian at lef3
        show holly2
        show lena2 at rig3
        with short
        if book_scifi:
            if book_card1 == "vengeance":
                "Ian and Holly were just talking about writing, discussing if vengeance was the most appropriate call to adventure in a sci-fi novel."
                h "Vengeance always works!"
                i "I had that feeling, ha ha."
                i "I was thinking about making the protagonist trying to find retribution for the loss of his ancestral lineage to a corrupt mega-corporation..."
            if book_card1 == "call_of_duty":
                "Ian and Holly were just talking about writing, discussing if duty to a cause was the most appropriate call to adventure in a sci-fi novel."
                h "Yes, it could work. But you'd have to create some interesting political organization to justify that call to arms..."
                i "Yeah, I was thinking about the protagonist serving a totalitarian space regime, so he'd be fulfilling the duty of the bad guys so to speak..."
            if book_card1 == "chosen_one":
                "Ian and Holly were just talking about writing, discussing if having a character be the Chosen One made sense in a sci-fi novel."
                i "I was thinking about making the protagonist discover that he lives in a completely deterministic universe, so his choices were made for him beforehand..."
                i "That way he was \"destined\" by physical causality, making him a paradoxical Chosen One..."
                h "Wow, that's genius! I love that idea! I haven't read that before, and I have read a lot..."
                i "Really? That's... great!"
        if book_historical:
            if book_card1 == "vengeance":
                "Ian and Holly were just talking about writing, discussing if vengeance was the most appropriate call to adventure in a Historical novel."
                i "There a lot of interesting feuds in real life, countries, families and individuals even whose animosity drove History forward..."
                h "I guess it can work, but you'll need to make it so that it's not too generic."
            if book_card1 == "call_of_duty":
                "Ian and Holly were just talking about writing, discussing if duty to a cause was the most appropriate call to adventure in a Historical novel."
                h "Yes, I'd say it fits that genre perfectly!"
                i "Seems like people back then were a lot more willing to die for a cause, for something bigger than themselves. For History itself."
            if book_card1 == "chosen_one":
                "Ian and Holly were just talking about writing, discussing if having a character be the Chosen One made sense in a Historical novel."
                h "It's a bit weird, isn't it?"
                i "Yeah, but you can argue he was chosen by History itself to make those things happen..."
        if book_fantasy:
            if book_card1 == "vengeance":
                "Ian and Holly were just talking about writing, discussing if vengeance was the most appropriate call to adventure in a fantasy novel."
                h "Vengeance always works!"
                i "I had that feeling, ha ha."
                i "The main characters are a dwarf who has a vengeance against the world and who has sworn an oath of death, and his human sidekick, who's a poet who has sworn to write the epic tale of the dwarf's death..."
                h "That's the perfect set-up for a series of grim and thrilling fantasy novels!"
            if book_card1 == "call_of_duty":
                "Ian and Holly were just talking about writing, discussing if duty to a cause was the most appropriate call to adventure in a fantasy novel."
                h "Yes, it could work. But you'd have to create some interesting worldbuilding to justify that call to arms..."
                i "Yeah, I was thinking about setting the story in a world were ancient cultures have grown into very different kingdoms who fight to create their own vision of God..."
            if book_card1 == "chosen_one":
                "Ian and Holly were just talking about writing, discussing if having a character be the Chosen One made sense in a fantasy novel."
                h "That's been done a million times already... It's pretty bland at this point."
                $ fian = "worried"
                i "I see... so I made it way too {i}cliché{/i}, didn't I?"
                h "Yeah..."
                $ fian = "smile"
        l "You sound really enthusiastic about your book, Ian."
        i "That's because I am... I know it's a very hard dream to achieve, but it's what I want to do."
        i "A life without that would just be nonsense."
        $ flena = "blush"
        $ fholly = "flirt"
        l "Oh..."
        h "..."
        $ fian = "worried"
        i "What? Did I say something weird?"
        $ flena = "shy"
        $ fholly = "blush"
        "Again, he was so clueless sometimes! But so genuine because of it."
        l "No, I just liked the passion that's in your words. You make me able to feel how much you really love writing."
        $ fian = "blush"
        i "Oh, I see..."
        "Judging by Holly's reaction, I was pretty sure she saw things the same way as I did..."
        "Below Ian's insecurities I could see the shine of a really passionate heart. And those are the best hearts."
        $ fian = "smile"
        i "What about you, Lena? What are you passionate about?"
        $ fholly = "smile"
        l "Me? Oh..."
        menu:
            "Writing songs":
                $ renpy.block_rollback()
                $ lena_passion = "song"
                $ flena = "smile"
                l "I'd say writing songs is what I'm most passionate about."
                i "Yeah, you told me about that... For you the most important part of a song are the lyrics, right?"
                l "The music is important, of course, but what really speaks to me are the lyrics..."
                h "It's no different than poetry. In fact, ancient poets believed poetry had to be sung, not spoken."
                play sound "sfx/xp.mp3"
                show wits_up
                $ lena_wits_xp += 1
                call screen skillsup
                l "It seems I'm from the same school of thought, then."
                
            "Enjoying life":
                $ renpy.block_rollback()
                $ lena_passion = "life"
                $ flena = "happy"
                "I'd say I enjoy life in many ways, different experiences and all kinds of activities..." 
                play sound "sfx/xp.mp3"
                show charisma_up
                $ lena_charisma_xp += 1
                call screen skillsup
                l "I just like being alive!"
                h "That's a great attitude..."
                i "And one of those things you enjoy is writing songs, right?"
                l "Oh, yeah, but it's more like a hobby... I don't know if I could call it a passion..."
                                            
            "Modeling":
                $ renpy.block_rollback()
                $ lena_passion = "model"
                $ flena = "smile"
                l "I'm really into modeling lately." 
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
                l "I'm still discovering that world, but I enjoy it."
                h "I see... That's something I could never do. I'd be too ashamed."
                i "Me too. Not that anybody would want to see me posing, ha ha."
                l "You need to be comfortable in your own skin, that's for sure. But if you are it's a pretty empowering experience, and an enjoyable sensation, too."
                l "To me, at least."
                i "And what about writing songs? You told me you loved it..."                
                l "Oh, yeah, but it's more like a hobby... I don't know if I could call it a passion..."
                
            "Making money":
                $ renpy.block_rollback()
                $ lena_passion = "money"
                $ lena_posh = 2
                $ flena = "evil"
                l "My passion would be making loads of money."
                $ fian = "worried"
                $ fholly = "sad"
                i "Really? I would've never guessed that was the case..."
                $ flena = "n"
                l "It was a joke, more or less..."
                l "It's true that I would love to have more money, but only because I don't have much..."
                l "I would like to earn enough to at least live a comfortable life without having to worry so much about working."
                $ fian = "smile"
                $ fholly = "n"
                i "That's something everyone can say they wish for, I guess."
                i "I'd love to be able to just concentrate on writing without worrying about paying the bills..."
                h "Hopefully you can turn your passion into a job and earn money doing what you love!"
                i "That's the dream, isn't it?"
                l "I guess so!"
                i "And what would that be for you, Lena? Writing songs?"
                l "Oh, I see that more as a hobby... I don't know if I could call it a passion, or even make a living out of it."
                
        if v2_holly_song:
            h "Oh, yeah, speaking about that...! You said you'd show me one of your songs."
            $ flena = "shy"
            l "That's true..."
            i "I'd love to listen to it, too!"
            l "Oh, geez, you two are way too interested... It makes me shy!"
            i "Oh, come on! You're a very confident girl, you can't be shy about this and not about posing!"
            l "Well, this feels more personal... But alright, I'll share it with you."
            $ flena = "smile"
            l "Do you guys want to drop by my place so I can show you real quick? I live close by."
            h "Oh, OK."
            l "Let's go then."
            jump v3hollysong

        else:
            h "It's getting late... I should make my way home. My parents don't like it when I'm too late."
            l "Sure. We can get going."
            $ flena = "happy"
            l "It's been a wonderful afternoon. Thank you, guys."
            $ fholly = "shy"
            h "No, thank you..."
            i "I had a lot of fun talking to you girls. Let's meet again sometime, just the three of us."
            l "That would be cool."
            if v2_kiss:
                $ fian = "shy"
                $ flena = "flirtshy"
                "Ian and I looked at each other and it felt like we could read each other's mind for a split second."
                "It was weird that we hadn't kissed once during the whole time... And now it was the perfect moment."
                "But with Holly present, none of us felt it was appropriate... So we held it in."            
            l "See you!"
            scene parknight
            with long
            stop music fadeout 2.0
            "We all said goodbye and went back to our homes."
            jump v3louisesong

## JUST HOLLY ##########

    else:
        $ v3_ian_date = False
        show holly3 at lef
        show lena2 at rig
        with short
        h "I've always liked this park... Sometimes I came here to wander when I needed to think about ideas for my book."
        l "Yes, it's a really nice place... I haven't spent too much time here, though, since I used to live in the outskirts."
        h "So you didn't grow up in the city?"
        l "No, in a small town a couple of hours away. That's where my parents always lived."
        l "I moved to the big city after quitting college, two years ago, to find a job."
        h "You quit college?"
        l "Yeah, I had to..."
        "I told Holly about my family's situation and my father's health."
        $ fholly = "sad"
        h "Oh, I had no idea... I'm sorry to hear that..."
        "I could tell she really meant it. She was so kind."
        l "I'm fine, and my father's fine, don't worry about it."
        h "I'm glad he's getting better. My grandfather died from cancer... I know how hard it can get."
        $ flena = "sad"
        l "Oh... I'm sorry about that..."
        $ fholly = "blush"
        h "But that was long ago! I'm sorry, I'm talking about depressing things and I'm ruining the mood."
        $ flena = "n"
        i "Hey, don't be sorry! We're just sharing. And friends do not share only the good, but the bad, too."
        l "You can talk about anything you want, Holly. I'll be happy to listen."
        h "Thank you... I'd love to do the same for you..."
        $ flena = "smile"
        l "So, Holly! You were supposed to tell me about your books!"
        $ fholly = "shy"
        h "Oh, that's true..."
        l "I hope you don't mind me turning into a fangirl and asking you a few questions, ha ha."
        $ fholly = "smile"
        h "Of course not..."
        $ flena = "sad"
        l "Oh, silly me! I forgot to bring them today!"
        l "I wanted to ask you to sign them for me!"
        $ fholly = "happyshy"
        h "Don't worry, I'll do it next time."
        $ fholly = "n"
        h "Though I never understood why people want my signature..."
        $ flena = "n"
        l "Why not? You never wanted a writer you admire to sign your books?"
        h "I guess... But I kinda see the author and his work like two separate things."
        l "What do you mean?"
        h "Some people seem to really like my books... But what they love is the world within those pages."
        $ fholly = "sad"
        h "They like the characters and their stories. And they have nothing to do with me..."
        $ flena = "sad"
        h "They are heroic and brave, they have powers, they fight and they are special... I'm nothing like that at all..."
        menu:
            "{image=icon_wits.png}Those characters are part of you" if lena_wits > 1:
                $ renpy.block_rollback()
                $ encourage_holly = 2
                $ flena = "smile"
                l "But Holly, you wrote those characters. You came up with those adventures."
                l "They live and play out inside of you, so I'd say those characters are part of you."
                l "If you were different from who you are you wouldn't be able to write those stories and characters people love!"
                l "Maybe you're not a fantasy hero, but you're special in your own way, and a great writer!"
                l "It's just natural for people to admire not just your work, but you yourself, and to want your signature."
                $ fholly = "shy"
                h "Stop it, you're making me blush..."
                l "But it's true."
                play sound "sfx/friendup.mp3"
                show friend_up
                $ lena_holly += 2
                $ fholly = "happyshy"
                h "Thank you, Lena."
                
            "Fantasy is different from the real world":
                $ renpy.block_rollback()
                $ flena = "n"
                l "Fantasy is different from the real world. Nobody is like that in real life."
                l "That doesn't mean you're less valuable! You write those stories and create something people can enjoy!"
                l "That's enough for someone to want your signature."
                $ fholly = "n"
                h "I guess..."
            
            "That shows you're a good writer":
                $ renpy.block_rollback()
                if encourage_holly < 2:
                    $ encourage_holly += 1
                $ flena = "smile"
                l "That just shows how good of a writer you are!"
                l "You can imagine and create cool characters and amazing stories that people can enjoy. Nobody's asking you to be a hero..."
                l "You're great at what you do, and that is writing. It's normal people want your signature."
                $ fholly = "n"
                play sound "sfx/friendup.mp3"
                show friend_up
                $ lena_holly += 1
                h "I guess you're right..."
        
        $ flena = "happy"
        l "Oh look, there's that kiosk! Let's grab some popcorn!"
        h "Alright."
        $ fholly = "n"
        $ flena = "smile"       
        "We sat down on a bench facing the river to eat our popcorn."
        l "So I take it you had a hard time at high school?"
        $ fholly = "sad"
        h "Um, yeah... I didn't have too many friends during that time."
        h "No, in fact, I think I didn't have any real friends even when I was a kid... But I don't want to bore you with that..."
        menu:
            "Please, tell me":
                $ renpy.block_rollback()
                l "Please, go ahead, tell me."
                h "I had this friend when I was a kid... She was a couple of years older than me, but we played together and got along really well."
                h "My mom always said I got on easier with people older than me, and I guess that's true, since I never got along too much with kids in my class."
                h "But at some point, when I started high school, she turned her back on me."
                $ flena = "sad"
                l "What happened?"
                h "She started hanging out with the cool girls in her class, and they didn't like me. I was a kid to them, and a nerdy one at that."
                l "And she threw you under the bus to fit in with them, right?"
                h "Yeah... She began avoiding me and they told me she said nasty things about me behind my back."
                h "I've had other friends since, but she was the closest one I ever had... And it didn't end well."
                l "She acted like a bitch... But that's pretty common during high school years, sadly."
                l "People are trying to fit in somewhere. The cowardly ones sell themselves to be part of a group."
                $ flena = "n"
                l "It's the brave ones who keep true to themselves, even if that means they are left alone."
                l "Besides, people change! You're not the girl you were in high school! You've grown and you can make new friends now."
                $ fholly = "happyshy"
                play sound "sfx/friendup.mp3"
                show friend_up
                $ lena_holly += 1
                h "I'm trying."
                
            "OK, let's change the subject":
                $ renpy.block_rollback()
                l "Alright, let's change the subject. I don't want to make you speak of things you'd rather not."
                $ fholly = "n"
        
        "We continued to talk about many things, from day to day stuff to pop culture or even art History."
        "Holly had a keen mind and great sensibility, but I also knew that from reading her books."
        "She was also so obviously shy and a scaredy-cat, afraid of the world but in need of a big, warm hug. And she was deserving on one."
        "She awakened the tender and protective instincts in me."
        scene park
        with long
        scene parknight
        with long
        "We sat there talking until night came, hiding the sun and making the lamps light the park in a warm, orange light."
        $ fholly = "smile"
        $ flena = "smile"
        show holly2 at lef
        show lena2 at rig
        with short
        "I had convinced Holly to tell me about her upcoming book, the one she was finishing and that would be published in the following months."
        l "I see, that's so cool... I didn't expect that love triangle to be resolved like that..."
        l "Ah, but I'm spoiling myself! When I read the book I will know what happens!"
        l "Though getting told the story by the author is pretty awesome, too, and I can't contain my curiosity!"
        $ fholly = "happy"
        h "Ha ha ha. It's a loaded choice either way."
        "Holly's laughter was so cute and joyous."
        h "It's funny seeing someone being so passionate about something I'm creating... I never shared a moment like this before."
        l "No? Not even with one of your fans?"
        h "No, that's different... They tell me what they like about the books and ask me about the next one..."
        h "But this is different, we're just talking so freely... I could never really tell any of them what I'm telling you now."
        h "That's why you must promise me you won't leak any of this info!"
        l "You have my word! Unless someone pays me a lot to reveal the information..."
        l "In that case, I'm totally not crossing my fingers behind my back right now!"
        h "Ha ha, silly..."
        $ fholly = "smile"
        h "What about you, Lena? What would you say you're passionate about?"
        l "Me? Oh..."
        menu:
            "Writing songs":
                $ renpy.block_rollback()
                $ lena_passion = "song"
                $ flena = "smile"
                l "I'd say writing songs is what I'm most passionate about."
                h "You prefer lyrics over music?"
                l "The music is important, of course, but what really speaks to me are the lyrics..."
                h "It's no different than poetry. In fact, ancient poets believed poetry had to be sung, not spoken."
                play sound "sfx/xp.mp3"
                show wits_up
                $ lena_wits_xp += 1
                call screen skillsup
                l "It seems I'm from the same school of thought, then."
                
            "Enjoying life":
                $ renpy.block_rollback()
                $ lena_passion = "life"
                $ flena = "happy"
                "I'd say I enjoy life in many ways, different experiences and all kinds of activities..." 
                play sound "sfx/xp.mp3"
                show charisma_up
                $ lena_charisma_xp += 1
                call screen skillsup
                l "I just like being alive!"
                h "That's a great attitude... I should be more like that..."
                h "What about writing songs, though?"
                l "Oh, yeah, but it's more like a hobby... I don't know if I could call it a passion..."
                                            
            "Modeling":
                $ renpy.block_rollback()
                $ lena_passion = "model"
                $ flena = "smile"
                l "I'm really into modeling lately." 
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
                l "I'm still discovering that world, but I enjoy it."
                h "I see... That's something I could never do. I'd be too ashamed."
                l "You need to be comfortable in your own skin, that's for sure. But if you are it's a pretty empowering experience, and an enjoyable sensation, too."
                l "To me, at least."
                h "I can't imagine myself in that scenario at all. I would do horribly..."
                h "What about writing songs, though?"            
                l "Oh, yeah, but it's more like a hobby... I don't know if I could call it a passion..."
                
            "Making money":
                $ renpy.block_rollback()
                $ lena_passion = "money"
                $ lena_posh = 2
                $ flena = "evil"
                l "My passion would be making loads of money."
                $ fholly = "sad"
                h "Oh, is that so...? I would've never guessed that was the case..."
                $ flena = "n"
                l "It was a joke, more or less..."
                l "It's true that I would love to have more money, but only because I don't have much..."
                l "I would like to earn enough to at least live a comfortable life without having to worry so much about working."
                $ fholly = "n"
                h "That's something everyone can say they wish for, I guess."
                l "Hopefully I can turn my passion into a job and earn money doing what I love, just like you do, Holly!"
                h "And what would that be for you, Lena? Writing songs?"
                l "Oh, I see that more as a hobby... I don't know if I could call it a passion, or even make a living out of it."
                
        if v2_holly_song:
            h "Oh, yeah, speaking about that...! You said you'd show me one of your songs."
            $ flena = "shy"
            l "That's true..."
            $ flena = "smile"
            l "Say, do you want to drop by my place so I can show you real quick? I live close by."
            h "Oh, OK."
            l "Let's go then."
            jump v3hollysong

        else:
            h "It's getting late... I should make my way home. My parents don't like it when I'm too late."
            l "Sure. We can get going."
            $ flena = "happy"
            l "It's been a wonderful afternoon. Thank you, Holly."
            $ fholly = "shy"
            hide holly2
            show holly3 at lef
            with short
            h "No, thank you... I had a lot of fun talking to you. I'd love to meet with you some other time..."
            l "Yes, let's do that."
            l "See you!"
            scene parknight
            with long
            stop music fadeout 2.0
            "We said goodbye and went back to our homes."
            jump v3louisesong        
 
 
## SHOW SONG ####################################################################################################################################################################

##HOLLY 
label v3hollysong:
    stop music fadeout 2.0
    if v3_ian_date:
        scene lenahomenight
        with long
        $ flena = "shy"
        $ fian = "smile"
        $ folly = "smile"
        play sound "sfx/door_home.mp3"
        show ian at lef3
        show holly2
        show lena2 at rig3
        with short
        l "So, this is my place..."
        i "It's pretty nice."
        l "I'm sharing with two other people and I didn't tell them I would bring people over tonight..."
        l "Let's go to my room so we don't disturb them."
        play sound "sfx/door.mp3"
        scene lenaroomnight
        show ian at lef3
        show holly2
        show lena2 at rig3
        with long
        $ flena = "n"
        l "And here's my room! It's small but it's cozy."
        "I kicked a box with stuff that I hadn't unpacked yet to make room for everyone."
        l "It's a bit messy, sorry."
        play sound "sfx/meow.mp3"
        show lola at centerlef
        with short
        $ fholly = "happy"
        h "Oh! So cute!"
        l "And this is my cat, Lola."
        "Holly scratched her head."
        play sound "sfx/purr.mp3"
        hide holly2
        show holly
        show lolahappy at centerlef
        with short
        h "Aww, she's adorable!"
        i "She is, ha ha."
        l "Only when she wants to."
        i "So, are we going to listen to one of your songs?"
        $ flena = "blush"
        l "Hey, I'm nervous, it's no joke."
        h "We'll sit here and be very quiet. Try to imagine we're not even here."
        $ flena = "shy"
        l "That will be difficult..."
    else:
        scene lenahomenight
        with long
        $ flena = "shy"
        $ folly = "shy"
        play sound "sfx/door_home.mp3"
        show holly2 at lef
        show lena2 at rig
        with short
        l "So, this is my place..."
        h "It's nice! thanks for inviting me..."
        l "I'm sharing with two other people and I didn't tell them I would bring people over tonight..."
        l "Let's go to my room so we don't disturb them."
        play sound "sfx/door.mp3"
        scene lenaroomnight
        show holly2 at lef
        show lena2 at rig
        with long
        $ flena = "n"
        l "And here's my room! It's small but it's cozy."
        "I kicked a box with stuff that I hadn't unpacked yet to make room for Holly."
        l "It's a bit messy, sorry."
        play sound "sfx/meow.mp3"
        show lola 
        with short
        $ fholly = "happy"
        h "Oh! So cute!"
        l "And this is my cat, Lola."
        "Holly scratched her head."
        play sound "sfx/purr.mp3"
        hide holly2
        show holly at lef
        show lolahappy 
        with short
        h "Aww, she's adorable!"
        "Holly returned her attention back to me."
        h "I'm so excited to listen to your song."
        $ flena = "blush"
        l "Don't be... That just makes me more nervous!"
        l "I just do it as a hobby, please don't expect anything too great..."
        h "I know showing your art can be nerve-wracking, especially live..."
        h "I'll sit here and be very quiet. Try to imagine I'm not even here."
        $ flena = "shy"
        l "That will be difficult..."
        
    scene lenaroomnight
    show lena_guitar1
    with long
    "I picked up my guitar and sat on the bed next to Holly."
    if v3_ian_date:
        "Ian took a seat on the desk chair."
    "I took a deep breath and tried to relax, concentrating on the song."
    l "OK, here I go."
    play music "music/lenas_theme.mp3"
    "I began playing a sad melody, my fingers softly strumming the guitar."
    l "It's called \"Broken Dreams\"."
    "I eased myself into the music and began singing."
    l "{i}So vast and dark, this cosmic field of dreams we live in...{/i}"
    if song_1a == "real":
        l "{i}With our child-like hands, reaching out, trying to grasp something real.{/i}"
    if song_1a == "precise":
        l "{i}With our child-like hands, reaching out, trying to grasp something precise.{/i}"
    if song_1a == "cool":
        l "{i}With our child-like hands, reaching out, trying to grasp something cool.{/i}"
    l "{i}Like two moons on a collision course, this is our gravity...{/i}"
    if song_1b == "tragedy":
        l "{i}Like a star that burns out too quick, this is our tragedy.{/i}"
    if song_1b == "story":
        l "{i}Like a star that burns out too quick, this is our story.{/i}"
    if song_1b == "stuff":
        l "{i}Like a star that burns out too quick, this is our stuff.{/i}"
    l "{i}So bright and terrifying, this cosmic field of dreams where I exist...{/i}"
    if song_1c == "abyss":
        l "{i}Down the rabbit hole, holding your hand. Spiraling into our abyss.{/i}"
    if song_1c == "kingdom":
        l "{i}Down the rabbit hole, holding your hand. Spiraling into our kingdom.{/i}"
    if song_1c == "cave":
        l "{i}Down the rabbit hole, holding your hand. Spiraling into our cave.{/i}"
    l "{i}Like two moons on a collision course, this is our gravity...{/i}"
    if song_1b == "tragedy":
        l "{i}Like a star that burns out too quick, this is our tragedy.{/i}"
    if song_1b == "story":
        l "{i}Like a star that burns out too quick, this is our story.{/i}"
    if song_1b == "stuff":
        l "{i}Like a star that burns out too quick, this is our stuff.{/i}"
    l "{i}Ours, until we burned out.{/i}"
    l "{i}Ours, until we ceased to be...{/i}"
    "The final notes of the song left my fingers and died down on the guitar's strings."
    stop music fadeout 2.0
    if lena_song1 == 6:
        $ fian = "depress"
        $ fholly = "cry"
    else:
        $ fian = "sad"
        $ fholly = "sad"
    scene lenaroomnight
    if v3_ian_date:
        show ian at lef3
        show holly2
        show lena2 at rig3
    else:
        show holly at lef
        show lena at rig
    with long
    l "Well... What did you think about it...?"
    if lena_song1 == 6:
        $ flena = "surprise"
        l "Holly, you're crying?"
        h "It was... really beautiful."
        $ flena = "blush"
        if v3_ian_date:
            i "It moved me, too..."
            l "Guys, now I'm feeling guilty for making you feel bad!"
            $ fholly = "smile"
            $ fian = "smile"
            "Holly wiped her tears and smiled."
            h "No, it was an incredible song, really. Thanks for sharing it with us."
            $ flena = "happy"
            l "I'm surprised to see it had such an effect on you..."
            i "I don't know much about poetry, but I would say it was perfect."
            h "Yes, it was one of the most beautiful songs I've ever heard."
        else:
            l "Now I'm feeling guilty for making you feel bad!"
            $ fholly = "smile"
            "Holly wiped her tears and smiled."
            h "No, it was one of the most beautiful songs I've ever heard. Thanks for sharing it with me."
        call screen willup
        l "Stop it... ha ha."
    elif lena_song1 > 3:
        $ fian = "sad"
        $ holly = "sad"
        h "It was a really beautiful song... But very sad..."
        $ flena = "sad"
        l "Oh, I'm sorry... I didn't want to make you feel bad..."
        if v3_ian_date:
            $ fian = "smile"
            i "That's because it is a very good sad song. I liked it a lot, too."
            $ fholly = "smile"
            h "That's right."
            $ flena = "shy"
            l "Oh, thank you."
        else:
            $ fholly = "smile"
            h "That's because it is a very good sad song."
            $ flena = "shy"
            l "Oh, thank you."
        h "If you want some advice though, there's maybe something you could think about changing..."
        l "What is it?"           
        if song_1a == "cool" or song_1a == "precise":
            h "I'd change the first verse... I think \"real\" is a better suited word."
            if v3_ian_date:
                if song_1b == "stuff" or song_1b == "story":
                    i "And what about using \"tragedy\" for the second verse? I think it's a much more powerful word."
            menu:
                "Change it":
                    $ renpy.block_rollback()
                    $ song_1a = "real"
                    if v3_ian_date:
                        if song_1b == "stuff" or song_1b == "story":
                            $ song_1b = "tragedy"
                    l "I think you're right. That way it sounds much better..."
                    l "Thanks for your advice!"
                    h "Thank you for sharing."
                "Leave it as is":
                    $ renpy.block_rollback()
                    l "I think I'll leave it as it is for now... It is what came out of my mind, after all."
                    h "Sure. You don't have to change anything if you don't want to."
        elif song_1b == "stuff" or song_1b == "story":
            h "I'd change the second verse... I think \"tragedy\" is a much more powerful word."
            if v3_ian_date:
                if song_1c == "cave" or song_1c == "kingdom":
                    i "And what about using \"abyss\" for the third verse? I think it rhymes better."
            menu:
                "Change it":
                    $ renpy.block_rollback()
                    $ song_1b = "tragedy"
                    if v3_ian_date:
                        if song_1c == "cave" or song_1c == "kingdom":
                            $ song_1c = "abyss"
                    l "I think you're right. That way it sounds much better..."
                    l "Thanks for your advice!"
                    h "Thank you for sharing."
                "Leave it as is":
                    $ renpy.block_rollback()
                    l "I think I'll leave it as it is for now... It is what came out of my mind, after all."
                    h "Sure. You don't have to change anything if you don't want to."
        elif song_1c == "cave" or song_1c == "kingdom":
            h "I'd change the third verse... I think \"abyss\" rhymes better."
            menu:
                "Change it":
                    $ renpy.block_rollback()
                    $ song_1c = "abyss"
                    l "I think you're right. That way it sounds much better..."
                    l "Thanks for your advice!"
                    h "Thank you for sharing."
                "Leave it as is":
                    $ renpy.block_rollback()
                    l "I think I'll leave it as it is for now... It is what came out of my mind, after all."
                    h "Sure. You don't have to change anything if you don't want to."    
    else:
        $ fian = "sad"
        $ holly = "sad"
        h "It was beautiful, and sad..."
        if v3_ian_date:
            i "I liked it. It was pretty good..."
        h "I really like the structure, but I don't know if some of those metaphors are the best..."
        l "They aren't? What would you say is the problem?"
        if song_1a == "cool" or song_1a == "precise":
            h "I'd change the first verse... I think \"real\" is a better suited word."
            if v3_ian_date:
                if song_1b == "stuff":
                    i "And what about using \"story\" for the second verse? I think it's better."
            menu:
                "Change it":
                    $ renpy.block_rollback()
                    $ song_1a = "real"
                    if v3_ian_date:
                        if song_1b == "stuff":
                            $ song_1b = "story"
                    l "I think you're right. That way it sounds much better..."
                    l "Thanks for your advice!"
                    h "Thank you for sharing."
                "Leave it as is":
                    $ renpy.block_rollback()
                    l "I think I'll leave it as it is for now... It is what came out of my mind, after all."
                    h "Sure. You don't have to change anything if you don't want to."
                    
        elif song_1b == "stuff" or song_1a == "story":
            h "I'd change the second verse... I think \"tragedy\" is a much more powerful word."
            if v3_ian_date:
                if song_1c == "cave":
                    i "And what about using \"kingdom\" for the third verse? I think it's better."
            menu:
                "Change it":
                    $ renpy.block_rollback()
                    $ song_1b = "tragedy"
                    if v3_ian_date:
                        if song_1c == "cave":
                            $ song_1c = "kingdom"
                    l "I think you're right. That way it sounds much better..."
                    l "Thanks for your advice!"
                    h "Thank you for sharing."
                "Leave it as is":
                    $ renpy.block_rollback()
                    l "I think I'll leave it as it is for now... It is what came out of my mind, after all."
                    h "Sure. You don't have to change anything if you don't want to."
        elif song_1c == "cave" or song_1a == "kingdom":
            h "I'd change the third verse... I think \"abyss\" rhymes better."
            menu:
                "Change it":
                    $ renpy.block_rollback()
                    $ song_1c = "abyss"
                    l "I think you're right. That way it sounds much better..."
                    l "Thanks for your advice!"
                    h "Thank you for sharing."
                "Leave it as is":
                    $ renpy.block_rollback()
                    l "I think I'll leave it as it is for now... It is what came out of my mind, after all."
                    h "Sure. You don't have to change anything if you don't want to."
    
    l "Well, so that was my song."
    if v3_ian_date:
        i "That's the only one you've written?"
        $ flena = "sad"
        l "No, I had several songs that I kinda liked... But I lost the notebooks where I had them written down."
    else:
        $ flena = "sad"
        l "I had several more songs that I kinda liked... But I lost the notebooks where I had them written down."
    h "What happened ot them?"
    l "I left them at my ex-boyfriend's house after breaking up..."
    l "I haven't seen them since. Same as my old guitar."
    $ flena = "smile"
    l "But now I have a brand new one, better than the one I used to have!"
    if v3_ian_date:
        h "It's getting late... I should make my way home. My parents don't like it when I'm too late."
        l "Of course."
        $ flena = "happy"
        l "It's been a wonderful afternoon. Thank you, guys."
        $ fholly = "shy"
        h "No, thank you... And thanks for inviting us to your home."
        i "I had a lot of fun talking to you girls. Let's meet again sometime, just the three of us."
        l "That would be cool."
        if v2_kiss:
            $ fian = "shy"
            $ flena = "flirtshy"
            "Ian and I looked at each other and it felt like we could read each other's mind for a split second."
            "It was weird that we hadn't kissed once during the whole time... And now it was the perfect moment."
            "But with Holly present, none of us felt it was appropriate... So we held it in."            
        scene lenahomenight
        show lena at rig3
        show ian at lef3
        show holly2
        with long
        "I walked them to the door and said goodbye."
        hide holly2
        hide ian
        with short
        show lena at rig
        with move
        
    else:
        h "It's getting late... I should make my way home. My parents don't like it when I'm too late."
        l "Of course."
        $ flena = "happy"
        l "It's been a wonderful afternoon. Thank you, Holly."
        $ fholly = "shy"
        hide holly
        show holly3 at lef
        with short
        h "No, thank you... I had a lot of fun talking to you. I'd love to meet with you some other time..."
        l "Yes, let's do that."
        h "And thanks for inviting me to your home!"
        scene lenahomenight
        show lena at rig
        show holly2 at lef
        with long
        "I walked Holly to the door and said goodbye."
        hide holly2
        with short
    $ flena = "n"    
    l "Well, that was nice..."
    $ flouise = "smile"
    $ louise_look = 2
    show louisebra2 at lef
    with short
    if v3_ian_date:
        lo "Who were those? Friends of yours?"
        l "Oh, Louise. Yes, they were Holly and Ian..."
        $ flouise = "happy"
        lo "Oh, the guy you have been telling me about? Damn, I wanted to meet him!"
        lo "I would've said hello, but as you can see I wasn't too presentable..."
        if v2_robert_home:
            lo "I've already met one of your lovers, now I have to meet the other one..."
            l "Shut up..."
    else:
        lo "Who was she? A friend of yours?"
        l "Oh, Louise. Yes, her name's Holly. She's a writer I met at the café, and I really liked her books..."
        lo "I see. I would've said hello, but as you can see I wasn't too presentable."
    $ flouise = "happy"
    "Louise came closer to me with a childish smile on her face."
    lo "So... You met Jeremy the other day!"
    l "Oh, yeah, I met your mysterious boyfriend..."
    if v3_spy:
        $ flena = "blush"
        "I had seen more of him than I should, but that was a secret I would take with me to the grave..."
        $ flena = "n"
    lo "What did you think of him?"
    show lena at rig3
    show louisebra2 at lef3
    with move
    $ flouise = "serious"
    $ fstan = "n"
    play sound "sfx/door.mp3"
    show stan 
    with short
    "At that moment Stan emerged from his room."
    st "Uh... Hi... Excuse me, I was gonna get some chips and a cola..."
    "He snuck between us and began searching in the pantry."
    lo "I don't know if you're aware, but we were talking about something private over here..."
    st "It'll be a second, it's just a snack..."
    menu:
        "About Jeremy...":
            $ renpy.block_rollback()
            $ v3_welcome_stan = True
            "I didn't think we were talking about something that Stan shouldn't hear, so I went on with the conversation."
            l "So, about Jeremy..."
            $ flouise = "sad"
            $ lena_louise -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            lo "Um..."
            
        "...":
            $ renpy.block_rollback()
            $ flena = "worried"
            "We waited for Stan to grab his snack in silence."
            l "..."
            lo "..."
            st "..."
            st "OK, done. Sorry for the interruption."
            play sound "sfx/door.mp3"
            hide stan
            with short
            lo "Can you believe this guy?"
            l "He's pretty awkward, yeah..."
            $ flena = "n"
            $ flouise = "n"
            l "Anyways, about Jeremy..."
            
        "{image=icon_mad.png}Beat it, fatso!" if lena_stan < 4:
            $ renpy.block_rollback()
            $ flena = "serious"
            l "Haven't you heard Louise? We're asking for privacy."
            $ fstan = "blush"
            st "But the living room is a common area..."
            $ flena = "mad"
            l "Are you even listening? Beat it, fatso!"
            $ fstan = "surprise"
            $ lena_stan = 2
            play sound "sfx/frienddown.mp3"
            show friend_down
            st "...!"
            play sound "sfx/door.mp3"
            hide stan
            with short
            "He finally got it and went back to his room."
            $ flena = "serious"
            $ flouise  = "happy"
            lo "That was awesome."
            l "It wasn't so hard to understand... He can wait five minutes for his snack."
            $ flena = "n"
            l "So, about Jeremy..."
                
    if v3_breakfast_jeremy:
        l "I thought he was pretty nice! I liked his energy and his attitude."
        $ flouise = "smile"
        lo "Right? He makes me feel so comfortable next to him, he's always positive and knows how to make me laugh..."
        l "Yeah, he seemed pretty funny. We had a silly conversation about avocado and toasts... But they were pretty good." 
        lo "Oh, so he made you his \"famous\" avocado toasts? Ha ha."
        l "Yeah. All in all, he seemed very extroverted and easygoing."
    else:
        l "I don't know what to tell you, to be honest. I barely talked to him..."
        l "He seemed quite extroverted and easygoing, though."
        $ flouise = "smile"
    if v3_welcome_stan:
        lo "Yes... That's what I like about him. I..."
        $ flouise = "serious"
        st "I'm done."
        "Stan squeezed through between Louise and me on his way back to his room, carrying a bag of chips and a bottle of cola."
        $ fstan = "smile"
        $ lena_stan += 1
        play sound "sfx/friendup.mp3"
        show friend_up
        "He looked at me and smiled. He didn't say anything though."
        play sound "sfx/door.mp3"
        hide stan
        with short
        lo "I can't believe this guy..."
        l "You're too jumpy with him."
        lo "I don't know how you're able to tolerate him so much..."
        l "What were you saying about Jeremy?"
        $ flouise = "smile"
        lo "Oh, yeah. I was saying I like how he makes me feel when I'm with him."        
    else:
        lo "Yes... That's what I like about him. I like how he makes me feel."
    l "That's very important... I'm happy for you. Really."
    lo "Thanks! I hope this really works out..."
    if lena_robert_sex_late:
        $ flena = "shy"
        l "By the way... Now that we're talking about guys..."
        l "Tonight Robert will come by and spend the night..."
        if v2_robert_home:
            $ flouise = "flirt"
            lo "Oh, I see... So he's spending the night again..."
            lo "I'll make sure me and Stan don't bother you, ha ha!"
        else:
            lo "Robert? Who's that?"
            l "The guy I work with at the restaurant. I think I've told you about him."
            $ flouise = "flirt"
            lo "Ohh, yes. So he's spending the night, huh... I'll make sure me and Stan don't bother you, ha ha!"
        $ flouise = "n"
        if v3_ian_date:
            lo "Though I thought maybe Ian would be the one to stay the night, since he was here just a moment ago..."
    elif v3_ian_date:
        $ flouise = "flirt"
        lo "What about you and Ian? I thought maybe you'd invite him to spend the night, since he was here just a moment ago..."
    $ flena = "blush"
    l "We don't have that kind of relationship..."
    $ flouise = "n"
    lo "Oh, I see..."
    lo "Well, I'm going back to my room."
    l "Yeah, me too. Goodnight, Louise."
    jump v3lenawednesdayroom
 
## LOUISE
label v3louisesong: 
    $ louise_look = 2
    show lenahomenight
    with long
    $ flena = "n"
    play sound "sfx/door_home.mp3"
    show lena2 at rig
    with short
    if lena_robert_sex_early or lena_robert_sex_late:
        "I got back home from the park. It had been a very nice afternoon."
    else:
        "I got back home from the park. It had been a very nice afternoon."
        "It had put me in a good mood, despite being worried about losing my job at the restaurant..."
    $ flouise = "smile"
    show louisebra at lef
    with short
    lo "Hey. Where are you coming from?"
    if v3_ian_date:
        l "I just took a stroll in the park with Ian and another girl."
        lo "Another girl?"
        l "Yeah, I met her at the café. Her name's Holly and turns out she's a writer whose books I really liked..."
    else:
        l "I just took a stroll in the park with a girl I met at the café. Her name's Holly and turns out she's a writer whose books I really liked..."
    if lena_robert_sex_late:
        lo "Oh, I see... Anything else I should know about?"
        $ flena = "shy"
        "She asked jokingly, but I had something to tell after all..."
        l "Um, well, tonight Robert will come by and spend the night..."
        if v2_robert_home:
            $ flouise = "flirt"
            lo "Oh, I see... So he's spending the night again..."
            lo "I'll make sure me and Stan don't bother you, ha ha!"
        else:
            lo "Robert? Who's that?"
            l "The guy I work with at the restaurant. I think I've told you about him."
            $ flouise = "flirt"
            lo "Ohh, yes. So he's spending the night, huh... I'll make sure me and Stan don't bother you, ha ha!"
        if v3_ian_date:
            $ flouise = "n"
            lo "Though I thought maybe Ian would be the one to stay the night, since you were just hanging out with him..."
            $ flena = "blush"
            l "We don't have that kind of relationship..."
            $ flouise = "n"
            lo "I see..."
    $ flouise = "happy"
    "Louise came closer to me with a childish smile on her face."
    lo "So... you met Jeremy the other day!"
    l "Oh, yeah, I met your mysterious boyfriend..."
    if v3_spy:
        $ flena = "blush"
        "I had seen more of him than I should, but that was a secret I would take with me to the grave..."
        $ flena = "n"
    lo "What did you think of him?"
    if v3_breakfast_jeremy:
        l "I thought he was pretty nice! I liked his energy and his attitude."
        lo "Right? He makes me feel so comfortable next to him, he's always positive and knows how to make me laugh..."
        l "Yeah, he seemed pretty funny. We had a silly conversation about avocado and toasts... But they were pretty good." 
        lo "Oh, so he made you his \"famous\" avocado toasts? Ha ha."
        l "Yeah. All in all, he seemed very extroverted and easygoing."
    else:
        l "I don't know what to tell you, to be honest. I barely talked to him..."
        l "He seemed quite extroverted and easygoing, though."
    lo "Yes... That's what I like about him. I like how he makes me feel."
    l "That's very important... I'm happy for you. Really."
    lo "Thanks! I hope this really works out..."
    l "By the way! I've been working on this song..."
    $ flena = "sad"
    l "I haven't showed anybody yet because I'm a bit insecure about it, but I need someone's opinion..." 
    l "I'd like you to be the first one to hear it..."
    $ flouise = "happy"
    $ lena_louise += 1
    play sound "sfx/friendup.mp3"
    show friend_up
    lo "Of course! I'd love that!"
    hide friend_up
    $ flena = "shy"
    l "Promise you won't laugh."
    lo "Of course not! It makes me so happy that you trust me enough to be the first person you show!"
    l "OK, let me get my guitar..."
    scene lenahomenight
    show lena_guitar1
    with long
    "I went to my room, picked up the instrument and sat on the couch."
    play sound "sfx/guitar.mp3"
    "I strummed the guitar while Louise paid close attention, her eyes bright..."
    $ flouise = "serious"
    $ fstan = "n"
    $ flena = "worried"
    scene lenahomenight
    play sound "sfx/door.mp3"
    show stan 
    show lena2 at rig3
    show louisebra2 at lef3
    with long
    "At that moment Stan emerged from his room."
    st "Uh... Hi... Excuse me, I was gonna get some chips and a cola..."
    "He walked up to the kitchen and began searching in the pantry."
    lo "I don't know if you're aware, but we're having a private moment in here..."
    st "It'll be a second, it's just a snack..."
    menu:
        "{image=icon_friend.png}Do you wanna listen, too, Stan?" if lena_stan > 5:
            $ renpy.block_rollback()
            $ v3_welcome_stan = True
            $ flena = "n"
            l "Stan, I was just about to show this song I've written to Louise..."
            l "Do you want to listen to it, too?"
            $ fstan = "blush"
            $ flouise = "sad"
            st "Who, me?"
            l "Yes, you're my friend too. I'd like your opinion..."
            $ lena_stan += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            st "Of course, yeah...!"
            $ lena_louise -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            lo "Um..."
            
        "...":
            $ renpy.block_rollback()
            $ flena = "worried"
            "We waited for Stan to grab his snack in silence."
            l "..."
            lo "..."
            st "..."
            st "OK, done. Sorry for the interruption."
            play sound "sfx/door.mp3"
            hide stan
            with short
            lo "Can you believe this guy?"
            l "He's pretty awkward, yeah..."
            $ flena = "n"
            $ flouise = "n"
            lo "Come on, play the song..."
            
        "{image=icon_mad.png}Beat it, fatso!" if lena_stan < 4:
            $ renpy.block_rollback()
            $ flena = "serious"
            l "Haven't you heard Louise? We're asking for privacy."
            $ fstan = "blush"
            st "But the living room is a common area..."
            $ flena = "mad"
            l "Are you even listening? Beat it, fatso!"
            $ fstan = "surprise"
            $ lena_stan = 2
            play sound "sfx/frienddown.mp3"
            show friend_down
            st "...!"
            play sound "sfx/door.mp3"
            hide stan
            with short
            "He finally got it and went back to his room."
            $ flena = "serious"
            $ flouise  = "happy"
            lo "That was awesome."
            l "I don't feel comfortable playing in front of him. He can wait five minutes for his snack."
            $ flena = "n"
            lo "Come on, play the song..."
    
    play music "music/lenas_theme.mp3" loop
    scene lenahomenight
    show lena_guitar1
    with long
    "I took a deep breath and relaxed, concentrating on the song."
    l "OK, here I go."
    play music "music/lenas_theme.mp3"
    "I began playing a sad melody, my fingers softly strumming the guitar."
    l "It's called \"Broken Dreams\"."
    "I eased myself into the music and began singing."
    l "{i}So vast and dark, this cosmic field of dreams we live in...{/i}"
    if song_1a == "real":
        l "{i}With our child-like hands, reaching out, trying to grasp something real.{/i}"
    if song_1a == "precise":
        l "{i}With our child-like hands, reaching out, trying to grasp something precise.{/i}"
    if song_1a == "cool":
        l "{i}With our child-like hands, reaching out, trying to grasp something cool.{/i}"
    l "{i}Like two moons on a collision course, this is our gravity...{/i}"
    if song_1b == "tragedy":
        l "{i}Like a star that burns out too quick, this is our tragedy.{/i}"
    if song_1b == "story":
        l "{i}Like a star that burns out too quick, this is our story.{/i}"
    if song_1b == "stuff":
        l "{i}Like a star that burns out too quick, this is our stuff.{/i}"
    l "{i}So bright and terrifying, this cosmic field of dreams where I exist...{/i}"
    if song_1c == "abyss":
        l "{i}Down the rabbit hole, holding your hand. Spiraling into our abyss.{/i}"
    if song_1c == "kingdom":
        l "{i}Down the rabbit hole, holding your hand. Spiraling into our kingdom.{/i}"
    if song_1c == "cave":
        l "{i}Down the rabbit hole, holding your hand. Spiraling into our cave.{/i}"
    l "{i}Like two moons on a collision course, this is our gravity...{/i}"
    if song_1b == "tragedy":
        l "{i}Like a star that burns out too quick, this is our tragedy.{/i}"
    if song_1b == "story":
        l "{i}Like a star that burns out too quick, this is our story.{/i}"
    if song_1b == "stuff":
        l "{i}Like a star that burns out too quick, this is our stuff.{/i}"
    l "{i}Ours, until we burned out.{/i}"
    l "{i}Ours, until we ceased to be...{/i}"
    "The final notes of the song left my fingers and died down on the guitar's strings."
    stop music fadeout 2.0
    
    $ flouise = "sad"
    $ fstan = "sad"
    $ flena = "worried"
    scene lenahomenight
    if v3_welcome_stan:
        show stan 
    show lena2 at rig3
    show louisebra2 at lef3
    with long
    l "Well... What did you think about it...?"
    if lena_song1 == 6:
        lo "It was so sad and beautiful... I'm about to cry..."
        $ flena = "blush"
        if v3_welcome_stan:
            st "It was really good... It made me sad, too..."
            l "Now I'm feeling guilty for making you guys feel bad!"
        else:
            l "Now I'm feeling guilty for making you feel bad!"
        $ flouise = "smile"
        lo "No, not at all! I love sad songs, they've always been my favorite..."
        lo "And this one was one of the most beautiful songs I've ever heard!"
        lo "You're an amazing songwriter, Lena!"        
        call screen willup
        l "Wow, I'm surprised you liked it so much..."
        lo "It's really good, believe me!"
        if v3_welcome_stan:
            $ fstan = "smile"
            st "Yeah, I think so too."
        
    elif lena_song1 > 3:
        lo "It was so sad and beautiful... It almost makes you want to cry..."
        $ flena = "sad"
        l "Oh, I'm sorry... I didn't want to make you feel bad..."
        if v3_welcome_stan:
            $ fstan = "smile"
            st "Yes, it was very sad, but I really liked it!"
        $ flouise = "smile"
        lo "It was a really cool song!"
        
    else:
        lo "It was sad and beautiful... A very emotional song!"
        l "Did you like it?"
        if v3_welcome_stan:
            $ fstan = "smile"
            st "I did. It was really good."
        $ flouise = "smile"
        lo "It's a cool song!"
        
    if song_1a == "cool":
        lo "I'm not sure about some of the lyrics, though... Maybe you could change something..."
        lo "I'd change the first verse... I think \"precise\" is a better suited word."
        menu:
            "Change it":
                $ renpy.block_rollback()
                $ song_1a = "precise"
                l "I think you're right. That way it sounds much better..."
                l "Thanks for your advice!"
                lo "You're welcome!"
            "Leave it as is":
                $ renpy.block_rollback()
                l "I think I'll leave it as it is for now... It is what came out of my mind, after all."
                lo "Of course, it was just a suggestion..."
    elif song_1b == "stuff":
        lo "I'm not sure about some of the lyrics, though... Maybe you could change something..."
        lo "I'd change the second verse... I think \"story\" is a better word."
        menu:
            "Change it":
                $ renpy.block_rollback()
                $ song_1b = "story"
                l "I think you're right. That way it sounds much better..."
                l "Thanks for your advice!"
                lo "You're welcome!"
            "Leave it as is":
                $ renpy.block_rollback()
                l "I think I'll leave it as it is for now... It is what came out of my mind, after all."
                lo "Of course, it was just a suggestion..."
    elif song_1c == "cave":
        lo "I'm not sure about some of the lyrics, though... Maybe you could change something..."
        lo "I'd change the third verse... I think \"kingdom\" sounds better."
        menu:
            "Change it":
                $ renpy.block_rollback()
                $ song_1c = "kingdom"
                l "I think you're right. That way it sounds much better..."
                l "Thanks for your advice!"
                lo "You're welcome!"
            "Leave it as is":
                $ renpy.block_rollback()
                l "I think I'll leave it as it is for now... It is what came out of my mind, after all."
                lo "Of course, it was just a suggestion..."

    l "Well, so that was my song."
    lo "Thank you for sharing with me."
    if v3_welcome_stan:
        st "And with me."
        $ flouise = "serious"
        st "Do you have any more songs?"
    else:
        lo "Have you written any more songs?"
        $ flena = "sad"
    l "No... I mean, I did. But I lost the notebooks where I had them written down."
    $ flouise = "sad"
    lo "What happened to them?"
    l "I left them at Axel's house after breaking up..."
    l "I haven't seen them since. Same as my old guitar."
    $ flena = "n"
    l "But it's OK. I've bought a new one and I will write new songs."
    $ flouise = "smile"
    lo "Show me when you do!"
    jump v3lenawednesdayroom
    
  
                
##MASTURBATE ######################################################################################################################################################################################################################

label v3lenawednesdayroom:
    
    scene lenaroomnight
    $ flena = "n"
    show lena2
    with long
    $ lena_song1 = 0                    
    if song_1a == "real":
        $ lena_song1 += 2
    if song_1a == "precise":
        $ lena_song1 += 1
    if song_1b == "tragedy":
        $ lena_song1 += 2
    if song_1b == "story":
        $ lena_song1 += 1
    if song_1c == "abyss":
        $ lena_song1 += 2
    if song_1c == "kingdom":
        $ lena_song1 += 1
    "I went to my room and closed the door."
    play sound "sfx/meow.mp3"
    show lola at lef3
    with short
    if v2_holly_song:
        l "Yes Lola, I'm alone now."
    else:
        l "Hey Lola, missed me?"
    if lena_robert_sex_late:
        play sound "sfx/sms.mp3"
        "I got a text from Robert."
        $ flena = "blush"
        r "{i}Hey babe! I've managed to convince the chef to let me out earlier from work tonight.{/i}"
        r "{i}I should be there in an hour or so! Can't wait to see you {image=emoji_fire.png} {image=emoji_fire.png}{/i}"
        "That's right... Robert would come shortly, and we would have sex..."
        "I would finally break the dry spell I had been living through since breaking up with Axel."
    hide lena2
    show lenaunder
    with long
    "I thought about these last few days while changing."
    $ lena_look = 2
    if v3_axel_call:
        $ flena = "worried"
        "I had decided I should talk to Axel at some point."
        l "Ahh, just thinking about it makes me nervous, Lola..."
        l "Do you think it's a good idea?"
        play sound "sfx/meow.mp3"
        l "I wish you could talk."
        if v1_talk_louise:
            l "Ivy thinks I should talk to him, and so does Louise..."
        if v1_talk_stan:
            l "Ivy thinks I should talk to him, but Stan says I shouldn't..."
        l "I have no idea how that will go. I have to make up my mind before calling him..."
    else:
        $ flena = "serious"
        "The thought of calling Axel had crossed my mind, but I had decided against it."
        l "He doesn't deserve it, don't you agree, Lola?"
        play sound "sfx/meow.mp3"
        $ flena = "sad"
        l "I wish you could talk."
        if v1_talk_louise:
            l "Ivy thinks I should talk to him, and so does Louise..."
            l "But that would only make things more complicated."
        if v1_talk_stan:
            l "Ivy thinks I should talk to him, but Stan says I shouldn't..."
            l "I agree with Stan on this."
        l "I don't want him in my life anymore. I wish I could just forget him..."
    if lena_robert_sex_early or lena_robert_sex_late:
        $ flena = "sad"
        "Getting my working hours reduced was something to worry about, too..."
        "I could make do with my salary from that and the café, but the budget would be extremely tight..."
        if v3_seymour_call or stalkfap:
            $ flena = "n"
            l "I'm already looking for ways to make more money, though."
            if stalkfap:
                l "I have no idea if that Stalkfap thing will work."
                l "It seems Ivy is making money with it, and she told me some girls earn quite a lot of money..."
            if v3_seymour_date:
                l "I'm also meeting Seymour Ward for dinner tomorrow night..."
                "Lola looked at me. Sometimes it was like she could understand me."
                "But even if that was the case, she couldn't answer back."
                l "He's quite mysterious, you know? I'm curious about him..."
                l "I'm not sure I like him, though. We'll see how it goes tomorrow..."
            else:
                $ flena = "serious"
                l "I thought about taking up Mr.Ward's offer, but I don't like his antics."
                l "If he wants to hire me as a model there's no need for stupid formalities like having dinner with him."
                l "It's not how I do things. He'll have to find himself another model."
                l "I'm sure it will be easy for him."
                $lena = "n"
            "I didn't want to worry too much about things..."
        "The situation could be worse, if it wasn't for Robert."
        $ flena = "blush"
        if lena_robert_sex_early:
            l "Robert... I really did it with him..."
            if v3_robert_orgasm:
                l "It was better than expected... Nothing crazy, but that's normal. It was our first time together after all."
            else:
                l "It wasn't fireworks, but that's to be expected. It had been quite some time since I last had sex with someone..."
                l "But I don't know, I'm still not entirely sure about Robert..."
        else:
            l "Robert... He'll be here shortly, Lola. You'll need to give us some privacy..."
            l "I guess I'm gonna really do it with him... I'm still not entirely sure about Robert, but the best way to find out is giving it a chance, right?"
    else:
        $ flena = "sad"
        l "What has me worried is losing my job at the restaurant..."
        l "This will be the last month I earn enough to pay for everything. With just the salary from the café I won't even have enough to scrape by..."
        if v3_seymour_call or stalkfap:
            $ flena = "n"
            l "I'm already looking for solutions to that problem, though."
            if stalkfap:
                l "I have no idea if that Stalkfap thing will work."
                l "It seems Ivy is making money with it, and she told me some girls earn quite a lot of money..."
            if v3_seymour_date:
                l "I'm also meeting Seymour Ward for dinner tomorrow night..."
                "Lola looked at me. Sometimes it was like she could understand me."
                "But even if that was the case, she couldn't answer back."
                l "He's quite mysterious, you know? I'm curious about him..."
                l "I'm not sure I like him, though. We'll see how it goes tomorrow..."
            else:
                $ flena = "serious"
                l "I thought about taking up Mr.Ward's offer, but I don't like his antics."
                l "If he wants to hire me as a model there's no need for stupid formalities like having dinner with him."
                l "It's not how I do things. He'll have to find himself another mode."
                l "I'm sure it will be easy for him."
                $lena = "n"
        else:
            l "I need to find a solution to that."
    play sound "sfx/meow.mp3"
    "Lola jumped down from the desk and asked me to open the door for her."
    $ flena = "n"
    l "Am I boring you? You're probably hungry, go..."
    play sound "sfx/door.mp3"
    hide lola
    with short
    l "Ahh..."
    l "Well, at least the afternoon was nice."
    if v3_ian_date:
        l "Ian seems like a really nice guy... I'd really like to get to know him better..."
    else:
        if v2_ian_date:
            l "I wonder why Ian canceled... I thought he'd want to hang out with me again."
    l "And Holly is such a lovable girl. And I'd say she's in dire need of a real friend..."
    if v3_seymour_call == False:
        l "And I'm in need of some financial security. I haven't gotten back to Mr. Ward about his job offer."
        "He had expressed interest in working with me as a model, since he was getting into photography."
        l "Maybe I should call him..."
        menu:
            "Call Mr. Ward":
                $ renpy.block_rollback()
                $ v3_seymour_call = True
                $ lena_look = 2
                hide lenaunder
                show lenabra
                l "It's not so late. Maybe I can still call him."
                l "He's supposed to be someone important and wealthy... I'm sure he pays good."
                "I pulled out his card and looked up his contact info."
                hide lenabra
                show lenabra_phone
                with short
                l "..."
                $ flena = "sad"
                l "... ..."
                l "... ... ..."
                "Just when I thought he wouldn't pick up, I heard his voice."
                show phone_seymour at lef3
                with short
                mr "Yes? Who's this?"
                l "Uh, it's me, Lena. We met this Friday at the exhibition. Sorry to call at this hour."
                hide phone_seymour
                show phone_seymour_smile at lef3
                mr "Oh, Lena, of course. I was expecting your call."
                $ flena = "n"
                mr "I take it you're interested in my offer?"
                l "Yes, I am."
                mr "Good. Let's schedule a meeting, then. When are you available?"
                l "Let's see, this week... I'm free on Wednesday or Thursday afternoon."
                mr "Lets make it this Thursday, but at night."
                $ flena = "worried"
                l "At night? Isn't that a bit late for a photo-shoot?"
                hide phone_seymour_smile
                show phone_seymour at lef3
                mr "I wasn't thinking about a photo-shoot. I'm very picky when it comes to the people I choose to work with."
                mr "You gave me a good impression on Friday, but I want to know more about you before hiring you as a model."
                mr "I want to make sure you're the right person for what I have in mind."
                "What was he talking about? Make sure I was the right one?"
                "He was just an amateur but he was acting like he was such a high-profile and important photographer."
                l "So you want us to talk or...?"
                mr "Let's meet for dinner. That way we'll be able to have some informal conversation and see if we can work together."
                menu:
                    "Accept":
                        $ renpy.block_rollback()
                        $ v3_seymour_date = True
                        "It was the first time someone asked me to do a job interview to pose for them..."
                        $ flena = "n"
                        l "Alright, I guess..."
                        hide phone_seymour
                        show phone_seymour_smile at lef3
                        mr "Thursday night it is, then. You live in the city, right?"
                        l "Yeah, pretty close to the downtown area."
                        mr "Perfect, since I wanted us to meet there. I'm picking the restaurant."
                        mr "See you on Thursday. Thanks for your interest, Lena."
                        l "No, thank you."
                        hide phone_seymour_smile
                        hide lenabra_phone
                        show lenaunder
                        with short
                        "So he wanted us to have dinner... That was unexpected, and unusual."
                        "I was well aware some men that hired models thought they were buying more than just a photo-shoot, but I hoped that wasn't the case..."
                        "Seymour didn't sound like someone so simple-minded, though that didn't guarantee anything. Cultured men could be big creeps, too."
                        "In any case I was intrigued. I had my doubts about his moral character, but one thing was sure: he was an intelligent and interesting man."
                        "He was arrogant and authoritative, too. Wanting to evaluate me..."
                        "Well, this dinner would serve me too as well. I would get the chance to know what kind of man he really was, and maybe then I would be the one not interested in working with him."
                        l "We'll see how that goes... It will be an interesting experience either way, it seems."
                        
                    "Refuse":
                        $ renpy.block_rollback()
                        $ flena = "serious"
                        $ v3_seymour_reject = True  
                        l "I'm sorry, but that's not how I work."
                        l "I thought you had already decided you wanted to work with me, but it's not my job to convince you if you're uncertain about that."
                        l "If you want me as a model I can give you references so you can judge the quality of my work, but I don't do dinners, or job interviews."
                        hide phone_seymour
                        show phone_seymour_serious at lef3
                        mr "Is that so? I thought you called me because you were interested in working with me."
                        l "I called to respond to your request, Mr. Ward."
                        l "And I'm sorry, but I'm not interested in doing business with you."
                        $ lena_seymour = 2
                        play sound "sfx/frienddown.mp3"
                        show friend_down
                        mr "So be it! I don't need to tell you how dumb it is to let this chance pass."
                        mr "I have the feeling you'll come to realize your mistake, and you'll come back to me on your knees."
                        l "Nice dream. Too bad it won't happen."
                        l "Have a good Sunday, Mr. Ward."
                        hide phone_seymour_serious
                        hide lenabra_phone
                        show lenaunder
                        with short
                        "I hung up."
                        "I didn't know what he was expecting, but I didn't like his arrogance at all."
                        "It was clear he was used to everybody playing by his rules. But I wouldn't."
                        "I didn't want to have dinner with him. Too many men like him thought they were buying more than just a photo-shoot."
                        "I was a model, not an escort girl. He'd have to find someone else for that."
                        $ flena = "n"
                $ lena_look = 1
                hide lenabra
                show lenaunder
                
            "Not interested":
                $ renpy.block_rollback()
                l "I don't think it's a good idea... I didn't really feel comfortable around him."
                l "He'll have to find himself another model."
 
    if lena_robert_sex_late:
        jump v3wednesdayrobert
    $ flena = "blush"
    hide lenaunder
    show lenabra2
    with short
    if v3_spy:
        "My mind kept meandering through these days' events, and then I remembered what I saw the other night."
        "Of course I remembered..."
        "Louise and her boyfriend going at it in her room..."
        if v3_spy_full:
            "I shouldn't have spied on them, but I did. I kept watching until the very end."
        else:
            "I shouldn't have spied on them, but I did. Even if I stopped halfway."
        "Remembering it was making me feel kinda horny..."
        l "Oh, gosh..."
        if lena_robert_sex_early:
            "What had happened with Robert in this room also came to mind..."
            "I had spent so long without having sex and just now I was realizing how much I had been missing it..."
        elif v2_kiss:
            "The kiss I had shared with Ian came to mind, too..."
            "The feel of his lips, his taste, his smell... His amber eyes looking at me..."
            "I imagined him holding me, his hands on my waist, my arms around his shoulders, chest to chest..."
        "I felt my belly heating up and a tingling sensation between my legs..."
        "My body was asking me to give it some attention... And I decided to listen to it."
    else:
        if lena_robert_sex_early:
            "My mind kept meandering through these days' events, remembering what Robert and I had done in this bed."
            "Thinking about it was making me horny..."
            l "Oh, gosh..."
            "I had spent so long without having sex and just now I was realizing how much I had been missing it..."
            "I felt my belly heating up and a tingling sensation between my legs..."
            "My body was asking me to give it some attention... And I decided to listen to it."
        elif v2_kiss:
            "My mind kept meandering through these days' events, and I remembered my kiss with Ian..."
            "The feel of his lips, his taste, his smell... His amber eyes looking at me..."
            "I imagined him holding me, his hands on my waist, my arms around his shoulders, chest to chest..."
            "I began getting horny..."
            l "Oh, gosh..."
            "I felt my belly heating up and a tingling sensation between my legs..."
            "My body was asking me to give it some attention... And I decided to listen to it."
        else:
            "My mind kept meandering through these days' events until it got tired."
            "I needed a break."
            "As I lay down on my bed, my body suggested what I could do to keep my mind off those things."
            menu:
                "Masturbate":
                    $ renpy.block_rollback()
                    "I felt my belly heating up and a tingling sensation between my legs..."
                    "My body was asking me to give it some attention... And I decided to listen to it."
                    play sound "sfx/xp.mp3"
                    show lust_up
                    $ lena_lust_xp += 1
                    call screen skillsup
                 
                "Go to sleep":
                    $ renpy.block_rollback()
                    "I felt sleepy, so I got into bed and closed my eyes."
                    jump v3lenathursday
    
    play music "music/sensual.mp3" loop
    scene lenaroomnight
    with long
    "I took off my underwear and sat comfortably on my bed."
    scene v3_solo1_animation
    with long
    "I slid my hand down my belly, slowly, until my fingers reached my sex."
    "The fingertips brushed my labia and I took a deep breath."
    "I could feel the warmth radiating through my skin, the subtle titillation that drove my hand in search for pleasure..."
    play sound "sfx/mh1.mp3"
    l "Mhhh..."
    "A soft moan, or maybe a sigh, escaped my lips as my fingers dived between my labia, slowly, like a guest who's not yet sure he's well received."
    "When was the last time I had masturbated?"
    "I had been so busy with everything, so tired working two jobs, too worried about life to even think about it."
    "I had been leaving my needs and desires unattended far too long... It was time to care about myself again."
    "My fingers caressed my clit gently, starting up my engine for good."
    "Soon they found wetness and I found tingling pleasure spreading through my body."
    play sound "sfx/ah1.mp3"
    l "Ahhh..."
    "This time I moaned a bit louder. I was getting into it..."
    scene v3_solo2_animation
    with long
    "I laid back and closed my eyes, forgetting about everything but the here and now."
    "Me, my body and my pleasure."
    play sound "sfx/ah3.mp3"
    "My fingers rubbed my clit more intensely, both reconciled after the long absence."
    "I bit my lip as my breathing got heavier, shaken by the pulsating waves of lust that were muddying my senses."
    "My hips began moving following that pulse, syncing with the hasty motion of my fingers."
    "Pleasure was growing and so was my excitement..."
    if lena_lust > 1:
        "Then something came to mind."
        "I remembered what I had stored in the back of a drawer. Something that could come in very handy right now..."
        scene v3_solo3
        with long
        "It was a vibrator Ivy had bought for my birthday a couple of years ago. A silly gift I had never really used that much."
        "I wasn't too used to using sex toys. I never really felt the need to."
        "But maybe it could make this moment even better..."
        menu:
            "{image=icon_love.png}Call Robert" if lena_robert_sex_early:
                $ renpy.block_rollback()
                $ v3_robert_repeat = True
                l "Wait a minute, I don't need this..."
                l "I have Robert!"
                jump v3wednesdayrobert2

            "{image=icon_lust.png}Use it":
                $ renpy.block_rollback()
                $ v3_use_dildo = True
                scene v3_solo4_animation
                with long
                "I pointed the vibrator towards my slit, turned it on and pushed it down slowly."
                play sound "sfx/ah3.mp3"
                "I felt it entering me, spreading my pussy while its vibrations did the same across my lower body."
                "I moved it back and forth, making way for it bit by bit."
                if lena_robert_sex:
                    "The feeling of Robert penetrating me came to mind..."
                else:
                    "It was the first thing penetrating my pussy in a long time..."
                "As the buzzing made my insides vibrate, I tried to concentrate on something that really turned me on..."
                
            "Don't use it":
                $ renpy.block_rollback()
                scene v3_solo2_animation
                with long
                "I tossed it aside. I preferred the warmth of my fingers, the human touch."
                "I didn't need a toy to stimulate myself. I just needed my mind and to use my imagination..."
                "To focus on what really turned me on..."
    else:
        "I still needed more to reach the climax. I needed to imagine, to focus on what really turned me on..."
    menu:
        "Think about Ian" if v2_ian_date:
            $ renpy.block_rollback()
            $ v3_masturbate = "ian"
            $ fian = "smile"
            scene lenaroomnight
            if v3_ian_date == False:
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
            if v3_use_dildo:
                "His cock..."                

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
                "I wanted to feel more of him. Of her. I wanted them to make me vibrate like I was vibrating now..."
            
        "Think about Robert" if lena_robert_sex:
            $ renpy.block_rollback()
            $ v3_masturbate = "robert"
            "I remembered what had happened in this bed the other day..."
            if v3_robert_orgasm:
                scene v3_robert10
                with long
                "Robert's naked body, his hands grabbing my flesh, his lips on my neck..."
                "I shivered, the vibrator plunged inside me like Robert's cock had been, too."
                "I imagined he was penetrating me again, rubbing my insides while I played with my clit, racing to orgasm..."
            else:
                scene v3_robert7
                with long
                "Robert's naked body, his hands grabbing my flesh, his hips hitting my butt..."
                "I shivered, the vibrator plunged inside me like Robert's cock had been, too."
                "I imagined he was penetrating me again, fucking me..."
            
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
            "I plunged the dildo even deeper inside me. I wondered what she had been feeling that night..."
            
        "Think about spying on Louise" if v3_spy:
            $ renpy.block_rollback()
            $ v3_masturbate = "spy"
            "I couldn't avoid thinking about what I had seen the other night."
            scene v3_louise2
            with long
            "I saw Louise pressed down against the bed, being penetrated by her boyfriend..."
            "Her expression and her moans were a mixture of pleasure and pain..."
            "Her red lips wide apart, her hands gripping the bed sheets, her body being rocked back and forth with every thrust..."
            "It was so hot..."

        "Focus on your body":
            $ renpy.block_rollback()
            "I focused on my body, on the sensations..."
            "Pleasure was building up and I wasn't going to let it deflate."
            "The simple experience of pleasure was enough to turn me on enough to cum..."            
    
    if v3_use_dildo:
        scene v3_solo4_animation
        with long
        "I tilted the dildo up and pressed it against my interior wall."
        "The vibration concentrated at the tip and stimulated the internal part of the clitoris directly."
        "My legs began trembling, the orgasm closing in."
        play sound "sfx/ah5.mp3"
    else:
        scene v3_solo2_animation
        with long
        "I rubbed my clit harder, pressing down, moving my fingers in circles."
        "I felt them being wet and sticky with my juices, the ones lubricating my eager endeavor..."
        "I could feel it coming. I was about to reach my oh so desired goal..."
        play sound "sfx/ah6.mp3"
    with vpunch
    l "Oh, God...! Yes...!"
    l "Ahhhh...!"
    "All the air in my lungs left me at the time of release. Pleasure washed away everything during a few blissful seconds."
    stop music fadeout 2.0
    scene lenaroomnight
    with long
    "My body was left relaxed and my eyes felt heavy. I was warm, tired, and feeling wonderful..."
    "I fell asleep shortly after."
    jump v3lenathursday
             
##WEDNESDAY ROBERT SEX ###############################################################################################################################################################################             

label v3wednesdayrobert:
    
    $ lena_robert_sex = True
    l "Robert shouldn't take too long..."
    if v3_spy:
        "While I waited for him, my mind kept meandering through these days' events, and then I remembered what I saw the other night."
        "Of course I remembered..."
        "Louise and her boyfriend going at it in her room..."
        if v3_spy_full:
            "I shouldn't have spied on them, but I did. I kept watching until the very end."
        else:
            "I shouldn't have spied on them, but I did. Even if I stopped halfway."
        "Remembering it was making me feel kinda horny..."
        l "Oh, gosh..."
    else:
        "My mind kept meandering through these days' events until it got tired."
        "I needed a break, and I was about to get one."
    "I felt my belly heating up and a tingling sensation between my legs..."
    "My body was asking me to give it some attention... And soon it would get what it wanted, thanks to Robert."
    play sound "sfx/sms.mp3"
    "My phone buzzed. It was Robert letting me know he was at the door."
    "I got up and grabbed my shirt."
    if lena_lust > 2:
        $ flena = "flirt"
        "But, on second thought, I dropped it. No need for it, considering what Robert was here to do."
    scene lenahomenight_dark
    with long
    if lena_lust > 3:
        $ flena = "slut"
        $ lena_look = 2
    else:
        $ flena = "flirt"
        $ lena_look = 1
    show lenabra at lef
    with short
    $ frobert = "flirt"
    $ robert_look = 1
    "I opened the door for him."
    show robert at rig
    with short
    play music "music/sensual.mp3" loop
    r "Hey, baby..."
    if lena_lust > 2:
        $ frobert = "evil"
        "He took a good look at me and licked his lips."
        r "Damn, I see you were expecting me..."
        l "I was... Let's go to my room."
    else:
        r "I hope I didn't make you wait for too long."
        l "It's OK... Let's go to my room."
    play sound "sfx/door.mp3"
    scene lenaroomnight
    with long
    if v2_robert_home:
        show lenabra at lef
        show robert at rig
        with short
        "I closed the door behind us. The tension was palpable, and Robert had no intention of wasting time."
        "We both knew why we were here."
    else:
        show lenabra at lef3
        show robert at rig3
        with short
        "When we entered the room Lola climbed on the bed, looking at us with curiosity."
        play sound "sfx/meow.mp3"
        show lola 
        with short
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
        $ frobert = "flirt"
        r "Never mind. Come here."
        show robert at rig
        show lenabra at lef
        $ flena = "flirt"
        with move
    
    hide robert
    hide lenabra
    show robertunder at rig
    show lenanude2 at lef
    with long
    "Robert removed my underwear hastily, his movements full of desire, while I took off his shirt."
    r "Damn, you're so sexy, Lena..."
    "Robert took out his wallet and a condom from a pocket before throwing his pants away."
    hide robertunder
    show robertnude at rig
    with short
    r "Mhh, here we go..."
    l "Come over here."
    scene lenaroom
    show v3_robert1b
    with long
    "He embraced me and his lips went for a deep kiss right away."
    "Our tongues slid over each other's with wet passion as Robert's desirous hands squeezed my bare ass."
    "I felt his skin against mine, the heat of his body bleeding into mine..."
    "My sensitive nipples rubbed against his chest, sending tingles up my spine. And his erect cock also did, but against my belly."
    "I felt his manhood pressed against my body, trapped between our pubes. It was sliding back and forth slightly, pushed by Robert's hip movements."
    "I felt the head of his dick rub over my labia, trying to spread it, as our wet kissing continued..."    
    scene v3_robert2
    with long
    "We moved to the bed, lying next to each other as our hands continued to caress our bodies."
    "Our lips were still glued together. Robert's kisses were anxious and a bit clumsy, blinded by his uncontrollable desire for me."
    "It was so obvious how he was losing his head over me..."
    "I had been feeling horny while waiting for him, and this was turning me on even more..."
    "I was finally feeling a real, naked, warm body against mine. I had been missing this sensation..."
    "My hand slid down his slender abdomen until I reached his cock."
    r "Mhh, baby..."
    "As I wrapped my fingers around the hard shaft I could tell how horny he was..."
    "He was completely erect, almost like he was ready to burst..."
    menu:
        "Eat me out":
            $ renpy.block_rollback()
            $ v3_robert_orgasm = True
            "I wanted to feel like that, too."
            l "Eat me out, Robert."
            scene v3_robert4
            with long
            "I didn't give him the option to answer."
            play sound "sfx/xp.mp3"
            show lust_up
            $ lena_lust_xp += 1
            call screen skillsup
            "I just lay back and spread my legs apart, inviting him. An offer he couldn't refuse."
            r "Mhpf!"
            play sound "sfx/mh1.mp3"
            l "Mhhh..."
            "He dove right in without any subtlety, propelled by that base desire he felt."
            "It was like he wanted to devour me and in his effort to satisfy his hunger he didn't know where to start from."
            "I felt his tongue swirling like crazy across my pussy, licking and lapping chaotically."
            "I guided his head up with my hand, slightly adjusting his position, driving his caresses to my clit."
            l "Mhh yeah, that's better..."
            "I closed my eyes and focused on just enjoying myself for a moment."
            play sound "sfx/ah6.mp3"
            "The wet and hot strokes of his tongue sent strong tingles up my belly and down my legs..."
            "His saliva mixed with my juices, flowing more profusely as my excitement grew..."
            "It wasn't the best cunnilingus ever, but it was still enjoyable..."
            "After a while I decided it was time to give Robert what he wanted. And I wanted it too..."
            l "Do me, Robert... Fuck me."
            
        "Let me suck you off":
            $ renpy.block_rollback()
            $ v3_robert_bj = True
            $ lena_bj += 1
            "I was sure Robert was dying to penetrate me right away, but I wanted to do something first..."
            l "Let me suck you off..."
            "It was an offer he wasn't going to refuse, obviously."
            r "Yeah baby, go ahead..."
            $ lena_robert += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            scene lenaroom
            show v3_robert3b
            with long
            "I crawled down his legs until his hard tool was right in front of my face, eager and ready for my attentions."
            play sound "sfx/bj4.mp3"
            "When I slid my tongue up the shaft I felt Robert shiver."
            r "Oh, baby!"
            "I wanted to have sex with him but I felt I wasn't wet enough yet. Working on his cock would surely do the trick."
            play sound "sfx/xp.mp3"
            show lust_up
            $ lena_lust_xp += 1
            call screen skillsup
            "I enjoyed it."
            l "Mhhh.. Ahh..."
            r "Fuck baby, your mouth is crazy good."
            "As I kept sucking and savoring his dick I felt my excitement and the heat in my lower belly grow."
            "Robert was more than pleased with my blowjob, of course."
            "But we hadn't come here just for that."
            l "Let's do it, now..."
            r "Hell yeah. Get up."
            
        "Put it in...":
            $ renpy.block_rollback()
            "I was ready for it."
            l "You can put it in... But do it slowly."
            r "Yes, of course, let me take care of it..."
     
    scene v3_robert5b
    if v3_robert_orgasm or v3_robert_bj:
        show v3_robert5_slut
    with long
    "Robert searched for a condom in his pants, cracked it open and quickly put it on."
    if v3_robert_orgasm or v3_robert_bj:
        "Robert positioned me on top of the bed to his liking."
        r "Yes, get on all fours..."
        "If that's how he wanted it that's how I was gonna give it to him. I was just so eager to feel his manhood inside of me!"
        "He finished adjusting the condom and slid the tip of his cock across my slit."
        l "Mhhh!"
        r "Oh yeah baby, I'm so hard...!"
        scene lenaroom
        show v3_robert6b
        show v3_robert5_slut
        with long
        r "Hmmm, you're tight!"
        play sound "sfx/ah3.mp3"
        "I was, but I also was really wet, so his cock slid in without too much trouble."
        "I felt it pressing onward, filling me in a single motion."
        l "Ohhh..."
        r "Damn, baby... You're really excited, aren't you?"
        l "Fuck yeah..."
        "Finally, I had broken my dry spell... I was having sex for the first time since my breakup with Axel."
        "He began moving his hips back and forth at a light pace, taking it somewhat slow."
        l "Mh, yes... Just like that..."
        "Bit by bit my insides turned more comfortable for Robert, welcoming him and making room for his cock." 
    else:
        r "Here, get like this... yeah."
        "Robert put me on all fours on top of the bed and got behind me while finishing adjusting the rubber."
        l "What, like this...?"
        r "Yeah, this way it will be easier, trust me."
        "He slid the tip of his cock across my slit, preparing it."
        "It was finally going to happen. I was about to have sex for the first time since my breakup with Axel..." 
        scene lenaroom
        show v3_robert6b
        with long
        "Robert began pushing it in slowly."
        play sound "sfx/ah3.mp3"
        r "Hmmm, you're tight...!"
        "I was a lot more excited and eager than last night, but I was somewhat hesitant, still..."
        "I wasn't as lubricated as I would've liked to, and that was making Robert's job a bit more difficult."
        l "Just a bit more, slowly..."
        r "Yeah..."
        "Thankfully he was taking his time and being considerate about it."
        "I felt his manhood penetrate me bit by bit, gaining half an inch of terrain with each thrust."
        r "Ahh, there, finally..."
    scene v3_robert7b
    with long
    "Robert began getting carried away, giving it to me faster each time."
    r "Oh Lena, oh yes..."
    r "I've wanted to do this since the first time I saw you at the restaurant...!"
    play sound "sfx/mh1.mp3"
    l "Mhhh...!"
    "His thrusts became harder as he pumped his hips hastily."
    "He fucked me fast and eagerly, his passion for me unbridled."
    "He was claiming my body, penetrating my sex, enjoying me..."
    "Having me on all fours at the end of his dick made Robert feel like he was in heaven, or so his groans told me..."
    "But tonight we had time, and I wanted to enjoy myself as much as possible, too."
    l "Wait, let's change position..."
    scene v3_robert9b
    with long
    "I guided him with my body, letting myself lie on the bed with Robert still inside, spooning me."
    "I felt his warm, sweaty chest on my back, his heavy breathing on my ear."
    r "You drive me crazy, Lena..."
    "His whisper made me shiver and fanned my fire. That's how I liked it..."
    "Robert kept pumping his hips, but this posture made him go at a slower pace. I liked it better..."
    l "Just like that... Ahh, don't go faster..."
    r "I don't need to... I'll cum like this, too..."
    "I wanted to cum, too! I wasn't gonna let this chance slip my hands, so I used them."
    scene lenaroom
    show v3_robert10b
    with short
    $ lena_lust_xp += 1
    play sound "sfx/xp.mp3"
    show lust_up
    call screen skillsup
    "I moved my hand to my pussy, and caressed it."
    "My fingers quickly found my clit and began rubbing it."
    "A new and intense source of pleasure added to the sensation of Robert's cock penetrating me."
    "That could do it..."
    l "Don't stop Robert, keep that rhythm!"
    r "This is how you like it, babe? You touching yourself is so damn hot...!"
    "I kept masturbating myself while Robert gave it to me from behind. Pleasure was building up and beginning to overflow..."
    l "Yeah...! Mhhh!"
    "I was almost there...! Just a bit more...!"
    "I stimulated my clit at the right speed, with the right pressure, giving myself just what I needed."
    "That, plus the hot sensation of Robert's cock sliding in and out of my pussy, was enough to finally drive me to climax."
    play sound "sfx/orgasm1.mp3"
    l "Ahhh!"
    with vpunch
    "My hips and legs trembled as the orgasm shook me."
    r "You're cumming?"
    l "Y..{w=0.3}yes!"
    r "That's so hot! Oh God!"
    "Robert felt like he had no need to hold back anymore."
    "He let himself loose, penetrating me fast and hard."
    "His climax followed within seconds."
    r "Ohhhh! Oh, yeah!"
    with flash
    with vpunch
    "He grunted and tensed behind me as he ejaculated inside the condom."
    l "Ahhh..."
    "I tried to relax while I felt the orgasm wash over my body before fading."
    "I had done it. I had finally fucked another guy."
    "I had feared it could've been terrible, but I ended up getting into it enough to even cum..."
    $ flena = "flirt"
    $ frobert = "smile"
    scene lenaroomnight
    show robertnude at rig
    show lenanude2 at lef
    with long
    stop music fadeout 2.0
    r "Whew... That was great... You liked it too, didn't you?"
    l "Yes, it was good..."
    $ v3_robert_orgasm = True
    r "I'm glad... We should've done this so much earlier..."
    l "Well, I'm glad we did it now."
    r "And I hope we can keep doing it for a long, long time..."
    "He kissed me on the forehead."
    $ frobert = "n"
    r "Man, I'm beat... After working all night and now giving it all with you..."
    "He yawned and closed his eyes."
    r "Good night, Lena."
    hide robertnude
    with long
    $ flena = "n"
    "So he would be spending the night here... Well, I was already counting on that."
    if v2_robert_home:
        "It wouldn't be the first time, after all."
    scene lenaroomnight
    with short
    "I closed my eyes too and tried to get some sleep."
    "My mind was surprisingly quiet... It was the first time in a long time."
    "I quickly fell asleep."
    jump v3wednesdayrobertmorning
        
label v3wednesdayrobert2:   
    stop music fadeout 2.0
    scene lenaroomnight
    $ flena = "slut"
    show lenanude_phone
    with long
    "I picked up my phone and called him."
    l "He should be getting off work right about now..."
    show phone_robert_smile at lef3
    with short
    r "Hey, Lena! What's up? I wasn't expecting you to call at this hour..."
    l "Are you free?"
    r "I still have to finish cleaning up and close the restaurant, but yeah..."
    l "I want you to come to my place."
    l "Right now."
    r "Right now?"
    l "I'm waiting for you. Naked."
    r "Holy shit! I'll have Samantha take care of this...!"
    r "I'm on my way!"
    hide phone_robert_smile
    hide lenanude_phone
    show lenanude2
    with short
    play sound "sfx/xp.mp3"
    show lust_up
    $ lena_lust_xp += 1
    call screen skillsup
    l "Good boy."
    scene v3_solo1_animation
    with long
    "While I waited for Robert I continued to play with my self."
    "Softly, slowly, without getting too carried away..."
    "Just keeping myself warm until his arrival."
    "He didn't take long."
    scene lenahomenight_dark
    with long
    $ frobert = "smile"
    "He sent me a text telling me he was at the door and I welcomed him."
    show lenanude2 at lef
    show robert at rig
    with short
    r "Hey baby... Oh my God, you were really waiting for me naked!"
    l "Don't talk. Let's go to my room."
    play music "music/sensual.mp3" loop
    play sound "sfx/door.mp3"
    scene v3_robert1b
    with long
    "He didn't complain and followed me to my bedroom."
    "As soon as I closed the door behind us we began making out, Robert's hands hungrily groping my naked body and mine stripping him off his clothes."
    "I felt powerful. I wished him here, to take care of my needs, and here he was."
    "Now I could enjoy myself to my heart's content. Unlike Sunday, we had all the time we wanted."
    if v3_robert_orgasm == False:
        "And this time I was determined to get my orgasm."
    scene v3_robert2
    with long
    "We moved to the bed, lying next to each other as our hands continued to caress our bodies."
    "Our lips were still glued together. Robert's kisses were anxious and a bit clumsy, blinded by his uncontrollable desire for me."
    "It was so obvious how he was losing his head over me... And I liked it."
    "My hand slid down his slender abdomen until I reached his cock."
    r "Mhh, baby..."
    "This would do the trick much better than the vibrator..."
    "I began jerking him off slowly, making him squirm with pleasure."
    "He was completely erect, almost like he was ready to burst..."
    if v3_robert_bj == False:
        menu:
            "Let me suck you off":
                $ renpy.block_rollback()
                $ v3_robert_bj = True
                $ lena_bj += 1
                "I was sure Robert was dying to penetrate me right away, but I wanted to do something first..."
                "I had plenty of time, after all."
                l "Let me suck you off..."
                "It was an offer he wasn't going to refuse, obviously."
                r "Yeah baby, go ahead..."
                $ lena_robert += 1
                play sound "sfx/friendup.mp3"
                show friend_up
                scene lenaroom
                show v3_robert3b
                with long
                "I crawled down his legs until his hard tool was right in front of my face, eager and ready for my attentions."
                play sound "sfx/bj4.mp3"
                "When I slid my tongue up the shaft I felt Robert shiver."
                r "Oh, baby!"
                "I wanted to have sex with him but I felt I wasn't wet enough yet. Working on his cock would surely do the trick."
                play sound "sfx/xp.mp3"
                show lust_up
                $ lena_lust_xp += 1
                call screen skillsup
                "I enjoyed it."
                l "Mhhh.. Ahh..."
                r "Fuck baby, your mouth is crazy good."
                "As I kept sucking and savoring his dick I felt my excitement and the heat in my lower belly grow."
                "I wanted him to make me feel good, too."
                l "Now's my turn... Eat me out."
            
            "Eat me out":
                $ renpy.block_rollback()
                "I wanted to feel like that too."
                l "Eat me out, Robert."
    else:
        "I wanted to feel like that, too."
        l "Eat me out, Robert."
    scene v3_robert4
    with long
    "I didn't give him the option to answer."
    "I just lay back and spread my legs apart, inviting him. An offer he couldn't refuse."
    r "Mhpf!"
    play sound "sfx/mh1.mp3"
    l "Mhhh..."
    "He dove right in without any subtlety, propelled by that base desire he felt."
    "It was like he wanted to devour me and in his effort to satisfy his hunger he didn't know where to start from."
    "I felt his tongue swirling like crazy across my pussy, licking and lapping chaotically."
    "I guided his head up with my hand, slightly adjusting his position, driving his caresses to my clit."
    l "Mhh yeah, that's better..."
    "I closed my eyes and focused on just enjoying myself for a moment."
    play sound "sfx/ah6.mp3"
    "The wet and hot strokes of his tongue sent strong tingles up my belly and down my legs..."
    "His saliva mixed with my juices, flowing more profusely as my excitement grew..."
    "I hadn't had the chance to enjoy a cunnilingus for such a long time..."
    "After a while I decided it was time to experience Robert's cock once again."
    "This time it would be me who took control, though."
    scene v3_robert8
    with long
    "I pushed him to the bed and climbed on top of him."
    r "Oh, baby!"
    "I grabbed his latex covered dick and positioned it at my slit, then I lowered my hips, welcoming him inside again."
    "I began moving my hips back and forth, grinding on him, controlling the speed and rhythm."
    "My clit rubbed against his pubis with each movement, and I angled my hips to feel his cock just the right way."
    play sound "sfx/ah1.mp3"
    l "Mhhh... Yes..."
    "I was liking it. But so was Robert, more than I was."
    "He was groaning, eyes closed and mouth open, pleasure painted on his face."
    r "Baby! Baby, I'm cumming!"
    with flash
    with vpunch
    r "Oahhhh!!"
    "He convulsed under me, writhing in ecstasy. But I was not done yet."
    "I kept grinding on top of him. His cock was still hard, although it was losing consistency bit by bit."
    r "Lena, you're killing me...!"
    l "Just a bit more...!"
    "I moved my hips faster, rubbing my clit harder against Robert's pubis."
    "The bed was squeaking under my frantic movements. I had to reach the breaking point before his cock shriveled completely."
    "I was so close...!"
    l "Yes, yes...!"
    play sound "sfx/ah4.mp3"
    with vpunch
    l "Yesssaahhh!"
    "My body tensed and my legs trembled as I was struck by the orgasm."
    if v3_robert_orgasm == False:
        "Finally, I managed to cum!"
        "Robert had granted me that wonderful sensation that I was missing..."
    else:
        "Robert had granted me that wonderful sensation once again..."
    stop music fadeout 2.0
    $ flena = "flirt"
    $ frobert = "sad"
    scene lenaroomnight
    show lenanude at lef
    show robertnude at rig
    with long
    "I dropped next to Robert, tired, relaxed and satisfied." 
    r "Wow Lena, that was intense..."
    l "Yeah..."
    $ v3_robert_orgasm = True
    r "Man, I'm beat... After working all night and now giving it all with you..."
    r "This was even better than the first time. I loved how you took control..."
    l "So you liked it?"
    r "Yeah, you can do any time you want with me, ha ha."
    "He yawned and closed his eyes. Then he kissed me on the forehead."
    r "Good night, Lena."
    hide robertnude
    with long
    $ flena = "n"
    "So he would be spending the night here... Well, I was already counting on that."
    if v2_robert_home:
        "It wouldn't be the first time, after all."
    "I closed my eyes too and tried to get some sleep."
    scene lenaroomnight
    with long
    "I closed my eyes too and tried to get some sleep."
    "My mind was surprisingly quiet... It was the first time in a long time."
    "I quickly fell asleep."
    jump v3wednesdayrobertmorning
      
label v3wednesdayrobertmorning:        
    $ day = "Thursday"
    $ louise_look = 1
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    $ flena = "n"
    "I opened my eyes with the first lights of day."
    show lenanude at rig
    with short
    "Robert was sound asleep next to me."
    $ flena = "surprise"
    $ frobert = "sad"
    "I looked at the time. It was really late!"
    l "Robert, wake up! I need to leave for work!"
    show robertnude at lef
    with short
    r "Uhh... This early?"
    $ flena = "worried"
    l "It's not early! I won't have time to even get a shower..."
    l "Quick, get dressed and let's be on our way."
    $ frobert = "n"
    r "Alright, alright..."
    if v2_robert_home:
        jump v3lenathursday2
    $ louise_look = 1
    play sound "sfx/door.mp3"
    scene lenahome
    with long
    $ lena_look = 1
    $ flena = "n"
    "I went to the bathroom and groomed myself a bit while Robert got dressed."
    show lena at rig
    show robert at lef
    with short
    l "OK, let's go..."
    show robert at truecenter
    show lena at rig3
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
    if v2_robert_home == False:
        lo "So you must be Robert, right?"
        $ frobert = "flirt"
        r "Yeah. I guess Lena has told you about me..."
        lo "She has."
    else:
        lo "Hey there again, Robert. Are you staying for breakfast?"
    l "We were just leaving. I'm late for work."
    lo "Oh, OK."
    $ frobert = "smile"
    r "Nice to meet you. Maybe next time we can make better introductions, ha ha."
    lo "Sure. Bye guys!"
    jump v3lenathursday2
    
        
##THURSDAY GYM IVY ###############################################################################################################################################################################             
        
label v3lenathursday:
    $ day = "Thursday"
    scene blackbg
    with long
    call screen calendar
    scene lenaroom
    with long
    $ flena = "n"
    show lenabra
    with short
    "I woke up feeling quite refreshed the next morning."
    "It had been so nice to finally have a night off..."
    if v3_seymour_date:
        "Tonight I would be meeting Mr. Ward, but first I had to go to work."
    else:
        "Tonight I had free time too, but first I had to go to work."
        
label v3lenathursday2: 
    $ v3chativy1 = False
    $ v3chativy2 = False
    $ v3chativy3 = False
    $ ivy_navel = True
    $ v3_ivy_chat = False
    $ lena_go_piercing = 0
    scene cafe
    with long
    $ lena_look = 1
    $ flena = "n"
    show lenawork
    with short
    "My shift was pretty calm and uneventful."
    "I prepared coffees, served tables and counted the cash drawer before leaving."
    "I had promised Ivy I would join her class today, since I hadn't been able to do so before all week."
    if v3_seymour_date:
        "I didn't want to tire myself out too much before dinner with Mr. Ward, though..."
    play music "music/jeremys_theme.mp3" loop
    scene polegym
    with long
    $ lena_look = 2
    $ ivy_look = 2
    $ fivy = "flirt"
    show lena at rig
    with short
    "I got changed and stepped into the studio."
    show ivy at lef
    with short
    v "Here you are, you bitch! I finally see you!"
    l "I promised I'd show up."
    v "How have you been?"
    if v2_robert_reject and v3_robert_date and v3_robert_reject == False:
        $ v2_robert_reject = False
    menu v3ivychat:
        "They're firing me from the restaurant" if v2_robert_reject and v3chativy1 == False or v3_robert_reject and v3chativy1 == False:
            $ renpy.block_rollback()
            $ v3chativy1 = True
            $ flena = "sad"
            l "I'm being fired from the restaurant."
            $ fivy = "sad"
            v "What? What happened, did you do something wrong?"
            l "No, I didn't! It seems they wanted to reduce staff to make a better profit... So they won't be renewing my contract after the end of the month."            
            $ fivy = "n"
            v "Well, you should look at it as an opportunity to get into new things. Better things."
            v "You're worth much more than a waitressing job!"
            v "I'm sure you can find better ways of making cash."
            $ flena = "n"
            l "I have no other choice..."
            jump v3ivychat
            
        "I'm getting less hours at work" if lena_robert_sex and v3chativy1 == False:
            $ renpy.block_rollback()
            $ v3chativy1 = True
            $ flena = "sad"
            l "I'm getting less working hours at the restaurant."
            v "That's good, isn't it?"
            l "No, it's not... I'm getting less pay, and I need the money!"
            $ fivy = "n"
            v "Well, you should look at this as an opportunity to get into new things. Better things."
            v "With your free time you can find other ways of making cash. You're worth much more than a waitressing job!"
            $ flena = "n"
            l "I have no other choice..."
            jump v3ivychat
            
        "I've been writing songs again" if v3chativy2 == False:
            $ renpy.block_rollback()
            $ v3chativy2 = True
            l "I bought a guitar and I've been writing songs again."
            $ fivy = "smile"
            v "Oh, so you're back at it again? You've always had the soul of a poet, ha ha."
            l "Yeah, I had been missing it... It helps me sort out my bottled-up emotions."
            v "You always liked to write poems and stuff like that. You were like this back in high school already."
            v "People said you were quite talented, right?"
            $ fivy = "flirt"
            v "I remember our English teacher being very fond of you..."
            $ flena = "blush"
            v "He always praised your poems and never gave you a grade lower than an A."
            l "That's because I was a very good student..."
            v "Yes, you surely were."
            $ flena = "n"
            l "Truth be told, he inspired me to keep writing and I learned a lot from him."
            $ fivy = "n"
            v "To think I was friends with the teacher's pet, ha ha."
            jump v3ivychat
            
        "You've gotten a new piercing!" if v3chativy3 == False:
            $ renpy.block_rollback()
            $ v3chativy3 = True
            $ flena = "smile"
            l "I see you've gotten a navel piercing!"
            $ fivy = "flirt"
            v "I was wondering if you'd notice!"
            l "Of course, I'm not blind!"
            v "Do you like it?"
            menu:
                "I'm thinking about getting one too":
                    $ renpy.block_rollback()
                    $ lena_go_piercing = 2
                    l "I do, I really do! It looks very good on you..."
                    l "In fact I'm thinking I should get one myself..."
                    v "You copycat!"
                    v "But yeah, I think it will suit you too!"                    
                "It suits you":
                    $ renpy.block_rollback()
                    $ lena_go_piercing = 1
                    l "It really suits you. It looks very sexy."
                    v "It does, huh? Good, ha ha."                    
                "It's not my thing":
                    $ renpy.block_rollback()
                    $ flena = "n"
                    l "It suits you, but it's not my thing."
                    v "Nothing is your thing, girl! You need to be a bit more open minded!"
                    l "I am open minded. I just don't think it would fit my style."
                    v "Your goody two-shoes style, ha ha."
            $ fivy ="n"
            $ flena = "n"
            jump v3ivychat
        
        "Start the class":
            $ renpy.block_rollback()
            "The other girls were taking positions, expecting the class to begin."
            v "Wait, I have to start the class..."
            hide ivy
            show ivy2 at lef
            with short
            v "OK girls, today we'll focus on fitness! Let's build up those booties!"
            v "Grab a kettlebell and do the same sets as last week..."
            "Her pupils did as Ivy instructed."
            hide ivy2
            show ivy at lef
            with short
            v "Alright, what were we saying?"                        
            
    if stalkfap:
        $ fivy = "flirt"
        v "Oh, yeah, I see you created a Stalkfap profile!"
        l "Yeah, I decided to give it a try as you said... But I only have like three or four followers so far."
        v "That's because you just uploaded one boring picture! You need to stay active, post content regularly..."
        v "Give the people what they want! I'm starting to make enough to think about quitting teaching pole classes..."
    else:
        l "What about you, Ivy? How are you doing?"
        v "Oh, you know me. Same as always! I've been focusing more on that Stalkfap thing I showed you..."
        v "And it's going pretty well! I'm starting to make enough to think about quitting teaching pole classes..."
    l "Really? Do you think you could end up living off of Stalkfap entirely?"
    $ fivy = "smile"
    v "It's entirely possible. But it's not so simple..."
    v "Listen, I have everything planned out..."
    v "The most important thing is getting visibility. Peoplegram is key for that."
    v "I need modeling accounts to repost my pictures. You know, the ones that post pictures of other Peoplegram models. They have a ton of followers."
    v "I've already gotten featured in some of those, and that's the best strategy to boost my follower count!"
    l "Sounds similar to doing collaborations with photographers and other models."
    v "Yes, I'm also doing that. But that's small league play."
    $ fivy = "flirt"
    v "I'm playing for the jackpot. And that means getting signed on by Wildcats!"
    l "Wildcats? What's that?"
    v "You really are clueless! It's the hottest model brand right now."
    v "The hottest and most popular models right now are signing on with Wildcats, and they host parties for big time celebrities and rich people."
    v "Getting signed on by them is like getting a golden ticket to the high spheres of society!"
    v "Not only do you get the chance to meet the really important people, but also tens of thousands of followers and tens of thousands of dollars!"
    l "Are you going to apply and try to get signed?"
    $ fivy = "smile"
    v "Ha, if it only were that easy! You don't \"apply\" to get signed on at Wildcats. Not unless you already have a ton of social traction."
    v "That's what I'm trying to achieve first, getting my pics reposted by modeling accounts..."
    v "I need to get featured by bigger and bigger promoters on Peoplegram until I'm ready to be noticed by Wildcats!"
    l "Wow, I see you really have a plan in mind..."
    v "See? I'm a clever girl, too, and I have a good nose for business."
    l "I never doubted you were clever. I'm sure you'll achieve your goals."
    $ fivy = "sad"
    v "I hope so... I'm still a long way from that. I need to work hard to get their attention with my social media..."
    $ fivy = "smile"
    v "But when I do I'll be sure to invite you to one of the amazing parties they host, ha ha."
    "The other girls were hard at work while Ivy and I chatted nonchalantly."
    if v3_seymour_date:
        "Better this way... I didn't want to get tired before my meeting with Mr. Ward."
    menu:
        "Keep chatting with Ivy":
            $ renpy.block_rollback()
            $ v3_ivy_chat = True
            if v3_seymour_date:
                l "I have a dinner tonight, so I think I'll pass on the exercises..."
                v "A dinner? With whom?"
                "I told her about meeting Mr. Ward at the exhibition and his weird proposal."
                v "Ugh, these rich guys love to show us around any chance they get... But as long as they pay!"
                v "He can be an interesting contact to have, though. If he likes working with you I'm sure you can charge him a higher fee!"
                l "Money doesn't seem to be an issue for him, that's for sure."
                v "I'm glad you followed my advice and are taking more modeling gigs."
            else:
                "I wasn't feeling like working out, sweating and suffering through all those squats, so I decided to keep talking to Ivy."
            l "Any news about that guy you told me about? The one working with you at the club..."
            $ fivy ="flirt"
            v "Things are getting pretty hot! I was testing him a bit, seeing if he would give up or if he was really interested..."
            v "But I think it's time to give him what he wants. I've made him suffer long enough, ha ha."
            v "Oh, and turns out he works out in this building! He does boxing or something at the gym in the lower floor."
            l "Seems like you're bound to run into him, ha ha."
            if v2_ian_date:
                v "What about you? Have you met that guy you told me about again?"
                $ flena = "blush"
                v "The one that you liked..."
                if v3_ian_date:
                    l "Ian? Yeah, we met yesterday..."
                    v "So, did something happen?"
                    l "No, no... There was another girl, too. We just took a stroll in the park, as friends."
                else:
                    l "Ian? No... We were supposed to, but he canceled."
                    v "That means he's probably not interested... He should be begging to see you!"
                    l "It's not like that. We're just friends..."
                if v2_kiss:
                    v "Friends who kissed."
                    l "Well... I don't know. It remains to be seen."
                else:
                    v "So you only see him as a friend?"
                    l "For the time being, yes..."
            if lena_robert_sex:
                v "What about the guy from the restaurant? Robert, right?"
                $ flena = "shy"
                l "Oh, yeah... About that..."
                l "I had sex with him."
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
                v "I don't want to end up visiting you at a convent! So don't go back to living like a nun, please!"
                $ flena = "happy"
                l "Don't be silly, ha ha!"
                v "I suppose he's not asking you to be his girlfriend or anything like that."
                l "No, he hasn't. It's not like we've talked about it, but I don't see him as boyfriend material."
            else:
                v "What about the guy from the restaurant? Robert, right?"
                l "I rejected him and he's quite butthurt."
                v "Guys can't take no for an answer without having their fragile masculine ego feeling hurt."
                v "I swear to God, sometimes they're just like kids."
            v "Anyways, avoid getting tied down at all costs."  
            v "Last thing you need is getting into another relationship after Axel."
            v "It's time for you to play the field for a while! Enjoy sex without all the drama and neediness and all that bullshit."
            if v3_axel_call:
                $ flena = "sad"
                l "About Axel... I've decided I will call him."
                $ fivy = "n"
                v "Oh, so you're gonna talk to him?"
                l "Yeah... But I'm still not sure it's a good idea. I don't know how to go about it."
                v "Try to stay calm. Don't get all riled up and give him reasons to think you're still invested in him."
                v "Listen to what he has to say, tell him very clearly what you've decided."
                l "What worries me is how he'll react."
                v "That's his problem, not yours."
            "We kept chatting about stuff while the other girls did their workout."
            $ lena_ivy += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            "Finally the class came to an end."
            v "We spent the whole hour talking! Well, we don't need to take a shower, which means..."
            
        "Do the exercise instead" if v3_seymour_date == False:
            $ renpy.block_rollback()
            l "I think I should start working out, too, or I won't get anything done today."
            $ fivy = "flirt"
            v "Oh, sure, go ahead. Pick one of these kettlebells and build that booty!"
            $ flena = "surprise"
            with vpunch
            "Ivy slapped my ass and sent me on my way."
            scene polegym
            show v2_gym
            with long
            if v2_lena_gogym:
                "I knew what I had to do already."
                "I repeated the exercises I did last week, working my squats and lunges."
                "Soon I began sweating and my muscles aching again..."
                "But I had powered through once, I could do it again."
                play sound "sfx/xp.mp3"
                $ lena_athletics_xp +=1
                show athletics_up
                call screen skillsup
                l "No pain, no gain... But I still hate it!"
                "Finally I finished the workout and the class ended."
                $ flena = "worried"
                $ fivy = "smile"
                scene polegym
                show lena at rig3
                show ivy at lef3
                with short
                l "Whew... I'm beat!"
                v "You need to do this a lot more to get really used to it!"
                l "Hey, what I need is encouragement right now..."
                v "Ha ha!"
            else:
                "I grabbed a kettlebell and took position next to the other girls."
                "We worked our legs, arms and core..."
                "As I squatted, holding the kettlebell, my legs trembled and ached."
                "Sweat ran down my forehead as pain spread through my thighs, like a thousand needles being buried in them."
                "But I wanted to be healthy and in good shape, so I had to suffer."
                l "No pain, no gain.... But I hate this quite a lot!"           
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
            "Ivy looked at the clock."
            v "Quick, let's take a shower and be on our way."
            $ fivy = "flirt"
            
    v "The guy I told you about should be finishing his workout right about now..."
    v "If we're quick we'll catch him at the exit, and I can introduce him to you! I want your opinion!"
    $ flena = "smile"
    l "Alright."       
    stop music fadeout 2.0
    scene streetnight
    with long
    $ lena_look = 1
    $ ivy_look = 1
    $ fivy = "n"
    $ flena = "n"
    $ fjeremy = "smile"
    $ fian = "surprise"
    $ ian_look = 1
    show lena at rig
    show ivy at lef
    with short
    "I followed Ivy to the street. And just like she had planned, we crossed paths with the guy she was interested in..."
    "But he wasn't alone."
    show lena at right
    show ivy at centerlef
    with move
    $ flena = "surprise"
    $ fivy = "flirt"
    show jeremy at rig
    show ian at left
    hide lena
    show lena at right
    with short
    j "Hey, we meet each other again, Ivy!"
    v "So it seems!"
    if ian_ivy > 3:
        v "Oh, and Ian too..."
        $ fivy = "n"
        $ flena = "blush"
        $ fian = "blush"
        v "Wait, Ian..."
        $ fivy = "surprise"
        v "That's the name of the guy you told me about!"
        "She was such a blabbermouth!"
        $ fivy = "smile"
        $ fian = "smile"
        i "Hey, Lena. What are you doing here?"
        $ flena = "shy"
        l "I take Ivy's pole dancing classes..."        
    else:
        i "Lena! What are you doing here?"
        $ flena = "shy"
        l "Hey Ian. I take Ivy's pole dancing classes..."
        $ fian = "smile"
        i "Oh..."
    $ flena = "sad"
    "But meeting Ian unexpectedly once again wasn't the thing that really shocked me."
    "It was discovering that Jeremy was also the guy Ivy had been telling me about..."
    $ fjeremy = "surprise"
    "Only then Jeremy seemed to piece things together and understand the situation he was in."
    "He looked at me, then at Ivy."
    j "Wait, you two are friends?"
    $ fivy = "sad"
    if v2_showlena_jeremy:
        "Ivy looked at me and then at Jeremy, visibly confused."
        v "You two know each other?"
        l "Yeah..."
        $ fian = "n"
    else:
        "Ian had questions, too."
        $ fian = "worried"
        i "You know Lena?"
        j "Well, yeah, we just met the other day... You also know her?"
        i "Yeah dude, she's the waitress I told you about..."
        "Ivy looked at me and then at Jeremy, visibly confused."
        v "Wait, wait. Since when do you two know each other?"
        "I had to explain."
    l "Jeremy was at my place the other day."
    $ fjeremy = "sad"
    v "At your place?"
    l "Yeah. He's my flat mate's... boyfriend."
    $ fivy = "mad"
    v "Your flatmate? Who, Louise?"
    l "Yeah..."
    "Ivy looked at Jeremy."
    $ fivy = "serious"
    v "So... He's Louise's boyfriend."
    v "I never knew you had a girlfriend."
    $ fian = "sad"
    j "Well, it's more like... an open relationship I would say..."
    v "Is that so? Either way, you failed to mention you had a girlfriend. Why's that?"
    j "Uh, no, I mean... She's not really my girlfriend, but she thinks she is, so..."
    $ fivy = "flirt"
    "Ivy laughed."
    v "So you don't want to burst her bubble? How nice of you."
    $ fivy = "n"
    v "Well, see you at the club, Jeremy. Let's go, Lena."
    hide ivy
    with short
    "Ivy began walking without waiting for me to agree."
    "I looked at Ian. How had I gotten myself tangled up in this mess?"
    show lena at truecenter
    show jeremy at rig3
    show ian at lef3
    with move
    $ flena = "n"
    l "Seems we're bound to meet by coincidence, huh?"
    $ fian = "smile"
    i "So it seems, yeah."
    if v2_showlena_jeremy:
        $ flena = "serious"
        "I gave Jeremy a harsh look."
        l "A lot of coincidences, it seems."
        j "Yeah..."
    else:
        $ fian = "n"
        i "You, me... and Jeremy."
        $ flena = "serious"
        "I gave Jeremy a harsh look."
        l "Yes, that's another weird coincidence."
        j "Yeah, super weird..."
    $ flena = "sad"
    l "Well, I gotta run."
    if v2_ian_date:
        l "See you soon, OK?"
        i "Whenever you want."
    else:
        l "See you!"
    hide jeremy
    hide ian
    with short
    show lena at rig
    with move
    "I caught up to Ivy."
    show ivy at lef
    with short
    l "Hey. That was such a mess..."
    v "It was! So Jeremy is friends with the guy you told me about. And you knew Jeremy because he's Louise's \"boyfriend\"."
    "The way she said that last word made me cringe."
    l "What he said was disgusting."
    l "You must be shocked to suddenly find out he's this kind of guy..."
    v "Ha! I'm hardly surprised. I've been around and I know how guys are."
    v "It's disappointing, yeah... But at least now I have a reason to give him shit for."
    $ fivy = "flirt"
    v "Making him pay will keep me quite entertained, ha ha."
    "She took it very well. But the one who worried me was Louise..."
    "If she knew, if she heard what Jeremy said... I feared how hard she would take it."
    if v3_seymour_date:
        jump v3seymourdinner
    else:
        jump master_script
    
## SEYMOUR DINNER ################################################################################################################################################################################################################ 
 
label v3seymourdinner:
    $ say_niet = False  # Lena picks Nietzsche
    $ filo = True       # Lena talks philosophy with Seymour
    
    scene lenaroomnight
    with long
    $ flena = "n"
    show lena
    with short
    "I got back home with only enough time to drop my gym bag and minimally grooming myself."
    "I was supposed to meet Seymour Ward in about fifteen minutes."
    if lena_posh > 1:
        l "I should put on something a bit more classy than shirt and jeans..."
        l "I'm having dinner with a pretty important individual."
        hide lena
        with short
        $ lena_look = 3
        "I dug through my wardrobe trying to find something appropriate."
        l "Not this... This is too plain... This is too old... This I should've thrown away ages ago..."
        l "..."
        show lena
        with long
        l "This will do."
        l "Mr. Ward will surely appreciate this. Elegant but not too formal."
    else:
        menu:
            "Change clothes":
                $ renpy.block_rollback()
                $ lena_posh += 1
                l "I should put on something a bit more classy than shirt and jeans..."
                l "I'm having dinner with a pretty important individual, or so it seems."
                hide lena
                with short
                $ lena_look = 3
                "I dug through my wardrobe trying to find something appropriate."
                l "Not this... This is too plain... This is too old... This I should've thrown away ages ago..."
                l "..."
                show lena
                with long
                l "This will do."
                l "It's elegant but not too formal."
                "This dinner was a job interview in disguise, after all. I had to look the part."
                
            "Wear your casual clothes":
                $ renpy.block_rollback()
                if lena_posh > 0:
                    $ lena_posh -= 1
                "I thought about changing, but I decided my casual clothes would do."
                "I wasn't trying to impress anybody. I liked my work to speak for itself."
                "If Mr. Ward wanted to hire me it would have to be based on that." 
    "Once ready I made sure I wasn't forgetting anything and left." 
 
    scene streetnight
    with long
    show lena with short
    "I arrived at the meeting point and waited for Seymour to show up."
    "I wondered how this dinner would play out... He was a mysterious character and I was curious to know more about him."
    "Then I would judge if I liked what I had seen or not."
    "Then I noticed someone walking up to me. I turned around, expecting Seymour, but..."
    show lena at rig
    with move
    show hobo at lef
    with short
    if help_bum == 2:
        "He noticed me looking at him and looked back."
        bum "What?"
        bum "Oh, wait, you're that girl from last night..."
        l "Yeah... Hi."
        if lena_look == 3:
            bum "I hadn't recognized you, dressed this fancy."
        "He looked at me again and I had the impression he was contrite, like he wanted to say something that wouldn't come out easy."
        "After a brief pause, he talked."
        bum "I, uh, I'm sorry if I made you uncomfortable the other day. I shouldn't have jumped on you at that time of night."
        bum "I had, uh... hit the booze a bit too hard that night. And I'm sorry for being ungrateful."
        $ flena = "sad"
        l "It's OK..."
        bum "That moment painted a very clear picture about myself and I couldn't bear to look at it."
        bum "It made me reflect on some... aspects of my life I'm not too proud of."
        bum "I want to blame the booze for that, though."
        $ flena = "n"
        l "It's always easier, huh?"
        bum "Yeah."
    elif help_bum == 1:
        $ flena = "worried"
        "He was that homeless man who harassed me the other night!"
        "He noticed me looking at him and looked back."
        bum "Huh? What?"
        bum "Oh, wait, you're that girl from the other day..."
        if lena_look == 3:
            bum "I hadn't recognized you, dressed this fancy."
        l "Um... Yeah..."
        "I felt safer now, being in a well lit street with other people around. Still, I hoped he would just move on and leave me be."
        "But I wasn't expecting what he said next."
        bum "Listen, I, uh, wanted to apologize for the other night. I know I was harsh and that I scared you."
        bum "That was a particularly rough night and I... tried to find solace in the booze."
        bum "Too much solace, if you know what I mean."
        "I didn't know what to answer to him. I almost felt bad for not giving him any change that night."
        l "Well, I, um... I'm sorry to hear that..."
    else:
        $ flena = "drama"
        "He was that creepy homeless guy I had ran away from!"
        "He noticed me looking at him and looked back."
        bum "Huh? What?"
        "It looked like he didn't remember me. Not surprising, considering how strongly he had reeked of alcohol that night..."
        bum "Wait, you're the girl from the other night..."
        "Now I wished he had kept ignorant about that fact. Last thing I wanted was to confront this man again."
        if lena_look == 3:
            bum "You're dressed fancy today..."
        l "Look, I... I'm sorry, but..."
    mr "Stop bothering the young lady."
    show lena at rig3
    show hobo at lef3
    with move
    $ fseymour = "serious"
    show seymour
    with short
    "The man I was actually waiting for appeared at that moment."
    "His voice was unwavering and commanded authority." 
    mr "Show you have some decency left in you and get going, come on."
    mr "This nice street doesn't need your unpleasant presence."
    if help_bum == 2:
        l "He wasn't bothering me..."
    elif help_bum == 1:
        "Thankfully Mr. Ward knew how to put an end to this awkward situation."
    else:
        "I let out a sigh of relief. My savior!"
    $ fseymour = "sad"
    mr "Wait a minute..."
    mr "Schelling? Charles Schelling?"
    bum "I don't know what you're talking about."
    hide hobo
    with short
    $ flena = "sad"
    "He turned around and walked away without looking back, disappearing after turning a corner."
    $ fseymour = "n"
    mr "Huh..."
    show seymour at lef
    show lena at rig
    with move
    l "Do you know him?"
    $ fseymour = "smile"
    mr "Yeah, I think I do. I used to, rather."
    mr "We graduated together in college. Small world."
    mr "And funny seeing how the wheel of time turns and puts everyone in his rightful place."
    l "So you think he deserves to be homeless?"
    $ fseymour = "n"
    mr "I think he brought it on himself. Men are the architects of their own downfall."
    mr "Nothing comes free in this world. You need to make yourself useful."
    mr "If you're not able to provide value for others it means you're not needed."
    mr "And if that's the case you're going to have a very bad time, like that bum over there."
    mr "People need to realize that reality."
    menu:
        "{image=icon_wits}What's my value, then?" if lena_wits > 1:
            $ renpy.block_rollback()
            $ flena = "n"
            l "So, if our standing in this world depends on our ability to provide value, what I am here for?"
            l "What's the value you see in me?"
            $ fseymour = "smile"
            mr "I brought you here precisely to discover that."
            l "But you had to see something prior that piqued your interest."
            mr "Of course, but that's obvious. I saw how beautiful you are."
            $ flena = "serious"
            "I scoffed."
            l "Is that my great value? How shallow!"
            play sound "sfx/friendup.mp3"
            show friend_up
            $ lena_seymour += 1
            mr "You're a smart girl, Lena. You should be aware that being beautiful is of enormous value."
            $ flena = "worried"
            mr "So is being smart, but don't downplay beauty."
            mr "Men are willing to die for beauty, and a woman who's beautiful wields enormous power."
            $ flena = "blush"
            mr "A kind of power that can get you what you desire or need much easier and faster than being smart."
            
        "That's harsh":
            $ renpy.block_rollback()
            l "That's pretty harsh..."
            mr "Life is harsh. I'm sure you've experienced that reality yourself."
            "I couldn't say I hadn't..."
            $ fseymour = "smile"
            mr "There's a big difference between that bum and you, though."
            mr "He ruined his chances to provide value. You, on the other hand, have so much potential."
            $ flena = "n"
            l "Potential? What kind of potential?"
            mr "The most obvious thing is you're beautiful. And that's of great value."
            l "To who?"
            mr "To men. To women, too. To society itself."
            mr "Men have been willing to die for beauty, and a woman who's beautiful wields an enormous power."
            $ flena = "blush"
            
        "I think the same" if help_bum < 2:
            $ renpy.block_rollback()
            $ flena = "n"
            l "I think you're right. I see it the same way."
            $ fseymour = "smile"
            mr "Oh, you do?"
            mr "It's a bit early to claim to see the sights at the top of the mountain...But your sights are on the right course."
            mr "You have a lot of value to offer."
            l "I hope so."
            mr "You don't need to downplay yourself. I know you're aware of at least the most obvious of your gifts."
            l "Which one would that be?"
            mr "You're a very beautiful young lady. And beauty is incredibly valuable."
            l "Really? Would you consider it {i}that{/i} valuable?"
            mr "Without a doubt. Men have been willing to die for beauty, and a woman who's beautiful wields an enormous power."
            $ flena = "blush"
            
    $ fseymour = "smile"
    mr "Anyways, because of this chance encounter we skipped a proper greeting."
    mr "I'm happy to see you decided to join me tonight, Lena."
    if lena_look == 3:
        $ flena = "n"
        mr "May I commend your choice of attire? You're looking really beautiful."
        mr "I knew I could trust in your good taste. Very fitting for the establishment we're visiting tonight."
        l "Thank you."
    else:
        $ fseymour = "n"
        play sound "sfx/frienddown.mp3"
        show friend_down
        $ lena_seymour -= 1
        mr "Though I was hoping you'd choose a more... tasteful attire for the occasion."
        $ flena = "n"
        l "Why?"
        mr "It would be more appropriate for the establishment we'll be visiting."
        l "I thought this was just a job interview. You never told me it would be so formal."
        mr "I thought it was to be expected, considering who you're dealing with."
        $ fseymour = "smile"
        mr "I like everything that surrounds me to be of... exquisite taste."
        mr "I'll try to be more clear in the future."
    mr "Shall we go, then?"
    if lena_seymour > 3:
        l "Yes, let's go."
    else:
        "I was already there, so I thought I might as well do what I came to do."
        l "Sure."
    mr "It's just around the corner."
    "I followed Seymour across the street. It was an area I knew very well..."
    $ flena = "worried"
    "Too well."
    "As our steps brought us closer to a building I was very familiar with, I started to fear the worst."
    mr "Here it is. Let's go up."
    $ flena = "blush"
    "He entered the hotel where Yunalesca was located."
    play music "music/flirty.mp3" loop
    scene restaurant
    with long
    "Indeed, he had brought me to the restaurant where I worked."
    show lena at rig
    show seymour at lef 
    with short
    "I couldn't believe it. How unlucky was I?"
    "As we took the elevator up I didn't know how to react. For some reason this situation was making me feel so ashamed..."
    "I got struck by some kind of impostor syndrome. I couldn't feel like a real client at the place where I spent so many hours slaving away."
    "Yunalesca was a place for people like Seymour to enjoy. The closest girls like me could get to this kind of luxury was as an employee..." 
    "When we finally reached to top floor and entered the restaurant we were greeted..."
    $ robert_look = 2
    $ frobert = "n"
    show seymour at truecenter
    show lena at rig3
    with move
    show robert at lef3
    with short
    "By Robert."
    mr "I have a reservation."
    r "Yes sir. VIP table. Follow me..."
    $ frobert = "sad"
    "Then Robert's eyes fixed on me and opened wide with surprise."
    r "Lena!"
    l "Hi..."
    $ frobert = "sad"
    $ fseymour = "n"
    "Thankfully, he regained composure and acted professionally."
    r "Please, this way..."
    hide robert
    with short
    show seymour at lef
    show lena at rig
    with move
    "He led us to our table and left us with the menus."
    mr "Did you know him?"
    menu:
        "He's my co-worker":
            $ renpy.block_rollback()
            $ seymour_restaurant = True
            l "Yes... Actually, I know all the staff."
            mr "How come?"
            l "Because I work here, too."
            $ fseymour = "sad"
            "I could tell he was surprised."
            mr "You work as a waitress here?"
            l "Yes..."
            $ fseymour = "n"
            mr "I had no idea. I imagine you were shocked when I brought you here."
            l "I would be lying if I said I wasn't."
            $ fseymour = "smile"
            mr "You could've said something. If I had known it would be uncomfortable for you I would've chosen another place."
            $ flena = "n"
            l "It's OK... I've been working here four months and I've never experienced it from the client point of view. It will be... interesting."
            mr "As I said before, it's indeed funny how the wheel turns putting everybody in their rightful place."
            mr "And I'd dare say you deserve to be on this side of the fence, where the grass is greener."
            
        "He's a friend":
            $ renpy.block_rollback()
            l "He's just a friend... He was surprised to see me here, that's all."
            mr "Didn't you know he worked here?"
            $ flena = "sad"
            l "No..."
            mr "I see. Then it's not a very deep friendship."
    show seymour at truecenter
    show lena at rig3
    with move
    show robert at left
    with short
    r "Do you know what you'll be ordering tonight? I can make a recommendation..."
    mr "It's not needed. I know what we'll be having."
    "Seymour asked for the best dishes and the most expensive wine. It was clear he had good taste when it came to cuisine."
    "Robert couldn't stop looking at me from the corner of his eyes while taking our order."
    if seymour_restaurant:
        "He was even more surprised about this situation than I was."
    else:
        "Thankfully he kept his mouth shut and didn't expose my lie."
        "I had already committed to that story. It would be super weird and awkward for Seymour to discover I worked as a waitress there."
    $ flena = "n"
    hide robert
    with short
    show seymour at lef
    show lena at rig
    with move
    mr "So, Lena. I'm interested in knowing something."
    mr "What made you choose to become a model?"
    menu:
        "I'm not sure":
            $ renpy.block_rollback()
            l "I'm not entirely sure, to be honest."
            $ fseymour = "n"
            mr "You're not?"
            l "I had this friend who was already doing some modeling and she said I should try it..."
            l "So I thought, why not give it a try? See if I like it..."
            l "But I didn't have a clear purpose in mind..."
            mr "Purpose is everything. We are all driven by purpose."
            mr "The only difference resides in being conscious about that purpose or being ignorant about it."
            mr "Only the conscious are free."
        
        "The circumstances":
            $ renpy.block_rollback()
            l "It was due to the circumstances."
            mr "Everything is. But what matters is if you were a victim of the circumstances or you took advantage of them."
            l "Considering things, I'd say the latter."
            play sound "sfx/xp.mp3"
            show wits_up
            $ lena_wits_xp += 1
            call screen skillsup
            l "I needed some extra income and my friend was already doing some modeling. She asked me to try it too, and so I did."
            mr "You saw a chance and took it. The only real freedom we have."
        
        "My friend convinced me":
            $ renpy.block_rollback()
            l "I don't know if I \"chose\" it. My friend was already doing some modeling, and I was in need of some extra income..."
            l "She said I should give it a try and I did, since I trusted her and she seemed to be doing nicely."
            mr "Surrounding yourself with people that provide opportunity and knowing which advice to follow is important."
            l "I don't regret it, that's for sure."
            mr "I see. I like seeing you're one of those people who don't regret following their will."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ lena_charisma_xp += 1
            call screen skillsup
            mr "That's the only real freedom we have."
            
        "I found it appealing":
            $ renpy.block_rollback()
            $ flena = "smile"
            l "I found it appealing, to be honest."
            l "I mean, it was never my intention to become a model, but my friend was already doing it, and I was in need of some extra income..." 
            l "She told me I should try, and I liked the idea. Making beautiful art with my body in front of a camera..."
            play sound "sfx/xp.mp3"
            show lust_up
            $ lena_lust_xp += 1
            call screen skillsup
            l "It was kinda freeing. I liked it."
            mr "To be free means to have the power to do as you will."
            mr "There's nothing more appealing than that."
            
    $ flena = "sad"
    "Seymour Ward was an intelligent and insightful man to an almost overwhelming degree."
    "He had some well thought out commentary about almost every subject... And I was feeling quite scrutinized, too."
    "I tried to change the focus to him."
    $ flena = "n"
    l "Tell me, Mr. Ward, why are you so interested in model photography all of a sudden?"
    $ fseymour = "smile"
    mr "I already answered that question when we first met. Wasn't that enough?"
    l "You also said you were interested in the business side of it, and that you didn't want to bore us with that talk."
    mr "And I still don't want to bore you with it, ha ha. Let's just say I've been meeting quite a lot of people who work in this field."
    mr "Award-winning photographers, top tier models, but mostly business owners and entrepreneurs."
    mr "It's a world I haven't conquered yet and I was intrigued by it."
    l "I'm surprised by your interest in hiring me, considering what you just told me."
    l "It seems you have access to a lot of top-tier models you could choose from."
    l "I'm sure you can afford to pay them and they would be more than happy to work with you."
    mr "You're right, but once again you're missing the point."
    $ flena = "serious"
    "He had already said something like that before, and also at the art gallery..."
    "His self-sufficiency was a bit irritating."
    l "It seems I'm always missing something..."
    mr "I didn't want to sound patronizing. It's not a question of wits, but of perspective."
    mr "Some things can only be appreciated when you've risen enough to see the complete picture."
    $ flena = "n"
    l "And what part of the picture am I missing regarding this issue?"
    mr "A man who possesses as much gold as his heart desires ceases to appreciate its shine."
    mr "His eyes search for a rarer glint, a gem he has no possession of... yet."
    mr "What I mean is, being able to pick and choose any model I want, I'm only interested in working with one that really suits my taste."
    $ flena = "blush"
    mr "You could say I'm searching for the rare diamond hidden under this mountain of gold coins."
    "He had a way with words, that couldn't be denied..."
    $ flena = "n"
    "I didn't want him to think I was impressed, though. I decided to try a more aggressive approach, to see how he would react."
    l "So that's the reason behind this dinner? Testing me to see if I'm that diamond?"
    "My direct question didn't throw him off at all, as he responded with calm and confidence."
    mr "It's a rather blunt way to put it, but you're right."
    mr "I'm a beginner when it comes to photography, but not when it comes to art."
    mr "And I know art can't be found on the surface of things. A model has to be beautiful, yes..."
    mr "But what turns her body into art is the soul and the mind that inhabits it."
    mr "If I'm going to dabble in the art of photography, that's what I want to capture. And that's why I won't be satisfied with just a pretty face."
    mr "That's the reason I'm testing you like this. And so far it's looking very promising."
    "I didn't know if to feel praised or insulted by his unapologetic scrutiny. I decided to fire back with sarcasm."
    l "Nothing makes a girl feel more comfortable than knowing she's being evaluated at all times..."
    mr "Oh, come on. It's plain to see you've been testing me all night, too. We're here trying to assess and convince each other."
    $ flena = "worried"
    "He was right about that... And once again I felt he could see through me much easier than I could through him."
    "Even though he was talking a lot and didn't seem to be hiding anything, I couldn't shake off this sensation he had the upper hand at all times..."
    mr "This brings me to my next question. As I have just told you, I'm not only looking for a pretty face. I'm interested in a keen mind, too."
    mr "A rare quality in the often shallow world of modeling..."
    "Again, he was not wrong... But I didn't like the condescending way in which he talked about models."
    "I struck again with acid sarcasm, though he had already shown he was not fazed by that..."
    $ flena = "n"
    l "So you'll have me take a quiz to determine my IQ now?"
    mr "A number won't tell me what I want to know about you. What I want is to see what's your vision of the world."
    l "You want to know my political leaning?"
    mr "There's something that tells one's views on the world better than politics. And that's philosophy." 
    mr "So tell me, who would you say is your favorite philosopher?"
    mr "Whose thoughts have influenced you the most?"
    menu:
        "{image=icon_wits.png}Plato" if lena_wits > 1:
            $ renpy.block_rollback()
            l "I'd say it's Plato. I like his famous allegory of the cave."
            l "His insight into our perception and our ideas about the world..."
            mr "Ah, Plato, the great seed from which everything originated."
            mr "They were wise, back then. But did you know he hated artists?"
            mr "He thought poorly of physical representation and called artists liars."
            mr "He wouldn't approve of what we're doing, you and I."
            l "No one's perfect."
            
        "{image=icon_wits.png}Descartes" if lena_wits > 1:
            $ renpy.block_rollback()
            l "I'd say it's Descartes. I always liked the way he thought about the world, devoid of superstition."
            mr "Descartes, huh? A fierce rationalist. And an individualist."
            mr "\"{i}Cogito ergo sum{/i}\". He was wise to only trust in the power of the human mind... Of one's own mind."
            l "His defense of reason was very positive for the world. He's considered the father of modern science for a reason."
            mr "He wasn't fond of passion, though. He sought to control it, rather than embrace it."
        
        "{image=icon_wits.png}Nietzsche" if lena_wits > 2:
            $ renpy.block_rollback()
            $ say_niet = True
            l "I'd say Nietzsche."
            "His eyebrows arched up with slight interest."
            mr "Oh, so Nietzsche... Interesting."
            l "Only if for how edgy he is!"
            l "But honestly, he has some deep insights into the psychology of mankind."
            $ lena_seymour += 1
            play sound "sfx/friendup.mp3"
            show friend_up
            $ fseymour = "happy"
            mr "He's my favorite philosopher too, you know? Then again, he's almost everybody's favorite..."
            mr "But most people haven't even read him. They only know about the washed out pop-culture version sold to them."
            $ fseymour = "smile"
            mr "His true philosophy can't be enforced by those ignorants. They are but sheep, in fear of it."
            
        "{image=icon_wits.png}Marx" if lena_wits > 1:
            $ renpy.block_rollback()
            l "I'd say it's Karl Marx. Thanks to him another way of viewing the world and society was made possible."
            $ fseymour = "serious"
            "Seymour scoffed."
            $ lena_seymour -= 1
            play sound "sfx/frienddown.mp3"
            show friend_down
            mr "Oh, don't get me started on how shallow his materialistic views of the world are."
            l "I'd guessed a wealthy man such as yourself wouldn't be too fond of Marxism."
            mr "He's not wrong about how control over the means of production grants wealth and dominance."
            mr "But he fails to see that what makes that dominance possible is not the material, but the mind."
            $ fseymour = "n"
            mr "That's why giving power to weak-minded communists always ends up in chaos and disarray."
            
        "I follow my own philosophy":
            $ renpy.block_rollback()
            l "I just follow my own philosophy."
            "He chuckled."
            $ fseymour = "happy"
            mr "Such a bold claim!"
            mr "One has to be very mighty or very ignorant to proclaim such a thing."
            $ fseymour = "smile"
            mr "And no one becomes mighty while neglecting to learn from the great men who came before him or her."
            "Was that just an underhanded way of calling me ignorant?"
        
        "None comes to mind":
            $ renpy.block_rollback()
            l "Uh... None comes to mind, right now."
            $ fseymour = "n"
            mr "I see. Such a pity."
            mr "The wise never forgets about how important it is to learn from the great men who came before him."
            "I guess he was implying I wasn't."
            
        "Philosophy bores me":
            $ renpy.block_rollback()
            $ filo = False
            l "Honestly, talking about philosophy bores me a bit."
            $ fseymour = "n"
            mr "I see... That's too bad. And too common."
            play sound "sfx/frienddown.mp3"
            show friend_down
            $ lena_seymour -= 1
            mr "I shouldn't have been expecting that much. Let's move on then."
            
    if filo:
        if say_niet == False:
            mr "You know who's my favorite?"
            mr "Nietzsche."
            l "I see. A lot of people like him."
            $ fseymour = "n"
            mr "Oh, please. Most people haven't even read him. They only know about the washed out pop-culture version sold to them."
            mr "His true philosophy can't be enforced by those ignorants. They are but sheep, in fear of it."
        $ fseymour = "n"
        mr "Do you know about Nietzsche's Three Metamorphoses?"
        l "I recall learning about it in high school..."
        mr "Everyone of us exists in one of three stages in this life."
        mr "The first form is the Camel. These are your everyday people, who follow the current of the world blindly."
        mr "They are beasts of burden, carrying the weight that's imposed on them."
        mr "Some times, an exceptional Camel can transform himself into the Lion."
        mr "He seeks to break free from social constraints and to become the captain of his own ship."
        mr "The Lion wants to be set free to do what he really wants to do."
        mr "But in doing so, the Lion now faces a great challenge: he has to find and realize his true purpose. His calling."
        mr "Few can really handle this challenge without suffering, for only those who are fierce can become the Lion."
        mr "A Lion has to fight to succeed, or be consumed in failure."
        mr "So..."
        mr "Which one are you? Camel or Lion?"
        menu:
            "{image=icon_wits.png}I'm the Child" if lena_wits > 2:
                $ renpy.block_rollback()
                $ flena = "serious"
                "I looked him directly into the eye. I had the upper hand this time."
                "I was going to show him how he had been underestimating me."
                $ flena = "n"
                l "I'd pick the third option. The Child."
                $ fseymour = "surprise"
                mr "Oh."
                "He flinched."
                $ fseymour = "smile"
                "But quickly recovered."
                if say_niet == False:
                    $ lena_seymour += 1
                    play sound "sfx/friendup.mp3"
                    show friend_up
                mr "I see you're familiar with Nietzsche's allegory."
                mr "Of course, I already knew you were smarter than the average girl."
                $ fseymour = "evil"
                mr "That just makes you so much better."
                $ flena = "blush"
                "The way he smiled and said those words made me... shiver."
                "For a second I wondered what exactly lay behind those cold, gray eyes..."
                "And what did he mean with \"that just made me much better\"? Was he grading me or something?"
                $ seymour = "smile"
                mr "It's no small claim to proclaim oneself as the culmination of Nietzsche's Metamorphose, though."
                mr "Most Camels delude themselves into thinking they are Lions. Same with Lions who think themselves Children."
                mr "Though deep down, everybody knows the truth, even if they do not want to acknowledge it."
                $ fseymour = "n"
                $ flena = "n"
                mr "Everybody's a slave to the world around them. Only the Child is truly free."   
                mr "Well, Nietzsche called it \"the Child\", but I personally prefer referring to this archetype as \"the Master\"."
                
            "{image=icon_charisma.png}I'm the Lion!" if lena_charisma > 1:
                $ renpy.block_rollback()
                "I gave a confident answer."
                l "I'm the Lion."
                $ fseymour = "smile"
                "Seymour smiled at me. He looked... amused."
                mr "A bold claim, but Lions are indeed bold."
                mr "But under the pelt of many Lions lies a Camel, trying to disguise himself."
                mr "Some pelts are cheap, and the trick can be spotted at first glance."
                mr "Yours is pretty... luxurious."
                "Why did his compliment made me almost shiver?"
                "Was it the word? How he uttered it? Or what lay behind those cold, gray eyes?"
                l "Thanks."
                mr "It's a well deserved compliment."
                mr "Lions face one sad truth though. Or should I rather say, \"lie\"."
                mr "They believe themselves free, but they, too, are slaves, like Camels."
                $ fseymour = "n"
                mr "Slaves to others and to the world around them."
                mr "The only one who's truly free is the Child."
                mr "The third stage, the culmination of Nietzsche's Metamorphose."
                mr "He called it \"the Child\", but I personally prefer referring to this archetype as \"the Master\"."
                
            "I'm the Camel":
                $ renpy.block_rollback()
                l "I guess I'm the Camel."
                $ fseymour = "smile"
                "He smiled like he was pleasantly surprised."
                mr "Ah, so you accept the truth of this world!"
                mr "I'll be honest, I was expecting you to act out and proclaim you're the Lion."
                mr "It is what every camel does. They think themselves lions but are unable to recognize the skin they really wear."
                mr "But you are not blind to that, and accept it."
                l "You speak like being a camel is something shameful and undesirable."
                l "But you said it yourself: they shoulder others' burdens. That's why society can exist."
                l "A world full of Lions would eat itself up. It's only through helping others that life can persist."
                l "And the truest source of doing that for someone is Love."
                "He looked rather... amused."
                mr "Bravo! I knew you looked like an intelligent girl!"
                mr "That's some very nice insight, even though naive. That's the Camel's nature, after all."
                mr "But your wool shines gold."
                mr "You're clear on where you stand, and that's something very few people do. Something you and I have in common."
                l "You mentioned three metamorphoses."
                mr "Oh, yes. The Child."
                mr "The culmination of Nietzsche's Metamorphoses."
                $ fseymour = "n"
                mr "He called it \"the Child\", but I personally prefer referring to this archetype as \"the Master\"."
                
            "Why don't you tell me?":
                $ renpy.block_rollback()
                l "I don't know. Why don't you tell me?"
                mr "It's not for me to decide. It will be your actions which will define what you are."
                mr "You can still be a Camel or turn out to be a Lion... Though your lack of will to define yourself is telling."
                "Was he telling me I was a Camel? It seemed clear he had not too much respect for them..."
                l "What about that third metamorphose you mentioned?"
                mr "Oh, yes. The Child."
                mr "The culmination of Nietzsche's Metamorphoses."
                mr "He called it \"the Child\", but I personally prefer referring to this archetype as \"the Master\"."
                
        mr "The Master is the one who creates. The one who claims control over reality and shapes it to his will."
        mr "He is Will incarnated into a being. Very few people in this world can really claim to possess that kind of power."
        mr "And we tend to get together, as you may have heard."
        "That line made me clear he thought himself way above me."
        $ fseymour = "smile"
        mr "Anyways, I'm afraid I'm beginning to bore you with my verbiage."
        mr "You'll have to excuse me. It's not everyday one finds someone he can engage with in the pleasure of conversation."
        mr "We were discussing something I'm passionate about and I got carried away."
        l "It's OK... If anything, it makes for interesting conversation, that's for sure."
        mr "I'm glad you see it that way."
        if lena_seymour > 4:
            "I was rather impressed by his speech..."
        else:
            "Interesting, but not enjoyable..."
        "By now we had almost finished our dinner."
    $ flena = "n"
    $ fseymour = "n"
    "What followed was mostly polite conversation until we called it a night and left the restaurant."
    stop music fadeout 2.0
    scene streetnight
    with long
    show lena at rig
    show seymour2 at lef
    with short
    if lena_seymour > 5:
        $ fseymour = "happy"
        mr "I hope you enjoyed the dinner. I haven't enjoyed myself so much in quite a while."
        mr "I think you're exactly what I've been looking for."
        $ fseymour = "smile"
        mr "Let's do a photo-shoot next week."
    elif lena_seymour > 4:
        $ fseymour = "smile"
        mr "I hope you enjoyed the dinner. I certainly did."
        mr "I have the feeling you're what I'm looking for, after all."
        mr "Let's do a photo-shoot next week."
    elif lena_seymour > 3:
        mr "I hope you enjoyed the dinner."
        mr "I'm still not quite sure, but maybe you really are what I'm looking for..."
        mr "Let's do a photo-shoot next week and see how that goes."
    else:
        mr "I hope you enjoyed the dinner."
        mr "Though I'm not sure you're what I'm looking for, I've seen enough to want to give you another chance."
        mr "We can try to work together, do a photo-shoot next week and see how that goes."
    menu:
        "{image=icon_friend.png}Accept" if lena_seymour > 2:
            $ renpy.block_rollback()
            l "OK, let's do that."
            if lena_seymour < 5:
                $ lena_seymour += 1
                play sound "sfx/friendup.mp3"
                show friend_up
            mr "Good. I'll let you know the day and hour when I have it set up with the studio."
            l "Alright. I'll send you my rates then."
            mr "I'm looking forward to working with you."
            
        "{image=icon_mad.png}Refuse":
            $ renpy.block_rollback()
            $ v3_seymour_reject = True 
            if lena_seymour > 4:
                $ flena = "sad"
                l "I'm sorry, but I'll have to decline."
                $ fseymour = "serious"
                "It seemed he wasn't expecting that."
                mr "Decline? For what reason?"
                l "For the reason that I'm not really comfortable around you, Mr. Ward. I didn't mind the dinner, but I have no further desire to work with you."
            else:
                $ flena = "serious"
                l "That second chance won't be needed, since I'm not gonna take it."        
                $ fseymour = "serious"
            mr "Are you sure about that?"
            $ flena = "serious"
            l "Yes. I'm certain you're not what I'm looking for."  
            l "So you'll have to find another model to work with."
            $ lena_seymour = 2
            play sound "sfx/frienddown.mp3"
            show friend_down
            mr "You must think very highly of yourself if you believe that is a good judgment."
            l "I think highly enough of myself to not put up with people and situations that make me uncomfortable."
            l "I'm sorry Mr. Ward, but I'm not interested in doing business with you."
            mr "So be it."
            mr "Though I have the feeling you'll come to realize your mistake and you'll come back to me on your knees."
            l "Nice dream. Too bad it won't happen."
 
    "Two cars pulled up in front of us."
    mr "Oh, right in time."
    mr "The taxi will take you home. Good night, Lena."
    hide seymour2
    with short
    "He got into one of the taxis and closed the door behind him."
    "He even called a taxi for me..."
    if v3_seymour_reject:
        l "I don't live far. I do this walk everyday to get to work, I'm used to it."
        show lena at truecenter
        with move
        "I ignored the taxi and made my way back home on foot."
        "Seymour was the kind of man who doesn't like it when someone says no to them."
        "And I was the kind of girl who doesn't like it when she's stepped on."
    else:
        show lena at truecenter
        with move
        "I got into the car and gave instructions to get home."
        "I didn't live far away, but this was a welcome gesture."
        l "Mr. Seymour Ward..."
        "That dinner had been quite interesting... It felt like a subtle contest of verbal fencing."
        "And I had the feeling he liked it when I challenged him... He had fun with it."
        if lena_seymour > 4:
            "I found it interesting, too, if not fun. He was clearly a very intelligent man, and that piqued my curiosity."
            "I was looking forward to working with him..."
        else:
            "I had the feeling he didn't like to lose, though."
            "I was curious to see how our shooting would go..."
 
    jump master_script
    
label jiulessontime:
    scene gym
    show ian at lef
    show wen at rig
    with short
    wen "Come on, Ian! React! Try again!"
    jump jiulesson1
    
screen book_screen_2:
    
    imagebutton idle "card2_vengeance.png" hover "card2_vengeance_hover.png" focus_mask True action SetVariable("book_card1", "vengeance") , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "card2_callofduty.png" hover "card2_callofduty_hover.png" focus_mask True action SetVariable("book_card1", "call_of_duty")  , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    imagebutton idle "card2_chosenone.png" hover "card2_chosenone_hover.png" focus_mask True action SetVariable("book_card1", "chosen_one") , [ Play ("ch_one", "sfx/paper_click.mp3") ] , Return at fade_in_skill 
    
screen v3poolgame1:
    
    imagebutton idle "v3_pool_screen1.png"
    imagebutton idle "v3_poolball_a.png" hover "v3_poolshot1a_hover.png" focus_mask True action SetVariable("v1_hitball", v1_hitball+1) , [ Play ("ch_one", "sfx/cue.mp3") ] , Return at fade_in_skill 
    imagebutton idle "v3_poolball_b.png" hover "v3_poolshot1b_hover.png" focus_mask True action SetVariable("v1_hitball", v1_hitball+2) , [ Play ("ch_one", "sfx/cue.mp3") ] , Return at fade_in_skill 
    imagebutton idle "v3_poolball_c.png" hover "v3_poolshot1c_hover.png" focus_mask True action SetVariable("v1_hitball", v1_hitball+3) , [ Play ("ch_one", "sfx/cue.mp3") ] , Return at fade_in_skill 
    

screen v3poolgame2:
    
    imagebutton idle "v3_pool_screen2.png"
    imagebutton idle "v1_pool_screen1.png" hover "v1_pool_screen1_hover.png" focus_mask True action SetVariable("v1_hitball", v1_hitball+1) , [ Play ("ch_one", "sfx/cue.mp3") ] , Return at fade_in_skill 
    imagebutton idle "v1_pool_screen2.png" hover "v1_pool_screen2_hover.png" focus_mask True action SetVariable("v1_hitball", v1_hitball+2) , [ Play ("ch_one", "sfx/cue.mp3") ] , Return at fade_in_skill 
    imagebutton idle "v1_pool_screen3.png" hover "v1_pool_screen3_hover.png" focus_mask True action SetVariable("v1_hitball", v1_hitball+3) , [ Play ("ch_one", "sfx/cue.mp3") ] , Return at fade_in_skill 

