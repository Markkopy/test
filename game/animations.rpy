## ANIMATIONS

transform bing:
    xalign 0.5 yalign 0.5
    linear 0.5 yalign 0.0
    
transform slide:
   xalign 0.5 yalign 0.5
   linear 0.5 yalign 0.0
   linear 1.0 yalign 0.5
    

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define long = Dissolve (0.6) 
define short = Dissolve (0.3)
define fps = Dissolve (0.25)
define fps2 = Dissolve (0.2)

define fade = Fade (1.0)

## 2 CHARACTERS on screen##
transform rig:
    xalign 0.70
transform lef:
    xalign 0.30

## 3 CHARACTERS on screen##
transform rig3:
    xalign 0.85
transform lef3:
    xalign 0.15

## 4 CHARACTERS on screen##

transform centerlef:
    xalign 0.35

## 5 CHARACTERS on screen##
transform left5:
    xpos -80
transform right5:
    xalign 1.09

transform lef5:
    xalign 0.20
transform rig5:
    xalign 0.75
transform rig5b:
    xalign 0.80


transform fade_in_skill:
    alpha 0.0
    easein 1.0 alpha 1.0  
    
    
image friend_up:
    "displays/xp_friend0.png"
    pause 0.03
    "displays/xp_friend1.png"
    pause 0.03
    "displays/xp_friend2.png"
    pause 0.03
    "displays/xp_friend3.png"
    pause 0.03
    "displays/xp_friend4.png"
    pause 0.03
    "displays/xp_friend5.png"
    pause 0.03
    "displays/xp_friend6.png"
    pause 0.03
    "displays/xp_friend7.png"
    pause 0.03
    "displays/xp_friend8.png"
    pause 0.03
    "displays/xp_friend9.png"
    pause 0.03
    "displays/xp_friend10.png"
    pause 0.03
    "displays/xp_friend11.png"
    pause 0.03
    "displays/xp_friend12.png"
    pause 0.03
    "displays/xp_friend13.png"
    pause 0.03
    "displays/xp_friend14.png"
    pause 0.03
    "displays/xp_friend15.png"
    pause 0.03
    "displays/xp_friend16.png"
    pause 0.03
    "displays/xp_friend17.png"
    pause 0.03
    "displays/xp_friend18.png"
    pause 0.03
    "displays/xp_friend19.png"
    pause 0.03
    "displays/xp_friend20.png"
    pause 0.03
    "displays/xp_friend21.png"
    pause 0.03
    "displays/xp_friend22.png"
    pause 0.03
    "displays/xp_friend23.png"
    pause 0.03
    "displays/xp_friend24.png"
    pause 0.03
    "displays/xp_friend25.png"
    pause 0.03
    "displays/xp_friend26.png"
    pause 0.03
    "displays/xp_friend27.png"
    pause 0.03
    "displays/xp_friend28.png"
    pause 0.03
    "displays/xp_friend29.png"
    pause 0.03
    "displays/xp_friend30.png"
    pause 0.03
   
image wits_up:
    "displays/xp_wits0.png"
    pause 0.03
    "displays/xp_wits1.png"
    pause 0.03
    "displays/xp_wits2.png"
    pause 0.03
    "displays/xp_wits3.png"
    pause 0.03
    "displays/xp_wits4.png"
    pause 0.03
    "displays/xp_wits5.png"
    pause 0.03
    "displays/xp_wits6.png"
    pause 0.03
    "displays/xp_wits7.png"
    pause 0.03
    "displays/xp_wits8.png"
    pause 0.03
    "displays/xp_wits9.png"
    pause 0.03
    "displays/xp_wits10.png"
    pause 0.03
    "displays/xp_wits11.png"
    pause 0.03
    "displays/xp_wits12.png"
    pause 0.03
    "displays/xp_wits13.png"
    pause 0.03
    "displays/xp_wits14.png"
    pause 0.03
    "displays/xp_wits15.png"
    pause 0.03
    "displays/xp_wits16.png"
    pause 0.03
    "displays/xp_wits17.png"
    pause 0.03
    "displays/xp_wits18.png"
    pause 0.03
    "displays/xp_wits19.png"
    pause 0.03
    "displays/xp_wits20.png"
    pause 0.03
    "displays/xp_wits21.png"
    pause 0.03
    "displays/xp_wits22.png"
    pause 0.03
    "displays/xp_wits23.png"
    pause 0.03
    "displays/xp_wits24.png"
    pause 0.03
    "displays/xp_wits25.png"
    pause 0.03
    "displays/xp_wits26.png"
    pause 0.03
    "displays/xp_wits27.png"
    pause 0.03
    "displays/xp_wits28.png"
    pause 0.03
    "displays/xp_wits29.png"
    pause 0.03
    "displays/xp_wits30.png"
    pause 0.03

