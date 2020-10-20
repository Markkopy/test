
## SPRITES ########################################

label define_sprites:
    
    $ lena_look = 1
    $ flena = "n"
    $ lena_style = "good"
    $ lena_necklace = 0
    $ lena_ring = 0
    $ lena_hair = 0
    $ lena_makeup = 0
    $ lena_hat = 0
    $ lena_nails = 0
    $ lena_boobs = 0
    $ lena_piercing1 = False
    $ lena_piercing2 = False
    $ lena_piercing3 = False
    $ lena_piercing4 = False
    $ lena_piercing5 = False
    $ lena_piercing6 = False
    $ lena_piercing7 = False
    $ lena_piercing8 = False
    $ lena_piercing9 = False
    $ lena_piercing10 = False
    $ lena_tattoo1 = False
    $ lena_tattoo2 = False
    $ lena_tattoo3 = False
    $ lena_tattoo4 = False
    $ lena_tattoo5 = False
    $ lena_tattoo6 = False
    $ lena_tattoo7 = False
    $ lena_tattoo8 = False
    $ lena_tattoo9 = False
    $ lena_tattoo10 = False
    $ lena_tattoo11 = False
    $ lena_tattoo12 = False
    $ lena_tattoo13 = False
    $ lena_tattoo14 = False
    $ lena_tattoo15 = False
    $ lena_tattoo16 = False
    $ lena_tattoo17 = False
    $ lena_tattoo18 = False
    $ lena_tattoo19 = False
    $ lena_tattoo20 = False
    $ lena_extras = 0
    
    
    $ ian_look = 1
    $ fian = "n"
    $ ian_style = "good"
    $ ian_headgear = False
    $ ian_hurt = 0
    $ ian_beard = 0
    $ ian_tattoo1 = False
    $ ian_tattoo2 = False
    $ ian_tattoo3 = False
    $ ian_tattoo4 = False
    $ ian_tattoo5 = False
    $ ian_tattoo6 = False
    $ ian_tattoo7 = False
    $ ian_tattoo8 = False
    $ ian_tattoo9 = False
    $ ian_tattoo10 = False
    $ ian_tattoo11 = False
    $ ian_tattoo12 = False
    $ ian_physique = 0
    $ ian_hair = 0
    $ ian_scar = 0
    $ ian_extras = 0
    
    $ alison_look = 1
    $ falison = "n"
    $ alison_sexy = False
    $ alison_tattoo = 0
    $ alison_extras = 0

    $ axel_look = 2
    $ faxel = "n"
    $ axel_hurt = 0
    $ axel_extras = 0
    
    $ cherry_look = 1
    $ fcherry = "n"
    $ cherry_stockings = False
    $ cherry_extras = 0

    $ cindy_look = 1
    $ fcindy = "n"
    $ cindy_tattoo = 0
    $ cindy_extras = 0

    $ emma_look = 1
    $ femma = "n"
    $ emma_tattoo = False
    $ emma_extras = 0
    
    $ holly_look = 1
    $ fholly = "n"
    $ holly_style = "good"
    $ holly_glasses = True
    $ holly_tattoo1 = False
    $ holly_tattoo2 = False
    $ holly_tattoo3 = False
    $ holly_tattoo4 = False
    $ holly_tattoo5 = False
    $ holly_extras = 0

    $ ivy_look = 1
    $ fivy = "n"
    $ ivy_navel = False
    $ ivy_tatoo1 = False
    $ ivy_tatoo2 = False
    $ ivy_tatoo3 = False
    $ ivy_tatoo4 = False
    $ ivy_tatoo5 = False
    $ ivy_extras = 0
    
    $ jeremy_look = 1
    $ fjeremy = "smile"
    $ jeremy_beard = 0
    $ jeremy_hurt = 0
    $ jeremy_extras = 0
    
    $ louise_look = 1
    $ flouise = "n"
    $ louise_tatoo = 0
    $ louise_extras = 0
    
    $ perry_look = 1
    $ fperry = "n"
    $ perry_glasses = True
    $ perry_extras = 0
    
    $ robert_look = 1
    $ frobert = "n"
    $ robert_splash = False
    $ robert_hurt = 0
    $ robert_extras = 0
    
    $ seymour_look = 1
    $ fseymour = "n"
    $ seymour_hurt = 0
    $ seymour_extras = 0
    
    $ stan_look = 1
    $ fstan = "n"
    $ stan_camera = False
    $ stan_extras = 0
    
    $ wade_look = 1
    $ fwade = "n"
    $ wade_hurt = 0
    $ wade_extras = 0
    
    $ fdanny = "n"
    
    $ minerva_look = 1
    $ fminerva  = "n"
    $ minerva_tattoo = 0
    $ minerva_extras = 0
    
    $ fed = "n"
    $ ed_look = 1
    $ ed_extras = 0
    
    $ molly_look = 1
    $ fmolly = "n"
    $ molly_extras = 0
    
    $ fdad = "n"
    $ fmom = "n"
    
    $ fgillian = "n"
    $ gillian_look = 1
    $ gillian_extras = 0
    
    $ fmark = "n"
    $ mark_look = 1
    $ mark_hurt = 0
    $ mark_extras = 0
    
    $ mayor_look = 1
    $ fmayor = "n"
    
    
    $ v1_fight = False
   
    
   
############################################################# ############################################################# #############################################################
## LENA ############################################################# ############################################################# ############################################################# LENA
############################################################# ############################################################# #########################################################
    
