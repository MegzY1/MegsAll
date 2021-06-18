import kivy
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
import webbrowser

Config.set('kivy', 'window_icon', 'Megs.ico')
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'height', 300)
Config.set('graphics', 'width', 600)
Config.write()

class WindowManager(ScreenManager):
	pass

# Support
class SupportWindow(Screen):
	pass

# Menu
class MenuWindow(Screen):
	pass

# Info
class InfoWindow(Screen):
	pass

class CSGOWindow(Screen):
	pass

class MCWindow(Screen):
	pass

class ChangeLogsWindow(Screen):
	pass

# Cheats	
class HcWindow(Screen):
	def go(self):
		webbrowser.open('https://hags-club.com/news/', new=2)

class ImmunityWindow(Screen):
	def go(self):
		webbrowser.open('https://immunity.digital/', new=2)

class ZeroxWindow(Screen):
	def go(self):
		webbrowser.open('https://0xcheats.net', new=2)

class GTApWindow(Screen):
	def go(self):
		webbrowser.open('https://discord.gg/dJ7YXcFymB', new=2)

class OnetapWindow(Screen):
	def go(self):
		webbrowser.open('https://www.onetap.com', new=2)

class WurstWindow(Screen):				
	def go(self):
		webbrowser.open('https://www.wurstclient.net/download/', new=2)
# Showcase
class ShowcaseWindow(Screen):
	pass

class Showcase2Window(Screen):
	pass

class Showcase3Window(Screen):
	pass

class Showcase4Window(Screen):
	pass

class Showcase5Window(Screen):
	pass

class Showcase6Window(Screen):
	pass	

# Buy
class BuyWindow(Screen):
	def go(self):
		webbrowser.open('https://discord.gg/VmG7pEaVar', new=2)

class BuyCSGOWindow(Screen):
	def go(self):
		webbrowser.open('https://discord.gg/ZZx7GDqwdW', new=2)

with open('Megs.kv', encoding='utf8') as fd:
	kv = Builder.load_string(fd.read())

class MegsApp(App):
	def build(self):
		return kv

if __name__ == "__main__":
	MegsApp().run()