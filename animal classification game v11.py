
import PIL.Image
from PIL import ImageTk, Image
from tkinter import *
from tkinter import ttk

import customtkinter

root = Tk()
root.title('animal classification game')
root.geometry("800x400")



#all have to do with displaying results- common aspects of all levels
global points
global m
points=0
global list_correct_animals
list_correct_animals= ""

score = Label(root, text="SCORE: ", font=(("Times New Roman"), 18))
animals_found = Label(root, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))



#subprogram used to determine which button was clicked, and store the animal name
def which_button(m): #when correct button clicked, used to store list of correct animals so far
    global list_correct_animals
    #adding to list of correct animals
    list_correct_animals=list_correct_animals + "\n" + m

def wrong_answer(m): #when wrong button clicked, ONLY FOR 1ST LEVEL
    
    def undo_wrong_answer() :
        # when try again clicked, returns to level
        oops.destroy()
        try_again.destroy()
        
    global oops
    global try_again
    #message for incorrect answer
    oops= Label(master=lvl1_game, text=("Oops, that isn't a bird!" + "\n" + "Remember birds have feathers and beaks!")) #, width=800) #bg="grey")
    oops.place(x=0, y=0)
    try_again= Button(master=lvl1_game, text=("Try again"), width=10, height=5, command=undo_wrong_answer)
    try_again.place(x=700, y=350)

def correct_choice(): #refects correct choice on screen; increment score and adds to list of animals found--ONLY FOR 1ST LEVEL
    global points
    global score
    global animals_found
    global list_correct_animals
    #increments points and adds correct animal to list
    which_button(m)
    points=points+1
    if points==3: #end level if so
        points=0
        animals_found=""
        lvl1_game.place_forget()
        lvl1_summary.place(x=0, y=0)
    score.config(text="SCORE: "+ str(points))
    animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
    #when to move on to next level  

def correct_choice2(m):
    global points
    global score
    global animals_found
    #increments points and adds correct animal to list
    which_button(m)
    points=points+1
    if points>3:
        points=0
        animals_found=""
        lvl2_game.place_forget()
        lvl2_summary.place(x=0, y=0)
    score.config(text="SCORE: "+ str(points))
    animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
def wrong_answer2(m):
    global oops2
    global try_again2
    def undo_wrong_answer2() :
        # when try again clicked, returns to level
        oops2.destroy()
        try_again2.destroy() 
    #message for incorrect answer
    oops2= Label(master=lvl2_game, text=("Oops, that isn't a mammal!" + "\n" + "Remember mammals have hair or fur!")) #, width=800) #bg="grey")
    oops2.place(x=0, y=0)
    try_again2= Button(master=lvl2_game, text=("Try again"), width=10, height=5, command=undo_wrong_answer2)
    try_again2.place(x=700, y=350)  

def correct_choice3():
    global points
    global score
    global animals_found
    #increments points and adds correct animal to list
    points=points+1
    if points>3:
        points=0
        animals_found=""
        lvl3_game.place_forget()
        lvl3_summary.place(x=0, y=0)
    score.config(text="SCORE: "+ str(points))
    animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
def wrong_answer3(m):
    global oops3
    global try_again3
    def undo_wrong_answer3() :
        # when try again clicked, returns to level
        oops3.destroy()
        try_again3.destroy() 
    #message for incorrect answer
    oops3= Label(master=lvl3_game, text=("Oops, that isn't a fish!" + "\n" + "Remember fish have scales and live underwater!")) #, width=800) #bg="grey")
    oops3.place(x=0, y=0)
    try_again3= Button(master=lvl3_game, text=("Try again"), width=10, height=5, command=undo_wrong_answer3)
    try_again3.place(x=700, y=350)

def correct_choice4():
    global points
    global score
    global animals_found
    #increments points and adds correct animal to list
    points=points+1
    if points>3:
        points=0
        animals_found=""
        lvl4_game.place_forget()
        lvl4_summary.place(x=0, y=0)
    score.config(text="SCORE: "+ str(points))
    animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
def wrong_answer4(m):
    global oops4
    global try_again4
    def undo_wrong_answer4() :
        # when try again clicked, returns to level
        oops4.destroy()
        try_again4.destroy() 
    #message for incorrect answer
    oops4= Label(master=lvl4_game, text=("Oops, that isn't an amphibian!" + "\n" + "Remember amphibians have slimy skin and live around water!")) #, width=800) # ) #="grey")
    oops4.place(x=0, y=0)
    try_again4= Button(master=lvl4_game, text=("Try again"), width=10, height=5, command=undo_wrong_answer4)
    try_again4.place(x=700, y=350)

def correct_choice5():
    global points
    global score
    global animals_found
    #increments points and adds correct animal to list
    points=points+1
    if points>3:
        points=0
        animals_found=""
        lvl5_game.place_forget()
        lvl5_summary.place(x=0, y=0)
    score.config(text="SCORE: "+ str(points))
    animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
def wrong_answer5(m):
    global oops5
    global try_again5
    def undo_wrong_answer5() :
        # when try again clicked, returns to level
        oops5.destroy()
        try_again5.destroy() 
    #message for incorrect answer
    oops5= Label(master=lvl5_game, text=("Oops, that isn't a reptile!" + "\n" + "Remember reptiles have scaly skin!")) #, width=800,  ) #="grey")
    oops5.place(x=0, y=0)
    try_again5= Button(master=lvl5_game, text=("Try again"), width=10, height=5, command=undo_wrong_answer5)
    try_again5.place(x=700, y=350)

def correct_choice6():
    global points
    global score
    global animals_found
    #increments points and adds correct animal to list
    points=points+1
    if points>3:
        points=0
        animals_found=""
        lvl6_game.place_forget()
        lvl6_summary.place(x=0, y=0)
    score.config(text="SCORE: "+ str(points))
    animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
def wrong_answer6(m):
    global oops6
    global try_again6
    def undo_wrong_answer6() :
        # when try again clicked, returns to level
        oops6.destroy()
        try_again6.destroy() 
    #message for incorrect answer
    oops6= Label(master=lvl6_game, text=("Oops, that isn't an invertebrate!" + "\n" + "Remember invertebrates don't have a spine and are really tiny!")) #, width=800,  ) #="grey")
    oops3.place(x=0, y=0)
    try_again6= Button(master=lvl6_game, text=("Try again"), width=10, height=5, command=undo_wrong_answer6)
    try_again6.place(x=700, y=350)

