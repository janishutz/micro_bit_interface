import bin.com.csv_parsers

cvr = bin.com.csv_parsers.CsvRead()


class AutoComplete:
    def __init__(self):
        self.__length_command_completion = 0
        self.__command_list = []
        self.__possible_completion = []
        self.item = ""
        self.items = ""
        self.__return_value = []
        self.__return_value_assembly = ""
        self.__command_count = 0
        self.text = ""

    def autocomplete(self, text, command_list_path):
        self.text = str(text).lower()
        if self.text[len(self.text) - 2:] == "\t\n":
            self.text = self.text[:len(self.text) - 2]
        elif self.text[len(self.text) - 1:] == "\t":
            self.text = self.text[:len(self.text) - 1]
        self.__command_list = cvr.importing(command_list_path).pop(0)
        self.__return_value = []
        self.__return_value_assembly = ""
        self.__possible_completion = []
        self.__command_count = 0
        for self.item in self.__command_list:
            if self.text == self.item[:len(self.text)]:
                self.__possible_completion.append(self.item)
            else:
                pass
        if len(self.__possible_completion) < 1:
            self.__return_value = [f"{self.text}\n-micro:bit - No such command", self.text[:len(self.text)]]
        elif len(self.__possible_completion) == 1:
            self.__return_value = ["", str(self.__possible_completion.pop(0))]
        else:
            for self.items in self.__possible_completion:
                self.__return_value_assembly += f"{str(self.items)}               "
                if self.__command_count > 2:
                    self.__return_value_assembly += "\n"
                    self.__command_count = 0
                else:
                    self.__command_count += 1
            self.__return_value.append(self.__return_value_assembly)
            self.__return_value.append(self.text[:len(self.text)])
        return self.__return_value
