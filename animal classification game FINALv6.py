import PIL.Image
from PIL import ImageTk, Image
from tkinter import *
from tkinter import Tk
import customtkinter
import googletrans
from googletrans import Translator
import textblob
from tkinter import ttk, messagebox
import threading
from langdetect import *
import tkinter.font as tkfont
import sys


root = Tk()
root.title('Animal Classification Game')
root.geometry("800x400")


########################################################################################################################################################################

#used to translate new frames as they're displayed
global to_language_key
to_language_key="en" #starts off with english

#language list from google translate
languages=googletrans.LANGUAGES
#convert to list
language_list=list(languages.values())


def translate_widgets():
    translator = Translator()

    if to_language_key!="en": #frame automatically disaplyed in english, if previous frame was in english no need to change
        
        #display loading which process occurs
        loading=Label(root, text="translating...", font=(("Arial"), 25), bg='#ffff54', height=3)
        loading.place(x=300, y=150)
        progress = ttk.Progressbar(root, orient = HORIZONTAL, length = 180, mode = 'indeterminate')
        progress.start()
        progress.place(x=300, y=150)

        for widget in root.winfo_children(): #every frame in root
            for widget in widget.winfo_children(): #every widget in that frame

                if isinstance(widget, Label):
                    if len(widget.cget("text"))>0: #if its label with text
                        
                        #get text, translate it, and replace with new text
                        words=str(widget.cget("text"))
                        words=translator.translate(words, dest=to_language_key)
                        widget.configure(text=(words.text))

                if isinstance(widget, Button):
                    if len(widget.cget("text"))>0: #if button with text

                        #get text, translate it, and replace with new text
                        words=str(widget.cget("text"))
                        words=translator.translate(words, dest=to_language_key)
                        widget.configure(text=(words.text))

                if isinstance(widget, customtkinter.CTkButton):
                    if len(widget.cget("text"))>0: #if custom tkinter button with text

                        #get text, translate it, and replace with new text
                        words=str(widget.cget("text"))
                        words=translator.translate(words, dest=to_language_key)
                        widget.configure(text=(words.text))

            widget.update() #update the frame

        #remove loading screen
        progress.stop
        progress.place_forget()
        loading.place_forget()

def update_widget_colour():
    global light_mode
    global dark_mode
    global contrast_mode
    global def_mode
    if contrast_mode==False and dark_mode==False and light_mode== False and def_mode==False:
        pass
    if dark_mode==True:
        colour1_change()
    if light_mode==True:
        colour2_change()
    if contrast_mode==True:
        colour3_change()
    if def_mode==True:
        colour4_change()


#############################################################################################################################################################################################

#subprogram used to determine which button was clicked, and store the animal name
def which_button(m): 
    global list_correct_animals
    #adding to list of correct animals
    list_correct_animals=list_correct_animals + "\n" + m

#disables buttons after click
def disable_button(event):
    button = event.widget
    button.configure(state=DISABLED)
    button.unbind("<Button-1>")




#all these to do with displaying results- common aspects of all levels
global m
global points
points=0
global list_correct_animals
list_correct_animals= ""


##########

def go_to_start(): #replay, sends to first frame
    for widget in congrats.winfo_children():
        widget.place_forget() 
    introduction()

def EndScreeN(): #displays congrats screen if level 6 completed
    for widget in lvl6_summary.winfo_children(): #erase all widgets from previous frame
        widget.place_forget() 


    global congrats
    congrats= Frame(root, width=800, height=400)

    #backgrouns
    congrats_bg = (PIL.Image.open("E:\\12SDD\\yr12\\congrats_bg.jpg")).resize((800, 400))
    global congrats_photo
    congrats_photo=ImageTk.PhotoImage(congrats_bg)
    congrats_label=Label(congrats, image=congrats_photo, height=400, width=800)
    congrats_label.place(x=0, y=0, relwidth=1, relheight=1)

    #congrats message
    congrats_message= Label(master=congrats, text=("Congrats, you are now an expert"+"\n"+" on the 6 categories of animals"), relief="ridge", width=30, height=4, bg="light green", fg="black", font=(("Comic Sans MS"), 13))
    congrats_message.place(x=250, y=50)

    #replay option
    ReplaY= Button(master=congrats, text=("replay"), width=10, height=5, bg="light green", command=go_to_start, relief="ridge")
    ReplaY.place(x=450, y=150)

    #quit option
    def quit_game(event):
        command=sys.exit()
        
    quit_end=Button(congrats, text="quit", width=10, height=5, bg="light green")
    quit_end.bind("<Button-1>", quit_game)
    quit_end.place(x=300, y=150)

    #place frame
    congrats.place(x=0, y=0)


    #when this frame is first disaplyed, update language and colour to match previous
    congrats.bind("<Visibility>", translate_widgets())
    for widget in congrats.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())



##########
def correct_choice6(m): #when a correct option is chosen in lvl6
    global points
    global score6
    global animals_found6
    global list_correct_animals

    #find out which button was pressed and add it to the list of animals
    which_button(m)

    #increment points and adds correct animal to list
    if points<2:
        points=points+1
        score6.config(text="SCORE: "+ str(points))
        animal_found_list6.config(text=list_correct_animals)
        translate_widgets()
    #if 3 points reached, display summary
    else:
        points=0 #reset points

        for widget in lvl6_game.winfo_children(): #clear lvl6
            widget.place_forget() 

        global lvl6_summary
        lvl6_summary= Frame(root, width=800, height=400)

        #bg
        backyard_bg = (PIL.Image.open("E:\\12SDD\\yr12\\project pics\\level 6\\backyard_bg.png")).resize((800, 400))
        global backyard_photo
        backyard_photo=ImageTk.PhotoImage(backyard_bg)
        backyard_label=Label(lvl6_summary, image=backyard_photo)
        backyard_label.place(x=0, y=0, relwidth=1, relheight=1)

        #next level button
        next_level6= Button(master=lvl6_summary, text=("finish"), relief="raised", width=10, height=5, bg="light green", font=(("Comic Sans MS"), 8), command=EndScreeN)
        #messege
        summary_screen6= Label(master=lvl6_summary, text=("You've found the following invertebrates" +"\n" + " in the backyard:" +"\n" + list_correct_animals), width=50, height=10, bg="grey", font=(("Comic Sans MS"), 12), fg="black")
        lvl6_summary.place(x=0, y=0)
        summary_screen6.place(x=150, y=75)
        next_level6.place(x=700, y=300)

        list_correct_animals="" #reset list

        #make 'go to level 6' available
        go_to_level.entryconfig("Level 6- invertebrates", state=NORMAL)

        #update lang and colours to match previous frame
        for widget in lvl6_summary.winfo_children():
            widget.bind("<Visibility>", update_widget_colour())
        lvl6_summary.bind("<Visibility>", translate_widgets())
    

def wrong_answer6(m): #wrong answer chosen in lvl6
    global oops6
    global try_again6

    def undo_wrong_answer6() :
        # when try again clicked, returns to level
        oops6.place_forget()
        try_again6.place_forget() 
        incorrect6.place_forget()

    if m=="mammal":
        justification="That is not an invertebrate, it is a mammal! \n This is because it is large, has fur, \n is warm blooded and gives birth to live \n young. It also doesn't have an \n exoskeleton and isn't tiny \n like an invertebrate would be."    
    if m=="amphibian":
        justification="That is not an invertebrate, it is an amphibian! \n This is because it has slimy \n skin and webbed feet that are good for \n leaping. It also doesn't have an \n exoskeleton and isn't tiny \n like an invertebrate would be."
    if m== "reptile":
        justification="That is not an invertebrate, it is a reptile! \n This is because it has \n scales and a long tail.\n It also doesn't have an \n exoskeleton and isn't tiny \n like an invertebrate would be."
    if m=="bird":
        justification="This is not an invertebrate, it is a bird! \n This is because it has feathers \n and a beak and is small.\n It also doesn't have an \n exoskeleton and isn't tiny \n like an invertebrate would be."

    #message for incorrect answer
    incorrect6=Frame(lvl6_game, bg="light green", height=400, width=450)
    incorrect6.place(x=0, y=0)

    oops6= Label(master=incorrect6, text="Oops! " + justification + "\n"+"\n" +"If your stuck try going back to the" +"\n" +" instructions page for a hint!",
                  font=(("Comic Sans MS"), 14), width=42, height=10, fg="black", bg="light green")
    try_again6= Button(master=incorrect6, text=("Try again"), width=15, height=3, command=undo_wrong_answer6, bg="grey", fg="black", font=(("Comic Sans MS"), 10), relief="ridge")
    translate_widgets()
    update_widget_colour()
    try_again6.place(x=170, y=270)
    oops6.place(x=0, y=0)





