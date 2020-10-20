  
################################################################################################################################################################################################
#### LEVEL UP SCREENS ##########################################################################################################################################################################
################################################################################################################################################################################################       

screen skillsup:
    
    if ian_active:
        if ian_wits_xp > 2:
            timer 0.3 action [ Play ("ch_one", "sfx/levelup.mp3") ]
            imagebutton idle "gui/levelup_wits.png" focus_mask None action [ Play ("ch_one", "sfx/phone_back.mp3") ] , SetVariable("ian_wits", ian_wits+1) , SetVariable("ian_wits_xp", ian_wits_xp-3) , Return at fade_in_skill
            
        elif ian_charisma_xp > 2:
            timer 0.3 action [ Play ("ch_one", "sfx/levelup.mp3") ]
            imagebutton idle "gui/levelup_charisma.png" focus_mask None action [ Play ("ch_one", "sfx/phone_back.mp3") ] , SetVariable("ian_charisma", ian_charisma+1) , SetVariable("ian_charisma_xp", ian_charisma_xp-3) , Return at fade_in_skill
        
        elif ian_athletics_xp > 2:
            timer 0.3 action [ Play ("ch_one", "sfx/levelup.mp3") ]
            imagebutton idle "gui/levelup_athletics.png" focus_mask None action [ Play ("ch_one", "sfx/phone_back.mp3") ] , SetVariable("ian_athletics", ian_athletics+1) , SetVariable("ian_athletics_xp", ian_athletics_xp-3) , Return at fade_in_skill
        
        elif ian_lust_xp > 2:
            timer 0.3 action [ Play ("ch_one", "sfx/levelup.mp3") ]
            imagebutton idle "gui/levelup_lust.png" focus_mask None action [ Play ("ch_one", "sfx/phone_back.mp3") ] , SetVariable("ian_lust", ian_lust+1) , SetVariable("ian_lust_xp", ian_lust_xp-3) , Return at fade_in_skill
        else:
            timer 0.1 action Return
    elif lena_active:
        if lena_wits_xp > 2:
            timer 0.3 action [ Play ("ch_one", "sfx/levelup.mp3") ]
            imagebutton idle "gui/levelup_wits.png" focus_mask None action [ Play ("ch_one", "sfx/phone_back.mp3") ] , SetVariable("lena_wits", lena_wits+1) , SetVariable("lena_wits_xp", lena_wits_xp-3) , Return at fade_in_skill
       
        elif lena_charisma_xp > 2:
            timer 0.3 action [ Play ("ch_one", "sfx/levelup.mp3") ]
            imagebutton idle "gui/levelup_charisma.png" focus_mask None action [ Play ("ch_one", "sfx/phone_back.mp3") ] , SetVariable("lena_charisma", lena_charisma+1) , SetVariable("lena_charisma_xp", lena_charisma_xp-3) , Return at fade_in_skill
       
        elif lena_athletics_xp > 2:
            timer 0.3 action [ Play ("ch_one", "sfx/levelup.mp3") ]
            imagebutton idle "gui/levelup_athletics.png" focus_mask None action [ Play ("ch_one", "sfx/phone_back.mp3") ] , SetVariable("lena_athletics", lena_athletics+1) , SetVariable("lena_athletics_xp", lena_athletics_xp-3) ,  Return at fade_in_skill
    
        elif lena_lust_xp > 2:
            timer 0.3 action [ Play ("ch_one", "sfx/levelup.mp3") ]
            imagebutton idle "gui/levelup_lust.png" focus_mask None action [ Play ("ch_one", "sfx/phone_back.mp3") ] , SetVariable("lena_lust", lena_lust+1) , SetVariable("lena_lust_xp", lena_lust_xp-3) , Return at fade_in_skill
        else:
            timer 0.1 action Return            

