import PIL.Image
from PIL import ImageTk, Image
from tkinter import *
from tkinter import Tk
import customtkinter
import sys

root = Tk()
root.title('animal classification game')
root.geometry("800x400")


def menu_options():
    def half():
        pass
    def reg():
        pass
    def double():
        root.geometry("1600x800")
        for widget in root.winfo_children():
            x=int(widget.winfo_rootx())
            y=int(widget.winfo_rooty())
            widget.place_configure(x=2*x, y=2*y)
            x=widget.cget("height")
            y=widget.cget("width")
            widget.config(height=2*x, width=2*y)
            for widget in widget.winfo_children():
                height=widget.cget("height")
                width=widget.cget("width")
                widget.configure(height=2*height, width=2*width)
                x=int(widget.winfo_rootx())
                y=int(widget.winfo_rooty())
                widget.place_configure(x=2*x, y=2*y)
                # if isinstance(widget, PhotoImage):
                #     widget.configure(size=(1600, 800))
                if len(widget.cget("image"))>0:
                    widget.place_configure(relheight=1, relwidth=1)

    def size_options():
        size_options=Frame(size_frame, height=15, width=5)
        size_options.place(x=790, y=300)
        half_button=Button(size_options, text="50%", height=10, width=20, command=half, bg="grey")
        half_button.grid(row=0, column=0)
        reg_button=Button(size_options, text="100%", height=10, width=20, command=reg, bg="grey")
        reg_button.grid(row=1, column=0)
        double_button=Button(size_options,text="200%", height=10, width=20, command=double, bg="grey")
        double_button.grid(row=2, column=0)
        size_options.place(x=790, y=300)
        size_options.lift()

    size_frame=Frame(root, height=3, width=6)
    size_frame.place(x=710, y=45)
    size=Button(size_frame, text="Size Options", command=size_options, height=2, width=12)
    size.pack(side=RIGHT)
    size_frame.lift()
    size.lift()

menu_frame=Frame(root, height=3, width=6, bg="grey")
menu_frame.place(x=750, y=0)
menu=Button(menu_frame, text="Menu", command=menu_options, height=3, width=6)
menu.pack(side=RIGHT)




#####################################################################################################################################################################################################################

#subprogram used to determine which button was clicked, and store the animal name
def which_button(m): #when correct button clicked, used to store list of correct animals so far
    global list_correct_animals
    #adding to list of correct animals
    list_correct_animals=list_correct_animals + "\n" + m

#disables buttons after click
def disable_button(event):
    button = event.widget
    button.config(state=DISABLED)
    button.unbind("<Button-1>")



#all have to do with displaying results- common aspects of all levels

global m
global points
points=0
global list_correct_animals
list_correct_animals= ""

##########

def go_to_start():
    for widget in congrats.winfo_children():
        widget.place_forget() 
    introduction()

def EndScreeN():
    for widget in lvl6_summary.winfo_children():
        widget.place_forget() 
    global congrats
    congrats= Frame(root, width=800, height=400, bg="white")
    congrats_bg = (PIL.Image.open("D:\\yr12\\congrats_bg.jpg")).resize((800, 400))
    congrats_photo=ImageTk.PhotoImage(congrats_bg)
    congrats_label=Label(congrats, image=congrats_photo)
    congrats_label.place(x=0, y=0, relwidth=1, relheight=1)
    congrats_message= Label(master=congrats, text=("Congrats, you are now an expert on the 6 categories of animals"), width=50, height=8, bg="grey", fg="black", font=("Comic Sans MS", 14))
    ReplaY= Button(master=congrats, text=("replay"), width=10, height=5, command=go_to_start)
    congrats.place(x=0, y=0)
    ReplaY.place(x=700, y=300)
    congrats_message.place(x=100, y=50)




##########
def correct_choice6(m):
    global points
    global score6
    global animals_found6
    global list_correct_animals
    which_button(m)
    #increments points and adds correct animal to list
    if points<2:
        points=points+1
        score6.config(text="SCORE: "+ str(points))
        animals_found6.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
    else:
        points=0
        for widget in lvl6_game.winfo_children():
            widget.place_forget() 
        global lvl6_summary
        lvl6_summary= Frame(root, width=800, height=400, bg="light green")

        backyard_bg = (PIL.Image.open("D:\\yr12\\project pics\\level 6\\backyard_bg.png")).resize((800, 400))
        backyard_photo=ImageTk.PhotoImage(backyard_bg)
        backyard_label=Label(lvl6_summary, image=backyard_photo)
        backyard_label.place(x=0, y=0, relwidth=1, relheight=1)

        next_level6= Button(master=lvl6_summary, text=("finish"), width=10, height=5, bg="light green", font=("Comic Sans MS", 8), command=EndScreeN)
        summary_screen6= Label(master=lvl6_summary, text=("You've found the following invertebrates" +"\n" + " in the backyard:" +"\n" + list_correct_animals), width=50, height=10, bg="grey", font=("Comic Sans MS", 12), fg="black")
        lvl6_summary.place(x=0, y=0)
        summary_screen6.place(x=150, y=75)
        next_level6.place(x=700, y=300)
        list_correct_animals=""

def wrong_answer6(m):
    global oops6
    global try_again6
    def undo_wrong_answer6() :
        # when try again clicked, returns to level
        oops6.place_forget()
        try_again6.place_forget() 
    #message for incorrect answer
    oops6= Label(master=lvl6_game, text=("Oops, that isn't an invertebrate!" + "\n" + "Remember invertebrates don't have a " + "\n" + "spine and are really tiny!" +"\n" +"If your stuck try going to the" +"\n" +" instructions page for a hint!"),
                  font=("Comic Sans MS", 14), width=42, height=15, fg="black", bg="light green")
    try_again6= Button(master=lvl6_game, text=("Try again"), width=42, height=7, command=undo_wrong_answer6, bg="grey", fg="black", font=("Comic Sans MS", 14))
    try_again6.place(x=0, y=250)
    oops6.place(x=0, y=0)




