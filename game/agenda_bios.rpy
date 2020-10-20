style bio:
    xpos 1300
    ypos 250
    xmaximum 450
    box_wrap True
    
style agenda:
    xpos 0.056 
    ypos 0.24
    ymaximum 655
    box_wrap True
    
style budget_income:
    xpos 0.056 
    ypos 0.34
    size 30
    ymaximum 655
    box_wrap True
    
style budget_expenses:
    xpos 0.056 
    ypos 0.59
    size 30
    ymaximum 655
    box_wrap True
    
## IAN ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_ian:
    tag agenda_screen
    imagebutton idle "gui/bio_ian.png"
    if lena_active:
        bar:
            value ian_lena
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_lena < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif chapter > 3 and ian_lena_sex:
            imagebutton idle "gui/thumb_love.png" xpos 1470 ypos 753
        elif ian_lena < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    else:
        imagebutton idle "gui/block_bio.png"
    hbox:
        style "bio"
        if chapter > 3 and ian_lena_sex:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Ian is a struggling writer wannabe. He studied literature and journalism, but he's far from achieving his dream of publishing a book and he's starting to wonder if that will ever happen. He barely gets by doing book reviews as an intern at a magazine, so the only way he could afford to move out of his parents' house was to go live with his friend Perry. His love life is a mess, too. He broke up with his four-year-long girlfriend a year ago, and it still weighs heavy on him. \nAfter meeting Ian and hanging out several times, they couldn't deny the strong attraction they felt for each other and finally slept together. Still, they both feel it's too early to define their relationship...{/size}"   
        else:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Ian is a struggling writer wannabe. He studied literature and journalism, but he's far from achieving his dream of publishing a book and he's starting to wonder if that will ever happen. He barely gets by doing book reviews as an intern at a magazine, so the only way he could afford to move out of his parents' house was to go live with his friend Perry. His love life is a mess, too. He broke up with his four-year-long girlfriend a year ago, and it still weighs heavy on him.{/size}"   


## LENA ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_lena:
    tag agenda_screen
    imagebutton idle "gui/bio_lena.png"
    if ian_active:
        bar:
            value ian_lena
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_lena < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif chapter > 3 and ian_lena_sex:
            imagebutton idle "gui/thumb_love.png" xpos 1470 ypos 753
        elif ian_lena < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    else:
        imagebutton idle "gui/block_bio.png"
    hbox:
        style "bio"
        if chapter > 3 and ian_lena_sex:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Lena is no ordinary girl. She might be beautiful, but there's a lot more under the surface. Hard-working, passionate and intelligent, she has never had it easy, having to struggle to get ahead most of the time. She had to stop studying to support herself and her humble family, and her emotional life has been tough, too. After having ended a toxic relationship with her ex-boyfrend, Axel, she's trying to find purpose and meaning in her life again. \nAfter meeting Ian and hanging out several times, they couldn't deny the strong attraction they felt for each other and finally slept together. Still, they both feel it's too early to define their relationship...{/size}"   
        else:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Lena is no ordinary girl. She might be beautiful, but there's a lot more under the surface. Hard-working, passionate and intelligent, she has never had it easy, having to struggle to get ahead most of the time. She had to stop studying to support herself and her humble family, and her emotional life has been tough, too. After having ended a toxic relationship with her ex-boyfrend, Axel, she's trying to find purpose and meaning in her life again.{/size}"   

    
