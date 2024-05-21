
import PIL.Image
from PIL import ImageTk, Image
from tkinter import *
from tkinter import Tk
import customtkinter
import sys

root = Tk()
root.title('animal classification game')
root.geometry("800x400")
sys.setrecursionlimit(500)

#subprogram used to determine which button was clicked, and store the animal name
def which_button(m): #when correct button clicked, used to store list of correct animals so far
    global list_correct_animals
    #adding to list of correct animals
    list_correct_animals=list_correct_animals + "\n" + m

#all have to do with displaying results- common aspects of all levels

global m
global points
points=0
global list_correct_animals
list_correct_animals= ""

##########
def endscreen():
    for widget in lvl6_summary.winfo_children():
        widget.destroy() 
    congrats= Frame(root, width=800, height=400, bg="white")
    congrats_message= Label(master=congrats, text=("Congrats, you are now an expert on the 6 categories of animals"), width=50, height=8, bg="grey", fg="black", font=("Times New Roman", 14))
    replay= Button(master=congrats, text=("replay"), width=10, height=5, command=start())
    replay.place(x=700, y=350)
    congrats.place(x=0, y=0)
    congrats_message.place(x=250, y=100)




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
            widget.destroy() 
        global lvl6_summary
        lvl6_summary= Frame(root, width=800, height=400, bg="lavender")
        next_level6= Button(master=lvl6_summary, text=("finish"), width=10, height=5, command=endscreen)
        summary_screen6= Label(master=lvl6_summary, text=("You've found the following invertebrates" + list_correct_animals), width=50, height=10, bg="grey", fg="black")
        lvl6_summary.place(x=0, y=0)
        summary_screen6.place(x=250, y=150)
        next_level6.place(x=700, y=300)

def wrong_answer6(m):
    global oops6
    global try_again6
    def undo_wrong_answer6() :
        # when try again clicked, returns to level
        oops6.destroy()
        try_again6.destroy() 
    #message for incorrect answer
    oops6= Label(master=lvl6_game, text=("Oops, that isn't an invertebrate!" + "\n" + "Remember invertebrates don't have a spine and are really tiny!"), font=("Times New Roman", 14), width=42, height=15, fg="black")
    oops6.place(x=0, y=0)
    try_again6= Button(master=lvl6_game, text=("Try again"), width=42, height=10, command=undo_wrong_answer6, bg="grey", fg="black", font=("Times New Roman", 14))
    try_again6.place(x=0, y=250)




##########
def Level6():
    global instr_lvl6
    for widget in instr_lvl6.winfo_children():
        widget.destroy()
    global lvl6_game
    lvl6_game= Frame(root, width=800, height=400, bg="lavender")
    #displaying options
    #Eastern Cottontail
    ECottontail_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\eastern-cottontail.jpg")
    ECottontail_CTK =  customtkinter.CTkImage(ECottontail_img,
                                        size=(130,110))
    ECottontail_button =  customtkinter.CTkButton(master=lvl6_game, image=ECottontail_CTK, text="Eastern Cottontail", compound="bottom",
                                        command=lambda m="Eastern Cottontail":wrong_answer6(m))
    #Field Mouse
    FMouse_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\field-mouse.jpg")
    FMouse_CTK =  customtkinter.CTkImage(FMouse_img,
                                        size=(130,110))
    FMouse_button =  customtkinter.CTkButton(master=lvl6_game, image=FMouse_CTK, text="Field Mouse", compound="bottom",
                                        command=lambda m="Field Mouse":wrong_answer6(m))
    #earthworm
    earthworm_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\earthworm.jpg")
    earthworm_CTK =  customtkinter.CTkImage(earthworm_img,
                                        size=(130,110))
    earthworm_button =  customtkinter.CTkButton(master=lvl6_game, image=earthworm_CTK, text="earthworm", compound="bottom",
                                        command=lambda m="earthworm":correct_choice6(m))
    #Garter Snake
    GSnake_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\garter-snake.jpg")
    GSnake_CTK =  customtkinter.CTkImage(GSnake_img,
                                        size=(130,110))
    GSnake_button =  customtkinter.CTkButton(master=lvl6_game, image=GSnake_CTK, text="Garter Snake", compound="bottom",
                                        command=lambda m="Garter Snake":wrong_answer6(m))
    #German Shephard
    GShephard_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\german-shephard.jpg")
    GShephard_CTK =  customtkinter.CTkImage(GShephard_img,
                                        size=(130,110))
    GShephard_button =  customtkinter.CTkButton(master=lvl6_game, image=GShephard_CTK, text="German Shephard", compound="bottom",
                                        command=lambda m="German Shephard":wrong_answer6(m))
    #ladybug
    ladybug_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\ladybug.jpg")
    ladybug_CTK =  customtkinter.CTkImage(ladybug_img,
                                        size=(130,110))
    ladybug_button =  customtkinter.CTkButton(master=lvl6_game, image=ladybug_CTK, text="ladybug", compound="bottom",
                                        command=lambda m="ladybug":correct_choice6(m))
    #Monarch Butterfly
    MButterfly_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\monarch-butterfly.jpg")
    MButterfly_CTK =  customtkinter.CTkImage(MButterfly_img,
                                        size=(130,110))
    MButterfly_button =  customtkinter.CTkButton(master=lvl6_game, image=MButterfly_CTK, text="Monarch Butterfly", compound="bottom",
                                        command=lambda m="Monarch Butterfly":correct_choice6(m))
    #honeyeater
    honeyeater_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\honeyeater.jpg")
    honeyeater_CTK =  customtkinter.CTkImage(honeyeater_img,
                                        size=(130,110))
    honeyeater_button =  customtkinter.CTkButton(master=lvl6_game, image=honeyeater_CTK, text="honeyeater", compound="bottom",
                                        command=lambda m="honeyeater":wrong_answer6(m))
    #Water Skink
    WSkink_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\water-skink.jpg")
    WSkink_CTK =  customtkinter.CTkImage(WSkink_img,
                                        size=(130,110))
    WSkink_button =  customtkinter.CTkButton(master=lvl6_game, image=WSkink_CTK, text="Water Skink", compound="bottom",
                                        command= (lambda m="Water Skink":wrong_answer6(m)))
    #results
    global score6
    global animals_found6
    score6 = Label(lvl6_game, text="SCORE: ", font=(("Times New Roman"), 18), fg="black", bg="grey")
    animals_found6 = Label(lvl6_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18), fg="black", bg="grey")
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
    animals_found6.place(x=450, y=50)
    #back option
    def back6_func():
        for widget in lvl6_game.winfo_children():
            widget.destroy() 
        transition5()
    back6= Button(master=lvl6_game, text=("back"), width=10, height=5, command=back6_func)
    back6.place(x=700, y=350)