################## CLOTHES
    
    image lena = Composite(
    (640, 1080), 
    (0, 0),"lenanude.png", # BASE BODY
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
    
    (0, 0), ConditionSwitch( # CLOTHES
        "lena_look == 1", "lena1.png",
        "lena_look == 2", "lenagym.png",
        "lena_look == 3", "lenadress1.png",
        "lena_look == 'sexy'", "lena_sexy.png",
        "lena_look == 4", "lenacasual.png"),
        
    (0, 0), ConditionSwitch( # FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
    image lena2 = Composite(
    (640, 1080), 
    (0, 0),"lenanude_b.png", # POSE 2
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
    
    (0, 0), ConditionSwitch( # CLOTHES
        "lena_look == 1", "lena1_b.png",
        "lena_look == 2", "lenagym_b.png",
        "lena_look == 3", "lenadress1.png",
        "lena_look == 'sexy'", "lena_sexy_b.png",
        "lena_look == 4", "lenacasual_b.png"),        
    (0, 0), ConditionSwitch( # FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
    image lena_phone = Composite(
    (640, 1080), 
    (0, 0),"lenanude_phone.png", # PHONE
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
    
    
    (0, 0), ConditionSwitch( # CLOTHES
        "lena_look == 1", "lena1_phone.png",
        "lena_look == 2", "lenagym_phone.png",
        "lena_look == 3", "lenadress1l_phone.png",
        "lena_look == 'sexy'", "lena_sexy_phone.png",
        "lena_look == 4", "lenacasual_phone.png"),
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
########### WORK CLOTHES

    image lenawork = Composite(
    (640, 1080), 
    (0, 0),"lenanude.png", # BASE BODY
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # CAFE AND RESTAURANT
        "lena_look == 1", "lenacafe.png",
        "lena_look == 2", "lenawaitress.png"),
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
    image lenawork_phone = Composite(
    (640, 1080), 
    (0, 0),"lenanude_phone.png", # BASE BODY
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # CAFE AND RESTAURANT
        "lena_look == 1", "lenacafe_phone.png",
        "lena_look == 2", "lenawaitress_phone.png"),
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
###################### UNDERWEAR
    
    image lenabra = Composite(
    (640, 1080), 
    (0, 0),"lenanude.png", # BASE BODY
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
    
    (0, 0), ConditionSwitch( # UNDERWEAR
        "lena_look == 1", "lenacomfy.png",
        "lena_look == 2", "lenabra.png",
        "lena_look == 'sexy'", "lenabra2.png",
        "lena_look == 'black_lingerie2'", "lena_lingerie1b.png",
        "lena_look == 'black_lingerie3'", "lena_lingerie1c.png",
        "lena_look == 'black_lingerie'", "lena_lingerie1a.png"),
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
    image lenabra2 = Composite(
    (640, 1080), 
    (0, 0),"lenanude_b.png", # BASE BODY
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),   
    
    (0, 0), ConditionSwitch( # UNDERWEAR POSE 2
        "lena_look == 1", "lenacomfy.png",
        "lena_look == 2", "lenabra.png",
        "lena_look == 'sexy'", "lenabra2.png",
        "lena_look == 'black_lingerie2'", "lena_lingerie1b.png",
        "lena_look == 'black_lingerie3'", "lena_lingerie1c.png",
        "lena_look == 'black_lingerie'", "lena_lingerie1a.png"),        
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
    image lenabra_phone = Composite(
    (640, 1080), 
    (0, 0),"lenanude_phone.png", # BASE BODY
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
    
    (0, 0), ConditionSwitch( # PHONE
        "lena_look == 1", "lenacomfy_phone.png",
        "lena_look == 2", "lenabra_phone.png",
        "lena_look == 'sexy'", "lenabra2.png",
        "lena_look == 'black_lingerie2'", "lena_lingerie1b.png",
        "lena_look == 'black_lingerie3'", "lena_lingerie1c.png",
        "lena_look == 'black_lingerie'", "lena_lingerie1a.png"),
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
    image lenaunder = Composite(
    (640, 1080), 
    (0, 0),"lenanude.png", # BASE BODY
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
    
    (0, 0), ConditionSwitch( # UNDERWEAR
        "lena_look == 1", "lenabra.png",
        "lena_look == 'sexy'", "lenabra2.png",
        "lena_look == 2", "lenabra.png"),        
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
################ TOPLESS
    
    image lenatopless = Composite(
    (640, 1080), 
    (0, 0),"lenanude.png", # BASE BODY
    (0, 0), ConditionSwitch( # TOPLESS
        "lena_look == 1", "lenanobra.png",
        "lena_look == 'sexy'", "lenanobra2.png",
        "lena_look == 2", "lenanobra.png"),
        
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),   
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
    image lenatopless2 = Composite(
    (640, 1080), 
    (0, 0),"lenanude_b.png", # BASE BODY
    (0, 0), ConditionSwitch( # TOPLESS POSE 2
        "lena_look == 1", "lenanobra.png",
        "lena_look == 'sexy'", "lenanobra2.png",
        "lena_look == 2", "lenanobra.png"),
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
        
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
    image lenatopless_phone = Composite(
    (640, 1080), 
    (0, 0),"lenanude_phone.png", # BASE BODY
    (0, 0), ConditionSwitch( # TOPLESS PHONE
        "lena_look == 1", "lenanobra.png",
        "lena_look == 'sexy'", "lenanobra2.png",
        "lena_look == 2", "lenanobra.png"),
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
        
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
#################### NUDE

    image lenanude = Composite(
    (640, 1080), 
    (0, 0),"lenanude.png", # BASE BODY
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
    
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
    
    image lenanude2 = Composite(
    (640, 1080), 
    (0, 0),"lenanude_b.png", # BASE BODY POSE 2
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
    
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )

    image lenanude_phone = Composite(
    (640, 1080), 
    (0, 0),"lenanude_phone.png", # BASE BODY PHONE
    (0, 0), ConditionSwitch( # MAKEUP
        "lena_makeup == 0", Null(),
        "lena_makeup == 1", "lena_eyeshadow1.png"),
    (0, 0), ConditionSwitch( # NECKLACE
        "lena_necklace == 0", Null(),
        "lena_necklace == 'choker'", "lena_choker.png"),
    (0, 0), ConditionSwitch( # PIERCING1
        "lena_piercing1 == False", Null(),
        "lena_piercing1 == True", "lena_navel1.png"),
    (0, 0), ConditionSwitch( # PIERCING2
        "lena_piercing2 == False", Null(),
        "lena_piercing2 == True", "lena_navel2.png"),
    
    (0, 0), ConditionSwitch( #FACES
        "flena == 'sad'", "lenasad.png",
        "flena == 'blush'", "lenablush.png",
        "flena == 'cry'", "lenacry.png",
        "flena == 'drama'", "lenadrama.png",
        "flena == 'evil'", "lenaevil.png",
        "flena == 'flirt'", "lenaflirt.png",
        "flena == 'flirtevil'", "lenaflirt.png",
        "flena == 'flirtshy'", "lenaflirtshy.png",
        "flena == 'happy'", "lenahappy.png",
        "flena == 'mad'", "lenamad.png",
        "flena == 'serious'", "lenaserious.png",
        "flena == 'shy'", "lenashy.png",
        "flena == 'slut'", "lenaslut.png",
        "flena == 'slutshy'", "lenaslutshy.png",
        "flena == 'smile'", "lenasmile.png",
        "flena == 'surprise'", "lenasurprise.png",
        "flena == 'worried'", "lenaworried.png",
        "flena == 'n'", "lena.png")
    )
############################################################# ############################################################# #############################################################
## IAN ############################################################# ############################################################# ############################################################# IAN
############################################################# ############################################################# #########################################################
    
############# CLOTHES
    
    image ian = Composite(
    (640, 1080), 
    (0, 0),"iannude_soft.png", # BASE BODY
    (0, 0), ConditionSwitch( # CLOTHES
        "ian_look == 1", "ian1.png",
        "ian_look == 2", "ian2.png",
        "ian_look == 3", "ian3.png",
        "ian_look == 'cool'", "ian_cool.png",
        "ian_look == 4", "ian4.png",
        "ian_look == 5", "ian4b.png",
        "ian_look == 6", "ian5.png",
        "ian_look == 7", "iangym.png",
        "ian_look == 'gi'", "ian_gi.png"),
    (0, 0), ConditionSwitch( #FACES
        "fian == 'sad'", "iansad.png",
        "fian == 'blush'", "ianblush.png",
        "fian == 'confident'", "ianconfident.png",
        "fian == 'cry'", "iancry.png",
        "fian == 'depress'", "iandepress.png",
        "fian == 'disgusted'", "iandisgusted.png",
        "fian == 'evil'", "ianevil.png",
        "fian == 'furious'", "ianfurious.png",
        "fian == 'happy'", "ianhappy.png",
        "fian == 'insecure'", "ianinsecure.png",
        "fian == 'mad'", "ianmad.png",
        "fian == 'serious'", "ianserious.png",                       
        "fian == 'smile'", "iansmile.png",
        "fian == 'surprise'", "iansurprise.png",                           
        "fian == 'worried'", "ianworried.png", 
        "fian == 'shy'", "ianshy.png",
        "fian == 'n'", "ian.png"),
    (0, 0), ConditionSwitch( # HEADGEAR
        "ian_headgear == False", Null (),
        "ian_headgear == True", "headgear.png"),
    (0, 0), ConditionSwitch( # HURT
        "ian_hurt == 0", Null (),
        "ian_hurt == 1", "ian_hurt.png",
        "ian_hurt == 2", "ian_hurt2.png")
    )
  
    image ian_phone = Composite(
    (640, 1080), 
    (0, 0),"iannude_phone.png", # BASE BODY
    (0, 0), ConditionSwitch( # CLOTHES
        "ian_look == 1", "ian1_phone.png",
        "ian_look == 2", "ian2_phone.png",
        "ian_look == 3", "ian3_phone.png",
        "ian_look == 'cool'", "ian_cool_phone.png",
        "ian_look == 4", "ian4_phone.png",
        "ian_look == 5", "ian4b_phone.png",
        "ian_look == 6", "ian5_phone.png",
        "ian_look == 7", "iangym.png"),
    (0, 0), ConditionSwitch( # FACES
        "fian == 'sad'", "iansad.png",
        "fian == 'blush'", "ianblush.png",
        "fian == 'confident'", "ianconfident.png",
        "fian == 'cry'", "iancry.png",
        "fian == 'depress'", "iandepress.png",
        "fian == 'disgusted'", "iandisgusted.png",
        "fian == 'evil'", "ianevil.png",
        "fian == 'furious'", "ianfurious.png",
        "fian == 'happy'", "ianhappy.png",
        "fian == 'insecure'", "ianinsecure.png",
        "fian == 'mad'", "ianmad.png",
        "fian == 'serious'", "ianserious.png",                       
        "fian == 'smile'", "iansmile.png",
        "fian == 'surprise'", "iansurprise.png",                           
        "fian == 'worried'", "ianworried.png",  
        "fian == 'shy'", "ianshy.png",
        "fian == 'n'", "ian.png"),
    (0, 0), ConditionSwitch( # HEADGEAR
        "ian_headgear == False", Null (),
        "ian_headgear == True", "headgear.png"),
    (0, 0), ConditionSwitch( # HURT
        "ian_hurt == 0", Null (),
        "ian_hurt == 1", "ian_hurt.png",
        "ian_hurt == 2", "ian_hurt2.png")
    )
    
################ UNDERWEAR
    
    image ianunder = Composite(
    (640, 1080), 
    (0, 0),"iannude_soft.png", # BASE BODY
    (0, 0), ConditionSwitch( # CLOTHES
        "ian_look == 1", "ian2.png",
        "ian_look == 2", "iannoshirt.png",
        "ian_look == 3", "ianunder.png",
        "ian_look == 'cool'", "ian_coolb.png",
        "ian_look == 4", "ian4b.png",
        "ian_look == 5", "ian4b.png",
        "ian_look == 6", "ian5b.png",
        "ian_look == 7", "iangym_b.png"),
    (0, 0), ConditionSwitch( #FACES
        "fian == 'sad'", "iansad.png",
        "fian == 'blush'", "ianblush.png",
        "fian == 'confident'", "ianconfident.png",
        "fian == 'cry'", "iancry.png",
        "fian == 'depress'", "iandepress.png",
        "fian == 'disgusted'", "iandisgusted.png",
        "fian == 'evil'", "ianevil.png",
        "fian == 'furious'", "ianfurious.png",
        "fian == 'happy'", "ianhappy.png",
        "fian == 'insecure'", "ianinsecure.png",
        "fian == 'mad'", "ianmad.png",
        "fian == 'serious'", "ianserious.png",                       
        "fian == 'smile'", "iansmile.png",
        "fian == 'surprise'", "iansurprise.png",                           
        "fian == 'worried'", "ianworried.png",   
        "fian == 'shy'", "ianshy.png",
        "fian == 'n'", "ian.png"),
    (0, 0), ConditionSwitch ( # HURT
        "ian_hurt == 0", Null (),
        "ian_hurt == 1", "ian_hurt.png",
        "ian_hurt == 2", "ian_hurt2.png")
    )
    
    image ianunder_phone = Composite(
    (640, 1080), 
    (0, 0),"iannude_phone.png", # BASE BODY
    (0, 0), ConditionSwitch( # CLOTHES
        "ian_look == 1", "ian2_phone.png",
        "ian_look == 2", "iannoshirt.png",
        "ian_look == 3", "ianunder.png",
        "ian_look == 'cool'", "ian_coolb.png",
        "ian_look == 4", "ian4b.png",
        "ian_look == 5", "ian4b.png",
        "ian_look == 6", "ian5b.png",
        "ian_look == 7", "iangym_b.png"),
    (0, 0), ConditionSwitch( #FACES
        "fian == 'sad'", "iansad.png",
        "fian == 'blush'", "ianblush.png",
        "fian == 'confident'", "ianconfident.png",
        "fian == 'cry'", "iancry.png",
        "fian == 'depress'", "iandepress.png",
        "fian == 'disgusted'", "iandisgusted.png",
        "fian == 'evil'", "ianevil.png",
        "fian == 'furious'", "ianfurious.png",
        "fian == 'happy'", "ianhappy.png",
        "fian == 'insecure'", "ianinsecure.png",
        "fian == 'mad'", "ianmad.png",
        "fian == 'serious'", "ianserious.png",                       
        "fian == 'smile'", "iansmile.png",
        "fian == 'surprise'", "iansurprise.png",                           
        "fian == 'worried'", "ianworried.png", 
        "fian == 'shy'", "ianshy.png",
        "fian == 'n'", "ian.png"),
    (0, 0), ConditionSwitch ( # HURT
        "ian_hurt == 0", Null (),
        "ian_hurt == 1", "ian_hurt.png",
        "ian_hurt == 2", "ian_hurt2.png")
    )
    
################# NUDE

    image iannude = Composite( 
    (640, 1080), 
    (0, 0),"iannude.png", # ERECT
    (0, 0), ConditionSwitch( # FACES
        "fian == 'sad'", "iansad.png",
        "fian == 'blush'", "ianblush.png",
        "fian == 'confident'", "ianconfident.png",
        "fian == 'cry'", "iancry.png",
        "fian == 'depress'", "iandepress.png",
        "fian == 'disgusted'", "iandisgusted.png",
        "fian == 'evil'", "ianevil.png",
        "fian == 'furious'", "ianfurious.png",
        "fian == 'happy'", "ianhappy.png",
        "fian == 'insecure'", "ianinsecure.png",
        "fian == 'mad'", "ianmad.png",
        "fian == 'serious'", "ianserious.png",                       
        "fian == 'smile'", "iansmile.png",
        "fian == 'surprise'", "iansurprise.png",                           
        "fian == 'worried'", "ianworried.png", 
        "fian == 'shy'", "ianshy.png",
        "fian == 'n'", "ian.png"),
    (0, 0), ConditionSwitch ( # HURT
        "ian_hurt == False", Null (),
        "ian_hurt == 1", "ian_hurt.png",
        "ian_hurt == 2", "ian_hurt2.png")
    )
    
    image iannude_phone = Composite( 
    (640, 1080), 
    (0, 0),"iannude_phone.png", # PHONE
    (0, 0), ConditionSwitch( #FACES
        "fian == 'sad'", "iansad.png",
        "fian == 'blush'", "ianblush.png",
        "fian == 'confident'", "ianconfident.png",
        "fian == 'cry'", "iancry.png",
        "fian == 'depress'", "iandepress.png",
        "fian == 'disgusted'", "iandisgusted.png",
        "fian == 'evil'", "ianevil.png",
        "fian == 'furious'", "ianfurious.png",
        "fian == 'happy'", "ianhappy.png",
        "fian == 'insecure'", "ianinsecure.png",
        "fian == 'mad'", "ianmad.png",
        "fian == 'serious'", "ianserious.png",                       
        "fian == 'smile'", "iansmile.png",
        "fian == 'surprise'", "iansurprise.png",                           
        "fian == 'worried'", "ianworried.png", 
        "fian == 'shy'", "ianshy.png",
        "fian == 'n'", "ian.png"),
    (0, 0), ConditionSwitch ( # HURT
        "ian_hurt == False", Null (),
        "ian_hurt == 1", "ian_hurt.png",
        "ian_hurt == 2", "ian_hurt2.png")
    )
    
    image iannude2 = Composite( 
    (640, 1080), 
    (0, 0),"iannude_soft.png", # SOFT
    (0, 0), ConditionSwitch( # FACES
        "fian == 'sad'", "iansad.png",
        "fian == 'blush'", "ianblush.png",
        "fian == 'confident'", "ianconfident.png",
        "fian == 'cry'", "iancry.png",
        "fian == 'depress'", "iandepress.png",
        "fian == 'disgusted'", "iandisgusted.png",
        "fian == 'evil'", "ianevil.png",
        "fian == 'furious'", "ianfurious.png",
        "fian == 'happy'", "ianhappy.png",
        "fian == 'insecure'", "ianinsecure.png",
        "fian == 'mad'", "ianmad.png",
        "fian == 'serious'", "ianserious.png",                       
        "fian == 'smile'", "iansmile.png",
        "fian == 'surprise'", "iansurprise.png",                           
        "fian == 'worried'", "ianworried.png",
        "fian == 'shy'", "ianshy.png",
        "fian == 'n'", "ian.png"),
    (0, 0), ConditionSwitch ( # HURT
        "ian_hurt == False", Null (),
        "ian_hurt == 1", "ian_hurt.png",
        "ian_hurt == 2", "ian_hurt2.png")
    )
    

############################################################# ############################################################# #############################################################
## ALISON ############################################################# ############################################################# ############################################################# ALISON
############################################################# ############################################################# #############################################################

    # CLOTHES
    
    image alison = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( # BODY
        "alison_look == 1", "alison1.png",
        "alison_look == 2", "alison2.png"),
    (0, 0), ConditionSwitch( # FACES
        "falison == 'sad'", "alisonsad.png",
        "falison == 'smile'", "alisonsmile.png",
        "falison == 'mad'", "alisonmad.png",
        "falison == 'serious'", "alisonserious.png",
        "falison == 'surprise'", "alisonsurprise.png",
        "falison == 'flirt'", "alisonflirt.png",
        "falison == 'blush'", "alisonblush.png",
        "falison == 'slut'", "alisonslut.png",
        "falison == 'n'", "alison.png")
    )

    # NUDE
    
    image alisonnude = Composite(
    (640, 1080), 
    (0, 0), "alisonnude.png",
    (0, 0), ConditionSwitch( #FACES
        "falison == 'sad'", "alisonsad.png",
        "falison == 'smile'", "alisonsmile.png",
        "falison == 'mad'", "alisonmad.png",
        "falison == 'serious'", "alisonserious.png",
        "falison == 'surprise'", "alisonsurprise.png",
        "falison == 'flirt'", "alisonflirt.png",
        "falison == 'blush'", "alisonblush.png",
        "falison == 'slut'", "alisonslut.png",
        "falison == 'n'", "alison.png")
    )

    # UNDERWEAR

    image alisonbra = Composite(
    (640, 1080), 
    (0, 0), "alisonbra.png",
    (0, 0), ConditionSwitch( #FACES
        "falison == 'sad'", "alisonsad.png",
        "falison == 'smile'", "alisonsmile.png",
        "falison == 'mad'", "alisonmad.png",
        "falison == 'serious'", "alisonserious.png",
        "falison == 'surprise'", "alisonsurprise.png",
        "falison == 'flirt'", "alisonflirt.png",
        "falison == 'blush'", "alisonblush.png",
        "falison == 'slut'", "alisonslut.png",
        "falison == 'n'", "alison.png")
    )

############################################################# ############################################################# #############################################################
## AXEL ############################################################# ############################################################# ############################################################# AXEL
############################################################# ############################################################# #############################################################

    # CLOTHES
    
    image axel = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( # BODY
        "axel_look == 1", "axel1.png",
        "axel_look == 2", "axel2.png"),
    (0, 0), ConditionSwitch( # FACE
        "faxel == 'furious'", "axelfurious.png",
        "faxel == 'happy'", "axelhappy.png",
        "faxel == 'mad'", "axelmad.png",
        "faxel == 'sad'", "axelsad.png",
        "faxel == 'smile'", "axelsmile.png",
        "faxel == 'cry'", "axelcry.png",
        "faxel == 'n'", "axel.png")
    )

    # NUDE
    
    image axelnude = Composite(
    (640, 1080),
    (0, 0), "axelnude.png",
    (0, 0), ConditionSwitch( # FACE
        "faxel == 'furious'", "axelfurious.png",
        "faxel == 'happy'", "axelhappy.png",
        "faxel == 'mad'", "axelmad.png",
        "faxel == 'sad'", "axelsad.png",
        "faxel == 'smile'", "axelsmile.png",
        "faxel == 'cry'", "axelcry.png",
        "faxel == 'n'", "axel.png")
    )


############################################################# ############################################################# #############################################################
## CHERRY ############################################################# ############################################################# ############################################################# CHERRY
############################################################# ############################################################# #############################################################


    # CLOTHES
    
    image cherry = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( # BODY
        "cherry_look == 1", "cherry1.png",
        "cherry_look == 2", "cherry2.png"),
    (0, 0), ConditionSwitch( # COSMETICS
        "cherry_stockings == False", Null(),
        "cherry_stockings == True", "cherry_stockings.png"),
    (0, 0), ConditionSwitch( # FACE
        "fcherry == 'mad'", "cherrymad.png",
        "fcherry == 'blush'", "cherryblush.png",
        "fcherry == 'sad'", "cherrysad.png",
        "fcherry == 'cry'", "cherrycry.png",
        "fcherry == 'smile'", "cherrysmile.png",
        "fcherry == 'happy'", "cherryhappy.png",
        "fcherry == 'flirt'", "cherryflirt.png",
        "fcherry == 'n'", "cherry.png")
    )
     
    # BRA
    
    image cherrynude = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( # BODY
        "cherry_look == 1", "cherrybra.png",
        "cherry_look == 2", "cherrybra_b.png"),
    (0, 0), ConditionSwitch( # COSMETICS
        "cherry_stockings == False", Null(),
        "cherry_stockings == True", "cherry_stockings.png"),
    (0, 0), ConditionSwitch( # FACE
        "fcherry == 'mad'", "cherrymad.png",
        "fcherry == 'blush'", "cherryblush.png",
        "fcherry == 'sad'", "cherrysad.png",
        "fcherry == 'cry'", "cherrycry.png",
        "fcherry == 'smile'", "cherrysmile.png",
        "fcherry == 'happy'", "cherryhappy.png",
        "fcherry == 'flirt'", "cherryflirt.png",
        "fcherry == 'n'", "cherry.png")
    )
     
    # NUDE
    
    image cherrynude = Composite(
    (640, 1080), 
    (0, 0), "cherrynude.png",
    (0, 0), ConditionSwitch( # COSMETICS
        "cherry_stockings == False", Null(),
        "cherry_stockings == True", "cherry_stockings.png"),
    (0, 0), ConditionSwitch( # FACE
        "fcherry == 'mad'", "cherrymad.png",
        "fcherry == 'blush'", "cherryblush.png",
        "fcherry == 'sad'", "cherrysad.png",
        "fcherry == 'cry'", "cherrycry.png",
        "fcherry == 'smile'", "cherrysmile.png",
        "fcherry == 'happy'", "cherryhappy.png",
        "fcherry == 'flirt'", "cherryflirt.png",
        "fcherry == 'n'", "cherry.png")
    )
    
############################################################# ############################################################# #############################################################
## CINDY ############################################################# ############################################################# ############################################################# CINDY
############################################################# ############################################################# #############################################################


    # CLOTHES
    
    image cindy = Composite(
    (640, 1080), 
    (0, 0), "cindy1.png",
    (0, 0), ConditionSwitch( # FACE
        "fcindy == 'blush'", "cindyblush.png",
        "fcindy == 'flirt'", "cindyflirt.png",
        "fcindy == 'mad'", "cindymad.png",
        "fcindy == 'sad'", "cindysad.png",
        "fcindy == 'serious'", "cindyserious.png",
        "fcindy == 'smile'", "cindysmile.png",
        "fcindy == 'surprise'", "cindysurprise.png",
        "fcindy == 'slut'", "cindyslut.png",
        "fcindy == 'cry'", "cindycry.png",
        "fcindy == 'shy'", "cindyshy.png",
        "fcindy == 'n'", "cindy.png")
    )
    
    image cindy2 = Composite(
    (640, 1080), 
    (0, 0), "cindy1_b.png",
    (0, 0), ConditionSwitch( # FACE
        "fcindy == 'blush'", "cindyblush.png",
        "fcindy == 'flirt'", "cindyflirt.png",
        "fcindy == 'mad'", "cindymad.png",
        "fcindy == 'sad'", "cindysad.png",
        "fcindy == 'serious'", "cindyserious.png",
        "fcindy == 'smile'", "cindysmile.png",
        "fcindy == 'surprise'", "cindysurprise.png",
        "fcindy == 'slut'", "cindyslut.png",
        "fcindy == 'cry'", "cindycry.png",
        "fcindy == 'shy'", "cindyshy.png",
        "fcindy == 'n'", "cindy.png")
    )
    
    # UNDERWEAR
    
    image cindybra = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( # BODY
        "cindy_look == 1", "cindybra.png",
        "cindy_look == 'comfy'", "cindycomfy.png",
        "cindy_look == 'comfytopless'", "cindycomfy2.png"),
    (0, 0), ConditionSwitch( # FACE
        "fcindy == 'blush'", "cindyblush.png",
        "fcindy == 'flirt'", "cindyflirt.png",
        "fcindy == 'mad'", "cindymad.png",
        "fcindy == 'sad'", "cindysad.png",
        "fcindy == 'serious'", "cindyserious.png",
        "fcindy == 'smile'", "cindysmile.png",
        "fcindy == 'surprise'", "cindysurprise.png",
        "fcindy == 'slut'", "cindyslut.png",
        "fcindy == 'cry'", "cindycry.png",
        "fcindy == 'shy'", "cindyshy.png",
        "fcindy == 'n'", "cindy.png")
    )
    
    image cindybra2 = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( # BODY
        "cindy_look == 1", "cindybra_b.png",
        "cindy_look == 'comfy'", "cindycomfy_b.png",
        "cindy_look == 'comfytopless'", "cindycomfy2_b.png"),
    (0, 0), ConditionSwitch( # FACE
        "fcindy == 'blush'", "cindyblush.png",
        "fcindy == 'flirt'", "cindyflirt.png",
        "fcindy == 'mad'", "cindymad.png",
        "fcindy == 'sad'", "cindysad.png",
        "fcindy == 'serious'", "cindyserious.png",
        "fcindy == 'smile'", "cindysmile.png",
        "fcindy == 'surprise'", "cindysurprise.png",
        "fcindy == 'slut'", "cindyslut.png",
        "fcindy == 'cry'", "cindycry.png",
        "fcindy == 'shy'", "cindyshy.png",
        "fcindy == 'n'", "cindy.png")
    )
    
    # NUDE
    
    image cindynude = Composite(
    (640, 1080), 
    (0, 0), "cindynude.png",
    (0, 0), ConditionSwitch( # FACE
        "fcindy == 'blush'", "cindyblush.png",
        "fcindy == 'flirt'", "cindyflirt.png",
        "fcindy == 'mad'", "cindymad.png",
        "fcindy == 'sad'", "cindysad.png",
        "fcindy == 'serious'", "cindyserious.png",
        "fcindy == 'smile'", "cindysmile.png",
        "fcindy == 'surprise'", "cindysurprise.png",
        "fcindy == 'slut'", "cindyslut.png",
        "fcindy == 'cry'", "cindycry.png",
        "fcindy == 'shy'", "cindyshy.png",
        "fcindy == 'n'", "cindy.png")
    )
    
    image cindynude2 = Composite(
    (640, 1080), 
    (0, 0), "cindynude_b.png",
    (0, 0), ConditionSwitch( # FACE
        "fcindy == 'blush'", "cindyblush.png",
        "fcindy == 'flirt'", "cindyflirt.png",
        "fcindy == 'mad'", "cindymad.png",
        "fcindy == 'sad'", "cindysad.png",
        "fcindy == 'serious'", "cindyserious.png",
        "fcindy == 'smile'", "cindysmile.png",
        "fcindy == 'surprise'", "cindysurprise.png",
        "fcindy == 'slut'", "cindyslut.png",
        "fcindy == 'cry'", "cindycry.png",
        "fcindy == 'shy'", "cindyshy.png",
        "fcindy == 'n'", "cindy.png")
    )
    

############################################################# ############################################################# #############################################################
## DANNY ############################################################# ############################################################# ############################################################# DANNY
############################################################# ############################################################# #############################################################

    # CLOTHES
    
    image danny = Composite(
    (640, 1080), 
    (0, 0), "danny2.png", 
    (0, 0), ConditionSwitch( 
        "fdanny == 'sad'", "dannysad.png",
        "fdanny == 'smile'", "dannysmile.png",
        "fdanny == 'mad'", "dannymad.png",
        "fdanny == 'surprise'", "dannysurprise.png",
        "fdanny == 'n'", "danny.png")
    )
    
    image danny2 = Composite(
    (640, 1080), 
    (0, 0), "danny1.png", 
    (0, 0), ConditionSwitch( 
        "fdanny == 'sad'", "dannysad.png",
        "fdanny == 'smile'", "dannysmile.png",
        "fdanny == 'mad'", "dannymad.png",
        "fdanny == 'surprise'", "dannysurprise.png",
        "fdanny == 'n'", "danny.png")
    )

############################################################# ############################################################# #############################################################
## EMMA ############################################################# ############################################################# ############################################################# EMMA
############################################################# ############################################################# #############################################################

    # CLOTHES
    
    image emma = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( # BODY
        "emma_look == 1", "emma1.png",
        "emma_look == 2", "emma2.png"),
    (0, 0), ConditionSwitch( # COSMETICS
        "emma_tattoo == False", Null(),
        "emma_tattoo == True", "emma_tattoo.png"),
    (0, 0), ConditionSwitch( 
        "femma == 'sad'", "emmasad.png",
        "femma == 'smile'", "emmasmile.png",
        "femma == 'mad'", "emmamad.png",
        "femma == 'serious'", "emmaserious.png",
        "femma == 'surprise'", "emmasurprise.png",
        "femma == 'flirt'", "emmaflirt.png",
        "femma == 'n'", "emma.png")
    )
        
    # NUDE
    
    image emmanude = Composite(
    (640, 1080), 
    (0, 0), "emmanude.png", 
    (0, 0), ConditionSwitch( # COSMETICS
        "emma_tattoo == False", Null(),
        "emma_tattoo == True", "emma_tattoo.png"),
    (0, 0), ConditionSwitch( 
        "femma == 'sad'", "emmasad.png",
        "femma == 'smile'", "emmasmile.png",
        "femma == 'mad'", "emmamad.png",
        "femma == 'serious'", "emmaserious.png",
        "femma == 'surprise'", "emmasurprise.png",
        "femma == 'flirt'", "emmaflirt.png",
        "femma == 'n'", "emma.png")
    )
    
############################################################# ############################################################# #############################################################
## HOLLY ############################################################# ############################################################# ############################################################# HOLLY
############################################################# ############################################################# #############################################################

    # CLOTHES
    
    image holly = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( # BODY
        "holly_look == 1", "holly1.png",
        "holly_look == 3", "hollygym.png",
        "holly_look == 2", "holly2.png"),
    (0, 0), ConditionSwitch( # FACE
        "fholly == 'flirtshy'", "hollyflirtshyb.png",
        "fholly == 'flirt'", "hollyflirtb.png",
        "fholly == 'surprise'", "hollysurpriseb.png",
        "fholly == 'shy'", "hollysmileshyb.png",
        "fholly == 'serious'", "hollyseriousb.png",
        "fholly == 'mad'", "hollymadb.png",
        "fholly == 'smile'", "hollysmileb.png",
        "fholly == 'happy'", "hollyhappyb.png",
        "fholly == 'happyshy'", "hollyhappyshyb.png",
        "fholly == 'sad'", "hollysadb.png",
        "fholly == 'blush'", "hollyblushb.png",
        "fholly == 'cry'", "hollycryb.png",
        "fholly == 'shy'", "hollyshy.png",
        "fholly == 'worried'", "hollyworried.png",
        "fholly == 'n'", "hollyb.png"),
    (0, 0), ConditionSwitch( # GLASSES
        "holly_glasses == False", Null(),
        "holly_glasses == True", "hollyglasses.png")
    )    
    image holly2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( # BODY
        "holly_look == 1", "holly1_b.png",
        "holly_look == 3", "hollygym_b.png",
        "holly_look == 2", "holly2_b.png"),
    (0, 0), ConditionSwitch( # FACE
        "fholly == 'flirtshy'", "hollyflirtshyb.png",
        "fholly == 'flirt'", "hollyflirtb.png",
        "fholly == 'surprise'", "hollysurpriseb.png",
        "fholly == 'shy'", "hollysmileshyb.png",
        "fholly == 'serious'", "hollyseriousb.png",
        "fholly == 'mad'", "hollymadb.png",
        "fholly == 'smile'", "hollysmileb.png",
        "fholly == 'happy'", "hollyhappyb.png",
        "fholly == 'happyshy'", "hollyhappyshyb.png",
        "fholly == 'sad'", "hollysadb.png",
        "fholly == 'blush'", "hollyblushb.png",
        "fholly == 'cry'", "hollycryb.png",
        "fholly == 'shy'", "hollyshy.png",
        "fholly == 'worried'", "hollyworried.png",
        "fholly == 'n'", "hollyb.png"),
    (0, 0), ConditionSwitch( # GLASSES
        "holly_glasses == False", Null(),
        "holly_glasses == True", "hollyglasses.png")
    )    
    image holly3 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( # BODY
        "holly_look == 1", "holly1_c.png",
        "holly_look == 3", "hollygym_c.png",
        "holly_look == 2", "holly2_c.png"),
    (0, 0), ConditionSwitch( # FACE
        "fholly == 'flirtshy'", "hollyflirtshyb.png",
        "fholly == 'flirt'", "hollyflirtb.png",
        "fholly == 'surprise'", "hollysurpriseb.png",
        "fholly == 'shy'", "hollysmileshyb.png",
        "fholly == 'serious'", "hollyseriousb.png",
        "fholly == 'mad'", "hollymadb.png",
        "fholly == 'smile'", "hollysmileb.png",
        "fholly == 'happy'", "hollyhappyb.png",
        "fholly == 'happyshy'", "hollyhappyshyb.png",
        "fholly == 'sad'", "hollysadb.png",
        "fholly == 'blush'", "hollyblushb.png",
        "fholly == 'cry'", "hollycryb.png",
        "fholly == 'shy'", "hollyshy.png",
        "fholly == 'worried'", "hollyworried.png",
        "fholly == 'n'", "hollyb.png"),
    (0, 0), ConditionSwitch( # GLASSES
        "holly_glasses == False", Null(),
        "holly_glasses == True", "hollyglasses.png")
    )    
    # UNDERWEAR
    
    image hollybra = Composite(
    (640, 1080),
    (0, 0), "hollybra.png",
    (0, 0), ConditionSwitch( # FACE
        "fholly == 'flirtshy'", "hollyflirtshyb.png",
        "fholly == 'flirt'", "hollyflirtb.png",
        "fholly == 'surprise'", "hollysurpriseb.png",
        "fholly == 'shy'", "hollysmileshyb.png",
        "fholly == 'serious'", "hollyseriousb.png",
        "fholly == 'mad'", "hollymadb.png",
        "fholly == 'smile'", "hollysmileb.png",
        "fholly == 'happy'", "hollyhappyb.png",
        "fholly == 'sad'", "hollysadb.png",
        "fholly == 'blush'", "hollyblushb.png",
        "fholly == 'cry'", "hollycryb.png",
        "fholly == 'shy'", "hollyshy.png",
        "fholly == 'worried'", "hollyworried.png",
        "fholly == 'n'", "hollyb.png"),
    (0, 0), ConditionSwitch( # GLASSES
        "holly_glasses == False", Null(),
        "holly_glasses == True", "hollyglasses.png")
    )    
    image hollybra2 = Composite(
    (640, 1080),
    (0, 0), "hollybra_b.png",
    (0, 0), ConditionSwitch( # FACE
        "fholly == 'flirtshy'", "hollyflirtshyb.png",
        "fholly == 'flirt'", "hollyflirtb.png",
        "fholly == 'surprise'", "hollysurpriseb.png",
        "fholly == 'shy'", "hollysmileshyb.png",
        "fholly == 'serious'", "hollyseriousb.png",
        "fholly == 'mad'", "hollymadb.png",
        "fholly == 'smile'", "hollysmileb.png",
        "fholly == 'happy'", "hollyhappyb.png",
        "fholly == 'sad'", "hollysadb.png",
        "fholly == 'blush'", "hollyblushb.png",
        "fholly == 'cry'", "hollycryb.png",
        "fholly == 'shy'", "hollyshy.png",
        "fholly == 'worried'", "hollyworried.png",
        "fholly == 'n'", "hollyb.png"),
    (0, 0), ConditionSwitch( # GLASSES
        "holly_glasses == False", Null(),
        "holly_glasses == True", "hollyglasses.png")
    )    
    image hollybra3 = Composite(
    (640, 1080),
    (0, 0), "hollybra_c.png",
    (0, 0), ConditionSwitch( # FACE
        "fholly == 'flirtshy'", "hollyflirtshyb.png",
        "fholly == 'flirt'", "hollyflirtb.png",
        "fholly == 'surprise'", "hollysurpriseb.png",
        "fholly == 'shy'", "hollysmileshyb.png",
        "fholly == 'serious'", "hollyseriousb.png",
        "fholly == 'mad'", "hollymadb.png",
        "fholly == 'smile'", "hollysmileb.png",
        "fholly == 'happy'", "hollyhappyb.png",
        "fholly == 'sad'", "hollysadb.png",
        "fholly == 'blush'", "hollyblushb.png",
        "fholly == 'cry'", "hollycryb.png",
        "fholly == 'shy'", "hollyshy.png",
        "fholly == 'worried'", "hollyworried.png",
        "fholly == 'n'", "hollyb.png"),
    (0, 0), ConditionSwitch( # GLASSES
        "holly_glasses == False", Null(),
        "holly_glasses == True", "hollyglasses.png")
    )    
    # NUDE
    
    image hollynude = Composite(
    (640, 1080),
    (0, 0), "hollynude.png",
    (0, 0), ConditionSwitch( # FACE
        "fholly == 'flirtshy'", "hollyflirtshyb.png",
        "fholly == 'flirt'", "hollyflirtb.png",
        "fholly == 'surprise'", "hollysurpriseb.png",
        "fholly == 'shy'", "hollysmileshyb.png",
        "fholly == 'serious'", "hollyseriousb.png",
        "fholly == 'mad'", "hollymadb.png",
        "fholly == 'smile'", "hollysmileb.png",
        "fholly == 'happy'", "hollyhappyb.png",
        "fholly == 'sad'", "hollysadb.png",
        "fholly == 'blush'", "hollyblushb.png",
        "fholly == 'cry'", "hollycryb.png",
        "fholly == 'happyshy'", "hollyhappyshyb.png",
        "fholly == 'shy'", "hollyshy.png",
        "fholly == 'worried'", "hollyworried.png",
        "fholly == 'n'", "hollyb.png"),
    (0, 0), ConditionSwitch( # GLASSES
        "holly_glasses == False", Null(),
        "holly_glasses == True", "hollyglasses.png")
    )
    image hollynude2 = Composite(
    (640, 1080),
    (0, 0), "hollynude_b.png",
    (0, 0), ConditionSwitch( # FACE
        "fholly == 'flirtshy'", "hollyflirtshyb.png",
        "fholly == 'flirt'", "hollyflirtb.png",
        "fholly == 'surprise'", "hollysurpriseb.png",
        "fholly == 'shy'", "hollysmileshyb.png",
        "fholly == 'serious'", "hollyseriousb.png",
        "fholly == 'mad'", "hollymadb.png",
        "fholly == 'smile'", "hollysmileb.png",
        "fholly == 'happy'", "hollyhappyb.png",
        "fholly == 'sad'", "hollysadb.png",
        "fholly == 'blush'", "hollyblushb.png",
        "fholly == 'cry'", "hollycryb.png",
        "fholly == 'happyshy'", "hollyhappyshyb.png",
        "fholly == 'shy'", "hollyshy.png",
        "fholly == 'worried'", "hollyworried.png",
        "fholly == 'n'", "hollyb.png"),
    (0, 0), ConditionSwitch( # GLASSES
        "holly_glasses == False", Null(),
        "holly_glasses == True", "hollyglasses.png")
    )
    image hollynude3 = Composite(
    (640, 1080),
    (0, 0), "hollynude_c.png",
    (0, 0), ConditionSwitch( # FACE
        "fholly == 'flirtshy'", "hollyflirtshyb.png",
        "fholly == 'flirt'", "hollyflirtb.png",
        "fholly == 'surprise'", "hollysurpriseb.png",
        "fholly == 'shy'", "hollysmileshyb.png",
        "fholly == 'serious'", "hollyseriousb.png",
        "fholly == 'mad'", "hollymadb.png",
        "fholly == 'smile'", "hollysmileb.png",
        "fholly == 'happy'", "hollyhappyb.png",
        "fholly == 'sad'", "hollysadb.png",
        "fholly == 'blush'", "hollyblushb.png",
        "fholly == 'cry'", "hollycryb.png",
        "fholly == 'happyshy'", "hollyhappyshyb.png",
        "fholly == 'shy'", "hollyshy.png",
        "fholly == 'worried'", "hollyworried.png",
        "fholly == 'n'", "hollyb.png"),
    (0, 0), ConditionSwitch( # GLASSES
        "holly_glasses == False", Null(),
        "holly_glasses == True", "hollyglasses.png")
    )


############################################################# ############################################################# #############################################################
## IVY ############################################################# ############################################################# ############################################################# IVY
############################################################# ############################################################# #############################################################

    # CLOTHES
    
    image ivy = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( # BODY
        "ivy_look == 1", "ivy1.png",
        "ivy_look == 2", "ivygym.png",
        "ivy_look == 'sexy'", "ivy2.png",
        "ivy_look == 'gogo'", "ivy3.png",
        "ivy_look == 5", "ivy4.png"),
    (0, 0), ConditionSwitch( # COSMETICS
        "ivy_navel == False", Null(),
        "ivy_navel == True", "ivy_navel.png"),
    (0, 0), ConditionSwitch( # FACE
        "fivy == 'sad'", "ivysad.png",
        "fivy == 'slut'", "ivyslut.png",
        "fivy == 'flirt'", "ivyflirt.png",
        "fivy == 'mad'", "ivymad.png",
        "fivy == 'serious'", "ivyserious.png",
        "fivy == 'smile'", "ivysmile.png",
        "fivy == 'surprise'", "ivysurprise.png",
        "fivy == 'blush'", "ivyblush.png",
        "fivy == 'n'", "ivy.png")
    )

    image ivy2 = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( # BODY
        "ivy_look == 1", "ivy1_b.png",
        "ivy_look == 2", "ivygym_b.png",
        "ivy_look == 'sexy'", "ivy2_b.png",
        "ivy_look == 'gogo'", "ivy3_b.png",
        "ivy_look == 5", "ivy4_b.png"),
    (0, 0), ConditionSwitch( # COSMETICS
        "ivy_navel == False", Null(),
        "ivy_navel == True", "ivy_navel.png"),
    (0, 0), ConditionSwitch( # FACE
        "fivy == 'sad'", "ivysad.png",
        "fivy == 'slut'", "ivyslut.png",
        "fivy == 'flirt'", "ivyflirt.png",
        "fivy == 'mad'", "ivymad.png",
        "fivy == 'serious'", "ivyserious.png",
        "fivy == 'smile'", "ivysmile.png",
        "fivy == 'surprise'", "ivysurprise.png",
        "fivy == 'blush'", "ivyblush.png",
        "fivy == 'n'", "ivy.png")
    )

    # UNDERWEAR
    
    image ivybra = Composite(
    (640, 1080), 
    (0, 0), "ivybra.png" ,  
    (0, 0), ConditionSwitch( # COSMETICS
        "ivy_navel == False", Null(),
        "ivy_navel == True", "ivy_navel.png"),
    (0, 0), ConditionSwitch( # FACE
        "fivy == 'sad'", "ivysad.png",
        "fivy == 'slut'", "ivyslut.png",
        "fivy == 'flirt'", "ivyflirt.png",
        "fivy == 'mad'", "ivymad.png",
        "fivy == 'serious'", "ivyserious.png",
        "fivy == 'smile'", "ivysmile.png",
        "fivy == 'surprise'", "ivysurprise.png",
        "fivy == 'blush'", "ivyblush.png",
        "fivy == 'n'", "ivy.png")
    )

    image ivybra2 = Composite(
    (640, 1080), 
    (0, 0), "ivybra_b.png", 
    (0, 0), ConditionSwitch( # COSMETICS
        "ivy_navel == False", Null(),
        "ivy_navel == True", "ivy_navel.png"),
    (0, 0), ConditionSwitch( # FACE
        "fivy == 'sad'", "ivysad.png",
        "fivy == 'slut'", "ivyslut.png",
        "fivy == 'flirt'", "ivyflirt.png",
        "fivy == 'mad'", "ivymad.png",
        "fivy == 'serious'", "ivyserious.png",
        "fivy == 'smile'", "ivysmile.png",
        "fivy == 'surprise'", "ivysurprise.png",
        "fivy == 'blush'", "ivyblush.png",
        "fivy == 'n'", "ivy.png")
    )

    # NUDE
    
    image ivynude = Composite(
    (640, 1080), 
    (0, 0), "ivynude.png",  
    (0, 0), ConditionSwitch( # COSMETICS
        "ivy_navel == False", Null(),
        "ivy_navel == True", "ivy_navel.png"),
    (0, 0), ConditionSwitch( # FACE
        "fivy == 'sad'", "ivysad.png",
        "fivy == 'slut'", "ivyslut.png",
        "fivy == 'flirt'", "ivyflirt.png",
        "fivy == 'mad'", "ivymad.png",
        "fivy == 'serious'", "ivyserious.png",
        "fivy == 'smile'", "ivysmile.png",
        "fivy == 'surprise'", "ivysurprise.png",
        "fivy == 'blush'", "ivyblush.png",
        "fivy == 'n'", "ivy.png")
    )
    
    image ivynude2 = Composite(
    (640, 1080), 
    (0, 0), "ivynude_b.png",  
    (0, 0), ConditionSwitch( # COSMETICS
        "ivy_navel == False", Null(),
        "ivy_navel == True", "ivy_navel.png"),
    (0, 0), ConditionSwitch( # FACE
        "fivy == 'sad'", "ivysad.png",
        "fivy == 'slut'", "ivyslut.png",
        "fivy == 'flirt'", "ivyflirt.png",
        "fivy == 'mad'", "ivymad.png",
        "fivy == 'serious'", "ivyserious.png",
        "fivy == 'smile'", "ivysmile.png",
        "fivy == 'surprise'", "ivysurprise.png",
        "fivy == 'blush'", "ivyblush.png",
        "fivy == 'n'", "ivy.png")
    )