##########
def Level6():
    global instr_lvl6
    for widget in instr_lvl6.winfo_children(): #hide instruction page
        widget.place_forget()


    global lvl6_game
    lvl6_game= Frame(root, width=800, height=400, bg="light green")

    #displaying options
    #Eastern Cottontail
    ECottontail_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 6\\inver\\eastern-cottontail.jpg")
    ECottontail_CTK =  customtkinter.CTkImage(ECottontail_img,
                                        size=(130,110))
    ECottontail_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=ECottontail_CTK, text="Eastern Cottontail", fg_color="light green", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer6 (m)) 
    ECottontail_button.bind("<Button-1>", disable_button)
    #Field Mouse
    FMouse_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 6\\inver\\field-mouse.jpg")
    FMouse_CTK =  customtkinter.CTkImage(FMouse_img,
                                        size=(130,110))
    FMouse_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=FMouse_CTK, text="Field Mouse", fg_color="light green", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer6 (m))  
    FMouse_button.bind("<Button-1>", disable_button)
    #earthworm
    earthworm_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 6\\inver\\earthworm.jpg")
    earthworm_CTK =  customtkinter.CTkImage(earthworm_img,
                                        size=(130,110))
    earthworm_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=earthworm_CTK, text="Earthworm", fg_color="light green", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Earthworm":correct_choice6 (m))  
    earthworm_button.bind("<Button-1>", disable_button)
    #Garter Snake
    GSnake_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 6\\inver\\garter-snake.jpg")
    GSnake_CTK =  customtkinter.CTkImage(GSnake_img,
                                        size=(130,110))
    GSnake_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=GSnake_CTK, text="Garter Snake", fg_color="light green", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="reptile":wrong_answer6 (m))  
    GSnake_button.bind("<Button-1>", disable_button)
    #German Shephard
    GShephard_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 6\\inver\\german-shephard.jpg")
    GShephard_CTK =  customtkinter.CTkImage(GShephard_img,
                                        size=(130,110))
    GShephard_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=GShephard_CTK, text="German Shephard", fg_color="light green", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer6 (m)) 
    GShephard_button.bind("<Button-1>", disable_button)
    #ladybug
    ladybug_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 6\\inver\\ladybug.jpg")
    ladybug_CTK =  customtkinter.CTkImage(ladybug_img,
                                        size=(130,110))
    ladybug_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=ladybug_CTK, text="Ladybug", fg_color="light green", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Ladybug":correct_choice6 (m)) 
    ladybug_button.bind("<Button-1>", disable_button)
    #Monarch Butterfly
    MButterfly_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 6\\inver\\monarch-butterfly.jpg")
    MButterfly_CTK =  customtkinter.CTkImage(MButterfly_img,
                                        size=(130,110))
    MButterfly_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=MButterfly_CTK, text="Monarch Butterfly", fg_color="light green", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Monarch Butterfly":correct_choice6 (m))  
    MButterfly_button.bind("<Button-1>", disable_button)
    #honeyeater
    honeyeater_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 6\\inver\\honeyeater.jpg")
    honeyeater_CTK =  customtkinter.CTkImage(honeyeater_img,
                                        size=(130,110))
    honeyeater_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=honeyeater_CTK, text="Honeyeater", fg_color="light green", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="bird":wrong_answer6 (m))  
    honeyeater_button.bind("<Button-1>", disable_button)
    #Water Skink
    WSkink_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 6\\inver\\water-skink.jpg")
    WSkink_CTK =  customtkinter.CTkImage(WSkink_img,
                                        size=(130,110))
    WSkink_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=WSkink_CTK, text="Water Skink", fg_color="light green", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command= (lambda m="amphibian":wrong_answer6 (m)))
    WSkink_button.bind("<Button-1>", disable_button)


    #results
    global score6
    global animal_found_list6
    score6 = Label(lvl6_game, text="SCORE: ", font=(("Times New Roman"), 18), fg="black", bg="light green")
    animals_found_label6 = Label(lvl6_game, text="ANIMALS FOUND: ", height=3, width=20, font=(("Times New Roman"), 18), fg="black", bg="light green")
    global animal_found_list6
    animal_found_list6= Label(lvl6_game, text="", font=(("comic sans MS"), 12), bg="#c0facb", width=30, height=7)

    #display everything
    lvl6_game.place(x=0, y=0)
    animals_found_label6.place(x=490, y=40)
    animal_found_list6.place(x=470, y=120)
    WSkink_button.place(x=280, y=260)
    honeyeater_button.place(x=140, y=260)
    MButterfly_button.place(x=0, y=260)
    ladybug_button.place(x=0, y=135)
    GShephard_button.place(x=140, y=135)
    GSnake_button.place(x=280, y=135)
    earthworm_button.place(x=280, y=0)
    FMouse_button.place(x=140, y=0)
    ECottontail_button.place(x=0, y=0)
    score6.place(x=550, y=0)


    #back option
    def back6_func():
        global instr_lvl6
        global cont6
        instr_lvl6.place(x=0, y=0)
        def return_lvl6():
            instr_lvl6.place_forget()
            cont6.configure(command=Level6)
        cont6.configure(command=return_lvl6)
        instr_lvl6.lift()
    back6= Button(master=lvl6_game, text=("instructions"), width=15, height=2, relief="raised", bg="light green", font=(("Comic Sans MS"), 8), command=back6_func)
    back6.place(x=565, y=305)

    #reset level
    def reset6_func():
        global points
        global list_correct_animals
        global animal_found_list
        points=0
        list_correct_animals=""
        animal_found_list6.configure(text="")
        Level6()

    reset6= Button(master=lvl6_game, text=("reset"), width=8, height=1, command=reset6_func, bg="grey", font=(("Comic Sans MS"), 6), relief="raised")
    reset6.place(x=600, y=360)

    #update lang and colour to previous frame
    for widget in lvl6_game.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())
    lvl6_game.bind("<Visibility>", translate_widgets())


##########

def transition5(): #hide level 5 summary and show level 6 instructions

    #hide summary screen
    for widget in lvl5_summary.winfo_children():
         widget.place_forget()
    

    #frame for level 6 instructions
    global instr_lvl6
    instr_lvl6= Frame(root, width=800, height=400, bg="light green")

    #display instructions for 6th level
    backyard = Label(instr_lvl6, text="Next we are going to look for " + "\n"+ "invertebrates in my backyard" +"\n" +"\n" + "Invertebrates don't have a spine, " +"\n"+ "but have a hard exoskeleton" +"\n" +"They are also often quite small," + "\n" + " like the invertebrates shown here!" + "\n"+"\n" +"Some examples of invertebrates you may know" + "\n" + " include slugs, insects and crabs!",
                      font=(("Comic Sans MS"), 12), bg="light green", width=40)
    
    #continue button to start 6th level
    global cont6
    cont6 =  Button(instr_lvl6, text="Continue", relief="raised", bg="light green", font=(("Comic Sans MS"), 8), command=Level6)

    #collage of invertebrates
    invertebrates_collage_image = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 6\\invertebrates.jpg")
    TK_invertebrates_collage =   customtkinter.CTkImage(invertebrates_collage_image,
        size=(400,400))
    invertebrates_collage =   customtkinter.CTkLabel(master=instr_lvl6, image=TK_invertebrates_collage)

    instr_lvl6.place(x=0, y=0)
    invertebrates_collage.place(x=0, y=0)
    cont6.place(x=700, y=300)
    backyard.place(x=400, y=50)

    #update language and colour to match previous
    for widget in instr_lvl6.winfo_children():
        widget.bind("<Visibility>", translate_widgets())
    instr_lvl6.bind("<Visibility>", update_widget_colour())




#########
def correct_choice5(m): #when correct option chosen in level 5
    global points
    global score5
    global animals_found5
    global list_correct_animals

    #find out which button was chosen and add it to list
    which_button(m)

    #increments points and adds correct animal to list
    if points<2:
        points=points+1
        score5.config(text="SCORE: "+ str(points))
        animal_found_list5.config(text=list_correct_animals)
        translate_widgets()
    else:
    #if 3 points reached, display level summary

        points=0 #reset

        #hide widgets in level 5 game
        for widget in lvl5_game.winfo_children():
            widget.place_forget() 

        global lvl5_summary
        lvl5_summary= Frame(root, width=800, height=400, bg="#cca47c")

        #background
        outback_bg = (PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 5\\outback_bg.png")).resize((800, 400))
        global outback_photo
        outback_photo=ImageTk.PhotoImage(outback_bg)
        outback_label=Label(lvl5_summary, image=outback_photo)
        outback_label.place(x=0, y=0, relwidth=1, relheight=1)

        next_level5= Button(master=lvl5_summary, text=("next level"), width=10, relief="raised", height=5, bg="#cca47c", font=(("Comic Sans MS"), 8), command=transition5)
        summary_screen5= Label(master=lvl5_summary, text=("These are the reptiles you found " +"\n" + " in the Australian Outback:" +"\n" + list_correct_animals), width=50, height=10, bg="grey", font=(("Comic Sans MS"), 12))
        lvl5_summary.place(x=0, y=0)
        summary_screen5.place(x=150, y=75)
        next_level5.place(x=700, y=300)

        list_correct_animals="" #reset
    
        #make 'go to level 5' available
        go_to_level.entryconfig("Level 5- reptiles", state=NORMAL)

        #update language and colour for summary screen
        for widget in lvl5_summary.winfo_children():
            widget.bind("<Visibility>", update_widget_colour())
        lvl5_summary.bind("<Visibility>", translate_widgets())



def wrong_answer5(m): #when wrong answer chosen in level 5
    global oops5
    global try_again5

    def undo_wrong_answer5() :
        # when try again clicked, returns to level
        oops5.place_forget()
        try_again5.place_forget() 
        incorrect5.place_forget()

    if m=="mammal":
        justification="That is not a reptile, it is a mammal! \n This is because it is large, has fur, \n is warm blooded and gives birth to live \n young. It also doesn't have hard, scaly \n skin and short/no feet like a \n reptile would."    
    if m=="invertebrate":
        justification="That is not a reptile, it is an invertebrate! \n This is because it has a hard \n exoskeleton and is really tiny.\n It also doesn't \n have hard, scaly skin and short/no \n feet like a reptile would."
    if m=="amphibian":
        justification="That is not a reptile, it is an amphibian! \n This is because it has slimy \n skin and webbed feet \n that are good for leaping.\n It also doesn't \n have hard, scaly skin and short/no \n feet like a reptile would."
    if m=="bird":
        justification="This is not a reptile, it is a bird! \n This is because it has feathers \n and a beak.\n It also doesn't \n have hard, scaly skin and short/no \n feet like a reptile would."

    #message for incorrect answer
    incorrect5=Frame(lvl5_game, bg="#cca47c", height=400, width=450)
    incorrect5.place(x=0, y=0)

    oops5= Label(master=incorrect5, text="Oops! " + justification + "\n"+"\n" +"If your stuck try going back to the" +"\n" +" instructions page for a hint!",
                  font=(("Comic Sans MS"), 14), width=42, height=10, fg="black", bg="#cca47c")
    try_again5= Button(master=incorrect5, text=("Try again"), width=15, height=3, command=undo_wrong_answer5, bg="grey", fg="black", font=(("Comic Sans MS"), 10), relief="ridge")
    translate_widgets()
    update_widget_colour()
    try_again5.place(x=170, y=270)
    oops5.place(x=0, y=0)




##########
def Level5():

    global instr_lvl5 #hide widgets from instruction screen
    for widget in instr_lvl5.winfo_children():
        widget.place_forget()

    ###
    global lvl5_game
    lvl5_game= Frame(root, width=800,  height=400, bg="#cca47c")


    #displaying options
    #Sand Goanna
    SGoanna_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 5\\reptiles\\sand-goanna.jpg")
    SGoanna_CTK =  customtkinter.CTkImage(SGoanna_img,
                                        size=(130,110))
    SGoanna_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=SGoanna_CTK, text="Sand Goanna", fg_color="#cca47c", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Sand Goanna":correct_choice5 (m))   
    SGoanna_button.bind("<Button-1>", disable_button)
    #Thorny Devil
    TDevil_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 5\\reptiles\\thorny-devil.jpg")
    TDevil_CTK =  customtkinter.CTkImage(TDevil_img,
                                        size=(130,110))
    TDevil_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=TDevil_CTK, text="Thorny Devil", fg_color="#cca47c", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Thorny Devil":correct_choice5 (m))  
    TDevil_button.bind("<Button-1>", disable_button)
    #dingo
    dingo_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 5\\other\\dingo.jpg")
    dingo_CTK =  customtkinter.CTkImage(dingo_img,
                                        size=(130,110))
    dingo_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=dingo_CTK, text="Dingo", fg_color="#cca47c", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer5 (m)) 
    dingo_button.bind("<Button-1>", disable_button)
    #Australian Feral Camel
    AFCamel_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 5\\other\\australian-feral-camel.jpg")
    AFCamel_CTK =  customtkinter.CTkImage(AFCamel_img,
                                        size=(130,110))
    AFCamel_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=AFCamel_CTK, text="Australian Feral Camel", fg_color="#cca47c", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer5 (m))  
    AFCamel_button.bind("<Button-1>", disable_button)
    #Frill Neck Lizard
    FNLizard_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 5\\reptiles\\frill-neck-lizard.jpg")
    FNLizard_CTK =  customtkinter.CTkImage(FNLizard_img,
                                        size=(130,110))
    FNLizard_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=FNLizard_CTK, text="Frill Neck Lizard", fg_color="#cca47c", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Frill Neck Lizard":correct_choice5 (m)) 
    FNLizard_button.bind("<Button-1>", disable_button)
    #Bilby
    Bilby_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 5\\other\\Bilby.png")
    Bilby_CTK =  customtkinter.CTkImage(Bilby_img,
                                        size=(130,110))
    Bilby_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=Bilby_CTK, text="Bilby", fg_color="#cca47c", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer5 (m)) 
    Bilby_button.bind("<Button-1>", disable_button)
    #Quokka
    quokka_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 5\\other\\quokka.jpg")
    quokka_CTK =  customtkinter.CTkImage(quokka_img,
                                        size=(130,110))
    quokka_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=quokka_CTK, text="Quokka", fg_color="#cca47c", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer5 (m))
    quokka_button.bind("<Button-1>", disable_button)
    #kangaroo
    kangaroo_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 5\\other\\kangaroo.jpg")
    kangaroo_CTK =  customtkinter.CTkImage(kangaroo_img,
                                        size=(130,110))
    kangaroo_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=kangaroo_CTK, text="Kangaroo", fg_color="#cca47c", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer5 (m))  
    kangaroo_button.bind("<Button-1>", disable_button)

    #Kookaburra
    kookaburra_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 5\\other\\kookaburra.jpg")
    kookaburra_CTK =  customtkinter.CTkImage(kookaburra_img,
                                        size=(130,110))
    kookaburra_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=kookaburra_CTK, text="Kookaburra", fg_color="#cca47c", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command= (lambda m="bird":wrong_answer5 (m)))
    kookaburra_button.bind("<Button-1>", disable_button)

    #results
    global score5
    global animal_found_list5
    score5 = Label(lvl5_game, text="SCORE: ", font=(("Times New Roman"), 18), bg="#cca47c")
    animals_found_label5 = Label(lvl5_game, text="ANIMALS FOUND: ", height=3, width=20, font=(("Times New Roman"), 18), bg="#cca47c")
    global animal_found_list5
    animal_found_list5= Label(lvl5_game, text="", font=(("comic sans MS"), 12), bg="#ebc6a2", height=7, width=30)

    #back option
    def back5_func():
        global instr_lvl5
        global cont5
        instr_lvl5.place(x=0, y=0)
        def return_lvl5():
            instr_lvl5.place_forget()
            cont5.configure(command=Level5)
        cont5.configure(command=return_lvl5)
        instr_lvl5.lift()
    back5= Button(master=lvl5_game, text=("instructions"), width=15, height=2, bg="#cca47c", font=(("Comic Sans MS"), 6), command=back5_func, relief="raised")

    #reset level
    def reset5_func():
        global points
        global list_correct_animals
        global animal_found_list
        points=0
        list_correct_animals=""
        animal_found_list5.configure(text="")
        Level5()

    reset5= Button(master=lvl5_game, text=("reset"), width=8, height=1, command=reset5_func, bg="grey", font=(("Comic Sans MS"), 6), relief="raised")
    reset5.place(x=600, y=360)

    lvl5_game.place(x=0, y=0)
    back5.place(x=565, y=305)
    score5.place(x=550, y=0)
    animals_found_label5.place(x=490, y=40)
    animal_found_list5.place(x=470, y=120)
    kookaburra_button.place(x=280, y=260)
    kangaroo_button.place(x=140, y=260)
    quokka_button.place(x=0, y=260)
    Bilby_button.place(x=0, y=135)
    FNLizard_button.place(x=140, y=135)
    AFCamel_button.place(x=280, y=135)
    dingo_button.place(x=280, y=0)
    TDevil_button.place(x=140, y=0)
    SGoanna_button.place(x=0, y=0)



    #update colour and language to match previous screen
    for widget in lvl5_game.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())
    lvl5_game.bind("<Visibility>", translate_widgets())