###
title_screen=Frame(root) #, width=800,  ) #="white")

###
instr_lvl1=Frame(root) #, width=800,  ) #bg="light green")

def start():
    title_screen.place_forget()
    instr_lvl1.place(x=0, y=0)

begin = Button(title_screen, text="Begin", command=start)
begin.place(x=350, y=250)

###subprograms used to control what  Frame is displayed when
def introduction():
    title_screen.place(x=0, y=0)


intro = Label(title_screen, text="Animal Classification Game", height = 3, width=25, font=("Times New Roman", 18))
intro.place(x=250, y=150)

###
lvl1_game= Frame(root) #, width=800,  ) #bg="light green")

#displaying options for lvl1
#Macaw
macaw_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\blue_macaw.jpg")
macaw_CTK =  customtkinter.CTkImage(macaw_img,
                                    size=(130,110))
macaw_button =  customtkinter.CTkButton(master=lvl1_game, image=macaw_CTK, text="Blue and Gold Macaw", compound="bottom",
                                    command=lambda m="Blue and Gold Macaw":correct_choice(m))
macaw_button.place(x=0, y=0)
#capybara
capybara_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\capybara.jpeg")
capybara_CTK =  customtkinter.CTkImage(capybara_img,
                                    size=(130,110))
capybara_button =  customtkinter.CTkButton(master=lvl1_game, image=capybara_CTK, text="capybara", compound="bottom",
                                    command=lambda m="capybara":wrong_answer(m))
capybara_button.place(x=140, y=0)
#jaguar
jaguar_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\jaguar.jpeg")
jaguar_CTK =  customtkinter.CTkImage(jaguar_img,
                                    size=(130,110))
jaguar_button =  customtkinter.CTkButton(master=lvl1_game, image=jaguar_CTK, text="jaguar", compound="bottom",
                                    command=lambda m="jaguar":wrong_answer(m))
jaguar_button.place(x=280, y=0)
#poison dart frog
PDfrog_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\poison-dart-frog.jpeg")
PDfrog_CTK =  customtkinter.CTkImage(PDfrog_img,
                                    size=(130,110))
PDfrog_button =  customtkinter.CTkButton(master=lvl1_game, image=PDfrog_CTK, text="poison dart frog", compound="bottom",
                                    command=lambda m="poison dart frog":wrong_answer(m))
PDfrog_button.place(x=280, y=135)
#Pantalón-de-Cuerno
Pcuerno_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\Pantalón-de-Cuerno.jpg")
Pcuerno_CTK =  customtkinter.CTkImage(Pcuerno_img,
                                    size=(130,110))
Pcuerno_button =  customtkinter.CTkButton(master=lvl1_game, image=Pcuerno_CTK, text="Pantalón-de-Cuerno", compound="bottom",
                                    command=lambda m="Pantalón-de-Cuerno":correct_choice(m))
Pcuerno_button.place(x=140, y=135)
#Red Howler Money
RHMonkey_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\red-howler-monkey.jpeg")
RHMonkey_CTK =  customtkinter.CTkImage(RHMonkey_img,
                                    size=(130,110))
RHMonkey_button =  customtkinter.CTkButton(master=lvl1_game, image=RHMonkey_CTK, text="Red Howler Monkey", compound="bottom",
                                    command=lambda m="Red Howler Monkey":wrong_answer(m))
RHMonkey_button.place(x=0, y=135)
#black capped squirrel monkey
BCSMonkey_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\black-capped-squirrel-monkey.jpeg")
BCSMonkey_CTK =  customtkinter.CTkImage(BCSMonkey_img,
                                    size=(130,110))
BCSMonkey_button =  customtkinter.CTkButton(master=lvl1_game, image=BCSMonkey_CTK, text="Black Capped Squirrel", compound="bottom",
                                    command=lambda m="Black Capped Squirrel":wrong_answer(m))
BCSMonkey_button.place(x=0, y=260)
#green anaconda
GAnaconda_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\green-anaconda.jpeg")
GAnaconda_CTK =  customtkinter.CTkImage(GAnaconda_img,
                                    size=(130,110))
GAnaconda_button =  customtkinter.CTkButton(master=lvl1_game, image=GAnaconda_CTK, text="Green Anaconda", compound="bottom",
                                    command=lambda m="Green Anaconda":wrong_answer(m))
GAnaconda_button.place(x=140, y=260)

#Toucan-Collared-Aracari
CAToucan_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\Toucan-Collared-Aracari.jpg")
CAToucan_CTK =  customtkinter.CTkImage(CAToucan_img,
                                    size=(130,110))
CAToucan_button =  customtkinter.CTkButton(master=lvl1_game, image=CAToucan_CTK, text="Toucan Collared Aracari", compound="bottom",
                                    command= (lambda m="Toucan Collared Aracari":correct_choice(m)))
CAToucan_button.place(x=280, y=260)
#displaying score and correct answers- lvl1
score = Label(lvl1_game, text="SCORE: ", font=(("Times New Roman"), 18))
animals_found = Label(lvl1_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))
score.place(x=550, y=0)
animals_found.place(x=450, y=50)



#display instructions for first level
Amazon = Label(instr_lvl1, text="Welcome to the Amazon Rainforest!" + "\n"+ "We need to find 3 aves." +"\n" + "Remember, aves is the scientific name for birds." + "\n"+ "Birds have feathers and beaks and lay eggs.", font=("Times New Roman", 12), width=40)
Amazon.place(x=30, y=100)

def Level1():
    title_screen.place_forget()
    instr_lvl1.place_forget()
    instr_lvl2.place_forget()
    instr_lvl3.place_forget()
    instr_lvl4.place_forget()
    instr_lvl5.place_forget()
    instr_lvl6.place_forget()
    lvl2_game.place_forget()
    lvl3_game.place_forget()
    lvl4_game.place_forget()
    lvl5_game.place_forget()
    lvl6_game.place_forget()
    lvl1_summary.place_forget()
    lvl2_summary.place_forget()
    lvl3_summary.place_forget()
    lvl4_summary.place_forget()
    lvl5_summary.place_forget()
    lvl6_summary.place_forget()
    lvl1_game.place(x=0, y=0)

