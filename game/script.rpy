                                                        
                                                                    ######################     OUR      RED     STRING  ######################
                                                                    
## CHARACTERS ########################################################################################################################                                                                    
define i = Character("Ian" , color="#B77D0A")
define l = Character("Lena" , color="#38317F")
define p = Character("Perry" , color="#B14B14")
define c = Character("Cindy" , color="#B0A000")
define w = Character("Wade" , color="#548212")
define h = Character("Holly" , color="#A978A7")
define a = Character("Alison" , color="#0FB286")
define j = Character("Jeremy" , color="#B51515")
define e = Character("Emma" , color="#B72E45")
define x = Character("Axel" , color="#2988C2")
define mr = Character("Mr. Ward" , color="#79A2D1")
define s = Character("Seymour" , color="#79A2D1")
define st = Character("Stan" , color="#426559")
define lo = Character("Louise" , color="#820628")
define v = Character("Ivy" , color="#8F0082")

define r = Character ("Robert", color="#425565")
define ch = Character ("Cherry", color="#BC215A")
define mi = Character("Minerva" , color="#503184")
define wen = Character("Wen" , color="#3E679E")
define ed = Character ("Ed", color="#DD7D0A")
define mo = Character ("Molly", color="#E46D93")
define lm = Character("Mom", color="#6064A7")
define ld = Character("Dad", color="#6064A7")
define dan = Character ("Danny", color="#7E8DA2")
define mayor = Character ("Mayor Vermeer", color="#8C5C0E")
define mwife = Character ("Mayor's wife", color="#B0833A")

define wai = Character("Waitress" , color="#38317F")
define drunk = Character("Drunk" , color="#425565")
define guy = Character("Guy" , color="#7E8DA2")
define girl = Character("Girl" , color="#7E8DA2")
define woman = Character("Woman" , color="#7E8DA2")
define man = Character("Man" , color="#7E8DA2")
define bum = Character("Bum" , color="#7E8DA2")
define bo = Character("Bouncer" , color="#2E2927")
define yuri = Character("Yuri" , color="#B4360A")
define ic = Character ("{color=#B77D0A}Ian{/color} + {color=#B0A000}Cindy{/color}")
define ip = Character ("{color=#B77D0A}Ian{/color} + {color=#B14B14}Perry{/color}")
define pw = Character ("{color=#B14B14}Perry{/color} + {color=#548212}Wade{/color}")

## v0.1 ################################################################################################################################################################################################################################################
## v0.1 ################################################################################################################################################################################################################################################
## v0.1 ################################################################################################################################################################################################################################################

label start:
    $ _game_menu_screen = None

### DEFAULT VARIABLES ########################################
    
# IAN
    $ ian_active = True
    
#stats    
    $ ian_wits = 0
    $ ian_charisma = 0
    $ ian_athletics = 0
    $ ian_lust = 0
    $ ian_will = 0     
    $ ian_money = 1
    $ ian_wits_xp = 2
    $ ian_charisma_xp = 2
    $ ian_athletics_xp = 2
    $ ian_lust_xp = 2
    $ ian_will_xp = 0  
# job
    $ ian_job_magazine = 2
    $ ian_stipend = 1
    $ ian_owed_money = 0
    $ ian_live_perry = True
# relationships    
    $ ian_perry = 5
    $ ian_lena = 3
    $ ian_cindy = 3
    $ ian_wade = 5
    $ ian_alison = 5
    $ ian_holly = 5
    $ ian_jeremy = 6
    $ ian_emma = 5
    $ ian_louise = 3
    $ ian_ivy = 3
    $ ian_axel = 3
    $ ian_seymour = 3
    $ ian_stan = 3
    
    $ ian_default = 4
    $ ian_minerva = 4
    $ ian_wen = 4
    $ ian_robert = 3
    $ ian_mark = 0
    $ ian_cherry = 3
    $ ian_lola = 3
    
