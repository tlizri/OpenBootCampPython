from pickle import dump, load


class ObjectManager:
    """Conceptual representation for a class manager
    :param _path: path pointed to file directory
    :type _path: str
    :param _filename: binary file name
    :type _filename: str
    :param _file: binary I/O stream
    :type _file: BufferedWriter
    :param _objeto: class to manage
    :type _objeto: class
    """
    _path = None
    _filename = None
    _file = None
    _objeto = None

    def __init__(self, path: str, filename: str, objeto=None):
        """Constructor method
        """
        self._path = path
        self._filename = filename
        self._objeto = objeto
        self._file = None

    def __del__(self):
        """Destructor method
        """
        del self._path, self._filename, self._file, self._objeto

    def _openFile(self, mode: str):
        """Private method to open a binary file
        :param mode: mode to open the binary file
        :type mode: str
        """
        self._file = open(f'{self._path}{self._filename}', mode)

    def _closeFile(self):
        """Private method to close a file
        """
        self._file.close()
        self._file = None

    def saveObject(self):
        """Method to save a class if provided
        """
        if self._objeto is None:
            pass
        else:
            self._openFile('wb')
            dump(self._objeto, self._file)
            self._closeFile()

    def loadObject(self):
        """Method to load and return a class from a binary file
        :return: loaded class or None if not loaded
        :rtype: class
        """
        try:
            self._openFile('rb')
            self._objeto = load(self._file)
            self._closeFile()
            return self._objeto
        except FileNotFoundError:
            return None