def Level2():
    title_screen.place_forget()
    instr_lvl1.place_forget()
    instr_lvl2.place_forget()
    # instr_lvl3.place_forget()
    # instr_lvl4.place_forget()
    # instr_lvl5.place_forget()
    # instr_lvl6.place_forget()
    lvl1_game.place_forget()
    # lvl3_game.place_forget()
    # lvl4_game.place_forget()
    # lvl5_game.place_forget()
    # lvl6_game.place_forget()
    lvl1_summary.place_forget()
    # lvl2_summary.place_forget()
    # lvl3_summary.place_forget()
    # lvl4_summary.place_forget()
    # lvl5_summary.place_forget()
    # lvl6_summary.place_forget()
    lvl2_game.place(x=0, y=0)

#continue button to start 1st level
cont = Button(instr_lvl1, text="Continue", command=Level1)
cont.place(x=30, y=350)

#collage of birds-illustration of what birds look like
birds_collage_image = PIL.Image.open(r"D:\\yr12\\lvl-1-intro.gif")
TK_birds_collage =  customtkinter.CTkImage(birds_collage_image,
    size=(400,400))
birds_collage =  customtkinter.CTkLabel(master=instr_lvl1, image=TK_birds_collage, text="")
birds_collage.place(x=400, y=0)

###
instr_lvl2= Frame(root) #, width=800,  ) #bg="#deb878", )

#display instructions for second level
Savanna = Label(instr_lvl2, text="Next we are going to look for " + "\n"+ "mammals in the African Savanna" +"\n" + "Mammals are warm blooded, have hair or fur " + "\n"+ "and have very complex brains.", font=("Times New Roman", 12), width=40)
Savanna.place(x=30, y=100)
#continue button to start 2nd level
cont2 =  Button(instr_lvl2, text="Continue", command=Level2)
cont2.place(x=30, y=350)
#collage of mammals- to refer to how mammals look
mammals_collage_image = PIL.Image.open(r"D:\yr12\project pics\level 2\Mammal_intro.jpg")
TK_mammals_collage =  customtkinter.CTkImage(mammals_collage_image,
    size=(400,400))
mammals_collage =  customtkinter.CTkLabel(master=instr_lvl2, image=TK_mammals_collage)
mammals_collage.place(x=400, y=0)


def transition1():
    list_correct_animals=""
    title_screen.place_forget()
    instr_lvl1.place_forget()
    #instr_lvl3.place_forget()
    # instr_lvl4.place_forget()
    # instr_lvl5.place_forget()
    # instr_lvl6.place_forget()
    # lvl1_game.place_forget()
    # lvl2_game.place_forget()
    # lvl3_game.place_forget()
    # lvl4_game.place_forget()
    # lvl5_game.place_forget()
    # lvl6_game.place_forget()
    # lvl1_summary.place_forget()
    # lvl2_summary.place_forget()
    # lvl3_summary.place_forget()
    # lvl4_summary.place_forget()
    # lvl5_summary.place_forget()
    # lvl6_summary.place_forget()
    instr_lvl2.place(x=0, y=0)

###
lvl1_summary= Frame(root) #, width=800,  ) #bg="light green")
summary_screen1= Label(master=lvl1_summary, text=("You've found the following Aves" + list_correct_animals)) #, width=800,  ) #bg="grey")
summary_screen1.place(x=0, y=0)
next_level= Button(master=lvl1_summary, text=("next level"), width=10, height=5, command=transition1())
next_level.place(x=700, y=350)


###
lvl2_game= Frame(root) #, width=800,  ) #bg="#deb878")
#displaying options
#cobra
Cobra_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\cobra.jpg")
cobra_CTK =  customtkinter.CTkImage(Cobra_img,
                                size=(130,110))
cobra_button =  customtkinter.CTkButton(master=lvl2_game, image=cobra_CTK, text="cobra", compound="bottom",
                                    command=lambda m="cobra":wrong_answer2(m))
cobra_button.place(x=0, y=0)
#aardvark
aardvark_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\mammals\\aardvark.jpg")
aardvark_CTK =  customtkinter.CTkImage(aardvark_img,
                                size=(130,110))
aardvark_button =  customtkinter.CTkButton(master=lvl2_game, image=aardvark_CTK, text="aardvark", compound="bottom",
                                    command=lambda m="aardvark":correct_choice2(m))
aardvark_button.place(x=140, y=0)
#african_elephant
african_elephant_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\mammals\\african_elephant.jpg")
african_elephant_CTK =  customtkinter.CTkImage(african_elephant_img,
                                size=(130,110))
african_elephant_button =  customtkinter.CTkButton(master=lvl2_game, image=african_elephant_CTK, text="african elephant", compound="bottom",
                                    command=lambda m="african elephant":correct_choice2(m))
african_elephant_button.place(x=280, y=0)
#hornbill
hornbill_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\hornbill.jpg")
hornbill_CTK =  customtkinter.CTkImage(hornbill_img,
                                size=(130,110))
hornbill_button =  customtkinter.CTkButton(master=lvl2_game, image=hornbill_CTK, text="hornbill", compound="bottom",
                                    command=lambda m="hornbill":wrong_answer2(m))
hornbill_button.place(x=280, y=135)
#scorpion
scorpion_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\scorpion.jpg")
scorpion_CTK =  customtkinter.CTkImage(scorpion_img,
                                size=(130,110))
scorpion_button =  customtkinter.CTkButton(master=lvl2_game, image=scorpion_CTK, text="scorpion", compound="bottom",
                                    command=lambda m="scorpion":wrong_answer2(m))
scorpion_button.place(x=140, y=135)
#rhinoceros
rhinoceros_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\mammals\\rhinoceros.jpg")
rhinoceros_CTK =  customtkinter.CTkImage(rhinoceros_img,
                                size=(130,110))
rhinoceros_button =  customtkinter.CTkButton(master=lvl2_game, image=rhinoceros_CTK, text="rhinoneros", compound="bottom",
                                    command=lambda m="rhinoceros":correct_choice2(m))
rhinoceros_button.place(x=0, y=135)
#ostrich
ostrich_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\ostrich.jpg")
ostrich_CTK =  customtkinter.CTkImage(ostrich_img,
                                size=(130,110))
ostrich_button =  customtkinter.CTkButton(master=lvl2_game, image=ostrich_CTK, text="ostrich", compound="bottom",
                                    command=lambda m="ostrich":wrong_answer2(m))
ostrich_button.place(x=0, y=260)
#dung beetle
dung_beetle_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\dung-beetle.jpg")
dung_beetle_CTK =  customtkinter.CTkImage(dung_beetle_img,
                                size=(130,110))