screen willup:
    if ian_active:
        timer 0.3 action [ Play ("ch_one", "sfx/willup.mp3") ]
        imagebutton idle "gui/levelup_will.png" focus_mask None action [ Play ("ch_one", "sfx/phone_back.mp3") ] , SetVariable("ian_will", ian_will+1) , Return at fade_in_skill
    if lena_active:
        timer 0.3 action [ Play ("ch_one", "sfx/willup.mp3") ]
        imagebutton idle "gui/levelup_will.png" focus_mask None action [ Play ("ch_one", "sfx/phone_back.mp3") ] , SetVariable("lena_will", lena_will+1) , Return at fade_in_skill

################################################################################################################################################################################################
#### UI SCREENS ################################################################################################################################################################################
################################################################################################################################################################################################



#############################################################################################
## TEXTBOX  #################################################################

screen ui:
    zorder 100
    
    imagebutton idle "gui/menu_icon.png" hover "gui/menu_icon_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_up.ogg") ] , ShowMenu('phone')

screen stats_ingame:
    imagebutton idle "gui/stat_popup.png"
    vbox:
        if ian_active:
            text "{font=big_noodle_titling_oblique.ttf}{color=#000000}[ian_wits]{/color}":
                size 30
                xpos 1815 ypos 390
            text "{font=big_noodle_titling_oblique.ttf}{color=#000000}[ian_charisma]{/color}":
                size 30
                xpos 1815 ypos 447
            text "{font=big_noodle_titling_oblique.ttf}{color=#000000}[ian_athletics]{/color}":
                size 30
                xpos 1815 ypos 504
            text "{font=big_noodle_titling_oblique.ttf}{color=#000000}[ian_lust]{/color}":
                size 30
                xpos 1815 ypos 561
            text "{font=big_noodle_titling_oblique.ttf}{color=#000000}[ian_money]{/color}":
                size 30
                xpos 1815 ypos 618
            text "{font=big_noodle_titling_oblique.ttf}{color=#E0CE39}[ian_will]{/color}":
                size 30
                xpos 1815 ypos 675
        
        elif lena_active:
            text "{font=big_noodle_titling_oblique.ttf}{color=#000000}[lena_wits]{/color}":
                size 30
                xpos 1815 ypos 390
            text "{font=big_noodle_titling_oblique.ttf}{color=#000000}[lena_charisma]{/color}":
                size 30
                xpos 1815 ypos 447
            text "{font=big_noodle_titling_oblique.ttf}{color=#000000}[lena_athletics]{/color}":
                size 30
                xpos 1815 ypos 504
            text "{font=big_noodle_titling_oblique.ttf}{color=#000000}[lena_lust]{/color}":
                size 30
                xpos 1815 ypos 561
            text "{font=big_noodle_titling_oblique.ttf}{color=#000000}[lena_money]{/color}":
                size 30
                xpos 1815 ypos 618
            text "{font=big_noodle_titling_oblique.ttf}{color=#E0CE39}[lena_will]{/color}":
                size 30
                xpos 1815 ypos 675
        
#############################################################################################
## PHONE MENU needs animation ###################################################