############################################################# ############################################################# #############################################################
## JEREMY ############################################################# ############################################################# ############################################################# JEREMY
############################################################# ############################################################# #############################################################

    # CLOTHES
    
    image jeremy = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( #BODY
        "jeremy_look == 2", "jeremygym.png",
        "jeremy_look == 3", "jeremy1b.png",
        "jeremy_look == 1", "jeremy1.png"),
    (0, 0), ConditionSwitch( # FACE
        "fjeremy == 'serious'", "jeremyserious.png",
        "fjeremy == 'evil'", "jeremyevil.png",
        "fjeremy == 'flirt'", "jeremyflirt.png",
        "fjeremy == 'surprise'", "jeremysurprise.png",
        "fjeremy == 'happy'", "jeremyhappy.png",
        "fjeremy == 'mad'", "jeremymad.png",
        "fjeremy == 'sad'", "jeremysad.png",
        "fjeremy == 'smile'", "jeremysmile.png",
        "fjeremy == 'n'", "jeremy.png")
    )
    
    # NUDE
    
    image jeremynude = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( #BODY
        "jeremy_look == 2", "jeremy_noshirt.png",
        "jeremy_look == 1", "jeremynude.png"),
    (0, 0), ConditionSwitch( # FACE
        "fjeremy == 'serious'", "jeremyserious.png",
        "fjeremy == 'evil'", "jeremyevil.png",
        "fjeremy == 'flirt'", "jeremyflirt.png",
        "fjeremy == 'surprise'", "jeremysurprise.png",
        "fjeremy == 'happy'", "jeremyhappy.png",
        "fjeremy == 'mad'", "jeremymad.png",
        "fjeremy == 'sad'", "jeremysad.png",
        "fjeremy == 'smile'", "jeremysmile.png",
        "fjeremy == 'n'", "jeremy.png")
    )