# agenda
    $ ian_agenda = False
    $ ian_perry_agenda = False
    $ ian_lena_agenda = False
    $ ian_cindy_agenda = False
    $ ian_wade_agenda = False
    $ ian_alison_agenda = False
    $ ian_holly_agenda = False
    $ ian_jeremy_agenda = False
    $ ian_emma_agenda = False
    $ ian_louise_agenda = False
    $ ian_ivy_agenda = False
    $ ian_axel_agenda = False
    $ ian_seymour_agenda = False
    $ ian_stan_agenda = False
    $ ian_minerva_agenda = False
    $ ian_wen_agenda = False
    $ ian_robert_agenda = False
    $ ian_mark_agenda = False
    $ ian_ed_agenda = False
    $ ian_molly_agenda = False
    $ ian_danny_agenda = False
    $ ian_lenamom_agenda = False
    $ ian_lenadad_agenda = False
    $ ian_cherry_agenda = False
    $ ian_producer_agenda = False
    $ ian_lola_agenda = False
    
# LENA
    $ lena_active = False
    
#stats    
    $ lena_wits = 1
    $ lena_charisma = 1
    $ lena_athletics = 1
    $ lena_lust = 1
    $ lena_will = 1     
    $ lena_money = 0
    
    $ lena_wits_xp = 0
    $ lena_charisma_xp = 0
    $ lena_athletics_xp = 0
    $ lena_lust_xp = 0
    $ lena_will_xp = 0   
# job
    $ lena_job_cafe = 2
    $ lena_job_restaurant = 2
    $ lena_owed_money = 0
    $ lena_live_stan_louise = True
    $ lena_money_family = 0
# relationships    
    $ lena_perry = 5
    $ lena_cindy = 3
    $ lena_wade = 3
    $ lena_alison = 3
    $ lena_holly = 4
    $ lena_jeremy = 3
    $ lena_emma = 4
    $ lena_louise = 5
    $ lena_ivy = 6
    $ lena_axel = 0
    $ lena_seymour = 4
    $ lena_stan = 3
    
    $ lena_default = 4
    $ lena_ed = 4
    $ lena_molly = 8
    $ lena_robert = 4
    $ lena_mark = 4
    $ lena_danny = 5
    $ lena_lenamom = 4
    $ lena_lenadad = 6
    $ lena_cherry = 0
    $ lena_producer = 0
    $ lena_lola = 10
# agenda
    $ lena_agenda = False
    $ lena_perry_agenda = False
    $ lena_ian_agenda = False
    $ lena_cindy_agenda = False
    $ lena_wade_agenda = False
    $ lena_alison_agenda = False
    $ lena_holly_agenda = False
    $ lena_jeremy_agenda = False
    $ lena_emma_agenda = False
    $ lena_louise_agenda = False
    $ lena_ivy_agenda = False
    $ lena_axel_agenda = False
    $ lena_seymour_agenda = False
    $ lena_stan_agenda = False
    
    $ lena_minerva_agenda = False
    $ lena_wen_agenda = False
    $ lena_robert_agenda = False
    $ lena_mark_agenda = False
    $ lena_ed_agenda = False
    $ lena_molly_agenda = False
    $ lena_danny_agenda = False
    $ lena_lenamom_agenda = False
    $ lena_lenadad_agenda = False
    $ lena_cherry_agenda = False
    $ lena_producer_agenda = False
    $ lena_lola_agenda = False
# status
    $ chapter = 0
    $ day = "Thursday"
    $ week = 1
    $ month = "April"
    
### v0.1 FLAGS ########################################
    $ tutorial_menu = False
    $ tutorial1 = False
    $ tutorial2 = False
    $ tutorial3 = False
    $ prologueover = False
    $ april = True
    
    $ v1_answer_cafe1 = False
    $ v1_answer_cafe2 = False
    $ v1_answer_cafe3 = False
    $ v1_answer_cafe4 = False
    $ v1_answer_cafe5 = False
    $ v1_answer_cafe6 = False
    $ v1_name_charisma = False
    $ v1_name_wits = False
    $ save_name = "Ian: Prologue"
    