dung_beetle_button =  customtkinter.CTkButton(master=lvl2_game, image=dung_beetle_CTK, text="dung beetle", compound="bottom",
                                    command=lambda m="dung beetle":wrong_answer2(m))
dung_beetle_button.place(x=140, y=260)

#african spurred tortoise
ASTortoise_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\african-spurred-tortoise.jpg")
ASTortoise_CTK =  customtkinter.CTkImage(ASTortoise_img,
                                size=(130,110))
ASTortoise_button =  customtkinter.CTkButton(master=lvl2_game, image=ASTortoise_CTK, text="african spurred tortoise", compound="bottom",
                                    command= (lambda m="african spurred tortoise":wrong_answer2(m)))
ASTortoise_button.place(x=280, y=260)
#results
score = Label(lvl2_game, text="SCORE: ", font=(("Times New Roman"), 18))
animals_found = Label(lvl2_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))
score.place(x=550, y=0)
animals_found.place(x=450, y=50)
#back option
back2=  Button(master=lvl2_game, text=("back"), width=10, height=5, command=transition1())
back2.place(x=700, y=350)

###
lvl3_game= Frame(root) #, width=800,  ) #bg="light blue")
#displaying options
#clownfish
Cfish_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\fish\\clownfish.jpg")
Cfish_CTK =  customtkinter.CTkImage(Cfish_img,
                                    size=(130,110))
Cfish_button =  customtkinter.CTkButton(master=lvl3_game, image=Cfish_CTK, text="clownfish", compound="bottom",
                                    command=lambda m="clownfish":correct_choice3(m))
Cfish_button.place(x=0, y=0)
#blanket octapus
Boctapus_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\blanket-octopus.jpg")
Boctapus_CTK =  customtkinter.CTkImage(Boctapus_img,
                                    size=(130,110))
Boctapus_button =  customtkinter.CTkButton(master=lvl3_game, image=Boctapus_CTK, text="blanket octapus", compound="bottom",
                                    command=lambda m="blanket octapus":wrong_answer3(m))
Boctapus_button.place(x=140, y=0)
#dugong
dugong_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\dugong.jpg")
dugong_CTK =  customtkinter.CTkImage(dugong_img,
                                    size=(130,110))
dugong_button =  customtkinter.CTkButton(master=lvl3_game, image=dugong_CTK, text="dugong", compound="bottom",
                                    command=lambda m="dugong":wrong_answer3(m))
dugong_button.place(x=280, y=0)
#green turtle
Gturtle_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\fish\\green-turtle.jpg")
Gturtle_CTK =  customtkinter.CTkImage(Gturtle_img,
                                    size=(130,110))
Gturtle_button =  customtkinter.CTkButton(master=lvl3_game, image=Gturtle_CTK, text="green turtle", compound="bottom",
                                    command=lambda m="green turtle":correct_choice3(m))
Gturtle_button.place(x=280, y=135)
#manta ray
Mray_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\fish\\manta-ray.jpg")
Mray_CTK =  customtkinter.CTkImage(Mray_img,
                                    size=(130,110))
Mray_button =  customtkinter.CTkButton(master=lvl3_game, image=Mray_CTK, text="manta ray", compound="bottom",
                                    command=lambda m="manta ray":correct_choice3(m))
Mray_button.place(x=140, y=135)
#giant clam
Gclam_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\giant-clam.jpg")
Gclam_CTK =  customtkinter.CTkImage(Gclam_img,
                                    size=(130,110))
Gclam_button =  customtkinter.CTkButton(master=lvl3_game, image=Gclam_CTK, text="giant clam", compound="bottom",
                                    command=lambda m="giant clam":wrong_answer3(m))
Gclam_button.place(x=0, y=135)
#humpback whale
HWhale_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\humpback-whale.jpg")
HWhale_CTK =  customtkinter.CTkImage(HWhale_img,
                                    size=(130,110))
HWhale_button =  customtkinter.CTkButton(master=lvl3_game, image=HWhale_CTK, text="Humpback Whale", compound="bottom",
                                    command=lambda m="Humpback Whale":wrong_answer3(m))
HWhale_button.place(x=0, y=260)
#jellyfish
jellyfish_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\jellyfish.jpg")
jellyfish_CTK =  customtkinter.CTkImage(jellyfish_img,
                                    size=(130,110))
jellyfish_button =  customtkinter.CTkButton(master=lvl3_game, image=jellyfish_CTK, text="jellyfish", compound="bottom",
                                    command=lambda m="jellyfish":wrong_answer3(m))
jellyfish_button.place(x=140, y=260)
#mantis shrimp
MShrimp_img = PIL.Image.open("D:\\yr12\\project pics\\level 3\\other\\mantis-shrimp.jpg")
MShrimp_CTK =  customtkinter.CTkImage(MShrimp_img,
                                    size=(130,110))
MShrimp_button =  customtkinter.CTkButton(master=lvl3_game, image=MShrimp_CTK, text="mantis shrimp", compound="bottom",
                                    command= (lambda m="mantis shrimp":wrong_answer3(m)))
MShrimp_button.place(x=280, y=260)
score = Label(lvl3_game, text="SCORE: ", font=(("Times New Roman"), 18))
animals_found = Label(lvl3_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))
score.place(x=550, y=0)
animals_found.place(x=450, y=50)

###
lvl2_summary= Frame(root) #, width=800,  ) #bg="#deb878")
summary_screen2= Label(master=lvl2_summary, text=("You've found the following mammals" + list_correct_animals)) #, width=800,  ) #bg="grey")
summary_screen2.place(x=0, y=0)
next_level2=Button(master=lvl2_summary, text=("next level"), width=10, height=5, command=transition1())
next_level2.place(x=700, y=350)

def Level3():
    title_screen.place_forget()
    instr_lvl1.place_forget()
    instr_lvl2.place_forget()
    instr_lvl3.place_forget()
    # instr_lvl4.place_forget()
    # instr_lvl5.place_forget()
    # instr_lvl6.place_forget()
    lvl1_game.place_forget()
    lvl2_game.place_forget()
    # lvl4_game.place_forget()
    # lvl5_game.place_forget()
    # lvl6_game.place_forget()
    lvl1_summary.place_forget()
    lvl2_summary.place_forget()
    # lvl3_summary.place_forget()
    # lvl4_summary.place_forget()
    # lvl5_summary.place_forget()
    # lvl6_summary.place_forget()
    lvl3_game.place(x=0, y=0)


