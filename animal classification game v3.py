
import PIL.Image
from PIL import ImageTk, Image
from tkinter import *
import customtkinter

root = Tk()
root.title('animal classification game')
root.geometry("800x400")

global points
points=0
global list_correct_animals
list_correct_animals= ""

#Intro to level1- description of birds + examples
def start():
    global Amazon
    global cont
    global birds_collage
    intro.destroy()
    begin.destroy()

    #display instructions for first level
    Amazon = Label(root, text="Welcome to the Amazon Rainforest!" + "\n"+ "We need to find 3 aves." +"\n" + "Remember, aves is the scientific name for birds." + "\n"+ "Birds have feathers and beaks and lay eggs.", font=("Times New Roman", 12), width=40)
    Amazon.place(x=30, y=100)

    #continue button to start 1st level
    cont = Button(root, text="Continue", command=Level1)
    cont.place(x=30, y=350)

    #collage of birds
    birds_collage_image = PIL.Image.open("D:\yr12\project pics\level 1\lvl-1-intro.png")
    TK_birds_collage = customtkinter.CTkImage(birds_collage_image,
        size=(400,400))
    birds_collage = customtkinter.CTkLabel(master=root, image=TK_birds_collage, text="")
    birds_collage.place(x=400, y=0)
    
#level 1 game
def Level1():
    level_1_done=False
    #while level_1_done==False:
    def wrong_answer(m):
        
        def undo_wrong_answer() :
            # when try again clicked, returns to level
            oops.destroy()
            try_again.destroy()
            
        global oops
        global try_again
        #message for incorrect answer
        oops=customtkinter.CTkLabel(master=root, text=("Oops, that isn't a bird!" + "\n" + "Remember birds have feathers and beaks!"), height=400, width=800, bg_color="grey")
        oops.place(x=0, y=0)
        try_again=customtkinter.CTkButton(master=root, text=("Try again"), width=10, height=5, command=undo_wrong_answer)
        try_again.place(x=700, y=350)
    def correct_choice():
        global points
        global score
        global animals_found
        global list_correct_animals
        #increments points and adds correct animal to list
        points=points+1
        if points>3:
            level_1_done=True
        score.config(text="SCORE: "+ str(points))
        animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)
        #when to move on to next level    
    def which_button(m):
        global list_correct_animals
        #adding to list of correct animals
        list_correct_animals=list_correct_animals + "\n" + m
        correct_choice()
    def Level1_options():
        global points
        score.place(x=550, y=0)
        animals_found.place(x=450, y=50)
        #resetting screen
        Amazon.destroy()
        cont.destroy()
        birds_collage.destroy()
        #global buttons
        global CAToucan_button
        global GAnaconda_button
        global BCSMonkey_button
        global RHMonkey_button
        global Pcuerno_button
        global PDfrog_button
        global jaguar_button
        global capybara_button
        global macaw_button
        #displaying options
        #Macaw
        macaw_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\blue_macaw.jpg")
        macaw_CTK = customtkinter.CTkImage(macaw_img,
                                            size=(130,110))
        macaw_button = customtkinter.CTkButton(master=root, image=macaw_CTK, text="Blue and Gold Macaw", compound="bottom",
                                            command=lambda m="Blue and Gold Macaw":which_button(m))
        macaw_button.place(x=0, y=0)
        #capybara
        capybara_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\capybara.jpeg")
        capybara_CTK = customtkinter.CTkImage(capybara_img,
                                            size=(130,110))
        capybara_button = customtkinter.CTkButton(master=root, image=capybara_CTK, text="capybara", compound="bottom",
                                            command=lambda m="capybara":wrong_answer(m))
        capybara_button.place(x=140, y=0)
        #jaguar
        jaguar_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\jaguar.jpeg")
        jaguar_CTK = customtkinter.CTkImage(jaguar_img,
                                            size=(130,110))
        jaguar_button = customtkinter.CTkButton(master=root, image=jaguar_CTK, text="jaguar", compound="bottom",
                                            command=lambda m="jaguar":wrong_answer(m))
        jaguar_button.place(x=280, y=0)
        #poison dart frog
        PDfrog_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\poison-dart-frog.jpeg")
        PDfrog_CTK = customtkinter.CTkImage(PDfrog_img,
                                            size=(130,110))
        PDfrog_button = customtkinter.CTkButton(master=root, image=PDfrog_CTK, text="poison dart frog", compound="bottom",
                                            command=lambda m="poison dart frog":wrong_answer(m))
        PDfrog_button.place(x=280, y=135)
        #Pantalón-de-Cuerno
        Pcuerno_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\Pantalón-de-Cuerno.jpg")
        Pcuerno_CTK = customtkinter.CTkImage(Pcuerno_img,
                                            size=(130,110))
        Pcuerno_button = customtkinter.CTkButton(master=root, image=Pcuerno_CTK, text="Pantalón-de-Cuerno", compound="bottom",
                                            command=lambda m="Pantalón-de-Cuerno":which_button(m))
        Pcuerno_button.place(x=140, y=135)
        #Red Howler Money
        RHMonkey_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\red-howler-monkey.jpeg")
        RHMonkey_CTK = customtkinter.CTkImage(RHMonkey_img,
                                            size=(130,110))
        RHMonkey_button = customtkinter.CTkButton(master=root, image=RHMonkey_CTK, text="Red Howler Monkey", compound="bottom",
                                            command=lambda m="Red Howler Monkey":wrong_answer(m))
        RHMonkey_button.place(x=0, y=135)
        #black capped squirrel monkey
        BCSMonkey_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\black-capped-squirrel-monkey.jpeg")
        BCSMonkey_CTK = customtkinter.CTkImage(BCSMonkey_img,
                                            size=(130,110))
        BCSMonkey_button = customtkinter.CTkButton(master=root, image=BCSMonkey_CTK, text="Black Capped Squirrel", compound="bottom",
                                            command=lambda m="Black Capped Squirrel":wrong_answer(m))
        BCSMonkey_button.place(x=0, y=260)
        #green anaconda
        GAnaconda_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\green-anaconda.jpeg")
        GAnaconda_CTK = customtkinter.CTkImage(GAnaconda_img,
                                            size=(130,110))
        GAnaconda_button = customtkinter.CTkButton(master=root, image=GAnaconda_CTK, text="Green Anaconda", compound="bottom",
                                            command=lambda m="Green Anaconda":wrong_answer(m))
        GAnaconda_button.place(x=140, y=260)
        
        #Toucan-Collared-Aracari
        CAToucan_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\Toucan-Collared-Aracari.jpg")
        CAToucan_CTK = customtkinter.CTkImage(CAToucan_img,
                                            size=(130,110))
        CAToucan_button = customtkinter.CTkButton(master=root, image=CAToucan_CTK, text="Toucan Collared Aracari", compound="bottom",
                                            command= (lambda m="Toucan Collared Aracari":which_button(m)))
        CAToucan_button.place(x=280, y=260)
    Level1_options()
        
    CAToucan_button.destroy()
    GAnaconda_button.destroy()
    BCSMonkey_button.destroy()
    RHMonkey_button.destroy()
    Pcuerno_button.destroy()
    PDfrog_button.destroy()
    jaguar_button.destroy()
    capybara_button.destroy()
    macaw_button.destroy()
    score.place_forget()
    animals_found.place_forget()
    points=0
    list_correct_animals=""
    Level2()
    
   



    


    

        