##########
def Level6():
    global instr_lvl6
    for widget in instr_lvl6.winfo_children():
        widget.place_forget()
    global lvl6_game
    lvl6_game= Frame(root, width=800, height=400, bg="light green")
    #displaying options
    #Eastern Cottontail
    ECottontail_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\eastern-cottontail.jpg")
    ECottontail_CTK =  customtkinter.CTkImage(ECottontail_img,
                                        size=(130,110))
    ECottontail_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=ECottontail_CTK, text="Eastern Cottontail", fg_color="light green", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Eastern Cottontail":wrong_answer6 (m)) 
    ECottontail_button.bind("<Button-1>", disable_button)
    #Field Mouse
    FMouse_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\field-mouse.jpg")
    FMouse_CTK =  customtkinter.CTkImage(FMouse_img,
                                        size=(130,110))
    FMouse_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=FMouse_CTK, text="Field Mouse", fg_color="light green", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Field Mouse":wrong_answer6 (m))  
    FMouse_button.bind("<Button-1>", disable_button)
    #earthworm
    earthworm_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\earthworm.jpg")
    earthworm_CTK =  customtkinter.CTkImage(earthworm_img,
                                        size=(130,110))
    earthworm_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=earthworm_CTK, text="earthworm", fg_color="light green", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="earthworm":correct_choice6 (m))  
    earthworm_button.bind("<Button-1>", disable_button)
    #Garter Snake
    GSnake_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\garter-snake.jpg")
    GSnake_CTK =  customtkinter.CTkImage(GSnake_img,
                                        size=(130,110))
    GSnake_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=GSnake_CTK, text="Garter Snake", fg_color="light green", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Garter Snake":wrong_answer6 (m))  
    GSnake_button.bind("<Button-1>", disable_button)
    #German Shephard
    GShephard_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\german-shephard.jpg")
    GShephard_CTK =  customtkinter.CTkImage(GShephard_img,
                                        size=(130,110))
    GShephard_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=GShephard_CTK, text="German Shephard", fg_color="light green", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="German Shephard":wrong_answer6 (m)) 
    GShephard_button.bind("<Button-1>", disable_button)
    #ladybug
    ladybug_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\ladybug.jpg")
    ladybug_CTK =  customtkinter.CTkImage(ladybug_img,
                                        size=(130,110))
    ladybug_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=ladybug_CTK, text="ladybug", fg_color="light green", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="ladybug":correct_choice6 (m)) 
    ladybug_button.bind("<Button-1>", disable_button)
    #Monarch Butterfly
    MButterfly_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\monarch-butterfly.jpg")
    MButterfly_CTK =  customtkinter.CTkImage(MButterfly_img,
                                        size=(130,110))
    MButterfly_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=MButterfly_CTK, text="Monarch Butterfly", fg_color="light green", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Monarch Butterfly":correct_choice6 (m))  
    MButterfly_button.bind("<Button-1>", disable_button)
    #honeyeater
    honeyeater_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\honeyeater.jpg")
    honeyeater_CTK =  customtkinter.CTkImage(honeyeater_img,
                                        size=(130,110))
    honeyeater_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=honeyeater_CTK, text="honeyeater", fg_color="light green", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="honeyeater":wrong_answer6 (m))  
    honeyeater_button.bind("<Button-1>", disable_button)
    #Water Skink
    WSkink_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\water-skink.jpg")
    WSkink_CTK =  customtkinter.CTkImage(WSkink_img,
                                        size=(130,110))
    WSkink_button =  customtkinter.CTkButton( text_color="black", master=lvl6_game, image=WSkink_CTK, text="Water Skink", fg_color="light green", font=("Comic Sans MS", 12), compound="bottom",
                                        command= (lambda m="Water Skink":wrong_answer6 (m)))
    WSkink_button.bind("<Button-1>", disable_button)
    #results
    global score6
    global animals_found6
    score6 = Label(lvl6_game, text="SCORE: ", font=(("Times New Roman"), 18), fg="black", bg="light green")
    animals_found6 = Label(lvl6_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18), fg="black", bg="light green")
    lvl6_game.place(x=0, y=0)
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
    animals_found6.place(x=500, y=50)
    #back option
    def back6_func():
        for widget in lvl6_game.winfo_children():
            if widget != animals_found6 or score6:
                widget.place_forget() 
        transition5()
    back6= Button(master=lvl6_game, text=("back"), width=10, height=5, bg="light green", font=("Comic Sans MS", 8), command=back6_func)
    back6.place(x=700, y=300)


##########

def transition5():
    for widget in lvl4_summary.winfo_children():
         widget.place_forget()
    global instr_lvl6
    instr_lvl6= Frame(root, width=800, height=400, bg="light green")
    #display instructions for 6th level
    backyard = Label(instr_lvl6, text="Next we are going to look for " + "\n"+ "invertebrates in my backyard" +"\n" + "Invertebrates don't have a spine and are often quite small," + "\n" + " like the invertebrates shown here!" + "\n" +"Some examples of invertebrates you may know" + "\n" + " include slugs, insects and crabs!",
                      font=("Comic Sans MS", 12), bg="light green", width=40)
    #continue button to start 6th level
    cont6 =  Button(instr_lvl6, text="Continue", bg="light green", font=("Comic Sans MS", 8), command=Level6)
    #collage of invertebrates
    invertebrates_collage_image = PIL.Image.open("D:\\yr12\\project pics\\level 6\\invertebrates.jpg")
    TK_invertebrates_collage =   customtkinter.CTkImage(invertebrates_collage_image,
        size=(400,400))
    invertebrates_collage =   customtkinter.CTkLabel(master=instr_lvl6, image=TK_invertebrates_collage)
    instr_lvl6.place(x=0, y=0)
    invertebrates_collage.place(x=0, y=0)
    cont6.place(x=700, y=300)
    backyard.place(x=400, y=100)




#########
def correct_choice5(m):
    global points
    global score5
    global animals_found5
    global list_correct_animals
    which_button(m)
    #increments points and adds correct animal to list
    if points<2:
        points=points+1
        score5.config(text="SCORE: "+ str(points))
        animals_found5.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
    else:
        points=0
        for widget in lvl5_game.winfo_children():
            widget.place_forget() 
        global lvl5_summary
        lvl5_summary= Frame(root, width=800, height=400, bg="#cca47c")

        outback_bg = (PIL.Image.open("D:\\yr12\\project pics\\level 5\\outback_bg.png")).resize((800, 400))
        global outback_photo
        outback_photo=ImageTk.PhotoImage(outback_bg)
        outback_label=Label(lvl5_summary, image=outback_photo)
        outback_label.place(x=0, y=0, relwidth=1, relheight=1)

        next_level5= Button(master=lvl5_summary, text=("next level"), width=10, height=5, bg="#cca47c", font=("Comic Sans MS", 8), command=transition5)
        summary_screen5= Label(master=lvl5_summary, text=("You've found the following reptiles" +"\n" + " in the Australian Outback:" +"\n" + list_correct_animals), width=50, height=10, bg="grey", font=("Comic Sans MS", 12))
        lvl5_summary.place(x=0, y=0)
        summary_screen5.place(x=150, y=75)
        next_level5.place(x=700, y=300)
        list_correct_animals=""

def wrong_answer5(m):
    global oops5
    global try_again5
    def undo_wrong_answer5() :
        # when try again clicked, returns to level
        oops5.place_forget()
        try_again5.place_forget() 
    #message for incorrect answer
    oops5= Label(master=lvl5_game, text=("Oops, that isn't a reptile!" + "\n" + "Remember reptiles have scaly skin!"+"\n" +"If your stuck try going to the" +"\n" +" instructions page for a hint!"),
                  font=("Comic Sans MS", 14), width=42, height=15, fg="black", bg="#cca47c")
    try_again5= Button(master=lvl5_game, text=("Try again"), width=42, height=7, command=undo_wrong_answer5, bg="grey", fg="black", font=("Comic Sans MS", 14))
    try_again5.place(x=0, y=250)
    oops5.place(x=0, y=0)