###
instr_lvl3= Frame(root) #, width=800,  ) #bg="light blue")
#display instructions for 3rd level
#great barrier reef
GBR = Label(instr_lvl3, text="Next we are going to look for " + "\n"+ "fish in the Great Barrier Reef" +"\n" + "Fish have scales and live underwater.", font=("Times New Roman", 12), width=40)
GBR.place(x=30, y=100)
#continue button to start 3rd level
cont3 =  Button(instr_lvl3, text="Continue", command=Level3)
cont3.place(x=30, y=350)
#collage of fish
fish_collage_image = PIL.Image.open(r"D:\yr12\project pics\level 3\fish-montage.jpg")
TK_fish_collage =   customtkinter.CTkImage(fish_collage_image,
    size=(400,400))
fish_collage =    customtkinter.CTkLabel(master=instr_lvl3, image=TK_fish_collage)
fish_collage.place(x=400, y=0)

def transition2():
    list_correct_animals=""
    title_screen.place_forget()
    instr_lvl1.place_forget()
    instr_lvl2.place_forget()
    # instr_lvl4.place_forget()
    # instr_lvl5.place_forget()
    # instr_lvl6.place_forget()
    lvl1_game.place_forget()
    lvl2_game.place_forget()
    # lvl3_game.place_forget()
    # lvl4_game.place_forget()
    # lvl5_game.place_forget()
    # lvl6_game.place_forget()
    lvl1_summary.place_forget()
    lvl2_summary.place_forget()
    # lvl3_summary.place_forget()
    # lvl4_summary.place_forget()
    # lvl5_summary.place_forget()
    # lvl6_summary.place_forget()
    instr_lvl3.place(x=0, y=0)

#back option
back3=  Button(master=lvl3_game, text=("back"), width=10, height=5, command=transition2())
back3.place(x=700, y=350)

###
lvl4_game= Frame(root) #, width=800,  ) #bg="salmon")
#displaying options
#Clouded Leopard
CLeopard_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\clouded-leopard.jpg")
CLeopard_CTK =  customtkinter.CTkImage(CLeopard_img,
                                    size=(130,110))
CLeopard_button =  customtkinter.CTkButton(master=lvl4_game, image=CLeopard_CTK, text="Clouded Leopard", compound="bottom",
                                    command=lambda m="Clouded Leopard":wrong_answer4(m))
CLeopard_button.place(x=0, y=0)
#red giant flying squirrel
RGFSquirrel_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\red-giant-flying-squirrel.jpg")
RGFSquirrel_CTK =  customtkinter.CTkImage(RGFSquirrel_img,
                                    size=(130,110))
RGFSquirrel_button =  customtkinter.CTkButton(master=lvl4_game, image=RGFSquirrel_CTK, text="red giant flying squirrel", compound="bottom",
                                    command=lambda m="red giant flying squirrel":wrong_answer4(m))
RGFSquirrel_button.place(x=140, y=0)
#Malay Civet
MCivet_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Malay-civet.jpg")
MCivet_CTK =  customtkinter.CTkImage(MCivet_img,
                                    size=(130,110))
MCivet_button =  customtkinter.CTkButton(master=lvl4_game, image=MCivet_CTK, text="Malay Civet", compound="bottom",
                                    command=lambda m="Malay Civet":wrong_answer4(m))
MCivet_button.place(x=280, y=0)
#Proboscis monkey
PMonkey_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Proboscis-monkey.jpg")
PMonkey_CTK =  customtkinter.CTkImage(PMonkey_img,
                                    size=(130,110))
PMonkey_button =  customtkinter.CTkButton(master=lvl4_game, image=PMonkey_CTK, text="Proboscis monkey", compound="bottom",
                                    command=lambda m="Proboscis monkey":wrong_answer4(m))
PMonkey_button.place(x=280, y=135)
#Wallaces flying frog
WFFrog_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\amphibians\\Wallaces-flying-frog.jpg")
WFFrog_CTK =  customtkinter.CTkImage(WFFrog_img,
                                    size=(130,110))
WFFrog_button =  customtkinter.CTkButton(master=lvl4_game, image=WFFrog_CTK, text="Wallaces Flying Frog", compound="bottom",
                                    command=lambda m="Wallaces Flying Frog":correct_choice4(m))
WFFrog_button.place(x=140, y=135)
#orangutan
orangutan_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Orangutan.jpg")
orangutan_CTK =  customtkinter.CTkImage(orangutan_img,
                                    size=(130,110))
orangutan_button =  customtkinter.CTkButton(master=lvl4_game, image=orangutan_CTK, text="orangutan", compound="bottom",
                                    command=lambda m="orangutan":wrong_answer4(m))
orangutan_button.place(x=0, y=135)

#jade tree frog
JTFrog_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\amphibians\\jade-tree-frog.jpg")
JTFrog_CTK =  customtkinter.CTkImage(JTFrog_img,
                                    size=(130,110))
JTFrog_button =  customtkinter.CTkButton(master=lvl4_game, image=JTFrog_CTK, text="jade tree frog", compound="bottom",
                                    command=lambda m="jade tree frog":correct_choice4(m))
JTFrog_button.place(x=0, y=260)

#Pygmy elephant
PElephant_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\other\\Pygmy-Elephant.jpg")
PElephant_CTK =  customtkinter.CTkImage(PElephant_img,
                                    size=(130,110))
PElephant_button =  customtkinter.CTkButton(master=lvl4_game, image=PElephant_CTK, text="Pygmy Elephant", compound="bottom",
                                    command=lambda m="Pygmy Elephant":wrong_answer4(m))
PElephant_button.place(x=140, y=260)

#BFHFrog
BFHFrog_img = PIL.Image.open("D: \\yr12\\project pics\\level 4\\amphibians\\bornean-flat-headed-frog.jpg")
BFHFrog_CTK =  customtkinter.CTkImage(BFHFrog_img,
                                    size=(130,110))
BFHFrog_button =  customtkinter.CTkButton(master=lvl4_game, image=BFHFrog_CTK, text="bornean flat headed frog", compound="bottom",
                                    command= (lambda m="bornean flat headed frog":correct_choice4(m)))
BFHFrog_button.place(x=280, y=260)
#results
score = Label(lvl4_game, text="SCORE: ", font=(("Times New Roman"), 18))
animals_found = Label(lvl4_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))
score.place(x=550, y=0)
animals_found.place(x=450, y=50)


