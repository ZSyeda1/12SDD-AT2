
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
    birds_collage_image = PIL.Image.open(r"lvl-1-intro.gif")
    TK_birds_collage = customtkinter.CTkImage(birds_collage_image,
        size=(400,400))
    birds_collage = customtkinter.CTkLabel(master=root, image=TK_birds_collage, text="")
    birds_collage.place(x=400, y=0)
    
#level 1 game
def Level1():
    global level_1_done
    points=0
    level_1_done=False #used to end level when score of 3 reached
    #while level_1_done==False:
    def wrong_answer(m): #when wrong button clicked
        
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
    def which_button(m): #when correct button clicked, used to store list of correct animals so far
        global list_correct_animals
        #adding to list of correct animals
        list_correct_animals=list_correct_animals + "\n" + m
        if len(list_correct_animals)==3:
            reset1()
    def Level1_set1():
        global m
        #back option
        back1=customtkinter.CTkButton(master=root, text=("back"), width=10, height=5, command=start())
        back1.place(x=700, y=350)
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
        #instructions
        instructions=Label(root, text="find the bird", font= ("Times New Roman", 18))
        instructions.place(x=200, y=10)
        #Macaw
        macaw_img = PIL.Image.open(r"blue_macaw.gif")
        macaw_CTK = customtkinter.CTkImage(macaw_img,
                                            size=(260,220))
        macaw_button = customtkinter.CTkButton(master=root, image=macaw_CTK, text="Blue and Gold Macaw", compound="bottom",
                                                command=lambda: (lambda m="Blue and Gold Macaw": [which_button(m), Level1_set2()]))
        macaw_button.place(x=0, y=135)
        #capybara
        capybara_img = PIL.Image.open(r"capybara.gif")
        capybara_CTK = customtkinter.CTkImage(capybara_img,
                                            size=(260,220))
        capybara_button = customtkinter.CTkButton(master=root, image=capybara_CTK, text="capybara", compound="bottom",
                                            command=lambda m="capybara":wrong_answer(m))
        capybara_button.place(x=250, y=135)
        #jaguar
        jaguar_img = PIL.Image.open(r"jaguar.gif")
        jaguar_CTK = customtkinter.CTkImage(jaguar_img,
                                            size=(260,220))
        jaguar_button = customtkinter.CTkButton(master=root, image=jaguar_CTK, text="jaguar", compound="bottom",
                                            command=lambda m="jaguar":wrong_answer(m))
        jaguar_button.place(x=500, y=135)
    def Level1_set2():
        global m
        #instructions
        instructions=Label(root, text="find the bird")
        instructions.place(x=200, y=10)
        #poison dart frog
        PDfrog_img = PIL.Image.open(r"poison-dart-frog.jpeg")
        PDfrog_CTK = customtkinter.CTkImage(PDfrog_img,
                                            size=(130,110))
        PDfrog_button = customtkinter.CTkButton(master=root, image=PDfrog_CTK, text="poison dart frog", compound="bottom",
                                            command=lambda m="poison dart frog":wrong_answer(m))
        PDfrog_button.place(x=280, y=135)
        #Pantalón-de-Cuerno
        Pcuerno_img = PIL.Image.open(r"Pantalón-de-Cuerno.jpg")
        Pcuerno_CTK = customtkinter.CTkImage(Pcuerno_img,
                                            size=(130,110))
        Pcuerno_button = customtkinter.CTkButton(master=root, image=Pcuerno_CTK, text="Pantalón-de-Cuerno", compound="bottom",
                                            command=lambda: (lambda m="Pantalón-de-Cuerno": [which_button(m), Level1_set3()]))
        Pcuerno_button.place(x=140, y=135)
        #Red Howler Money
        RHMonkey_img = PIL.Image.open(r"red-howler-monkey.jpeg")
        RHMonkey_CTK = customtkinter.CTkImage(RHMonkey_img,
                                            size=(130,110))
        RHMonkey_button = customtkinter.CTkButton(master=root, image=RHMonkey_CTK, text="Red Howler Monkey", compound="bottom",
                                            command=lambda m="Red Howler Monkey":wrong_answer(m))
        RHMonkey_button.place(x=0, y=135)
    def Level1_set3():
        global m
        #instructions
        instructions=Label(root, text="find the bird")
        instructions.place(x=200, y=10)
        #black capped squirrel monkey
        BCSMonkey_img = PIL.Image.open(r"black-capped-squirrel-monkey.jpeg")
        BCSMonkey_CTK = customtkinter.CTkImage(BCSMonkey_img,
                                            size=(130,110))
        BCSMonkey_button = customtkinter.CTkButton(master=root, image=BCSMonkey_CTK, text="Black Capped Squirrel", compound="bottom",
                                            command=lambda m="Black Capped Squirrel":wrong_answer(m))
        BCSMonkey_button.place(x=0, y=260)
        #green anaconda
        GAnaconda_img = PIL.Image.open(r"green-anaconda.jpeg")
        GAnaconda_CTK = customtkinter.CTkImage(GAnaconda_img,
                                            size=(130,110))
        GAnaconda_button = customtkinter.CTkButton(master=root, image=GAnaconda_CTK, text="Green Anaconda", compound="bottom",
                                            command=lambda m="Green Anaconda":wrong_answer(m))
        GAnaconda_button.place(x=140, y=260)
        
        #Toucan-Collared-Aracari
        CAToucan_img = PIL.Image.open(r"Toucan-Collared-Aracari.jpg")
        CAToucan_CTK = customtkinter.CTkImage(CAToucan_img,
                                            size=(130,110))
        CAToucan_button = customtkinter.CTkButton(master=root, image=CAToucan_CTK, text="Toucan Collared Aracari", compound="bottom",
                                            command=lambda m="Toucan Collared Aracari":which_button(m))
        CAToucan_button.place(x=280, y=260)
    Level1_set1()

