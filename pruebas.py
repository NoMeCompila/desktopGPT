import tkinter as tk

if __name__ == '__main__':
    ventana = tk.Tk()

    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    ancho_ventana = 500
    alto_ventana = 500

    pos_x = int(ancho_pantalla/2 - ancho_ventana/2)
    pos_y = int(alto_pantalla/2 - alto_ventana/2)

    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    ventana.mainloop()