## ALISON ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_alison:
    tag agenda_screen
    imagebutton idle "gui/bio_alison.png"
    if ian_active:
        bar:
            value ian_alison
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if chapter > 1 and ian_alison_sex:
            imagebutton idle "gui/thumb_love.png" xpos 1470 ypos 753
        elif ian_alison < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_alison < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_alison
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_alison < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_alison < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        if chapter > 2 and ian_alison_sex and alison_jeremy:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Alison was another of Ian's classmates during high school. Though she has her own group of friends, her and Ian had a very good relationship. After high school, Alison focused on her Civil Engineering studies and her and Ian grew distant, even though they kept in touch occasionally. Even though she's a beautiful and intelligent woman, she seems to be going through a though break. She recently lost her job and broke off her three-year realtionship with her boyfriend... \nIan couldn't keep ignoring the sexual tension between him and Alison, and they ended up having sex. Alison doesn't seem to be looking for a serious relationship, though, since she also slept with Jeremy... {/size}"   
        elif chapter > 2 and ian_alison_sex:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Alison was another of Ian's classmates during high school. Though she has her own group of friends, her and Ian had a very good relationship. After high school, Alison focused on her Civil Engineering studies and her and Ian grew distant, even though they kept in touch occasionally. Even though she's a beautiful and intelligent woman, she seems to be going through a though break. She recently lost her job and broke off her three-year realtionship with her boyfriend... \nIan couldn't keep ignoring the sexual tension between him and Alison, and they ended up having sex. Alison doesn't seem to be looking for a serious relationship, though... {/size}"   
        elif chapter > 2 and alison_jeremy:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Alison was another of Ian's classmates during high school. Though she has her own group of friends, her and Ian had a very good relationship. After high school, Alison focused on her Civil Engineering studies and her and Ian grew distant, even though they kept in touch occasionally. Even though she's a beautiful and intelligent woman, she seems to be going through a though break. She recently lost her job and broke off her three-year realtionship with her boyfriend... \nShe and Jeremy hooked up and are now seeing each other. {/size}"   
        
        else:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Alison was another of Ian's classmates during high school. Though she has her own group of friends, her and Ian had a very good relationship. After high school, Alison focused on her Civil Engineering studies and her and Ian grew distant, even though they kept in touch occasionally. Even though she's a beautiful and intelligent woman, she seems to be going through a though break. She recently lost her job and broke off her three-year realtionship with her boyfriend... {/size}"   


## AXEL ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_axel:
    tag agenda_screen
    imagebutton idle "gui/bio_axel.png"
    if ian_active:
        bar:
            value ian_axel
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_axel < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_axel < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_axel
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_axel < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_axel < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        if lena_active:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Axel is Lena's ex-boyfriend. They met through Ivy and both of them got Lena into the modelling world. He makes a living both as a model and photographer, though he claims to be more interested in being behind a camera rather than in front of one. His magnetic and dominant personality has granted him a lot of success, but that doesn't seem to be enough to make him happy.{/size}"   
        elif ian_active:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Axel is a professional photographer Cindy met one night at a bar. He seems very confident and no wonder why: he's tall, handsome and charming. One could say he's the kind of guy who gets everything he wants served on a silver plate...{/size}"
                  
## CINDY ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_cindy:
    tag agenda_screen
    imagebutton idle "gui/bio_cindy.png"
    if ian_active:
        bar:
            value ian_cindy
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_cindy < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_cindy < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_cindy
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_cindy < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_cindy < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Cindy is Wade’s girlfriend. They met in college and have been dating for about three years. Cindy is a beautiful, charming and cheerful girl, always full of energy, but she has a temper and always wants things to go her way, and she’s used to get what she wants.{/size}"

        
## EMMA ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_emma:
    tag agenda_screen
    imagebutton idle "gui/bio_emma.png"
    if ian_active:
        bar:
            value ian_emma
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if chapter > 4 and ian_emma_sex:
            imagebutton idle "gui/thumb_love.png" xpos 1470 ypos 753
        elif ian_emma < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_emma < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_emma
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_emma < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_emma < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        if chapter > 4 and ian_emma_sex:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Emma is one of the most easy-going human beings one can meet. She's a free soul and she wanders through life like a leaf moved by the wind, always with a smile and positive attitude, open to experience what the world has to offer. Even though she was a couple of years younger than Ian and Perry, she played in a band with them while they were in highschool and they have been friends ever since. She's always moving and making new friends, so it can be hard to see her sometimes, much to Perry's discontent. \nDuring a night out at the club, Ian realized Emma was interested in something more than plain friendship. After dancing and flirting they ended up at Ian's place, where they had an intense night of sex. If Perry only knew...!{/size}"

        else:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Emma is one of the most easy-going human beings one can meet. She's a free soul and she wanders through life like a leaf moved by the wind, always with a smile and positive attitude, open to experience what the world has to offer. Even though she was a couple of years younger than Ian and Perry, she played in a band with them while they were in highschool and they have been friends ever since. She's always moving and making new friends, so it can be hard to see her sometimes, much to Perry's discontent.{/size}"