def reset1():
    # when score of 3 reached, destroy all elements of this level and move to next    
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
    points=0 #reset score
    list_correct_animals="" #reset list of animals found
    summary_screen1=customtkinter.CTkLabel(master=root, text=("You've found the following Aves" + list_correct_animals), height=400, width=800, bg_color="grey")
    summary_screen1.place(x=0, y=0)
    next_level=customtkinter.CTkButton(master=root, text=("next level"), width=10, height=5, command=Level2())
    next_level.place(x=700, y=350)
    
def reset2():
    #when to move on to next level
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
    list_correct_animals=""
    points=0
    summary_screen2=customtkinter.CTkLabel(master=root, text=("You've found the following mammals" + list_correct_animals2), height=400, width=800, bg_color="grey")
    summary_screen2.place(x=0, y=0)
    next_level2=customtkinter.CTkButton(master=root, text=("next level"), width=10, height=5, command=Level3())
    next_level2.place(x=700, y=350)   
   
def Level2():
    global level_2_done
    level_2_done=False
    #while level_2_done==False:

    def correct_choice2():
        global points
        global score
        global animals_found
        #increments points and adds correct animal to list
        points=points+1
        if points>3:
            reset2()
        score.config(text="SCORE: "+ str(points))
        animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals2)
    def which_button2(m):
        global list_correct_animals2
        #adding to list of correct animals
        list_correct_animals2=list_correct_animals + "\n" + m
        correct_choice2() 
    def wrong_answer2(m):
        global oops2
        global try_again2
        def undo_wrong_answer2() :
            # when try again clicked, returns to level
            oops2.destroy()
            try_again2.destroy() 
        #message for incorrect answer
        oops2=customtkinter.CTkLabel(master=root, text=("Oops, that isn't a mammal!" + "\n" + "Remember mammals have hair or fur!"), height=400, width=800, bg_color="grey")
        oops2.place(x=0, y=0)
        try_again2=customtkinter.CTkButton(master=root, text=("Try again"), width=10, height=5, command=undo_wrong_answer2)
        try_again2.place(x=700, y=350)
    def Level2_options():
        global points
        score.place(x=550, y=0)
        animals_found.place(x=450, y=50)
        #back option
        back2=customtkinter.CTkButton(master=root, text=("back"), width=10, height=5, command=Level1())
        back2.place(x=700, y=350)
        #resetting screen
        Savanna.destroy()
        cont2.destroy()
        mammals_collage.destroy()
        #making options global- to delete later
        global ASTortoise_button
        global dung_beetle_button
        global ostrich_button
        global rhinoceros_button
        global scorpion_button
        global hornbill_button
        global african_elephant_button
        global aardvark_button
        global cobra_button
        #displaying options
        #cobra
        cobra_img = PIL.Image.open("cobra.jpg")
        cobra_CTK = customtkinter.CTkImage(cobra_img,
                                            size=(130,110))
        cobra_button = customtkinter.CTkButton(master=root, image=cobra_CTK, text="cobra", compound="bottom",
                                            command=lambda m="cobra":wrong_answer2(m))
        cobra_button.place(x=0, y=0)
        #aardvark
        aardvark_img = PIL.Image.open("aardvark.jpg")
        aardvark_CTK = customtkinter.CTkImage(aardvark_img,
                                            size=(130,110))
        aardvark_button = customtkinter.CTkButton(master=root, image=aardvark_CTK, text="aardvark", compound="bottom",
                                            command=lambda m="aardvark":which_button2(m))
        aardvark_button.place(x=140, y=0)
        #african_elephant
        african_elephant_img = PIL.Image.open("african_elephant.jpg")
        african_elephant_CTK = customtkinter.CTkImage(african_elephant_img,
                                            size=(130,110))
        african_elephant_button = customtkinter.CTkButton(master=root, image=african_elephant_CTK, text="african elephant", compound="bottom",
                                            command=lambda m="african elephant":which_button2(m))
        african_elephant_button.place(x=280, y=0)
        #hornbill
        hornbill_img = PIL.Image.open("hornbill.jpg")
        hornbill_CTK = customtkinter.CTkImage(hornbill_img,
                                            size=(130,110))
        hornbill_button = customtkinter.CTkButton(master=root, image=hornbill_CTK, text="hornbill", compound="bottom",
                                            command=lambda m="hornbill":wrong_answer2(m))
        hornbill_button.place(x=280, y=135)
        #scorpion
        scorpion_img = PIL.Image.open("scorpion.jpg")
        scorpion_CTK = customtkinter.CTkImage(scorpion_img,
                                            size=(130,110))
        scorpion_button = customtkinter.CTkButton(master=root, image=scorpion_CTK, text="scorpion", compound="bottom",
                                            command=lambda m="scorpion":wrong_answer2(m))
        scorpion_button.place(x=140, y=135)
        #rhinoceros
        rhinoceros_img = PIL.Image.open("rhinoceros.jpg")
        rhinoceros_CTK = customtkinter.CTkImage(rhinoceros_img,
                                            size=(130,110))
        rhinoceros_button = customtkinter.CTkButton(master=root, image=rhinoceros_CTK, text="rhinoneros", compound="bottom",
                                            command=lambda m="rhinoceros":which_button2(m))
        rhinoceros_button.place(x=0, y=135)
        #ostrich
        ostrich_img = PIL.Image.open("ostrich.jpg")
        ostrich_CTK = customtkinter.CTkImage(ostrich_img,
                                            size=(130,110))
        ostrich_button = customtkinter.CTkButton(master=root, image=ostrich_CTK, text="ostrich", compound="bottom",
                                            command=lambda m="ostrich":wrong_answer2(m))
        ostrich_button.place(x=0, y=260)
        #dung beetle
        dung_beetle_img = PIL.Image.open("dung-beetle.jpg")
        dung_beetle_CTK = customtkinter.CTkImage(dung_beetle_img,
                                            size=(130,110))
        dung_beetle_button = customtkinter.CTkButton(master=root, image=dung_beetle_CTK, text="dung beetle", compound="bottom",
                                            command=lambda m="dung beetle":wrong_answer2(m))
        dung_beetle_button.place(x=140, y=260)
        
        #african spurred tortoise
        ASTortoise_img = PIL.Image.open("african-spurred-tortoise.jpg")
        ASTortoise_CTK = customtkinter.CTkImage(ASTortoise_img,
                                            size=(130,110))
        ASTortoise_button = customtkinter.CTkButton(master=root, image=ASTortoise_CTK, text="african spurred tortoise", compound="bottom",
                                            command= (lambda m="african spurred tortoise":which_button2(m)))
        ASTortoise_button.place(x=280, y=260)
    def Intro2():
        #display instructions for second level
        global Savanna
        Savanna =customtkinter.CTkLabel(root, text="Next we are going to look for " + "\n"+ "mammals in the African Savanna" +"\n" + "Mammals are warm blooded, have hair or fur " + "\n"+ "and have very complex brains.", font=("Times New Roman", 12), width=40)
        Savanna.place(x=30, y=100)
        #continue button to start 2nd level
        global cont2
        cont2 = customtkinter.CTkButton(root, text="Continue", command=Level2_options)
        cont2.place(x=30, y=350)
        #collage of mammals
        global mammals_collage
        mammals_collage_image = PIL.Image.open("Mammal_intro.jpg")
        TK_mammals_collage = customtkinter.CTkImage(mammals_collage_image,
            size=(400,400))
        mammals_collage = customtkinter.CTkLabel(master=root, image=TK_mammals_collage)
        mammals_collage.place(x=400, y=0)

    Intro2()

