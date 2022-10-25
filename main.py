from distutils.log import debug
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
import json
from datetime import datetime

Builder.load_file('design.kv')

# create classe that have same name as rules in kivy

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        print(users)
        users[uname] = {'username': uname, 'password': pword,
        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

# overwrite prev file & create new file & from empty file write new users dictionary
        with open("users.json", "w") as file:
            json.dump(users, file)

class SignUpScreenSuccess(Screen):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()