## HOLLY ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_holly:
    tag agenda_screen
    imagebutton idle "gui/bio_holly.png"
    if ian_active:
        bar:
            value ian_holly
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_holly < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_holly < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_holly
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_holly < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_holly < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Though young, Holly is quite a successful writer. For as long as she can remember, she was the kind of girl who enjoyed living between the pages of a book rather than going to parties and doing all that extrovert stuff. Her books are now gaining quite a following, so she combines her job as a professional writer with an internship to finally earn her college degree. Despite her devoted fanbase, she still can't believe her books are appreciated and she often acts insecurely around other people, feeling afraid of leaving her shell.{/size}"   



## IVY ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_ivy:
    tag agenda_screen
    imagebutton idle "gui/bio_ivy.png"
    if ian_active:
        bar:
            value ian_ivy
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_ivy < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_ivy < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_ivy
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_ivy < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_ivy < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Ivy is Lena's closest friend and the only one she still keeps from her high school years. Ivy has always been a whirlwind, passionate, adventurous and quite brash, but also fun and loyal. It was Ivy who introduced Lena to the modelling world and to Axel. She's an incredibly sexy girl and she has never shyed away from it, quite the contrary, using for her benefit and making a living off her looks. She loves dancing, partying, flirting and meeting new people, and she there's always something crazy going on wit her.{/size}"   

## JEREMY ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_jeremy:
    tag agenda_screen
    imagebutton idle "gui/bio_jeremy.png"
    if ian_active:
        bar:
            value ian_jeremy
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_jeremy < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_jeremy < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_jeremy
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_jeremy < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_jeremy < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Ian has known Jeremy for a very long time. They used to be friend when they were kids and even took karate lessons together after school for a few years. Their paths diverged after high school, until they met each other again at the local gym. Jeremy has changed quite a lot after all these years. He's a confident and easy-going guy who loves to go out, party and flirt with the ladies.{/size}"

## LOUISE ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_louise:
    tag agenda_screen
    imagebutton idle "gui/bio_louise.png"
    if ian_active:
        bar:
            value ian_louise
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_louise < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_louise < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_louise
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if chapter > 4 and lena_louise_sex:
            imagebutton idle "gui/thumb_love.png" xpos 1470 ypos 753
        elif lena_louise < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_louise < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        if chapter > 4:
            if lena_louise_sex:
                text "{font=big_noodle_titling_oblique.ttf}{size=23}Louise and Lena met at college and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with, since she's not the most out-going person. In fact, she tends to be moody and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her she's a nice, sensitive girl and a loyal friend. \nTurns out her mysterious boyfriend was Jeremy, Ian's friend. However, he was playing the field and being unfaithful to Louise. Lena told her about it, but she didn't believe it... Until she saw it with her own eyes. Seeking solace in her friend, Louise made a move on Lena and both girls shared a night of sapphic passion together.{/size}"
            elif louise_jeremy == False:
                text "{font=big_noodle_titling_oblique.ttf}{size=23}Louise and Lena met at college and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with, since she's not the most out-going person. In fact, she tends to be moody and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her she's a nice, sensitive girl and a loyal friend. \nTurns out her mysterious boyfriend was Jeremy, Ian's friend. However, he was playing the field and being unfaithful to Louise. Lena told her about it, but she didn't believe it... Until she saw it with her own eyes. Seeking solace in her friend, Louise made a move on Lena, but she was rejected.{/size}"
            else:
                text "{font=big_noodle_titling_oblique.ttf}{size=23}Louise and Lena met at college and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with, since she's not the most out-going person. In fact, she tends to be moody and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her she's a nice, sensitive girl and a loyal friend. \nTurns out her mysterious boyfriend was Jeremy, Ian's friend. However, he was playing the field and being unfaithful to Louise. Lena learned about this, but decided against telling her friend...{/size}"
        elif chapter > 3:
            if louise_jeremy == False:
                text "{font=big_noodle_titling_oblique.ttf}{size=23}Louise and Lena met at college and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with, since she's not the most out-going person. In fact, she tends to be moody and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her she's a nice, sensitive girl and a loyal friend. \nTurns out her mysterious boyfriend was Jeremy, Ian's friend. However, he was playing the field and being unfaithful to Louise. When Lena learned about this, she decided to tell her friend.{/size}"   
            else:
                text "{font=big_noodle_titling_oblique.ttf}{size=23}Louise and Lena met at college and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with, since she's not the most out-going person. In fact, she tends to be moody and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her she's a nice, sensitive girl and a loyal friend. \nTurns out her mysterious boyfriend was Jeremy, Ian's friend. However, he was playing the field and being unfaithful to Louise. Lena learned about this, but decided against telling her friend...{/size}"
        else:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Louise and Lena met at college and they became good friends. She moved to the city to study and didn't know too many people, so she was glad to find someone she could get along with, since she's not the most out-going person. In fact, she tends to be moody and she always has some drama going on, especially with guys. She has a complicated character, but once you get to know her she's a nice, sensitive girl and a loyal friend.{/size}"   