screen phone:
   
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        imagebutton idle "gui/icon_stats.png" hover "gui/icon_stats_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_stats')
        imagebutton idle "gui/icon_agenda.png" hover "gui/icon_agenda_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_agenda')
        imagebutton idle "gui/icon_budget.png" hover "gui/icon_budget_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_budget')
        imagebutton idle "gui/icon_save.png" hover "gui/icon_save_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_save')
        imagebutton idle "gui/icon_load.png" hover "gui/icon_load_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_load')
        imagebutton idle "gui/icon_settings.png" hover "gui/icon_settings_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_settings')
        imagebutton idle "gui/icon_mainmenu.png" hover "gui/icon_mainmenu_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , MainMenu()
        imagebutton idle "gui/icon_patreon.png" hover "gui/icon_patreon_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_patreon')
        imagebutton idle "gui/icon_gallery.png" hover "gui/icon_gallery_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_gallery')
        imagebutton idle "gui/icon_back.png" hover "gui/icon_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_down.mp3") ] , Return()
        imagebutton idle "gui/icon_quit.png" hover "gui/icon_quit_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Quit(confirm=not main_menu)
        
    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        imagebutton idle "gui/icon_stats.png" hover "gui/icon_stats_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_stats')
        imagebutton idle "gui/icon_agenda.png" hover "gui/icon_agenda_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_agenda')
        imagebutton idle "gui/icon_budget.png" hover "gui/icon_budget_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_budget')
        imagebutton idle "gui/icon_save.png" hover "gui/icon_save_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_save')
        imagebutton idle "gui/icon_load.png" hover "gui/icon_load_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_load')
        imagebutton idle "gui/icon_settings.png" hover "gui/icon_settings_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_settings')
        imagebutton idle "gui/icon_mainmenu.png" hover "gui/icon_mainmenu_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , MainMenu()
        imagebutton idle "gui/icon_patreon.png" hover "gui/icon_patreon_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_patreon')
        imagebutton idle "gui/icon_gallery.png" hover "gui/icon_gallery_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('phone') , ShowMenu('menu_gallery')
        imagebutton idle "gui/icon_back.png" hover "gui/icon_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_down.mp3") ] , Return()
        imagebutton idle "gui/icon_quit.png" hover "gui/icon_quit_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Quit(confirm=not main_menu)
        
    vbox:
        xpos 120
        ypos 156
        text "{font=big_noodle_titling.ttf}{size=25}{color=#E1E1E1}[day]{/color}"
    vbox:
        xpos 215
        ypos 162
        text "{font=big_noodle_titling.ttf}{size=18} {color=#B7B7B7}[month], week [week]{/color}"

#############################################################################################
## STATS ####################################################################

screen menu_stats:
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        imagebutton idle "gui/header_stats.png" 
        imagebutton idle "gui/header_back.png" hover "gui/header_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] , Hide('menu_stats') , ShowMenu('phone')
        imagebutton idle "gui/subicon_stats.png"
        
        bar:
            value ian_wits_xp
            xysize (161,5)
            range 3
            xpos 173 ypos 427
        bar:
            value ian_charisma_xp
            xysize (158,5)
            range 3
            xpos 173 ypos 559
        bar:
            value ian_athletics_xp
            xysize (157,5)
            range 3
            xpos 173 ypos 692
        bar:
            value ian_lust_xp
            xysize (158,5)
            range 3
            xpos 173 ypos 824    
        
        imagebutton idle "gui/subicon_wits.png" hover "gui/helptext_wits.png" focus_mask True action Null
        imagebutton idle "gui/subicon_charisma.png" hover "gui/helptext_charisma.png" focus_mask True action Null
        imagebutton idle "gui/subicon_athletics.png" hover "gui/helptext_athletics.png" focus_mask True action Null
        imagebutton idle "gui/subicon_lust.png" hover "gui/helptext_lust.png" focus_mask True action Null
        imagebutton idle "gui/subicon_money.png" hover "gui/helptext_money.png" focus_mask True action Null
        imagebutton idle "gui/subicon_will.png" hover "gui/helptext_will.png" focus_mask True action Null
        
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[ian_wits]{/color}":
            size 50
            xpos 235 ypos 360
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[ian_charisma]{/color}":
            size 50
            xpos 235 ypos 490
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[ian_athletics]{/color}":
            size 50
            xpos 235 ypos 625
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[ian_lust]{/color}":
            size 50
            xpos 235 ypos 755
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[ian_money]{/color}":
            size 50
            xpos 485 ypos 495
        text "{font=big_noodle_titling_oblique.ttf}{color=#E0CE39}[ian_will]{/color}":
            size 50
            xpos 485 ypos 630
            
    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        imagebutton idle "gui/header_stats.png" 
        imagebutton idle "gui/header_back.png" hover "gui/header_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] , Hide('menu_stats') , ShowMenu('phone')
        imagebutton idle "gui/subicon_stats.png"
        
        bar:
            value lena_wits_xp
            xysize (161,5)
            range 3
            xpos 173 ypos 427
        bar:
            value lena_charisma_xp
            xysize (158,5)
            range 3
            xpos 173 ypos 559
        bar:
            value lena_athletics_xp
            xysize (157,5)
            range 3
            xpos 173 ypos 692
        bar:
            value lena_lust_xp
            xysize (158,5)
            range 3
            xpos 173 ypos 824    
        
        imagebutton idle "gui/subicon_wits.png" hover "gui/helptext_wits.png" focus_mask True action Null
        imagebutton idle "gui/subicon_charisma.png" hover "gui/helptext_charisma.png" focus_mask True action Null
        imagebutton idle "gui/subicon_athletics.png" hover "gui/helptext_athletics.png" focus_mask True action Null
        imagebutton idle "gui/subicon_lust.png" hover "gui/helptext_lust.png" focus_mask True action Null
        imagebutton idle "gui/subicon_money.png" hover "gui/helptext_money.png" focus_mask True action Null
        imagebutton idle "gui/subicon_will.png" hover "gui/helptext_will.png" focus_mask True action Null
        
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[lena_wits]{/color}":
            size 50
            xpos 235 ypos 360
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[lena_charisma]{/color}":
            size 50
            xpos 235 ypos 490
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[lena_athletics]{/color}":
            size 50
            xpos 235 ypos 625
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[lena_lust]{/color}":
            size 50
            xpos 235 ypos 755
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[lena_money]{/color}":
            size 50
            xpos 485 ypos 495
        text "{font=big_noodle_titling_oblique.ttf}{color=#E0CE39}[lena_will]{/color}":
            size 50
            xpos 485 ypos 630
    