image charisma_up:
    "displays/xp_charisma0.png"
    pause 0.03
    "displays/xp_charisma1.png"
    pause 0.03
    "displays/xp_charisma2.png"
    pause 0.03
    "displays/xp_charisma3.png"
    pause 0.03
    "displays/xp_charisma4.png"
    pause 0.03
    "displays/xp_charisma5.png"
    pause 0.03
    "displays/xp_charisma6.png"
    pause 0.03
    "displays/xp_charisma7.png"
    pause 0.03
    "displays/xp_charisma8.png"
    pause 0.03
    "displays/xp_charisma9.png"
    pause 0.03
    "displays/xp_charisma10.png"
    pause 0.03
    "displays/xp_charisma11.png"
    pause 0.03
    "displays/xp_charisma12.png"
    pause 0.03
    "displays/xp_charisma13.png"
    pause 0.03
    "displays/xp_charisma14.png"
    pause 0.03
    "displays/xp_charisma15.png"
    pause 0.03
    "displays/xp_charisma16.png"
    pause 0.03
    "displays/xp_charisma17.png"
    pause 0.03
    "displays/xp_charisma18.png"
    pause 0.03
    "displays/xp_charisma19.png"
    pause 0.03
    "displays/xp_charisma20.png"
    pause 0.03
    "displays/xp_charisma21.png"
    pause 0.03
    "displays/xp_charisma22.png"
    pause 0.03
    "displays/xp_charisma23.png"
    pause 0.03
    "displays/xp_charisma24.png"
    pause 0.03
    "displays/xp_charisma25.png"
    pause 0.03
    "displays/xp_charisma26.png"
    pause 0.03
    "displays/xp_charisma27.png"
    pause 0.03
    "displays/xp_charisma28.png"
    pause 0.03
    "displays/xp_charisma29.png"
    pause 0.03
    "displays/xp_charisma30.png"
    pause 0.03
   
image athletics_up:
    "displays/xp_athletics0.png"
    pause 0.03
    "displays/xp_athletics1.png"
    pause 0.03
    "displays/xp_athletics2.png"
    pause 0.03
    "displays/xp_athletics3.png"
    pause 0.03
    "displays/xp_athletics4.png"
    pause 0.03
    "displays/xp_athletics5.png"
    pause 0.03
    "displays/xp_athletics6.png"
    pause 0.03
    "displays/xp_athletics7.png"
    pause 0.03
    "displays/xp_athletics8.png"
    pause 0.03
    "displays/xp_athletics9.png"
    pause 0.03
    "displays/xp_athletics10.png"
    pause 0.03
    "displays/xp_athletics11.png"
    pause 0.03
    "displays/xp_athletics12.png"
    pause 0.03
    "displays/xp_athletics13.png"
    pause 0.03
    "displays/xp_athletics14.png"
    pause 0.03
    "displays/xp_athletics15.png"
    pause 0.03
    "displays/xp_athletics16.png"
    pause 0.03
    "displays/xp_athletics17.png"
    pause 0.03
    "displays/xp_athletics18.png"
    pause 0.03
    "displays/xp_athletics19.png"
    pause 0.03
    "displays/xp_athletics20.png"
    pause 0.03
    "displays/xp_athletics21.png"
    pause 0.03
    "displays/xp_athletics22.png"
    pause 0.03
    "displays/xp_athletics23.png"
    pause 0.03
    "displays/xp_athletics24.png"
    pause 0.03
    "displays/xp_athletics25.png"
    pause 0.03
    "displays/xp_athletics26.png"
    pause 0.03
    "displays/xp_athletics27.png"
    pause 0.03
    "displays/xp_athletics28.png"
    pause 0.03
    "displays/xp_athletics29.png"
    pause 0.03
    "displays/xp_athletics30.png"
    pause 0.03
   