def Level3():
    global level_3_done
    level_3_done=False
    while level_3_done==False:

        def correct_choice3():
            global points
            global score
            global animals_found
            #increments points and adds correct animal to list
            points=points+1
            if points>3:
                level_3_done=True
            score.config(text="SCORE: "+ str(points))
            animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals3)
        def which_button3(m):
            global list_correct_animals3
            #adding to list of correct animals
            list_correct_animals3=list_correct_animals + "\n" + m
            correct_choice3() 
        def wrong_answer3(m):
            global oops3
            global try_again3
            def undo_wrong_answer3() :
                # when try again clicked, returns to level
                oops3.destroy()
                try_again3.destroy() 
            #message for incorrect answer
            oops3=customtkinter.CTkLabel(master=root, text=("Oops, that isn't a fish!" + "\n" + "Remember fish have scales and live underwater!"), height=400, width=800, bg_color="grey")
            oops3.place(x=0, y=0)
            try_again3=customtkinter.CTkButton(master=root, text=("Try again"), width=10, height=5, command=undo_wrong_answer3)
            try_again3.place(x=700, y=350)
        def Level3_options():
            global points
            score.place(x=550, y=0)
            animals_found.place(x=450, y=50)
            #back option
            back3=customtkinter.CTkButton(master=root, text=("back"), width=10, height=5, command=Level2())
            back3.place(x=700, y=350)
            #resetting screen
            GBR.destroy()
            cont3.destroy()
            fish_collage.destroy()
            #making options global- to delete later
            global MShrimp_button
            global HWhale_button
            global Gclam_button
            global jellyfish_button
            global Mray_button
            global Gturtle_button
            global dugong_button
            global Boctapus_button
            global Cfish_button
            #displaying options
            #clownfish
            Cfish_img = PIL.Image.open("clownfish.jpg")
            Cfish_CTK = customtkinter.CTkImage(Cfish_img,
                                               size=(130,110))
            Cfish_button = customtkinter.CTkButton(master=root, image=Cfish_CTK, text="clownfish", compound="bottom",
                                                command=lambda m="clownfish":which_button3(m))
            Cfish_button.place(x=0, y=0)
            #blanket octapus
            Boctapus_img = PIL.Image.open("Boctapus.jpg")
            Boctapus_CTK = customtkinter.CTkImage(Boctapus_img,
                                               size=(130,110))
            Boctapus_button = customtkinter.CTkButton(master=root, image=Boctapus_CTK, text="blanket octapus", compound="bottom",
                                                command=lambda m="blanket octapus":wrong_answer3(m))
            Boctapus_button.place(x=140, y=0)
            #dugong
            dugong_img = PIL.Image.open("dugong.jpg")
            dugong_CTK = customtkinter.CTkImage(dugong_img,
                                               size=(130,110))
            dugong_button = customtkinter.CTkButton(master=root, image=dugong_CTK, text="dugong", compound="bottom",
                                                command=lambda m="dugong":wrong_answer3(m))
            dugong_button.place(x=280, y=0)
            #green turtle
            Gturtle_img = PIL.Image.open("green-turtle.jpg")
            Gturtle_CTK = customtkinter.CTkImage(Gturtle_img,
                                               size=(130,110))
            Gturtle_button = customtkinter.CTkButton(master=root, image=Gturtle_CTK, text="green turtle", compound="bottom",
                                                command=lambda m="green turtle":which_button3(m))
            Gturtle_button.place(x=280, y=135)
            #manta ray
            Mray_img = PIL.Image.open("manta-ray.jpg")
            Mray_CTK = customtkinter.CTkImage(Mray_img,
                                               size=(130,110))
            Mray_button = customtkinter.CTkButton(master=root, image=Mray_CTK, text="manta ray", compound="bottom",
                                                command=lambda m="manta ray":which_button3(m))
            Mray_button.place(x=140, y=135)
            #giant clam
            Gclam_img = PIL.Image.open("giant-clam.jpg")
            Gclam_CTK = customtkinter.CTkImage(Gclam_img,
                                               size=(130,110))
            Gclam_button = customtkinter.CTkButton(master=root, image=Gclam_CTK, text="giant clam", compound="bottom",
                                                command=lambda m="giant clam":wrong_answer3(m))
            Gclam_button.place(x=0, y=135)
            #humpback whale
            HWhale_img = PIL.Image.open("humpback-whale.jpg")
            HWhale_CTK = customtkinter.CTkImage(HWhale_img,
                                               size=(130,110))
            HWhale_button = customtkinter.CTkButton(master=root, image=HWhale_CTK, text="Humpback Whale", compound="bottom",
                                                command=lambda m="Humpback Whale":wrong_answer3(m))
            HWhale_button.place(x=0, y=260)
            #jellyfish
            jellyfish_img = PIL.Image.open("jellyfish.jpg")
            jellyfish_CTK = customtkinter.CTkImage(jellyfish_img,
                                               size=(130,110))
            jellyfish_button = customtkinter.CTkButton(master=root, image=jellyfish_CTK, text="jellyfish", compound="bottom",
                                                command=lambda m="jellyfish":wrong_answer3(m))
            jellyfish_button.place(x=140, y=260)
            
            #mantis shrimp
            MShrimp_img = PIL.Image.open("mantis-shrimp.jpg")
            MShrimp_CTK = customtkinter.CTkImage(MShrimp_img,
                                               size=(130,110))
            MShrimp_button = customtkinter.CTkButton(master=root, image=MShrimp_CTK, text="mantis shrimp", compound="bottom",
                                                command= (lambda m="mantis shrimp":wrong_answer3(m)))
            MShrimp_button.place(x=280, y=260)
        def Intro3():
            #display instructions for 3rd level
            #great barrier reef
            global GBR
            GBR =customtkinter.CTkLabel(root, text="Next we are going to look for " + "\n"+ "fish in the Great Barrier Reef" +"\n" + "Fish have scales and live underwater.", font=("Times New Roman", 12), width=40)
            GBR.place(x=30, y=100)
            #continue button to start 3rd level
            global cont3
            cont3 = customtkinter.CTkButton(root, text="Continue", command=Level3_options)
            cont3.place(x=30, y=350)
            #collage of fish
            global fish_collage
            fish_collage_image = PIL.Image.open("fish-montage.jpg")
            TK_fish_collage = customtkinter.CTkImage(fish_collage_image,
                size=(400,400))
            fish_collage = customtkinter.CTkLabel(master=root, image=TK_fish_collage)
            fish_collage.place(x=400, y=0)

        Intro3()
        
    #when to move on to next level
    MShrimp_button.destroy()
    jellyfish_button.destroy()
    HWhale_button.destroy()
    Gclam_button.destroy()
    Mray_button.destroy()
    Gturtle_button.destroy()
    dugong_button.destroy()
    Boctapus_button.destroy()
    Cfish_button.destroy()
    score.place_forget()
    animals_found.place_forget()
    list_correct_animals=""
    points=0
    summary_screen3=customtkinter.CTkLabel(master=root, text=("You've found the following fish" + list_correct_animals3), height=400, width=800, bg_color="grey")
    summary_screen3.place(x=0, y=0)
    next_level3=customtkinter.CTkButton(master=root, text=("next level"), width=10, height=5, command=Level4())
    next_level3.place(x=700, y=350)


  