#############################################################################################
## AGENDA #################################################################
 
screen menu_agenda:
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        imagebutton idle "gui/header_agenda.png" 
        imagebutton idle "gui/header_back.png" hover "gui/header_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] , Hide('menu_agenda') , Hide('agenda_screen') , ShowMenu('phone')
        
        vbox:
            style "agenda"
            if ian_agenda:
                 textbutton "{font=big_noodle_titling_oblique.ttf}Ian" action [ Play ("ch_one", "sfx/phone_click.mp3") ] ,  ShowMenu('bio_ian')
            if ian_alison_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Alison" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_alison')
            if ian_axel_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Axel" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_axel')
            if ian_cherry_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Cherry" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_cherry')
            if ian_cindy_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Cindy" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_cindy')
            if ian_emma_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Emma" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_emma')
            if ian_holly_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Holly" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_holly')
            if ian_ivy_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Ivy" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_ivy')
            if ian_jeremy_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Jeremy" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_jeremy')
            if ian_lena_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Lena" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_lena')
            if ian_louise_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Louise" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_louise')
            if chapter > 3 and ian_mayor_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Mayor Vermeer" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_mayor')
            if ian_minerva_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Minerva" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_minerva')
            if ian_perry_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Perry" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_perry') 
            if ian_robert_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Robert" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_robert')
            if ian_seymour_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Seymour" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_seymour')
            if ian_stan_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Stan" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_stan')
            if chapter > 4 and ian_yuri_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Yuri" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_yuri')
            if ian_wade_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Wade" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_wade')
            if ian_wen_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Wen" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_wen')
                
    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        imagebutton idle "gui/header_agenda.png" 
        imagebutton idle "gui/header_back.png" hover "gui/header_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] , Hide('menu_agenda') , Hide('agenda_screen') , ShowMenu('phone')
        
        vbox:
            style "agenda"
            if lena_agenda:
                 textbutton "{font=big_noodle_titling_oblique.ttf}Lena" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_lena')
            if lena_lola_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Lola" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_lola')
            if lena_alison_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Alison" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_alison')
            if lena_axel_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Axel" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_axel')
            if lena_cherry_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Cherry" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_cherry')
            if lena_cindy_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Cindy" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_cindy')
            if lena_lenadad_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Dad" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_dad')
            if lena_danny_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Danny" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_danny')
            if lena_ed_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Ed" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_ed')
            if lena_emma_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Emma" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_emma')
            if lena_holly_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Holly" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_holly')
            if lena_ian_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Ian" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_ian')
            if lena_ivy_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Ivy" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_ivy')
            if lena_jeremy_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Jeremy" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_jeremy')
            if lena_louise_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Louise" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_louise')
            if chapter > 4 and lena_mike_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Mike" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_mike')
            if chapter > 3 and lena_mayor_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Mayor Vermeer" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_mayor')
            if lena_molly_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Molly" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_molly')
            if lena_lenamom_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Mom" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_mom')
            if lena_perry_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Perry" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_perry') 
            if lena_robert_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Robert" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_robert')
            if lena_seymour_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Seymour" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_seymour')
            if lena_stan_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Stan" action [ Play ("ch_one", "sfx/phone_click.mp3") ]  , ShowMenu('bio_stan')
            if lena_wade_agenda:
                textbutton "{font=big_noodle_titling_oblique.ttf}Wade" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , ShowMenu('bio_wade')
            
            