###
lvl3_summary= Frame(root) #, width=800,  ) #bg="light blue")
summary_screen3= Label(master=lvl3_summary, text=("You've found the following fish" + list_correct_animals)) #, width=800,  ) #bg="grey")
summary_screen3.place(x=0, y=0)

def Level4():
    title_screen.place_forget()
    instr_lvl1.place_forget()
    instr_lvl2.place_forget()
    instr_lvl3.place_forget()
    instr_lvl4.place_forget()
    # instr_lvl5.place_forget()
    # instr_lvl6.place_forget()
    lvl1_game.place_forget()
    lvl2_game.place_forget()
    lvl3_game.place_forget()
    # lvl5_game.place_forget()
    # lvl6_game.place_forget()
    lvl1_summary.place_forget()
    lvl2_summary.place_forget()
    lvl3_summary.place_forget()
    # lvl4_summary.place_forget()
    # lvl5_summary.place_forget()
    # lvl6_summary.place_forget()
    lvl4_game.place(x=0, y=0)

###
instr_lvl4= Frame(root) #, width=800,  ) #bg="salmon")
#display instructions for 4th level
BRF = Label(instr_lvl4, text="Next we are going to look for " + "\n"+ "amphibians in the Borneo Rainforest!" +"\n" + "Amphibians have slimy skin and live around water.", font=("Times New Roman", 12), width=40)
BRF.place(x=30, y=100)
#continue button to start 4th level
cont4 =  Button(instr_lvl4, text="Continue", command=Level4)
cont4.place(x=30, y=350)
#collage of amphibians
amphibians_collage_image = PIL.Image.open("D:\\yr12\\project pics\\level 4\\amphibians.jpg")
TK_amphibians_collage =  customtkinter.CTkImage(amphibians_collage_image,
    size=(400,400))
amphibians_collage =  customtkinter.CTkLabel(master=instr_lvl4, image=TK_amphibians_collage)
amphibians_collage.place(x=400, y=0)


def transition3():
    list_correct_animals=""
    title_screen.place_forget()
    instr_lvl1.place_forget()
    instr_lvl2.place_forget()
    instr_lvl3.place_forget()
    # instr_lvl5.place_forget()
    # instr_lvl6.place_forget()
    lvl1_game.place_forget()
    lvl2_game.place_forget()
    lvl3_game.place_forget()
    # lvl4_game.place_forget()
    # lvl5_game.place_forget()
    # lvl6_game.place_forget()
    lvl1_summary.place_forget()
    lvl2_summary.place_forget()
    lvl3_summary.place_forget()
    # lvl4_summary.place_forget()
    # lvl5_summary.place_forget()
    # lvl6_summary.place_forget()
    instr_lvl4.place(x=0, y=0)

next_level3= Button(master=lvl3_summary, text=("next level"), width=10, height=5, command=transition3())
next_level3.place(x=700, y=350)

def Level5():
    title_screen.place_forget()
    instr_lvl1.place_forget()
    instr_lvl2.place_forget()
    instr_lvl3.place_forget()
    instr_lvl4.place_forget()
    instr_lvl5.place_forget()
    #instr_lvl6.place_forget()
    lvl1_game.place_forget()
    lvl2_game.place_forget()
    lvl3_game.place_forget()
    lvl4_game.place_forget()
    #lvl6_game.place_forget()
    lvl1_summary.place_forget()
    lvl2_summary.place_forget()
    lvl3_summary.place_forget()
    lvl4_summary.place_forget()
    # lvl5_summary.place_forget()
    # lvl6_summary.place_forget()    
    lvl5_game.place(x=0, y=0)

#back option
back4= Button(master=lvl4_game, text=("back"), width=10, height=5, command=transition3())
back4.place(x=700, y=350)


###
lvl5_game= Frame(root) #, width=800,  ) #bg="light yellow")
#displaying options
#Sand Goanna
SGoanna_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\reptiles\\sand-goanna.jpg")
SGoanna_CTK =  customtkinter.CTkImage(SGoanna_img,
                                    size=(130,110))
SGoanna_button =  customtkinter.CTkButton(master=lvl5_game, image=SGoanna_CTK, text="Sand Goanna", compound="bottom",
                                    command=lambda m="Sand Goanna":correct_choice5(m))
SGoanna_button.place(x=0, y=0)
#Throny Devil
TDevil_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\reptiles\\throny-devil.jpg")
TDevil_CTK =  customtkinter.CTkImage(TDevil_img,
                                    size=(130,110))
TDevil_button =  customtkinter.CTkButton(master=lvl5_game, image=TDevil_CTK, text="Throny Devil", compound="bottom",
                                    command=lambda m="Throny Devil":correct_choice5(m))
TDevil_button.place(x=140, y=0)
#dingo
dingo_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\dingo.jpg")
dingo_CTK =  customtkinter.CTkImage(dingo_img,
                                    size=(130,110))
dingo_button =  customtkinter.CTkButton(master=lvl5_game, image=dingo_CTK, text="dingo", compound="bottom",
                                    command=lambda m="dingo":wrong_answer5(m))
dingo_button.place(x=280, y=0)
#Australian Feral Camel
AFCamel_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\australian-feral-camel.jpg")
AFCamel_CTK =  customtkinter.CTkImage(AFCamel_img,
                                    size=(130,110))
AFCamel_button =  customtkinter.CTkButton(master=lvl5_game, image=AFCamel_CTK, text="Australian Feral Camel", compound="bottom",
                                    command=lambda m="Australian Feral Camel":wrong_answer5(m))
AFCamel_button.place(x=280, y=135)
#Frill Neck Lizard
FNLizard_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\reptiles\\frill-neck-lizard.jpg")
FNLizard_CTK =  customtkinter.CTkImage(FNLizard_img,
                                    size=(130,110))
FNLizard_button =  customtkinter.CTkButton(master=lvl5_game, image=FNLizard_CTK, text="Frill Neck Lizard", compound="bottom",
                                    command=lambda m="Frill Neck Lizard":correct_choice5(m))
FNLizard_button.place(x=140, y=135)
#Stimson's Python
SPython_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\stimson's-python.jpg")
SPython_CTK =  customtkinter.CTkImage(SPython_img,
                                    size=(130,110))
SPython_button =  customtkinter.CTkButton(master=lvl5_game, image=SPython_CTK, text="Stimson's Python", compound="bottom",
                                    command=lambda m="Stimson's Python":wrong_answer5(m))