##########
def Level5():
    global instr_lvl5
    for widget in instr_lvl5.winfo_children():
        widget.place_forget()
    ###
    global lvl5_game
    lvl5_game= Frame(root, width=800,  height=400, bg="#cca47c")
    #displaying options
    #Sand Goanna
    SGoanna_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\reptiles\\sand-goanna.jpg")
    SGoanna_CTK =  customtkinter.CTkImage(SGoanna_img,
                                        size=(130,110))
    SGoanna_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=SGoanna_CTK, text="Sand Goanna", fg_color="#cca47c", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Sand Goanna":correct_choice5 (m))   
    SGoanna_button.bind("<Button-1>", disable_button)
    #Throny Devil
    TDevil_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\reptiles\\throny-devil.jpg")
    TDevil_CTK =  customtkinter.CTkImage(TDevil_img,
                                        size=(130,110))
    TDevil_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=TDevil_CTK, text="Throny Devil", fg_color="#cca47c", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Throny Devil":correct_choice5 (m))  
    TDevil_button.bind("<Button-1>", disable_button)
    #dingo
    dingo_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\dingo.jpg")
    dingo_CTK =  customtkinter.CTkImage(dingo_img,
                                        size=(130,110))
    dingo_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=dingo_CTK, text="dingo", fg_color="#cca47c", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="dingo":wrong_answer5 (m)) 
    dingo_button.bind("<Button-1>", disable_button)
    #Australian Feral Camel
    AFCamel_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\australian-feral-camel.jpg")
    AFCamel_CTK =  customtkinter.CTkImage(AFCamel_img,
                                        size=(130,110))
    AFCamel_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=AFCamel_CTK, text="Australian Feral Camel", fg_color="#cca47c", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Australian Feral Camel":wrong_answer5 (m))  
    AFCamel_button.bind("<Button-1>", disable_button)
    #Frill Neck Lizard
    FNLizard_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\reptiles\\frill-neck-lizard.jpg")
    FNLizard_CTK =  customtkinter.CTkImage(FNLizard_img,
                                        size=(130,110))
    FNLizard_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=FNLizard_CTK, text="Frill Neck Lizard", fg_color="#cca47c", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Frill Neck Lizard":correct_choice5 (m)) 
    FNLizard_button.bind("<Button-1>", disable_button)
    #Stimson's Python
    SPython_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\stimson's-python.jpg")
    SPython_CTK =  customtkinter.CTkImage(SPython_img,
                                        size=(130,110))
    SPython_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=SPython_CTK, text="Stimson's Python", fg_color="#cca47c", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Stimson's Python":wrong_answer5 (m)) 
    SPython_button.bind("<Button-1>", disable_button)
    #Quokka
    quokka_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\quokka.jpg")
    quokka_CTK =  customtkinter.CTkImage(quokka_img,
                                        size=(130,110))
    quokka_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=quokka_CTK, text="Quokka", fg_color="#cca47c", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Quokka":wrong_answer5 (m))
    quokka_button.bind("<Button-1>", disable_button)
    #kangaroo
    kangaroo_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\kangaroo.jpg")
    kangaroo_CTK =  customtkinter.CTkImage(kangaroo_img,
                                        size=(130,110))
    kangaroo_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=kangaroo_CTK, text="kangaroo", fg_color="#cca47c", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="kangaroo":wrong_answer5 (m))  
    kangaroo_button.bind("<Button-1>", disable_button)

    #Kookaburra
    kookaburra_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\kookaburra.jpg")
    kookaburra_CTK =  customtkinter.CTkImage(kookaburra_img,
                                        size=(130,110))
    kookaburra_button =  customtkinter.CTkButton( text_color="black", master=lvl5_game, image=kookaburra_CTK, text="Kookaburra", fg_color="#cca47c", font=("Comic Sans MS", 12), compound="bottom",
                                        command= (lambda m="Kookaburra":wrong_answer5 (m)))
    kookaburra_button.bind("<Button-1>", disable_button)
    #results
    global score5
    global animals_found5
    score5 = Label(lvl5_game, text="SCORE: ", font=(("Times New Roman"), 18), bg="#cca47c")
    animals_found5 = Label(lvl5_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18), bg="#cca47c")

    #back option
    def back5_func():
        for widget in lvl5_game.winfo_children():
            if widget != animals_found5 or score5:
                widget.place_forget() 
        transition4()
    back5= Button(master=lvl5_game, text=("back"), width=10, height=5, bg="#cca47c", font=("Comic Sans MS", 8), command=back5_func)


    lvl5_game.place(x=0, y=0)
    back5.place(x=700, y=300)
    score5.place(x=550, y=0)
    animals_found5.place(x=500, y=50)
    kookaburra_button.place(x=280, y=260)
    kangaroo_button.place(x=140, y=260)
    quokka_button.place(x=0, y=260)
    SPython_button.place(x=0, y=135)
    FNLizard_button.place(x=140, y=135)
    AFCamel_button.place(x=280, y=135)
    dingo_button.place(x=280, y=0)
    TDevil_button.place(x=140, y=0)
    SGoanna_button.place(x=0, y=0)


##########
def transition4():
    for widget in lvl4_summary.winfo_children():
         widget.place_forget()
    global instr_lvl5
    instr_lvl5= Frame(root, width=800, height=400, bg="#cca47c")
    #display instructions for 5th level
    outback = Label(instr_lvl5, text="Next we are going to look for " + "\n"+ "reptiles in the outback!" +"\n" + "Reptiles have scaly skin and lay eggs," + "\n" + " like the reptiles shown here!" + "\n" +"Some examples of reptiles you may know" + "\n" + " include lizards, snakes and crocodiles!",
                     font=("Comic Sans MS", 12), bg="#cca47c", width=40)
    #continue button to start 5th level
    cont5 =  Button(instr_lvl5, text="Continue", bg="#cca47c", command=Level5, font=("Comic Sans MS", 8))
    #collage of reptiles
    reptiles_collage_image = PIL.Image.open("D:\\yr12\\project pics\\level 5\\Reptiles.jpg")
    TK_reptiles_collage =   customtkinter.CTkImage(reptiles_collage_image,
        size=(400,400))
    reptiles_collage =   customtkinter.CTkLabel(master=instr_lvl5, image=TK_reptiles_collage)
    instr_lvl5.place(x=0, y=0)
    reptiles_collage.place(x=0, y=0)
    cont5.place(x=700, y=300)
    outback.place(x=400, y=100)




##########
def correct_choice4(m):
    global points
    global list_correct_animals
    #increments points and adds correct animal to list
    which_button(m)
    if points<2:
        points=points+1
        score4.config(text="SCORE: "+ str(points))
        animals_found4.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
    else:
        points=0
        for widget in lvl4_game.winfo_children():
            widget.place_forget() 
        ###
        global lvl4_summary
        lvl4_summary= Frame(root, width=800, height=400, bg="#877c94")

        BRF_bg = (PIL.Image.open("D:\\yr12\\project pics\\level 4\\BRF_bg.png")).resize((800, 400))
        global BRF_photo
        BRF_photo=ImageTk.PhotoImage(BRF_bg)
        BRF_label=Label(lvl4_summary, image=BRF_photo)
        BRF_label.place(x=0, y=0, relwidth=1, relheight=1)

        next_level4= Button(master=lvl4_summary, text=("next level"), width=10, height=5, bg="#877c94", font=("Comic Sans MS", 8), command=transition4)
        summary_screen4= Label(master=lvl4_summary, text=("You've found the following amphibians" +"\n" + " in the Borneo Rainforest:" +"\n" + list_correct_animals), width=50, height=10, font=("Comic Sans MS", 12), bg="grey")
        lvl4_summary.place(x=0, y=0)
        summary_screen4.place(x=150, y=75)
        next_level4.place(x=700, y=300)
        list_correct_animals=""