#############################################################################################
## GALLERY ##################################################################################

screen menu_gallery:
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        
        vbox:
            style "agenda"
            
            if ian_alison_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Alison" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_alison')
            if ian_axel_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Axel" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_axel')
            if ian_cherry_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Cherry" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_cherry')
            if ian_cindy_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Cindy" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_cindy')
            if ian_emma_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Emma" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_emma')
            if ian_gillian_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Gillian" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_gillian')
            if ian_holly_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Holly" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_holly')
            if ian_ian_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Ian" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_ian')
            if ian_ivy_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Ivy" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_ivy')
            if ian_jeremy_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Jeremy" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_jeremy')
            if ian_lena_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Lena" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_lena')
            if ian_louise_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Louise" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_louise')
            if ian_minerva_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Minerva" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_minerva')
            if ian_perry_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Perry" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_perry')
            if ian_robert_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Robert" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_robert')
            if ian_seymour_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Seymour" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_seymour')
            if ian_stan_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Stan" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_stan')
            if ian_wade_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Wade" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_wade')
            if ian_misc_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Miscellaneous" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_misc')
     
    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        
        vbox:
            style "agenda"
            
            if lena_alison_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Alison" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_alison')
            if lena_axel_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Axel" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_axel')
            if lena_cindy_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Cindy" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_cindy')
            if lena_emma_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Emma" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_emma')
            if lena_holly_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Holly" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_holly')
            if lena_ian_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Ian" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_Ian')
            if lena_ivy_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Ivy" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_ivy')
            if lena_jeremy_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Jeremy" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_jeremy')
            if lena_lena_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Lena" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_lena')
            if lena_louise_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Louise" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_louise')
            if lena_mike_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Mike" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_mike')
            if lena_minerva_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Minerva" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_minerva')
            if lena_perry_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Perry" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_perry')
            if lena_robert_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Robert" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_robert')
            if lena_seymour_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Seymour" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_seymour')
            if lena_stan_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Stan" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_stan')
            if lena_wade_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Wade" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_wade')
            if lena_misc_gallery:
                textbutton "{font=big_noodle_titling_oblique.ttf}Miscellaneous" action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery') , ShowMenu('menu_gallery_misc')
            
    imagebutton idle "gui/header_gallery.png" 
    imagebutton idle "gui/header_back.png" hover "gui/header_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] , Hide('menu_gallery') , ShowMenu('phone')

#############################################################################################
## BUDGET ####################################################################

