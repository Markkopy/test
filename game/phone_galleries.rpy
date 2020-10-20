####################################################################################
# Galleries ########################################################################

# Alison ###########################################################################
screen menu_gallery_alison:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            # gallery_length declares how many pictures there are in the gallery
            $ ia_gallery_length = len(ian_alison_pics)

            # image_nr is the image where the gallery starts, changes whenever you click a previous or next button.
            imagebutton idle ian_alison_pics[ia_image_nr] action Null


        # Buttons for going back and forth in the gallery
        # Looping to the front of the gallery, so the gallery backwards button doesn't make the index go out of range
        imagebutton idle "gui/gallery_base.png"
        if ia_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ia_image_nr", ia_gallery_length-1)
        # Button for looking at the previous image
        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ia_image_nr", ia_image_nr-1)
        
        # Default back button to the menu
        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_alison') , ShowMenu('menu_gallery')

        # Looping back to 0, so the forward button doesn't make the index go out of range
        if ia_image_nr == ia_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ia_image_nr", 0)
        # Button for looking at the next image
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ia_image_nr", ia_image_nr+1)

    # Same as for Ian, except for slightly different variable names. "i" is "l" and "ian" is "lena".
    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            

            $ ia_gallery_length = len(lena_alison_pics)

            imagebutton idle lena_alison_pics[ia_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if la_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("la_image_nr", la_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("la_image_nr", la_image_nr-1)
        
        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_alison') , ShowMenu('menu_gallery')

        if la_image_nr == la_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("la_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("la_image_nr", la_image_nr+1)
            
            

# Axel ##############################################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_axel:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ix_gallery_length = len(ian_axel_pics)
            
            imagebutton idle ian_axel_pics[ix_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ix_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ix_image_nr", ix_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ix_image_nr", ix_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_axel') , ShowMenu('menu_gallery')

        if ix_image_nr == ix_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ix_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ix_image_nr", ix_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lx_gallery_length = len(lena_axel_pics)
            
            imagebutton idle lena_axel_pics[lx_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lx_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lx_image_nr", lx_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lx_image_nr", lx_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_axel') , ShowMenu('menu_gallery')

        if lx_image_nr == lx_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lx_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lx_image_nr", lx_image_nr+1) 


# Cherry ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_cherry:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ic_gallery_length = len(ian_cherry_pics)
            
            imagebutton idle ian_cherry_pics[ic_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ic_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_cherry') , ShowMenu('menu_gallery')

        if ic_image_nr == ic_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lc_gallery_length = len(lena_cherry_pics)
            
            imagebutton idle lena_cherry_pics[lc_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lc_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_cherry') , ShowMenu('menu_gallery')

        if lc_image_nr == lc_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_image_nr+1)   


# Cindy ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_cindy:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ic_gallery_length = len(ian_cindy_pics)
            
            imagebutton idle ian_cindy_pics[ic_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ic_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_cindy') , ShowMenu('menu_gallery')

        if ic_image_nr == ic_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lc_gallery_length = len(lena_cindy_pics)
            
            imagebutton idle lena_cindy_pics[lc_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lc_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_cindy') , ShowMenu('menu_gallery')

        if lc_image_nr == lc_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_image_nr+1)   


# Emma ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_emma:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ie_gallery_length = len(ian_emma_pics)
            
            imagebutton idle ian_emma_pics[ie_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ie_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ie_image_nr", ie_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ie_image_nr", ie_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_emma') , ShowMenu('menu_gallery')

        if ie_image_nr == ie_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ie_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ie_image_nr", ie_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ le_gallery_length = len(lena_emma_pics)
            
            imagebutton idle lena_emma_pics[le_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if le_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("le_image_nr", le_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("le_image_nr", le_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_emma') , ShowMenu('menu_gallery')

        if le_image_nr == le_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("le_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("le_image_nr", le_image_nr+1)
            
            

# Gillian ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_gillian:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ic_gallery_length = len(ian_gillian_pics)
            
            imagebutton idle ian_gillian_pics[ic_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ic_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_gillian') , ShowMenu('menu_gallery')

        if ic_image_nr == ic_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lc_gallery_length = len(lena_gillian_pics)
            
            imagebutton idle lena_gillian_pics[lc_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lc_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_gollian') , ShowMenu('menu_gallery')

        if lc_image_nr == lc_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_image_nr+1)   


# Holly ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_holly:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ih_gallery_length = len(ian_holly_pics)
            
            imagebutton idle ian_holly_pics[ih_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ih_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ih_image_nr", ih_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ih_image_nr", ih_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_holly') , ShowMenu('menu_gallery')

        if ih_image_nr == ih_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ih_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ih_image_nr", ih_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lh_gallery_length = len(lena_holly_pics)
            
            imagebutton idle lena_holly_pics[lh_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lh_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lh_image_nr", lh_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lh_image_nr", lh_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_holly') , ShowMenu('menu_gallery')

        if lh_image_nr == lh_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lh_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lh_image_nr", lh_image_nr+1)  


# Ian ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_ian:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ii_gallery_length = len(ian_ian_pics)
            
            imagebutton idle ian_ian_pics[ii_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ii_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ii_image_nr", ii_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ii_image_nr", ii_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_ian') , ShowMenu('menu_gallery')

        if ii_image_nr == ii_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ii_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ii_image_nr", ii_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ li_gallery_length = len(lena_ian_pics)
            
            imagebutton idle lena_ian_pics[li_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if li_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("li_image_nr", li_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("li_image_nr", li_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_ian') , ShowMenu('menu_gallery')

        if li_image_nr == li_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("li_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("li_image_nr", li_image_nr+1)


# Ivy ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_ivy:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ iv_gallery_length = len(ian_ivy_pics)
            
            imagebutton idle ian_ivy_pics[iv_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if iv_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("iv_image_nr", iv_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("iv_image_nr", iv_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_ivy') , ShowMenu('menu_gallery')

        if iv_image_nr == iv_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("iv_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("iv_image_nr", iv_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lv_gallery_length = len(lena_ivy_pics)
            
            imagebutton idle lena_ivy_pics[lv_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lv_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lv_image_nr", lv_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lv_image_nr", lv_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_ivy') , ShowMenu('menu_gallery')

        if lv_image_nr == lv_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lv_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lv_image_nr", lv_image_nr+1)



# Jeremy ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_jeremy:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ij_gallery_length = len(ian_jeremy_pics)
            
            imagebutton idle ian_jeremy_pics[ij_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ij_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ij_image_nr", ij_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ij_image_nr", ij_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_jeremy') , ShowMenu('menu_gallery')

        if ij_image_nr == ij_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ij_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ij_image_nr", ij_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lj_gallery_length = len(lena_jeremy_pics)
            
            imagebutton idle lena_jeremy_pics[lj_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lj_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lj_image_nr", lj_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lj_image_nr", lj_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_jeremy') , ShowMenu('menu_gallery')

        if lj_image_nr == lj_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lj_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lj_image_nr", lj_image_nr+1)   


# Lena ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_lena:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ il_gallery_length = len(ian_lena_pics)
            
            imagebutton idle ian_lena_pics[il_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if il_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("il_image_nr", il_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("il_image_nr", il_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_lena') , ShowMenu('menu_gallery')

        if il_image_nr == il_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("il_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("il_image_nr", il_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ll_gallery_length = len(lena_lena_pics)
            
            imagebutton idle lena_lena_pics[ll_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if ll_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ll_image_nr", ll_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ll_image_nr", ll_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_lena') , ShowMenu('menu_gallery')

        if ll_image_nr == ll_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ll_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ll_image_nr", ll_image_nr+1)


# Louise ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_louise:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ilo_gallery_length = len(ian_louise_pics)
            
            imagebutton idle ian_louise_pics[ilo_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ilo_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ilo_image_nr", ilo_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ilo_image_nr", ilo_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_louise') , ShowMenu('menu_gallery')

        if ilo_image_nr == ilo_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ilo_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ilo_image_nr", ilo_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ llo_gallery_length = len(lena_louise_pics)
            
            imagebutton idle lena_louise_pics[llo_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if llo_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("llo_image_nr", llo_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("llo_image_nr", llo_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_louise') , ShowMenu('menu_gallery')

        if llo_image_nr == llo_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("llo_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("llo_image_nr", llo_image_nr+1)


# MIKE ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_mike:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ic_gallery_length = len(ian_mike_pics)
            
            imagebutton idle ian_mike_pics[ic_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ic_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_mike') , ShowMenu('menu_gallery')

        if ic_image_nr == ic_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ic_image_nr", ic_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lc_gallery_length = len(lena_mike_pics)
            
            imagebutton idle lena_mike_pics[lc_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lc_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_mike') , ShowMenu('menu_gallery')

        if lc_image_nr == lc_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lc_image_nr", lc_image_nr+1)   
            
            
# Miscellaneous ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_misc:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ imsc_gallery_length = len(ian_misc_pics)
            
            imagebutton idle ian_misc_pics[imsc_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if imsc_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("imsc_image_nr", imsc_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("imsc_image_nr", imsc_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_misc') , ShowMenu('menu_gallery')

        if imsc_image_nr == imsc_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("imsc_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("imsc_image_nr", imsc_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lmsc_gallery_length = len(lena_misc_pics)
            
            imagebutton idle lena_misc_pics[lmsc_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lmsc_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lmsc_image_nr", lmsc_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lmsc_image_nr", lmsc_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_misc') , ShowMenu('menu_gallery')

        if lmsc_image_nr == lmsc_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lmsc_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lmsc_image_nr", lmsc_image_nr+1)    

# Minerva ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_minerva:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ imi_gallery_length = len(ian_minerva_pics)
            
            imagebutton idle ian_minerva_pics[imi_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if imi_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("imi_image_nr", imi_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("imi_image_nr", imi_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_minerva') , ShowMenu('menu_gallery')

        if imi_image_nr == imi_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("imi_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("imi_image_nr", imi_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lmi_gallery_length = len(lena_minerva_pics)
            
            imagebutton idle lena_minerva_pics[lmi_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lmi_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lmi_image_nr", lmi_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lmi_image_nr", lmi_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_minerva') , ShowMenu('menu_gallery')

        if lmi_image_nr == lmi_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lmi_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lmi_image_nr", lmi_image_nr+1)    


# Perry ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_perry:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ip_gallery_length = len(ian_perry_pics)
            
            imagebutton idle ian_perry_pics[ip_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ip_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ip_image_nr", ip_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ip_image_nr", ip_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_perry') , ShowMenu('menu_gallery')

        if ip_image_nr == ip_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ip_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ip_image_nr", ip_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lp_gallery_length = len(lena_perry_pics)
            
            imagebutton idle lena_perry_pics[lp_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lp_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lp_image_nr", lp_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lp_image_nr", lp_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_perry') , ShowMenu('menu_gallery')

        if lp_image_nr == lp_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lp_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lp_image_nr", lp_image_nr+1)  

# Robert ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_robert:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ir_gallery_length = len(ian_robert_pics)
            
            imagebutton idle ian_robert_pics[ir_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ir_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ir_image_nr", ir_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ir_image_nr", ir_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_robert') , ShowMenu('menu_gallery')

        if ir_image_nr == ir_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ir_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ir_image_nr", ir_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lr_gallery_length = len(lena_robert_pics)
            
            imagebutton idle lena_robert_pics[lr_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lr_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lr_image_nr", lr_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lr_image_nr", lr_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_robert') , ShowMenu('menu_gallery')

        if lr_image_nr == lr_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lr_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lr_image_nr", lr_image_nr+1) 

# Seymour ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_seymour:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ is_gallery_length = len(ian_seymour_pics)
            
            imagebutton idle ian_seymour_pics[is_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if is_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("is_image_nr", is_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("is_image_nr", is_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_seymour') , ShowMenu('menu_gallery')

        if is_image_nr == is_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("is_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("is_image_nr", is_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ls_gallery_length = len(lena_seymour_pics)
            
            imagebutton idle lena_seymour_pics[ls_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if ls_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ls_image_nr", ls_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ls_image_nr", ls_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_seymour') , ShowMenu('menu_gallery')

        if ls_image_nr == ls_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ls_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ls_image_nr", ls_image_nr+1) 

# Stan ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_stan:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ ist_gallery_length = len(ian_stan_pics)
            
            imagebutton idle ian_stan_pics[ist_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if ist_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ist_image_nr", ist_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ist_image_nr", ist_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_stan') , ShowMenu('menu_gallery')

        if ist_image_nr == ist_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ist_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("ist_image_nr", ist_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lst_gallery_length = len(lena_stan_pics)
            
            imagebutton idle lena_stan_pics[lst_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lst_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lst_image_nr", lst_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lst_image_nr", lst_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_stan') , ShowMenu('menu_gallery')

        if lst_image_nr == lst_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lst_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lst_image_nr", lst_image_nr+1) 

# Wade ###########################################################################
# See comments for Alison. Same, except for some changed variable names.
screen menu_gallery_wade:            
    
    if ian_active:
        imagebutton idle "gui/phone_ian.png"
        vbox:
            xpos -629
            ypos 5
            
            $ iw_gallery_length = len(ian_wade_pics)
            
            imagebutton idle ian_wade_pics[iw_image_nr] action Null


        imagebutton idle "gui/gallery_base.png"
        if iw_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("iw_image_nr", iw_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("iw_image_nr", iw_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_wade') , ShowMenu('menu_gallery')

        if iw_image_nr == iw_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("iw_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("iw_image_nr", iw_image_nr+1)

    elif lena_active:
        imagebutton idle "gui/phone_lena.png"
        vbox:
            xpos -629
            ypos 5
            
            $ lw_gallery_length = len(lena_wade_pics)
            
            imagebutton idle lena_wade_pics[lw_image_nr] action Null

        imagebutton idle "gui/gallery_base.png"
        if lw_image_nr == 0:
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lw_image_nr", lw_gallery_length-1)

        else: 
            imagebutton idle "gui/gallery_prev.png" hover "gui/gallery_prev_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lw_image_nr", lw_image_nr-1)

        imagebutton idle "gui/gallery_back.png" hover "gui/gallery_back_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , Hide('menu_gallery_wade') , ShowMenu('menu_gallery')

        if lw_image_nr == lw_gallery_length-1:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lw_image_nr", 0)
        else:
            imagebutton idle "gui/gallery_next.png"  hover "gui/gallery_next_hover.png" focus_mask True action [ Play ("ch_one", "sfx/phone_click.mp3") ] , SetVariable("lw_image_nr", lw_image_nr+1)             