############################################################# ############################################################# #############################################################
## LOUISE ############################################################# ############################################################# ############################################################# LOUISE
############################################################# ############################################################# #############################################################

    # CLOTHES
    
    image louise = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( #BODY
        "louise_look == 1", "louise1.png",
        "louise_look == 2", "louise2.png",
        "louise_look == 3", "louise3.png"),
    (0, 0), ConditionSwitch( # FACE
        "flouise == 'sad'", "louisesad.png",
        "flouise == 'happy'", "louisehappy.png",
        "flouise == 'mad'", "louisemad.png",
        "flouise == 'blush'", "louiseblush.png",
        "flouise == 'serious'", "louiseserious.png",
        "flouise == 'smile'", "louisesmile.png",
        "flouise == 'surprise'", "louisesurprise.png",
        "flouise == 'flirt'", "louiseflirt.png",
        "flouise == 'slut'", "louiseslut.png",
        "flouise == 'cry'", "louisecry.png",
        "flouise == 'n'", "louise.png")
    )
        
    image louise2 = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( #BODY
        "louise_look == 1", "louise1_b.png",
        "louise_look == 2", "louise2_b.png",
        "louise_look == 3", "louise3_b.png"),
    (0, 0), ConditionSwitch( # FACE
        "flouise == 'sad'", "louisesad.png",
        "flouise == 'happy'", "louisehappy.png",
        "flouise == 'mad'", "louisemad.png",
        "flouise == 'blush'", "louiseblush.png",
        "flouise == 'serious'", "louiseserious.png",
        "flouise == 'smile'", "louisesmile.png",
        "flouise == 'surprise'", "louisesurprise.png",
        "flouise == 'flirt'", "louiseflirt.png",
        "flouise == 'slut'", "louiseslut.png",
        "flouise == 'cry'", "louisecry.png",
        "flouise == 'n'", "louise.png")
    )
        
    # UNDERWEAR
    
    image louisebra = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( #BODY
        "louise_look == 1", "louisebra.png",
        "louise_look == 3", "louisetopless.png",
        "louise_look == 2", "louisecomfy.png"),
    (0, 0), ConditionSwitch( # FACE
        "flouise == 'sad'", "louisesad.png",
        "flouise == 'happy'", "louisehappy.png",
        "flouise == 'mad'", "louisemad.png",
        "flouise == 'blush'", "louiseblush.png",
        "flouise == 'serious'", "louiseserious.png",
        "flouise == 'smile'", "louisesmile.png",
        "flouise == 'surprise'", "louisesurprise.png",
        "flouise == 'flirt'", "louiseflirt.png",
        "flouise == 'slut'", "louiseslut.png",
        "flouise == 'cry'", "louisecry.png",
        "flouise == 'n'", "louise.png")
    )
    image louisebra2 = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( #BODY
        "louise_look == 1", "louisebra_b.png",
        "louise_look == 3", "louisetopless_b.png",
        "louise_look == 2", "louisecomfy_b.png"),
    (0, 0), ConditionSwitch( # FACE
        "flouise == 'sad'", "louisesad.png",
        "flouise == 'happy'", "louisehappy.png",
        "flouise == 'mad'", "louisemad.png",
        "flouise == 'blush'", "louiseblush.png",
        "flouise == 'serious'", "louiseserious.png",
        "flouise == 'smile'", "louisesmile.png",
        "flouise == 'surprise'", "louisesurprise.png",
        "flouise == 'flirt'", "louiseflirt.png",
        "flouise == 'slut'", "louiseslut.png",
        "flouise == 'cry'", "louisecry.png",
        "flouise == 'n'", "louise.png")
    )
        
    # NUDE
    image louisenude = Composite(
    (640, 1080), 
    (0, 0), "louisenude.png",
    (0, 0), ConditionSwitch( # FACE
        "flouise == 'sad'", "louisesad.png",
        "flouise == 'happy'", "louisehappy.png",
        "flouise == 'mad'", "louisemad.png",
        "flouise == 'blush'", "louiseblush.png",
        "flouise == 'serious'", "louiseserious.png",
        "flouise == 'smile'", "louisesmile.png",
        "flouise == 'surprise'", "louisesurprise.png",
        "flouise == 'flirt'", "louiseflirt.png",
        "flouise == 'slut'", "louiseslut.png",
        "flouise == 'cry'", "louisecry.png",
        "flouise == 'n'", "louise.png")
    )
    image louisenude2 = Composite(
    (640, 1080), 
    (0, 0), "louisenude_b.png",
    (0, 0), ConditionSwitch( # FACE
        "flouise == 'sad'", "louisesad.png",
        "flouise == 'happy'", "louisehappy.png",
        "flouise == 'mad'", "louisemad.png",
        "flouise == 'blush'", "louiseblush.png",
        "flouise == 'serious'", "louiseserious.png",
        "flouise == 'smile'", "louisesmile.png",
        "flouise == 'surprise'", "louisesurprise.png",
        "flouise == 'flirt'", "louiseflirt.png",
        "flouise == 'slut'", "louiseslut.png",
        "flouise == 'cry'", "louisecry.png",
        "flouise == 'n'", "louise.png")
    )
 