screen menu_budget:
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        imagebutton idle "gui/header_budget.png" 
        imagebutton idle "gui/header_back.png" hover "gui/header_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] , Hide('menu_gallery') , ShowMenu('phone')
        
        ## INCOME
        
        if ian_job_magazine == 2 and ian_stipend == 1:
            text "{font=big_noodle_titling_oblique.ttf}{color=#1ED50F}+3{/color}":
                size 50
                xpos 415 ypos 298  
        elif ian_job_magazine == 1 and ian_stipend == 1:
            text "{font=big_noodle_titling_oblique.ttf}{color=#1ED50F}+2{/color}":
                size 50
                xpos 415 ypos 298  
        elif ian_job_magazine == 1 and ian_stipend == 2:
            text "{font=big_noodle_titling_oblique.ttf}{color=#1ED50F}+3{/color}":
                size 50
                xpos 415 ypos 298 
        elif ian_job_magazine == 0 and ian_stipend == 2:
            text "{font=big_noodle_titling_oblique.ttf}{color=#1ED50F}+2{/color}":
                size 50
                xpos 415 ypos 298 
        elif ian_job_magazine == 0 and ian_stipend == 1:
            text "{font=big_noodle_titling_oblique.ttf}{color=#1ED50F}+1{/color}":
                size 50
                xpos 415 ypos 298  
        
        vbox:
            style "budget_income"
            if ian_job_magazine > 0:
                 text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}Magazine internship{/color}   {color=#1ED50F}+[ian_job_magazine]{/color}"
            if ian_stipend > 0:
                 text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}Family stipend{/color}   {color=#1ED50F}+[ian_stipend]{/color}"
                    
        ## EXPENSES
        
        if ian_live_perry:
            text "{font=big_noodle_titling_oblique.ttf}{color=#C20B0B}-2{/color}":
                size 50
                xpos 415 ypos 553            
        else:
            text "{font=big_noodle_titling_oblique.ttf}{color=#C20B0B}-2{/color}":
                size 50
                xpos 415 ypos 553     
        
        vbox:
            style "budget_expenses"
            if ian_live_perry:
                 text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}Rent{/color}   {color=#C20B0B}-1{/color}"
            text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}Living expenses{/color}   {color=#C20B0B}-1{/color}"
                 
        ## GLOBAL
        
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[ian_money]{/color}":
            size 50
            xpos 185 ypos 860
            
        if ian_owed_money == 0:
            text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[ian_owed_money]{/color}":
                size 50
                xpos 455 ypos 860
        else:
            text "{font=big_noodle_titling_oblique.ttf}{color=#C20B0B}[ian_owed_money]{/color}":
                size 50
                xpos 455 ypos 860
        
    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        imagebutton idle "gui/header_budget.png" 
        imagebutton idle "gui/header_back.png" hover "gui/header_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] , Hide('menu_gallery') , ShowMenu('phone')
        
        ## INCOME
        
        if lena_job_cafe == 2 and lena_job_restaurant == 2:
            text "{font=big_noodle_titling_oblique.ttf}{color=#1ED50F}+4{/color}":
                size 50
                xpos 415 ypos 298  
        elif lena_job_cafe == 1 and lena_job_restaurant == 1:
            text "{font=big_noodle_titling_oblique.ttf}{color=#1ED50F}+2{/color}":
                size 50
                xpos 415 ypos 298   
        elif lena_job_restaurant == 1:
            text "{font=big_noodle_titling_oblique.ttf}{color=#1ED50F}+1{/color}":
                size 50
                xpos 415 ypos 298  
        elif lena_job_cafe == 1:
            text "{font=big_noodle_titling_oblique.ttf}{color=#1ED50F}+1{/color}":
                size 50
                xpos 415 ypos 298  
        else:
            text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}+0{/color}":
                size 50
                xpos 415 ypos 298  
        
        vbox:
            style "budget_income"
            if lena_job_cafe == 2:
                text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}Cafe job{/color}   {color=#1ED50F}+2{/color}"
            elif lena_job_cafe == 1:
                text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}Cafe job{/color}   {color=#1ED50F}+1{/color}"
            if lena_job_restaurant == 2:
                text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}Restaurant job{/color}   {color=#1ED50F}+2{/color}"
            elif lena_job_restaurant == 1:
                text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}Restaurant job{/color}   {color=#1ED50F}+1{/color}"
                    
        
        ##EXPENSES
        
        if lena_live_stan_louise:
            text "{font=big_noodle_titling_oblique.ttf}{color=#C20B0B}-3{/color}":
                size 50
                xpos 415 ypos 553           
        else:
            text "{font=big_noodle_titling_oblique.ttf}{color=#C20B0B}-3{/color}":
                size 50
                xpos 415 ypos 553     
            
        vbox:
            style "budget_expenses"
            if lena_live_stan_louise:
                 text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}Rent{/color}   {color=#C20B0B}-2{/color}"
            text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}Living expenses{/color}   {color=#C20B0B}-1{/color}"
                 
       
            
        ## GLOBAL
        
        text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[lena_money]{/color}":
            size 50
            xpos 185 ypos 860
            
        if lena_owed_money == 0:
            text "{font=big_noodle_titling_oblique.ttf}{color=#FFFFFF}[lena_owed_money]{/color}":
                size 50
                xpos 455 ypos 860
        else:
            text "{font=big_noodle_titling_oblique.ttf}{color=#C20B0B}[lena_owed_money]{/color}":
                size 50
                xpos 455 ypos 860


#############################################################################################
## PATREON ############################################################################


screen menu_patreon:
    imagebutton idle "gui/phone_ian.png"
    imagebutton idle "gui/header_patreon.png" 
    imagebutton idle "gui/header_patreon_continue.png" hover "gui/header_patreon_continue_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , OpenURL ("https://www.patreon.com/Evakiss")
    imagebutton idle "gui/header_patreon_back.png" hover "gui/header_patreon_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] ,  Hide('menu_patreon') , ShowMenu('phone')
    

#############################################################################################
## SETTINGS #################################################################################

# Creating a style (style_settings) for placing all game preference options inside the phone
# Also sets the spacing between the display/rollback/skip box and the text/sound box
style style_settings:
    xpos 113
    ypos 275
    spacing 17
   
# Changing the size of the bars for text speed and sound
style style_phonebar:
    xsize 427

# Screen for the menu, together with if-clause depending on which GUI to use    
screen menu_settings:
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
   
    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
   
    imagebutton idle "gui/header_settings.png"
    imagebutton idle "gui/header_back.png" hover "gui/header_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] , Hide('menu_settings') , ShowMenu('phone')

# Initial box for all settings and using the placement style called style_settings       
    vbox:
        style "style_settings"

# Box for the Display, Rollback and Skip columns, altering the spacing between the columns        
        hbox:
            spacing 33
            box_wrap True

            if renpy.variant("pc"):

                vbox:                
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

            vbox:
                label _("Rollback")
                textbutton _("Disable") action Preference("rollback side", "disable")
                textbutton _("Left") action Preference("rollback side", "left")
                textbutton _("Right") action Preference("rollback side", "right")

            vbox:
                label _("Skip")
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
                textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

# Box for all the draggable bars together with if clauses in case the game doesn't use sounds.
# Also setting the bar size with the style called style_phonebar from about 50 lines up
# Text speed settings first
        vbox:
            style "style_phonebar"
            label _("Text Speed")

            bar value Preference("text speed")

            label _("Auto-Forward Time")

            bar value Preference("auto-forward time")

# Music settings
            if config.has_music:
                label _("Music Volume")

                hbox:
                    bar value Preference("music volume")

# Sound settings
            if config.has_sound:

                label _("Sound Volume")

                hbox:
                    bar value Preference("sound volume")
                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)