image lust_up:
    "displays/xp_lust0.png"
    pause 0.03
    "displays/xp_lust1.png"
    pause 0.03
    "displays/xp_lust2.png"
    pause 0.03
    "displays/xp_lust3.png"
    pause 0.03
    "displays/xp_lust4.png"
    pause 0.03
    "displays/xp_lust5.png"
    pause 0.03
    "displays/xp_lust6.png"
    pause 0.03
    "displays/xp_lust7.png"
    pause 0.03
    "displays/xp_lust8.png"
    pause 0.03
    "displays/xp_lust9.png"
    pause 0.03
    "displays/xp_lust10.png"
    pause 0.03
    "displays/xp_lust11.png"
    pause 0.03
    "displays/xp_lust12.png"
    pause 0.03
    "displays/xp_lust13.png"
    pause 0.03
    "displays/xp_lust14.png"
    pause 0.03
    "displays/xp_lust15.png"
    pause 0.03
    "displays/xp_lust16.png"
    pause 0.03
    "displays/xp_lust17.png"
    pause 0.03
    "displays/xp_lust18.png"
    pause 0.03
    "displays/xp_lust19.png"
    pause 0.03
    "displays/xp_lust20.png"
    pause 0.03
    "displays/xp_lust21.png"
    pause 0.03
    "displays/xp_lust22.png"
    pause 0.03
    "displays/xp_lust23.png"
    pause 0.03
    "displays/xp_lust24.png"
    pause 0.03
    "displays/xp_lust25.png"
    pause 0.03
    "displays/xp_lust26.png"
    pause 0.03
    "displays/xp_lust27.png"
    pause 0.03
    "displays/xp_lust28.png"
    pause 0.03
    "displays/xp_lust29.png"
    pause 0.03
    "displays/xp_lust30.png"
    pause 0.03
   
image money_up:
    "displays/xp_money0.png"
    pause 0.03
    "displays/xp_money1.png"
    pause 0.03
    "displays/xp_money2.png"
    pause 0.03
    "displays/xp_money3.png"
    pause 0.03
    "displays/xp_money4.png"
    pause 0.03
    "displays/xp_money5.png"
    pause 0.03
    "displays/xp_money6.png"
    pause 0.03
    "displays/xp_money7.png"
    pause 0.03
    "displays/xp_money8.png"
    pause 0.03
    "displays/xp_money9.png"
    pause 0.03
    "displays/xp_money10.png"
    pause 0.03
    "displays/xp_money11.png"
    pause 0.03
    "displays/xp_money12.png"
    pause 0.03
    "displays/xp_money13.png"
    pause 0.03
    "displays/xp_money14.png"
    pause 0.03
    "displays/xp_money15.png"
    pause 0.03
    "displays/xp_money16.png"
    pause 0.03
    "displays/xp_money17.png"
    pause 0.03
    "displays/xp_money18.png"
    pause 0.03
    "displays/xp_money19.png"
    pause 0.03
    "displays/xp_money20.png"
    pause 0.03
    "displays/xp_money21.png"
    pause 0.03
    "displays/xp_money22.png"
    pause 0.03
    "displays/xp_money23.png"
    pause 0.03
    "displays/xp_money24.png"
    pause 0.03
    "displays/xp_money25.png"
    pause 0.03
    "displays/xp_money26.png"
    pause 0.03
    "displays/xp_money27.png"
    pause 0.03
    "displays/xp_money28.png"
    pause 0.03
    "displays/xp_money29.png"
    pause 0.03
    "displays/xp_money30.png"
    pause 0.03
   
image money_down:
    "displays/unxp_money0.png"
    pause 0.03
    "displays/unxp_money1.png"
    pause 0.03
    "displays/unxp_money2.png"
    pause 0.03
    "displays/unxp_money3.png"
    pause 0.03
    "displays/unxp_money4.png"
    pause 0.03
    "displays/unxp_money5.png"
    pause 0.03
    "displays/unxp_money6.png"
    pause 0.03
    "displays/unxp_money7.png"
    pause 0.03
    "displays/unxp_money8.png"
    pause 0.03
    "displays/unxp_money9.png"
    pause 0.03
    "displays/unxp_money10.png"
    pause 0.03
    "displays/unxp_money11.png"
    pause 0.03
    "displays/unxp_money12.png"
    pause 0.03
    "displays/unxp_money13.png"
    pause 0.03
    "displays/unxp_money14.png"
    pause 0.03
    "displays/unxp_money15.png"
    pause 0.03
    "displays/unxp_money16.png"
    pause 0.03
    "displays/unxp_money17.png"
    pause 0.03
    "displays/unxp_money18.png"
    pause 0.03
    "displays/unxp_money19.png"
    pause 0.03
    "displays/unxp_money20.png"
    pause 0.03
    "displays/unxp_money21.png"
    pause 0.03
    "displays/unxp_money22.png"
    pause 0.03
    "displays/unxp_money23.png"
    pause 0.03
    "displays/unxp_money24.png"
    pause 0.03
    "displays/unxp_money25.png"
    pause 0.03
    "displays/unxp_money26.png"
    pause 0.03
    "displays/unxp_money27.png"
    pause 0.03
    "displays/unxp_money28.png"
    pause 0.03
    "displays/unxp_money29.png"
    pause 0.03
    "displays/unxp_money30.png"
    pause 0.03
   