##########

def transition5():
    global list_correct_animals
    list_correct_animals=""
    for widget in lvl4_summary.winfo_children():
         widget.destroy()
    global instr_lvl6
    instr_lvl6= Frame(root, width=800, height=400, bg="lavender")
    #display instructions for 6th level
    backyard = Label(instr_lvl6, text="Next we are going to look for " + "\n"+ "invertebrates in my backyard" +"\n" + "Invertebrates don't have a spine and are often quite small.", font=("Times New Roman", 12), width=40)
    #continue button to start 6th level
    cont6 =  Button(instr_lvl6, text="Continue", command=Level6)
    #collage of invertebrates
    invertebrates_collage_image = PIL.Image.open("D:\\yr12\\project pics\\level 6\\invertebrates.jpg")
    TK_invertebrates_collage =   customtkinter.CTkImage(invertebrates_collage_image,
        size=(400,400))
    invertebrates_collage =   customtkinter.CTkLabel(master=instr_lvl6, image=TK_invertebrates_collage)
    instr_lvl6.place(x=0, y=0)
    invertebrates_collage.place(x=400, y=0)
    cont6.place(x=30, y=350)
    backyard.place(x=30, y=100)




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
            widget.destroy() 
        global lvl5_summary
        lvl5_summary= Frame(root, width=800, height=400, bg="light yellow")
        next_level5= Button(master=lvl5_summary, text=("next level"), width=10, height=5, command=transition5)
        summary_screen5= Label(master=lvl5_summary, text=("You've found the following reptiles" + list_correct_animals), width=50, height=10, bg="grey")
        lvl5_summary.place(x=0, y=0)
        summary_screen5.place(x=250, y=150)
        next_level5.place(x=700, y=300)

def wrong_answer5(m):
    global oops5
    global try_again5
    def undo_wrong_answer5() :
        # when try again clicked, returns to level
        oops5.destroy()
        try_again5.destroy() 
    #message for incorrect answer
    oops5= Label(master=lvl5_game, text=("Oops, that isn't a reptile!" + "\n" + "Remember reptiles have scaly skin!"), font=("Times New Roman", 14), width=42, height=15, fg="black")
    oops5.place(x=0, y=0)
    try_again5= Button(master=lvl5_game, text=("Try again"), width=42, height=10, command=undo_wrong_answer5, bg="grey", fg="black", font=("Times New Roman", 14))
    try_again5.place(x=0, y=250)



