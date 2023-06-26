from tkinter import  *

def init_window():
    #Starting Window and title
    app = Tk()
    app.title("Restaurant Managment")

    #Positioning the app at the middle of the screen and setting up its width and height
    center_x = int((app.winfo_screenwidth()/2) - (1020/2))
    center_y = int((app.winfo_screenheight()/2) - (630/2))
    res = f'1020x630+{center_x}+{center_y}'
    app.geometry(res)

    #Non resizable window
    app.resizable(0,0)

    return app

if __name__ == "__main__":
    init_window().mainloop()