image friend_down:
    "displays/unxp_friend0.png"
    pause 0.03
    "displays/unxp_friend1.png"
    pause 0.03
    "displays/unxp_friend2.png"
    pause 0.03
    "displays/unxp_friend3.png"
    pause 0.03
    "displays/unxp_friend4.png"
    pause 0.03
    "displays/unxp_friend5.png"
    pause 0.03
    "displays/unxp_friend6.png"
    pause 0.03
    "displays/unxp_friend7.png"
    pause 0.03
    "displays/unxp_friend8.png"
    pause 0.03
    "displays/unxp_friend9.png"
    pause 0.03
    "displays/unxp_friend10.png"
    pause 0.03
    "displays/unxp_friend11.png"
    pause 0.03
    "displays/unxp_friend12.png"
    pause 0.03
    "displays/unxp_friend13.png"
    pause 0.03
    "displays/unxp_friend14.png"
    pause 0.03
    "displays/unxp_friend15.png"
    pause 0.03
    "displays/unxp_friend16.png"
    pause 0.03
    "displays/unxp_friend17.png"
    pause 0.03
    "displays/unxp_friend18.png"
    pause 0.03
    "displays/unxp_friend19.png"
    pause 0.03
    "displays/unxp_friend20.png"
    pause 0.03
    "displays/unxp_friend21.png"
    pause 0.03
    "displays/unxp_friend22.png"
    pause 0.03
    "displays/unxp_friend23.png"
    pause 0.03
    "displays/unxp_friend24.png"
    pause 0.03
    "displays/unxp_friend25.png"
    pause 0.03
    "displays/unxp_friend26.png"
    pause 0.03
    "displays/unxp_friend27.png"
    pause 0.03
    "displays/unxp_friend28.png"
    pause 0.03
    "displays/unxp_friend29.png"
    pause 0.03
    "displays/unxp_friend30.png"
    pause 0.03
   
image love_down:
    "displays/unxp_love0.png"
    pause 0.03
    "displays/unxp_love1.png"
    pause 0.03
    "displays/unxp_love2.png"
    pause 0.03
    "displays/unxp_love3.png"
    pause 0.03
    "displays/unxp_love4.png"
    pause 0.03
    "displays/unxp_love5.png"
    pause 0.03
    "displays/unxp_love6.png"
    pause 0.03
    "displays/unxp_love7.png"
    pause 0.03
    "displays/unxp_love8.png"
    pause 0.03
    "displays/unxp_love9.png"
    pause 0.03
    "displays/unxp_love10.png"
    pause 0.03
    "displays/unxp_love11.png"
    pause 0.03
    "displays/unxp_love12.png"
    pause 0.03
    "displays/unxp_love13.png"
    pause 0.03
    "displays/unxp_love14.png"
    pause 0.03
    "displays/unxp_love15.png"
    pause 0.03
    "displays/unxp_love16.png"
    pause 0.03
    "displays/unxp_love17.png"
    pause 0.03
    "displays/unxp_love18.png"
    pause 0.03
    "displays/unxp_love19.png"
    pause 0.03
    "displays/unxp_love20.png"
    pause 0.03
    "displays/unxp_love21.png"
    pause 0.03
    "displays/unxp_love22.png"
    pause 0.03
    "displays/unxp_love23.png"
    pause 0.03
    "displays/unxp_love24.png"
    pause 0.03
    "displays/unxp_love25.png"
    pause 0.03
    "displays/unxp_love26.png"
    pause 0.03
    "displays/unxp_love27.png"
    pause 0.03
    "displays/unxp_love28.png"
    pause 0.03
    "displays/unxp_love29.png"
    pause 0.03
    "displays/unxp_love30.png"
    pause 0.03
   