##########
def Level5():
    global instr_lvl5
    for widget in instr_lvl5.winfo_children():
        widget.destroy()
    ###
    global lvl5_game
    lvl5_game= Frame(root, width=800,  height=400, bg="light yellow")
    #displaying options
    #Sand Goanna
    SGoanna_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\reptiles\\sand-goanna.jpg")
    SGoanna_CTK =  customtkinter.CTkImage(SGoanna_img,
                                        size=(130,110))
    SGoanna_button =  customtkinter.CTkButton(master=lvl5_game, image=SGoanna_CTK, text="Sand Goanna", compound="bottom",
                                        command=lambda m="Sand Goanna":correct_choice5(m))
    #Throny Devil
    TDevil_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\reptiles\\throny-devil.jpg")
    TDevil_CTK =  customtkinter.CTkImage(TDevil_img,
                                        size=(130,110))
    TDevil_button =  customtkinter.CTkButton(master=lvl5_game, image=TDevil_CTK, text="Throny Devil", compound="bottom",
                                        command=lambda m="Throny Devil":correct_choice5(m))
    #dingo
    dingo_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\dingo.jpg")
    dingo_CTK =  customtkinter.CTkImage(dingo_img,
                                        size=(130,110))
    dingo_button =  customtkinter.CTkButton(master=lvl5_game, image=dingo_CTK, text="dingo", compound="bottom",
                                        command=lambda m="dingo":wrong_answer5(m))
    #Australian Feral Camel
    AFCamel_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\australian-feral-camel.jpg")
    AFCamel_CTK =  customtkinter.CTkImage(AFCamel_img,
                                        size=(130,110))
    AFCamel_button =  customtkinter.CTkButton(master=lvl5_game, image=AFCamel_CTK, text="Australian Feral Camel", compound="bottom",
                                        command=lambda m="Australian Feral Camel":wrong_answer5(m))
    #Frill Neck Lizard
    FNLizard_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\reptiles\\frill-neck-lizard.jpg")
    FNLizard_CTK =  customtkinter.CTkImage(FNLizard_img,
                                        size=(130,110))
    FNLizard_button =  customtkinter.CTkButton(master=lvl5_game, image=FNLizard_CTK, text="Frill Neck Lizard", compound="bottom",
                                        command=lambda m="Frill Neck Lizard":correct_choice5(m))
    #Stimson's Python
    SPython_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\stimson's-python.jpg")
    SPython_CTK =  customtkinter.CTkImage(SPython_img,
                                        size=(130,110))
    SPython_button =  customtkinter.CTkButton(master=lvl5_game, image=SPython_CTK, text="Stimson's Python", compound="bottom",
                                        command=lambda m="Stimson's Python":wrong_answer5(m))
    #Quokka
    quokka_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\quokka.jpg")
    quokka_CTK =  customtkinter.CTkImage(quokka_img,
                                        size=(130,110))
    quokka_button =  customtkinter.CTkButton(master=lvl5_game, image=quokka_CTK, text="Quokka", compound="bottom",
                                        command=lambda m="Quokka":wrong_answer5(m))
    #kangaroo
    kangaroo_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\kangaroo.jpg")
    kangaroo_CTK =  customtkinter.CTkImage(kangaroo_img,
                                        size=(130,110))
    kangaroo_button =  customtkinter.CTkButton(master=lvl5_game, image=kangaroo_CTK, text="kangaroo", compound="bottom",
                                        command=lambda m="kangaroo":wrong_answer5(m))

    #Kookaburra
    kookaburra_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\kookaburra.jpg")
    kookaburra_CTK =  customtkinter.CTkImage(kookaburra_img,
                                        size=(130,110))
    kookaburra_button =  customtkinter.CTkButton(master=lvl5_game, image=kookaburra_CTK, text="Kookaburra", compound="bottom",
                                        command= (lambda m="Kookaburra":wrong_answer5(m)))
    #results
    global score5
    global animals_found5
    score5 = Label(lvl5_game, text="SCORE: ", font=(("Times New Roman"), 18))
    animals_found5 = Label(lvl5_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))

    #back option
    def back5_func():
        for widget in lvl5_game.winfo_children():
            widget.destroy() 
        transition4()
    back5= Button(master=lvl5_game, text=("back"), width=10, height=5, command=back5_func)


    lvl5_game.place(x=0, y=0)
    back5.place(x=700, y=350)
    score5.place(x=550, y=0)
    animals_found5.place(x=450, y=50)
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
    global list_correct_animals
    list_correct_animals=""
    for widget in lvl4_summary.winfo_children():
         widget.destroy()
    global instr_lvl5
    instr_lvl5= Frame(root, width=800, height=400, bg="light yellow")
    #display instructions for 5th level
    outback = Label(instr_lvl5, text="Next we are going to look for " + "\n"+ "reptiles in the outback!" +"\n" + "Reptiles have scaly skin and lay eggs.", font=("Times New Roman", 12), width=40)
    #continue button to start 5th level
    cont5 =  Button(instr_lvl5, text="Continue", command=Level5)
    #collage of reptiles
    reptiles_collage_image = PIL.Image.open("D:\\yr12\\project pics\\level 5\\Reptiles.jpg")
    TK_reptiles_collage =   customtkinter.CTkImage(reptiles_collage_image,
        size=(400,400))
    reptiles_collage =   customtkinter.CTkLabel(master=instr_lvl5, image=TK_reptiles_collage)
    instr_lvl5.place(x=0, y=0)
    reptiles_collage.place(x=400, y=0)
    cont5.place(x=30, y=350)
    outback.place(x=30, y=100)




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
            widget.destroy() 
        ###
        global lvl4_summary
        lvl4_summary= Frame(root, width=800, height=400, bg="salmon")
        next_level4= Button(master=lvl4_summary, text=("next level"), width=10, height=5, command=transition4)
        summary_screen4= Label(master=lvl4_summary, text=("You've found the following amphibians" + list_correct_animals), width=50, height=10, bg="grey")
        lvl4_summary.place(x=0, y=0)
        summary_screen4.place(x=250, y=150)
        next_level4.place(x=700, y=300)


def wrong_answer4(m):
    global oops4
    global try_again4
    def undo_wrong_answer4() :
        # when try again clicked, returns to level
        oops4.destroy()
        try_again4.destroy() 
    #message for incorrect answer
    oops4= Label(master=lvl4_game, text=("Oops, that isn't an amphibian!" + "\n" + "Remember amphibians have slimy skin and live around water!"), font=("Times New Roman", 14), width=42, height=15, fg="black")
    oops4.place(x=0, y=0)
    try_again4= Button(master=lvl4_game, text=("Try again"), width=42, height=10, command=undo_wrong_answer4, bg="grey", fg="black", font=("Times New Roman", 14) )
    try_again4.place(x=0, y=250)


