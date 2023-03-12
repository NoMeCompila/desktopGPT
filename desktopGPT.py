from tkinter import *



if __name__ == '__main__':
    # create a windows and set a title
    windows = Tk()
    windows.title('DesktopGPT')

    # arithmetic calculation to always open the windows at the center of the screen
    screen_width = windows.winfo_screenwidth()
    screen_height = windows.winfo_screenheight()
    windows_width = 700
    windows_height = 650
    pos_x = int(screen_width / 2 - windows_width / 2)
    pos_y = int(screen_height / 2 - windows_height / 2)
    windows.geometry(f"{windows_width}x{windows_height}+{pos_x}+{pos_y}")

    # set the windows color
    windows.configure(background="#444654")

    # chat text label config
    input_label = Label(windows,
                        text="PROMPT",
                        bg="#444654")
    input_label.config(fg="white", font=("Roboto", 12))
    input_label.pack(pady=5)

    # text box to enter prompt
    input_textbox = Text\
            (
                windows,
                height=8,
                width=70,
                bg="#343541",
                fg="white",
                font=("Roboto", 12),
                highlightthickness=1,
                highlightbackground="white"
            )
    input_textbox.pack(pady=10)

    output_label = Label(windows,
                        text="OUTPUT",
                        bg="#444654")
    output_label.config(fg="white", font=("Roboto", 12))
    output_label.pack(pady=5)

    # create an output textbox
    output_textbox = Text\
            (
                windows,
                height=18,
                width=70,
                bg="#343541",
                fg="white",
                font=("Roboto", 12),
                highlightthickness=1,
                highlightbackground="white"
            )
    output_textbox.pack(pady=5)


    def imprimir_hola_mundo():
        output_textbox.insert("end", "Hola Mundo\n")
    # Make a custom button
    button = Button(windows, text="Responder", bg="gray15", fg="white", relief="flat", cursor="hand2", bd=0, padx=10, command=imprimir_hola_mundo)
    button.config(width=10, height=2, borderwidth=0, highlightthickness=0, highlightbackground="gray",
                  highlightcolor="gray", bd=0, pady=0, padx=10, takefocus=0, )
    button.pack(pady=5)
    windows.mainloop()