##########
def transition4():
    #hide widgets from previous screen
    for widget in lvl4_summary.winfo_children():
         widget.place_forget()



    global instr_lvl5
    instr_lvl5= Frame(root, width=800, height=400, bg="#cca47c")
    
    #display instructions for 5th level
    outback = Label(instr_lvl5, text="Next we are going to look for " + "\n"+ "reptiles in the outback!" +"\n"+"\n" + "Reptiles have scaly skin, short legs" +"\n" + "(or none) and long tails," + "\n" + " like the reptiles shown here!" + "\n"+"\n" +"Some examples of reptiles you may know" + "\n" + " include lizards, snakes and crocodiles!",
                     font=(("Comic Sans MS"), 12), bg="#cca47c", width=40)
    
    #continue button to start 5th level
    global cont5
    cont5 =  Button(instr_lvl5, text="Continue", bg="#cca47c", command=Level5, font=(("Comic Sans MS"), 8), relief="raised")

    #collage of reptiles
    reptiles_collage_image = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 5\\Reptiles.jpg")
    TK_reptiles_collage =   customtkinter.CTkImage(reptiles_collage_image,
        size=(400,400))
    reptiles_collage =   customtkinter.CTkLabel(master=instr_lvl5, image=TK_reptiles_collage)

    instr_lvl5.place(x=0, y=0)
    reptiles_collage.place(x=0, y=0)
    cont5.place(x=700, y=300)
    outback.place(x=400, y=50)



    #update colour and language to match previous screen
    for widget in instr_lvl5.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())
    instr_lvl5.bind("<Visibility>", translate_widgets())