##########
def Level4():
    global instr_lvl4
    for widget in instr_lvl4.winfo_children():
        widget.destroy()
    
    ###
    global lvl4_game
    lvl4_game= Frame(root, width=800,  height=400, bg="salmon")
    #displaying options
    #Clouded Leopard
    CLeopard_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\clouded-leopard.jpg")
    CLeopard_CTK =  customtkinter.CTkImage(CLeopard_img,
                                        size=(130,110))
    CLeopard_button =  customtkinter.CTkButton(master=lvl4_game, image=CLeopard_CTK, text="Clouded Leopard", compound="bottom",
                                        command=lambda m="Clouded Leopard":wrong_answer4(m))
    #red giant flying squirrel
    RGFSquirrel_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\red-giant-flying-squirrel.jpg")
    RGFSquirrel_CTK =  customtkinter.CTkImage(RGFSquirrel_img,
                                        size=(130,110))
    RGFSquirrel_button =  customtkinter.CTkButton(master=lvl4_game, image=RGFSquirrel_CTK, text="red giant flying squirrel", compound="bottom",
                                        command=lambda m="red giant flying squirrel":wrong_answer4(m))
    #Malay Civet
    MCivet_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Malay-civet.jpg")
    MCivet_CTK =  customtkinter.CTkImage(MCivet_img,
                                        size=(130,110))
    MCivet_button =  customtkinter.CTkButton(master=lvl4_game, image=MCivet_CTK, text="Malay Civet", compound="bottom",
                                        command=lambda m="Malay Civet":wrong_answer4(m))
    #Proboscis monkey
    PMonkey_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Proboscis-monkey.jpg")
    PMonkey_CTK =  customtkinter.CTkImage(PMonkey_img,
                                        size=(130,110))
    PMonkey_button =  customtkinter.CTkButton(master=lvl4_game, image=PMonkey_CTK, text="Proboscis monkey", compound="bottom",
                                        command=lambda m="Proboscis monkey":wrong_answer4(m))
    #Wallaces flying frog
    WFFrog_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\amphibians\\Wallaces-flying-frog.jpg")
    WFFrog_CTK =  customtkinter.CTkImage(WFFrog_img,
                                        size=(130,110))
    WFFrog_button =  customtkinter.CTkButton(master=lvl4_game, image=WFFrog_CTK, text="Wallaces Flying Frog", compound="bottom",
                                        command=lambda m="Wallaces Flying Frog":correct_choice4(m))
    #orangutan
    orangutan_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Orangutan.jpg")
    orangutan_CTK =  customtkinter.CTkImage(orangutan_img,
                                        size=(130,110))
    orangutan_button =  customtkinter.CTkButton(master=lvl4_game, image=orangutan_CTK, text="orangutan", compound="bottom",
                                        command=lambda m="orangutan":wrong_answer4(m))

    #jade tree frog
    JTFrog_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\amphibians\\jade-tree-frog.jpg")
    JTFrog_CTK =  customtkinter.CTkImage(JTFrog_img,
                                        size=(130,110))
    JTFrog_button =  customtkinter.CTkButton(master=lvl4_game, image=JTFrog_CTK, text="jade tree frog", compound="bottom",
                                        command=lambda m="jade tree frog":correct_choice4(m))

    #Pygmy elephant
    PElephant_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Pygmy-Elephant.jpg")
    PElephant_CTK =  customtkinter.CTkImage(PElephant_img,
                                        size=(130,110))
    PElephant_button =  customtkinter.CTkButton(master=lvl4_game, image=PElephant_CTK, text="Pygmy Elephant", compound="bottom",
                                        command=lambda m="Pygmy Elephant":wrong_answer4(m))

    #BFHFrog
    BFHFrog_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\amphibians\\bornean-flat-headed-frog.jpg")
    BFHFrog_CTK =  customtkinter.CTkImage(BFHFrog_img,
                                        size=(130,110))
    BFHFrog_button =  customtkinter.CTkButton(master=lvl4_game, image=BFHFrog_CTK, text="bornean flat headed frog", compound="bottom",
                                        command= (lambda m="bornean flat headed frog":correct_choice4(m)))

    #results
    global score4
    global animals_found4
    score4 = Label(lvl4_game, text="SCORE: ", font=(("Times New Roman"), 18))
    animals_found4 = Label(lvl4_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18), fg="black")

    # #back option
    def back4_func():
        for widget in lvl4_game.winfo_children():
            widget.destroy() 
        transition3()
    back4= Button(master=lvl4_game, text=("back"), width=10, height=5, command=back4_func)

    lvl4_game.place(x=0, y=0)
    back4.place(x=700, y=350)
    score4.place(x=550, y=0)
    animals_found4.place(x=450, y=50)
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
    global list_correct_animals
    list_correct_animals=""
    for widget in lvl3_summary.winfo_children():
         widget.destroy()
    global instr_lvl4
    instr_lvl4= Frame(root, width=800,  height=400, bg="salmon")
    #display instructions for 4th level
    BRF = Label(instr_lvl4, text="Next we are going to look for " + "\n"+ "amphibians in the Borneo Rainforest!" +"\n" + "Amphibians have slimy skin and live around water.", font=("Times New Roman", 12), width=40)
    #continue button to start 4th level
    cont4 =  Button(instr_lvl4, text="Continue", command=Level4)
    #collage of amphibians
    amphibians_collage_image = PIL.Image.open("D:\\yr12\\project pics\\level 4\\amphibians.jpg")
    TK_amphibians_collage =  customtkinter.CTkImage(amphibians_collage_image,
        size=(400,400))
    amphibians_collage =  customtkinter.CTkLabel(master=instr_lvl4, image=TK_amphibians_collage)
    instr_lvl4.place(x=0, y=0)
    amphibians_collage.place(x=400, y=0)
    cont4.place(x=30, y=350)
    BRF.place(x=30, y=100)



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
            widget.destroy() 
        global lvl3_summary
        lvl3_summary= Frame(root, width=800,  height=400, bg="light blue")
        summary_screen3= Label(master=lvl3_summary, text=("You've found the following fish" + list_correct_animals), width=50, height=10, bg="grey", fg="black")
        next_level3= Button(master=lvl3_summary, text=("next level"), width=10, height=5, command=transition3)
        lvl3_summary.place(x=0, y=0)
        summary_screen3.place(x=250, y=150)
        next_level3.place(x=700, y=300)