def Intro2():
    global Savanna
    global cont2
    global mammals_collage
    #display instructions for second level
    Savanna =customtkinter.CTkLabel(root, text="Next we are going to look for " + "\n"+ "mammals in the African Savanna" +"\n" + "Mammals are warm blooded, have hair or fur " + "\n"+ "and have very complex brains.", font=("Times New Roman", 12), width=40)
    Savanna.place(x=30, y=100)
    #continue button to start 1st level
    cont2 = customtkinter.CTkButton(root, text="Continue", command=Level2)
    cont2.place(x=30, y=350)
    #collage of birds
    mammals_collage_image = PIL.Image.open("D:\\yr12\\project\\pics\\level 2\\Mammal_intro.jpg")
    TK_mammals_collage = customtkinter.CTkImage(mammals_collage_image,
        size=(400,400))
    mammals_collage = customtkinter.CTkLabel(master=root, image=TK_mammals_collage)
    mammals_collage.place(x=400, y=0)
    
def Level2():
    global points
    score.place(x=550, y=0)
    animals_found.place(x=450, y=50)
    #resetting screen
    Savanna.destroy()
    cont2.destroy()
    mammals_collage.destroy()
    #displaying options
    global ASTortoise_button
    global dung_beetle_button
    global ostrich_button
    global rhinoceros_button
    global scorpion_button
    global hornbill_button
    global african_elephant_button
    global aardvark_button
    global cobra_button
    #cobra
    Cobra_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\cobra.jpg")
    cobra_CTK = customtkinter.CTkImage(Cobra_img,
                                       size=(130,110))
    cobra_button = customtkinter.CTkButton(master=root, image=cobra_CTK, text="cobra", compound="bottom",
                                        command=lambda m="cobra":wrong_answer2(m))
    cobra_button.place(x=0, y=0)
    #aardvark
    aardvark_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\aardvark.jpg")
    aardvark_CTK = customtkinter.CTkImage(aardvark_img,
                                       size=(130,110))
    aardvark_button = customtkinter.CTkButton(master=root, image=aardvark_CTK, text="aardvark", compound="bottom",
                                        command=lambda m="aardvark":which_button2(m))
    aardvark_button.place(x=140, y=0)
    #african_elephant
    african_elephant_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\mammals\\african_elephant.jpg")
    african_elephant_CTK = customtkinter.CTkImage(african_elephant_img,
                                       size=(130,110))
    african_elephant_button = customtkinter.CTkButton(master=root, image=african_elephant_CTK, text="african elephant", compound="bottom",
                                        command=lambda m="african elephant":which_button2(m))
    african_elephant_button.place(x=280, y=0)
    #hornbill
    hornbill_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\hornbill.jpg")
    hornbill_CTK = customtkinter.CTkImage(hornbill_img,
                                       size=(130,110))
    hornbill_button = customtkinter.CTkButton(master=root, image=hornbill_CTK, text="hornbill", compound="bottom",
                                        command=lambda m="hornbill":wrong_answer2(m))
    hornbill_button.place(x=280, y=135)
    #scorpion
    scorpion_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\scorpion.jpg")
    scorpion_CTK = customtkinter.CTkImage(scorpion_img,
                                       size=(130,110))
    scorpion_button = customtkinter.CTkButton(master=root, image=scorpion_CTK, text="scorpion", compound="bottom",
                                        command=lambda m="scorpion":wrong_answer2(m))
    scorpion_button.place(x=140, y=135)
    #rhinoceros
    rhinoceros_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\mammals\\rhinoceros.jpg")
    rhinoceros_CTK = customtkinter.CTkImage(rhinoceros_img,
                                       size=(130,110))
    rhinoceros_button = customtkinter.CTkButton(master=root, image=rhinoceros_CTK, text="rhinoneros", compound="bottom",
                                        command=lambda m="rhinoceros":which_button2(m))
    rhinoceros_button.place(x=0, y=135)
    #ostrich
    ostrich_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\ostrich.jpg")
    ostrich_CTK = customtkinter.CTkImage(ostrich_img,
                                       size=(130,110))
    ostrich_button = customtkinter.CTkButton(master=root, image=ostrich_CTK, text="ostrich", compound="bottom",
                                        command=lambda m="ostrich":wrong_answer2(m))
    ostrich_button.place(x=0, y=260)
    #dung beetle
    dung_beetle_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\dung-beetle.jpg")
    dung_beetle_CTK = customtkinter.CTkImage(dung_beetle_img,
                                       size=(130,110))
    dung_beetle_button = customtkinter.CTkButton(master=root, image=dung_beetle_CTK, text="dung beetle", compound="bottom",
                                        command=lambda m="dung beetle":wrong_answer2(m))
    dung_beetle_button.place(x=140, y=260)
    
    #african spurred tortoise
    ASTortoise_img = PIL.Image.open("D:\\yr12\\project pics\\level 2\\other\\african-spurred-tortoise.jpg")
    ASTortoise_CTK = customtkinter.CTkImage(ASTortoise_img,
                                       size=(130,110))
    ASTortoise_button = customtkinter.CTkButton(master=root, image=ASTortoise_CTK, text="african spurred tortoise", compound="bottom",
                                        command= (lambda m="african spurred tortoise":which_button2(m)))
    ASTortoise_button.place(x=280, y=260)


    
