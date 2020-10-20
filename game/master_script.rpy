label master_script:


##################################################################################################################################################        
## v0.1 variables TWO SIDES OF THE COIN ################################################################################################################################################## 
##################################################################################################################################################    
    
    if chapter == 0:
        
        $ chapter = 1
        
        $ save_name = "Ian: Chapter One"
        $ prologueover = True
        
##IAN VARIABLES

    # lena
        $ v1_name = False
        $ ian_tell_lenaperry = False
    # mma
        $ ian_lowkick = False
        $ ian_grappling = False
    # alison
        $ v1_alisonlunch = False
        $ v1_encourage_alison = False
        $ v1_alisonoften = False
    # night bar
        $ v1_teamcindy = False
        $ v1_poolcindywin = False
        $ v1_teamwade = False
        $ v1_poolwadewin = False
        $ v1_poolpoints = 0
        $ v1_hitball = 0
        $ v1_drunk = False
    # robert
        $ v1_perry_help = False
        $ v1_fight = False
        $ v1_fight_kick = False
        $ v1_fight_grappling = False
        $ v1_fight_charisma = False
    # holly
        $ holly_change = 0 # Holly wants to be like Lena
        
# LENA VARIABLES
        
    # louise
        $ v1_lena_louisecarriedaway = False
    # cafe
        $ v1_ed_truth = False
        $ v1_ed_flirt = False
    # photoshoot
        $ v1_choosepic = 0
    # stan louise ivy
        $ v1_talk_stan = False
        $ v1_talk_louise = False
        $ v1_talk_ivy = False
    # peoplegram
        $ v1_rss_quote = 0
        
        jump chapter_one
        

##################################################################################################################################################        
## v0.2 variables ################################################################################################################################################## 
##################################################################################################################################################    
    
    if chapter == 1:
        
        $ chapter = 2
        
## IAN VARIABLES
    
    # status
        $ ian_chad = 1                      # Ian's mainstream and alpha-ness. 0/1/2 BASE. +3 to 5 max.
    # mma status
        $ jiujitsu = 0                      # Ian's jiu jitsu skill level  +1 Ian starts training Jiu Jitsu (max 3 -armbar)
        $ kickboxing = 0                    # Ian's striking skill level  +1 low kick +1 heavy bag (max 2) 
    # drawing
        $ v2_photo_draw = False             # Lena takes a pic of Ian's good drawing
        $ v2_addlena = False
    # emma
        $ emma_tattoo = True
    # book
        $ book_scifi = False
        $ book_fantasy = False
        $ book_historical = False
        $ book_card1 = "n"                  # Book Cards for CALL TO ADVENTURE
    # alison
        $ v2_alisonflirt = 0
        $ ian_alison_interest = 0
    # jeremy
        $ v2_showlena_jeremy = False
    # minerva
        $ decide_review_holly = False       # secondary menu var
        $ ian_minerva_review = False
        $ ian_honest_review = False
        $ ian_switch_review = False
    # lena
        $ v2_ian_date = False
    # night bar alison cherry
        $ v2_alison_clothes = False 
        $ v2_tell_jeremy_girl = False       # tell alison jeremy is with a girl
        $ v2_cocktail = 0
    # alison bar
        $ v2_bar_alison = False             # go with her at the bar
        $ alison_sexy = False               # what alison will be wearing from now on
        $ v2_find_alison = False
        $ v2_alison_home = False
        $ ian_alison_sex = False
    # cherry bar
        $ v2_cherry_interest = 0
        $ perry_cherry = 0                  # has to be >1 for her to give phone number
        $ v2_cherry_home = False
        $ ian_cherry_sex = False
    # limp status
        $ v2_ian_limp = False               # ian goes limp dick  
                
        