############################################################# ############################################################# #############################################################
## MINERVA ############################################################# ############################################################# ############################################################# MINERVA
############################################################# ############################################################# #############################################################
 
    # CLOTHES
    
    image minerva = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( #BODY
        "minerva_look == 1", "minerva1.png",
        "minerva_look == 2", "minervagym.png",
        "minerva_look == 3", "minerva3.png"),
    (0, 0), ConditionSwitch( # FACE
        "fminerva == 'mad'", "minervamad.png",
        "fminerva == 'smile'", "minervasmile.png",
        "fminerva == 'furious'", "minervafurious.png",
        "fminerva == 'sad'", "minervasad.png",
        "fminerva == 'flirt'", "minervaflirt.png",
        "fminerva == 'n'", "minerva.png")
    )
    
    # NUDE
    
    image minervanude = Composite(
    (640, 1080), 
    (0, 0), "minervanude.png",
    (0, 0), ConditionSwitch( # FACE
        "fminerva == 'mad'", "minervamad.png",
        "fminerva == 'smile'", "minervasmile.png",
        "fminerva == 'furious'", "minervafurious.png",
        "fminerva == 'sad'", "minervasad.png",
        "fminerva == 'flirt'", "minervaflirt.png",
        "fminerva == 'n'", "minerva.png")
    )
 