## PERRY ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_perry:
    tag agenda_screen
    imagebutton idle "gui/bio_perry.png"
    if ian_active:
        bar:
            value ian_perry
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_perry < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_perry < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_perry
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_perry < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_perry < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Perry is Ian's flatmate. He's been a loyal friend of his since high school, and they even played in a band together during that time. When Ian had to move out of his parents' house, Perry offered him to share his family's flat for a small rent, and he accepted. Perry is laid back and lazy, and prefers to drink beer, play videogames and watch porn rather than get a job or do something productive. He has artistic talents to tap into, but he needs to get off his butt and take responsibility for his life.{/size}"

## SEYMOUR ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_seymour:
    tag agenda_screen
    imagebutton idle "gui/bio_seymour.png"
    if ian_active:
        bar:
            value ian_seymour
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_seymour < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_seymour < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_seymour
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_seymour < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_seymour < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        if chapter > 3:
            if v3_seymour_reject:
                text "{font=big_noodle_titling_oblique.ttf}{size=23}Seymour is one of the most important figures in the literary world. He began his career as a book writer and after moderate success he struck gold when he became a publisher. Now he's the head of one of the biggest publishing brands in the world, having a ton of the most important best-selling books and authors under his wing. He's well-mannered and cultured and has the calm but imposing presence of someone who's used to being obeyed. One can clearly get a glimpse of the intelligence that resides behind his clear, icy eyes. \nHe showed interest in hiring Lena as a model, but she refused. Used to always get what he wants, Seymour didn't like being rejected...{/size}"            
            else:
                text "{font=big_noodle_titling_oblique.ttf}{size=23}Seymour is one of the most important figures in the literary world. He began his career as a book writer and after moderate success he struck gold when he became a publisher. Now he's the head of one of the biggest publishing brands in the world, having a ton of the most important best-selling books and authors under his wing. He's well-mannered and cultured and has the calm but imposing presence of someone who's used to being obeyed. One can clearly get a glimpse of the intelligence that resides behind his clear, icy eyes. \nHe showed interest in hiring Lena as a model, and she agreed. Being in business with someone that influential could prove useful... But she was also intrigued by him.{/size}"            
        else:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Seymour is one of the most important figures in the literary world. He began his career as a book writer and after moderate success he struck gold when he became a publisher. Now he's the head of one of the biggest publishing brands in the world, having a ton of the most important best-selling books and authors under his wing. He's well-mannered and cultured and has the calm but imposing presence of someone who's used to being obeyed. One can clearly get a glimpse of the intelligence that resides behind his clear, icy eyes.{/size}"            
            
            
