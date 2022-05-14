#########################################################
"""@package docstring
Micro:bit Bluetooth Interface, developed by simplePCBuilding, alpha 1.0

This App allows you to connect to a micro:bit via the USB cable and as such transmit to
and recieve Data from it. This file here is the control file for the UI and as such
should not be interfaced with. All the api files are located in the bin directory."""
#########################################################

# IMPORTS
import logging
import os
import configparser
import datetime
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.base import Builder
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
import bin.others.autocomplete
import bin.others.run_command


################################
# VARIABLE SETUP
################
config = configparser.ConfigParser()
config.read('./config/settings.ini')
version_app = f"{config['Info']['version']}{config['Info']['subVersion']}"
ac = bin.others.autocomplete.AutoComplete()
rc = bin.others.run_command.RunCommand()

################################


################################
# LOGGER SETUP
##############

# BASIC SETUP
logging.basicConfig(level=logging.DEBUG, filename="./log/main_log.log", filemode="w")
logs = f"./log/{datetime.datetime.now()}-log-main.log"
logger = logging.getLogger(__name__)

# SETUP OF HANDLER & FORMATTER
handler = logging.FileHandler(logs)
formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(name)s: %(message)s -- %(lineno)d")
handler.setFormatter(formatter)
logger.addHandler(handler)

# FINAL CONFIG & FIRST LOG ENTRY
logger.setLevel(config['Dev Settings']['log_level'])
logger.info(f"Logger initialized, app is running Version: {version_app}")
################################


################################
# SETTINGS HANDLER
##################

class SettingsHandler:
    def __init__(self):
        pass

    def settings_handler(self):
        pass

################################


##############################################################
#                           SCREENS
##############################################################


################################
# LOAD SCREEN
#############

class Load(MDScreen):
    def start_pb(self):
        self.ids.progress.start()


################################


################################
# MAIN SCREEN
#############

class Main(MDScreen):
    pass


################################


################################
# COMMAND SCREEN
################

class Command(MDScreen):
    def autocomplete(self):
        self.text = self.ids.tin.text
        self.input = self.text[len(self.text) - 1:]
        if self.input == "\t":
            self.__ac = ac.autocomplete(self.text, "./bin/data/full_command_list.csv")
            self.__history = self.ids.cmd_out.text
            self.__output_text = self.__history + "\n\n" + str(self.__ac.pop(0))
            self.ids.cmd_out.text = self.__output_text
            self.ids.tin.text = self.__ac.pop(0)
        else:
            pass

    def runcommand(self):
        self.__info = rc.runcommand(self.ids.tin.text, "./bin/data/full_command_list.csv")
        if self.__info == "The command executed successfully":
            logger.debug(f"The following command has been run successfully: {self.ids.tin.text}")
        else:
            logger.debug(f"The following command has failed to run: {self.ids.tin.text}")
        self.ids.tin.text = ""
        self.__history = self.ids.cmd_out.text
        self.__output_text = self.__history + "\n\n" + str(self.__info)
        self.ids.cmd_out.text = self.__output_text


################################


####################################################


################################
# SCREEN MANAGER
################

class RootScreen(ScreenManager):
    pass


################################
# UI MANAGER
################################

class MicrobitInterface(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    logger.info("building app...")

    def build(self):
        self.title = f"Microbit Bluetooth Interface {version_app}"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "BlueGray"
        # self.icon =
        screen_manager.add_widget(Builder.load_file("./bin/gui/load_screen.kv"))
        screen_manager.add_widget(Builder.load_file("./bin/gui/main_screen.kv"))
        screen_manager.add_widget(Builder.load_file("./bin/gui/command_screen.kv"))
        return screen_manager

    # Redirect start instructions to switch screen
    def on_start(self):
        logger.info("App is starting")
        Clock.schedule_once(self.launch_app, 0.5)

    # Switching screens after init
    def launch_app(self, dt):
        screen_manager.current = "HomeScreen"
        screen_manager.transition.duration = 0.2
        screen_manager.transition.direction = "left"


logger.info("App start successful")
MicrobitInterface().run()
