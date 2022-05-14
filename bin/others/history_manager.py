import bin.com.csv_parsers

cvr = bin.com.csv_parsers.CsvRead()
cvw = bin.com.csv_parsers.CsvWrite()


class HistroyManager:
    def __init__(self):
        self.__history = []
        self.__history_mod = []

    def append_history(self, command, path):
        try:
            self.__history_mod = cvr.importing(path).pop(0)
        except IndexError:
            pass
        if command != "":
            self.__history_mod.insert(0, command)
            cvw.write_str(path, self.__history_mod)
        else:
            pass

    def get_history(self, path):
        return cvr.importing(path)