## STAN ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_stan:
    tag agenda_screen
    imagebutton idle "gui/bio_stan.png"
    if ian_active:
        bar:
            value ian_stan
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_stan < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_stan < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_stan
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_stan < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_stan < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Anyone would say Stan is a typical nerd. He is a shy and usually quiet guy who works as a programmer from home. He spends most of the time in his room, glued to his computer screen, be it working, playing games or who knows what else. It seems like most of his social life is conducted on-line, and he has no luck with the ladies. His clumsy social skills and unattractive appearance are to blame...{/size}"           
                        
## WADE ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_wade:
    tag agenda_screen
    imagebutton idle "gui/bio_wade.png"
    if ian_active:
        bar:
            value ian_wade
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_wade < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_wade < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_wade
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_wade < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_wade < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Wade has been friends with Ian and Perry since high school and played in a band together with them. He has never had any trouble with the ladies, since his good looks always made him stand out, especially compared to his friends. He always had a few girls to hook up with, until he began dating Cindy. Since he never had to really make any effort and he has an incredibly beautiful girlfriend already, he's gotten even more complacent these last few years. Seems all he's interested in is playing videogames, drinking beer and enjoying a simple life. Maybe that's why Perry and him get along really well.{/size}"               
            
            
            
            
            
            
            
 
 
 
 
 
 
 
 
## MINERVA ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_minerva:
    
    tag agenda_screen
    imagebutton idle "gui/bio_minerva.png"
    if ian_active:
        bar:
            value ian_minerva
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_minerva < 4:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_minerva < 7:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_default
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_default < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Minerva is a cultured, hard-working, fashionable and empowered woman. She runs the magazine and is a competent boss. Too bad she seems to dislike Ian for some reason, and is never happy with anything he does... On the other hand, she displays a motherly attitude when dealing with Holly.{/size}"   


            
            
## ED VAN DYKE ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_ed:
    tag agenda_screen
    imagebutton idle "gui/bio_ed.png"
    if ian_active:
        bar:
            value ian_default
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_default < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_default < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_ed
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_ed < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_ed < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Ed is as kind and friendly as his wife Molly. Together they run a café, which they opened several years back. Ed is in charge of the kitchen, and he's a great cook. He has always led a simple life and never wanted for anything more than to have a happy and fullfilling life near those he loves. His only regret is not having had a son...{/size}"   
           
            
## MOLLY VAN DYKE ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_molly:
    tag agenda_screen
    imagebutton idle "gui/bio_molly.png"
    if ian_active:
        bar:
            value ian_default
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_default < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_default < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_molly
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_molly < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_molly < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Molly is one of the kindest and most good-hearted persons one can meet. She's been married to her loving husband, Ed, for many years, and together they opened a small business that they run together. She would've made for a great mom, too bad she could never bear children... Maybe that's the reason she extends her motherly and heart-warming nature to those around her.{/size}"             
                 
            
## ROBERT ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_robert:
    tag agenda_screen
    imagebutton idle "gui/bio_robert.png"
    if ian_active:
        bar:
            value ian_robert
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_robert < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_robert < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_robert
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if chapter > 2 and lena_robert_sex:
            imagebutton idle "gui/thumb_love.png" xpos 1470 ypos 753
        elif chapter > 3 and lena_robert_over:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        elif lena_robert < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_robert < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        if chapter > 3 and lena_robert_sex and lena_robert_over:
           text "{font=big_noodle_titling_oblique.ttf}{size=23}Robert works as head waiter in a prestigious restaurant, an achievement which he's proud of. His job's not his passion, though, but a means to pay the bills and enjoy the kind of life he wants. Right now he's intrerested in partying and going out, but he would probably like to get a girlfriend, too... \nLena was trying to get over her breakup with Axel and, following Ivy's advice, decided to break her dry spell with Robert. They began a physical relationship, but Lena never saw Robert as boyfriend material. \nShe didn't take long to dump him, seeing their relationship wasn't going anywhere.{/size}"   
        if chapter > 2 and lena_robert_sex:
           text "{font=big_noodle_titling_oblique.ttf}{size=23}Robert works as head waiter in a prestigious restaurant, an achievement which he's proud of. His job's not his passion, though, but a means to pay the bills and enjoy the kind of life he wants. Right now he's intrerested in partying and going out, but he would probably like to get a girlfriend, too... \nLena was trying to get over her breakup with Axel and, following Ivy's advice, decided to break her dry spell with Robert. They began a physical relationship, but Lena never saw Robert as boyfriend material.{/size}"   
        else:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Robert works as head waiter in a prestigious restaurant, an achievement which he's proud of. His job's not his passion, though, but a means to pay the bills and enjoy the kind of life he wants. Right now he's intrerested in partying and going out, but he would probably like to get a girlfriend, too...{/size}"   
            