def wrong_answer3(m):
    global oops3
    global try_again3
    def undo_wrong_answer3() :
        # when try again clicked, returns to level
        oops3.destroy()
        try_again3.destroy() 
    #message for incorrect answer
    oops3= Label(master=lvl3_game, text="Oops, that isn't a fish!" + "\n" + "Remember fish have scales and live underwater!", font=("Times New Roman", 14), width=42, height=15, fg="black")
    try_again3= Button(master=lvl3_game, text=("Try again"), width=42, height=10, command=undo_wrong_answer3, bg="grey", fg="black", font=("Times New Roman", 14))
    oops3.place(x=0, y=0)
    try_again3.place(x=0, y=250)  

########
def Level3():
    global instr_lvl3
    for widget in instr_lvl3.winfo_children():
        widget.destroy()
    ###
    global lvl3_game
    lvl3_game= Frame(root, width=800,  height=400, bg="light blue")
    #displaying options
    #clownfish
    Cfish_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\fish\\clownfish.jpg")
    Cfish_CTK =  customtkinter.CTkImage(Cfish_img,
                                        size=(130,110))
    Cfish_button =  customtkinter.CTkButton(master=lvl3_game, image=Cfish_CTK, text="clownfish", compound="bottom",
                                        command=lambda m="clownfish":correct_choice3(m))
    #blanket octapus
    Boctapus_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\blanket-octopus.jpg")
    Boctapus_CTK =  customtkinter.CTkImage(Boctapus_img,
                                        size=(130,110))
    Boctapus_button =  customtkinter.CTkButton(master=lvl3_game, image=Boctapus_CTK, text="blanket octapus", compound="bottom",
                                        command=lambda m="blanket octapus":wrong_answer3(m))
    #dugong
    dugong_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\dugong.jpg")
    dugong_CTK =  customtkinter.CTkImage(dugong_img,
                                        size=(130,110))
    dugong_button =  customtkinter.CTkButton(master=lvl3_game, image=dugong_CTK, text="dugong", compound="bottom",
                                        command=lambda m="dugong":wrong_answer3(m))
    #green turtle
    Gturtle_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\fish\\green-turtle.jpg")
    Gturtle_CTK =  customtkinter.CTkImage(Gturtle_img,
                                        size=(130,110))
    Gturtle_button =  customtkinter.CTkButton(master=lvl3_game, image=Gturtle_CTK, text="green turtle", compound="bottom",
                                        command=lambda m="green turtle":correct_choice3(m))
    #manta ray
    Mray_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\fish\\manta-ray.jpg")
    Mray_CTK =  customtkinter.CTkImage(Mray_img,
                                        size=(130,110))
    Mray_button =  customtkinter.CTkButton(master=lvl3_game, image=Mray_CTK, text="manta ray", compound="bottom",
                                        command=lambda m="manta ray":correct_choice3(m))
    #giant clam
    Gclam_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\giant-clam.jpg")
    Gclam_CTK =  customtkinter.CTkImage(Gclam_img,
                                        size=(130,110))
    Gclam_button =  customtkinter.CTkButton(master=lvl3_game, image=Gclam_CTK, text="giant clam", compound="bottom",
                                        command=lambda m="giant clam":wrong_answer3(m))
    #humpback whale
    HWhale_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\humpback-whale.jpg")
    HWhale_CTK =  customtkinter.CTkImage(HWhale_img,
                                        size=(130,110))
    HWhale_button =  customtkinter.CTkButton(master=lvl3_game, image=HWhale_CTK, text="Humpback Whale", compound="bottom",
                                        command=lambda m="Humpback Whale":wrong_answer3(m))
    #jellyfish
    jellyfish_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\jellyfish.jpg")
    jellyfish_CTK =  customtkinter.CTkImage(jellyfish_img,
                                        size=(130,110))
    jellyfish_button =  customtkinter.CTkButton(master=lvl3_game, image=jellyfish_CTK, text="jellyfish", compound="bottom",
                                        command=lambda m="jellyfish":wrong_answer3(m))
    #mantis shrimp
    MShrimp_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\mantis-shrimp.jpg")
    MShrimp_CTK =  customtkinter.CTkImage(MShrimp_img,
                                        size=(130,110))
    MShrimp_button =  customtkinter.CTkButton(master=lvl3_game, image=MShrimp_CTK, text="mantis shrimp", compound="bottom",
                                        command= (lambda m="mantis shrimp":wrong_answer3(m)))
    #results
    global score3
    global animals_found3
    score3 = Label(lvl3_game, text="SCORE: ", font=(("Times New Roman"), 18))
    animals_found3 = Label(lvl3_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18), fg="black")

    #back option
    def back3_func():
        for widget in lvl3_game.winfo_children():
            widget.destroy() 
        transition2()
    
    back3=  Button(master=lvl3_game, text=("back"), width=10, height=5, command=back3_func())
    lvl3_game.place(x=0, y=0)
    score3.place(x=550, y=0)
    animals_found3.place(x=450, y=50)
    MShrimp_button.place(x=280, y=260)
    jellyfish_button.place(x=140, y=260)
    HWhale_button.place(x=0, y=260)
    Gclam_button.place(x=0, y=135)
    Mray_button.place(x=140, y=135)
    Gturtle_button.place(x=280, y=135)
    dugong_button.place(x=280, y=0)
    Boctapus_button.place(x=140, y=0)
    Cfish_button.place(x=0, y=0)
    back3.place(x=700, y=350)