# LENA VARIABLES
    
    # lena status
        $ lena_posh = 1                     # Lena becomes spoiled. 0/1/2 BASE. +3 máx 5
    # ivy
        $ v2_berate_minerva = False         # lena talks with ivy
    # louise
        $ v2_sleep_louise = False
    # stan
        $ lena_stan_model_cash = False
        $ lena_stan_model_free = False
        $ v2_lena_stan_model_shirt = False  # if free, takes shirt with lust
    # cafe
        $ ed_callout = False
    # holly
        $ v2_holly_song = False             # lena will show holly her song
    # robert
        $ v2_robert_invite = False          # Lena offers Robert to go get some drinks
        $ v2_robert_spoiler = False         # Rober baits Lena with secret info to get drinks
        $ v2_robert_date = False
        $ v2_robert_kiss = False
        $ v2_robert_reject = False
        $ v2_robert_home = False
        $ v2_robert_bj = False   
        $ v2_robert_swallow = False
        $ v2_robert_chance = False          # second chance after rejecting
        $ v3_robert_date = False            # date on chapter 3
    # ian date
        $ v2_ian_like = False               # lena tells ian she like him
        $ v2_almost_kiss = False 
        $ v2_kiss = False
        $ v2_lena_kiss = False
        $ v2_ian_kiss = False
    # status branch
        $ v2_lena_gogym = False
        $ v2_lena_gohome = False
    # song
        $ song_1a = "n"
        $ song_1b = "n"
        $ song_1c = "n"
        
        jump chapter_two
        
##################################################################################################################################################        
## v0.3 variables ################################################################################################################################################## 
##################################################################################################################################################    
    
    if chapter == 2:
        
        $ chapter = 3
        
# LENA VARIABLES
    
    # status lena
        $ lena_passion = "n"                # What Lena says she's passionate about, song, model, life, money
        $ lena_metal = 0                    # Lena likes metal, not really or hates it
        $ lena_bdick = 0                    # Lena likes big dicks (+1 Jeremy spy, +1 Jeremy masturbate, +1 Axel pics) max. 3 
        $ lena_bj = 0                       # Lena likes to give blowjobs max.5
        if v2_robert_bj:
            $ lena_bj += 1
        if v2_robert_swallow:
            $ lena_bj += 1
    # song
        $ lena_song1 = 0                    # Lena's first song value                   
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
    # robert
        $ v3_robert_ignore = False          # Lena ignores Robert's call at night
        $ lena_robert_sex = False
        $ lena_robert_sex_early = False     # Lena has sex with Robert before going to work
        $ lena_robert_sex_late = False      # Lena has sex with Robert later at night
        $ v3_robert_reject = False
        $ v3_robert_bj = False
        $ v3_robert_orgasm = False          # Lena gets to cum with Robert
        $ v3_robert_repeat = False          # Lena has sex 2 times with Robert after calling him at night
    # stan
        $ v3_defend_stan = False            # Lena defends Stan before Louise
        $ v3_welcome_stan = False           # Lena lets Stan hear song/conversation with Louise
    # peoplegram
        $ v3_pg_ian = False                 # Lena posts Ian's drawing on Peoplegram
        $ v3_pg_danny = False               # Lena posts Danny's picture on Peoplegram
    # stalkfap
        $ v3_check_stalkfap = False         # create account -passive
        $ stalkfap = False                  # decide to upload -active
    # seymour
        $ v3_seymour_call = False           # text about proposal to Seymour
        $ v3_seymour_date = False           # accept dinner with Seymour
        $ v3_seymour_reject = False         # Lena rejects the dinner date
        $ seymour_restaurant = False        # Seymour knows Lena works at the restaurant
        $ help_bum = 0                      # Lena helps or runs away from homeless guy 0- run away, 1- don't give, 2- give
    # louise
        $ v3_spy = False                    # spy on Louise
        $ v3_spy_full = False               # watch full scene
        $ v3_breakfast_jeremy = False       # Lena has breakfast with Jeremy
    # cafe
        $ v3_talk_molly = False             # Lena tells Molly about Axel and Mom
    # ian
        $ v3_ian_date = False               # Lena goes with Holly and brings Ian
    # axel
        $ v3_axel_call = False              # Decide to call Axel
    # maturbate
        $ v3_use_dildo = False              # Use vibrator to masturbate
        $ v3_masturbate = "n"               # What Lena thinks about when masturbating , ian, robert, holly, spy, jeremy
    # holly
        $ lena_go_holly = 0                 # Lena's interest in Holly-- max. 1?
        