def wrong_answer4(m):
    global oops4
    global try_again4
    def undo_wrong_answer4() :
        # when try again clicked, returns to level
        oops4.place_forget()
        try_again4.place_forget() 
    #message for incorrect answer
    oops4= Label(master=lvl4_game, text=("Oops, that isn't an amphibian!" + "\n" + "Remember amphibians have slimy skin and live around water!"+"\n" +"If your stuck try going to the" +"\n" +" instructions page for a hint!"),
                  font=("Comic Sans MS", 14), width=42, height=15, fg="black", bg="#877c94")
    try_again4= Button(master=lvl4_game, text=("Try again"), width=42, height=7, command=undo_wrong_answer4, bg="grey", fg="black", font=("Comic Sans MS", 14) )
    try_again4.place(x=0, y=250)
    oops4.place(x=0, y=0)


##########
def Level4():
    global instr_lvl4
    for widget in instr_lvl4.winfo_children():
        widget.place_forget()
    
    ###
    global lvl4_game
    lvl4_game= Frame(root, width=800,  height=400, bg="#877c94")
    #displaying options
    #Clouded Leopard
    CLeopard_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\clouded-leopard.jpg")
    CLeopard_CTK =  customtkinter.CTkImage(CLeopard_img,
                                        size=(130,110))
    CLeopard_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=CLeopard_CTK, text="Clouded Leopard", fg_color="#877c94", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Clouded Leopard":wrong_answer4 (m))  
    CLeopard_button.bind("<Button-1>", disable_button)
    #red giant flying squirrel
    RGFSquirrel_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\red-giant-flying-squirrel.jpg")
    RGFSquirrel_CTK =  customtkinter.CTkImage(RGFSquirrel_img,
                                        size=(130,110))
    RGFSquirrel_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=RGFSquirrel_CTK, text="red giant flying squirrel", fg_color="#877c94", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="red giant flying squirrel":wrong_answer4 (m)) 
    RGFSquirrel_button.bind("<Button-1>", disable_button)
    #Malay Civet
    MCivet_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Malay-civet.jpg")
    MCivet_CTK =  customtkinter.CTkImage(MCivet_img,
                                        size=(130,110))
    MCivet_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=MCivet_CTK, text="Malay Civet", fg_color="#877c94", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Malay Civet":wrong_answer4 (m)) 
    MCivet_button.bind("<Button-1>", disable_button)
    #Proboscis monkey
    PMonkey_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Proboscis-monkey.jpg")
    PMonkey_CTK =  customtkinter.CTkImage(PMonkey_img,
                                        size=(130,110))
    PMonkey_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=PMonkey_CTK, text="Proboscis monkey", fg_color="#877c94", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Proboscis monkey":wrong_answer4 (m))  
    PMonkey_button.bind("<Button-1>", disable_button)
    #Wallaces flying frog
    WFFrog_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\amphibians\\Wallaces-flying-frog.jpg")
    WFFrog_CTK =  customtkinter.CTkImage(WFFrog_img,
                                        size=(130,110))
    WFFrog_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=WFFrog_CTK, text="Wallaces Flying Frog", fg_color="#877c94", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Wallaces Flying Frog":correct_choice4 (m)) 
    WFFrog_button.bind("<Button-1>", disable_button)
    #orangutan
    orangutan_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Orangutan.jpg")
    orangutan_CTK =  customtkinter.CTkImage(orangutan_img,
                                        size=(130,110))
    orangutan_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=orangutan_CTK, text="orangutan", fg_color="#877c94", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="orangutan":wrong_answer4 (m))  
    orangutan_button.bind("<Button-1>", disable_button)

    #jade tree frog
    JTFrog_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\amphibians\\jade-tree-frog.jpg")
    JTFrog_CTK =  customtkinter.CTkImage(JTFrog_img,
                                        size=(130,110))
    JTFrog_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=JTFrog_CTK, text="jade tree frog", fg_color="#877c94", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="jade tree frog":correct_choice4 (m))   
    JTFrog_button.bind("<Button-1>", disable_button)

    #Pygmy elephant
    PElephant_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Pygmy-Elephant.jpg")
    PElephant_CTK =  customtkinter.CTkImage(PElephant_img,
                                        size=(130,110))
    PElephant_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=PElephant_CTK, text="Pygmy Elephant", fg_color="#877c94", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Pygmy Elephant":wrong_answer4 (m))   
    PElephant_button.bind("<Button-1>", disable_button)

    #BFHFrog
    BFHFrog_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\amphibians\\bornean-flat-headed-frog.jpg")
    BFHFrog_CTK =  customtkinter.CTkImage(BFHFrog_img,
                                        size=(130,110))
    BFHFrog_button =  customtkinter.CTkButton( text_color="black", master=lvl4_game, image=BFHFrog_CTK, text="bornean flat headed frog", fg_color="#877c94", font=("Comic Sans MS", 12), compound="bottom",
                                        command= (lambda m="bornean flat headed frog":correct_choice4 (m)))
    BFHFrog_button.bind("<Button-1>", disable_button)

    #results
    global score4
    global animals_found4
    score4 = Label(lvl4_game, text="SCORE: ", font=(("Times New Roman"), 18), bg="#877c94")
    animals_found4 = Label(lvl4_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18), bg="#877c94", fg="black")

    # #back option
    def back4_func():
        for widget in lvl4_game.winfo_children():
            if widget != animals_found4 or score4:
                widget.place_forget() 
        transition3()
    back4= Button(master=lvl4_game, text=("back"), width=10, height=5, bg="#877c94", font=("Comic Sans MS", 8), command=back4_func)

    lvl4_game.place(x=0, y=0)
    back4.place(x=700, y=300)
    score4.place(x=550, y=0)
    animals_found4.place(x=500, y=50)
    BFHFrog_button.place(x=280, y=260)
    PElephant_button.place(x=140, y=260)
    JTFrog_button.place(x=0, y=260)
    orangutan_button.place(x=0, y=135)
    WFFrog_button.place(x=140, y=135)
    PMonkey_button.place(x=280, y=135)
    MCivet_button.place(x=280, y=0)
    RGFSquirrel_button.place(x=140, y=0)
    CLeopard_button.place(x=0, y=0)



##########
def transition3():
    for widget in lvl3_summary.winfo_children():
         widget.place_forget()
    global instr_lvl4
    instr_lvl4= Frame(root, width=800,  height=400, bg="#877c94")
    #display instructions for 4th level
    BRF = Label(instr_lvl4, text="Next we are going to look for " + "\n"+ "amphibians in the Borneo Rainforest!" +"\n" + "Amphibians have slimy skin and live around water," + "\n" + " like the amphibians shown here!" + "\n" +"Some examples of amphibians you may know" + "\n" + " include frogs, newts and salamanders!",
                 font=("Comic Sans MS", 12), bg="#877c94", width=40)
    #continue button to start 4th level
    cont4 =  Button(instr_lvl4, text="Continue", command=Level4, bg="#877c94", font=("Comic Sans MS", 8))
    #collage of amphibians
    amphibians_collage_image = PIL.Image.open("D:\\yr12\\project pics\\level 4\\amphibians.jpg")
    TK_amphibians_collage =  customtkinter.CTkImage(amphibians_collage_image,
        size=(400,400))
    amphibians_collage =  customtkinter.CTkLabel(master=instr_lvl4, image=TK_amphibians_collage)
    instr_lvl4.place(x=0, y=0)
    amphibians_collage.place(x=0, y=0)
    cont4.place(x=700, y=300)
    BRF.place(x=400, y=100)



