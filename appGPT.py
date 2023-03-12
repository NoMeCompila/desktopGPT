import textwrap
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
                        text="Igresa una pregunta, una petición, un texto a resumir, un listado, etc."
                             "\nTu imaginación es el límite",
                        bg="#444654")
    input_label.config(fg="white", font=("Roboto", 12))
    input_label.pack(pady=10)

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

    # button = Button(windows, text="Haz clic aquí") # command=button_click
    # button.pack()

    # Crear un botón y asociar la función de clic
    button = Button(windows, text="Haz clic aquí", bg="gray15", fg="white", relief="flat", cursor="hand2", bd=0, padx=10)

    # Establecer el radio de borde para hacer el botón redondeado
    button.config(width=10, height=2, borderwidth=0, highlightthickness=0, highlightbackground="gray",
                  highlightcolor="gray", bd=0, pady=0, padx=10, takefocus=0, )

    # Agregar el botón a la ventana
    button.pack(pady=10)
    windows.mainloop()