## IAN VARIABLES
    
    # jeremy
        $ louise_jeremy = True              # Jeremy dates Louise
        $ alison_jeremy = True              # Alison and Jeremy fucked
        if v2_alison_home:
             $ alison_jeremy = False
    # cherry
        $ know_cherry_model = False         # Ian knows Cherry has done modeling gigs
        $ ian_cherry_free = False           # Ian tells Cherry no strings attached
    # holly
        $ v3_holly_date = False             # Ian meets Holly on Sunday
        $ ian_go_holly = 0                  # Ian's interest in Holly -- tells Holly she's cute +1 or very cute +2 -- max. 2 - v0.6 Turns True or 0 to accept trip with Holly
        $ encourage_holly = 0               # Ian or Lena encourage Holly to be more confident. 4 max. 3 or 4 will join poledance.
    # cindy
        $ v3_pool_win = False
        $ ian_go_cindy = 0                  # Ian's interest in Cindy, max 3
        $ v3_cindy_comment = False          # Ian comments on Cindy's pic on Peoplegram
        $ v3_cindy_date = False             # Ian goes to the bar with Cindy
        $ v3_cindy_dance = False            # Dance TOGETHER with Cindy
        $ v3_cindy_dance_signs = False      # Ian sees signs of Cindy's attraction
        $ v3_cindy_reject = False           # Cindy rejects Ian's touchiness
        $ ian_cindy_model = False           # Ian asks Cindy to show her pictures
    # alison
        $ alison_voyeur = False             # Jeremy will share exploits with Alison
        $ alison_no_voyeur = False          # Ian tells Jeremy not to tell him about Alison
        $ v3_alison_date = False            # Ian meet Alison at night instead of Lena and Holly
        $ v3_alison_sex = False             # Ian has sex with Alison after the date
        $ v3_alison_boobjob = False         # Ian get a boob job from Alison
        $ v3_alison_cunnilingus = False     # Ian eats Alison out
        $ alison_satisfaction = 0           # Alison's sexual satisfaction with Ian, max 2 (cunnilingus + athletics) chapter 5 max 4 (public/fingering)        
            
        jump chapter_three
        