# Voice volume settings
            if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

# A mute all-button
                textbutton _("Mute All"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"



#############################################################################################
## SAVE SCREEN ##############################################################################


# The screen menu_save opens up a few images, and then calls upon the screen file_slots2,
# which contains the info about the saved games.

screen menu_save:
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
   
    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
   
    imagebutton idle "gui/header_save.png"
    imagebutton idle "gui/header_back.png" hover "gui/header_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] , Hide('menu_save') , ShowMenu('phone')
    use file_slots2(_("Save"))


#############################################################################################
## LOAD SCREEN ##############################################################################

# Same as the menu_save screen, except that it has the command "Load" instead of "Save" when 
# calling the screen file_slots2.

screen menu_load:
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
   
    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
   
    imagebutton idle "gui/header_load.png"
    imagebutton idle "gui/header_back.png" hover "gui/header_back_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] , Hide('menu_load') , ShowMenu('phone')
    use file_slots2(_("Load"))


# File_slots2 is a copy of file_slots from the main menu. A few differences being ypos and xpos
# for the page name button, the grid and the buttons for accessing the other pages.
# The command "use game_menu(title)" from the top of screen file_slots2(title)

screen file_slots2(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
   
    #use game_menu(title):

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on a button.
        button:
            style "page_label"

            key_events True
            ypos 80
            xpos 1150
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xpos 690
            ypos 130

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        hbox:
            style_prefix "page"

            xpos 723
            ypos 945
            #yalign 0.94

            spacing gui.page_spacing

            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1,21):
                textbutton "[page]" action FilePage(page)

            textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")





















#############################################################################################
## TUTORIALS #################################################################################
#############################################################################################

screen tutorial2screen:
    imagebutton idle "gui/tutorial3.png" action Hide('tutorial2screen')  , ShowMenu('tutorial3screen')

screen tutorial3screen:
    imagebutton idle "gui/tutorial4.png" action Hide('tutorial3screen')  , ShowMenu('tutorial4screen')

screen tutorial4screen:
    imagebutton idle "gui/tutorial5.png" action Hide('tutorial4screen') , ShowMenu('tutorial5screen')

screen tutorial5screen:
    imagebutton idle "gui/tutorial6.png" action Hide('tutorial5screen')  , Start('tutorial_diverge')

screen tutorialagenda:
    imagebutton idle "gui/tutorial7.png" action Hide('tutorialagenda')  , ShowMenu('tutorialagenda2')

screen tutorialagenda2:
    imagebutton idle "gui/tutorial8.png" action Hide('tutorialagenda2')  , Start('endtutorial')


screen basetutorial:
    imagebutton idle "gui/tutorial1.png" action Hide('basetutorial')  , ShowMenu('basetutorialb')
    
screen basetutorialb:
    imagebutton idle "gui/tutorial2.png" action Hide('basetutorialb')  , Start('chapterone')

screen tutorialquit:
    imagebutton idle "gui/tutorialquit.png" hover "gui/tutorialquit_hoover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_back.mp3") ] , Quit(confirm=not main_menu)
    