##########

def correct_choice3(m):
    global points
    global score3
    global animals_found3
    global list_correct_animals
    #increments points and adds correct animal to list
    which_button(m)
    if points<2:
        points=points+1
        score3.config(text="SCORE: "+ str(points))
        animals_found3.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
    else:
        points=0
        for widget in lvl3_game.winfo_children():
            widget.place_forget() 
        
        global lvl3_summary
        lvl3_summary= Frame(root, width=800,  height=400, bg="light blue")

        GBR_bg = (PIL.Image.open("D:\\yr12\\project pics\\level 3\\GBR_bg.png")).resize((800, 400))
        global GBR_photo
        GBR_photo=ImageTk.PhotoImage(GBR_bg)
        GBR_label=Label(lvl3_summary, image=GBR_photo)
        GBR_label.place(x=0, y=0, relwidth=1, relheight=1)

        summary_screen3= Label(master=lvl3_summary, text=("You've found the following fish" +"\n" + " in the Great Barrier Reef:" +"\n" + list_correct_animals), width=50, height=10, bg="grey", font=("Comic Sans MS", 12), fg="black")
        next_level3= Button(master=lvl3_summary, text=("next level"), width=10, height=5, bg="light blue", font=("Comic Sans MS", 8), command=transition3)
        lvl3_summary.place(x=0, y=0)
        summary_screen3.place(x=150, y=75)
        next_level3.place(x=700, y=300)
        list_correct_animals=""

def wrong_answer3(m):
    global oops3
    global try_again3
    def undo_wrong_answer3() :
        # when try again clicked, returns to level
        oops3.place_forget()
        try_again3.place_forget() 
    #message for incorrect answer
    oops3= Label(master=lvl3_game, text="Oops, that isn't a fish!" + "\n" + "Remember fish have scales and live underwater!"+"\n" +"If your stuck try going to the" +"\n" +" instructions page for a hint!",
                  font=("Comic Sans MS", 14), width=42, height=15, fg="black", bg="light blue")
    try_again3= Button(master=lvl3_game, text=("Try again"), width=42, height=7, command=undo_wrong_answer3, bg="grey", fg="black", font=("Comic Sans MS", 14))
    try_again3.place(x=0, y=250)  
    oops3.place(x=0, y=0)

########
def Level3():
    global instr_lvl3
    for widget in instr_lvl3.winfo_children():
        widget.place_forget()
    ###
    global lvl3_game
    lvl3_game= Frame(root, width=800,  height=400, bg="light blue")
    #displaying options
    #clownfish
    Cfish_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\fish\\clownfish.jpg")
    Cfish_CTK =  customtkinter.CTkImage(Cfish_img,
                                        size=(130,110))
    Cfish_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=Cfish_CTK, text="clownfish", fg_color="light blue", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="clownfish":correct_choice3 (m)) 
    Cfish_button.bind("<Button-1>", disable_button)
    #blanket octapus
    Boctapus_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\blanket-octopus.jpg")
    Boctapus_CTK =  customtkinter.CTkImage(Boctapus_img,
                                        size=(130,110))
    Boctapus_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=Boctapus_CTK, text="blanket octapus", fg_color="light blue", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="blanket octapus":wrong_answer3 (m))  
    Boctapus_button.bind("<Button-1>", disable_button)
    #dugong
    dugong_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\dugong.jpg")
    dugong_CTK =  customtkinter.CTkImage(dugong_img,
                                        size=(130,110))
    dugong_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=dugong_CTK, text="dugong", fg_color="light blue", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="dugong":wrong_answer3 (m)) 
    dugong_button.bind("<Button-1>", disable_button)
    #green turtle
    Gturtle_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\green-turtle.jpg")
    Gturtle_CTK =  customtkinter.CTkImage(Gturtle_img,
                                        size=(130,110))
    Gturtle_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=Gturtle_CTK, text="green turtle", fg_color="light blue", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="green turtle":wrong_answer3 (m)) 
    Gturtle_button.bind("<Button-1>", disable_button)
    #manta ray
    Mray_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\fish\\manta-ray.jpg")
    Mray_CTK =  customtkinter.CTkImage(Mray_img,
                                        size=(130,110))
    Mray_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=Mray_CTK, text="manta ray", fg_color="light blue", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="manta ray":correct_choice3 (m))  
    Mray_button.bind("<Button-1>", disable_button)
    #giant clam
    Wshark_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\fish\\whale-shark.jpg")
    Wshark_CTK =  customtkinter.CTkImage(Wshark_img,
                                        size=(130,110))
    Wshark_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=Wshark_CTK, text="whale shark", fg_color="light blue", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="whale shark":correct_choice3 (m)) 
    Wshark_button.bind("<Button-1>", disable_button)
    #humpback whale
    HWhale_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\humpback-whale.jpg")
    HWhale_CTK =  customtkinter.CTkImage(HWhale_img,
                                        size=(130,110))
    HWhale_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=HWhale_CTK, text="Humpback Whale", fg_color="light blue", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Humpback Whale":wrong_answer3 (m))  
    HWhale_button.bind("<Button-1>", disable_button)
    #jellyfish
    jellyfish_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\jellyfish.jpg")
    jellyfish_CTK =  customtkinter.CTkImage(jellyfish_img,
                                        size=(130,110))
    jellyfish_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=jellyfish_CTK, text="jellyfish", fg_color="light blue", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="jellyfish":wrong_answer3 (m))   
    jellyfish_button.bind("<Button-1>", disable_button)
    #mantis shrimp
    MShrimp_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\mantis-shrimp.jpg")
    MShrimp_CTK =  customtkinter.CTkImage(MShrimp_img,
                                        size=(130,110))
    MShrimp_button =  customtkinter.CTkButton( text_color="black", master=lvl3_game, image=MShrimp_CTK, text="mantis shrimp", fg_color="light blue", font=("Comic Sans MS", 12), compound="bottom",
                                        command= (lambda m="mantis shrimp":wrong_answer3 (m)))   
    MShrimp_button.bind("<Button-1>", disable_button)
    #results
    global score3
    global animals_found3
    score3 = Label(lvl3_game, text="SCORE: ", font=(("Times New Roman"), 18), background="light blue")
    animals_found3 = Label(lvl3_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18), background="light blue", fg="black")

    #back option
    def back3_func():
        for widget in lvl3_game.winfo_children():
            if widget != animals_found3 or score3:
                widget.place_forget() 
        transition2()
    
    back3=  Button(master=lvl3_game, text=("back"), width=10, height=5, bg="light blue", font=("Comic Sans MS", 8), command=back3_func)
    lvl3_game.place(x=0, y=0)
    score3.place(x=550, y=0)
    animals_found3.place(x=500, y=50)
    MShrimp_button.place(x=280, y=260)
    jellyfish_button.place(x=140, y=260)
    HWhale_button.place(x=0, y=260)
    Wshark_button.place(x=0, y=135)
    Mray_button.place(x=140, y=135)
    Gturtle_button.place(x=280, y=135)
    dugong_button.place(x=280, y=0)
    Boctapus_button.place(x=140, y=0)
    Cfish_button.place(x=0, y=0)
    back3.place(x=700, y=300)