def Level4():
    global level_4_done
    level_4_done=False
    while level_4_done==False:

        def correct_choice4():
            global points
            global score
            global animals_found
            #increments points and adds correct animal to list
            points=points+1
            if points>3:
                level_3_done=True
            score.config(text="SCORE: "+ str(points))
            animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals4)
        def which_button4(m):
            global list_correct_animals4
            #adding to list of correct animals
            list_correct_animals4=list_correct_animals + "\n" + m
            correct_choice4() 
        def wrong_answer4(m):
            global oops4
            global try_again4
            def undo_wrong_answer4() :
                # when try again clicked, returns to level
                oops4.destroy()
                try_again4.destroy() 
            #message for incorrect answer
            oops4=customtkinter.CTkLabel(master=root, text=("Oops, that isn't an amphibian!" + "\n" + "Remember amphibians have slimy skin and live around water!"), height=400, width=800, bg_color="grey")
            oops4.place(x=0, y=0)
            try_again4=customtkinter.CTkButton(master=root, text=("Try again"), width=10, height=5, command=undo_wrong_answer4)
            try_again4.place(x=700, y=350)
        def Level4_options():
            global points
            score.place(x=550, y=0)
            animals_found.place(x=450, y=50)
            #back option
            back4=customtkinter.CTkButton(master=root, text=("back"), width=10, height=5, command=Level3())
            back4.place(x=700, y=350)
            #resetting screen
            BRF.destroy()#borneo rainforest
            cont4.destroy()
            amphibians_collage.destroy()
            #making options global- to delete later
            global BFHFrog_button
            global PElephant_button
            global JTFrog_button
            global orangutan_button
            global WFFrog_button
            global PMonkey_button
            global MCivet_button
            global RGFSquirrel_button
            global CLeopard_button
            #displaying options
            #Clouded Leopard
            CLeopard_img = PIL.Image.open("clouded-leopard.jpg")
            CLeopard_CTK = customtkinter.CTkImage(CLeopard_img,
                                               size=(130,110))
            CLeopard_button = customtkinter.CTkButton(master=root, image=CLeopard_CTK, text="Clouded Leopard", compound="bottom",
                                                command=lambda m="Clouded Leopard":wrong_answer4(m))
            CLeopard_button.place(x=0, y=0)
            #red giant flying squirrel
            RGFSquirrel_img = PIL.Image.open("red-giant-flying-squirrel.jpg")
            RGFSquirrel_CTK = customtkinter.CTkImage(RGFSquirrel_img,
                                               size=(130,110))
            RGFSquirrel_button = customtkinter.CTkButton(master=root, image=RGFSquirrel_CTK, text="red giant flying squirrel", compound="bottom",
                                                command=lambda m="red giant flying squirrel":wrong_answer4(m))
            RGFSquirrel_button.place(x=140, y=0)
            #Malay Civet
            MCivet_img = PIL.Image.open("Malay-civet.jpg")
            MCivet_CTK = customtkinter.CTkImage(MCivet_img,
                                               size=(130,110))
            MCivet_button = customtkinter.CTkButton(master=root, image=MCivet_CTK, text="Malay Civet", compound="bottom",
                                                command=lambda m="Malay Civet":wrong_answer4(m))
            MCivet_button.place(x=280, y=0)
            #Proboscis monkey
            PMonkey_img = PIL.Image.open("Proboscis-monkey.jpg")
            PMonkey_CTK = customtkinter.CTkImage(PMonkey_img,
                                               size=(130,110))
            PMonkey_button = customtkinter.CTkButton(master=root, image=PMonkey_CTK, text="Proboscis monkey", compound="bottom",
                                                command=lambda m="Proboscis monkey":wrong_answer4(m))
            PMonkey_button.place(x=280, y=135)
            #Wallaces flying frog
            WFFrog_img = PIL.Image.open("Wallaces-flying-frog.jpg")
            WFFrog_CTK = customtkinter.CTkImage(WFFrog_img,
                                               size=(130,110))
            WFFrog_button = customtkinter.CTkButton(master=root, image=WFFrog_CTK, text="Wallaces Flying Frog", compound="bottom",
                                                command=lambda m="Wallaces Flying Frog":which_button4(m))
            WFFrog_button.place(x=140, y=135)
            #orangutan
            orangutan_img = PIL.Image.open("Orangutan.jpg")
            orangutan_CTK = customtkinter.CTkImage(orangutan_img,
                                               size=(130,110))
            orangutan_button = customtkinter.CTkButton(master=root, image=orangutan_CTK, text="orangutan", compound="bottom",
                                                command=lambda m="orangutan":wrong_answer4(m))
            orangutan_button.place(x=0, y=135)
            
            #jade tree frog
            JTFrog_img = PIL.Image.open("jade-tree-frog.jpg")
            JTFrog_CTK = customtkinter.CTkImage(JTFrog_img,
                                               size=(130,110))
            JTFrog_button = customtkinter.CTkButton(master=root, image=JTFrog_CTK, text="jade tree frog", compound="bottom",
                                                command=lambda m="jade tree frog":which_button4(m))
            JTFrog_button.place(x=0, y=260)
            
            #Pygmy elephant
            PElephant_img = PIL.Image.open("Pygmy-Elephant.jpg")
            PElephant_CTK = customtkinter.CTkImage(PElephant_img,
                                               size=(130,110))
            PElephant_button = customtkinter.CTkButton(master=root, image=PElephant_CTK, text="Pygmy Elephant", compound="bottom",
                                                command=lambda m="Pygmy Elephant":wrong_answer4(m))
            PElephant_button.place(x=140, y=260)
            
            #BFHFrog
            BFHFrog_img = PIL.Image.open("bornean-flat-headed-frog.jpg")
            BFHFrog_CTK = customtkinter.CTkImage(BFHFrog_img,
                                               size=(130,110))
            BFHFrog_button = customtkinter.CTkButton(master=root, image=BFHFrog_CTK, text="bornean flat headed frog", compound="bottom",
                                                command= (lambda m="bornean flat headed frog":which_button4(m)))
            BFHFrog_button.place(x=280, y=260)
        def Intro4():
            #display instructions for 4th level
            global BRF
            BRF =customtkinter.CTkLabel(root, text="Next we are going to look for " + "\n"+ "amphibians in the Borneo Rainforest!" +"\n" + "Amphibians have slimy skin and live around water.", font=("Times New Roman", 12), width=40)
            BRF.place(x=30, y=100)
            #continue button to start 4th level
            global cont4
            cont4 = customtkinter.CTkButton(root, text="Continue", command=Level4_options)
            cont4.place(x=30, y=350)
            #collage of amphibians
            global amphibians_collage
            amphibians_collage_image = PIL.Image.open("amphibians.jpg")
            TK_amphibians_collage = customtkinter.CTkImage(amphibians_collage_image,
                size=(400,400))
            amphibians_collage = customtkinter.CTkLabel(master=root, image=TK_amphibians_collage)
            amphibians_collage.place(x=400, y=0)

        Intro4()
        
    #when to move on to next level
    BFHFrog_button.destroy()
    PElephant_button.destroy()
    JTFrog_button.destroy()
    orangutan_button.destroy()
    WFFrog_button.destroy()
    PMonkey_button.destroy()
    MCivet_button.destroy()
    RGFSquirrel_button.destroy()
    CLeopard_button.destroy()
    score.place_forget()
    animals_found.place_forget()
    list_correct_animals=""
    points=0
    summary_screen4=customtkinter.CTkLabel(master=root, text=("You've found the following amphibians" + list_correct_animals5), height=400, width=800, bg_color="grey")
    summary_screen4.place(x=0, y=0)
    next_level4=customtkinter.CTkButton(master=root, text=("next level"), width=10, height=5, command=Level5())
    next_level4.place(x=700, y=350)

    