##########
def correct_choice4(m): #when correct option chosen in level 4
    global points
    global list_correct_animals

    #increments points and adds correct animal to list
    which_button(m)
    if points<2:
        points=points+1
        score4.config(text="SCORE: "+ str(points))
        animal_found_list4.config(text=list_correct_animals)
        translate_widgets()
    else:
    #when 3 points reached

        points=0 #reset

        #hide widgets from level 4 game
        for widget in lvl4_game.winfo_children():
            widget.place_forget() 



        #summary screen
        global lvl4_summary
        lvl4_summary= Frame(root, width=800, height=400, bg="#877c94")

        #background
        BRF_bg = (PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 4\\BRF_bg.png")).resize((800, 400))
        global BRF_photo
        BRF_photo=ImageTk.PhotoImage(BRF_bg)
        BRF_label=Label(lvl4_summary, image=BRF_photo)
        BRF_label.place(x=0, y=0, relwidth=1, relheight=1)

        next_level4= Button(master=lvl4_summary, text=("next level"), relief="raised", width=10, height=5, bg="#877c94", font=(("Comic Sans MS"), 8), command=transition4)
        summary_screen4= Label(master=lvl4_summary, text=("These are the amphibians you found " +"\n" + " in the Borneo Rainforest:" +"\n" + list_correct_animals), width=50, height=10, font=(("Comic Sans MS"), 12), bg="grey")
        lvl4_summary.place(x=0, y=0)
        summary_screen4.place(x=150, y=75)
        next_level4.place(x=700, y=300)

        list_correct_animals="" #reset once list displayed

        #make 'go to level 4' available
        go_to_level.entryconfig("Level 4- amphibians", state=NORMAL)

        #update colour and language to match previous screen
        for widget in lvl4_summary.winfo_children():
            widget.bind("<Visibility>", update_widget_colour())
        lvl4_summary.bind("<Visibility>", translate_widgets())



def wrong_answer4(m): #when wrong option chosen in level 4
    global oops4
    global try_again4

    def undo_wrong_answer4() :
        # when try again clicked, returns to level
        oops4.place_forget()
        try_again4.place_forget() 
        incorrect4.place_forget()

    if m=="mammal":
        justification="That is not an amphibian, it is a mammal! \n This is because it is large, has fur, \n is warm blooded and gives birth to \n live young. It also doesn't have slimy \n skin or webbed feet that are great for \n leaping, like an amphibian would."

    #message for incorrect answer
    incorrect4=Frame(lvl4_game, bg="#877c94", height=400, width=450)
    incorrect4.place(x=0, y=0)

    oops4= Label(master=incorrect4, text="Oops! " + justification + "\n"+"\n" +"If your stuck try going back to the" +"\n" +" instructions page for a hint!",
                  font=(("Comic Sans MS"), 14), width=42, height=10, fg="black", bg="#877c94")
    try_again4= Button(master=incorrect4, text=("Try again"), width=15, height=3, command=undo_wrong_answer4, bg="grey", fg="black", font=(("Comic Sans MS"), 10), relief="ridge" )
    translate_widgets()
    update_widget_colour()
    try_again4.place(x=170, y=270)
    oops4.place(x=0, y=0)



##########
def Level4():
    #hide widgets from previous screen
    global instr_lvl4
    for widget in instr_lvl4.winfo_children():
        widget.place_forget()
    
    ###
    global lvl4_game
    lvl4_game= Frame(root, width=800,  height=400, bg="#877c94")



    #displaying options
    #Clouded Leopard
    CLeopard_img = PIL.Image.open("E:\\12SDD\\ \\yr12\\project pics\\level 4\\other\\clouded-leopard.jpg")
    CLeopard_CTK =  customtkinter.CTkImage(CLeopard_img,
                                        size=(130,110))
    CLeopard_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=CLeopard_CTK, text="Clouded Leopard", fg_color="#877c94", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer4 (m))  
    CLeopard_button.bind("<Button-1>", disable_button)
    #red giant flying squirrel
    RGFSquirrel_img = PIL.Image.open("E:\\12SDD\\ \\yr12\\project pics\\level 4\\other\\red-giant-flying-squirrel.jpg")
    RGFSquirrel_CTK =  customtkinter.CTkImage(RGFSquirrel_img,
                                        size=(130,110))
    RGFSquirrel_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=RGFSquirrel_CTK, text="Red Giant Flying Squirrel", fg_color="#877c94", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer4 (m)) 
    RGFSquirrel_button.bind("<Button-1>", disable_button)
    #Malay Civet
    MCivet_img = PIL.Image.open("E:\\12SDD\\ \\yr12\\project pics\\level 4\\other\\Malay-civet.jpg")
    MCivet_CTK =  customtkinter.CTkImage(MCivet_img,
                                        size=(130,110))
    MCivet_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=MCivet_CTK, text="Malay Civet", fg_color="#877c94", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer4 (m)) 
    MCivet_button.bind("<Button-1>", disable_button)
    #Proboscis monkey
    PMonkey_img = PIL.Image.open("E:\\12SDD\\ \\yr12\\project pics\\level 4\\other\\Proboscis-monkey.jpg")
    PMonkey_CTK =  customtkinter.CTkImage(PMonkey_img,
                                        size=(130,110))
    PMonkey_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=PMonkey_CTK, text="Proboscis Monkey", fg_color="#877c94", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer4 (m))  
    PMonkey_button.bind("<Button-1>", disable_button)
    #Wallaces flying frog
    WFFrog_img = PIL.Image.open("E:\\12SDD\\ \\yr12\\project pics\\level 4\\amphibians\\Wallaces-flying-frog.jpg")
    WFFrog_CTK =  customtkinter.CTkImage(WFFrog_img,
                                        size=(130,110))
    WFFrog_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=WFFrog_CTK, text="Wallaces Flying Frog", fg_color="#877c94", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Wallaces Flying Frog":correct_choice4 (m)) 
    WFFrog_button.bind("<Button-1>", disable_button)
    #orangutan
    orangutan_img = PIL.Image.open("E:\\12SDD\\ \\yr12\\project pics\\level 4\\other\\Orangutan.jpg")
    orangutan_CTK =  customtkinter.CTkImage(orangutan_img,
                                        size=(130,110))
    orangutan_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=orangutan_CTK, text="Orangutan", fg_color="#877c94", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer4 (m))  
    orangutan_button.bind("<Button-1>", disable_button)

    #jade tree frog
    JTFrog_img = PIL.Image.open("E:\\12SDD\\ \\yr12\\project pics\\level 4\\amphibians\\jade-tree-frog.jpg")
    JTFrog_CTK =  customtkinter.CTkImage(JTFrog_img,
                                        size=(130,110))
    JTFrog_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=JTFrog_CTK, text="Jade Tree Frog", fg_color="#877c94", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Jade Tree Frog":correct_choice4 (m))   
    JTFrog_button.bind("<Button-1>", disable_button)

    #Pygmy elephant
    PElephant_img = PIL.Image.open("E:\\12SDD\\ \\yr12\\project pics\\level 4\\other\\Pygmy-Elephant.jpg")
    PElephant_CTK =  customtkinter.CTkImage(PElephant_img,
                                        size=(130,110))
    PElephant_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=PElephant_CTK, text="Pygmy Elephant", fg_color="#877c94", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer4 (m))   
    PElephant_button.bind("<Button-1>", disable_button)

    #BFHFrog
    BFHFrog_img = PIL.Image.open("E:\\12SDD\\ \\yr12\\project pics\\level 4\\amphibians\\bornean-flat-headed-frog.jpg")
    BFHFrog_CTK =  customtkinter.CTkImage(BFHFrog_img,
                                        size=(130,110))
    BFHFrog_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=BFHFrog_CTK, text="Bornean Flat Headed Frog", fg_color="#877c94", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command= (lambda m="Bornean Flat Headed Frog":correct_choice4 (m)))
    BFHFrog_button.bind("<Button-1>", disable_button)

    #results
    global score4
    global animal_found_list4
    score4 = Label(lvl4_game, text="SCORE: ", font=(("Times New Roman"), 18), bg="#877c94")
    animals_found_label4 = Label(lvl4_game, text="ANIMALS FOUND: ", height=3, width=20, font=(("Times New Roman"), 18), bg="#877c94", fg="black")
    global animal_found_list4
    animal_found_list4= Label(lvl4_game, text="", font=(("comic sans MS"), 12), bg="#b7a7c9", height=7, width=30)

    # #back option
    def back4_func():
        global instr_lvl4
        global cont4
        instr_lvl4.place(x=0, y=0)
        def return_lvl4():
            instr_lvl4.place_forget()
            cont4.configure(command=Level4)
        cont4.configure(command=return_lvl4)
        instr_lvl4.lift()
    back4= Button(master=lvl4_game, text=("instructions"), relief="raised", width=15, height=2, bg="#877c94", font=(("Comic Sans MS"), 8), command=back4_func)

    #reset level
    def reset4_func():
        global points
        global list_correct_animals
        global animal_found_list
        points=0
        list_correct_animals=""
        animal_found_list4.configure(text="")
        Level5()

    reset4= Button(master=lvl4_game, text=("reset"), width=8, height=1, command=reset4_func, bg="grey", font=(("Comic Sans MS"), 6), relief="raised")
    reset4.place(x=600, y=360)

    lvl4_game.place(x=0, y=0)
    back4.place(x=565, y=305)
    score4.place(x=550, y=0)
    animals_found_label4.place(x=490, y=40)
    animal_found_list4.place(x=470, y=120)
    BFHFrog_button.place(x=280, y=260)
    PElephant_button.place(x=140, y=260)
    JTFrog_button.place(x=0, y=260)
    orangutan_button.place(x=0, y=135)
    WFFrog_button.place(x=140, y=135)
    PMonkey_button.place(x=280, y=135)
    MCivet_button.place(x=280, y=0)
    RGFSquirrel_button.place(x=140, y=0)
    CLeopard_button.place(x=0, y=0)



    #update colour and language to match previous screen
    for widget in lvl4_game.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())
    lvl4_game.bind("<Visibility>", translate_widgets())




##########
def transition3(): 
    #hide widgets from summary screen
    for widget in lvl3_summary.winfo_children():
         widget.place_forget()
    
    global instr_lvl4
    instr_lvl4= Frame(root, width=800,  height=400, bg="#877c94")



    #display instructions for 4th level
    BRF = Label(instr_lvl4, text="Next we are going to look for " + "\n"+ "amphibians in the Borneo Rainforest!" +"\n"+"\n" + "Amphibians have slimy skin, webbed feet and" +"\n" +" short but stong limbs for leaping" + "\n" + " like the amphibians shown here!" + "\n"+"\n" +"Some examples of amphibians you may know" + "\n" + " include frogs, newts and salamanders!",
                 font=(("Comic Sans MS"), 12), bg="#877c94", width=40)
    
    #continue button to start 4th level
    global cont4
    cont4 =  Button(instr_lvl4, text="Continue", command=Level4, bg="#877c94", font=(("Comic Sans MS"), 8), relief="raised")

    #collage of amphibians
    amphibians_collage_image = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 4\\amphibians.jpg")
    TK_amphibians_collage =  customtkinter.CTkImage(amphibians_collage_image,
        size=(400,400))
    amphibians_collage =  customtkinter.CTkLabel(master=instr_lvl4, image=TK_amphibians_collage)

    instr_lvl4.place(x=0, y=0)
    amphibians_collage.place(x=0, y=0)
    cont4.place(x=700, y=300)
    BRF.place(x=400, y=40)



    #update colour and language to match previous screen
    for widget in instr_lvl4.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())
    instr_lvl4.bind("<Visibility>", translate_widgets())




##########