#########
def transition2():
    for widget in lvl2_summary.winfo_children():
         widget.place_forget()
    global instr_lvl3
    instr_lvl3= Frame(root, width=800,  height=400, bg="light blue")
    #display instructions for 3rd level
    #great barrier reef
    GBR = Label(instr_lvl3, text="Next we are going to look for " + "\n"+ "fish in the Great Barrier Reef" +"\n" + "Fish have scales and live underwater," + "\n" + " like the fish shown here!" + "\n" +"Some examples of fish you may know" + "\n" + " include salmon, trout and string rays!",
                 font=("Comic Sans MS", 12), bg="light blue", width=40)
    #continue button to start 3rd level
    global cont3
    cont3 =  Button(instr_lvl3, text="Continue", bg="light blue", font=("Comic Sans MS", 8), command=Level3)
    #collage of fish
    fish_collage_image = PIL.Image.open(r"D:\yr12\project pics\level 3\fish-montage.jpg")
    TK_fish_collage =   customtkinter.CTkImage(fish_collage_image,
        size=(400,400))
    fish_collage =  customtkinter.CTkLabel(master=instr_lvl3, image=TK_fish_collage)
    instr_lvl3.place(x=0, y=0)
    fish_collage.place(x=0, y=0)
    cont3.place(x=700, y=300)
    GBR.place(x=400, y=100)



##########

def correct_choice2(m):
    global points
    global score2
    global animals_found2
    global list_correct_animals
    #increments points and adds correct animal to list
    which_button(m)
    if points<2:
        points=points+1
        score2.config(text="SCORE: "+ str(points))
        animals_found2.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
    else:
        points=0
        for widget in lvl2_game.winfo_children():
            widget.place_forget() 
        ###
        global lvl2_summary
        lvl2_summary= Frame(root, width=800,  height=400, bg="#ebd483")

        savanna_bg = PIL.Image.open("D:\\yr12\\project pics\\level 2\\savanna_bg.png").resize((800, 400))
        global savanna_photo
        savanna_photo=ImageTk.PhotoImage(savanna_bg)
        savanna_label=Label(lvl2_summary, image=savanna_photo)

        summary_screen2= Label(master=lvl2_summary, text="You've found the following mammals" + "\n" + " in the African Savanna:" +"\n" + list_correct_animals, fg="black", font=("Comic Sans MS", 12), width=50, height=10, bg="grey")
        next_level2=Button(master=lvl2_summary, text=("next level"), width=10, height=5, bg="#ebd483", font=("Comic Sans MS", 8), command=transition2)
        lvl2_summary.place(x=0, y=0)
        savanna_label.place(x=0, y=0, relwidth=1, relheight=1)
        summary_screen2.place(x=150, y=75)
        next_level2.place(x=700, y=300)
        list_correct_animals=""


def wrong_answer2(m):
    global oops2
    global try_again2
    def undo_wrong_answer2() :
        # when try again clicked, returns to level
        oops2.place_forget()
        try_again2.place_forget()
    #message for incorrect answer
    oops2= Label(master=lvl2_game, text="Oops, that isn't a mammal!" + "\n" + "Remember mammals have hair or fur!"+"\n" +"If your stuck try going to the" +"\n" +" instructions page for a hint!",
                  font=("Comic Sans MS", 14), width=42, height=15, fg="black", bg="#ebd483")
    try_again2= Button(master=lvl2_game, text=("Try again"), width=42, height=7, command=undo_wrong_answer2, bg="grey", fg="black", font=("Comic Sans MS", 14))
    try_again2.place(x=0, y=250) 
    oops2.place(x=0, y=0)
 


##########

def Level2():
    for widget in instr_lvl2.winfo_children():
         widget.place_forget()
    
    ###
    global lvl2_game
    lvl2_game= Frame(root, width=800,  height=400, bg="#ebd483")
    #displaying options
    #cobra
    Cobra_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\cobra.jpg")
    cobra_CTK =  customtkinter.CTkImage(Cobra_img,
                                    size=(130,110))
    cobra_button =  customtkinter.CTkButton( master=lvl2_game, image=cobra_CTK, text="cobra", fg_color="#ebd483", font=("Comic Sans MS", 12), text_color="black", compound="bottom",
                                        command=lambda m="cobra":wrong_answer2 (m))   
    cobra_button.bind("<Button-1>", disable_button)
    #aardvark
    aardvark_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\mammals\\aardvark.jpg")
    aardvark_CTK =  customtkinter.CTkImage(aardvark_img,
                                    size=(130,110))
    aardvark_button =  customtkinter.CTkButton(master=lvl2_game, image=aardvark_CTK, text="aardvark", fg_color="#ebd483", font=("Comic Sans MS", 12), text_color="black", compound="bottom",
                                        command=lambda m="aardvark":correct_choice2 (m))   
    aardvark_button.bind("<Button-1>", disable_button)
    #african_elephant
    african_elephant_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\mammals\\african_elephant.jpg")
    african_elephant_CTK =  customtkinter.CTkImage(african_elephant_img,
                                    size=(130,110))
    african_elephant_button =  customtkinter.CTkButton( master=lvl2_game, image=african_elephant_CTK, text="african elephant", fg_color="#ebd483", font=("Comic Sans MS", 12), text_color="black", compound="bottom",
                                        command=lambda m="african elephant":correct_choice2 (m))   
    african_elephant_button.bind("<Button-1>", disable_button)
    #hornbill
    hornbill_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\hornbill.jpg")
    hornbill_CTK =  customtkinter.CTkImage(hornbill_img,
                                    size=(130,110))
    hornbill_button =  customtkinter.CTkButton( master=lvl2_game, image=hornbill_CTK, text="hornbill", fg_color="#ebd483", font=("Comic Sans MS", 12), text_color="black", compound="bottom",
                                        command=lambda m="hornbill":wrong_answer2 (m))   
    hornbill_button.bind("<Button-1>", disable_button)
    #scorpion
    scorpion_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\scorpion.jpg")
    scorpion_CTK =  customtkinter.CTkImage(scorpion_img,
                                    size=(130,110))
    scorpion_button =  customtkinter.CTkButton( master=lvl2_game, image=scorpion_CTK, text="scorpion", fg_color="#ebd483", font=("Comic Sans MS", 12), text_color="black", compound="bottom",
                                        command=lambda m="scorpion":wrong_answer2 (m))   
    scorpion_button.bind("<Button-1>", disable_button)
    #rhinoceros
    rhinoceros_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\mammals\\rhinoceros.jpg")
    rhinoceros_CTK =  customtkinter.CTkImage(rhinoceros_img,
                                    size=(130,110))
    rhinoceros_button =  customtkinter.CTkButton( master=lvl2_game, image=rhinoceros_CTK, text="rhinoneros", fg_color="#ebd483", font=("Comic Sans MS", 12), text_color="black", compound="bottom",
                                        command=lambda m="rhinoceros":correct_choice2 (m))   
    rhinoceros_button.bind("<Button-1>", disable_button)
    #ostrich
    ostrich_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\ostrich.jpg")
    ostrich_CTK =  customtkinter.CTkImage(ostrich_img,
                                    size=(130,110))
    ostrich_button =  customtkinter.CTkButton( master=lvl2_game, image=ostrich_CTK, text="ostrich", fg_color="#ebd483", font=("Comic Sans MS", 12), text_color="black", compound="bottom",
                                        command=lambda m="ostrich":wrong_answer2 (m))   
    ostrich_button.bind("<Button-1>", disable_button)
    #dung beetle
    dung_beetle_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\dung-beetle.jpg")
    dung_beetle_CTK =  customtkinter.CTkImage(dung_beetle_img,
                                    size=(130,110))
    dung_beetle_button =  customtkinter.CTkButton( master=lvl2_game, image=dung_beetle_CTK, text="dung beetle", fg_color="#ebd483", font=("Comic Sans MS", 12), text_color="black", compound="bottom",
                                        command=lambda m="dung beetle":wrong_answer2 (m))   
    dung_beetle_button.bind("<Button-1>", disable_button)

    #african spurred tortoise
    ASTortoise_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\african-spurred-tortoise.jpg")
    ASTortoise_CTK =  customtkinter.CTkImage(ASTortoise_img,
                                    size=(130,110))
    ASTortoise_button =  customtkinter.CTkButton(master=lvl2_game, image=ASTortoise_CTK, text="african spurred tortoise", fg_color="#ebd483", font=("Comic Sans MS", 12), text_color="black", compound="bottom",
                                        command= (lambda m="african spurred tortoise":wrong_answer2 (m)))   
    ASTortoise_button.bind("<Button-1>", disable_button)
    #results
    global score2
    global animals_found2
    score2 = Label(lvl2_game, text="SCORE: ", font=(("Times New Roman"), 18), bg="#ebd483")
    animals_found2 = Label(lvl2_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18), bg="#ebd483")

    #back option
    def back2_func():
        for widget in lvl2_game.winfo_children():
            if widget != animals_found2 or score2:
                widget.place_forget() 
        transition1()

    back2=  Button(master=lvl2_game, text=("back"), bg="#ebd483", width=10, height=5, font=("Comic Sans MS", 8), command=back2_func)

    lvl2_game.place(x=0, y=0)
    back2.place(x=700, y=300)
    score2.place(x=550, y=0)
    animals_found2.place(x=500, y=50)
    ASTortoise_button.place(x=280, y=260)
    dung_beetle_button.place(x=140, y=260)
    ostrich_button.place(x=0, y=260)
    rhinoceros_button.place(x=0, y=135)
    scorpion_button.place(x=140, y=135)
    hornbill_button.place(x=280, y=135)
    african_elephant_button.place(x=280, y=0)
    aardvark_button.place(x=140, y=0)
    cobra_button.place(x=0, y=0)