def Level5():
    global level_5_done
    level_5_done=False
    while level_5_done==False:

        def correct_choice5():
            global points
            global score
            global animals_found
            #increments points and adds correct animal to list
            points=points+1
            if points>3:
                level_5_done=True
            score.config(text="SCORE: "+ str(points))
            animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals5)
        def which_button5(m):
            global list_correct_animals5
            #adding to list of correct animals
            list_correct_animals5=list_correct_animals + "\n" + m
            correct_choice5() 
        def wrong_answer5(m):
            global oops5
            global try_again5
            def undo_wrong_answer5() :
                # when try again clicked, returns to level
                oops5.destroy()
                try_again5.destroy() 
            #message for incorrect answer
            oops5=customtkinter.CTkLabel(master=root, text=("Oops, that isn't a reptile!" + "\n" + "Remember reptiles have scaly skin!"), height=400, width=800, bg_color="grey")
            oops5.place(x=0, y=0)
            try_again5=customtkinter.CTkButton(master=root, text=("Try again"), width=10, height=5, command=undo_wrong_answer5)
            try_again5.place(x=700, y=350)
        def Level5_options():
            global points
            score.place(x=550, y=0)
            animals_found.place(x=450, y=50)
            #back option
            back5=customtkinter.CTkButton(master=root, text=("back"), width=10, height=5, command=Level4())
            back5.place(x=700, y=350)
            #resetting screen
            outback.destroy()
            cont5.destroy()
            reptiles_collage.destroy()
            #making options global- to delete later
            global kookaburra_button
            global kangaroo_button
            global quokka_button
            global SPython_button
            global FNLizard_button
            global AFCamel_button
            global dingo_button
            global TDevil_button
            global SGoanna_button
            #displaying options
            #Sand Goanna
            SGoanna_img = PIL.Image.open("sand-goanna.jpg")
            SGoanna_CTK = customtkinter.CTkImage(SGoanna_img,
                                               size=(130,110))
            SGoanna_button = customtkinter.CTkButton(master=root, image=SGoanna_CTK, text="Sand Goanna", compound="bottom",
                                                command=lambda m="Sand Goanna":which_button5(m))
            SGoanna_button.place(x=0, y=0)
            #Throny Devil
            TDevil_img = PIL.Image.open("throny-devil.jpg")
            TDevil_CTK = customtkinter.CTkImage(TDevil_img,
                                               size=(130,110))
            TDevil_button = customtkinter.CTkButton(master=root, image=TDevil_CTK, text="Throny Devil", compound="bottom",
                                                command=lambda m="Throny Devil":which_button5(m))
            TDevil_button.place(x=140, y=0)
            #dingo
            dingo_img = PIL.Image.open("dingo.jpg")
            dingo_CTK = customtkinter.CTkImage(dingo_img,
                                               size=(130,110))
            dingo_button = customtkinter.CTkButton(master=root, image=dingo_CTK, text="dingo", compound="bottom",
                                                command=lambda m="dingo":wrong_answer5(m))
            dingo_button.place(x=280, y=0)
            #Australian Feral Camel
            AFCamel_img = PIL.Image.open("australian-feral-camel.jpg")
            AFCamel_CTK = customtkinter.CTkImage(AFCamel_img,
                                               size=(130,110))
            AFCamel_button = customtkinter.CTkButton(master=root, image=AFCamel_CTK, text="Australian Feral Camel", compound="bottom",
                                                command=lambda m="Australian Feral Camel":wrong_answer5(m))
            AFCamel_button.place(x=280, y=135)
            #Frill Neck Lizard
            FNLizard_img = PIL.Image.open("frill-neck-lizard.jpg")
            FNLizard_CTK = customtkinter.CTkImage(FNLizard_img,
                                               size=(130,110))
            FNLizard_button = customtkinter.CTkButton(master=root, image=FNLizard_CTK, text="Frill Neck Lizard", compound="bottom",
                                                command=lambda m="Frill Neck Lizard":which_button5(m))
            FNLizard_button.place(x=140, y=135)
            #Stimson's Python
            SPython_img = PIL.Image.open("stimson's-python.jpg")
            SPython_CTK = customtkinter.CTkImage(SPython_img,
                                               size=(130,110))
            SPython_button = customtkinter.CTkButton(master=root, image=SPython_CTK, text="Stimson's Python", compound="bottom",
                                                command=lambda m="Stimson's Python":wrong_answer5(m))
            SPython_button.place(x=0, y=135)
            #Quokka
            quokka_img = PIL.Image.open("quokka.jpg")
            quokka_CTK = customtkinter.CTkImage(quokka_img,
                                               size=(130,110))
            quokka_button = customtkinter.CTkButton(master=root, image=quokka_CTK, text="Quokka", compound="bottom",
                                                command=lambda m="Quokka":wrong_answer5(m))
            quokka_button.place(x=0, y=260)
            #kangaroo
            kangaroo_img = PIL.Image.open("kangaroo.jpg")
            kangaroo_CTK = customtkinter.CTkImage(kangaroo_img,
                                               size=(130,110))
            kangaroo_button = customtkinter.CTkButton(master=root, image=kangaroo_CTK, text="kangaroo", compound="bottom",
                                                command=lambda m="kangaroo":wrong_answer5(m))
            kangaroo_button.place(x=140, y=260)
            
            #Kookaburra
            kookaburra_img = PIL.Image.open("kookaburra.jpg")
            kookaburra_CTK = customtkinter.CTkImage(kookaburra_img,
                                               size=(130,110))
            kookaburra_button = customtkinter.CTkButton(master=root, image=kookaburra_CTK, text="Kookaburra", compound="bottom",
                                                command= (lambda m="Kookaburra":wrong_answer5(m)))
            kookaburra_button.place(x=280, y=260)
        def Intro5():
            #display instructions for 5th level
            global outback
            outback =customtkinter.CTkLabel(root, text="Next we are going to look for " + "\n"+ "reptiles in the outback!" +"\n" + "Reptiles have scaly skin and lay eggs.", font=("Times New Roman", 12), width=40)
            outback.place(x=30, y=100)
            #continue button to start 5th level
            global cont5
            cont5 = customtkinter.CTkButton(root, text="Continue", command=Level5_options)
            cont5.place(x=30, y=350)
            #collage of reptiles
            global reptiles_collage
            reptiles_collage_image = PIL.Image.open("Reptiles.jpg")
            TK_reptiles_collage = customtkinter.CTkImage(reptiles_collage_image,
                size=(400,400))
            reptiles_collage = customtkinter.CTkLabel(master=root, image=TK_reptiles_collage)
            reptiles_collage.place(x=400, y=0)

        Intro5()
        
    #when complete move on to 5th level
    kookaburra_button.destroy()
    kangaroo_button.destroy()
    quokka_button.destroy()
    SPython_button.destroy()
    FNLizard_button.destroy()
    AFCamel_button.destroy()
    dingo_button.destroy()
    TDevil_button.destroy()
    SGoanna_button.destroy()
    score.place_forget()
    animals_found.place_forget()
    list_correct_animals=""
    points=0
    summary_screen5=customtkinter.CTkLabel(master=root, text=("You've found the following reptiles" + list_correct_animals5), height=400, width=800, bg_color="grey")
    summary_screen5.place(x=0, y=0)
    next_level5=customtkinter.CTkButton(master=root, text=("next level"), width=10, height=5, command=Level6())
    next_level5.place(x=700, y=350)
    