#######################################################

    show blackbg
    with long
    $ quick_menu = False
    $ _game_menu_screen = "tutorialquit"
    menu:
        "Do you want to play the tutorial?"
        "Enable tutorial":
            $ renpy.block_rollback()
            $ tutorial_menu = True
            $ tutorial1 = True
            $ tutorial2 = True
            $ tutorial3 = True
            show tutorial_0
            with short
            pause 4
            hide tutorial_0
            with long
            jump define_sprites

            
        "Skip":
            $ renpy.block_rollback()
            show screen ui
            $ _game_menu_screen = "phone"
            $ quick_menu = True
            jump define_sprites
            
        "Cheat mode":
            $ renpy.block_rollback()
            "You will start the game with 10 points in every stat. Do you want to play with the cheat mode active?"
            menu:
                "Yes, let's cheat": 
                    $ renpy.block_rollback()
                    $ lena_wits = 10
                    $ lena_charisma = 10
                    $ lena_athletics = 10
                    $ lena_lust = 10
                    $ lena_will = 10     
                    $ lena_money = 10
                    $ ian_wits = 10
                    $ ian_charisma = 10
                    $ ian_athletics =10
                    $ ian_lust = 10
                    $ ian_will = 10     
                    $ ian_money = 10
                    $ ian_wits_xp = 0
                    $ ian_charisma_xp = 0
                    $ ian_athletics_xp = 0
                    $ ian_lust_xp = 0
                    play sound "sfx/willup.mp3"
                    "Cheats activated {image=icon_wits.png}{image=icon_charisma.png}{image=icon_athletics.png}{image=icon_lust.png}{image=icon_will.png}{image=icon_money.png}"
                    
                "No, let's play the game":
                    $ renpy.block_rollback()
                    
            show screen ui
            $ _game_menu_screen = "phone"
            $ quick_menu = True
            jump define_sprites
    pause (0.5)
    
    
    