##################################################################################################################################################        
## v0.4 variables ################################################################################################################################################## 
##################################################################################################################################################    
    
    if chapter == 3:
        
        $ chapter = 4
        
    # LENA VARIABLES
        
    # seymour photoshoot
        if v3_seymour_date == False:
            $ v3_seymour_reject = True
        $ v4_seymour_date = False           # Lena has a photo-shoot with Seymour
        if v3_seymour_date and v3_seymour_reject == False:
            $ v4_seymour_date = True
        $ seymour_shoot = 0                 # How satisfied Seymour is with Lena's shoot - max. 3 / 4 means she masturbated
    # ian        
        $ lena_go_ian = 0                   # Lena's interest in Ian (0-none 1-doubt 2-yes)
        $ v4_ian_date = False               # Lena meets Ian at night
    # robert
        $ lena_robert_over = False          # Lena breaks up with Robert after having sex
        $ v4_robert_sex = False             # Lena fucks Robert at her home
        $ v4_robert_top = False             # Lena takes top position with Robert
        $ v4_robert_public = False          # Lena blows Robert at the restaurant
        $ v4_robert_repeat = False          # Lena calls Robert to have sex after Ian's date
    # axel
        $ v4_axel_date = False              # Lena agrees to meet Axel
        $ axel_pictures_watch = False       # Lena watches Axel's pics
        $ axel_pictures_destroy = False     # Lena destroys Axel pictures
    # stan
        $ v4_accuse_stan = False            # Lena accuses Stan of stealing underwear
        $ v4_defend_stan = False            # Lena takes Stan's side against Louise
    # photoshoot stan danny
        $ v4_danny_shoot = False            # Lena sets up a photo-shoot with Danny
        $ v4_stan_shoot = False             # Lena will ask Stan to take pictures 
    # status sex
        $ lena_anal = 0                     # Lena experiments with anal play (0-uninitiated 1-initiated)
    # cafe
        $ v4_compliment_ed = False          # Lena tells Ed he looks young
        $ cafe_help = False                 # Lena will try to help Ed and Molly with the café
        $ cafe_steal = False                # Lena decides to steal from Molly and Ed
    # louise
        $ v4_confront_louise = False        # Lena tells Louise Jeremy is lying when making up, she will get mad        
    # holly
        $ holly_gym = False                 # Holly joins pole dance
       
        
    ## IAN VARIABLES
    
    # status book
        $ book_card2 = "n"                  # Book Cards for ENEMY
    # alison and cherry
        $ v4_alison_sexting = False         # Ian texts Alison and gets a selfie
        $ v4_cherry_sexting = False         # Ian texts Cherry and gets a selfie       
    # jeremy alison
        $ alison_jeremy_block = False       # Ian tells Jeremy to stay away form Alison                          # these two vars only matter if ian_alison_sex = True
        $ alison_jeremy_doubt = False       # Ian tells Jeremy he feels uncomfortable with him pursuing Alison  #  
    # cindy
        $ wade_cindy = 0                    # Wade's relationship with Cindy. 0 min, 1 Ian encourages Wade, 2 Ian encourages Cindy
        $ v4_cindy_date = False             # Ian goes with Cindy to the gallery
        $ v5_cindy_shoot = False            # Ian will go with Cindy to the photo-shoot
    # seympour
        $ v5_hand_proposal = False          # Ian wants to hand his proposal to Seymour himself
        $ v5_hand_proposal_lena = False     # Lena agrees to hand Ian's proposal to Seymour
    # lena date
        $ v4_place = "n"                    # The place where Ian takes Lena to the date, fortress or shine
        $ v4_ian_kiss = False               # Ian makes out with Lena at the date
        $ ian_lena_sex = False              # Ian and Lena have sex
        $ v4_ian_lena_sex = False           # Lena invites Ian over after the date
    # status
        $ tournament = False                # Ian is interested in taking part in MMA tournament
        $ lena_mayor_agenda = False
        $ ian_mayor_agenda = False
        $ lena_mayorswife_agenda = False
        $ ian_mayorswife_agenda = False   
        $ ian_yuri = 3
        $ ian_yuri_agenda = False
        
        jump chapter_four
        
##################################################################################################################################################    
## v0.5 variables ################################################################################################################################################## 
##################################################################################################################################################    
    if chapter == 4:
        
        $ chapter = 5
        
