import tkinter as tk


class Application:
    """Conceptual class for GUI application
    :param master: main window of an application, default to None
    :type master: tkinter.Tk
    """

    def __init__(self, master: tk.Tk = None):
        """Constructor method
        """
        # Parent setting
        # # Size of the window
        master.geometry('420x420')

        # # Title of the window
        master.title('Ejercicio 10.A')

        # # Max and min window size
        master.maxsize(width=400, height=400)
        master.minsize(width=220, height=220)

        # Variable
        self._rbv = tk.StringVar(value=' ')

        # Widgets
        self._rb1 = tk.Radiobutton()
        self._rb2 = tk.Radiobutton()
        self._rb3 = tk.Radiobutton()
        self._bt = tk.Button()
        self._lb = tk.Label()

        # Frame
        # # Init main frame
        self._main = tk.Frame(master=master, height=420, width=420)
        self._main.grid_propagate(True)
        self._main.pack(fill='both', expand=True)
        self._main.rowconfigure(index=0, weight=420)
        self._main.columnconfigure(index=0, weight=420)

        # # Init button frame
        self._fb = tk.Frame(master=self._main, height=1, width=1)
        self._fb.pack(side='bottom', expand=False)
        self._fb.rowconfigure(index=0, weight=1)
        self._fb.columnconfigure(index=0, weight=1)

        # # Init radio buttons frame
        self._frb = tk.Frame(master=self._main, height=1, width=1)
        self._frb.pack(side='left', expand=False)
        self._frb.rowconfigure(index=0, weight=1)
        self._frb.columnconfigure(index=0, weight=1)

        # Place widgets into frames
        self._createWidgets()

        # Start application
        master.mainloop()

    def _cambiarLabel(self):
        """Method to change label text
        :return: None
        :rtype: NoneType
        """
        self._lb.config(text=self._rbv.get())

    def _reiniciar(self):
        """Method to restore radio button selections
        :return: None
        :rtype: NoneType
        """
        self._rbv.set(' ')

    def _createWidgets(self):
        """Method to instance and place buttons and label widgets
        :return: None
        :rtype: NoneType
        """
        # Radio buttons
        # # Init radio buttons
        self._rb1 = tk.Radiobutton(self._frb, text='Opción 1', value='Opción 1',
                                   variable=self._rbv, command=lambda: self._cambiarLabel())
        self._rb2 = tk.Radiobutton(self._frb, text='Opción 2', value='Opción 2',
                                   variable=self._rbv, command=lambda: self._cambiarLabel())
        self._rb3 = tk.Radiobutton(self._frb, text='Opción 3', value='Opción 3',
                                   variable=self._rbv, command=lambda: self._cambiarLabel())

        # # Place radio buttons
        self._rb1.grid(column=0, row=0, ipadx=0, ipady=0, padx=10, pady=5, sticky=tk.W + tk.N)
        self._rb2.grid(column=0, row=1, ipadx=0, ipady=0, padx=10, pady=5, sticky=tk.W + tk.N)
        self._rb3.grid(column=0, row=2, ipadx=0, ipady=0, padx=10, pady=5, sticky=tk.W + tk.N)

        # Button and label
        # # Init button and label
        self._bt = tk.Button(self._fb, command=lambda: self._reiniciar(), text='Reiniciar')
        self._lb = tk.Label(self._fb, textvariable=self._rbv)
        # # Place button and label
        self._lb.grid(column=0, row=0, ipadx=0, ipady=0, padx=10, pady=5, sticky=tk.N)
        self._bt.grid(column=0, row=1, ipadx=0, ipady=0, padx=10, pady=5, sticky=tk.S)


def mainApp() -> tuple[int, Application or None]:
    """Main function to start Application class
    :return: Application class, None when error exist
    :rtype: tuple[tk.TclError, Application or None]
    """
    # Main window of an application
    root = tk.Tk()

    try:
        # Class instance
        app = Application(master=root)
        return 0, app
    except tk.TclError:
        return 1, None