image will_down:
    "displays/unxp_will0.png"
    pause 0.03
    "displays/unxp_will1.png"
    pause 0.03
    "displays/unxp_will2.png"
    pause 0.03
    "displays/unxp_will3.png"
    pause 0.03
    "displays/unxp_will4.png"
    pause 0.03
    "displays/unxp_will5.png"
    pause 0.03
    "displays/unxp_will6.png"
    pause 0.03
    "displays/unxp_will7.png"
    pause 0.03
    "displays/unxp_will8.png"
    pause 0.03
    "displays/unxp_will9.png"
    pause 0.03
    "displays/unxp_will10.png"
    pause 0.03
    "displays/unxp_will11.png"
    pause 0.03
    "displays/unxp_will12.png"
    pause 0.03
    "displays/unxp_will13.png"
    pause 0.03
    "displays/unxp_will14.png"
    pause 0.03
    "displays/unxp_will15.png"
    pause 0.03
    "displays/unxp_will16.png"
    pause 0.03
    "displays/unxp_will17.png"
    pause 0.03
    "displays/unxp_will18.png"
    pause 0.03
    "displays/unxp_will19.png"
    pause 0.03
    "displays/unxp_will20.png"
    pause 0.03
    "displays/unxp_will21.png"
    pause 0.03
    "displays/unxp_will22.png"
    pause 0.03
    "displays/unxp_will23.png"
    pause 0.03
    "displays/unxp_will24.png"
    pause 0.03
    "displays/unxp_will25.png"
    pause 0.03
    "displays/unxp_will26.png"
    pause 0.03
    "displays/unxp_will27.png"
    pause 0.03
    "displays/unxp_will28.png"
    pause 0.03
    "displays/unxp_will29.png"
    pause 0.03
    "displays/unxp_will30.png"
    pause 0.03
##ANIMATIONS #########################################################################################################################################################
# CHAPTER 1
image v1_ianfap_animation:
    "images/v1_ianfap.png" with fps
    pause 0.6
    "images/v1_ianfapb.png" with fps
    pause 0.6
    repeat
    
# CHAPTER 2
image v2_robert5_animation:
    "images/v2_robert5.png" with fps
    pause 0.7
    "images/v2_robert5b.png" with fps
    pause 0.7
    repeat
image v2_robert6_animation:
    "images/v2_robert6.png" with fps
    pause 0.7
    "images/v2_robert6b.png" with fps
    pause 0.7
    repeat
image v2_robert6_animation2:
    "images/v2_robert6.png" with fps
    pause 0.3
    "images/v2_robert6b.png" with fps
    pause 0.3
    repeat
image v2_robert7_animation1:
    "images/v2_robert7b.png" with fps
    pause 0.7
    "images/v2_robert7bb.png" with fps
    pause 0.7
    repeat
image v2_robert7_animation2:
    "images/v2_robert7.png" with fps
    pause 0.7
    "images/v2_robert7a.png" with fps
    pause 0.7
    repeat
image v2_alison5_animation:
    "images/v2_alison5.png" with fps
    pause 0.7
    "images/v2_alison5b.png" with fps
    pause 0.7
    repeat
image v2_alison6_animation:
    "images/v2_alison6.png" with fps
    pause 0.7
    "images/v2_alison6a.png" with fps
    pause 0.7
    repeat
image v2_alison6_animation2:
    "images/v2_alison6.png" with fps
    pause 0.4
    "images/v2_alison6a.png" with fps
    pause 0.4
    repeat
image v2_alison6b_animation:
    "images/v2_alison6b.png" with fps
    pause 0.7
    "images/v2_alison6ba.png" with fps
    pause 0.7
    repeat
image v2_alison6b_animation2:
    "images/v2_alison6b.png" with fps
    pause 0.4
    "images/v2_alison6ba.png" with fps
    pause 0.4
    repeat
image v2_cherry4_animation:
    "images/v2_cherry4.png" with fps
    pause 0.7
    "images/v2_cherry4a.png" with fps
    pause 0.7
    repeat