def correct_choice2():
    global points
    global score
    global animals_found
    #increments points and adds correct animal to list
    points=points+1
    score.config(text="SCORE: "+ str(points))
    animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals2)
    #when to move on to next level
    if points>2:
        ASTortoise_button.destroy()
        dung_beetle_button.destroy()
        ostrich_button.destroy()
        rhinoceros_button.destroy()
        scorpion_button.destroy()
        hornbill_button.destroy()
        african_elephant_button.destroy()
        aardvark_button.destroy()
        cobra_button.destroy()
        score.place_forget()
        animals_found.place_forget()
        points=0
        Intro2


def which_button2(m):
    global list_correct_animals2
    #adding to list of correct animals
    list_correct_animals2=list_correct_animals + "\n" + m
    correct_choice2()


def wrong_answer2(m):
    global oops2
    global try_again2
    #message for incorrect answer
    oops2=customtkinter.CTkLabel(master=root, text=("Oops, that isn't a bird!" + "\n" + "Remember birds have feathers and beaks!"), height=400, width=800, bg_color="grey")
    oops2.place(x=0, y=0)
    try_again2=customtkinter.CTkButton(master=root, text=("Try again"), width=10, height=5, command=undo_wrong_answer2)
    try_again2.place(x=700, y=350)



def undo_wrong_answer2() :
    # when try again clicked, returns to level
    oops2.destroy()
    try_again2.destroy()

                        

intro = Label(root, text="Animal Classification Game", height = 3, width=25, font=("Times New Roman", 18))
intro.place(x=250, y=150)

begin = Button(root, text="Begin", command=start)
begin.place(x=350, y=250)

score = Label(root, text="SCORE: ", font=(("Times New Roman"), 18))

animals_found = Label(root, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))












root.mainloop()
