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
        master.title('Ejercicio 9.A')

        # # Max and min window size
        master.maxsize(width=400, height=400)
        master.minsize(width=220, height=220)

        # Variable
        self._rbv = tk.IntVar()

        # Widgets
        self._rb1 = tk.Radiobutton()
        self._rb2 = tk.Radiobutton()
        self._rb3 = tk.Radiobutton()
        self._bt = tk.Button()

        # Frame
        # # Init main frame
        self._main = tk.Frame(master=master, height=420, width=420)
        self._main.grid_propagate(False)
        self._main.pack(fill='both', expand=True)
        self._main.rowconfigure(index=0, weight=1)
        self._main.columnconfigure(index=0, weight=1)

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

    def _reiniciar(self):
        """Method to restore radio button selections
        :return: None
        :rtype: NoneType
        """
        self._rbv.set(False)

    def _createWidgets(self):
        """Method to instance and place button widgets
        :return: None
        :rtype: NoneType
        """
        # Radio buttons
        # # Init radio buttons
        self._rb1 = tk.Radiobutton(self._frb, text='Opcion 1', value=1, variable=self._rbv)
        self._rb2 = tk.Radiobutton(self._frb, text='Opcion 2', value=2, variable=self._rbv)
        self._rb3 = tk.Radiobutton(self._frb, text='Opcion 3', value=3, variable=self._rbv)
        # # Place radio buttons
        self._rb1.grid(column=0, row=0, ipadx=0, ipady=0, padx=10, pady=5, sticky=tk.W + tk.N)
        self._rb2.grid(column=0, row=1, ipadx=0, ipady=0, padx=10, pady=5, sticky=tk.W + tk.N)
        self._rb3.grid(column=0, row=2, ipadx=0, ipady=0, padx=10, pady=5, sticky=tk.W + tk.N)

        # Button
        # # Init button
        self._bt = tk.Button(self._fb, command=lambda: self._reiniciar(), text='Reiniciar')
        # # Place button
        self._bt.grid(column=0, row=0, ipadx=0, ipady=0, padx=10, pady=5, sticky=tk.S)


def mainApp() -> tuple[int, Application or None]:
    """Main function to start Application class
    :return: Application class, None when error exist
    :rtype: Application
    """
    # Main window of an application
    root = tk.Tk()

    try:
        # Class instance
        app = Application(master=root)
        return 0, app
    except tk.TclError:
        return 1, None