############################################################# ############################################################# #############################################################
## PERRY ############################################################# ############################################################# ############################################################# PERRY
############################################################# ############################################################# #############################################################


    # CLOTHES
    
    image perry = Composite(
    (640, 1080), 
    (0, 0), "perry1.png",
    (0, 0), ConditionSwitch( # FACE
        "fperry == 'sad'", "perrysadb.png",
        "fperry == 'happy'", "perryhappyb.png",
        "fperry == 'smile'", "perryhappyb.png",
        "fperry == 'mad'", "perrymadb.png",
        "fperry == 'meh'", "perrymehb.png",
        "fperry == 'serious'", "perryseriousb.png",
        "fperry == 'surprise'", "perrysurpriseb.png",
        "fperry == 'flirt'", "perryflirtb.png",
        "fperry == 'n'", "perryb.png"),
    (0, 0), ConditionSwitch( # GLASSES
        "perry_glasses == False", Null(),
        "perry_glasses == True", "perryglasses.png")
    )
    
    image perry2 = Composite(
    (640, 1080), 
    (0, 0), "perry2.png",
    (0, 0), ConditionSwitch( # FACE
        "fperry == 'sad'", "perrysadb.png",
        "fperry == 'happy'", "perryhappyb.png",
        "fperry == 'smile'", "perryhappyb.png",
        "fperry == 'mad'", "perrymadb.png",
        "fperry == 'meh'", "perrymehb.png",
        "fperry == 'serious'", "perryseriousb.png",
        "fperry == 'surprise'", "perrysurpriseb.png",
        "fperry == 'flirt'", "perryflirtb.png",
        "fperry == 'n'", "perryb.png"),
    (0, 0), ConditionSwitch( # GLASSES
        "perry_glasses == False", Null(),
        "perry_glasses == True", "perryglasses.png")
    )