def correct_choice3(m): #when correct option chosen in level 3
    global points
    global score3
    global animal_found_list3
    global list_correct_animals

    #increments points and adds correct animal to list
    which_button(m)
    if points<2:
        points=points+1
        score3.config(text="SCORE: "+ str(points))
        animal_found_list3.config(text=list_correct_animals)
        translate_widgets()
    else:
    #when score of 3 reached
        points=0 

        #hide widgets from game screen
        for widget in lvl3_game.winfo_children():
            widget.place_forget() 
        
        #display summary
        global lvl3_summary
        lvl3_summary= Frame(root, width=800,  height=400, bg="light blue")



        #background
        GBR_bg = (PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 3\\GBR_bg.png")).resize((800, 400))
        global GBR_photo
        GBR_photo=ImageTk.PhotoImage(GBR_bg)
        GBR_label=Label(lvl3_summary, image=GBR_photo)
        GBR_label.place(x=0, y=0, relwidth=1, relheight=1)

        summary_screen3= Label(master=lvl3_summary, text=("These are the animals you found" +"\n" + " in the Great Barrier Reef:" +"\n" + list_correct_animals), width=50, height=10, bg="grey", font=(("Comic Sans MS"), 12), fg="black")
        next_level3= Button(master=lvl3_summary, text=("next level"), relief="raised", width=10, height=5, bg="light blue", font=(("Comic Sans MS"), 8), command=transition3)
        lvl3_summary.place(x=0, y=0)
        summary_screen3.place(x=150, y=75)
        next_level3.place(x=700, y=300)

        #reset once list displayed
        list_correct_animals=""

        #make 'go to level 3' available
        go_to_level.entryconfig("Level 3- fish", state=NORMAL)


        #update colour and language to match previous screen
        for widget in lvl3_summary.winfo_children():
            widget.bind("<Visibility>", update_widget_colour())
        lvl3_summary.bind("<Visibility>", translate_widgets())
    


def wrong_answer3(m): #when wrong anser chosen in level 3
    global oops3
    global try_again3

    def undo_wrong_answer3() :
        # when try again clicked, returns to level
        oops3.place_forget()
        try_again3.place_forget() 
        incorrect3.place_forget()

    if m== "reptile":
        justification="That is not a fish, it is a reptile! \n This is because it is covered with \n a hard shell and lays eggs. \n It also doesn't have fins or \n a streamlined body like a \n fish would."
    if m=="mammal":
        justification="That is not a fish, it is a mammal! \n This is because it is large, \n warm blooded and gives birth to live \n young. It also doesn't have fins or \n a streamlined body like a fish would."
    if m== "invertebrate":
        justification="That is not a fish, it is \n an invertebrate! This is because it \n doesn't have a spine and is tiny. \n It also doesn't have fins or \n a streamlined body like a \n fish would."

    #message for incorrect answer
    incorrect3=Frame(lvl3_game, bg="light blue", height=400, width=450)
    incorrect3.place(x=0, y=0)

    oops3= Label(master=incorrect3, text="Oops! "+ justification + "\n"+"\n" +"If your stuck try going back to the" +"\n" +" instructions page for a hint!",
                  font=(("Comic Sans MS"), 14), width=42, height=10, fg="black", bg="light blue")
    try_again3= Button(master=incorrect3, text=("Try again"), width=15, height=3, command=undo_wrong_answer3, bg="grey", fg="black", font=(("Comic Sans MS"), 10), relief="ridge")
    translate_widgets()
    update_widget_colour()
    try_again3.place(x=170, y=270)  
    oops3.place(x=0, y=0)


########
def Level3():
    #hide widgets from instruction screen
    global instr_lvl3
    for widget in instr_lvl3.winfo_children():
        widget.place_forget()
    ###



    global lvl3_game
    lvl3_game= Frame(root, width=800,  height=400, bg="light blue")
    #displaying options
    #clownfish
    Cfish_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 3\\fish\\clownfish.jpg")
    Cfish_CTK =  customtkinter.CTkImage(Cfish_img,
                                        size=(130,110))
    Cfish_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=Cfish_CTK, text="Clownfish", fg_color="light blue", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Clownfish":correct_choice3 (m)) 
    Cfish_button.bind("<Button-1>", disable_button)
    #blanket octapus
    Boctapus_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 3\\other\\blanket-octopus.jpg")
    Boctapus_CTK =  customtkinter.CTkImage(Boctapus_img,
                                        size=(130,110))
    Boctapus_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=Boctapus_CTK, text="Blanket Octapus", fg_color="light blue", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="invertebrate":wrong_answer3 (m))  
    Boctapus_button.bind("<Button-1>", disable_button)
    #dugong
    dugong_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 3\\other\\dugong.jpg")
    dugong_CTK =  customtkinter.CTkImage(dugong_img,
                                        size=(130,110))
    dugong_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=dugong_CTK, text="Dugong", fg_color="light blue", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer3 (m)) 
    dugong_button.bind("<Button-1>", disable_button)
    #green turtle
    Gturtle_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 3\\other\\green-turtle.jpg")
    Gturtle_CTK =  customtkinter.CTkImage(Gturtle_img,
                                        size=(130,110))
    Gturtle_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=Gturtle_CTK, text="Green Turtle", fg_color="light blue", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="reptile":wrong_answer3 (m)) 
    Gturtle_button.bind("<Button-1>", disable_button)
    #manta ray
    Mray_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 3\\fish\\manta-ray.jpg")
    Mray_CTK =  customtkinter.CTkImage(Mray_img,
                                        size=(130,110))
    Mray_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=Mray_CTK, text="Manta Ray", fg_color="light blue", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Manta Ray":correct_choice3 (m))  
    Mray_button.bind("<Button-1>", disable_button)
    #giant clam
    Wshark_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 3\\fish\\whale-shark.jpg")
    Wshark_CTK =  customtkinter.CTkImage(Wshark_img,
                                        size=(130,110))
    Wshark_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=Wshark_CTK, text="Whale Shark", fg_color="light blue", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Whale Shark":correct_choice3 (m)) 
    Wshark_button.bind("<Button-1>", disable_button)
    #humpback whale
    HWhale_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 3\\other\\humpback-whale.jpg")
    HWhale_CTK =  customtkinter.CTkImage(HWhale_img,
                                        size=(130,110))
    HWhale_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=HWhale_CTK, text="Humpback Whale", fg_color="light blue", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer3 (m))  
    HWhale_button.bind("<Button-1>", disable_button)
    #jellyfish
    jellyfish_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 3\\other\\jellyfish.jpg")
    jellyfish_CTK =  customtkinter.CTkImage(jellyfish_img,
                                        size=(130,110))
    jellyfish_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=jellyfish_CTK, text="Jellyfish", fg_color="light blue", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="invertebrate":wrong_answer3 (m))   
    jellyfish_button.bind("<Button-1>", disable_button)
    #mantis shrimp
    MShrimp_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 3\\other\\mantis-shrimp.jpg")
    MShrimp_CTK =  customtkinter.CTkImage(MShrimp_img,
                                        size=(130,110))
    MShrimp_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=MShrimp_CTK, text="Mantis Shrimp", fg_color="light blue", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command= (lambda m="invertebrate":wrong_answer3 (m)))   
    MShrimp_button.bind("<Button-1>", disable_button)

    #results
    global score3
    global animal_found_list3
    score3 = Label(lvl3_game, text="SCORE: ", font=(("Times New Roman"), 18), background="light blue")
    animals_found_label3 = Label(lvl3_game, text="ANIMALS FOUND: ", height=3, width=20, font=(("Times New Roman"), 18), background="light blue", fg="black")
    global animal_found_list3
    animal_found_list3= Label(lvl3_game, text="", font=(("comic sans MS"), 12), bg="#cad2fc", height=7, width=30)

    #back option
    def back3_func():
        global instr_lvl3
        global cont3
        instr_lvl3.place(x=0, y=0)
        def return_lvl3():
            instr_lvl3.place_forget()
            cont3.configure(command=Level3)
        cont3.configure(command=return_lvl3)
        instr_lvl3.lift()

    #reset level
    def reset3_func():
        global points
        global list_correct_animals
        global animal_found_list
        points=0
        list_correct_animals=""
        animal_found_list3.configure(text="")
        Level3()

    reset3= Button(master=lvl3_game, text=("reset"), width=8, height=1, command=reset3_func, bg="grey", font=(("Comic Sans MS"), 6), relief="raised")
    reset3.place(x=600, y=360)
    
    back3=  Button(master=lvl3_game, text=("instructions"), width=15, height=2, bg="light blue", font=(("Comic Sans MS"), 8), command=back3_func, relief="raised")
    lvl3_game.place(x=0, y=0)
    score3.place(x=550, y=0)
    animals_found_label3.place(x=490, y=40)
    animal_found_list3.place(x=470, y=120)
    MShrimp_button.place(x=280, y=260)
    jellyfish_button.place(x=140, y=260)
    HWhale_button.place(x=0, y=260)
    Wshark_button.place(x=0, y=135)
    Mray_button.place(x=140, y=135)
    Gturtle_button.place(x=280, y=135)
    dugong_button.place(x=280, y=0)
    Boctapus_button.place(x=140, y=0)
    Cfish_button.place(x=0, y=0)
    back3.place(x=565, y=305)


    #update colour and language to match previous screen
    for widget in lvl3_game.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())
    lvl3_game.bind("<Visibility>", translate_widgets())




#########
def transition2():
    #hide summary of level 2
    for widget in lvl2_summary.winfo_children():
         widget.place_forget()
    


    global instr_lvl3
    instr_lvl3= Frame(root, width=800,  height=400, bg="light blue")

    #display instructions for 3rd level
    GBR = Label(instr_lvl3, text="Next we are going to look for " + "\n"+ "fish in the Great Barrier Reef" +"\n"+"\n" + "Fish have fins and a streamlined body for swimmming," + "\n" + " like the fish shown here!" + "\n"+"\n" +"Some examples of fish you may know" + "\n" + " include salmon, trout and string rays!",
                 font=(("Comic Sans MS"), 12), bg="light blue", width=40)
    
    #continue button to start 3rd level
    global cont3
    cont3 =  Button(instr_lvl3, text="Continue", bg="light blue", font=(("Comic Sans MS"), 8), command=Level3, relief="raised")

    #collage of fish
    fish_collage_image = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 3\\fish-montage.jpg")
    TK_fish_collage =   customtkinter.CTkImage(fish_collage_image,
        size=(400,400))
    fish_collage =  customtkinter.CTkLabel(master=instr_lvl3, image=TK_fish_collage)

    instr_lvl3.place(x=0, y=0)
    fish_collage.place(x=0, y=0)
    cont3.place(x=700, y=300)
    GBR.place(x=400, y=50)



    #update colour and language to match previous screen
    for widget in instr_lvl3.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())
    instr_lvl3.bind("<Visibility>", translate_widgets())



##########

def correct_choice2(m): #when correct option chosen in level 2
    global points
    global score2
    global animal_found_list2
    global list_correct_animals
    #increments points and adds correct animal to list
    which_button(m)
    if points<2:
        points=points+1
        score2.config(text="SCORE: "+ str(points))
        animal_found_list2.configure(text=list_correct_animals)
        translate_widgets()
    else:
    #score of 3 reached, display summary
        points=0
        #hide widgets from level 2
        for widget in lvl2_game.winfo_children():
            widget.place_forget() 
        ###
        global lvl2_summary
        lvl2_summary= Frame(root, width=800,  height=400, bg="#ebd483")

        #background
        savanna_bg = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 2\\savanna_bg.png").resize((800, 400))
        global savanna_photo
        savanna_photo=ImageTk.PhotoImage(savanna_bg)
        savanna_label=Label(lvl2_summary, image=savanna_photo)

        summary_screen2= Label(master=lvl2_summary, text="These are the mammals you found" + "\n" + " in the African Savanna:" +"\n" + list_correct_animals, fg="black", font=(("Comic Sans MS"), 12), width=50, height=10, bg="grey")
        next_level2=Button(master=lvl2_summary, text=("next level"), width=10, height=5, bg="#ebd483", font=(("Comic Sans MS"), 8), command=transition2, relief="raised")

        lvl2_summary.place(x=0, y=0)
        savanna_label.place(x=0, y=0, relwidth=1, relheight=1)
        summary_screen2.place(x=150, y=75)
        next_level2.place(x=700, y=300)

        #reset list once displayed
        list_correct_animals=""
    
        #make 'go to level 2' available
        go_to_level.entryconfig("Level 2- mammals", state=NORMAL)

        #update colour and language to match previous screen
        for widget in lvl2_summary.winfo_children():
            widget.bind("<Visibility>", update_widget_colour())
        lvl2_summary.bind("<Visibility>", translate_widgets())
    



def wrong_answer2(m): #when wrong option chosen in level 2
    global oops2
    global try_again2

    def undo_wrong_answer2() :
        # when try again clicked, returns to level
        oops2.place_forget()
        try_again2.place_forget()
        incorrect2.place_forget()
    
    if m=="invertebrate":
        justification="That is not a mammal, it is an invertebrate! \n This is because it has a hard \n exoskeleton and is really tiny."
    if m=="amphibian":
        justification="That is not a mammal, it is an amphibian! \n This is because it has slimy \n skin and webbed feet \n that are good for leaping."
    if m== "reptile":
        justification="That is not a mammal, it is a reptile! \n This is because it has \n scales and short/no legs."
    if m=="bird":
        justification="This is not a mammal, it is a bird! \n This is because it has feathers \n and a beak."


    #message for incorrect answer
    incorrect2=Frame(lvl2_game, bg="#ebd483", height=400, width=450)
    incorrect2.place(x=0, y=0)

    oops2= Label(master=incorrect2, text="Oops! " + justification + "\n"+"\n" +"If your stuck try going back to the" +"\n" +" instructions page for a hint!",
                  font=(("Comic Sans MS"), 14), width=42, height=10, fg="black", bg="#ebd483")
    try_again2= Button(master=incorrect2, text=("Try again"), width=15, height=3, command=undo_wrong_answer2, bg="grey", fg="black", font=(("Comic Sans MS"), 10), relief="ridge") 
    translate_widgets()
    update_widget_colour()
    try_again2.place(x=170, y=270)
    oops2.place(x=0, y=0)





##########

