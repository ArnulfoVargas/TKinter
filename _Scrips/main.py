from tkinter import  *

def init_window():
    ###############################################
    ################  Init Window  ################
    ###############################################

    # Starting Window and title
    app = Tk()
    app.title("Restaurant Managment")

    # Positioning the app at the middle of the screen and setting up its width and height
    center_x = int((app.winfo_screenwidth()/2) - (1020/2))
    center_y = int((app.winfo_screenheight()/2) - (630/2))
    res = f'1020x630+{center_x}+{center_y}'
    app.geometry(res)

    # Non resizable window
    app.resizable(0,0)

    # App bg
    app.config(bg='#D9D9D9')

    #############################################
    ################  Top frame  ################
    #############################################

    top_pannel = Frame(app, bd = .5, relief= FLAT)
    top_pannel.pack(side=TOP)
    title = Label(top_pannel, text = "Restaurant Admin", fg ="#272D40", font = ("Consolas", 68, 'bold'), bg = "#D9D9D9", width = 20)
    title.grid(row = 0, column = 0)

    ##############################################
    ################  Left frame  ################
    ##############################################

    left_pannel = Frame(app, bd = .5, relief = FLAT)
    left_pannel.pack(side=LEFT)

    # Costs pannel
    costs_pannel = Frame(left_pannel, bd = .5, relief = FLAT)
    costs_pannel.pack(side = BOTTOM)

    # Foods pannel
    foods_pannel = LabelFrame(left_pannel, bd = .5, relief = FLAT, text = "Food", font = ("Consolas", 22, 'bold'), bg = "#D9D9D9", fg="#272D40")
    foods_pannel.pack(side = LEFT)

    # Drinks pannel
    drinks_pannel = LabelFrame(left_pannel, bd=.5, relief=FLAT, text="Drinks", font=("Consolas", 22, 'bold'), bg="#D9D9D9", fg = "#272D40")
    drinks_pannel.pack(side=LEFT)

    # Desserts pannel
    desserts_pannel = LabelFrame(left_pannel, bd=.5, relief=FLAT, text="Drinks", font=("Consolas", 22, 'bold'), bg="#D9D9D9", fg = "#272D40")
    desserts_pannel.pack(side=LEFT)

    # Products
    foods = ["Baguette", "Kebab", "Taco", "Pizza", "Hot-Dog", "Pozole", "Tamal", "Sushi"]
    drinks = ["Coca-Cola", "Pepsi", "Fanta", "Lemonade", "Orange Juice", "Apple Juice", "Coffee", "Tea"]
    desserts = ["Ice-cream", "Flan", "Muffin", "Mousse", "Cake", "Cup-cake", "Biscuit","Gelatin"]

    # Check-list
    food_variables = []
    food_entries = []
    food_text = []

    drinks_variables = []
    drinks_entries = []
    drinks_text = []

    desserts_variables = []
    desserts_entries = []
    desserts_text = []

    for i in range(8):
        # Create Food Check-List
        food_variables.append("")
        food_variables[i] = IntVar()
        food_cl = Checkbutton(foods_pannel, text = foods[i], font=("Consolas", 16, 'bold'), onvalue = 1, offvalue = 0, bg = "#D9D9D9", variable = food_variables[i], fg = "#8C8B88")
        food_cl.grid(row = i, column = 0, sticky = W)

        # Create Food Entries
        food_entries.append('')
        food_text.append('')
        food_text[i] = StringVar()
        food_text[i].set('0')
        food_entries[i] = Entry(foods_pannel, font=("Consolas", 16, 'bold'), bd = 1, width = 6, state = DISABLED, textvariable = food_text[i])
        food_entries[i].grid(row = i, column = 1)

        # Create Drinks Check-List
        drinks_variables.append("")
        drinks_variables[i] = IntVar()
        drinks_cl = Checkbutton(drinks_pannel, text=drinks[i], font=("Consolas", 16, 'bold'), onvalue=1, offvalue=0,bg="#D9D9D9", variable = drinks_variables[i], fg = "#8C8B88")
        drinks_cl.grid(row=i, column=0, sticky=W)

        # Create Drinks Entries
        drinks_entries.append('')
        drinks_text.append('')
        drinks_text[i] = StringVar()
        drinks_text[i].set('0')
        drinks_entries[i] = Entry(drinks_pannel, font=("Consolas", 16, 'bold'), bd=1, width=6, state=DISABLED, textvariable=drinks_text[i])
        drinks_entries[i].grid(row=i, column=1)

        # Create Dessert Check-List
        desserts_variables.append("")
        desserts_variables[i] = IntVar()
        desserts_cl = Checkbutton(desserts_pannel, text=desserts[i], font=("Consolas", 16, 'bold'), onvalue=1, offvalue=0,bg="#D9D9D9", variable = desserts_variables[i], fg = "#8C8B88")
        desserts_cl.grid(row=i, column=0, sticky=W)

        # Create Desserts Entries
        desserts_entries.append('')
        desserts_text.append('')
        desserts_text[i] = StringVar()
        desserts_text[i].set('0')
        desserts_entries[i] = Entry(desserts_pannel, font=("Consolas", 16, 'bold'), bd=1, width=6, state=DISABLED, textvariable=desserts_text[i])
        desserts_entries[i].grid(row=i, column=1)

    ###############################################
    ################  Right frame  ################
    ###############################################

    right_pannel = Frame(app, bd=.5, relief=FLAT)
    right_pannel.pack(side=RIGHT)

    # Calculator pannel
    calculator_pannel = Frame(right_pannel, bd=.5, relief=FLAT, bg="#D9D9D9")
    calculator_pannel.pack()

    # Billing pannel
    billing_pannel = Frame(right_pannel, bd=.5, relief=FLAT, bg="#D9D9D9")
    billing_pannel.pack()

    # Buttons pannel
    buttons_pannel = Frame(right_pannel, bd=.5, relief=FLAT, bg="#D9D9D9")
    buttons_pannel.pack()

    return app

if __name__ == "__main__":
    init_window().mainloop()