#########
def transition2():
    global list_correct_animals
    list_correct_animals=""
    for widget in lvl2_summary.winfo_children():
         widget.destroy()
    global instr_lvl3
    instr_lvl3= Frame(root, width=800,  height=400, bg="light blue")
    #display instructions for 3rd level
    #great barrier reef
    GBR = Label(instr_lvl3, text="Next we are going to look for " + "\n"+ "fish in the Great Barrier Reef" +"\n" + "Fish have scales and live underwater.", font=("Times New Roman", 12), width=40)
    #continue button to start 3rd level
    global cont3
    cont3 =  Button(instr_lvl3, text="Continue", command=Level3)
    #collage of fish
    fish_collage_image = PIL.Image.open(r"D:\yr12\project pics\level 3\fish-montage.jpg")
    TK_fish_collage =   customtkinter.CTkImage(fish_collage_image,
        size=(400,400))
    fish_collage =  customtkinter.CTkLabel(master=instr_lvl3, image=TK_fish_collage)
    instr_lvl3.place(x=0, y=0)
    fish_collage.place(x=400, y=0)
    cont3.place(x=30, y=350)
    GBR.place(x=30, y=100)



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
            widget.destroy() 
        ###
        global lvl2_summary
        lvl2_summary= Frame(root, width=800,  height=400, bg="#deb878")
        summary_screen2= Label(master=lvl2_summary, text="You've found the following mammals:" + list_correct_animals, fg="black", width=50, height=10, bg="grey")
        next_level2=Button(master=lvl2_summary, text=("next level"), width=10, height=5, command=transition2)
        lvl2_summary.place(x=0, y=0)
        summary_screen2.place(x=250, y=150)
        next_level2.place(x=700, y=300)



def wrong_answer2(m):
    global oops2
    global try_again2
    def undo_wrong_answer2() :
        # when try again clicked, returns to level
        oops2.destroy()
        try_again2.destroy()
    #message for incorrect answer
    oops2= Label(master=lvl2_game, text="Oops, that isn't a mammal!" + "\n" + "Remember mammals have hair or fur!", font=("Times New Roman", 14), width=42, height=15, fg="black")
    try_again2= Button(master=lvl2_game, text=("Try again"), width=42, height=10, command=undo_wrong_answer2, bg="grey", fg="black", font=("Times New Roman", 14))
    oops2.place(x=0, y=0)
    try_again2.place(x=0, y=250)  


##########