def Level2():
    #hide widgets from instructions
    for widget in instr_lvl2.winfo_children():
         widget.place_forget()
    
    ###


    global lvl2_game
    lvl2_game= Frame(root, width=800,  height=400, bg="#ebd483")
    #displaying options
    #cobra
    Cobra_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 2\\other\\cobra.jpg")
    cobra_CTK =  customtkinter.CTkImage(Cobra_img,
                                    size=(130,110))
    cobra_button =  customtkinter.CTkButton( master=lvl2_game, image=cobra_CTK, text="Cobra", fg_color="#ebd483", font=(("Comic Sans MS"), 12), text_color="black", compound="bottom",
                                        command=lambda m="reptile":wrong_answer2 (m))   
    cobra_button.bind("<Button-1>", disable_button)
    #aardvark
    aardvark_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 2\\mammals\\aardvark.jpg")
    aardvark_CTK =  customtkinter.CTkImage(aardvark_img,
                                    size=(130,110))
    aardvark_button =  customtkinter.CTkButton(master=lvl2_game, image=aardvark_CTK, text="Aardvark", fg_color="#ebd483", font=(("Comic Sans MS"), 12), text_color="black", compound="bottom",
                                        command=lambda m="Aardvark":correct_choice2 (m))   
    aardvark_button.bind("<Button-1>", disable_button)
    #african_elephant
    african_elephant_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 2\\mammals\\african_elephant.jpg")
    african_elephant_CTK =  customtkinter.CTkImage(african_elephant_img,
                                    size=(130,110))
    african_elephant_button =  customtkinter.CTkButton( master=lvl2_game, image=african_elephant_CTK, text="African Elephant", fg_color="#ebd483", font=(("Comic Sans MS"), 12), text_color="black", compound="bottom",
                                        command=lambda m="African Elephant":correct_choice2 (m))   
    african_elephant_button.bind("<Button-1>", disable_button)
    #hornbill
    hornbill_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 2\\other\\hornbill.jpg")
    hornbill_CTK =  customtkinter.CTkImage(hornbill_img,
                                    size=(130,110))
    hornbill_button =  customtkinter.CTkButton( master=lvl2_game, image=hornbill_CTK, text="Hornbill", fg_color="#ebd483", font=(("Comic Sans MS"), 12), text_color="black", compound="bottom",
                                        command=lambda m="bird":wrong_answer2 (m))   
    hornbill_button.bind("<Button-1>", disable_button)
    #scorpion
    scorpion_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 2\\other\\scorpion.jpg")
    scorpion_CTK =  customtkinter.CTkImage(scorpion_img,
                                    size=(130,110))
    scorpion_button =  customtkinter.CTkButton( master=lvl2_game, image=scorpion_CTK, text="Scorpion", fg_color="#ebd483", font=(("Comic Sans MS"), 12), text_color="black", compound="bottom",
                                        command=lambda m="invertebrate":wrong_answer2 (m))   
    scorpion_button.bind("<Button-1>", disable_button)
    #rhinoceros
    rhinoceros_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 2\\mammals\\rhinoceros.jpg")
    rhinoceros_CTK =  customtkinter.CTkImage(rhinoceros_img,
                                    size=(130,110))
    rhinoceros_button =  customtkinter.CTkButton( master=lvl2_game, image=rhinoceros_CTK, text="Rhinoneros", fg_color="#ebd483", font=(("Comic Sans MS"), 12), text_color="black", compound="bottom",
                                        command=lambda m="Rhinoceros":correct_choice2 (m))   
    rhinoceros_button.bind("<Button-1>", disable_button)
    #ostrich
    ostrich_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 2\\other\\ostrich.jpg")
    ostrich_CTK =  customtkinter.CTkImage(ostrich_img,
                                    size=(130,110))
    ostrich_button =  customtkinter.CTkButton( master=lvl2_game, image=ostrich_CTK, text="Ostrich", fg_color="#ebd483", font=(("Comic Sans MS"), 12), text_color="black", compound="bottom",
                                        command=lambda m="bird":wrong_answer2 (m))   
    ostrich_button.bind("<Button-1>", disable_button)
    #dung beetle
    dung_beetle_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 2\\other\\dung-beetle.jpg")
    dung_beetle_CTK =  customtkinter.CTkImage(dung_beetle_img,
                                    size=(130,110))
    dung_beetle_button =  customtkinter.CTkButton( master=lvl2_game, image=dung_beetle_CTK, text="Dung Beetle", fg_color="#ebd483", font=(("Comic Sans MS"), 12), text_color="black", compound="bottom",
                                        command=lambda m="invertebrate":wrong_answer2 (m))   
    dung_beetle_button.bind("<Button-1>", disable_button)

    #african spurred tortoise
    ASTortoise_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 2\\other\\african-spurred-tortoise.jpg")
    ASTortoise_CTK =  customtkinter.CTkImage(ASTortoise_img,
                                    size=(130,110))
    ASTortoise_button =  customtkinter.CTkButton(master=lvl2_game, image=ASTortoise_CTK, text="African Spurred Tortoise", fg_color="#ebd483", font=(("Comic Sans MS"), 12), text_color="black", compound="bottom",
                                        command= (lambda m="reptile":wrong_answer2 (m)))   
    ASTortoise_button.bind("<Button-1>", disable_button)

    #results
    global score2
    global animal_found_list2
    score2 = Label(lvl2_game, text="SCORE: ", font=(("Times New Roman"), 18), bg="#ebd483")
    animals_found_label2 = Label(lvl2_game, text="ANIMALS FOUND: ", height=3, width=20, font=(("Times New Roman"), 18), bg="#ebd483")
    global animal_found_list2
    animal_found_list2= Label(lvl2_game, text="", font=(("comic sans MS"), 12), height=7, width=30, bg="#edda98")

    #back option
    def back2_func():
        global instr_lvl2
        global cont2
        instr_lvl2.place(x=0, y=0)
        def return_lvl2():
            instr_lvl2.place_forget()
            cont2.configure(command=Level2)
        cont2.configure(command=return_lvl2)
        instr_lvl2.lift()

    back2=  Button(master=lvl2_game, text=("instructions"), bg="#ebd483", width=15, height=2, font=(("Comic Sans MS"), 8), command=back2_func)

    #reset level
    def reset2_func():
        global points
        global list_correct_animals
        global animal_found_list
        points=0
        list_correct_animals=""
        animal_found_list2.configure(text="")
        Level2()

    reset2= Button(master=lvl2_game, text=("reset"), width=8, height=1, command=reset2_func, bg="grey", font=(("Comic Sans MS"), 6), relief="raised")
    reset2.place(x=600, y=360)

    lvl2_game.place(x=0, y=0)
    back2.place(x=565, y=305)
    score2.place(x=550, y=0)
    animals_found_label2.place(x=490, y=40)
    animal_found_list2.place(x=470, y=120)
    ASTortoise_button.place(x=280, y=260)
    dung_beetle_button.place(x=140, y=260)
    ostrich_button.place(x=0, y=260)
    rhinoceros_button.place(x=0, y=135)
    scorpion_button.place(x=140, y=135)
    hornbill_button.place(x=280, y=135)
    african_elephant_button.place(x=280, y=0)
    aardvark_button.place(x=140, y=0)
    cobra_button.place(x=0, y=0)




    #update colour and language to match previous screen
    for widget in lvl2_game.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())
    lvl2_game.bind("<Visibility>", translate_widgets())




##########


def transition1():
    #hide widgets from level 1 summary
    for widget in lvl1_summary.winfo_children():
         widget.place_forget()
    


    global instr_lvl2
    instr_lvl2= Frame(root, width=800,  height=400, bg="#ebd483" )

    #display instructions for second level
    Savanna = Label(instr_lvl2, text="Next we are going to look for " + "\n"+ "mammals in the African Savanna" +"\n"+"\n" + "Mammals have skin " + "\n"+ "and are ussually really big," + "\n" + " like the mammals shown here!" + "\n"+"\n" +"Some examples of mammals you may know" + "\n" + " include dogs, horses and humans!", 
                    font=(("Comic Sans MS"), 12), bg="#ebd483", width=40)
    
    #continue button to start 2nd level
    global cont2
    cont2 =  Button(instr_lvl2, text="Continue", bg="#ebd483", font=(("Comic Sans MS"), 8), command=Level2, relief="raised")

    #collage of mammals- to refer to how mammals look
    mammals_collage_image = PIL.Image.open(r"E:\\12SDD\\\yr12\project pics\level 2\Mammal_intro.jpg")
    TK_mammals_collage =  customtkinter.CTkImage(mammals_collage_image,
        size=(400,400))
    mammals_collage =  customtkinter.CTkLabel(master=instr_lvl2, image=TK_mammals_collage, text="")

    instr_lvl2.place(x=0, y=0)
    mammals_collage.place(x=0, y=0)
    cont2.place(x=700, y=300)
    Savanna.place(x=400, y=50)



    #update colour and language to match previous screen
    for widget in instr_lvl2.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())
    instr_lvl2.bind("<Visibility>", translate_widgets())



##########


##
#defining what happens when correct/incorrect buttons are pressed for LEVEL 1


def wrong_answer(m): #when wrong button clicked, UNIQUE TO EACH LEVEL
    
    def undo_wrong_answer() :
        # when try again clicked, returns to level
        oops.place_forget()
        try_again.place_forget()
        incorrect.place_forget()
    if m=="mammal":
        justification="That is not a bird, it is a mammal! \n This is because it has fur, is big,\n and gives birth to live young."
    if m=="amphibian":
        justification="That is not a bird, it is an amphibian! \n This is because it has slimy skin and \n webbed feet that are good for \n leaping, not feathers or a beak."
    if m== "reptile":
        justification="That is not a bird, it is a reptile! \n This is because it has scales and a \n long tail, not feathers or a beak."

    global oops
    global try_again
    #message for incorrect answer
    incorrect=Frame(lvl1_game, bg="#4c5751", height=400, width=450)
    incorrect.place(x=0, y=0)
    oops= Label(master=incorrect, text="Oops! " + justification + "\n" + "\n" +"If your stuck try going back to the" +"\n" +" instructions page for a hint!",
                 font=(("Comic Sans MS"), 14), width=42, height=10, fg="black", bg="#4c5751")
    try_again= Button(master=incorrect, text=("Try again"), width=15, height=3, command=undo_wrong_answer, bg="grey", fg="black", font=(("Comic Sans MS"), 10), relief="ridge")
    translate_widgets()
    update_widget_colour()
    oops.place(x=0, y=0)
    try_again.place(x=170, y=270)



    