image v2_cherry4b_animation:
    "images/v2_cherry4b.png" with fps
    pause 0.7
    "images/v2_cherry4ba.png" with fps
    pause 0.7
    repeat
image v2_cherry5_animation:
    "images/v2_cherry5.png" with fps
    pause 0.7
    "images/v2_cherry5b.png" with fps
    pause 0.7
    repeat
image v2_cherry5_animation2:
    "images/v2_cherry5.png" with fps
    pause 0.4
    "images/v2_cherry5b.png" with fps
    pause 0.4
    repeat
    
# CHAPTER 3
image v3_cherry2_animation:
    "images/v3_cherry2.png" with fps
    pause 0.7
    "images/v3_cherry2b.png" with fps
    pause 0.7
    repeat
image v3_cherry2_animation2:
    "images/v3_cherry2.png" with fps
    pause 0.4
    "images/v3_cherry2b.png" with fps
    pause 0.4
    repeat
image v3_alison5_animation:
    "images/v3_alison5.png" with fps
    pause 0.7
    "images/v3_alison5b.png" with fps
    pause 0.7
    repeat

image v3_alison6_animation:
    "images/v3_alison6.png" with fps
    pause 0.4
    "images/v3_alison6b.png" with fps
    pause 0.4
    repeat
    
image v3_alison7_animation:
    "images/v3_alison7.png" with fps
    pause 0.7
    "images/v3_alison7b.png" with fps
    pause 0.7
    repeat
image v3_alison7cum_animation:
    "images/v3_alison7cum.png" with fps
    pause 0.7
    "images/v3_alison7cumb.png" with fps
    pause 0.7
    repeat
image v3_alison8_animation:
    "images/v3_alison8.png" with fps
    pause 0.7
    "images/v3_alison8b.png" with fps
    pause 0.7
    repeat
image v3_solo1_animation:
    "images/v3_solo1.png" with fps
    pause 0.7
    "images/v3_solo1b.png" with fps
    pause 0.7
    repeat
image v3_solo2_animation:
    "images/v3_solo2.png" with fps
    pause 0.7
    "images/v3_solo2b.png" with fps
    pause 0.7
    repeat
image v3_solo4_animation:
    "images/v3_solo4.png" with fps
    pause 0.7
    "images/v3_solo4b.png" with fps
    pause 0.7
    repeat
image v3_louise2_animation:
    "images/v3_louise2.png" with vpunch
    pause 0.7
    "images/v3_louise2b.png" with fps
    pause 0.7
    repeat
image v3_louise3_animation:
    "images/v3_louise3.png" with fps
    pause 0.5
    "images/v3_louise3b.png" with fps
    pause 0.5
    repeat

# CHAPTER 4
image v4_solo2_animation:
    "images/v4_solo2.png" with short
    pause 1
    "images/v4_solo2b.png" with short
    pause 1
    repeat
image v4_solo3_animation:
    "images/v4_solo3.png" with short
    pause 0.7
    "images/v4_solo3b.png" with short
    pause 0.7
    repeat
image v4_robert_animation:
    "images/v4_restaurant3.png" with fps
    pause 0.5
    "images/v4_restaurant3b.png" with fps
    pause 0.5
    repeat
image v4_robert_animation2:
    "images/v4_restaurant4.png" with fps
    pause 0.4
    "images/v4_restaurant4b.png" with fps
    pause 0.4
    repeat

# CHAPTER 5   
image v5_emma7_animation:
    "images/v5_emma7.png" with fps
    pause 0.7
    "images/v5_emma7b.png" with fps
    pause 0.7
    repeat
image v5_emma7_animation_slow:
    "images/v5_emma7.png" with fps
    pause 1
    "images/v5_emma7b.png" with fps
    pause 1
    repeat
image v5_emma7_animation_fast:
    "images/v5_emma7.png" with fps
    pause 0.4
    "images/v5_emma7b.png" with fps
    pause 0.4
    repeat
image v5_emma8_animation:
    "images/v5_emma8.png" with fps2
    pause 0.5
    "images/v5_emma8b.png" with fps2
    pause 0.5
    repeat
image v5_alison4_animation:
    "images/v5_alison4.png" with fps
    pause 0.7
    "images/v5_alison4b.png" with fps
    pause 0.7
    repeat
image v5_louise6_animation:
    "images/v5_louise6.png" with fps
    pause 0.7
    "images/v5_louise6b.png" with fps
    pause 0.7
    repeat