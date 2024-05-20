
import PIL.Image
from PIL import ImageTk, Image
from tkinter import *
import customtkinter

root = Tk()
root.title('animal classification game')
root.geometry("800x400")

global points
points=0
list_correct_animals=""

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
    birds_collage_image = PIL.Image.open("D:\yr12\project pics\level 1\lvl 1 intro.png")
    TK_birds_collage = customtkinter.CTkImage(birds_collage_image,
        size=(400,400))
    birds_collage = customtkinter.CTkLabel(master=root, image=TK_birds_collage, text="")
    birds_collage.place(x=400, y=0)
    
    

def Level1():
    score.place(x=550, y=0)
    animals_found.place(x=450, y=50)
    #resetting screen
    Amazon.destroy()
    cont.destroy()
    birds_collage.destroy()
    #displaying options
    #Macaw
    macaw_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\blue&gold_macaw.jpg")
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
                                        command=lambda m="Toucan Collared Aracari":which_button(m))
    CAToucan_button.place(x=280, y=260)
    
def correct_choice():
    global points
    points=points+1
    score.config(text="SCORE: "+ str(points))
    animals_found.config(text= "ANIMALS FOUND: "+ "\n" + list_correct_animals)

def which_button(m):
    global list_correct_animals
    list_correct_animals=list_correct_animals + "\n" + m
    correct_choice()


def wrong_answer(m):
    global oops
    global try_again
    oops=customtkinter.CTkLabel(master=root, text=("Oops, that isn't a bird!" + "\n" + "Remember birds have feathers and beaks!"), height=400, width=800, bg_color="grey")
    oops.place(x=0, y=0)
    try_again=customtkinter.CTkButton(master=root, text=("Try again"), width=10, height=5, command=undo_wrong_answer)
    try_again.place(x=700, y=350)

def undo_wrong_answer() :
    oops.destroy()
    try_again.destroy()
                        

intro = Label(root, text="Animal Classification Game", height = 3, width=25, font=("Times New Roman", 18))
intro.place(x=250, y=150)

begin = Button(root, text="Begin", command=start)
begin.place(x=350, y=250)

score = Label(root, text="SCORE: ", font=(("Times New Roman"), 18))

animals_found = Label(root, text="ANIMALS FOUND: ", height=10, width=20, font=(("Times New Roman"), 18))












root.mainloop()