############################################################# ############################################################# #############################################################
## ROBERT ############################################################# ############################################################# ############################################################# ROBERT
############################################################# ############################################################# #############################################################

    # CLOTHES
    
    image robert = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( # BODY
        "robert_look == 1", "robert1.png",
        "robert_look == 2", "robert2.png"),
    (0, 0), ConditionSwitch( # FACE
        "frobert == 'flirt'", "robertflirt.png",
        "frobert == 'mad'", "robertmad.png",
        "frobert == 'sad'", "robertsad.png",
        "frobert == 'smile'", "robertsmile.png",
        "frobert == 'serious'", "robertserious.png",
        "frobert == 'evil'", "robertevil.png",
        "frobert == 'n'", "robert.png"),
    (0, 0), ConditionSwitch( # SPLASH
        "robert_splash == False", Null(),
        "robert_splash == True", "robert_splash.png"),
    (0, 0), ConditionSwitch( # HURT
        "robert_hurt == 0", Null(),
        "robert_hurt == 1", "roberthurt.png",
        "robert_hurt == 2", "roberthurt2.png")    
    )

    # UNDERWEAR
    image robertunder = Composite(
    (640, 1080),
    (0, 0), "robertnoshirt.png",
    (0, 0), ConditionSwitch( # FACE
        "frobert == 'flirt'", "robertflirt.png",
        "frobert == 'mad'", "robertmad.png",
        "frobert == 'sad'", "robertsad.png",
        "frobert == 'smile'", "robertsmile.png",
        "frobert == 'serious'", "robertserious.png",
        "frobert == 'evil'", "robertevil.png",
        "frobert == 'n'", "robert.png"),
    (0, 0), ConditionSwitch( # HURT
        "robert_hurt == 0", Null(),
        "robert_hurt == 1", "roberthurt.png",
        "robert_hurt == 2", "roberthurt2.png") 
    )
    
    # NUDE
    
    image robertnude = Composite(
    (640, 1080),
    (0, 0), "robertnude.png",
    (0, 0), ConditionSwitch( # FACE
        "frobert == 'flirt'", "robertflirt.png",
        "frobert == 'mad'", "robertmad.png",
        "frobert == 'sad'", "robertsad.png",
        "frobert == 'smile'", "robertsmile.png",
        "frobert == 'serious'", "robertserious.png",
        "frobert == 'evil'", "robertevil.png",
        "frobert == 'n'", "robert.png"),
    (0, 0), ConditionSwitch( # HURT
        "robert_hurt == 0", Null(),
        "robert_hurt == 1", "roberthurt.png",
        "robert_hurt == 2", "roberthurt2.png") 
    )

############################################################# ############################################################# #############################################################
## SEYMOUR ############################################################# ############################################################# ############################################################# SEYMOUR
############################################################# ############################################################# #############################################################

    # CLOTHES
    
    image seymour = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch ( # BODY  
        "seymour_look == 1", "seymour1.png",
        "seymour_look == 2", "seymour2.png"),
    (0, 0), ConditionSwitch( # FACE
        "fseymour == 'sad'", "seymoursad.png",
        "fseymour == 'happy'", "seymourhappy.png",
        "fseymour == 'serious'", "seymourserious.png",
        "fseymour == 'smile'", "seymoursmile.png",
        "fseymour == 'surprise'", "seymoursurprise.png",
        "fseymour == 'evil'", "seymourevil.png",
        "fseymour == 'mad'", "seymourmad.png",
        "fseymour == 'n'", "seymour.png")
    )
        
    image seymour2 = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch ( # BODY  
        "seymour_look == 1", "seymour1_b.png",
        "seymour_look == 2", "seymour2_b.png"),
    (0, 0), ConditionSwitch( # FACE
        "fseymour == 'sad'", "seymoursad.png",
        "fseymour == 'happy'", "seymourhappy.png",
        "fseymour == 'serious'", "seymourserious.png",
        "fseymour == 'smile'", "seymoursmile.png",
        "fseymour == 'surprise'", "seymoursurprise.png",
        "fseymour == 'evil'", "seymourevil.png",
        "fseymour == 'mad'", "seymourmad.png",
        "fseymour == 'n'", "seymour.png")
    )
        
    # NUDE
    
    image seymournude = Composite(
    (640, 1080), 
    (0, 0), "seymournude.png",
    (0, 0), ConditionSwitch( # FACE
        "fseymour == 'sad'", "seymoursad.png",
        "fseymour == 'happy'", "seymourhappy.png",
        "fseymour == 'serious'", "seymourserious.png",
        "fseymour == 'smile'", "seymoursmile.png",
        "fseymour == 'surprise'", "seymoursurprise.png",
        "fseymour == 'evil'", "seymourevil.png",
        "fseymour == 'mad'", "seymourmad.png",
        "fseymour == 'n'", "seymour.png")
    )
    
    