def Level6():
    global level_6_done
    level_6_done=False
    while level_6_done==False:

        def correct_choice6():
            global points
            global score
            global animals_found
            #increments points and adds correct animal to list
            points=points+1
            if points>3:
                level_6_done=True
            score.config(text="SCORE: "+ str(points))
            animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals6)
        def which_button6(m):
            global list_correct_animals6
            #adding to list of correct animals
            list_correct_animals6=list_correct_animals + "\n" + m
            correct_choice6() 
        def wrong_answer6(m):
            global oops6
            global try_again6
            def undo_wrong_answer6() :
                # when try again clicked, returns to level
                oops6.destroy()
                try_again6.destroy() 
            #message for incorrect answer
            oops6=customtkinter.CTkLabel(master=root, text=("Oops, that isn't an invertebrate!" + "\n" + "Remember invertebrates don't have a spine and are really tiny!"), height=400, width=800, bg_color="grey")
            oops3.place(x=0, y=0)
            try_again6=customtkinter.CTkButton(master=root, text=("Try again"), width=10, height=5, command=undo_wrong_answer6)
            try_again6.place(x=700, y=350)
        def Level6_options():
            global points
            score.place(x=550, y=0)
            animals_found.place(x=450, y=50)
            #back option
            back6=customtkinter.CTkButton(master=root, text=("back"), width=10, height=5, command=Level5())
            back6.place(x=700, y=350)
            #resetting screen
            backyard.destroy()
            cont6.destroy()
            invertebrates_collage.destroy()
            #making options global- to delete later
            global WSkink_button
            global honeyeater_button
            global MButterfly_button
            global ladybug_button
            global GShephard_button
            global GSnake_button
            global earthworm_button
            global FMouse_button
            global ECottontail_button
            #displaying options
            #Eastern Cottontail
            ECottontail_img = PIL.Image.open("eastern-cottontail.jpg")
            ECottontail_CTK = customtkinter.CTkImage(ECottontail_img,
                                               size=(130,110))
            ECottontail_button = customtkinter.CTkButton(master=root, image=ECottontail_CTK, text="Eastern Cottontail", compound="bottom",
                                                command=lambda m="Eastern Cottontail":wrong_answer6(m))
            ECottontail_button.place(x=0, y=0)
            #Field Mouse
            FMouse_img = PIL.Image.open("field-mouse.jpg")
            FMouse_CTK = customtkinter.CTkImage(FMouse_img,
                                               size=(130,110))
            FMouse_button = customtkinter.CTkButton(master=root, image=FMouse_CTK, text="Field Mouse", compound="bottom",
                                                command=lambda m="Field Mouse":wrong_answer6(m))
            FMouse_button.place(x=140, y=0)
            #earthworm
            earthworm_img = PIL.Image.open("earthworm.jpg")
            earthworm_CTK = customtkinter.CTkImage(earthworm_img,
                                               size=(130,110))
            earthworm_button = customtkinter.CTkButton(master=root, image=earthworm_CTK, text="earthworm", compound="bottom",
                                                command=lambda m="earthworm":which_button6(m))
            earthworm_button.place(x=280, y=0)
            #Garter Snake
            GSnake_img = PIL.Image.open("garter-snake.jpg")
            GSnake_CTK = customtkinter.CTkImage(GSnake_img,
                                               size=(130,110))
            GSnake_button = customtkinter.CTkButton(master=root, image=GSnake_CTK, text="Garter Snake", compound="bottom",
                                                command=lambda m="Garter Snake":wrong_answer6(m))
            GSnake_button.place(x=280, y=135)
            #German Shephard
            GShephard_img = PIL.Image.open("german-shephard.jpg")
            GShephard_CTK = customtkinter.CTkImage(GShephard_img,
                                               size=(130,110))
            GShephard_button = customtkinter.CTkButton(master=root, image=GShephard_CTK, text="German Shephard", compound="bottom",
                                                command=lambda m="German Shephard":wrong_answer6(m))
            GShephard_button.place(x=140, y=135)
            #ladybug
            ladybug_img = PIL.Image.open("ladybug.jpg")
            ladybug_CTK = customtkinter.CTkImage(ladybug_img,
                                               size=(130,110))
            ladybug_button = customtkinter.CTkButton(master=root, image=ladybug_CTK, text="ladybug", compound="bottom",
                                                command=lambda m="ladybug":which_button6(m))
            ladybug_button.place(x=0, y=135)
            #Monarch Butterfly
            MButterfly_img = PIL.Image.open("monarch-butterfly.jpg")
            MButterfly_CTK = customtkinter.CTkImage(MButterfly_img,
                                               size=(130,110))
            MButterfly_button = customtkinter.CTkButton(master=root, image=MButterfly_CTK, text="Monarch Butterfly", compound="bottom",
                                                command=lambda m="Monarch Butterfly":which_button6(m))
            MButterfly_button.place(x=0, y=260)
            #honeyeater
            honeyeater_img = PIL.Image.open("honeyeater.jpg")
            honeyeater_CTK = customtkinter.CTkImage(honeyeater_img,
                                               size=(130,110))
            honeyeater_button = customtkinter.CTkButton(master=root, image=honeyeater_CTK, text="honeyeater", compound="bottom",
                                                command=lambda m="honeyeater":wrong_answer6(m))
            honeyeater_button.place(x=140, y=260)
            
            #Water Skink
            WSkink_img = PIL.Image.open("water-skink.jpg")
            WSkink_CTK = customtkinter.CTkImage(WSkink_img,
                                               size=(130,110))
            WSkink_button = customtkinter.CTkButton(master=root, image=WSkink_CTK, text="Water Skink", compound="bottom",
                                                command= (lambda m="Water Skink":wrong_answer6(m)))
            WSkink_button.place(x=280, y=260)
        def Intro6():
            #display instructions for 6th level
            global backyard
            backyard =customtkinter.CTkLabel(root, text="Next we are going to look for " + "\n"+ "invertebrates in my backyard" +"\n" + "Invertebrates don't have a spine and are often quite small.", font=("Times New Roman", 12), width=40)
            backyard.place(x=30, y=100)
            #continue button to start 6th level
            global cont6
            cont6 = customtkinter.CTkButton(root, text="Continue", command=Level6_options)
            cont6.place(x=30, y=350)
            #collage of invertebrates
            global invertebrates_collage
            invertebrates_collage_image = PIL.Image.open("invertebrates.jpg")
            TK_invertebrates_collage = customtkinter.CTkImage(invertebrates_collage_image,
                size=(400,400))
            invertebrates_collage = customtkinter.CTkLabel(master=root, image=TK_invertebrates_collage)
            invertebrates_collage.place(x=400, y=0)

        Intro6()
        
    #when complete move on to end screen
    WSkink_button.destroy()
    honeyeater_button.destroy()
    MButterfly_button.destroy()
    ladybug_button.destroy()
    GShephard_button.destroy()
    GSnake_button.destroy()
    earthworm_button.destroy()
    FMouse_button.destroy()
    ECottontail_button.destroy()
    score.place_forget()
    animals_found.place_forget()
    list_correct_animals=""
    points=0
    summary_screen6=customtkinter.CTkLabel(master=root, text=("You've found the following invertebrates" + list_correct_animals6), height=400, width=800, bg_color="grey")
    summary_screen6.place(x=0, y=0)
    next_level6=customtkinter.CTkButton(master=root, text=("next level"), width=10, height=5, command=endscreen())
    next_level6.place(x=700, y=350)

def endscreen():
    congrats=customtkinter.CTkLabel(master=root, text=("Congrats, you are now an expert on the 6 categories of animals"), height=400, width=800, bg_color="grey")
    congrats.place(x=0, y=0)
    replay=customtkinter.CTkButton(master=root, text=("replay"), width=10, height=5, command=start())
    replay.place(x=700, y=350)

global intro
intro = Label(root, text="Animal Classification Game", height = 3, width=25, font=("Times New Roman", 18))
intro.place(x=250, y=150)

global begin
begin = Button(root, text="Begin", command=start)
begin.place(x=350, y=250)

score = Label(root, text="SCORE: ", font=(("Times New Roman"), 18))

animals_found = Label(root, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))












root.mainloop()
