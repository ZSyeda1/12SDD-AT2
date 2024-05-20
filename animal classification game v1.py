
import PIL.Image
from PIL import ImageTk, Image
from tkinter import *
import customtkinter

root = Tk()
root.title('animal classification game')
root.geometry("800x400")

global points
points=0

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
    score.place(x=600, y=50)
    animals_found.place(x=600, y=100)
    #resetting screen
    Amazon.destroy()
    cont.destroy()
    birds_collage.destroy()
    #displaying options
    #Macaw
    macaw_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\birds\\blue&gold_macaw.jpg")
    macaw_CTK = customtkinter.CTkImage(macaw_img,
                                       size=(130,120))
    macaw_button = customtkinter.CTkButton(master=root, image=macaw_CTK, text="Blue and Gold Macaw", compound="bottom",
                                        command=lambda m="Amazon Bird":which_button(m))
    macaw_button.place(x=5, y=5)
    #capybara
    capybara_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\capybara.jpeg")
    capybara_CTK = customtkinter.CTkImage(capybara_img,
                                       size=(130,120))
    capybara_button = customtkinter.CTkButton(master=root, image=capybara_CTK, text="capybara", compound="bottom",
                                        command=lambda m="Amazon Bird":which_button(m))
    capybara_button.place(x=140, y=5)
    #jaguar
    jaguar_img = PIL.Image.open("D:\\yr12\\project pics\\level 1\\other\\jaguar.jpeg")
    jaguar_CTK = customtkinter.CTkImage(jaguar_img,
                                       size=(130,120))
    jaguar_button = customtkinter.CTkButton(master=root, image=jaguar_CTK, text="jaguar", compound="bottom",
                                        command=lambda m="Amazon Bird":which_button(m))
    jaguar_button.place(x=275, y=5)
    
def correct_choice():
    global points
    points=points+1
    score.config(text="score: "+ str(points))
    animals_found.config(text= "animals found: "+ "\n" + list_correct_animals)

def which_button(m):
    global list_correct_animals
    list_correct_animals=m
    correct_choice()



                        

intro = Label(root, text="Animal Classification Game", height = 3, width=25, font=("Times New Roman", 18))
intro.place(x=250, y=150)

begin = Button(root, text="Begin", command=start)
begin.place(x=350, y=250)

score = Label(root, text="score: ", height=5, width=10)

animals_found = Label(root, text="animals found: ", height=20, width=15)












root.mainloop()