############################################################# ############################################################# #############################################################
## STAN ############################################################# ############################################################# ############################################################# STAN
############################################################# ############################################################# #############################################################

    # CLOTHES

    image stan = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( # BODY
        "stan_look == 3", "stan3.png",
        "stan_look == 2", "stan2.png",
        "stan_look == 1", "stan1.png"),
    (0, 0), ConditionSwitch( # FACES
        "fstan == 'surprise'", "stansurprise.png",
        "fstan == 'smile'", "stansmile.png",
        "fstan == 'shy'", "stanshy.png",
        "fstan == 'serious'", "stanserious.png",
        "fstan == 'sad'", "stansad.png",
        "fstan == 'perv'", "stanperv.png",
        "fstan == 'mad'", "stanmad.png",
        "fstan == 'happy'", "stanhappy.png",
        "fstan == 'blush'", "stanblush.png",
        "fstan == 'n'", "stan.png"),
    (0, 0), ConditionSwitch( # CAMERA
        "stan_camera == False", Null(),
        "stan_camera == True", "stancamera.png")
    )
        
    image stan2 = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( # BODY
        "stan_look == 2", "stan1_b.png",
        "stan_look == 1", "stan1_c.png"),
    (0, 0), ConditionSwitch( # FACES
        "fstan == 'surprise'", "stansurprise.png",
        "fstan == 'smile'", "stansmile.png",
        "fstan == 'shy'", "stanshy.png",
        "fstan == 'serious'", "stanserious.png",
        "fstan == 'sad'", "stansad.png",
        "fstan == 'perv'", "stanperv.png",
        "fstan == 'mad'", "stanmad.png",
        "fstan == 'happy'", "stanhappy.png",
        "fstan == 'blush'", "stanblush.png",
        "fstan == 'n'", "stan.png"),
    (0, 0), ConditionSwitch( # CAMERA
        "stan_camera == False", Null(),
        "stan_camera == True", "stancamera.png")
    )
        
    # NUDE
    
    image stannude = Composite(
    (640, 1080), 
    (0, 0), "stannude.png",
    (0, 0), ConditionSwitch( # FACES
        "fstan == 'surprise'", "stansurprise.png",
        "fstan == 'smile'", "stansmile.png",
        "fstan == 'shy'", "stanshy.png",
        "fstan == 'serious'", "stanserious.png",
        "fstan == 'sad'", "stansad.png",
        "fstan == 'perv'", "stanperv.png",
        "fstan == 'mad'", "stanmad.png",
        "fstan == 'happy'", "stanhappy.png",
        "fstan == 'blush'", "stanblush.png",
        "fstan == 'n'", "stan.png"),
    (0, 0), ConditionSwitch( # CAMERA
        "stan_camera == False", Null(),
        "stan_camera == True", "stancamera.png")
    )
        
    image stannude2 = Composite(
    (640, 1080), 
    (0, 0), "stannude_soft.png",
    (0, 0), ConditionSwitch( # FACES
        "fstan == 'surprise'", "stansurprise.png",
        "fstan == 'smile'", "stansmile.png",
        "fstan == 'shy'", "stanshy.png",
        "fstan == 'serious'", "stanserious.png",
        "fstan == 'sad'", "stansad.png",
        "fstan == 'perv'", "stanperv.png",
        "fstan == 'mad'", "stanmad.png",
        "fstan == 'happy'", "stanhappy.png",
        "fstan == 'blush'", "stanblush.png",
        "fstan == 'n'", "stan.png"),
    (0, 0), ConditionSwitch( # CAMERA
        "stan_camera == False", Null(),
        "stan_camera == True", "stancamera.png")
    )

############################################################# ############################################################# #############################################################
## VAN DYKES ############################################################# ############################################################# ############################################################# VAN DYKES
############################################################# ############################################################# #############################################################

    # MOLLY
    
    image molly = Composite(
    (640, 1080),
    (0, 0), "molly1.png",
    (0, 0), ConditionSwitch( # FACE
        "fmolly == 'sad'", "mollysad.png",
        "fmolly == 'smile'", "mollysmile.png",
        "fmolly == 'mad'", "mollymad.png",
        "fmolly == 'serious'", "mollyserious.png",
        "fmolly == 'n'", "molly.png")
    )
    
    # ED
    
    image ed = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch ( # BODY  
        "ed_look == 1", "ed1.png",
        "ed_look == 2", "ed2.png"),
    (0, 0), ConditionSwitch( # FACE
        "fed == 'perv'", "edperv.png",
        "fed == 'smile'", "edsmile.png",
        "fed == 'surprise'", "edsurprise.png",
        "fed == 'mad'", "edmad.png",
        "fed == 'sad'", "edsad.png",
        "fed == 'n'", "ed.png")
    )
    

############################################################# ############################################################# #############################################################
## WADE ############################################################# ############################################################# ############################################################# WADE
############################################################# ############################################################# #############################################################

    # CLOTHES

    image wade = Composite(
    (640, 1080),
    (0, 0), "wade1.png",
    (0, 0), ConditionSwitch( # FACE
        "fwade == 'sad'", "wadesad.png",
        "fwade == 'happy'", "wadehappy.png",
        "fwade == 'smile'", "wadesmile.png",
        "fwade == 'serious'", "wadeserious.png",
        "fwade == 'mad'", "wademad.png",
        "fwade == 'surprise'", "wadesurprise.png",
        "fwade == 'n'", "wade.png")
    )
    image wade2 = Composite(
    (640, 1080),
    (0, 0), "wade2.png",
    (0, 0), ConditionSwitch( # FACE
        "fwade == 'sad'", "wadesad.png",
        "fwade == 'happy'", "wadehappy.png",
        "fwade == 'smile'", "wadesmile.png",
        "fwade == 'serious'", "wadeserious.png",
        "fwade == 'mad'", "wademad.png",
        "fwade == 'surprise'", "wadesurprise.png",
        "fwade == 'n'", "wade.png")
    )
    image wade3 = Composite(
    (640, 1080),
    (0, 0), "wade3.png",
    (0, 0), ConditionSwitch( # FACE
        "fwade == 'sad'", "wadesad.png",
        "fwade == 'happy'", "wadehappy.png",
        "fwade == 'smile'", "wadesmile.png",
        "fwade == 'serious'", "wadeserious.png",
        "fwade == 'mad'", "wademad.png",
        "fwade == 'surprise'", "wadesurprise.png",
        "fwade == 'n'", "wade.png")
    )
         
############################################################# ############################################################# #############################################################
## PARENTS ############################################################# ############################################################# ############################################################# PARENTS
############################################################# ############################################################# #############################################################

    # MOM
    
    image mom = Composite(
    (640, 1080),
    (0, 0), "mom1.png",
    (0, 0), ConditionSwitch( # FACE
        "fmom == 'sad'", "momsad.png",
        "fmom == 'smile'", "momsmile.png",
        "fmom == 'surprise'", "momsurprise.png",
        "fmom == 'serious'", "momserious.png",
        "fmom == 'cry'", "momcry.png",
        "fmom == 'n'", "mom.png")
    )

    # DAD
    
    image dad = Composite(
    (640, 1080),
    (0, 0), "dad1.png",
    (0, 0), ConditionSwitch( # FACE
        "fdad == 'sad'", "dadsad.png",
        "fdad == 'smile'", "dadsmile.png",
        "fdad == 'mad'", "dadmad.png",
        "fdad == 'n'", "mom.png")
    )


############################################################# ############################################################# #############################################################
## MIKE SPRITES ############################################################# ############################################################# ############################################################# 
############################################################# ############################################################# #############################################################
label mike_sprites:
    
    $ fmike = "n"
    $ mike_look = 1
    $ mike_hurt = 0
    $ mike_extras = 0
    
    # CLOTHES
     
    image mike = Composite(
    (640, 1080), 
    (0, 0), "mike1.png",
    (0, 0), ConditionSwitch( # FACE
        "fmike == 'sad'", "mikesad.png",
        "fmike == 'happy'", "mikehappy.png",
        "fmike == 'smile'", "mikesmile.png",
        "fmike == 'blush'", "mikeblush.png",
        "fmike == 'mad'", "mikemad.png",
        "fmike == 'serious'", "mikeserious.png",
        "fmike == 'flirt'", "mikeflirt.png",
        "fmike == 'worried'", "mikeworried.png",
        "fmike == 'n'", "mike.png")
    )
    
    image mike2 = Composite(
    (640, 1080), 
    (0, 0), "mike2.png",
    (0, 0), ConditionSwitch( # FACE
        "fmike == 'sad'", "mikesad.png",
        "fmike == 'happy'", "mikehappy.png",
        "fmike == 'smile'", "mikesmile.png",
        "fmike == 'blush'", "mikeblush.png",
        "fmike == 'mad'", "mikemad.png",
        "fmike == 'serious'", "mikeserious.png",
        "fmike == 'flirt'", "mikeflirt.png",
        "fmike == 'worried'", "mikeworried.png",
        "fmike == 'n'", "mike.png")
    )

    image mikenude = Composite(
    (640, 1080), 
    (0, 0), "mikenude.png",
    (0, 0), ConditionSwitch( # FACE
        "fmike == 'sad'", "mikesad.png",
        "fmike == 'happy'", "mikehappy.png",
        "fmike == 'smile'", "mikesmile.png",
        "fmike == 'blush'", "mikeblush.png",
        "fmike == 'mad'", "mikemad.png",
        "fmike == 'serious'", "mikeserious.png",
        "fmike == 'flirt'", "mikeflirt.png",
        "fmike == 'worried'", "mikeworried.png",
        "fmike == 'n'", "mike.png")
    )
    
    if chapter == 5:
        jump v5lenafriday

jump define_galleries