## LENAs MOM ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_mom:
    tag agenda_screen
    imagebutton idle "gui/bio_mom.png"
    if ian_active:
        bar:
            value ian_default
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_default < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_default < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_lenamom
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_lenamom < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_lenamom < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Lena's mom has always been a hard-working woman. Maybe too preoccupied with meeting ends meet to be as caring as Lena would've needed, she can be a bit obtuse and disregard her daughter's feelings. That's why they have always had a difficult relationship, to the extend Lena knew from a very early age she wanted to go live on her own. {/size}"               
            
## LENAs DAD ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_dad:
    tag agenda_screen
    imagebutton idle "gui/bio_dad.png"
    if ian_active:
        bar:
            value ian_default
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_default < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_default < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_lenadad
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_lenadad < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_lenadad < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}Boris is a simple man. He learned the baker trade from his father and opened up his own bakery in the neighborhood after marrying Denna. He would've felt way more comfortable having a son rather than a daughter. He loves her dearly, and because of that he always tends to be way too overprotective. He was diagnosed with cancer a couple years ago, fell ill and was forced to sell the bakery. Thankfully, he seems to be recovering.{size=23}{/size}"        
                   
            
            
## WEN ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_wen:
    tag agenda_screen
    imagebutton idle "gui/bio_wen.png"
    if ian_active:
        bar:
            value ian_wen
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_wen < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_wen < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_default
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_default < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_default < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}You can always find Wen at the gym or at the bar, emptying bottle after bottle of beer. Those are his two passions: martial arts and drinking, and maybe also fucking around with people. Despite his short stature, he's built like a tank and was a high-caliber competitor when he was younger.{size=23}{/size}" 
        
## YURI ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_yuri:
    tag agenda_screen
    imagebutton idle "gui/bio_yuri.png"
    if ian_active:
        bar:
            value ian_yuri
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_yuri < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_yuri < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_default
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_default < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_default < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}Yuri is the kickboxing coach at the gym where Ian trains. Sometimes he's absent, since he still goes to Thailand to train, even though he's been retired for a couple years. However, he was a successful professional fighter, with twenty-three fights, with a record of nineteen wins and twelve knockouts{size=23}{/size}"
        
## LOLA ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_lola:
    tag agenda_screen
    imagebutton idle "gui/bio_lola.png"
    if ian_active:
        bar:
            value ian_lola
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_lola < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_lola < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_lola
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_lola < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_lola < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Lola is Lena's cat. She's had her since she was sixteen and loves her very much. Not much can be said about Lola, since she's just a normal house cat... Or is she?{/size}"   
        
## DANNY ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_danny:
    tag agenda_screen
    imagebutton idle "gui/bio_danny.png"
    if ian_active:
        bar:
            value ian_default
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_default < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_default < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_danny
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_danny < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_danny < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Danny's passion is art and photography, more specifically artistic nude portraits. Though he can't afford to work as a photographer full time yet, he's dedicated to making a name for himself and getting deeper into this scene. He met Ivy and Lena through a friend who's also a photographer, and has wanted to shoot Lena since that day. If he ends up making it, he can be a good contact to have.{/size}" 
        
## CHERRY ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