def Level2():
    for widget in instr_lvl2.winfo_children():
         widget.destroy()
    
    ###
    global lvl2_game
    lvl2_game= Frame(root, width=800,  height=400, bg="#deb878")
    #displaying options
    #cobra
    Cobra_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\cobra.jpg")
    cobra_CTK =  customtkinter.CTkImage(Cobra_img,
                                    size=(130,110))
    cobra_button =  customtkinter.CTkButton(master=lvl2_game, image=cobra_CTK, text="cobra", compound="bottom",
                                        command=lambda m="cobra":wrong_answer2(m))
    #aardvark
    aardvark_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\mammals\\aardvark.jpg")
    aardvark_CTK =  customtkinter.CTkImage(aardvark_img,
                                    size=(130,110))
    aardvark_button =  customtkinter.CTkButton(master=lvl2_game, image=aardvark_CTK, text="aardvark", compound="bottom",
                                        command=lambda m="aardvark":correct_choice2(m))
    #african_elephant
    african_elephant_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\mammals\\african_elephant.jpg")
    african_elephant_CTK =  customtkinter.CTkImage(african_elephant_img,
                                    size=(130,110))
    african_elephant_button =  customtkinter.CTkButton(master=lvl2_game, image=african_elephant_CTK, text="african elephant", compound="bottom",
                                        command=lambda m="african elephant":correct_choice2(m))
    #hornbill
    hornbill_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\hornbill.jpg")
    hornbill_CTK =  customtkinter.CTkImage(hornbill_img,
                                    size=(130,110))
    hornbill_button =  customtkinter.CTkButton(master=lvl2_game, image=hornbill_CTK, text="hornbill", compound="bottom",
                                        command=lambda m="hornbill":wrong_answer2(m))
    #scorpion
    scorpion_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\scorpion.jpg")
    scorpion_CTK =  customtkinter.CTkImage(scorpion_img,
                                    size=(130,110))
    scorpion_button =  customtkinter.CTkButton(master=lvl2_game, image=scorpion_CTK, text="scorpion", compound="bottom",
                                        command=lambda m="scorpion":wrong_answer2(m))
    #rhinoceros
    rhinoceros_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\mammals\\rhinoceros.jpg")
    rhinoceros_CTK =  customtkinter.CTkImage(rhinoceros_img,
                                    size=(130,110))
    rhinoceros_button =  customtkinter.CTkButton(master=lvl2_game, image=rhinoceros_CTK, text="rhinoneros", compound="bottom",
                                        command=lambda m="rhinoceros":correct_choice2(m))
    #ostrich
    ostrich_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\ostrich.jpg")
    ostrich_CTK =  customtkinter.CTkImage(ostrich_img,
                                    size=(130,110))
    ostrich_button =  customtkinter.CTkButton(master=lvl2_game, image=ostrich_CTK, text="ostrich", compound="bottom",
                                        command=lambda m="ostrich":wrong_answer2(m))
    #dung beetle
    dung_beetle_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\dung-beetle.jpg")
    dung_beetle_CTK =  customtkinter.CTkImage(dung_beetle_img,
                                    size=(130,110))
    dung_beetle_button =  customtkinter.CTkButton(master=lvl2_game, image=dung_beetle_CTK, text="dung beetle", compound="bottom",
                                        command=lambda m="dung beetle":wrong_answer2(m))

    #african spurred tortoise
    ASTortoise_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\african-spurred-tortoise.jpg")
    ASTortoise_CTK =  customtkinter.CTkImage(ASTortoise_img,
                                    size=(130,110))
    ASTortoise_button =  customtkinter.CTkButton(master=lvl2_game, image=ASTortoise_CTK, text="african spurred tortoise", compound="bottom",
                                        command= (lambda m="african spurred tortoise":wrong_answer2(m)))
    #results
    global score2
    global animals_found2
    score2 = Label(lvl2_game, text="SCORE: ", font=(("Times New Roman"), 18))
    animals_found2 = Label(lvl2_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))

    #back option
    def back2_func():
        for widget in lvl2_game.winfo_children():
            widget.destroy() 
        transition1()

    back2=  Button(master=lvl2_game, text=("back"), width=10, height=5, command=back2_func)

    lvl2_game.place(x=0, y=0)
    back2.place(x=700, y=300)
    score2.place(x=550, y=0)
    animals_found2.place(x=450, y=50)
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
    global list_correct_animals
    list_correct_animals=""
    for widget in lvl1_summary.winfo_children():
         widget.destroy()
    global instr_lvl2
    instr_lvl2= Frame(root, width=800,  height=400, bg="#deb878" )
    #display instructions for second level
    Savanna = Label(instr_lvl2, text="Next we are going to look for " + "\n"+ "mammals in the African Savanna" +"\n" + "Mammals are warm blooded, have hair or fur " + "\n"+ "and have very complex brains.", font=("Times New Roman", 12), width=40)
    #continue button to start 2nd level
    cont2 =  Button(instr_lvl2, text="Continue", command=Level2)
    #collage of mammals- to refer to how mammals look
    mammals_collage_image = PIL.Image.open(r"D:\yr12\project pics\level 2\Mammal_intro.jpg")
    TK_mammals_collage =  customtkinter.CTkImage(mammals_collage_image,
        size=(400,400))
    mammals_collage =  customtkinter.CTkLabel(master=instr_lvl2, image=TK_mammals_collage)
    instr_lvl2.place(x=0, y=0)
    mammals_collage.place(x=400, y=0)
    cont2.place(x=30, y=350)
    Savanna.place(x=30, y=100)


##########


##
#defining what happens when correct/incorrect buttons are pressed for LEVEL 1


def wrong_answer(m): #when wrong button clicked, ONLY FOR 1ST LEVEL
    
    def undo_wrong_answer() :
        # when try again clicked, returns to level
        oops.destroy()
        try_again.destroy()
        
    global oops
    global try_again
    #message for incorrect answer
    try_again= Button(master=lvl1_game, text=("Try again"), width=42, height=10, command=undo_wrong_answer, bg="grey", fg="black", font=("Times New Roman", 14))
    oops= Label(master=lvl1_game, text="Oops, that isn't a bird!" + "\n" + "Remember birds have feathers and beaks!", font=("Times New Roman", 14), width=42, height=15, fg="black")
    oops.place(x=0, y=0)
    try_again.place(x=0, y=250)

    

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
            widget.destroy() 
        ###
        global lvl1_summary
        lvl1_summary= Frame(root, width=800,  height=400, bg="light green")
        summary_screen1= Label(master=lvl1_summary, text="You've found the following Aves:" + list_correct_animals, fg="black", width=50, height=10, bg="grey")
        next_level= Button(master=lvl1_summary, text=("next level"), width=10, height=5, command=transition1)
        lvl1_summary.place(x=0, y=0)
        summary_screen1.place(x=250, y=150)
        next_level.place(x=700, y=300)
    
      

##


