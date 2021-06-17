import kivy
import webbrowser
import colorama
from colorama import Back, Fore, Style
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang.builder import Builder
from kivy.uix.video import Video

colorama.init(autoreset = True)


Config.set('kivy', 'window_icon', 'Megs.ico')
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'width', 325)
Config.write()

class WindowManager(ScreenManager):
	pass

class HelpWindow(Screen):
	def go(self):
		webbrowser.open('https://discord.gg/ZZx7GDqwdW', new=2)

class LoginWindow(Screen):
	dcname = ObjectProperty(None)
	product = ObjectProperty(None)

	def btn(self):
		print(Fore.GREEN + "Username : ", Fore.GREEN + self.dcname.text)
		print(Fore.GREEN + "Key : ", Fore.GREEN + self.product.text)

with open('panel.kv', encoding='utf8') as fd:
	kv = Builder.load_string(fd.read())

class PanelApp(App):
	def build(self):
		return kv

if __name__ == "__main__":
	PanelApp().run()