## CALENDAR and CHAPTER SCREENS ############################################################################################################################################################################################

screen calendar:
    if ian_active:
        imagebutton idle "gui/iancalendar.png" action Null, Return at fade_in_skill
    
        vbox:
            xcenter 0.5
            ypos 430
            text "{font=peach_pen.ttf}{size=120}[day]"
    
        vbox:
            xcenter 0.5
            ypos 735
            text "{font=peach_pen.ttf}{size=60}[month], week [week]"
    
    
    elif lena_active:
        imagebutton idle "gui/lenacalendar.png" action Null, Return at fade_in_skill
    
        vbox:
            xcenter 0.5
            ypos 430
            text "{font=peach_pen.ttf}{size=120}[day]"
    
        vbox:
            xcenter 0.5
            ypos 735
            text "{font=peach_pen.ttf}{size=60}[month], week [week]"
        
screen chapter_title:
    if chapter == 1:
        imagebutton idle "gui/chapter_1.png" action Null, Return at fade_in_skill
    elif chapter == 2:
        imagebutton idle "gui/chapter_2.png" action Null, Return at fade_in_skill
    elif chapter == 3:
        imagebutton idle "gui/chapter_3.png" action Null, Return at fade_in_skill
    elif chapter == 4:
        imagebutton idle "gui/chapter_4.png" action Null, Return at fade_in_skill
    elif chapter == 5:
        imagebutton idle "gui/chapter_5.png" action Null, Return at fade_in_skill
    elif chapter == 6:
        imagebutton idle "gui/chapter_6.png" action Null, Return at fade_in_skill
    elif chapter == 7:
        imagebutton idle "gui/chapter_7.png" action Null, Return at fade_in_skill
    elif chapter == 8:
        imagebutton idle "gui/chapter_8.png" action Null, Return at fade_in_skill
    elif chapter == 9:
        imagebutton idle "gui/chapter_9.png" action Null, Return at fade_in_skill
    elif chapter == 10:
        imagebutton idle "gui/chapter_10.png" action Null, Return at fade_in_skill
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        