def correct_choice(m): #refects correct choice on screen; increment score and adds to list of animals found--UNIQUE TO EACH LEVEL
    #increments points and adds correct animal to list
    which_button(m)
    global points
    global list_correct_animals
    if points<2: #score of 3 not reached
        points=points+1
        score1.config(text="SCORE: "+ str(points))
        animal_found_list.config(text=list_correct_animals)
        translate_widgets()
    else:# move on to next level when score =3
        points=0

        #hide widgets from level 1
        for widget in lvl1_game.winfo_children():
            widget.place_forget() 



        #display level 1 summary
        global lvl1_summary
        lvl1_summary= Frame(root, width=800,  height=400, bg="#4c5751")

        #background
        amazon_bg = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 1\\amazon_bg.png")
        global amazon_photo
        amazon_photo=ImageTk.PhotoImage(amazon_bg)
        amazon_label=Label(lvl1_summary, image=amazon_photo)

        summary_screen1= Label(master=lvl1_summary, text="These are the aves you " +"\n" + "found in the Amazon Rainforest:" + "\n" + list_correct_animals,
                                fg="black", width=50, height=10, bg="grey", font=(("Comic Sans MS"), 12))
        next_level= Button(master=lvl1_summary, text=("next level"), width=10, height=5, command=transition1, bg="#4c5751", font=(("Comic Sans MS"), 8), relief="raised")

        lvl1_summary.place(x=0, y=0)
        amazon_label.place(x=0, y=0, relwidth=1, relheight=1)
        summary_screen1.place(x=150, y=75)
        next_level.place(x=700, y=300)

        #reset list once displayed
        list_correct_animals=""

        #make 'go to level 1' available
        go_to_level.entryconfig("Level 1- birds", state=NORMAL)


        #update colour and language to match previous screen
        for widget in lvl1_summary.winfo_children():
            widget.bind("<Visibility>", update_widget_colour())
        lvl1_game.bind("<Visibility>", translate_widgets())
    

   
      

##


def Level1():
    #hide widgets from instruction screen
    for widget in root.winfo_children():
         widget.place_forget() 
    


    global lvl1_game
    lvl1_game= Frame(root, width=800, height=400, bg="#4c5751")

    #displaying options for lvl1
    #Macaw
    macaw_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 1\\birds\\blue_macaw.jpg")
    macaw_CTK =  customtkinter.CTkImage(macaw_img,
                                        size=(130,110))
    macaw_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=macaw_CTK, text="Blue and Gold Macaw", fg_color="#4c5751", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Blue and Gold Macaw":correct_choice (m))   
    macaw_button.bind("<Button-1>", disable_button)
    #capybara
    capybara_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 1\\other\\capybara.jpeg")
    capybara_CTK =  customtkinter.CTkImage(capybara_img,
                                        size=(130,110))
    capybara_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=capybara_CTK, text="Capybara", fg_color="#4c5751", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer (m))   
    capybara_button.bind("<Button-1>", disable_button)
    #jaguar
    jaguar_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 1\\other\\jaguar.jpeg")
    jaguar_CTK =  customtkinter.CTkImage(jaguar_img,
                                        size=(130,110))
    jaguar_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=jaguar_CTK, text="Jaguar", fg_color="#4c5751", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer (m))   
    jaguar_button.bind("<Button-1>", disable_button)
    #poison dart frog
    PDfrog_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 1\\other\\poison-dart-frog.jpeg")
    PDfrog_CTK =  customtkinter.CTkImage(PDfrog_img,
                                        size=(130,110))
    PDfrog_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=PDfrog_CTK, text="Poison dart frog", fg_color="#4c5751", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="amphibian":wrong_answer (m))   
    PDfrog_button.bind("<Button-1>", disable_button)
    #Pantalón-de-Cuerno
    Pcuerno_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 1\\birds\\Pantalón-de-Cuerno.jpg")
    Pcuerno_CTK =  customtkinter.CTkImage(Pcuerno_img,
                                        size=(130,110))
    Pcuerno_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=Pcuerno_CTK, text="Pantalón-de-Cuerno", fg_color="#4c5751", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="Pantalón-de-Cuerno":correct_choice (m))   
    Pcuerno_button.bind("<Button-1>", disable_button)
    #Red Howler Money
    RHMonkey_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 1\\other\\red-howler-monkey.jpeg")
    RHMonkey_CTK =  customtkinter.CTkImage(RHMonkey_img,
                                        size=(130,110))
    RHMonkey_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=RHMonkey_CTK, text="Red Howler Monkey", fg_color="#4c5751", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer (m))   
    RHMonkey_button.bind("<Button-1>", disable_button)
    #black capped squirrel monkey
    BCSMonkey_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 1\\other\\black-capped-squirrel-monkey.jpeg")
    BCSMonkey_CTK =  customtkinter.CTkImage(BCSMonkey_img,
                                        size=(130,110))
    BCSMonkey_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=BCSMonkey_CTK, text="Black Capped Squirrel", fg_color="#4c5751", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="mammal":wrong_answer (m))   
    BCSMonkey_button.bind("<Button-1>", disable_button)
    #green anaconda
    GAnaconda_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 1\\other\\green-anaconda.jpeg")
    GAnaconda_CTK =  customtkinter.CTkImage(GAnaconda_img,
                                        size=(130,110))
    GAnaconda_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=GAnaconda_CTK, text="Green Anaconda", fg_color="#4c5751", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command=lambda m="reptile":wrong_answer (m))   
    GAnaconda_button.bind("<Button-1>", disable_button)

    #Toucan-Collared-Aracari
    CAToucan_img = PIL.Image.open("E:\\12SDD\\\\yr12\\project pics\\level 1\\birds\\Toucan-Collared-Aracari.jpg")
    CAToucan_CTK =  customtkinter.CTkImage(CAToucan_img,
                                        size=(130,110))
    CAToucan_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=CAToucan_CTK, text="Toucan Collared Aracari", fg_color="#4c5751", font=(("Comic Sans MS"), 12), compound="bottom",
                                        command= (lambda m="Toucan Collared Aracari":correct_choice (m)))   
    CAToucan_button.bind("<Button-1>", disable_button)
    #displaying score and correct answers- lvl1
    global score1
    global animals_found1
    score1 = Label(lvl1_game, text="SCORE: ", font=(("Times New Roman"), 18), bg="#4c5751")
    animals_found_label = Label(lvl1_game, text="ANIMALS FOUND: ", height=3, width=20, font=(("Times New Roman"), 18), bg="#4c5751")
    global animal_found_list
    animal_found_list= Label(lvl1_game, text="", font=(("comic sans MS"), 12), bg="#72827a", height=7, width=30)

    #back option
    def back1_func():
        global instr_lvl1
        global cont
        instr_lvl1.place(x=0, y=0)
        def return_lvl1():
            instr_lvl1.place_forget()
            cont2.configure(command=Level1)
        cont.configure(command=return_lvl1)
        instr_lvl1.lift()
    back1= Button(master=lvl1_game, text=("instructions"), width=15, height=2, command=back1_func, bg="#4c5751", font=(("Comic Sans MS"), 8), relief="raised")

    #reset level
    def reset1_func():
        global points
        global list_correct_animals
        global animal_found_list
        points=0
        list_correct_animals=""
        animal_found_list.configure(text="")
        Level1()

    reset1= Button(master=lvl1_game, text=("reset"), width=8, height=1, command=reset1_func, bg="grey", font=(("Comic Sans MS"), 6), relief="raised")
    reset1.place(x=600, y=360)


    lvl1_game.place(x=0, y=0)
    back1.place(x=565, y=305)
    score1.place(x=570, y=0)
    animals_found_label.place(x=490, y=40)
    animal_found_list.place(x=470, y=120)
    CAToucan_button.place(x=280, y=260)
    GAnaconda_button.place(x=140, y=260)
    BCSMonkey_button.place(x=0, y=260)
    RHMonkey_button.place(x=0, y=135)
    Pcuerno_button.place(x=140, y=135)
    PDfrog_button.place(x=280, y=135)
    jaguar_button.place(x=280, y=0)
    capybara_button.place(x=140, y=0)
    macaw_button.place(x=0, y=0)

    #update colour and language to match previous screen
    for widget in lvl1_game.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())
    lvl1_game.bind("<Visibility>", translate_widgets())



    




##########



def start(): #displayed first set of instruction
    #hide widgets from intro screen
    for widget in title_screen.winfo_children():
         widget.place_forget() 



    global instr_lvl1
    instr_lvl1=Frame(root, width=800, height=400, bg="#4c5751")

    #display instructions for first level
    Amazon = Label(instr_lvl1, text="Welcome to the Amazon Rainforest!" + "\n"+"\n"+ "We need to find 3 aves." +"\n" + "Remember, aves is the scientific name for birds." + "\n"+"\n"+ "Birds have feathers and beaks and lay eggs," + "\n" + " like the birds shown here!", font=(("Comic Sans MS"), 12), width=40, bg="#4c5751")

    #continue button to start 1st level
    global cont
    cont = Button(instr_lvl1, text="Continue", command=Level1, bg="#4c5751", font=(("Comic Sans MS"), 8), relief="raised")

    #collage of birds-illustration of what birds look like
    birds_collage_image = PIL.Image.open("E:\\12SDD\\\yr12\\project pics\\level 1\\lvl-1-intro.png")
    TK_birds_collage =  customtkinter.CTkImage(birds_collage_image,
        size=(400,400))
    birds_collage =  customtkinter.CTkLabel(master=instr_lvl1, image=TK_birds_collage, text="")

    instr_lvl1.place(x=0, y=0)
    birds_collage.place(x=0, y=0)
    cont.place(x=700, y=300)
    Amazon.place(x=400, y=100)

    #update colour and language to match previous screen
    for widget in instr_lvl1.winfo_children():
        widget.bind("<Visibility>", update_widget_colour())
    instr_lvl1.bind("<Visibility>", translate_widgets())
 






############


def introduction(): #first screen displayed 
    global title_screen
    title_screen=Frame(root , width=800, height=400)

    #background of intro
    title_bg = PIL.Image.open("E:\\12SDD\\\\yr12\\intro_screen_bg.png")
    global title_photo
    title_photo=ImageTk.PhotoImage(title_bg)
    bg_label=Label(title_screen, image=title_photo, text="")

    global begin
    begin = customtkinter.CTkButton(title_screen, text="Begin", command=start, text_color="black", font=(("Comic Sans MS"), 18), height=15, width=25, corner_radius=5, border_width=2, border_color="brown", fg_color="white")
    intro = Label(title_screen, text="Animal Classification Game" + "\n" + "Journey Across the Globe", height = 3, width=20, font=(("Comic Sans MS"), 16), bg="white")

    title_screen.place(x=0, y=0)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    intro.place(x=275, y=110)
    begin.place(x=370, y=210)
    title_screen.lift()


######################################################################################################################################################


# Create a menubar.
menubar = Menu()
menubar.configure(bg="#686968")

