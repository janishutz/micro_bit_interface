import serial
import bin.com.csv_parsers
import bin.com.lib


cvr = bin.com.csv_parsers.CsvRead()
com = bin.com.lib.Com()


class RunCommand:
    def __init__(self):
        self.__all_commands = []
        self.__return = ""

    def runcommand(self, command, command_list_path):
        self.__all_commands = cvr.importing(command_list_path).pop(0)
        if command in self.__all_commands:
            try:
                com.connect(19200, "")
                com.send(command)
                self.__return = f"[micro:bit - {command}] The command executed successfully"
            except serial.SerialException as e:
                self.__return = f"[micro:bit - {command}]: An error occurred running the command. (Maybe disconnected or no permission?) {e}"
        else:
            self.__return = "-micro:bit - No such command"
        return self.__return