##########


def transition1():
    for widget in lvl1_summary.winfo_children():
         widget.place_forget()
    global instr_lvl2
    instr_lvl2= Frame(root, width=800,  height=400, bg="#ebd483" )
    #display instructions for second level
    Savanna = Label(instr_lvl2, text="Next we are going to look for " + "\n"+ "mammals in the African Savanna" +"\n" + "Mammals have skin covered with hair or fur " + "\n"+ "and have very complex brains," + "\n" + " like the mammals shown here!" + "\n" +"Some examples of mammals you may know" + "\n" + " include dogs, horses and humans!", 
                    font=("Comic Sans MS", 12), bg="#ebd483", width=40)
    #continue button to start 2nd level
    cont2 =  Button(instr_lvl2, text="Continue", bg="#ebd483", font=("Comic Sans MS", 8), command=Level2)
    #collage of mammals- to refer to how mammals look
    mammals_collage_image = PIL.Image.open(r"D:\yr12\project pics\level 2\Mammal_intro.jpg")
    TK_mammals_collage =  customtkinter.CTkImage(mammals_collage_image,
        size=(400,400))
    mammals_collage =  customtkinter.CTkLabel(master=instr_lvl2, image=TK_mammals_collage)
    instr_lvl2.place(x=0, y=0)
    mammals_collage.place(x=0, y=0)
    cont2.place(x=700, y=300)
    Savanna.place(x=400, y=100)


##########


##
#defining what happens when correct/incorrect buttons are pressed for LEVEL 1


def wrong_answer(m): #when wrong button clicked, ONLY FOR 1ST LEVEL
    
    def undo_wrong_answer() :
        # when try again clicked, returns to level
        oops.place_forget()
        try_again.place_forget()
        
    global oops
    global try_again
    #message for incorrect answer
    oops= Label(master=lvl1_game, text="Oops, that isn't a bird!" + "\n" + "Remember birds have feathers and beaks!"+"\n" +"If your stuck try going to the" +"\n" +" instructions page for a hint!",
                 font=("Comic Sans MS", 14), width=42, height=15, fg="black", bg="#4c5751")
    try_again= Button(master=lvl1_game, text=("Try again"), width=42, height=7, command=undo_wrong_answer, bg="grey", fg="black", font=("Comic Sans MS", 14))
    try_again.place(x=0, y=250)
    oops.place(x=0, y=0)


    

def correct_choice(m): #refects correct choice on screen; increment score and adds to list of animals found--ONLY FOR 1ST LEVEL
    #increments points and adds correct animal to list
    which_button(m)
    global points
    global list_correct_animals
    if points<2: #score of 3 not reached
        points=points+1
        score1.config(text="SCORE: "+ str(points))
        animals_found1.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
    else:#when to move on to next level
        points=0
        for widget in lvl1_game.winfo_children():
            widget.place_forget() 
        ###
        global lvl1_summary
        lvl1_summary= Frame(root, width=800,  height=400, bg="#4c5751")

        amazon_bg = PIL.Image.open("D:\\yr12\\project pics\\level 1\\amazon_bg.png")
        global amazon_photo
        amazon_photo=ImageTk.PhotoImage(amazon_bg)
        amazon_label=Label(lvl1_summary, image=amazon_photo)

        summary_screen1= Label(master=lvl1_summary, text="You've found the following Aves" +"\n" + " in the Amazon Rainforest:" + "\n" + list_correct_animals,
                                fg="black", width=50, height=10, bg="grey", font=("Comic Sans MS", 12))
        next_level= Button(master=lvl1_summary, text=("next level"), width=10, height=5, command=transition1, bg="#4c5751", font=("Comic Sans MS", 8))
        lvl1_summary.place(x=0, y=0)
        amazon_label.place(x=0, y=0, relwidth=1, relheight=1)
        summary_screen1.place(x=150, y=75)
        next_level.place(x=700, y=300)
        list_correct_animals=""
    
      

##