## IAN VARIABLES
    
    # status
        $ ian_mike = 4                     # Mike friendship
        $ ian_mike_agenda = False
    # status book
        $ book_card3 = "n"                  # Book Cards for MENTOR
    # minerva
        $ v5_ian_showup = False             # Ian goes to the office when Seymour appears (Will or compliant with Minerva)              
    # cindy
        $ v5_cindy_nude = 0                 # Cindy gets naked in photo-shoot 1- topless 2- nude
    # perry and emma
        $ v5_perry_feelings = False         # Perry tells Ian about his feelings for Emma
        $ v5_perry_club = False             # Perry goes to the club
        $ v5_emma_talk = False              # Ian agreed to talk to Emma on Perry's behalf / if v5_emma_grind = True Ian won't actually talk to her/ v5_emma_convo3 has to be True
        $ perry_emma = 0                    # Progress on Perry's and Emma's relationship. +1 Perry goes to club. +1 Ian talks to Emma favorably.
    # holly
        $ v5_holly_date = False             # Ian meets Holly on Sunday at the park
        $ v5_tell_holly = "n"               # What Ian tells Holly when she asks if he has a girlfriend "wantgf" "nogf" "hategf"
    # status 
        $ v5_ian_morning = "n"              # How Ian spends his Saturday morning "gym" "write" or "n" (nothing)
    # night out
        $ v5_ian_cool = False               # Ian wears the red shirt to the club
        $ v5_bouncer_in = False             # Ian gets past the bouncer
    # emma sex
        $ v5_ogle = "n"                     # Who Ian looks while dancing, can be "emma" or "alison"
        $ v5_emma_convo1 = False            # Talk with Emma about her clothes
        $ v5_emma_convo2 = False            # Talk with Emma about her relationships
        $ v5_emma_convo3 = False            # Talk with Emma about Perry / $ v5_emma_talk
        $ v5_dancing_emma = False           # Ask Emma to dance
        $ v5_emma_grind = False             # Sexy dance with Emma
        $ ian_emma_sex = False              # Ian kisses Emma and ends up in his place having sex
        $ v5_emma_finger = False            # Ian tells Emma to finger herself while fucking her ass
        $ emma_satisfaction = 0             # How much Ian pleasures Emma. 0 base, 1 dirty talk
    # alison sex
        $ v5_tell_alison = "n"              # What Ian tells Alison about Lena. n - nothing concrete, kiss -hook up at bar, sex- had sex at Lena's place
        $ v5_alison_public = False          # Ian fingers Alison in the club
        $ v5_alison_sex = False             # Ian has sex with Alison after the club
        $ v5_alison_boobjob = False
        $ v5_alison_boobjob_cum = False
        $ v5_alison_dirty_talk = False      # Ian talks dirty during sex
        $ v5_alison_jeremy = False          # Jeremy fucks Alison that night
        
# LENA VARIABLES
    
    # stalkfap
        $ stalkfap_pro = 0                  # Lena decides to take stalkfap seriously. Post naughty content +1
    # night out
        $ v5_lena_sexy = False              # Lena wears sexy outfit to club
        $ v5_lena_music = False             # Lena likes the music at the club
        $ v5_defend_ivy = False             # Lena says Ivy is not so bad to Louise
    # mike
        $ lena_mike = 4                     # Mike friendship
        $ lena_mike_agenda = False
        $ v5_mike_flirt = 0                 # Lena flirts with Mike at the club. 0 - don't like him, 1 - polite, 2 - find him hot. 
        $ v5_mike_convo1 = False
        $ v5_mike_convo2 = False
        $ v5_mike_convo3 = False            # Flirting conversation, Mike tells he had GF
        $ v5_mike_dance = False             # Lena tries to seduce Mike
        $ lena_mike_sex = False             # Lena takes Mike home and has sex
        $ v5_mike_bj = False                # Lena takes the lead and sucks Mike's cock
        $ v5_mike_bareback = False          # Lena fucks Mike without condom
        $ v5_mike_cum = False               # Mike cums in Lena's pussy
    # louise sex
        $ v5_louise_sex = False             # Lena has sex with Louise after clubbing
        $ v5_teach_louise = False           # Lena teaches Louise the sapphic ways
        $ v5_louise_orgasm = False          # Lena returns the favor to Louise
        $ lena_louise_sex = False           # Lena has sex with Louise
        $ lena_reject_louise = False        # Lena rejects Louise's sexual advances
    # photoshoot
        $ v5_art_shoot = False              # Lena chooses tasteful pics
        $ v5_spicy_shoot = False            # Lena chooses sexy pics
    # robert sexting
        $ v5_robert_sexting = False         # Lena sends sexy pics to Robert
    # status ian
        $ ian_lena_dating = False           # Ian and Lena are seeing each other
    
        jump chapter_five
        
        
##################################################################################################################################################    
## v0.6 variables ################################################################################################################################################## 
##################################################################################################################################################            
        
    if chapter == 5:
        jump end
        $ chapter = 6  
        
## IAN VARIABLES
    
        $ ian_alison_dating = False     # Ian and Alison are consistently dating




# LENA VARIABLES










##################################################################################################################################################    
## END ################################################################################################################################################## 
##################################################################################################################################################     

    else:
        jump end