screen bio_cherry:
    tag agenda_screen
    imagebutton idle "gui/bio_cherry.png"
    if ian_active:
        bar:
            value ian_cherry
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if chapter > 1 and ian_cherry_sex:
            imagebutton idle "gui/thumb_love.png" xpos 1470 ypos 753
        elif ian_cherry < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_cherry < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
        hbox:
            style "bio"
            if chapter > 1 and ian_cherry_sex:
                text "{font=big_noodle_titling_oblique.ttf}{size=23}Cherry met Alison at the office and they became friends. It's trhough her that Perry and Ian got to meet her. She's a stylish girl, and her stunning looks turn many heads. Cherry studied Fine Arts and loves avant-garde art, but she's been unable to make a living as a painter. Other than that, she's outgoing, nice and confident, but there's more to know about her... \nThe night Cherry met Ian she ended up at his place and had sex with him, but it seems Cherry isn't looking for a relationship.{/size}"  
            else:
                text "{font=big_noodle_titling_oblique.ttf}{size=23}Cherry met Alison at the office and they became friends. It's trhough her that Perry and Ian got to meet her. She's a stylish girl, and her stunning looks turn many heads. Cherry studied Fine Arts and loves avant-garde art, but she's been unable to make a living as a painter. Other than that, she's outgoing, nice and confident, but there's more to know about her...{/size}"  
            
    if lena_active:
        bar:
            value lena_cherry
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_cherry < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_cherry < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
        hbox:
            style "bio"
            text "{font=big_noodle_titling_oblique.ttf}{size=23} .{/size}"           
            
        
## MAYOR VERMEER ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
            
screen bio_mayor:
    tag agenda_screen
    imagebutton idle "gui/bio_mayor.png"
    if ian_active:
        bar:
            value ian_default
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_default < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_default < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_default
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_default < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_default < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        text "{font=big_noodle_titling_oblique.ttf}{size=23}Thomas Vermeer is Perry's father and was elected Mayor of the city almost four years ago. He's affiliated to a left-leaning party, but due to the current and complicated economical situation, they have been falling short on their promised social policies. Perry doesn't want to have anything to do with the political struggles that his father is immersed on, and he feels he's a disappointment to his high-achieving father.{/size}" 
                
        
        
        
        
## MIKE ################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
            
screen bio_mike:
    tag agenda_screen
    imagebutton idle "gui/bio_mike.png"
    if ian_active:
        bar:
            value ian_mike
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if ian_mike < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif ian_mike < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    if lena_active:
        bar:
            value lena_mike
            xysize (405,10)
            range 12
            xpos 1317
            ypos 831
        if lena_mike < 2:
            imagebutton idle "gui/thumb_mad.png" xpos 1470 ypos 753
        elif lena_mike_sex:
            imagebutton idle "gui/thumb_love.png" xpos 1470 ypos 753
        elif lena_mike < 4:
            imagebutton idle "gui/thumb_neutral.png" xpos 1470 ypos 753
        else:
            imagebutton idle "gui/thumb_smile.png" xpos 1470 ypos 753
    hbox:
        style "bio"
        if lena_active and lena_mike_sex:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Mike is a part-time DJ at Blazer club. He seems to be an easy-going guy abd his laid back attitude and good looks make him pretty popular with people. He seems to have a good relationship with Jeremy and Ivy. He has a girlfriend and they live together. \nLena met him at the club and was immediatly attracted to him. After flirting with him the whole night, she invited him over and had sex with him.{/size}"
        elif lena_active and v5_mike_dance:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Mike is a part-time DJ at Blazer club. He seems to be an easy-going guy abd his laid back attitude and good looks make him pretty popular with people. He seems to have a good relationship with Jeremy and Ivy. He has a girlfriend and they live together. \nLena met him at the club and was immediatly attracted to him, but decided against taking things further, since Mike is already in a relationship.{/size}"
        else:
            text "{font=big_noodle_titling_oblique.ttf}{size=23}Mike is a part-time DJ at Blazer club. He seems to be an easy-going guy abd his laid back attitude and good looks make him pretty popular with people. He seems to have a good relationship with Jeremy and Ivy. He has a girlfriend and they live together.{/size}" 
                
        
                
        