def Level1():
    for widget in root.winfo_children():
         widget.place_forget() 
    
    global lvl1_game
    lvl1_game= Frame(root, width=800, height=400, bg="#4c5751")

    #displaying options for lvl1
    #Macaw
    macaw_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\blue_macaw.jpg")
    macaw_CTK =  customtkinter.CTkImage(macaw_img,
                                        size=(130,110))
    macaw_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=macaw_CTK, text="Blue and Gold Macaw", fg_color="#4c5751", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Blue and Gold Macaw":correct_choice (m))   
    macaw_button.bind("<Button-1>", disable_button)
    #capybara
    capybara_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\capybara.jpeg")
    capybara_CTK =  customtkinter.CTkImage(capybara_img,
                                        size=(130,110))
    capybara_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=capybara_CTK, text="capybara", fg_color="#4c5751", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="capybara":wrong_answer (m))   
    capybara_button.bind("<Button-1>", disable_button)
    #jaguar
    jaguar_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\jaguar.jpeg")
    jaguar_CTK =  customtkinter.CTkImage(jaguar_img,
                                        size=(130,110))
    jaguar_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=jaguar_CTK, text="jaguar", fg_color="#4c5751", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="jaguar":wrong_answer (m))   
    jaguar_button.bind("<Button-1>", disable_button)
    #poison dart frog
    PDfrog_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\poison-dart-frog.jpeg")
    PDfrog_CTK =  customtkinter.CTkImage(PDfrog_img,
                                        size=(130,110))
    PDfrog_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=PDfrog_CTK, text="poison dart frog", fg_color="#4c5751", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="poison dart frog":wrong_answer (m))   
    PDfrog_button.bind("<Button-1>", disable_button)
    #Pantalón-de-Cuerno
    Pcuerno_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\Pantalón-de-Cuerno.jpg")
    Pcuerno_CTK =  customtkinter.CTkImage(Pcuerno_img,
                                        size=(130,110))
    Pcuerno_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=Pcuerno_CTK, text="Pantalón-de-Cuerno", fg_color="#4c5751", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Pantalón-de-Cuerno":correct_choice (m))   
    Pcuerno_button.bind("<Button-1>", disable_button)
    #Red Howler Money
    RHMonkey_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\red-howler-monkey.jpeg")
    RHMonkey_CTK =  customtkinter.CTkImage(RHMonkey_img,
                                        size=(130,110))
    RHMonkey_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=RHMonkey_CTK, text="Red Howler Monkey", fg_color="#4c5751", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Red Howler Monkey":wrong_answer (m))   
    RHMonkey_button.bind("<Button-1>", disable_button)
    #black capped squirrel monkey
    BCSMonkey_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\black-capped-squirrel-monkey.jpeg")
    BCSMonkey_CTK =  customtkinter.CTkImage(BCSMonkey_img,
                                        size=(130,110))
    BCSMonkey_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=BCSMonkey_CTK, text="Black Capped Squirrel", fg_color="#4c5751", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Black Capped Squirrel":wrong_answer (m))   
    BCSMonkey_button.bind("<Button-1>", disable_button)
    #green anaconda
    GAnaconda_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\green-anaconda.jpeg")
    GAnaconda_CTK =  customtkinter.CTkImage(GAnaconda_img,
                                        size=(130,110))
    GAnaconda_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=GAnaconda_CTK, text="Green Anaconda", fg_color="#4c5751", font=("Comic Sans MS", 12), compound="bottom",
                                        command=lambda m="Green Anaconda":wrong_answer (m))   
    GAnaconda_button.bind("<Button-1>", disable_button)

    #Toucan-Collared-Aracari
    CAToucan_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\Toucan-Collared-Aracari.jpg")
    CAToucan_CTK =  customtkinter.CTkImage(CAToucan_img,
                                        size=(130,110))
    CAToucan_button =  customtkinter.CTkButton( text_color="black", master=lvl1_game, image=CAToucan_CTK, text="Toucan Collared Aracari", fg_color="#4c5751", font=("Comic Sans MS", 12), compound="bottom",
                                        command= (lambda m="Toucan Collared Aracari":correct_choice (m)))   
    CAToucan_button.bind("<Button-1>", disable_button)
    #displaying score and correct answers- lvl1
    global score1
    global animals_found1
    score1 = Label(lvl1_game, text="SCORE: ", font=(("Times New Roman"), 18), bg="#4c5751")
    animals_found1 = Label(lvl1_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18), bg="#4c5751")

    #back option
    def back1_func():
        for widget in lvl1_game.winfo_children():
            widget.place_forget() 
        start()
    back1= Button(master=lvl1_game, text=("back"), width=10, height=5, command=back1_func, bg="#4c5751", font=("Comic Sans MS", 8))

    lvl1_game.place(x=0, y=0)
    back1.place(x=700, y=300)
    score1.place(x=550, y=0)
    animals_found1.place(x=500, y=50)
    CAToucan_button.place(x=280, y=260)
    GAnaconda_button.place(x=140, y=260)
    BCSMonkey_button.place(x=0, y=260)
    RHMonkey_button.place(x=0, y=135)
    Pcuerno_button.place(x=140, y=135)
    PDfrog_button.place(x=280, y=135)
    jaguar_button.place(x=280, y=0)
    capybara_button.place(x=140, y=0)
    macaw_button.place(x=0, y=0)
    




##########



def start():
    for widget in title_screen.winfo_children():
         widget.place_forget() 
    global instr_lvl1
    instr_lvl1=Frame(root, width=800, height=400, bg="#4c5751")
    #display instructions for first level
    Amazon = Label(instr_lvl1, text="Welcome to the Amazon Rainforest!" + "\n"+ "We need to find 3 aves." +"\n" + "Remember, aves is the scientific name for birds." + "\n"+ "Birds have feathers and beaks and lay eggs," + "\n" + " like the birds shown here!", font=("Comic Sans MS", 12), width=40, bg="#4c5751")

    #continue button to start 1st level
    cont = Button(instr_lvl1, text="Continue", command=Level1, bg="#4c5751", font=("Comic Sans MS", 8))

    #collage of birds-illustration of what birds look like
    birds_collage_image = PIL.Image.open(r"D:\yr12\\project pics\level 1\lvl-1-intro.png")
    TK_birds_collage =  customtkinter.CTkImage(birds_collage_image,
        size=(400,400))
    birds_collage =  customtkinter.CTkLabel(master=instr_lvl1, image=TK_birds_collage, text="")
    instr_lvl1.place(x=0, y=0)
    birds_collage.place(x=0, y=0)
    cont.place(x=700, y=300)
    Amazon.place(x=400, y=100)



############


def introduction():
    global title_screen
    title_screen=Frame(root , width=800, height=400)

    title_bg = PIL.Image.open("D:\\yr12\\intro_screen_bg.png")
    global title_photo
    title_photo=ImageTk.PhotoImage(title_bg)
    bg_label=Label(title_screen, image=title_photo)

    begin = customtkinter.CTkButton(title_screen, text="Begin", command=start, text_color="black", font=("Comic Sans MS", 18), height=15, width=25, corner_radius=5, border_width=2, border_color="brown", fg_color="white")
    intro = Label(title_screen, text="Animal Classification Game" + "\n" + "Journey Across the Globe", height = 3, width=20, font=("Comic Sans MS", 16), bg="white")

    title_screen.place(x=0, y=0)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    intro.place(x=275, y=110)
    begin.place(x=370, y=210)
    menu_frame.lift()
    menu.lift()

introduction()

############




root.mainloop()