label prologue:
    
    with long
    stop music fadeout 2.0
    scene cafe
    with long
    pause 1
    "..."
    "*{i}Sigh...{/i}*"
    play music "music/flirty.mp3" loop
    show v1_iancafe 
    with short
    i "I'm really not feeling it today."
    "I looked at the blank page on the screen of my laptop. My fingers hovered over the keyboard."
    "I had no idea of what to write."
    i "Ahhh...!"
    "I let out another sigh of frustration and dragged my hand over my face."
    i "I give up."
    "I picked up the book that was lying on the table and flipped through its pages again."
    i "..."
    "There was nothing of value that I had missed in those highlighted paragraphs."
    i "Man, I hate this book."
    scene cafe 
    show v1_book 
    with short
    i "\"Fangs on my neck\"..."
    i "What a pile of shit."
    "There were so many interesting books out there. Why the hell did it fall to me to review this one?"
    "It was one of those clichéd vampire teenager romance stories. When would people get tired of those?"
    "That's how unimaginative writers, readers and publishers had become."
    scene cafe 
    show v1_iancafe 
    with short
    "I threw the book on the table and looked at the screen again."
    i "Do they really want me to write something positive about this flimsy excuse for a book?"
    "Once again, I had to find a way to lie and praise what I thought was crap."
    wai "Do you want anything else?"
    i "Huh?"
    scene cafe
    show lenawork
    with short
    "I snapped out of my sullen thoughts and turned my head."
    "The waitress was looking at me with a hearty smile, waiting for my response."
    pause (0.5)
    "She was so damn cute."
    show lenawork at rig
    with move
    show ian at lef
    with short
    i "Oh, sorry, yeah. Another latte, please."
    "I was going to need it."
    wai "Coming right away."
    hide lenawork
    with short
    "She picked up my used cup and walked away."
    scene cafe
    show v1_iancafe2
    with short
    "I followed her with my stare."
    "I had noticed her before. {w=1}Of course I had."
    "I came to this café to work and write sometimes, when I couldn't concentrate at home."
    "I had only seen her recently though, so I supposed she was a new employee."
    "And boy, was she a beauty..."
    "Another good reason to get out of home and come to this café."
    scene cafe
    show v1_iancafe 
    with short
    "I turned my attention back to my blank review. I really had no energy to write about it."
    i "Come on... Push through."
    "I focused my eyes and my mind, fingers ready to type."
    play sound "sfx/keyboard.mp3"
    "\"Fangs on my Neck is the latest book of the reputed Alana McDollinger, a writer that has managed to captivate the hearts and minds of tens of thousands of teenage readers with her vivid pages...\""
    scene cafe
    show ian at lef
    show lenawork at rig
    with short
    wai "Here you go."
    i "Oh."
    "I felt my focus drain through my fingers as I diverted my attention back to the waitress."
    i "Yeah, thanks."
    i "..."
    "What small wind I'd had on my back deflated."
    "Back to the starting square..."
    "As I was about to try and focus again, I noticed the waitress lingering a bit longer next to my table."
    "I looked at her, and she at me."
    $ flena = "smile"
    wai "\"Fangs on my Neck\". Is it good?"
    "She had a funny smile on her face, like she found it kind of hilarious."
    menu:
        "It's not the kind of book I like!":
            $ renpy.block_rollback()
            $ v1_answer_cafe1 = True
            $ fian = "surprise"
            i "Oh, no, it's not the kind of book I usually read!"
            $ fian = "insecure"
            i "I mean, it's not something I read because I like it."
            $ flena = "happy"
            "She chuckled and I felt like I had just made a fool of myself."
            wai "That's funny."
            wai "I've met a lot of people that hate to read. But not someone yet who reads something he actively hates."
            i "Believe me, I wouldn't read this if I could afford not to."
            $ flena = "n"
            wai "So you have a reason to force yourself?"
        
        "It's terrible":
            $ renpy.block_rollback()
            $ v1_answer_cafe2 = True
            i "Well... It's terrible."
            $ lena = "happy"
            "She chuckled and her smile got a bit wider."
            $ fian = "smile"
            "Not because I wanted to, but mine also did."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            if tutorial2:
                $ tutorial2 = False
                call screen tutorial2screen
            label v1_ans2:
                wai "I used to read these kind of books when I was, like, twelve or thirteen. But I see they have an older audience, too."
                "She was teasing me openly. I kept the playful tone."
                i "Please, don't be mistaken. I'm not reading this for my enjoyment!"
                wai "You're not? What brings you to put yourself through such torture, then?"
            
        "It's... passable":
            $ renpy.block_rollback()
            $ v1_answer_cafe3 = True
            $ fian = "worried"
            i "Euh, it's, eh... Passable."
            $ flena = "happy"
            "Her smile got a bit wider, like she was very amused."
            wai "Passable, huh... Do you recommend it to me, then?"
            "I had the impression she was... kind of playing with me or something?"
            "I decided to drop the politically correct act and play along."
            $ fian = "smile"
            i "It depends. Do you like poorly written stories that pander to a demographic too young to spot a cliché when they see it?"
            wai "I don't think so."
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            if tutorial2:
                $ tutorial2 = False
                call screen tutorial2screen
            label v1_ans3:
                i "Well, then this book will surely disappoint you."
                $ flena = "happy"
                wai "That's not a very good recommendation."
                $ fian = "worried"
                i "*{i}Sigh{/i}*... Yeah, I know. I guess I'm not very good at my job."
                $ flena = "n"
                wai "What job?"  
                $ fian = "n"
    
    i "I'm doing an internship at a literature magazine, writing reviews on books and stuff."
    wai "Really? That sounds cool."
    i "Not cool at all... I don't get to choose what to review."
    i "And the things I have to read... Well, don't get me started on those."
    wai "Those reviews must be worth the read, ha ha."
    $ fian = "sad"
    i "If only...!"
    i "If I wrote what I really thought, they would fire me in a week."
    i "They don't want a review, they just want me to write propaganda so the book sells and the publishers are happy."
    $ flena = "n"
    wai "That's pretty sad."
    menu:
        "I'm fed up!":
            $ renpy.block_rollback()
            $ v1_answer_cafe4 = True
            $ fian = "serious"
            i "I'm really fed up with it, to be honest."
            i "They've turned me into an ill-paid salesman."
            wai "Damn, that's... tough."
            wai "The book industry can be very frustrating! Good luck with that!"
            $ fian = "worried"
            i "Sure, thanks..."
            "She smiled, turned around and went to take care of another table."
            $ fian = "n"
            
        "Sorry, I didn't intend to vent":
            $ renpy.block_rollback()
            $ v1_answer_cafe5 = True
            $ fian ="n"
            i "It's pretty boring, rather than sad... Anyways, sorry. I didn't intend to vent."
            play sound "sfx/xp.mp3"
            show charisma_up
            $ ian_charisma_xp += 1
            call screen skillsup
            if tutorial2:
                $ tutorial2 = False
                call screen tutorial2screen
            label v1_ans5:
                "I supposed the waitress wouldn't want to hear my problems."
                "She was working and I was probably keeping her."
                $ flena = "serious"
                wai "No, I think it's really sad."
                wai "And not only where books are concerned. In music, too."
                wai "Publishers are hurting new voices and real artists by flooding the market with easy-to-sell crap."
                wai "All they care about is making money, art be damned."
                "Her comment left me a bit perplexed."
                "I wasn't expecting a random waitress to have an opinion on that subject."
                i "Yeah, it's a real curse..."
                $ flena = "shy"
                wai "Sorry, I got a bit carried away, ha ha..."
                $ flena = "smile"
                wai "Seems like we see eye to eye on this!"
                "She took a quick look over her shoulder."
                wai "Well, duty calls. I have work to do."
                "She pointed at my computer."
                wai "Good luck with that!"
                i "Sure, thanks!"    
            
        "Explain how the industry works":
            $ renpy.block_rollback()
            $ v1_answer_cafe6 = True
            $ fian = "n"
            i "This is how the industry works, you know?"
            i "Publishers only want to make money."
            i "They get a big name author to write about what's popular in pop culture..."
            i "And then they pay the magazines underhand to write good reviews that act as good publicity."
            play sound "sfx/xp.mp3"
            show wits_up
            $ ian_wits_xp += 1
            call screen skillsup
            if tutorial2:
                $ tutorial2 = False
                call screen tutorial2screen
            label v1_ans6:
                $ flena = "serious"
                wai "I see! It's the same as with the music industry."
                wai "They push out the most commercial, soul-less and simple-minded products possible!"
                wai "As you said, all they care about is making money, art be damned."
                wai "Publishers are hurting new voices and real artists by flooding the market with easy-to-sell crap."
                "Her comment left me a bit perplexed."
                "I wasn't expecting a random waitress to have an opinion on that subject."
                i "Yeah, it's a real curse..."
                $ flena = "shy"
                wai "Sorry, I got a bit carried away, ha ha..."
                $ flena = "smile"
                wai "Seems like we see eye to eye on this!"
                "She took a quick look over her shoulder."
                wai "Well, duty calls. I have work to do."
                "She pointed at my computer."
                wai "Good luck with that!"
                i "Sure, thanks!"    
    
    hide lenawork
    with short
    $ fian = "n"
    show ian at truecenter
    with move
    "The conversation we had just had lingered in my mind as I watched her return to work."
    "It was a rare occurrence getting the chance to chat with such a cute girl."
    "And it had been her who initiated the exchange, hadn't it?"
    "I was trying to remember what exactly had prompted the conversation..."
    $ fian = "serious"
    i "No, no. Focus."
    "I shook my head and tried to get back to the work at hand."
    scene cafe
    with long
    play sound "sfx/keyboard.mp3"
    pause (1)
    show v1_iancafe
    with short
    $ fian = "n"
    i "Whew..."
    i "Finally."
    "After two more lattes and a lot of head scratching, I had managed to finish the review."
    i "It shouldn't take so much time to write these... I'm not inspired lately."
    "I packed my stuff, got up, stretched my back and walked to the counter to pay the bill."
    $ flena = "n"
    scene cafe
    show ian at lef
    show lenawork at rig
    with short
    i "How much is it?"
    wai "Ten dollars and fifty cents."
    menu:
        "Here you go":
            $ renpy.block_rollback()
            i "Sure, here you go..."
            "I opened my wallet and gave her the money."
            wai "Thank you very much."
            i "No, thank you."
            wai "Hope to see you again!"
            i "I will come some other time, yeah."
            i "Bye."
            
        "{image=icon_wits.png}Those are some expensive lattes" if ian_wits > 0:
            $ renpy.block_rollback()
            $ v1_name_wits = True
            "I handed her the money."
            i "Well, those are some expensive lattes."
            $ flena = "smile"
            wai "Ha ha, blame yourself for liking fancy stuff."
            $ fian = "smile"
            i "Our economy's so bad that now a simple latte is considered fancy?"
            $ flena = "happy"
            "I had caught on the game she was trying to play with me before, and I decided to try myself this time."
            "She smiled before voicing her comeback."
            wai "If they are prepared with as much care and love as the ones I make, yes."
            i "So that's why today's lattes tasted better than usual."
            wai "Come on, now you're just messing with me."
            i "Ha ha, yes, I definitely am."
            wai "My name's Lena, by the way."
            "I wasn't expecting her to introduce herself all of a sudden."
            "She was giving me her name without me even asking it!"
            i "Oh. I'm Ian. Nice to make your acquaintance."
            l "So formal, ha ha."
            l "Nice to meet you too. I guess I'll be seeing you around?"
            i "Yeah, I come to this café from time to time."
            l "Till next time, then!"
            
        "{image=icon_charisma.png}My name's Ian, by the way" if ian_charisma > 0:
            $ renpy.block_rollback()
            $ v1_name_charisma = True
            "I handed her the money."
            $ fian = "smile"
            i "Here you go. My name's Ian, by the way."
            "I didn't know why I introduced myself."
            "I surprised myself, but it felt just... natural to do so."
            wai "Oh." 
            "She seemed a bit surprised that I introduced myself all of a sudden, but quickly got over it."
            $ flena = "smile"
            wai "I'm Lena, nice to meet you."
            "I had wanted to know her name, and she had just given it to me."
            i "Cool. The coffee was good, but I liked the conversation just as much."
            $ flena = "happy"
            "She smiled at me, a smile that seemed somewhat more sincere than the ones I had seen from her before."
            l "Better than the book you had to read, that's for sure!"
            $ fian = "happy"
            i "That's not hard to achieve at all, ha ha."
            i "Well, Lena, I guess I'll see you around then."
            l "I'll be here."
            i "See you!"
            
    stop music fadeout 2.0        
    scene v1_title    
    with short
    "I stepped out of the café and walked down the street, heading back home."
    if v1_name_wits:
        i "\"Nice to make your acquaintance\"? How much of a nerd can you be, Ian?"
        i "..."
        i "Lena..."
        i "So that's her name."
        "Pushing myself to write that review had made for a miserable afternoon, but I felt like something of value had come out of it."
        i "Normally you don't give your name to people that don't ask for it." 
        i "Even less if it's a random customer..."
        i "Could it be that she found me interesting?"
        i "Lena. What an interesting girl."
    elif v1_name_charisma:
        i "Lena..."
        i "So that's her name."
        "Pushing myself to write that review had made for a miserable afternoon, but I felt like something of value had come out of it."
        "I was amazed I had had the courage to approach such a beautiful girl out of the blue."
        i "That went really smoothly..."
        i "I'd say she was really enjoying talking to me."
        i "Lena. What an interesting girl."
    else:
        i "Shit, shit, shit... I'm an idiot."
        i "I should've asked her name."
        "After she made conversation with me I just paid the bill and treated her like I was just another random customer..."
        "Well, I guess that's exactly what I am."
        "That was just some small talk, there's no point in thinking she might've been interested in me."
        "Still..."
        i "Next time."
        i "I'll ask her name next time."
    hide v1_title
    $ renpy.movie_cutscene("intro_movie.mov")
    show fade
    
    jump master_script
    
label tutorial_diverge:
    if prologueover:
        jump chapterone
    elif v1_answer_cafe2:
        jump v1_ans2
    elif v1_answer_cafe3:
        jump v1_ans3
    elif v1_answer_cafe5:
        jump v1_ans5
    elif v1_answer_cafe6:
        jump v1_ans6
        
    
  
    
## END ################################################################################################################################################################################################################################################
## END ################################################################################################################################################################################################################################################
## END ################################################################################################################################################################################################################################################
label end:
    scene fade with long
    call screen tobecontinuedscreen
        
    return

screen tobecontinuedscreen:
    imagebutton idle "gui/tobecontinued.png" action Null, Return at fade_in_skill