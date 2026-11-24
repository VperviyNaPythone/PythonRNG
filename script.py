import tkinter as tk
from tkinter import ttk
import random

from audio import mythicsound, legsound, ultrasound, brsound, clicksound
from config import (
    CHANCES as chances,
    FREE_GLOVE_CHANCES as freegchances,
    LUCKY_GLOVE_CHANCES as luckychances,
    RARITIES as rarities,
    RARITY_COLORS as rarity_colors,
)
from storage import load_save, save_game


balance, mythics, legendaries, ultras, BREAKTHROUGH, rolls, lucky_glove_buy = load_save()

free_glove = False
lucky_glove = False
equippedgloves = 0


autorun = False

window = tk.Tk()
window.title("Clicker")
window.geometry("1200x850")






window.configure(bg="#000000")









window.option_add("*Background", "#000000")
window.option_add("*Foreground", "#ffffff")
window.option_add("*Button.Background", "#1c1c1c")
window.option_add("*Button.Foreground", "#ffffff")
window.option_add("*Button.activeBackground", "#333333")
window.option_add("*Button.activeForeground", "#ffffff")
window.option_add("*Button.borderWidth", "0")


style = ttk.Style()
style.theme_use('clam')


style.configure("TNotebook", background="#000000", borderwidth=0, padding=0)


style.configure("TNotebook.Tab",
                background="#1c1c1c",
                foreground="#ffffff",
                font=("Arial", 14, "bold"),
                padding=[10, 5],
                borderwidth=0)


style.map("TNotebook.Tab",
          background=[("selected", "#333333"), ("active", "#252525")],
          foreground=[("selected", "#ffffff")])

style.configure("TFrame", background="#000000", borderwidth=0)


style.configure("TLabel", background="#000000", foreground="#ffffff")









notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)


notebook.add(tab1, text="Game")
notebook.add(tab2, text="Inventory")
notebook.add(tab3, text="Gloves")









def reset_cooldown():
    roll_button.config(state="normal", text="Roll")






def roll():

    global rarities, balance, mythics, legendaries, ultras, BREAKTHROUGH, rolls, autorun, free_glove, lucky_glove



    clicksound.play()

    if rolls >= 500:
        roll_button.config(state="normal", text="Roll")
    else:
        roll_button.config(state="disabled", text="Roll")

    if autorun == True:
        roll_button.config(state="disabled", text="Roll")
    else:
        window.after(250, reset_cooldown)


    rolls += 1



    rolls_label.config(text=f"Rolls: {rolls}")



    roll_button.config(text="Roll")

    if lucky_glove:
        print("luckbuff active")
        result = random.choices(rarities, weights=luckychances, k=1)[0]
    elif free_glove:
        print("freebuff active")
        result = random.choices(rarities, weights=freegchances, k=1)[0]
    else:
        print("all buff unactive")
        result = random.choices(rarities, weights=chances, k=1)[0]

    print(f"[ПРИНТ 2] Итоговый результат (ушел на экран): {result}")

    result_label.config(text=result, foreground=rarity_colors[result])


    if result == "Arcane":
        mythicsound.play()
        mythics += 1
        balance += 5
        balance_label.config(text=f"Balance: {balance}")
        mythics_label.config(text=f"Arcane: {mythics}")

    elif result == "Lily":
        legsound.play()
        legendaries += 1
        balance += 10
        balance_label.config(text=f"Balance: {balance}")
        legendaries_label.config(text=f"Lily: {legendaries}")

    elif result == "Overture":
        ultrasound.play()
        ultras += 1
        balance += 15
        balance_label.config(text=f"Balance: {balance}")
        ultras_label.config(text=f"Overture: {ultras}")



    elif result == "BREAKTHROUGH":
        brsound.play()
        BREAKTHROUGH += 1
        balance += 250
        balance_label.config(text=f"Balance: {balance}")
        breakthrough_label.config(text=f"???: {BREAKTHROUGH}")



    window.after(250, reset_cooldown)





def autotoggle():
    global autorun
    autorun = not autorun
    if autorun:
        autoroll()