def Level1():
    for widget in root.winfo_children():
         widget.destroy() 
    
    global lvl1_game
    lvl1_game= Frame(root, width=800, height=400, bg="light green")

    #displaying options for lvl1
    #Macaw
    macaw_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\blue_macaw.jpg")
    macaw_CTK =  customtkinter.CTkImage(macaw_img,
                                        size=(130,110))
    macaw_button =  customtkinter.CTkButton(master=lvl1_game, image=macaw_CTK, text="Blue and Gold Macaw", compound="bottom",
                                        command=lambda m="Blue and Gold Macaw":correct_choice(m))
    #capybara
    capybara_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\capybara.jpeg")
    capybara_CTK =  customtkinter.CTkImage(capybara_img,
                                        size=(130,110))
    capybara_button =  customtkinter.CTkButton(master=lvl1_game, image=capybara_CTK, text="capybara", compound="bottom",
                                        command=lambda m="capybara":wrong_answer(m))
    #jaguar
    jaguar_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\jaguar.jpeg")
    jaguar_CTK =  customtkinter.CTkImage(jaguar_img,
                                        size=(130,110))
    jaguar_button =  customtkinter.CTkButton(master=lvl1_game, image=jaguar_CTK, text="jaguar", compound="bottom",
                                        command=lambda m="jaguar":wrong_answer(m))
    #poison dart frog
    PDfrog_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\poison-dart-frog.jpeg")
    PDfrog_CTK =  customtkinter.CTkImage(PDfrog_img,
                                        size=(130,110))
    PDfrog_button =  customtkinter.CTkButton(master=lvl1_game, image=PDfrog_CTK, text="poison dart frog", compound="bottom",
                                        command=lambda m="poison dart frog":wrong_answer(m))
    #Pantalón-de-Cuerno
    Pcuerno_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\Pantalón-de-Cuerno.jpg")
    Pcuerno_CTK =  customtkinter.CTkImage(Pcuerno_img,
                                        size=(130,110))
    Pcuerno_button =  customtkinter.CTkButton(master=lvl1_game, image=Pcuerno_CTK, text="Pantalón-de-Cuerno", compound="bottom",
                                        command=lambda m="Pantalón-de-Cuerno":correct_choice(m))
    #Red Howler Money
    RHMonkey_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\red-howler-monkey.jpeg")
    RHMonkey_CTK =  customtkinter.CTkImage(RHMonkey_img,
                                        size=(130,110))
    RHMonkey_button =  customtkinter.CTkButton(master=lvl1_game, image=RHMonkey_CTK, text="Red Howler Monkey", compound="bottom",
                                        command=lambda m="Red Howler Monkey":wrong_answer(m))
    #black capped squirrel monkey
    BCSMonkey_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\black-capped-squirrel-monkey.jpeg")
    BCSMonkey_CTK =  customtkinter.CTkImage(BCSMonkey_img,
                                        size=(130,110))
    BCSMonkey_button =  customtkinter.CTkButton(master=lvl1_game, image=BCSMonkey_CTK, text="Black Capped Squirrel", compound="bottom",
                                        command=lambda m="Black Capped Squirrel":wrong_answer(m))
    #green anaconda
    GAnaconda_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\green-anaconda.jpeg")
    GAnaconda_CTK =  customtkinter.CTkImage(GAnaconda_img,
                                        size=(130,110))
    GAnaconda_button =  customtkinter.CTkButton(master=lvl1_game, image=GAnaconda_CTK, text="Green Anaconda", compound="bottom",
                                        command=lambda m="Green Anaconda":wrong_answer(m))

    #Toucan-Collared-Aracari
    CAToucan_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\Toucan-Collared-Aracari.jpg")
    CAToucan_CTK =  customtkinter.CTkImage(CAToucan_img,
                                        size=(130,110))
    CAToucan_button =  customtkinter.CTkButton(master=lvl1_game, image=CAToucan_CTK, text="Toucan Collared Aracari", compound="bottom",
                                        command= (lambda m="Toucan Collared Aracari":correct_choice(m)))
    #displaying score and correct answers- lvl1
    global score1
    global animals_found1
    score1 = Label(lvl1_game, text="SCORE: ", font=(("Times New Roman"), 18))
    animals_found1 = Label(lvl1_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))

    #back option
    def back1_func():
        for widget in lvl1_game.winfo_children():
            widget.destroy() 
        start()

    
    back1= Button(master=lvl1_game, text=("back"), width=10, height=5, command=back1_func)
    lvl1_game.place(x=0, y=0)
    back1.place(x=700, y=300)
    score1.place(x=550, y=0)
    animals_found1.place(x=450, y=50)
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
         widget.destroy() 
    global instr_lvl1
    instr_lvl1=Frame(root, width=800, height=400, bg="light green")
    #display instructions for first level
    Amazon = Label(instr_lvl1, text="Welcome to the Amazon Rainforest!" + "\n"+ "We need to find 3 aves." +"\n" + "Remember, aves is the scientific name for birds." + "\n"+ "Birds have feathers and beaks and lay eggs.", font=("Times New Roman", 12), width=40)

    #continue button to start 1st level
    cont = Button(instr_lvl1, text="Continue", command=Level1)

    #collage of birds-illustration of what birds look like
    birds_collage_image = PIL.Image.open(r"D:\yr12\lvl-1-intro.gif")
    TK_birds_collage =  customtkinter.CTkImage(birds_collage_image,
        size=(400,400))
    birds_collage =  customtkinter.CTkLabel(master=instr_lvl1, image=TK_birds_collage, text="")
    instr_lvl1.place(x=0, y=0)
    birds_collage.place(x=400, y=0)
    cont.place(x=30, y=350)
    Amazon.place(x=30, y=100)


############
title_screen=Frame(root , width=800, height=400, bg="white")
begin = Button(title_screen, text="Begin", command=start)
intro = Label(title_screen, text="Animal Classification Game", height = 3, width=25, font=("Times New Roman", 18))

def introduction():
    title_screen.place(x=0, y=0)
    intro.place(x=250, y=150)
    begin.place(x=350, y=250)

introduction()

############




root.mainloop()