# Create the settings menu.
settings_menu = Menu(menubar, tearoff=False)

# Append settings menu to the menubar.
menubar.add_cascade(menu=settings_menu, label="Settings")


######language options#####

def change_language():
    def clicked(event):# what to do when an option is chosen
        #while working on translating, a loading label & progressbar are displayed
        loading=Label(root, text="translating...", font=(("Arial"), 25), bg='#ffff54', height=3)
        loading.place(x=300, y=150)
        progress = ttk.Progressbar(root, orient = HORIZONTAL, length = 180, mode = 'indeterminate')
        progress.start()
        progress.place(x=300, y=150)
        def translation_task(): #how to translate
            try:
                for widget in root.winfo_children(): #for every frame in root
                    for widget in widget.winfo_children(): #for every widget in that frame
                        try:

                            #get original language code
                            language_code = detect(widget.cget("text")) #detect what the current language is  

                            #get the language key which your trying to change to       
                            for key, value in languages.items(): #go through each language
                                if(value==options.get()): #if it matches what was chosen
                                    global to_language_key
                                    to_language_key=key

                            #turn original text into text blob
                            words=textblob.TextBlob(widget.cget("text"))

                            #translate text
                            words=words.translate(from_lang=language_code, to=to_language_key)
                            widget.configure(text=words)
                        except:
                            pass

            except Exception as e:#if something goes wrong show an error
                messagebox.showerror("Translator", e)
            
            #remove loading screen
            progress.stop
            progress.place_forget()
            loading.place_forget()
        
        translation_thread=threading.Thread(target=translation_task)
        translation_thread.start()

    #display the language options when 'language' button clicked
    options=ttk.Combobox(root, width=30, value=language_list)
    options.place(x=0, y=5)
    lang_options=True #the language options open, so its true
    options.bind("<<ComboboxSelected>>", clicked) #when something from the combobox is chosen, run 'clicked' function

settings_menu.add_command(
    label="Language options",
    command=change_language,
)

settings_menu.add_separator()

######colour options######

global dark_mode
global light_mode
global contrast_mode
global def_mode
dark_mode=False
light_mode=False
contrast_mode=False
def_mode=False

def colour1_change():  
    global dark_mode
    global light_mode
    global contrast_mode
    global def_mode
    try:  
        #changes all widgets to shades to white & black

        if hasattr(root, 'bg'):
                root.configure(bg="black") #if the widget has a background, make  it black

        for widget in root.winfo_children(): #for every frame in root, make the bg black
            if hasattr(widget, 'bg'):
                widget.configure(bg="black")

            for widget in widget.winfo_children(): # for every widget in that frame, make its bg black and text colour white
                if isinstance(widget, Label):
                    widget.configure(bg="black", fg="white")
                if isinstance(widget, Button):
                    widget.configure(bg="black", fg="white")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="black", text_color="white")
                if isinstance(widget, customtkinter.CTkLabel):  
                    pass
            widget.update()
        root.update()
        
        dark_mode=True
        light_mode=False
        contrast_mode=False
        def_mode=False
    except Exception as e:
        pass
    root.update()

def colour2_change():
    global dark_mode
    global light_mode
    global contrast_mode
    global def_mode
    try:
        #changes all widgets to white bg and black text 
        if hasattr(root, 'bg'):
            root.configure(bg="white")
        root.update()

        for widget in root.winfo_children():
            if hasattr(widget, 'bg'):
                widget.configure(bg="black")
            for widget in widget.winfo_children():
                if isinstance(widget, Label):
                    widget.configure(bg="white", fg="black")
                if isinstance(widget, Button):
                    widget.configure(bg="white", fg="black") 
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="white", text_color="black")  
            widget.update()

        light_mode=True
        dark_mode=False
        contrast_mode=False
        def_mode=False
    except Exception as e:
        pass
    root.update()


def colour3_change():
    global dark_mode
    global light_mode
    global contrast_mode
    global def_mode
    try:
        #changes all widgets to red bg and green text
        if hasattr(root, 'bg'):
            root.configure(bg="red")
        for widget in root.winfo_children():
            for widget in widget.winfo_children():
                if isinstance(widget, Label):
                    widget.configure(bg="red", fg="green")
                if isinstance(widget, Button):
                    widget.configure(bg="red", fg="green") 
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="red", text_color="green")  
            widget.update()

        contrast_mode=True
        light_mode=False
        dark_mode=False
        def_mode=False
    except Exception as e:
        pass
    root.update()

    

def colour4_change():
    global dark_mode
    global light_mode
    global contrast_mode
    global def_mode
    try:
        if instr_lvl1.winfo_exists:
            for widget in instr_lvl1.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#4c5751", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#4c5751", text_color="black")
            root.update()
        if lvl1_game.winfo_exists: 
            for widget in lvl1_game.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#4c5751", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#4c5751", text_color="black")
            root.update()
        if lvl1_summary.winfo_exists:
            for widget in lvl1_summary.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#4c5751", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#4c5751", text_color="black")
            root.update()
        if instr_lvl2.winfo_exists:
            for widget in instr_lvl2.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#ebd483", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#ebd483", text_color="black")
            root.update()                    
        if lvl2_game.winfo_exists: 
            for widget in lvl2_game.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#ebd483", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#ebd483", text_color="black")
            root.update()
        if lvl2_summary.winfo_exists:
            for widget in lvl2_summary.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#ebd483", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#ebd483", text_color="black")
            root.update()
        if instr_lvl3.winfo_exists:
            for widget in instr_lvl3.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="light blue", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="light blue", text_color="black")
            root.update()
        if lvl3_game.winfo_exists: 
            for widget in lvl3_game.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="light blue", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="light blue", text_color="black")
            root.update()
        if lvl3_summary.winfo_exists:
            for widget in lvl3_summary.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="light blue", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="light blue", text_color="black")
            root.update()
        if instr_lvl4.winfo_exists:
            for widget in instr_lvl4.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#877c94", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#877c94", text_color="black")
            root.update()
        if lvl4_game.winfo_exists: 
            for widget in lvl4_game.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#877c94", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#877c94", text_color="black")
            root.update()
        if lvl4_summary.winfo_exists:
            for widget in lvl4_summary.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#877c94", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#877c94", text_color="black")
            root.update()      
        if instr_lvl5.winfo_exists:
            for widget in instr_lvl5.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#cca47c", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#cca47c", text_color="black")
            root.update()
        if lvl5_game.winfo_exists: 
            for widget in lvl5_game.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#cca47c", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#cca47c", text_color="black")
            root.update()
        if lvl5_summary.winfo_exists:
            for widget in lvl5_summary.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="#cca47c", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="#cca47c", text_color="black")
            root.update()
        if instr_lvl6.winfo_exists:
            for widget in instr_lvl6.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="light green", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="light green", text_color="black")
            root.update()
        if lvl6_game.winfo_exists: 
            for widget in lvl6_game.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="light green", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="light green", text_color="black")
            root.update()
        if lvl6_summary.winfo_exists:
            for widget in lvl6_summary.winfo_children():
                if isinstance(widget, Button) or isinstance (widget, Label):
                    widget.configure(bg="light green", fg="black")
                if isinstance(widget, customtkinter.CTkButton):
                    widget.configure(fg_color="light green", text_color="black")
            root.update()

        def_mode=True
        contrast_mode=False
        light_mode=False
        dark_mode=False
    except Exception as e:
        pass
    root.update()
    

        


theme_menu = Menu(menubar, tearoff=False)
settings_menu.add_cascade(menu=theme_menu, label="Theme")


global theme
theme=IntVar()
theme.set(4)
theme_menu.add_radiobutton(
    label="Dark",
    command=colour1_change,
    variable=theme,
    value=1,
)
theme_menu.add_radiobutton(
    label="Light",
    command=colour2_change,
    variable=theme,
    value=2,
)
theme_menu.add_radiobutton(
    label="High Contrast",
    command=colour3_change,
    variable=theme,
    value=3,
)
theme_menu.add_radiobutton(
    label="Default",
    command=colour4_change,
    variable=theme,
    value=4,
)


settings_menu.add_separator()



#text size options


def scale_widget(scale, widget): #change each widget's text size according to scale
    new_size=0
    def widget_has_text(widget): #how to check if widget has text
        try:
            text = widget.cget("text")
            return text != ""
        except TclError:
            return False

    if widget_has_text(widget): 
        try:
            if len(widget.cget("text"))>1: #if the widget has text

                # Retrieve the font configuration of the label
                current_font = widget.cget("font")

                # make it into approproate format
                font_obj = tkfont.Font(font=current_font)

                #adjust according to scale
                if scale==0.2:
                    new_size = int(font_obj['size'] * 0.7)
                if scale==1.5:
                    new_size = int(font_obj['size'] * 1.5)
                #create new_font variable
                new_font = current_font

                #replace the size part of the font
                y = [new_font[0], new_font[1]]
                y[1] = new_size
                x = tuple(y)
                
                #adjust the size of text
                widget.configure(font=x)
        except TypeError:
            pass    

def scale_all_widgets(scale): #send every widget to scale_widget function
    root.update()
    for widget in root.winfo_children():
        if isinstance(widget, Frame):
            for widget in widget.winfo_children():
                scale_widget(scale, widget)
        else:
            scale_widget(scale, widget)
        widget.update()
    


size_menu = Menu(menubar, tearoff=False)
settings_menu.add_cascade(menu=size_menu, label="Text size")


size_menu.add_radiobutton(
    label="+",
    command=lambda: scale_all_widgets(1.5), 
)

size_menu.add_radiobutton(
    label="-",
    command=lambda: scale_all_widgets(0.5),
)



#quit option
def quit_game():
    sys.exit()

menubar.add_cascade(label="Quit Game", command=quit_game)

# Append replay button to the menubar.
menubar.add_cascade(command=introduction, label="Replay")


go_to_level = Menu(menubar, tearoff=False)
menubar.add_cascade(menu=go_to_level, label="Go to level...")


# def to_lvl1():
#     try:
#         instr_lvl1

go_to_level.add_command(
    label="Level 1- birds",
    command= start, 
    state=DISABLED
)

go_to_level.add_command(
    label="Level 2- mammals",
    command= transition1, 
    state=DISABLED

)

go_to_level.add_command(
    label="Level 3- fish",
    command= transition2, 
    state=DISABLED

)

go_to_level.add_command(
    label="Level 4- amphibians",
    command= transition3, 
    state=DISABLED

)

go_to_level.add_command(
    label="Level 5- reptiles",
    command= transition4,
    state=DISABLED
 
)

go_to_level.add_command(
    label="Level 6- invertebrates",
    command= transition5,
    state=DISABLED
 
)










# Insert the menubar in the main window.
root.config(menu=menubar)







############################################################################################################################################################

introduction()

root.mainloop()