SPython_button.place(x=0, y=135)
#Quokka
quokka_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\quokka.jpg")
quokka_CTK =  customtkinter.CTkImage(quokka_img,
                                    size=(130,110))
quokka_button =  customtkinter.CTkButton(master=lvl5_game, image=quokka_CTK, text="Quokka", compound="bottom",
                                    command=lambda m="Quokka":wrong_answer5(m))
quokka_button.place(x=0, y=260)
#kangaroo
kangaroo_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\kangaroo.jpg")
kangaroo_CTK =  customtkinter.CTkImage(kangaroo_img,
                                    size=(130,110))
kangaroo_button =  customtkinter.CTkButton(master=lvl5_game, image=kangaroo_CTK, text="kangaroo", compound="bottom",
                                    command=lambda m="kangaroo":wrong_answer5(m))
kangaroo_button.place(x=140, y=260)

#Kookaburra
kookaburra_img = PIL.Image.open("D:\\yr12\\project pics\\level 5\\other\\kookaburra.jpg")
kookaburra_CTK =  customtkinter.CTkImage(kookaburra_img,
                                    size=(130,110))
kookaburra_button =  customtkinter.CTkButton(master=lvl5_game, image=kookaburra_CTK, text="Kookaburra", compound="bottom",
                                    command= (lambda m="Kookaburra":wrong_answer5(m)))
kookaburra_button.place(x=280, y=260)
#results
score = Label(lvl4_game, text="SCORE: ", font=(("Times New Roman"), 18))
animals_found = Label(lvl4_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))
score.place(x=550, y=0)
animals_found.place(x=450, y=50)
#back option
back5= Button(master=lvl5_game, text=("back"), width=10, height=5, command=Level4())
back5.place(x=700, y=350)

###
lvl6_game= Frame(root) #, width=800,  ) #bg="lavender")
#displaying options
#Eastern Cottontail
ECottontail_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\eastern-cottontail.jpg")
ECottontail_CTK =  customtkinter.CTkImage(ECottontail_img,
                                    size=(130,110))
ECottontail_button =  customtkinter.CTkButton(master=lvl6_game, image=ECottontail_CTK, text="Eastern Cottontail", compound="bottom",
                                    command=lambda m="Eastern Cottontail":wrong_answer6(m))
ECottontail_button.place(x=0, y=0)
#Field Mouse
FMouse_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\field-mouse.jpg")
FMouse_CTK =  customtkinter.CTkImage(FMouse_img,
                                    size=(130,110))
FMouse_button =  customtkinter.CTkButton(master=lvl6_game, image=FMouse_CTK, text="Field Mouse", compound="bottom",
                                    command=lambda m="Field Mouse":wrong_answer6(m))
FMouse_button.place(x=140, y=0)
#earthworm
earthworm_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\earthworm.jpg")
earthworm_CTK =  customtkinter.CTkImage(earthworm_img,
                                    size=(130,110))
earthworm_button =  customtkinter.CTkButton(master=lvl6_game, image=earthworm_CTK, text="earthworm", compound="bottom",
                                    command=lambda m="earthworm":correct_choice6(m))
earthworm_button.place(x=280, y=0)
#Garter Snake
GSnake_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\garter-snake.jpg")
GSnake_CTK =  customtkinter.CTkImage(GSnake_img,
                                    size=(130,110))
GSnake_button =  customtkinter.CTkButton(master=lvl6_game, image=GSnake_CTK, text="Garter Snake", compound="bottom",
                                    command=lambda m="Garter Snake":wrong_answer6(m))
GSnake_button.place(x=280, y=135)
#German Shephard
GShephard_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\german-shephard.jpg")
GShephard_CTK =  customtkinter.CTkImage(GShephard_img,
                                    size=(130,110))
GShephard_button =  customtkinter.CTkButton(master=lvl6_game, image=GShephard_CTK, text="German Shephard", compound="bottom",
                                    command=lambda m="German Shephard":wrong_answer6(m))
GShephard_button.place(x=140, y=135)
#ladybug
ladybug_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\ladybug.jpg")
ladybug_CTK =  customtkinter.CTkImage(ladybug_img,
                                    size=(130,110))
ladybug_button =  customtkinter.CTkButton(master=lvl6_game, image=ladybug_CTK, text="ladybug", compound="bottom",
                                    command=lambda m="ladybug":correct_choice6(m))
ladybug_button.place(x=0, y=135)
#Monarch Butterfly
MButterfly_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\monarch-butterfly.jpg")
MButterfly_CTK =  customtkinter.CTkImage(MButterfly_img,
                                    size=(130,110))
MButterfly_button =  customtkinter.CTkButton(master=lvl6_game, image=MButterfly_CTK, text="Monarch Butterfly", compound="bottom",
                                    command=lambda m="Monarch Butterfly":correct_choice6(m))
MButterfly_button.place(x=0, y=260)
#honeyeater
honeyeater_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\honeyeater.jpg")
honeyeater_CTK =  customtkinter.CTkImage(honeyeater_img,
                                    size=(130,110))
honeyeater_button =  customtkinter.CTkButton(master=lvl6_game, image=honeyeater_CTK, text="honeyeater", compound="bottom",
                                    command=lambda m="honeyeater":wrong_answer6(m))
honeyeater_button.place(x=140, y=260)
#Water Skink
WSkink_img = PIL.Image.open("D:\\yr12\\project pics\\level 6\\inver\\water-skink.jpg")
WSkink_CTK =  customtkinter.CTkImage(WSkink_img,
                                    size=(130,110))
WSkink_button =  customtkinter.CTkButton(master=lvl6_game, image=WSkink_CTK, text="Water Skink", compound="bottom",
                                    command= (lambda m="Water Skink":wrong_answer6(m)))
WSkink_button.place(x=280, y=260)
#results
score = Label(lvl5_game, text="SCORE: ", font=(("Times New Roman"), 18))
animals_found = Label(lvl5_game, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))
score.place(x=550, y=0)
animals_found.place(x=450, y=50)

