class FileManager:
    """Conceptual representation of a file manager
    :param _path: path.txt pointed to file directory
    :type _path: str
    :param _filename: file name
    :type _filename: str
    :param _file: text input output object
    :type _file: TextIO
    """
    _path = None
    _filename = None
    _file = None

    def __init__(self, path: str, filename: str):
        """Constructor method
        :param path: path.txt pointed to file directory
        :type path: str
        :param filename: file name
        :type filename: str
        """
        self._path = path
        self._filename = filename

    def __del__(self):
        """Destructor method
        :return: None
        :rtype: NoneType
        """
        del self._path, self._filename, self._file

    def _closeFile(self):
        """Private method to close a file
        :return: None
        :rtype: NoneType
        """
        self._file.close()
        self._file = None

    def _openTextFile(self, mode: str):
        """Private method to open a text file
        :param mode: mode to open the text file
        :type mode: str
        :return: None
        :rtype: NoneType
        """
        self._file = open(f'{self._path}{self._filename}', mode)

    def createTextFile(self):
        """Method to create a text file
        :return: None
        :rtype: NoneType
        """
        try:
            self._openTextFile(mode='xt')
            self._closeFile()
        except FileExistsError:
            pass

    def writeTextFile(self, text: str):
        """Method that open a text file, delete its content, write text and close
        :param text: text to be written in the text file
        :type text: str
        :return: None
        :rtype: NoneType
        """
        self._openTextFile('wt')
        self._file.write(text)
        self._closeFile()