def autoroll():
    if autorun == False:
        roll_button.config(state="normal", text="Roll")
        return
    else:
        roll_button.config(state="disabled", text="Roll")
        roll()

    window.after(250, autoroll)







def free_glovetog():
    global free_glove, equippedgloves, lucky_glove

    if equippedgloves >= 1:
        lucky_glove = False
        free_glove = False
        free_glovebut.config(state="normal", text="Free Glove")
        lucky_glovebut.config(state="normal", text="Lucky glove \n (need 1 arcane)")
        equippedgloves = 0
    else:





        free_glove = not free_glove


        if free_glove == True:
            equippedgloves += 1
            free_glovebut.config(state="normal", text="Unequip")
        else:
            equippedgloves -= 1
            free_glovebut.config(state="normal", text="Free Glove")



def lucky_glovetog():
    global lucky_glove, mythics, lucky_glove_buy, free_glove, equippedgloves

    if equippedgloves >= 1:
        lucky_glove = False
        free_glove = False
        free_glovebut.config(state="normal", text="Free Glove")
        lucky_glovebut.config(state="normal", text="Lucky glove \n (need 1 arcane)")
        equippedgloves = 0
    else:



        if lucky_glove_buy == 0:

            if mythics >= 1:
                mythics -= 1
                lucky_glove_buy += 1
                mythics_label.config(text=f"Arcane: {mythics}")
            else:
                return




        lucky_glove = not lucky_glove
        if lucky_glove == True:
            equippedgloves += 1
            lucky_glovebut.config(state="normal", text="Unequip")
        else:
            equippedgloves -= 1
            lucky_glovebut.config(state="normal", text="Lucky glove \n (need 1 arcane)")







def save():
    save_game(balance, mythics, legendaries, ultras, BREAKTHROUGH, rolls, lucky_glove_buy)

#OTHER UI(working 100%)

balance_label = ttk.Label(tab1, text=f"Balance: {balance}", font=("Arial", 24))
balance_label.place(x=20, y=20)

result_label = ttk.Label(tab1, text="Нажми Roll", font=("Arial", 42), justify = tk.CENTER, anchor = tk.CENTER)
result_label.place(x=450, y=100)

#MYTHIC AURAS

mythics_label = ttk.Label(tab2, text=f"Arcane: {mythics}", font=("Arial", 24))
mythics_label.place(x=20, y=100)




#LEGENDARY AURAS

legendaries_label = ttk.Label(tab2, text=f"Lily: {legendaries}", font=("Arial", 24))
legendaries_label.place(x=20, y=140)



#ULTRA AURAS


ultras_label = ttk.Label(tab2, text=f"Overture: {ultras}", font=("Arial", 24))
ultras_label.place(x=20, y=180)




#BREAKTHROUGH AURAS


breakthrough_label = ttk.Label(tab2, text=f"???: {BREAKTHROUGH}", font=("Arial", 24))
breakthrough_label.place(x=20, y=220)



#OTHER


rolls_label = ttk.Label(tab1, text=f"Rolls: {rolls}", font=("Arial", 24))
rolls_label.place(x=20, y=60)

needing_label = ttk.Label(tab1, text="You need 500 rolls for quick roll!", font=("Arial", 24))
needing_label.place(x=730, y=760)

roll_button = tk.Button(tab1, text="Roll", command=roll, font=("Arial", 30))
roll_button.place(x=390, y=300, width=400, height=400)

save_button = tk.Button(tab1, text="Save", command=save, font=("Arial", 30))
save_button.place(x=20, y=700)

auto_button = tk.Button(tab1, text="Auto-Roll", command=autotoggle,font=("Arial", 30))
auto_button.place(x=800, y=300)


inventory_label = ttk.Label(tab2, text="| Inventory |", font=("Arial", 30))
inventory_label.place(x=20, y=20)





#GLOVES UI

free_glovebut = tk.Button(tab3, text="Free Glove", command=free_glovetog, font=("Arial", 14))
free_glovebut.place(x=20, y=20, width=100, height=100)

lucky_glovebut = tk.Button(tab3, text="Lucky glove \n (need 1 arcane)", command=lucky_glovetog)
lucky_glovebut.place(x=160, y=20, width=100, height=100)




window.mainloop()







