import tkinter as tk


class Application:
    """Conceptual class for GUI application
    :param master: main window of an application, default to None
    :type master: tkinter.Tk
    """
    def __init__(self, master: tk.Tk = None):
        """Constructor method
        :return: None
        :rtype: NoneType
        """
        # Parent setting
        # # Size of the window
        master.geometry('420x420')

        # # Title of the window
        master.title('Ejercicio 10.B')

        # # Max and min window size
        master.maxsize(width=420, height=420)
        master.minsize(width=257, height=257)

        # Variable
        self._lbelements = ['Pan', 'Manzana', 'Tomate', 'Ternera', 'Quita grasa',
                            'Bayeta', 'Escoba', 'Champú', 'Esponja', 'Crema hidratante']

        # Widgets
        self._lb = tk.Listbox()
        self._l = tk.Label()

        # Frame
        # # Init main frame
        self._main = tk.Frame(master=master, height=420, width=420)
        self._main.grid_propagate(True)
        self._main.pack(fill='both', expand=True)
        self._main.rowconfigure(index=0, weight=420)
        self._main.columnconfigure(index=0, weight=420)

        # # Init listbox frame
        self._flb = tk.Frame(master=self._main, height=1, width=1)
        self._flb.pack(side='top', anchor='nw', expand=False)
        self._flb.rowconfigure(index=0, weight=1)
        self._flb.columnconfigure(index=0, weight=1)

        # # Init label frame
        self._fl = tk.Frame(master=self._main, height=1, width=1)
        self._fl.pack(side='top', anchor='nw', expand=False)
        self._fl.rowconfigure(index=0, weight=1)
        self._fl.columnconfigure(index=0, weight=1)

        # Place widgets into frames
        self._createWidgets()

        # Start application
        master.mainloop()

    def _createWidgets(self):
        """Method to instance and place a listbox and label widgets
        :return: None
        :rtype: NoneType
        """
        # Listbox
        # # Init radio buttons
        self._lb = tk.Listbox(master=self._flb)
        for item in self._lbelements:
            self._lb.insert(tk.END, item)
        self._lb.grid(column=0, row=0, ipadx=0, ipady=0, padx=10, pady=5, sticky=tk.N + tk.W)
        self._l = tk.Label(master=self._fl, text='Seleccione un producto')
        self._l.grid(column=0, row=1, ipadx=0, ipady=0, padx=10, pady=5, sticky=tk.N + tk.W)


def mainApp() -> tuple[int, Application or None]:
    """Main function to start Application class
    :return: Application class, None when error exist
    :rtype: tuple[tk.TclError, Application]
    """
    # Main window of an application
    root = tk.Tk()

    try:
        # Class instance
        app = Application(master=root)
        return 0, app
    except tk.TclError:
        return 1, None