###
instr_lvl5= Frame(root) #) #, width=800,  ) #bg="light yellow")
#display instructions for 5th level
outback = Label(instr_lvl5, text="Next we are going to look for " + "\n"+ "reptiles in the outback!" +"\n" + "Reptiles have scaly skin and lay eggs.", font=("Times New Roman", 12), width=40)
outback.place(x=30, y=100)
#continue button to start 5th level
cont5 =  Button(instr_lvl5, text="Continue", command=Level5)
cont5.place(x=30, y=350)
#collage of reptiles
reptiles_collage_image = PIL.Image.open("D:\\yr12\\project pics\\level 5\\Reptiles.jpg")
TK_reptiles_collage =   customtkinter.CTkImage(reptiles_collage_image,
    size=(400,400))
reptiles_collage =   customtkinter.CTkLabel(master=instr_lvl5, image=TK_reptiles_collage)
reptiles_collage.place(x=400, y=0)

def transition4():
    list_correct_animals=""
    title_screen.place_forget()
    instr_lvl1.place_forget()
    instr_lvl2.place_forget()
    instr_lvl3.place_forget()
    instr_lvl4.place_forget()
    # instr_lvl6.place_forget()
    lvl1_game.place_forget()
    lvl2_game.place_forget()
    lvl3_game.place_forget()
    lvl4_game.place_forget()
    # lvl5_game.place_forget()
    # lvl6_game.place_forget()
    lvl1_summary.place_forget()
    lvl2_summary.place_forget()
    lvl3_summary.place_forget()
    lvl4_summary.place_forget()
    # lvl5_summary.place_forget()
    # lvl6_summary.place_forget()
    instr_lvl5.place(x=0, y=0)


###
lvl4_summary= Frame(root) #, width=800,  ) #bg="salmon")
summary_screen4= Label(master=lvl4_summary, text=("You've found the following amphibians" + list_correct_animals)) #, width=800,  ) #bg="grey")
summary_screen4.place(x=0, y=0)
next_level4= Button(master=lvl4_summary, text=("next level"), width=10, height=5, command=transition4())
next_level4.place(x=700, y=350)

def Level6():
    title_screen.place_forget()
    instr_lvl1.place_forget()
    instr_lvl2.place_forget()
    instr_lvl3.place_forget()
    instr_lvl4.place_forget()
    instr_lvl5.place_forget()
    instr_lvl6.place_forget()
    lvl1_game.place_forget()
    lvl2_game.place_forget()
    lvl3_game.place_forget()
    lvl4_game.place_forget()
    lvl5_game.place_forget()
    lvl1_summary.place_forget()
    lvl2_summary.place_forget()
    lvl3_summary.place_forget()
    lvl4_summary.place_forget()
    lvl5_summary.place_forget()
    # lvl6_summary.place_forget()    
    lvl6_game.place(x=0, y=0)


###
instr_lvl6= Frame(root) #, width=800,  ) #bg="lavender")
#display instructions for 6th level
backyard = Label(instr_lvl6, text="Next we are going to look for " + "\n"+ "invertebrates in my backyard" +"\n" + "Invertebrates don't have a spine and are often quite small.", font=("Times New Roman", 12), width=40)
backyard.place(x=30, y=100)
#continue button to start 6th level
cont6 =  Button(instr_lvl6, text="Continue", command=Level6)
cont6.place(x=30, y=350)
#collage of invertebrates
invertebrates_collage_image = PIL.Image.open("D:\\yr12\\project pics\\level 6\\invertebrates.jpg")
TK_invertebrates_collage =   customtkinter.CTkImage(invertebrates_collage_image,
    size=(400,400))
invertebrates_collage =   customtkinter.CTkLabel(master=instr_lvl6, image=TK_invertebrates_collage)
invertebrates_collage.place(x=400, y=0)

def transition5():
    list_correct_animals=""
    title_screen.place_forget()
    instr_lvl1.place_forget()
    instr_lvl2.place_forget()
    instr_lvl3.place_forget()
    instr_lvl4.place_forget()
    instr_lvl5.place_forget()
    lvl1_game.place_forget()
    lvl2_game.place_forget()
    lvl3_game.place_forget()
    lvl4_game.place_forget()
    lvl5_game.place_forget()
    # lvl6_game.place_forget()
    lvl1_summary.place_forget()
    lvl2_summary.place_forget()
    lvl3_summary.place_forget()
    lvl4_summary.place_forget()
    #lvl5_summary.place_forget()
    # lvl6_summary.place_forget()
    instr_lvl6.place(x=0, y=0)

###
lvl5_summary= Frame(root) #, width=800) #bg="light yellow")
summary_screen5= Label(master=lvl5_summary, text=("You've found the following reptiles" + list_correct_animals)) #, width=800) #bg="grey")
summary_screen5.place(x=0, y=0)
next_level5= Button(master=lvl5_summary, text=("next level"), width=10, height=5, command=transition5())
next_level5.place(x=700, y=350)

#back option
back6= Button(master=lvl6_game, text=("back"), width=10, height=5, command=transition5())
back6.place(x=700, y=350)


























###
congrats= Frame(root) #, width=800, bg="gold")
congrats_message= Label(master=congrats, text=("Congrats, you are now an expert on the 6 categories of animals")) #, width=800) #bg="grey")
congrats_message.place(x=0, y=0)
# replay= Button(master=congrats, text=("replay"), width=10, height=5, command=start())
# replay.place(x=700, y=350)
 
def endscreen():
    title_screen.place_forget()
    instr_lvl1.place_forget()
    instr_lvl2.place_forget()
    instr_lvl3.place_forget()
    instr_lvl4.place_forget()
    instr_lvl5.place_forget()
    instr_lvl6.place_forget()
    lvl1_game.place_forget()
    lvl2_game.place_forget()
    lvl3_game.place_forget()
    lvl4_game.place_forget()
    lvl5_game.place_forget()
    lvl6_game.place_forget()
    lvl1_summary.place_forget()
    lvl2_summary.place_forget()
    lvl3_summary.place_forget()
    lvl4_summary.place_forget()
    lvl5_summary.place_forget()
    lvl6_summary.place_forget()
    congrats.place(x=0, y=0)

























###
lvl6_summary= Frame(root) #, width=800, bg="lavender")
summary_screen6= Label(master=lvl6_summary, text=("You've found the following invertebrates" + list_correct_animals)) #, width=800) #bg="grey")
summary_screen6.place(x=0, y=0)
next_level6= Button(master=lvl6_summary, text=("next level"), width=10, height=5, command=endscreen())
next_level6.place(x=700, y=350)








#back option
back1= Button(master=lvl1_game, text=("back"), width=10, height=5, command=start)
back1.place(x=700, y=350)



introduction()


















root.mainloop()
