import json
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious
from kivy.uix.image import Image
from kivy.uix.actionbar import ActionButton
from kivy.core.window import Window
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup


# Utility functions to handle JSON data
def load_data():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open('users.json', 'w') as f:
        json.dump(data, f)
Window.size = (400, 640)


# Difficulty Selection Screen
class DifficultyScreen(Screen):
    def __init__(self, **kwargs):
        super(DifficultyScreen, self).__init__(**kwargs)

        self.is_logged_in = False  # Track if the user is logged in

        # Tracking level progress
        self.level1_unlocked = True
        self.level2_unlocked = True
        self.level3_unlocked = True

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Menu bar
        action_bar = ActionBar(size_hint=(1, 0.1))
        action_view = ActionView()
        action_view.add_widget(ActionPrevious(title="creativitycode", with_previous=False))
        action_view.add_widget(ActionButton(text="Login", on_press=self.go_to_login))
        action_view.add_widget(ActionButton(text="Sign Up", on_press=self.go_to_signup))
        action_view.add_widget(ActionButton(text="About Us", on_press=self.go_to_about_us))
        action_view.add_widget(ActionButton(text="Help", on_press=self.go_to_help))
        action_bar.add_widget(action_view)
        layout.add_widget(action_bar)

        # Title and image
        title = Label(text="creativitycode", font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(title)

        # Image
        image = Image(source='D:\\programming project\\python\\kivy\\kivyproject\\lo.png', size_hint=(1, 0.2))
        layout.add_widget(image)

        # Additional text
        description = Label(text="Creativity Code: The Ideal Solution in Mathematics", font_size='17sp', size_hint=(1, 0.1))
        layout.add_widget(description)

        # Difficulty buttons
        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height='60dp')

        # Level 1 button
        easy_button = Button(text="LEVEL1", font_size='20sp', size_hint=(0.45, None))
        easy_button.bind(on_press=self.go_to_level1)
        button_layout.add_widget(easy_button)

        # Level 2 button
        medium_button = Button(text="LEVEL2", font_size='20sp', size_hint=(0.45, None))
        medium_button.bind(on_press=self.go_to_level2)
        button_layout.add_widget(medium_button)

        # Level 3 button
        hard_button = Button(text="LEVEL3", font_size='20sp', size_hint=(0.45, None))
        hard_button.bind(on_press=self.go_to_level3)
        button_layout.add_widget(hard_button)

        layout.add_widget(button_layout)

        # Back Button
        self.add_back_button(layout)

        self.add_widget(layout)

    def go_to_level1(self, instance):
        if not self.is_logged_in:
            self.manager.current = 'login'
        else:
            self.manager.current = 'level1'

    def go_to_level2(self, instance):
        if not self.is_logged_in:
            self.manager.current = 'login'
        elif self.level2_unlocked:
            self.manager.current = 'level2'
        else:
            self.show_locked_message()

    def go_to_level3(self, instance):
        if not self.is_logged_in:
            self.manager.current = 'login'
        elif self.level3_unlocked:
            self.manager.current = 'level3'
        else:
            self.show_locked_message()

    def show_locked_message(self):
        # Display a message indicating that the level is locked
        popup = Popup(title='Level Locked',
                      content=Label(text='This level is locked. Complete the previous levels first.'),
                      size_hint=(1, 0.3))
        popup.open()

    def go_to_login(self, instance):
        self.manager.current = 'login'

    def go_to_signup(self, instance):
        self.manager.current = 'signup'

    def go_to_about_us(self, instance):
        self.manager.current = 'about_us'

    def go_to_help(self, instance):
        self.manager.current = 'help'

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.1))
        def go_back(instance):
            self.manager.current = 'difficulty'
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)

    # Method to update level status after completing a level
    def unlock_next_level(self, completed_level):
        if completed_level == 1:
            self.level2_unlocked = True
        elif completed_level == 2:
            self.level3_unlocked = True



# Sign-Up Screen
class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super(SignUpScreen, self).__init__(**kwargs)
        
        # إنشاء التخطيط الأساسي
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # العنوان في الأعلى
        title = Label(text="sign up", font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(title)

        # الصورة أسفل العنوان
        image = Image(source='D:\\programming project\\python\\kivy\\kivyproject\\lo.png', size_hint=(1, 0.2))
        layout.add_widget(image)

        # حقول الإدخال الأربعة
        input_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height='200dp')
        input_grid.add_widget(TextInput(hint_text='username', size_hint=(0.45, None), height='40dp'))
        input_grid.add_widget(TextInput(hint_text='email', size_hint=(0.45, None), height='40dp'))
        input_grid.add_widget(TextInput(hint_text='phone', size_hint=(0.45, None), height='40dp'))
        input_grid.add_widget(TextInput(hint_text='password', password=True, size_hint=(0.45, None), height='40dp'))
        layout.add_widget(input_grid)

        # قائمة اختيار العمر
        
        # أزرار التسجيل والعودة
        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height='50dp')
        signup_button = Button(text="sign up", size_hint=(0.45, 0.005),pos_hint={'x': 0.05, 'y': 2})
        signup_button.bind(on_press=self.sign_up)
        buttons_layout.add_widget(signup_button)
        
        back_button = Button(text="back", size_hint=(0.45, 0.05),pos_hint={'x': 0.05, 'y': 2})
        back_button.bind(on_press=self.go_back)
        buttons_layout.add_widget(back_button)

        layout.add_widget(buttons_layout)
        self.age_spinner = Spinner(text='age', values=[str(i) for i in range(3, 13)], size_hint=(0.90, 0.05),pos_hint={'x': 0.05, 'y': 3})
        layout.add_widget(self.age_spinner)

        self.add_widget(layout)

    def sign_up(self, instance):
        # منطق التسجيل هنا
        pass

    def go_back(self, instance):
        # العودة إلى الشاشة السابقة
        self.manager.current = 'difficulty'

    def sign_up(self, instance):
        name = self.name_input.text
        email = self.email_input.text
        phone = self.phone_input.text
        password = self.password_input.text
        age = self.age_spinner.text

        if not all([name, email, phone, password, age]):
            print("All fields must be filled!")
            return

        data = load_data()
        if email in data:
            print("User already exists!")
            return

        if len(password) < 6:
            print("Password must be at least 6 characters long!")
            return

        data[email] = {
            'name': name,
            'phone': phone,
            'password': password,
            'age': age
        }
        save_data(data)
        print("Account created successfully!")
        self.manager.current = 'login'

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.1))
    
    # استخدام دالة لتغيير الشاشة عند الضغط على زر "Back"
        def go_back(instance):
            self.manager.current = 'difficulty'
    
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)



# Login Screen
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()  # استخدام FloatLayout لتحقيق تحكم دقيق في المواضع

        # Title
        title = Label(text="Login", font_size='24sp', size_hint=(0.9, 0.1), pos_hint={'x': 0.05, 'y': 0.85})
        layout.add_widget(title)

        # Image
        image = Image(source='D:\\programming project\\python\\kivy\\kivyproject\\lo.png', size_hint=(0.9, 0.2), pos_hint={'x': 0.05, 'y': 0.65})
        layout.add_widget(image)

        # Input fields
        self.email_input = TextInput(hint_text='Email', size_hint=(0.9, 0.1), pos_hint={'x': 0.05, 'y': 0.55})
        layout.add_widget(self.email_input)
        
        self.password_input = TextInput(hint_text='Password', password=True, size_hint=(0.9, 0.1), pos_hint={'x': 0.05, 'y': 0.45})
        layout.add_widget(self.password_input)

        # Buttons
        login_button = Button(text="Login", size_hint=(0.45, 0.1), pos_hint={'x': 0.05, 'y': 0.3})
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)

        signup_button = Button(text="Go to Sign Up", size_hint=(0.45, 0.1), pos_hint={'x': 0.5, 'y': 0.3})
        signup_button.bind(on_press=self.go_to_signup)
        layout.add_widget(signup_button)

        # Back Button
        self.add_back_button(layout)

        self.add_widget(layout)

    def login(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        data = load_data()
        if email in data and data[email]['password'] == password:
            print("Logged in successfully!")
            self.manager.get_screen('difficulty').is_logged_in = True
            self.manager.current = 'difficulty'
        else:
            print("Invalid email or password!")

    def go_to_signup(self, instance):
        self.manager.current = 'signup'

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(0.9, 0.1), pos_hint={'x': 0.05, 'y': 0})
    
    # استخدام دالة لتغيير الشاشة عند الضغط على زر "Back"
        def go_back(instance):
            self.manager.current = 'difficulty'
    
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)


    def go_to_signup(self, instance):
        self.manager.current = 'signup'

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(0.9, 0.1), pos_hint={'x': 0.05, 'y': 0})
    
    # استخدام دالة لتغيير الشاشة عند الضغط على زر "Back"
        def go_back(instance):
            self.manager.current = 'difficulty'
    
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)



# About Us Screen


class AboutUsScreen(Screen):
    def __init__(self, **kwargs):
        super(AboutUsScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title = Label(text="About Us", font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(title)

        # Image
        about_image = Image(source='D:\\programming project\\python cource\\11.png', size_hint=(1, 0.5))
        layout.add_widget(about_image)

        # Social Media Buttons
        button_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height='120dp')

        facebook_button = Button(text="Facebook", size_hint=(0.45, 0.5))
        facebook_button.bind(on_press=lambda x: webbrowser.open('https://www.facebook.com/profile.php?id=61558357762152&mibextid=ZbWKwL'))
        button_layout.add_widget(facebook_button)

        instagram_button = Button(text="Instagram", size_hint=(0.45, 0.5))
        instagram_button.bind(on_press=lambda x: webbrowser.open('https://www.instagram.com/creativitycode7878?igsh=MTVmdmRwYTVmdzY5Yw=='))
        button_layout.add_widget(instagram_button)

        youtube_button = Button(text="YouTube", size_hint=(0.45, 0.5))
        youtube_button.bind(on_press=lambda x: webbrowser.open('https://www.youtube.com/channel/UCe8NoiDsqqMPMKOhhRKg1yA'))
        button_layout.add_widget(youtube_button)

        linkedin_button = Button(text="LinkedIn", size_hint=(0.45, 0.5))
        linkedin_button.bind(on_press=lambda x: webbrowser.open('http://www.linkedin.com/in/creativity-code-862604305'))
        button_layout.add_widget(linkedin_button)

        layout.add_widget(button_layout)

        # Back Button
        self.add_back_button(layout)

        self.add_widget(layout)

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.1))
        def go_back(instance):
            self.manager.current = 'difficulty'
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)


        # Back Button
        self.add_back_button(layout)

        self.add_widget(layout)

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.1))
        def go_back(instance):
            self.manager.current = 'difficulty'
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)



# Help Screen

class HelpScreen(Screen):
    def __init__(self, **kwargs):
        super(HelpScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title = Label(text="Help", font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(title)

        # Image
        help_image = Image(source='D:\\programming project\\python cource\\111.png', size_hint=(1, 0.5))
        layout.add_widget(help_image)

        # Social Media Buttons
        button_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height='120dp')

        facebook_button = Button(text="Facebook", size_hint=(0.45, 0.5))
        facebook_button.bind(on_press=lambda x: webbrowser.open('https://www.facebook.com/profile.php?id=61558357762152&mibextid=ZbWKwL'))
        button_layout.add_widget(facebook_button)

        whatsapp_button = Button(text="WhatsApp", size_hint=(0.45, 0.5))
        whatsapp_button.bind(on_press=lambda x: webbrowser.open('https://wa.me/201029102507'))  # Example link, adjust as needed
        button_layout.add_widget(whatsapp_button)

        instagram_button = Button(text="Instagram", size_hint=(0.45, 0.5))
        instagram_button.bind(on_press=lambda x: webbrowser.open('https://www.instagram.com/creativitycode7878?igsh=MTVmdmRwYTVmdzY5Yw=='))
        button_layout.add_widget(instagram_button)

        telegram_button = Button(text="Telegram", size_hint=(0.45, 0.5))
        telegram_button.bind(on_press=lambda x: webbrowser.open('https://t.me/+201029102507'))  # Example link, adjust as needed
        button_layout.add_widget(telegram_button)

        layout.add_widget(button_layout)

        # Back Button
        self.add_back_button(layout)

        self.add_widget(layout)

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.1))
        def go_back(instance):
            self.manager.current = 'difficulty'
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)

class FirstLevelScreen(Screen):
    def __init__(self, **kwargs):
        super(FirstLevelScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title = Label(text="First Level", font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(title)

        # Sections buttons
        section_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height='120dp')

        addition_button = Button(text="Addition", size_hint=(0.45, 0.5))
        addition_button.bind(on_press=self.go_to_addition)
        section_layout.add_widget(addition_button)

        Subtraction_button = Button(text="Subtraction", size_hint=(0.45, 0.5))
        # Bind the button to a method for subtraction
        Subtraction_button.bind(on_press=self.go_to_Subtraction)

        section_layout.add_widget(Subtraction_button)

        multiplication_button = Button(text="Multiplication", size_hint=(0.45, 0.5))
        # Bind the button to a method for multiplication
        multiplication_button.bind(on_press=self.go_to_Multiplication)
        section_layout.add_widget(multiplication_button)

        division_button = Button(text="Division", size_hint=(0.45, 0.5))
        # Bind the button to a method for division
        division_button.bind(on_press=self.go_to_Division)
        section_layout.add_widget(division_button)

        layout.add_widget(section_layout)

        # Back Button
        self.add_back_button(layout)

        self.add_widget(layout)

    def go_to_addition(self, instance):
        self.manager.current = 'addition'
    def go_to_Subtraction(self, instance):
        self.manager.current = 'Subtraction'
    def go_to_Multiplication(self, instance):
        self.manager.current ='Multiplication'

    def go_to_Division(self, instance):
        self.manager.current= 'Division'
    

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.01))
        def go_back(instance):
            self.manager.current = 'difficulty'
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)
class Level2Screen(Screen):
    def __init__(self, **kwargs):
        super(Level2Screen, self).__init__(**kwargs)
        
        layout1 = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title1 = Label(text="Level2", font_size='24sp', size_hint=(1, 0.1))
        layout1.add_widget(title1)

        # Sections buttons
        section_layout1 = GridLayout(cols=2, spacing=10, size_hint_y=None, height='120dp')

        addition_button1 = Button(text="Addition", size_hint=(0.45, 0.5))
        addition_button1.bind(on_press=self.go_to_addition_2)
        section_layout1.add_widget(addition_button1)

        Subtraction_button1 = Button(text="Subtraction", size_hint=(0.45, 0.5))
        # Bind the button to a method for subtraction
        Subtraction_button1.bind(on_press=self.go_to_Subtraction_2)

        section_layout1.add_widget(Subtraction_button1)

        multiplication_button1 = Button(text="Multiplication", size_hint=(0.45, 0.5))
        # Bind the button to a method for multiplication
        multiplication_button1.bind(on_press=self.go_to_Multiplication_2)
        section_layout1.add_widget(multiplication_button1)

        division_button1 = Button(text="Division", size_hint=(0.45, 0.5))
        # Bind the button to a method for division
        division_button1.bind(on_press=self.go_to_Division_2)
        section_layout1.add_widget(division_button1)

        layout1.add_widget(section_layout1)

        # Back Button
        self.add_back_button(layout1)

        self.add_widget(layout1)

    def go_to_addition_2(self, instance):
        self.manager.current = 'Addition2'
    def go_to_Subtraction_2(self, instance):
        self.manager.current = 'Subtraction2'
    def go_to_Multiplication_2(self, instance):
        self.manager.current='multiplication2'

    def go_to_Division_2(self, instance):
        self.manager.current= 'division2'
    

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.01))
        def go_back(instance):
            self.manager.current = 'difficulty'
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)
# Addition Section Screen

from kivy.graphics import Color, Rectangle
import os

class BackgroundLabel(Label):
    def __init__(self, **kwargs):
        super(BackgroundLabel, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0.1, 0.6, 0.8, 1)  # اللون الذي تريده
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class AdditionScreen(Screen):
    def __init__(self, **kwargs):
        super(AdditionScreen, self).__init__(**kwargs)

        # تحميل الحالة الحالية أو البدء من جديد
        self.load_user_data()

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        with layout.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # لون الخلفية الرمادي الفاتح
            self.rect = Rectangle(size=self.size, pos=self.pos)

            layout.bind(size=self._update_rect, pos=self._update_rect)
        # Title
        title = BackgroundLabel(text="Addition Section", font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(title)
        with title.canvas.before:
            Color(0.2, 0.4, 0.6, 1)  # لون خلفية العنوان
            self.rect_title = Rectangle(size=title.size, pos=title.pos)
            title.bind(size=self._update_rect_title, pos=self._update_rect_title)

        # Examples
        examples_text = BackgroundLabel(text="Examples:\n1 + 1 = 2\n2 + 2 = 4\n3 + 3 = 6\n4 + 4 = 8\n5 + 5 = 10",
                              size_hint=(1, 0.4), color=(1, 1, 1, 1))
        layout.add_widget(examples_text)

        # Question Layout
        self.question_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.question_label = BackgroundLabel(text=self.get_current_question_text(), size_hint=(0.7, None), height='30dp', color=(1, 1, 1, 1))
        self.answer_input = TextInput(hint_text='Enter your answer', size_hint=(0.3, None), height='30dp')
        self.question_layout.add_widget(self.question_label)
        self.question_layout.add_widget(self.answer_input)
        layout.add_widget(self.question_layout)

        # Coins and Hearts Display
        status_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.coins_label = Label(text=f"Coins: {self.coins}", size_hint=(0.5, 1),color=(0, 0.5, 0, 1))
        self.hearts_label = Label(text=f"Hearts: {self.hearts}", size_hint=(0.5, 1),color=(1, 0, 0, 1))
        status_layout.add_widget(self.coins_label)
        status_layout.add_widget(self.hearts_label)
        layout.add_widget(status_layout)

        # Submit Button
        submit_button = Button(text="Submit Answer", size_hint=(1, 0.1))
        submit_button.bind(on_press=self.check_answer)
        layout.add_widget(submit_button)

        # Back Button
        self.add_back_button(layout)

        self.add_widget(layout)

    def get_current_question_text(self):
        questions = ["1 + 1", "2 + 2", "3 + 3", "4 + 4", "5 + 5", "6 + 6", "7 + 7", "8 + 8", "9 + 9", "10 + 10", 
                 "11 + 11", "12 + 12", "13 + 13", "14 + 14", "15 + 15"]
    
        if self.current_question < 0 or self.current_question >= len(questions):
        # Handle the out-of-range index case
            return "Invalid question index"
    
        return f"Question {self.current_question + 1}: {questions[self.current_question]} = ?"


    def check_answer(self, instance):
        correct_answers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
        try:
            answer = int(self.answer_input.text)
            if answer == correct_answers[self.current_question]:
                self.coins += 10
                self.current_question += 1
                if self.current_question < len(correct_answers):
                    self.question_label.text = self.get_current_question_text()
                    self.answer_input.text = ''
                else:
                    print("Congratulations! You've completed all the questions.")
            else:
                self.hearts -= 1
        except ValueError:
            self.hearts -= 1

        self.update_status()
        self.save_user_data()

        if self.hearts <= 0:
            print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")
            # منطق لتعطيل الإجابات أو طلب دفع كوينزات لشراء القلوب

    def update_status(self):
        self.coins_label.text = f"Coins: {self.coins}"
        self.hearts_label.text = f"Hearts: {self.hearts}"

    def load_user_data(self):
        if os.path.exists('user_data.json'):
            with open('user_data.json', 'r') as f:
                data = json.load(f)
                self.coins = data.get('coins', 0)
                self.hearts = data.get('hearts', 10)
                self.current_question = data.get('current_question', 0)
        else:
            self.coins = 0
            self.hearts = 10
            self.current_question = 0

    def save_user_data(self):
        data = {
            'coins': self.coins,
            'hearts': self.hearts,
            'current_question': self.current_question
        }
        with open('user_data.json', 'w') as f:
            json.dump(data, f)

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.1))
        def go_back(instance):
            self.manager.current = 'level1'
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _update_rect_title(self, instance, value):
        self.rect_title.pos = instance.pos
        self.rect_title.size = instance.size

    def _update_rect_examples(self, instance, value):
        self.rect_examples.pos = instance.pos
        self.rect_examples.size = instance.size

    def _update_rect_question(self, instance, value):
        self.rect_question.pos = instance.pos
        self.rect_question.size = instance.size




class SubtractionScreen(Screen):
    def __init__(self, **kwargs):
        super(SubtractionScreen, self).__init__(**kwargs)

        self.save_file = "subtraction_progress.json"
        self.load_progress()

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        with layout.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # لون الخلفية الرمادي الفاتح
            self.rect = Rectangle(size=self.size, pos=self.pos)

            layout.bind(size=self._update_rect, pos=self._update_rect)

        # Title
        title = Label(text="Subtraction Section", font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(title)

        with title.canvas.before:
            Color(0.2, 0.4, 0.6, 1)  # لون خلفية العنوان
            self.rect_title = Rectangle(size=title.size, pos=title.pos)
            title.bind(size=self._update_rect_title, pos=self._update_rect_title)

        # Examples
        examples_text = Label(
            text="Examples:\n5 - 2 = 3\n10 - 4 = 6\n7 - 1 = 6\n9 - 3 = 6\n8 - 5 = 3",
            size_hint=(1, 0.3),
            color=(1, 1, 1, 1)  # لون النص أبيض
        )
        layout.add_widget(examples_text)

        with examples_text.canvas.before:
            Color(0.3, 0.6, 0.8, 1)  # لون خلفية الأمثلة
            self.rect_examples = Rectangle(size=examples_text.size, pos=examples_text.pos)
            examples_text.bind(size=self._update_rect_examples, pos=self._update_rect_examples)

        # Questions
        self.questions = [
            ("6 - 3 =", 3),
            ("10 - 5 =", 5),
            ("15 - 7 =", 8),
            ("20 - 10 =", 10),
            ("8 - 4 =", 4),
            ("7 - 2 =", 5),
            ("9 - 6 =", 3),
            ("12 - 5 =", 7),
            ("14 - 9 =", 5),
            ("17 - 8 =", 9),
            ("11 - 3 =", 8),
            ("16 - 7 =", 9),
            ("18 - 11 =", 7),
            ("20 - 14 =", 6),
            ("13 - 5 =", 8)
        ]

    def get_current_question_text(self):
        questions = ["1 + 1", "2 + 2", "3 + 3", "4 + 4", "5 + 5", "6 + 6", "7 + 7", "8 + 8", "9 + 9", "10 + 10", 
                 "11 + 11", "12 + 12", "13 + 13", "14 + 14", "15 + 15"]
    
        if self.current_question_index < 0 or self.current_question_index >= len(questions):
        # Handle the out-of-range index case
            return "Invalid question index"
    
        return f"Question {self.current_question_index + 1}: {questions[self.current_question_index]} = ?"

        layout.add_widget(self.question_label)

        with self.question_label.canvas.before:
            Color(0.8, 0.9, 1, 1)  # لون خلفية السؤال
            self.rect_question = Rectangle(size=self.question_label.size, pos=self.question_label.pos)
            self.question_label.bind(size=self._update_rect_question, pos=self._update_rect_question)

        self.answer_input = TextInput(hint_text='Enter your answer', size_hint=(1, 0.1))
        layout.add_widget(self.answer_input)

        # Coins and Hearts Display
        status_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.coins_label = Label(
            text=f"Coins: {self.coins}",
            size_hint=(0.5, 1),
            color=(0, 0.5, 0, 1)  # لون النص أخضر داكن
        )
        self.hearts_label = Label(
            text=f"Hearts: {self.hearts}",
            size_hint=(0.5, 1),
            color=(1, 0, 0, 1)  # لون النص أحمر
        )
        status_layout.add_widget(self.coins_label)
        status_layout.add_widget(self.hearts_label)
        layout.add_widget(status_layout)

        # Submit Button
        submit_button = Button(text="Submit Answer", size_hint=(1, 0.1))
        submit_button.bind(on_press=self.check_answer)
        layout.add_widget(submit_button)

        # Back Button
        self.add_back_button(layout)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _update_rect_title(self, instance, value):
        self.rect_title.pos = instance.pos
        self.rect_title.size = instance.size

    def _update_rect_examples(self, instance, value):
        self.rect_examples.pos = instance.pos
        self.rect_examples.size = instance.size

    def _update_rect_question(self, instance, value):
        self.rect_question.pos = instance.pos
        self.rect_question.size = instance.size

    def load_progress(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, "r") as f:
                data = json.load(f)
                self.coins = data.get("coins", 0)
                self.hearts = data.get("hearts", 10)
                self.current_question_index = data.get("current_question_index", 0)
        else:
            self.coins = 0
            self.hearts = 10
            self.current_question_index = 0

    def save_progress(self):
        data = {
            "coins": self.coins,
            "hearts": self.hearts,
            "current_question_index": self.current_question_index
        }
        with open(self.save_file, "w") as f:
            json.dump(data, f)

    def check_answer(self, instance):
        correct_answer = self.questions[self.current_question_index][1]
        try:
            user_answer = int(self.answer_input.text)
            if user_answer == correct_answer:
                self.coins += 10
                self.current_question_index += 1
                if self.current_question_index < len(self.questions):
                    self.question_label.text = self.questions[self.current_question_index][0]
                    self.answer_input.text = ''
                else:
                    print("Congratulations! You completed all the questions.")
            else:
                self.hearts -= 1
        except ValueError:
            self.hearts -= 1

        self.save_progress()
        self.update_status()

        if self.hearts <= 0:
            print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")

    def update_status(self):
        self.coins_label.text = f"Coins: {self.coins}"
        self.hearts_label.text = f"Hearts: {self.hearts}"

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.1))
        def go_back(instance):
            self.save_progress()
            self.manager.current = 'level1'
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)



class MultiplicationScreen(Screen):
    def __init__(self, **kwargs):
        super(MultiplicationScreen, self).__init__(**kwargs)

        self.save_file = "multiplication_progress.json"
        self.load_progress()

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        with layout.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # Light gray background color
            self.rect = Rectangle(size=self.size, pos=self.pos)
            layout.bind(size=self._update_rect, pos=self._update_rect)

        # Title
        title = Label(text="Multiplication Section", font_size='24sp', size_hint=(1, 0.1), color=(1, 1, 1, 1))  # White text color
        layout.add_widget(title)

        with title.canvas.before:
            Color(0.2, 0.4, 0.6, 1)  # Title background color
            self.rect_title = Rectangle(size=title.size, pos=title.pos)
            title.bind(size=self._update_rect_title, pos=self._update_rect_title)

        # Examples
        examples_text = Label(text="Examples:\n1 x 1 = 1\n2 x 2 = 4\n3 x 3 = 9\n4 x 4 = 16", size_hint=(1, 0.3), color=(0, 0, 0, 1))  # Black text color
        layout.add_widget(examples_text)

        with examples_text.canvas.before:
            Color(0.8, 0.9, 1, 1)  # Examples background color
            self.rect_examples = Rectangle(size=examples_text.size, pos=examples_text.pos)
            examples_text.bind(size=self._update_rect_examples, pos=self._update_rect_examples)

        # Current Question Layout
        self.current_question_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.current_question_label = Label(text="", size_hint=(0.7, None), height='30dp', color=(0, 0, 0, 1))  # White text color
        self.current_answer_input = TextInput(hint_text='Enter your answer', size_hint=(0.3, None), height='30dp')
        self.current_question_layout.add_widget(self.current_question_label)
        self.current_question_layout.add_widget(self.current_answer_input)
        layout.add_widget(self.current_question_layout)

        # Coins and Hearts Display
        status_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.coins_label = Label(text=f"Coins: {self.coins}", size_hint=(0.5, 1), color=(0, 0.5, 0, 1))  # White text color
        self.hearts_label = Label(text=f"Hearts: {self.hearts}", size_hint=(0.5, 1), color=(1, 0, 0, 1))  # White text color
        status_layout.add_widget(self.coins_label)
        status_layout.add_widget(self.hearts_label)
        layout.add_widget(status_layout)

        # Submit Button
        submit_button = Button(text="Submit Answer", size_hint=(1, 0.1))
        submit_button.bind(on_press=self.check_answer)
        layout.add_widget(submit_button)

        # Back Button
        self.add_back_button(layout)

        self.add_widget(layout)

        # Display the current question
        self.show_current_question()

    def show_current_question(self):
        if self.current_question_index < len(self.correct_answers):
            num1 = (self.current_question_index % 4) + 1
            num2 = ((self.current_question_index // 4) % 4) + 1
            self.current_question_label.text = f"Question {self.current_question_index + 1}: {num1} x {num2} ="
        else:
            self.current_question_label.text = "All questions completed!"

    def check_answer(self, instance):
        try:
            answer = int(self.current_answer_input.text)
            correct_answer = self.correct_answers[self.current_question_index]
            if answer == correct_answer:
                self.coins += 10
                self.update_status()  # إضافة هذا السطر
                self.current_question_index += 1
                self.save_progress()
                self.show_current_question()
            else:
                self.hearts -= 1
                self.update_status()  # إضافة هذا السطر
                if self.hearts <= 0:
                    print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")
                    # Logic to disable further answers or require coins
        except ValueError:
            self.hearts -= 1
            self.update_status()  # إضافة هذا السطر

        self.current_answer_input.text = ""


    def update_status(self):
        self.coins_label.text = f"Coins: {self.coins}"
        self.hearts_label.text = f"Hearts: {self.hearts}"

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.1))
        def go_back(instance):
            self.manager.current = 'level1'
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)

    def load_progress(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as file:
                data = json.load(file)
                self.coins = data.get('coins', 0)
                self.hearts = data.get('hearts', 10)
                self.current_question_index = data.get('current_question', 0)
                self.correct_answers = data.get('correct_answers', self.generate_correct_answers())
        else:
            self.coins = 0
            self.hearts = 10
            self.current_question_index = 0
            self.correct_answers = self.generate_correct_answers()

    def save_progress(self):
        data = {
            'coins': self.coins,
            'hearts': self.hearts,
            'current_question': self.current_question_index,
            'correct_answers': self.correct_answers
        }
        with open(self.save_file, 'w') as file:
            json.dump(data, file)

    def generate_correct_answers(self):
        correct_answers = []
        for i in range(15):
            num1 = (i % 4) + 1
            num2 = ((i // 4) % 4) + 1
            correct_answers.append(num1 * num2)
        return correct_answers

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _update_rect_title(self, instance, value):
        self.rect_title.pos = instance.pos
        self.rect_title.size = instance.size

    def _update_rect_examples(self, instance, value):
        self.rect_examples.pos = instance.pos
        self.rect_examples.size = instance.size
class DivisionScreen(Screen):
    def __init__(self, **kwargs):
        super(DivisionScreen, self).__init__(**kwargs)

        self.save_file = "division_progress.json"
        self.load_progress()

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        with layout.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # لون الخلفية الرمادي الفاتح
            self.rect = Rectangle(size=self.size, pos=self.pos)
            layout.bind(size=self._update_rect, pos=self._update_rect)

        # العنوان
        title = Label(text="Division Section", font_size='24sp', size_hint=(1, 0.1), color=(1, 1, 1, 1))  # لون النص الأبيض
        layout.add_widget(title)

        with title.canvas.before:
            Color(0.2, 0.4, 0.6, 1)  # لون خلفية العنوان
            self.rect_title = Rectangle(size=title.size, pos=title.pos)
            title.bind(size=self._update_rect_title, pos=self._update_rect_title)

        # الأمثلة
        examples_text = Label(text="Examples:\n4 ÷ 2 = 2\n6 ÷ 2 = 3\n9 ÷ 3 = 3\n12 ÷ 4 = 3", size_hint=(1, 0.3), color=(0, 0, 0, 1))  # لون النص الأسود
        layout.add_widget(examples_text)

        with examples_text.canvas.before:
            Color(0.8, 0.9, 1, 1)  # لون خلفية الأمثلة
            self.rect_examples = Rectangle(size=examples_text.size, pos=examples_text.pos)
            examples_text.bind(size=self._update_rect_examples, pos=self._update_rect_examples)

        # تخطيط السؤال الحالي
        self.current_question_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.current_question_label = Label(text="", size_hint=(0.7, None), height='30dp', color=(0, 0, 0, 1))  # لون النص الأسود
        self.current_answer_input = TextInput(hint_text='Enter your answer', size_hint=(0.3, None), height='30dp')
        self.current_question_layout.add_widget(self.current_question_label)
        self.current_question_layout.add_widget(self.current_answer_input)
        layout.add_widget(self.current_question_layout)

        # عرض الكوينز والقلوب
        status_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.coins_label = Label(text=f"Coins: {self.coins}", size_hint=(0.5, 1), color=(0, 0.5, 0, 1))  # لون النص الأخضر
        self.hearts_label = Label(text=f"Hearts: {self.hearts}", size_hint=(0.5, 1), color=(1, 0, 0, 1))  # لون النص الأحمر
        status_layout.add_widget(self.coins_label)
        status_layout.add_widget(self.hearts_label)
        layout.add_widget(status_layout)

        # زر الإرسال
        submit_button = Button(text="Submit Answer", size_hint=(1, 0.1))
        submit_button.bind(on_press=self.check_answer)
        layout.add_widget(submit_button)

        # زر العودة
        self.add_back_button(layout)

        self.add_widget(layout)

        # عرض السؤال الحالي
        self.show_current_question()

    def show_current_question(self):
        if self.current_question_index < len(self.correct_answers):
            num1 = (self.current_question_index % 4 + 1) * 2
            num2 = 2 if num1 == 4 else 3 if num1 == 9 else num1 // 2
            self.current_question_label.text = f"Question {self.current_question_index + 1}: {num1} ÷ {num2} ="
        else:
            self.current_question_label.text = "All questions completed!"

    def check_answer(self, instance):
        try:
            answer = int(self.current_answer_input.text)
            correct_answer = self.correct_answers[self.current_question_index]
            if answer == correct_answer:
                self.coins += 10
                self.update_status()  # تحديث العرض
                self.current_question_index += 1
                self.save_progress()
                self.show_current_question()
            else:
                self.hearts -= 1
                self.update_status()  # تحديث العرض
                if self.hearts <= 0:
                    print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")
        except ValueError:
            self.hearts -= 1
            self.update_status()  # تحديث العرض

        self.current_answer_input.text = ""

    def update_status(self):
        self.coins_label.text = f"Coins: {self.coins}"
        self.hearts_label.text = f"Hearts: {self.hearts}"

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.1))
        def go_back(instance):
            self.manager.current = 'level1'
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)

    def load_progress(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as file:
                data = json.load(file)
                self.coins = data.get('coins', 0)
                self.hearts = data.get('hearts', 10)
                self.current_question_index = data.get('current_question', 0)
                self.correct_answers = data.get('correct_answers', self.generate_correct_answers())
        else:
            self.coins = 0
            self.hearts = 10
            self.current_question_index = 0
            self.correct_answers = self.generate_correct_answers()

    def save_progress(self):
        data = {
            'coins': self.coins,
            'hearts': self.hearts,
            'current_question': self.current_question_index,
            'correct_answers': self.correct_answers
        }
        with open(self.save_file, 'w') as file:
            json.dump(data, file)

    def generate_correct_answers(self):
        correct_answers = []
        for i in range(15):
            num1 = (i % 4 + 1) * 2
            num2 = 2 if num1 == 4 else 3 if num1 == 9 else num1 // 2
            correct_answers.append(num1 // num2)
        return correct_answers

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _update_rect_title(self, instance, value):
        self.rect_title.pos = instance.pos
        self.rect_title.size = instance.size

    def _update_rect_examples(self, instance, value):
        self.rect_examples.pos = instance.pos
        self.rect_examples.size = instance.size

class AdditionScreen2(Screen):
    def __init__(self, **kwargs):
        super(AdditionScreen2, self).__init__(**kwargs)

        # تحميل الحالة الحالية أو البدء من جديد
        self.load_user_data2()

        layout2 = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Title
        title2 = BackgroundLabel(text="Addition Section", font_size='24sp', size_hint=(1, 0.1))
        layout2.add_widget(title2)

        # Examples
        examples_text2 = BackgroundLabel(text="Examples:\n12 + 15 = 27\n23 + 34 = 57\n45 + 19 = 64\n78 + 26 = 104\n99 + 88 = 187",
                              size_hint=(1, 0.4), color=(1, 1, 1, 1))
        layout2.add_widget(examples_text2)

        # Question Layout
        self.question_layout2 = BoxLayout(orientation='horizontal', spacing=10)
        self.question_label2 = BackgroundLabel(text=self.get_current_question_text2(), size_hint=(0.7, None), height='30dp', color=(1, 1, 1, 1))
        self.answer_input2 = TextInput(hint_text='Enter your answer', size_hint=(0.3, None), height='30dp')
        self.question_layout2.add_widget(self.question_label2)
        self.question_layout2.add_widget(self.answer_input2)
        layout2.add_widget(self.question_layout2)

        # Coins and Hearts Display
        status_layout2 = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.coins_label2 = Label(text=f"Coins: {self.coins2}", size_hint=(0.5, 1))
        self.hearts_label2 = Label(text=f"Hearts: {self.hearts2}", size_hint=(0.5, 1))
        status_layout2.add_widget(self.coins_label2)
        status_layout2.add_widget(self.hearts_label2)
        layout2.add_widget(status_layout2)

        # Submit Button
        submit_button2 = Button(text="Submit Answer", size_hint=(1, 0.1))
        submit_button2.bind(on_press=self.check_answer2)
        layout2.add_widget(submit_button2)

        # Back Button
        self.add_back_button2(layout2)

        self.add_widget(layout2)

    def get_current_question_text2(self):
        questions2 = ["12 + 15", "23 + 34", "45 + 19", "78 + 26", "99 + 88", 
                    "67 + 45", "54 + 32", "89 + 56", "73 + 27", "100 + 50", 
                    "81 + 29", "62 + 38", "90 + 45", "76 + 24", "88 + 33"]
        
        if self.current_question2 < 0 or self.current_question2 >= len(questions2):
            return "Invalid question index"
        
        return f"Question {self.current_question2 + 1}: {questions2[self.current_question2]} = ?"


    def check_answer2(self, instance):
        correct_answers2 = [27, 57, 64, 104, 187, 112, 86, 145, 100, 150, 110, 100, 135, 100, 121]
        try:
            answer2 = int(self.answer_input2.text)
            if answer2 == correct_answers2[self.current_question2]:
                self.coins2 += 10
                self.current_question2 += 1
                if self.current_question2 < len(correct_answers2):
                    self.question_label2.text = self.get_current_question_text2()
                    self.answer_input2.text = ''
                else:
                    print("Congratulations! You've completed all the questions.")
            else:
                self.hearts2 -= 1
        except ValueError:
            self.hearts2 -= 1

        self.update_status2()
        self.save_user_data2()

        if self.hearts2 <= 0:
            print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")
            # منطق لتعطيل الإجابات أو طلب دفع كوينزات لشراء القلوب

    def update_status2(self):
        self.coins_label2.text = f"Coins: {self.coins2}"
        self.hearts_label2.text = f"Hearts: {self.hearts2}"

    def load_user_data2(self):
        if os.path.exists('user_data2.json'):
            with open('user_data2.json', 'r') as f:
                data2 = json.load(f)
                self.coins2 = data2.get('coins2', 0)
                self.hearts2 = data2.get('hearts2', 10)
                self.current_question2 = data2.get('current_question2', 0)
        else:
            self.coins2 = 0
            self.hearts2 = 10
            self.current_question2 = 0

    def save_user_data2(self):
        data2 = {
            'coins2': self.coins2,
            'hearts2': self.hearts2,
            'current_question2': self.current_question2
        }
        with open('user_data2.json', 'w') as f:
            json.dump(data2, f)

    def add_back_button2(self, layout2):
        back_button2 = Button(text="Back", size_hint=(1, 0.1))
        def go_back2(instance):
            self.manager.current = 'level2'
        back_button2.bind(on_press=go_back2)
        layout2.add_widget(back_button2)
class SubtractionScreen2(Screen):
    def __init__(self, **kwargs):
        super(SubtractionScreen2, self).__init__(**kwargs)

        self.save_file2 = "subtraction_progress2.json"
        self.load_progress2()

        layout2 = BoxLayout(orientation='vertical', padding=20, spacing=10)

        with layout2.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # لون الخلفية الرمادي الفاتح
            self.rect2 = Rectangle(size=self.size, pos=self.pos)

            layout2.bind(size=self._update_rect2, pos=self._update_rect2)

        # Title
        title2 = Label(text="Subtraction Section", font_size='24sp', size_hint=(1, 0.1))
        layout2.add_widget(title2)

        with title2.canvas.before:
            Color(0.2, 0.4, 0.6, 1)  # لون خلفية العنوان
            self.rect_title2 = Rectangle(size=title2.size, pos=title2.pos)
            title2.bind(size=self._update_rect_title2, pos=self._update_rect_title2)

        # Examples
        examples_text2 = Label(
            text="Examples:\n15 - 8 = 7\n25 - 13 = 12\n40 - 18 = 22\n60 - 33 = 27\n90 - 45 = 45",
            size_hint=(1, 0.3),
            color=(1, 1, 1, 1)  # لون النص أبيض
        )
        layout2.add_widget(examples_text2)

        with examples_text2.canvas.before:
            Color(0.3, 0.6, 0.8, 1)  # لون خلفية الأمثلة
            self.rect_examples2 = Rectangle(size=examples_text2.size, pos=examples_text2.pos)
            examples_text2.bind(size=self._update_rect_examples2, pos=self._update_rect_examples2)

        # Questions
        self.questions2 = [
            ("25 - 11 =", 14),
            ("50 - 19 =", 31),
            ("75 - 28 =", 47),
            ("100 - 42 =", 58),
            ("45 - 23 =", 22),
            ("38 - 16 =", 22),
            ("62 - 35 =", 27),
            ("89 - 48 =", 41),
            ("72 - 39 =", 33),
            ("95 - 55 =", 40),
            ("64 - 21 =", 43),
            ("82 - 36 =", 46),
            ("90 - 53 =", 37),
            ("78 - 44 =", 34),
            ("56 - 19 =", 37)
        ]

        self.current_question_index2 = 0  # تأكد من أن القيمة هنا ضمن نطاق الأسئلة
        
        # تحقق من صحة الفهرس قبل الوصول إلى العناصر
        if 0 <= self.current_question_index2 < len(self.questions2):
            question_text = self.questions2[self.current_question_index2]
        else:
            question_text = "Invalid question index"  # نص بديل عند حدوث خطأ
        
        # إنشاء تسميات الأسئلة
        self.question_label2 = Label(
            text=str(question_text),
            size_hint=(1, 0.1),
            color=(0, 0, 0, 1)  # لون النص أسود
        )
        layout2.add_widget(self.question_label2)

        with self.question_label2.canvas.before:
            Color(0.8, 0.9, 1, 1)  # لون خلفية السؤال
            self.rect_question2 = Rectangle(size=self.question_label2.size, pos=self.question_label2.pos)
            self.question_label2.bind(size=self._update_rect_question2, pos=self._update_rect_question2)

        self.answer_input2 = TextInput(hint_text='Enter your answer', size_hint=(1, 0.1))
        layout2.add_widget(self.answer_input2)

        # Coins and Hearts Display
        status_layout2 = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.coins_label2 = Label(
            text=f"Coins: {self.coins2}",
            size_hint=(0.5, 1),
            color=(0, 0.5, 0, 1)  # لون النص أخضر داكن
        )
        self.hearts_label2 = Label(
            text=f"Hearts: {self.hearts2}",
            size_hint=(0.5, 1),
            color=(1, 0, 0, 1)  # لون النص أحمر
        )
        status_layout2.add_widget(self.coins_label2)
        status_layout2.add_widget(self.hearts_label2)
        layout2.add_widget(status_layout2)

        # Submit Button
        submit_button2 = Button(text="Submit Answer", size_hint=(1, 0.1))
        submit_button2.bind(on_press=self.check_answer2)
        layout2.add_widget(submit_button2)

        # Back Button
        self.add_back_button2(layout2)

        self.add_widget(layout2)

    def _update_rect2(self, instance, value):
        self.rect2.pos = instance.pos
        self.rect2.size = instance.size

    def _update_rect_title2(self, instance, value):
        self.rect_title2.pos = instance.pos
        self.rect_title2.size = instance.size

    def _update_rect_examples2(self, instance, value):
        self.rect_examples2.pos = instance.pos
        self.rect_examples2.size = instance.size

    def _update_rect_question2(self, instance, value):
        self.rect_question2.pos = instance.pos
        self.rect_question2.size = instance.size

    def load_progress2(self):
        if os.path.exists(self.save_file2):
            with open(self.save_file2, "r") as f:
                data2 = json.load(f)
                self.coins2 = data2.get("coins2", 0)
                self.hearts2 = data2.get("hearts2", 10)
                self.current_question_index2 = data2.get("current_question_index2", 0)
        else:
            self.coins2 = 0
            self.hearts2 = 10
            self.current_question_index2 = 0

    def save_progress2(self):
        data2 = {
            "coins2": self.coins2,
            "hearts2": self.hearts2,
            "current_question_index2": self.current_question_index2
        }
        with open(self.save_file2, "w") as f:
            json.dump(data2, f)

    def check_answer2(self, instance):
        correct_answer2 = self.questions2[self.current_question_index2][1]
        try:
            user_answer2 = int(self.answer_input2.text)
            if user_answer2 == correct_answer2:
                self.coins2 += 10
                self.current_question_index2 += 1
                if self.current_question_index2 < len(self.questions2):
                    self.question_label2.text = self.questions2[self.current_question_index2][0]
                    self.answer_input2.text = ''
                else:
                    print("Congratulations! You completed all the questions.")
            else:
                self.hearts2 -= 1
        except ValueError:
            self.hearts2 -= 1

        self.save_progress2()
        self.update_status2()

        if self.hearts2 <= 0:
            print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")

    def update_status2(self):
        self.coins_label2.text = f"Coins: {self.coins2}"
        self.hearts_label2.text = f"Hearts: {self.hearts2}"

    def add_back_button2(self, layout2):
        back_button2 = Button(text="Back", size_hint=(1, 0.1))
        def go_back2(instance):
            self.save_progress2()
            self.manager.current = 'level2'
        back_button2.bind(on_press=go_back2)
        layout2.add_widget(back_button2)

class MultiplicationScreen2(Screen):
    def __init__(self, **kwargs):
        super(MultiplicationScreen2, self).__init__(**kwargs)

        self.save_file2 = "multiplication_progress2.json"
        self.load_progress2()

        layout2 = BoxLayout(orientation='vertical', padding=20, spacing=10)

        with layout2.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # Light gray background color
            self.rect2 = Rectangle(size=self.size, pos=self.pos)
            layout2.bind(size=self._update_rect2, pos=self._update_rect2)

        # Title
        title2 = Label(text="Advanced Multiplication Section", font_size='24sp', size_hint=(1, 0.1), color=(1, 1, 1, 1))  # White text color
        layout2.add_widget(title2)

        with title2.canvas.before:
            Color(0.2, 0.4, 0.6, 1)  # Title background color
            self.rect_title2 = Rectangle(size=title2.size, pos=title2.pos)
            title2.bind(size=self._update_rect_title2, pos=self._update_rect_title2)

        # Examples
        examples_text2 = Label(
            text="Examples:\n5 x 5 = 25\n6 x 7 = 42\n8 x 9 = 72\n10 x 12 = 120\n15 x 14 = 210", 
            size_hint=(1, 0.4), 
            color=(0, 0, 0, 1)  # Black text color
        )
        layout2.add_widget(examples_text2)

        with examples_text2.canvas.before:
            Color(0.8, 0.9, 1, 1)  # Examples background color
            self.rect_examples2 = Rectangle(size=examples_text2.size, pos=examples_text2.pos)
            examples_text2.bind(size=self._update_rect_examples2, pos=self._update_rect_examples2)

        # Current Question Layout
        self.current_question_layout2 = BoxLayout(orientation='horizontal', spacing=10)
        self.current_question_label2 = Label(text="", size_hint=(0.7, None), height='30dp', color=(0, 0, 0, 1))  # Black text color
        self.current_answer_input2 = TextInput(hint_text='Enter your answer', size_hint=(0.3, None), height='30dp')
        self.current_question_layout2.add_widget(self.current_question_label2)
        self.current_question_layout2.add_widget(self.current_answer_input2)
        layout2.add_widget(self.current_question_layout2)

        # Coins and Hearts Display
        status_layout2 = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.coins_label2 = Label(text=f"Coins: {self.coins2}", size_hint=(0.5, 1), color=(0, 0.5, 0, 1))  # Dark green text color
        self.hearts_label2 = Label(text=f"Hearts: {self.hearts2}", size_hint=(0.5, 1), color=(1, 0, 0, 1))  # Red text color
        status_layout2.add_widget(self.coins_label2)
        status_layout2.add_widget(self.hearts_label2)
        layout2.add_widget(status_layout2)

        # Submit Button
        submit_button2 = Button(text="Submit Answer", size_hint=(1, 0.1))
        submit_button2.bind(on_press=self.check_answer2)
        layout2.add_widget(submit_button2)

        # Back Button
        self.add_back_button2(layout2)

        self.add_widget(layout2)

        # Display the current question
        self.show_current_question2()

    def show_current_question2(self):
        if self.current_question_index2 < len(self.correct_answers2):
            num1 = (self.current_question_index2 % 5) + 5
            num2 = ((self.current_question_index2 // 5) % 5) + 6
            self.current_question_label2.text = f"Question {self.current_question_index2 + 1}: {num1} x {num2} ="
        else:
            self.current_question_label2.text = "All questions completed!"

    def check_answer2(self, instance):
        try:
            answer2 = int(self.current_answer_input2.text)
            correct_answer2 = self.correct_answers2[self.current_question_index2]
            if answer2 == correct_answer2:
                self.coins2 += 10
                self.update_status2()
                self.current_question_index2 += 1
                self.save_progress2()
                self.show_current_question2()
            else:
                self.hearts2 -= 1
                self.update_status2()
                if self.hearts2 <= 0:
                    print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")
        except ValueError:
            self.hearts2 -= 1
            self.update_status2()

        self.current_answer_input2.text = ""

    def update_status2(self):
        self.coins_label2.text = f"Coins: {self.coins2}"
        self.hearts_label2.text = f"Hearts: {self.hearts2}"

    def add_back_button2(self, layout2):
        back_button2 = Button(text="Back", size_hint=(1, 0.1))
        def go_back2(instance):
            self.manager.current = 'level2'
        back_button2.bind(on_press=go_back2)
        layout2.add_widget(back_button2)

    def load_progress2(self):
        if os.path.exists(self.save_file2):
            with open(self.save_file2, 'r') as file2:
                data2 = json.load(file2)
                self.coins2 = data2.get('coins2', 0)
                self.hearts2 = data2.get('hearts2', 10)
                self.current_question_index2 = data2.get('current_question2', 0)
                self.correct_answers2 = data2.get('correct_answers2', self.generate_correct_answers2())
        else:
            self.coins2 = 0
            self.hearts2 = 10
            self.current_question_index2 = 0
            self.correct_answers2 = self.generate_correct_answers2()

    def save_progress2(self):
        data2 = {
            'coins2': self.coins2,
            'hearts2': self.hearts2,
            'current_question2': self.current_question_index2,
            'correct_answers2': self.correct_answers2
        }
        with open(self.save_file2, 'w') as file2:
            json.dump(data2, file2)

    def generate_correct_answers2(self):
        correct_answers2 = []
        for i in range(15):
            num1 = (i % 5) + 5
            num2 = ((i // 5) % 5) + 6
            correct_answers2.append(num1 * num2)
        return correct_answers2

    def _update_rect2(self, instance, value):
        self.rect2.pos = instance.pos
        self.rect2.size = instance.size

    def _update_rect_title2(self, instance, value):
        self.rect_title2.pos = instance.pos
        self.rect_title2.size = instance.size

    def _update_rect_examples2(self, instance, value):
        self.rect_examples2.pos = instance.pos
        self.rect_examples2.size = instance.size

class DivisionScreen2(Screen):  # إضافة "2" لاسم الكلاس
    def __init__(self, **kwargs):
        super(DivisionScreen2, self).__init__(**kwargs)  # تعديل اسم الكلاس

        self.save_file2 = "division_progress2.json"  # إضافة "2" لاسم الملف
        self.load_progress2()  # تعديل اسم الدالة

        layout2 = BoxLayout(orientation='vertical', padding=20, spacing=10)  # إضافة "2" لاسم المتغير

        with layout2.canvas.before:  # تعديل اسم المتغير
            Color(0.9, 0.9, 0.9, 1)
            self.rect2 = Rectangle(size=self.size, pos=self.pos)  # تعديل اسم المتغير
            layout2.bind(size=self._update_rect2, pos=self._update_rect2)  # تعديل اسم الدالة

        title2 = Label(text="Division Section", font_size='24sp', size_hint=(1, 0.1), color=(1, 1, 1, 1))
        layout2.add_widget(title2)  # تعديل اسم المتغير

        with title2.canvas.before:  # تعديل اسم المتغير
            Color(0.2, 0.4, 0.6, 1)
            self.rect_title2 = Rectangle(size=title2.size, pos=title2.pos)  # تعديل اسم المتغير
            title2.bind(size=self._update_rect_title2, pos=self._update_rect_title2)  # تعديل اسم الدالة

        examples_text2 = Label(text="Examples:\n20 ÷ 2 = 10\n24 ÷ 4 = 6\n30 ÷ 5 = 6\n50 ÷ 5 = 10",
                               size_hint=(1, 0.3), color=(0, 0, 0, 1))
        layout2.add_widget(examples_text2)  # تعديل اسم المتغير

        with examples_text2.canvas.before:  # تعديل اسم المتغير
            Color(0.8, 0.9, 1, 1)
            self.rect_examples2 = Rectangle(size=examples_text2.size, pos=examples_text2.pos)  # تعديل اسم المتغير
            examples_text2.bind(size=self._update_rect_examples2, pos=self._update_rect_examples2)  # تعديل اسم الدالة

        self.current_question_layout2 = BoxLayout(orientation='horizontal', spacing=10)  # تعديل اسم المتغير
        self.current_question_label2 = Label(text="", size_hint=(0.7, None), height='30dp', color=(0, 0, 0, 1))  # تعديل اسم المتغير
        self.current_answer_input2 = TextInput(hint_text='Enter your answer', size_hint=(0.3, None), height='30dp')  # تعديل اسم المتغير
        self.current_question_layout2.add_widget(self.current_question_label2)  # تعديل اسم المتغير
        self.current_question_layout2.add_widget(self.current_answer_input2)  # تعديل اسم المتغير
        layout2.add_widget(self.current_question_layout2)  # تعديل اسم المتغير

        status_layout2 = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))  # تعديل اسم المتغير
        self.coins_label2 = Label(text=f"Coins: {self.coins2}", size_hint=(0.5, 1), color=(0, 0.5, 0, 1))  # تعديل اسم المتغير
        self.hearts_label2 = Label(text=f"Hearts: {self.hearts2}", size_hint=(0.5, 1), color=(1, 0, 0, 1))  # تعديل اسم المتغير
        status_layout2.add_widget(self.coins_label2)  # تعديل اسم المتغير
        status_layout2.add_widget(self.hearts_label2)  # تعديل اسم المتغير
        layout2.add_widget(status_layout2)  # تعديل اسم المتغير

        submit_button2 = Button(text="Submit Answer", size_hint=(1, 0.1))  # تعديل اسم المتغير
        submit_button2.bind(on_press=self.check_answer2)  # تعديل اسم الدالة
        layout2.add_widget(submit_button2)  # تعديل اسم المتغير

        self.add_back_button2(layout2)  # تعديل اسم الدالة والمتغير

        self.add_widget(layout2)  # تعديل اسم المتغير

        self.show_current_question2()  # تعديل اسم الدالة

    def show_current_question2(self):  # تعديل اسم الدالة
        if self.current_question_index2 < len(self.correct_answers2):  # تعديل اسم المتغير
            num1 = 20 + (self.current_question_index2 * 2)  # تعديل المنطق لبدء الأرقام من 20 إلى 50
            num2 = 2 if num1 % 4 == 0 else 5
            self.current_question_label2.text = f"Question {self.current_question_index2 + 1}: {num1} ÷ {num2} ="  # تعديل اسم المتغير
        else:
            self.current_question_label2.text = "All questions completed!"  # تعديل اسم المتغير

    def check_answer2(self, instance):  # تعديل اسم الدالة
        try:
            answer = int(self.current_answer_input2.text)  # تعديل اسم المتغير
            correct_answer = self.correct_answers2[self.current_question_index2]  # تعديل اسم المتغير
            if answer == correct_answer:
                self.coins2 += 10  # تعديل اسم المتغير
                self.update_status2()  # تعديل اسم الدالة
                self.current_question_index2 += 1  # تعديل اسم المتغير
                self.save_progress2()  # تعديل اسم الدالة
                self.show_current_question2()  # تعديل اسم الدالة
            else:
                self.hearts2 -= 1  # تعديل اسم المتغير
                self.update_status2()  # تعديل اسم الدالة
                if self.hearts2 <= 0:  # تعديل اسم المتغير
                    print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")
        except ValueError:
            self.hearts2 -= 1  # تعديل اسم المتغير
            self.update_status2()  # تعديل اسم الدالة

        self.current_answer_input2.text = ""  # تعديل اسم المتغير

    def update_status2(self):  # تعديل اسم الدالة
        self.coins_label2.text = f"Coins: {self.coins2}"  # تعديل اسم المتغير
        self.hearts_label2.text = f"Hearts: {self.hearts2}"  # تعديل اسم المتغير

    def add_back_button2(self, layout2):  # تعديل اسم الدالة والمتغير
        back_button2 = Button(text="Back", size_hint=(1, 0.1))  # تعديل اسم المتغير
        def go_back(instance):
            self.manager.current = 'level2'  # تعديل اسم الكلاس
        back_button2.bind(on_press=go_back)  # تعديل اسم المتغير
        layout2.add_widget(back_button2)  # تعديل اسم المتغير

    def load_progress2(self):  # تعديل اسم الدالة
        if os.path.exists(self.save_file2):  # تعديل اسم المتغير
            with open(self.save_file2, 'r') as file:  # تعديل اسم المتغير
                data = json.load(file)
                self.coins2 = data.get('coins2', 0)  # تعديل اسم المتغير
                self.hearts2 = data.get('hearts2', 10)  # تعديل اسم المتغير
                self.current_question_index2 = data.get('current_question2', 0)  # تعديل اسم المتغير
                self.correct_answers2 = data.get('correct_answers2', self.generate_correct_answers2())  # تعديل اسم المتغير
        else:
            self.coins2 = 0  # تعديل اسم المتغير
            self.hearts2 = 10  # تعديل اسم المتغير
            self.current_question_index2 = 0  # تعديل اسم المتغير
            self.correct_answers2 = self.generate_correct_answers2()  # تعديل اسم المتغير

    def save_progress2(self):  # تعديل اسم الدالة
        data = {
            'coins2': self.coins2,  # تعديل اسم المتغير
            'hearts2': self.hearts2,  # تعديل اسم المتغير
            'current_question2': self.current_question_index2,  # تعديل اسم المتغير
            'correct_answers2': self.correct_answers2  # تعديل اسم المتغير
        }
        with open(self.save_file2, 'w') as file:  # تعديل اسم المتغير
            json.dump(data, file)

    def generate_correct_answers2(self):  # تعديل اسم الدالة
        correct_answers2 = []  # تعديل اسم المتغير
        for i in range(15):
            num1 = 20 + (i * 2)  # الأرقام الزوجية من 20 إلى 50
            num2 = 2 if num1 % 4 == 0 else 5  # القسمة على 2 أو 5
            correct_answers2.append(num1 // num2)  # تعديل اسم المتغير
        return correct_answers2

    def _update_rect2(self, instance, value):  # تعديل اسم الدالة
        self.rect2.pos = instance.pos  # تعديل اسم المتغير
        self.rect2.size = instance.size  # تعديل اسم المتغير

    def _update_rect_title2(self, instance, value):  # تعديل اسم الدالة
        self.rect_title2.pos = instance.pos  # تعديل اسم المتغير
        self.rect_title2.size = instance.size  # تعديل اسم المتغير

    def _update_rect_examples2(self, instance, value):  # تعديل اسم الدالة
        self.rect_examples2.pos = instance.pos  # تعديل اسم المتغير
        self.rect_examples2.size = instance.size  # تعديل اسم المتغير

class Level3Screen(Screen):
    def __init__(self, **kwargs):
        super(Level3Screen, self).__init__(**kwargs)
        
        layout11 = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        title11 = Label(text="LEVEL3", font_size='24sp', size_hint=(1, 0.1))
        layout11.add_widget(title11)

        # Sections buttons
        section_layout11 = GridLayout(cols=2, spacing=10, size_hint_y=None, height='120dp')

        addition_button11 = Button(text="Addition", size_hint=(0.45, 0.5))
        addition_button11.bind(on_press=self.go_to_addition_3)
        section_layout11.add_widget(addition_button11)

        Subtraction_button11 = Button(text="Subtraction", size_hint=(0.45, 0.5))
        # Bind the button to a method for subtraction
        Subtraction_button11.bind(on_press=self.go_to_Subtraction_3)

        section_layout11.add_widget(Subtraction_button11)

        multiplication_button11 = Button(text="Multiplication", size_hint=(0.45, 0.5))
        # Bind the button to a method for multiplication
        multiplication_button11.bind(on_press=self.go_to_Multiplication_3)
        section_layout11.add_widget(multiplication_button11)

        division_button11 = Button(text="Division", size_hint=(0.45, 0.5))
        # Bind the button to a method for division
        division_button11.bind(on_press=self.go_to_Division_3)
        section_layout11.add_widget(division_button11)

        layout11.add_widget(section_layout11)

        # Back Button
        self.add_back_button(layout11)

        self.add_widget(layout11)

    def go_to_addition_3(self, instance):
        self.manager.current = 'Addition3'
    def go_to_Subtraction_3(self, instance):
        self.manager.current = 'Subtraction3'
    def go_to_Multiplication_3(self, instance):
        self.manager.current='multiplication3'

    def go_to_Division_3(self, instance):
        self.manager.current= 'division3'
    

    def add_back_button(self, layout):
        back_button = Button(text="Back", size_hint=(1, 0.01))
        def go_back(instance):
            self.manager.current = 'difficulty'
        back_button.bind(on_press=go_back)
        layout.add_widget(back_button)
class DivisionScreen3(Screen):  # تعديل اسم الكلاس
    def __init__(self, **kwargs):
        super(DivisionScreen3, self).__init__(**kwargs)  # تعديل اسم الكلاس

        self.save_file3 = "division_progress3.json"  # تعديل اسم الملف
        self.load_progress3()  # تعديل اسم الدالة

        layout3 = BoxLayout(orientation='vertical', padding=20, spacing=10)  # تعديل اسم المتغير

        with layout3.canvas.before:  # تعديل اسم المتغير
            Color(0.9, 0.9, 0.9, 1)
            self.rect3 = Rectangle(size=self.size, pos=self.pos)  # تعديل اسم المتغير
            layout3.bind(size=self._update_rect3, pos=self._update_rect3)  # تعديل اسم الدالة

        title3 = Label(text="Advanced Division Section", font_size='24sp', size_hint=(1, 0.1), color=(1, 1, 1, 1))
        layout3.add_widget(title3)  # تعديل اسم المتغير

        with title3.canvas.before:  # تعديل اسم المتغير
            Color(0.2, 0.4, 0.6, 1)
            self.rect_title3 = Rectangle(size=title3.size, pos=title3.pos)  # تعديل اسم المتغير
            title3.bind(size=self._update_rect_title3, pos=self._update_rect_title3)  # تعديل اسم الدالة

        examples_text3 = Label(text="Examples:\n100 ÷ 4 = 25\n120 ÷ 6 = 20\n144 ÷ 8 = 18\n196 ÷ 14 = 14",
                               size_hint=(1, 0.3), color=(0, 0, 0, 1))  # صعوبة أعلى
        layout3.add_widget(examples_text3)  # تعديل اسم المتغير

        with examples_text3.canvas.before:  # تعديل اسم المتغير
            Color(0.8, 0.9, 1, 1)
            self.rect_examples3 = Rectangle(size=examples_text3.size, pos=examples_text3.pos)  # تعديل اسم المتغير
            examples_text3.bind(size=self._update_rect_examples3, pos=self._update_rect_examples3)  # تعديل اسم الدالة

        self.current_question_layout3 = BoxLayout(orientation='horizontal', spacing=10)  # تعديل اسم المتغير
        self.current_question_label3 = Label(text="", size_hint=(0.7, None), height='30dp', color=(0, 0, 0, 1))  # تعديل اسم المتغير
        self.current_answer_input3 = TextInput(hint_text='Enter your answer', size_hint=(0.3, None), height='30dp')  # تعديل اسم المتغير
        self.current_question_layout3.add_widget(self.current_question_label3)  # تعديل اسم المتغير
        self.current_question_layout3.add_widget(self.current_answer_input3)  # تعديل اسم المتغير
        layout3.add_widget(self.current_question_layout3)  # تعديل اسم المتغير

        status_layout3 = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))  # تعديل اسم المتغير
        self.coins_label3 = Label(text=f"Coins: {self.coins3}", size_hint=(0.5, 1), color=(0, 0.5, 0, 1))  # تعديل اسم المتغير
        self.hearts_label3 = Label(text=f"Hearts: {self.hearts3}", size_hint=(0.5, 1), color=(1, 0, 0, 1))  # تعديل اسم المتغير
        status_layout3.add_widget(self.coins_label3)  # تعديل اسم المتغير
        status_layout3.add_widget(self.hearts_label3)  # تعديل اسم المتغير
        layout3.add_widget(status_layout3)  # تعديل اسم المتغير

        submit_button3 = Button(text="Submit Answer", size_hint=(1, 0.1))  # تعديل اسم المتغير
        submit_button3.bind(on_press=self.check_answer3)  # تعديل اسم الدالة
        layout3.add_widget(submit_button3)  # تعديل اسم المتغير

        self.add_back_button3(layout3)  # تعديل اسم الدالة والمتغير

        self.add_widget(layout3)  # تعديل اسم المتغير

        self.show_current_question3()  # تعديل اسم الدالة

    def show_current_question3(self):  # تعديل اسم الدالة
        if self.current_question_index3 < len(self.correct_answers3):  # تعديل اسم المتغير
            num1 = 100 + (self.current_question_index3 * 10)  # زيادة الأرقام لزيادة الصعوبة
            num2 = 4 if num1 % 4 == 0 else 7
            self.current_question_label3.text = f"Question {self.current_question_index3 + 1}: {num1} ÷ {num2} ="  # تعديل اسم المتغير
        else:
            self.current_question_label3.text = "All questions completed!"  # تعديل اسم المتغير

    def check_answer3(self, instance):  # تعديل اسم الدالة
        try:
            answer = int(self.current_answer_input3.text)  # تعديل اسم المتغير
            correct_answer = self.correct_answers3[self.current_question_index3]  # تعديل اسم المتغير
            if answer == correct_answer:
                self.coins3 += 15  # تعديل اسم المتغير وزيادة المكافأة
                self.update_status3()  # تعديل اسم الدالة
                self.current_question_index3 += 1  # تعديل اسم المتغير
                self.save_progress3()  # تعديل اسم الدالة
                self.show_current_question3()  # تعديل اسم الدالة
            else:
                self.hearts3 -= 1  # تعديل اسم المتغير
                self.update_status3()  # تعديل اسم الدالة
                if self.hearts3 <= 0:  # تعديل اسم المتغير
                    print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")
        except ValueError:
            self.hearts3 -= 1  # تعديل اسم المتغير
            self.update_status3()  # تعديل اسم الدالة

        self.current_answer_input3.text = ""  # تعديل اسم المتغير

    def update_status3(self):  # تعديل اسم الدالة
        self.coins_label3.text = f"Coins: {self.coins3}"  # تعديل اسم المتغير
        self.hearts_label3.text = f"Hearts: {self.hearts3}"  # تعديل اسم المتغير

    def add_back_button3(self, layout3):  # تعديل اسم الدالة والمتغير
        back_button3 = Button(text="Back", size_hint=(1, 0.1))  # تعديل اسم المتغير
        def go_back(instance):
            self.manager.current = 'level3'  # تعديل اسم الكلاس
        back_button3.bind(on_press=go_back)  # تعديل اسم المتغير
        layout3.add_widget(back_button3)  # تعديل اسم المتغير

    def load_progress3(self):  # تعديل اسم الدالة
        if os.path.exists(self.save_file3):  # تعديل اسم المتغير
            with open(self.save_file3, 'r') as file:  # تعديل اسم المتغير
                data = json.load(file)
                self.coins3 = data.get('coins3', 0)  # تعديل اسم المتغير
                self.hearts3 = data.get('hearts3', 10)  # تعديل اسم المتغير
                self.current_question_index3 = data.get('current_question3', 0)  # تعديل اسم المتغير
                self.correct_answers3 = data.get('correct_answers3', self.generate_correct_answers3())  # تعديل اسم المتغير
        else:
            self.coins3 = 0  # تعديل اسم المتغير
            self.hearts3 = 10  # تعديل اسم المتغير
            self.current_question_index3 = 0  # تعديل اسم المتغير
            self.correct_answers3 = self.generate_correct_answers3()  # تعديل اسم المتغير

    def save_progress3(self):  # تعديل اسم الدالة
        data = {
            'coins3': self.coins3,  # تعديل اسم المتغير
            'hearts3': self.hearts3,  # تعديل اسم المتغير
            'current_question3': self.current_question_index3,  # تعديل اسم المتغير
            'correct_answers3': self.correct_answers3  # تعديل اسم المتغير
        }
        with open(self.save_file3, 'w') as file:  # تعديل اسم المتغير
            json.dump(data, file)

    def generate_correct_answers3(self):  # تعديل اسم الدالة
        correct_answers3 = []  # تعديل اسم المتغير
        for i in range(15):
            num1 = 100 + (i * 10)  # الأرقام الأكبر لتكون أكثر تحديًا
            num2 = 4 if num1 % 4 == 0 else 7
            correct_answers3.append(num1 // num2)  # تعديل اسم المتغير
        return correct_answers3

    def _update_rect3(self, instance, value):  # تعديل اسم الدالة
        self.rect3.pos = instance.pos  # تعديل اسم المتغير
        self.rect3.size = instance.size  # تعديل اسم المتغير

    def _update_rect_title3(self, instance, value):  # تعديل اسم الدالة
        self.rect_title3.pos = instance.pos  # تعديل اسم المتغير
        self.rect_title3.size = instance.size  # تعديل اسم المتغير

    def _update_rect_examples3(self, instance, value):  # تعديل اسم الدالة
        self.rect_examples3.pos = instance.pos  # تعديل اسم المتغير
        self.rect_examples3.size = instance.size  # تعديل اسم المتغير
    
class MultiplicationScreen3(Screen):  # تعديل اسم الكلاس
    def __init__(self, **kwargs):
        super(MultiplicationScreen3, self).__init__(**kwargs)  # تعديل اسم الكلاس

        self.save_file3 = "multiplication_progress3.json"  # تعديل اسم الملف
        self.load_progress3()  # تعديل اسم الدالة

        layout3 = BoxLayout(orientation='vertical', padding=20, spacing=10)  # تعديل اسم المتغير

        with layout3.canvas.before:  # تعديل اسم المتغير
            Color(0.9, 0.9, 0.9, 1)
            self.rect3 = Rectangle(size=self.size, pos=self.pos)  # تعديل اسم المتغير
            layout3.bind(size=self._update_rect3, pos=self._update_rect3)  # تعديل اسم الدالة

        title3 = Label(text="Advanced Multiplication Section", font_size='24sp', size_hint=(1, 0.1), color=(1, 1, 1, 1))
        layout3.add_widget(title3)  # تعديل اسم المتغير

        with title3.canvas.before:  # تعديل اسم المتغير
            Color(0.2, 0.4, 0.6, 1)
            self.rect_title3 = Rectangle(size=title3.size, pos=title3.pos)  # تعديل اسم المتغير
            title3.bind(size=self._update_rect_title3, pos=self._update_rect_title3)  # تعديل اسم الدالة

        examples_text3 = Label(text="Examples:\n15 × 12 = 180\n25 × 14 = 350\n18 × 16 = 288\n21 × 19 = 399",
                               size_hint=(1, 0.3), color=(0, 0, 0, 1))  # صعوبة أعلى
        layout3.add_widget(examples_text3)  # تعديل اسم المتغير

        with examples_text3.canvas.before:  # تعديل اسم المتغير
            Color(0.8, 0.9, 1, 1)
            self.rect_examples3 = Rectangle(size=examples_text3.size, pos=examples_text3.pos)  # تعديل اسم المتغير
            examples_text3.bind(size=self._update_rect_examples3, pos=self._update_rect_examples3)  # تعديل اسم الدالة

        self.current_question_layout3 = BoxLayout(orientation='horizontal', spacing=10)  # تعديل اسم المتغير
        self.current_question_label3 = Label(text="", size_hint=(0.7, None), height='30dp', color=(0, 0, 0, 1))  # تعديل اسم المتغير
        self.current_answer_input3 = TextInput(hint_text='Enter your answer', size_hint=(0.3, None), height='30dp')  # تعديل اسم المتغير
        self.current_question_layout3.add_widget(self.current_question_label3)  # تعديل اسم المتغير
        self.current_question_layout3.add_widget(self.current_answer_input3)  # تعديل اسم المتغير
        layout3.add_widget(self.current_question_layout3)  # تعديل اسم المتغير

        status_layout3 = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))  # تعديل اسم المتغير
        self.coins_label3 = Label(text=f"Coins: {self.coins3}", size_hint=(0.5, 1), color=(0, 0.5, 0, 1))  # تعديل اسم المتغير
        self.hearts_label3 = Label(text=f"Hearts: {self.hearts3}", size_hint=(0.5, 1), color=(1, 0, 0, 1))  # تعديل اسم المتغير
        status_layout3.add_widget(self.coins_label3)  # تعديل اسم المتغير
        status_layout3.add_widget(self.hearts_label3)  # تعديل اسم المتغير
        layout3.add_widget(status_layout3)  # تعديل اسم المتغير

        submit_button3 = Button(text="Submit Answer", size_hint=(1, 0.1))  # تعديل اسم المتغير
        submit_button3.bind(on_press=self.check_answer3)  # تعديل اسم الدالة
        layout3.add_widget(submit_button3)  # تعديل اسم المتغير

        self.add_back_button3(layout3)  # تعديل اسم الدالة والمتغير

        self.add_widget(layout3)  # تعديل اسم المتغير

        self.show_current_question3()  # تعديل اسم الدالة

    def show_current_question3(self):  # تعديل اسم الدالة
        if self.current_question_index3 < len(self.correct_answers3):  # تعديل اسم المتغير
            num1 = 15 + (self.current_question_index3 * 2)  # زيادة الأرقام لزيادة الصعوبة
            num2 = 12 + (self.current_question_index3 * 2)
            self.current_question_label3.text = f"Question {self.current_question_index3 + 1}: {num1} × {num2} ="  # تعديل اسم المتغير
        else:
            self.current_question_label3.text = "All questions completed!"  # تعديل اسم المتغير

    def check_answer3(self, instance):  # تعديل اسم الدالة
        try:
            answer = int(self.current_answer_input3.text)  # تعديل اسم المتغير
            correct_answer = self.correct_answers3[self.current_question_index3]  # تعديل اسم المتغير
            if answer == correct_answer:
                self.coins3 += 15  # تعديل اسم المتغير وزيادة المكافأة
                self.update_status3()  # تعديل اسم الدالة
                self.current_question_index3 += 1  # تعديل اسم المتغير
                self.save_progress3()  # تعديل اسم الدالة
                self.show_current_question3()  # تعديل اسم الدالة
            else:
                self.hearts3 -= 1  # تعديل اسم المتغير
                self.update_status3()  # تعديل اسم الدالة
                if self.hearts3 <= 0:  # تعديل اسم المتغير
                    print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")
        except ValueError:
            self.hearts3 -= 1  # تعديل اسم المتغير
            self.update_status3()  # تعديل اسم الدالة

        self.current_answer_input3.text = ""  # تعديل اسم المتغير

    def update_status3(self):  # تعديل اسم الدالة
        self.coins_label3.text = f"Coins: {self.coins3}"  # تعديل اسم المتغير
        self.hearts_label3.text = f"Hearts: {self.hearts3}"  # تعديل اسم المتغير

    def add_back_button3(self, layout3):  # تعديل اسم الدالة والمتغير
        back_button3 = Button(text="Back", size_hint=(1, 0.1))  # تعديل اسم المتغير
        def go_back(instance):
            self.manager.current = 'level3'  # تعديل اسم الكلاس
        back_button3.bind(on_press=go_back)  # تعديل اسم المتغير
        layout3.add_widget(back_button3)  # تعديل اسم المتغير

    def load_progress3(self):  # تعديل اسم الدالة
        if os.path.exists(self.save_file3):  # تعديل اسم المتغير
            with open(self.save_file3, 'r') as file:  # تعديل اسم المتغير
                data = json.load(file)
                self.coins3 = data.get('coins3', 0)  # تعديل اسم المتغير
                self.hearts3 = data.get('hearts3', 10)  # تعديل اسم المتغير
                self.current_question_index3 = data.get('current_question3', 0)  # تعديل اسم المتغير
                self.correct_answers3 = data.get('correct_answers3', self.generate_correct_answers3())  # تعديل اسم المتغير
        else:
            self.coins3 = 0  # تعديل اسم المتغير
            self.hearts3 = 10  # تعديل اسم المتغير
            self.current_question_index3 = 0  # تعديل اسم المتغير
            self.correct_answers3 = self.generate_correct_answers3()  # تعديل اسم المتغير

    def save_progress3(self):  # تعديل اسم الدالة
        data = {
            'coins3': self.coins3,  # تعديل اسم المتغير
            'hearts3': self.hearts3,  # تعديل اسم المتغير
            'current_question3': self.current_question_index3,  # تعديل اسم المتغير
            'correct_answers3': self.correct_answers3  # تعديل اسم المتغير
        }
        with open(self.save_file3, 'w') as file:  # تعديل اسم المتغير
            json.dump(data, file)

    def generate_correct_answers3(self):  # تعديل اسم الدالة
        correct_answers3 = []  # تعديل اسم المتغير
        for i in range(15):
            num1 = 15 + (i * 2)  # الأرقام الأكبر لتكون أكثر تحديًا
            num2 = 12 + (i * 2)
            correct_answers3.append(num1 * num2)  # تعديل اسم المتغير
        return correct_answers3

    def _update_rect3(self, instance, value):  # تعديل اسم الدالة
        self.rect3.pos = instance.pos  # تعديل اسم المتغير
        self.rect3.size = instance.size  # تعديل اسم المتغير

    def _update_rect_title3(self, instance, value):  # تعديل اسم الدالة
        self.rect_title3.pos = instance.pos  # تعديل اسم المتغير
        self.rect_title3.size = instance.size  # تعديل اسم المتغير

    def _update_rect_examples3(self, instance, value):  # تعديل اسم الدالة
        self.rect_examples3.pos = instance.pos  # تعديل اسم المتغير
        self.rect_examples3.size = instance.size  # تعديل اسم المتغير


class SubtractionScreen3(Screen):  # تعديل اسم الكلاس
    def __init__(self, **kwargs):
        super(SubtractionScreen3, self).__init__(**kwargs)  # تعديل اسم الكلاس

        self.save_file3 = "subtraction_progress3.json"  # تعديل اسم الملف
        self.load_progress3()  # تعديل اسم الدالة

        layout3 = BoxLayout(orientation='vertical', padding=20, spacing=10)  # تعديل اسم المتغير

        with layout3.canvas.before:  # تعديل اسم المتغير
            Color(0.9, 0.9, 0.9, 1)
            self.rect3 = Rectangle(size=self.size, pos=self.pos)  # تعديل اسم المتغير
            layout3.bind(size=self._update_rect3, pos=self._update_rect3)  # تعديل اسم الدالة

        title3 = Label(text="Advanced Subtraction Section", font_size='24sp', size_hint=(1, 0.1), color=(1, 1, 1, 1))
        layout3.add_widget(title3)  # تعديل اسم المتغير

        with title3.canvas.before:  # تعديل اسم المتغير
            Color(0.2, 0.4, 0.6, 1)
            self.rect_title3 = Rectangle(size=title3.size, pos=title3.pos)  # تعديل اسم المتغير
            title3.bind(size=self._update_rect_title3, pos=self._update_rect_title3)  # تعديل اسم الدالة

        examples_text3 = Label(text="Examples:\n80 - 35 = 45\n92 - 47 = 45\n63 - 28 = 35\n75 - 31 = 44",
                               size_hint=(1, 0.3), color=(0, 0, 0, 1))  # صعوبة أعلى
        layout3.add_widget(examples_text3)  # تعديل اسم المتغير

        with examples_text3.canvas.before:  # تعديل اسم المتغير
            Color(0.8, 0.9, 1, 1)
            self.rect_examples3 = Rectangle(size=examples_text3.size, pos=examples_text3.pos)  # تعديل اسم المتغير
            examples_text3.bind(size=self._update_rect_examples3, pos=self._update_rect_examples3)  # تعديل اسم الدالة

        self.current_question_layout3 = BoxLayout(orientation='horizontal', spacing=10)  # تعديل اسم المتغير
        self.current_question_label3 = Label(text="", size_hint=(0.7, None), height='30dp', color=(0, 0, 0, 1))  # تعديل اسم المتغير
        self.current_answer_input3 = TextInput(hint_text='Enter your answer', size_hint=(0.3, None), height='30dp')  # تعديل اسم المتغير
        self.current_question_layout3.add_widget(self.current_question_label3)  # تعديل اسم المتغير
        self.current_question_layout3.add_widget(self.current_answer_input3)  # تعديل اسم المتغير
        layout3.add_widget(self.current_question_layout3)  # تعديل اسم المتغير

        status_layout3 = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))  # تعديل اسم المتغير
        self.coins_label3 = Label(text=f"Coins: {self.coins3}", size_hint=(0.5, 1), color=(0, 0.5, 0, 1))  # تعديل اسم المتغير
        self.hearts_label3 = Label(text=f"Hearts: {self.hearts3}", size_hint=(0.5, 1), color=(1, 0, 0, 1))  # تعديل اسم المتغير
        status_layout3.add_widget(self.coins_label3)  # تعديل اسم المتغير
        status_layout3.add_widget(self.hearts_label3)  # تعديل اسم المتغير
        layout3.add_widget(status_layout3)  # تعديل اسم المتغير

        submit_button3 = Button(text="Submit Answer", size_hint=(1, 0.1))  # تعديل اسم المتغير
        submit_button3.bind(on_press=self.check_answer3)  # تعديل اسم الدالة
        layout3.add_widget(submit_button3)  # تعديل اسم المتغير

        self.add_back_button3(layout3)  # تعديل اسم الدالة والمتغير

        self.add_widget(layout3)  # تعديل اسم المتغير

        self.show_current_question3()  # تعديل اسم الدالة

    def show_current_question3(self):  # تعديل اسم الدالة
        if self.current_question_index3 < len(self.correct_answers3):  # تعديل اسم المتغير
            num1 = 80 + (self.current_question_index3 * 2)  # زيادة الأرقام لزيادة الصعوبة
            num2 = num1 - 45 - (self.current_question_index3 % 10)
            self.current_question_label3.text = f"Question {self.current_question_index3 + 1}: {num1} - {num2} ="  # تعديل اسم المتغير
        else:
            self.current_question_label3.text = "All questions completed!"  # تعديل اسم المتغير

    def check_answer3(self, instance):  # تعديل اسم الدالة
        try:
            answer = int(self.current_answer_input3.text)  # تعديل اسم المتغير
            correct_answer = self.correct_answers3[self.current_question_index3]  # تعديل اسم المتغير
            if answer == correct_answer:
                self.coins3 += 15  # تعديل اسم المتغير وزيادة المكافأة
                self.update_status3()  # تعديل اسم الدالة
                self.current_question_index3 += 1  # تعديل اسم المتغير
                self.save_progress3()  # تعديل اسم الدالة
                self.show_current_question3()  # تعديل اسم الدالة
            else:
                self.hearts3 -= 1  # تعديل اسم المتغير
                self.update_status3()  # تعديل اسم الدالة
                if self.hearts3 <= 0:  # تعديل اسم المتغير
                    print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")
        except ValueError:
            self.hearts3 -= 1  # تعديل اسم المتغير
            self.update_status3()  # تعديل اسم الدالة

        self.current_answer_input3.text = ""  # تعديل اسم المتغير

    def update_status3(self):  # تعديل اسم الدالة
        self.coins_label3.text = f"Coins: {self.coins3}"  # تعديل اسم المتغير
        self.hearts_label3.text = f"Hearts: {self.hearts3}"  # تعديل اسم المتغير

    def add_back_button3(self, layout3):  # تعديل اسم الدالة والمتغير
        back_button3 = Button(text="Back", size_hint=(1, 0.1))  # تعديل اسم المتغير
        def go_back(instance):
            self.manager.current = 'level3'  # تعديل اسم الكلاس
        back_button3.bind(on_press=go_back)  # تعديل اسم المتغير
        layout3.add_widget(back_button3)  # تعديل اسم المتغير

    def load_progress3(self):  # تعديل اسم الدالة
        if os.path.exists(self.save_file3):  # تعديل اسم المتغير
            with open(self.save_file3, 'r') as file:  # تعديل اسم المتغير
                data = json.load(file)
                self.coins3 = data.get('coins3', 0)  # تعديل اسم المتغير
                self.hearts3 = data.get('hearts3', 10)  # تعديل اسم المتغير
                self.current_question_index3 = data.get('current_question3', 0)  # تعديل اسم المتغير
                self.correct_answers3 = data.get('correct_answers3', self.generate_correct_answers3())  # تعديل اسم المتغير
        else:
            self.coins3 = 0  # تعديل اسم المتغير
            self.hearts3 = 10  # تعديل اسم المتغير
            self.current_question_index3 = 0  # تعديل اسم المتغير
            self.correct_answers3 = self.generate_correct_answers3()  # تعديل اسم المتغير

    def save_progress3(self):  # تعديل اسم الدالة
        data = {
            'coins3': self.coins3,  # تعديل اسم المتغير
            'hearts3': self.hearts3,  # تعديل اسم المتغير
            'current_question3': self.current_question_index3,  # تعديل اسم المتغير
            'correct_answers3': self.correct_answers3  # تعديل اسم المتغير
        }
        with open(self.save_file3, 'w') as file:  # تعديل اسم المتغير
            json.dump(data, file)

    def generate_correct_answers3(self):  # تعديل اسم الدالة
        correct_answers3 = []  # تعديل اسم المتغير
        for i in range(15):
            num1 = 80 + (i * 2)  # الأرقام الأكبر لتكون أكثر تحديًا
            num2 = num1 - 45 - (i % 10)
            correct_answers3.append(num1 - num2)  # تعديل اسم المتغير
        return correct_answers3

    def _update_rect3(self, instance, value):  # تعديل اسم الدالة
        self.rect3.pos = instance.pos  # تعديل اسم المتغير
        self.rect3.size = instance.size  # تعديل اسم المتغير

    def _update_rect_title3(self, instance, value):  # تعديل اسم الدالة
        self.rect_title3.pos = instance.pos  # تعديل اسم المتغير
        self.rect_title3.size = instance.size  # تعديل اسم المتغير

    def _update_rect_examples3(self, instance, value):  # تعديل اسم الدالة
        self.rect_examples3.pos = instance.pos  # تعديل اسم المتغير
        self.rect_examples3.size = instance.size  # تعديل اسم المتغير



class AdditionScreen3(Screen):  # تعديل اسم الكلاس
    def __init__(self, **kwargs):
        super(AdditionScreen3, self).__init__(**kwargs)  # تعديل اسم الكلاس

        self.save_file3 = "addition_progress3.json"  # تعديل اسم الملف
        self.load_progress3()  # تعديل اسم الدالة

        layout3 = BoxLayout(orientation='vertical', padding=20, spacing=10)  # تعديل اسم المتغير

        with layout3.canvas.before:  # تعديل اسم المتغير
            Color(0.9, 0.9, 0.9, 1)
            self.rect3 = Rectangle(size=self.size, pos=self.pos)  # تعديل اسم المتغير
            layout3.bind(size=self._update_rect3, pos=self._update_rect3)  # تعديل اسم الدالة

        title3 = Label(text="Advanced Addition Section", font_size='24sp', size_hint=(1, 0.1), color=(1, 1, 1, 1))
        layout3.add_widget(title3)  # تعديل اسم المتغير

        with title3.canvas.before:  # تعديل اسم المتغير
            Color(0.2, 0.4, 0.6, 1)
            self.rect_title3 = Rectangle(size=title3.size, pos=title3.pos)  # تعديل اسم المتغير
            title3.bind(size=self._update_rect_title3, pos=self._update_rect_title3)  # تعديل اسم الدالة

        examples_text3 = Label(text="Examples:\n65 + 34 = 99\n72 + 58 = 130\n89 + 76 = 165\n45 + 54 = 99", 
                               size_hint=(1, 0.3), color=(0, 0, 0, 1))  # صعوبة أعلى
        layout3.add_widget(examples_text3)  # تعديل اسم المتغير

        with examples_text3.canvas.before:  # تعديل اسم المتغير
            Color(0.8, 0.9, 1, 1)
            self.rect_examples3 = Rectangle(size=examples_text3.size, pos=examples_text3.pos)  # تعديل اسم المتغير
            examples_text3.bind(size=self._update_rect_examples3, pos=self._update_rect_examples3)  # تعديل اسم الدالة

        self.current_question_layout3 = BoxLayout(orientation='horizontal', spacing=10)  # تعديل اسم المتغير
        self.current_question_label3 = Label(text="", size_hint=(0.7, None), height='30dp', color=(0, 0, 0, 1))  # تعديل اسم المتغير
        self.current_answer_input3 = TextInput(hint_text='Enter your answer', size_hint=(0.3, None), height='30dp')  # تعديل اسم المتغير
        self.current_question_layout3.add_widget(self.current_question_label3)  # تعديل اسم المتغير
        self.current_question_layout3.add_widget(self.current_answer_input3)  # تعديل اسم المتغير
        layout3.add_widget(self.current_question_layout3)  # تعديل اسم المتغير

        status_layout3 = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))  # تعديل اسم المتغير
        self.coins_label3 = Label(text=f"Coins: {self.coins3}", size_hint=(0.5, 1), color=(0, 0.5, 0, 1))  # تعديل اسم المتغير
        self.hearts_label3 = Label(text=f"Hearts: {self.hearts3}", size_hint=(0.5, 1), color=(1, 0, 0, 1))  # تعديل اسم المتغير
        status_layout3.add_widget(self.coins_label3)  # تعديل اسم المتغير
        status_layout3.add_widget(self.hearts_label3)  # تعديل اسم المتغير
        layout3.add_widget(status_layout3)  # تعديل اسم المتغير

        submit_button3 = Button(text="Submit Answer", size_hint=(1, 0.1))  # تعديل اسم المتغير
        submit_button3.bind(on_press=self.check_answer3)  # تعديل اسم الدالة
        layout3.add_widget(submit_button3)  # تعديل اسم المتغير

        self.add_back_button3(layout3)  # تعديل اسم الدالة والمتغير

        self.add_widget(layout3)  # تعديل اسم المتغير

        self.show_current_question3()  # تعديل اسم الدالة

    def show_current_question3(self):  # تعديل اسم الدالة
        if self.current_question_index3 < len(self.correct_answers3):  # تعديل اسم المتغير
            num1 = 65 + (self.current_question_index3 * 7)  # زيادة الأرقام لزيادة الصعوبة
            num2 = 34 + (self.current_question_index3 * 6)
            self.current_question_label3.text = f"Question {self.current_question_index3 + 1}: {num1} + {num2} ="  # تعديل اسم المتغير
        else:
            self.current_question_label3.text = "All questions completed!"  # تعديل اسم المتغير

    def check_answer3(self, instance):  # تعديل اسم الدالة
        try:
            answer = int(self.current_answer_input3.text)  # تعديل اسم المتغير
            correct_answer = self.correct_answers3[self.current_question_index3]  # تعديل اسم المتغير
            if answer == correct_answer:
                self.coins3 += 15  # تعديل اسم المتغير وزيادة المكافأة
                self.update_status3()  # تعديل اسم الدالة
                self.current_question_index3 += 1  # تعديل اسم المتغير
                self.save_progress3()  # تعديل اسم الدالة
                self.show_current_question3()  # تعديل اسم الدالة
            else:
                self.hearts3 -= 1  # تعديل اسم المتغير
                self.update_status3()  # تعديل اسم الدالة
                if self.hearts3 <= 0:  # تعديل اسم المتغير
                    print("You are out of hearts! Wait 3 hours or pay 50 coins for each heart.")
        except ValueError:
            self.hearts3 -= 1  # تعديل اسم المتغير
            self.update_status3()  # تعديل اسم الدالة

        self.current_answer_input3.text = ""  # تعديل اسم المتغير

    def update_status3(self):  # تعديل اسم الدالة
        self.coins_label3.text = f"Coins: {self.coins3}"  # تعديل اسم المتغير
        self.hearts_label3.text = f"Hearts: {self.hearts3}"  # تعديل اسم المتغير

    def add_back_button3(self, layout3):  # تعديل اسم الدالة والمتغير
        back_button3 = Button(text="Back", size_hint=(1, 0.1))  # تعديل اسم المتغير
        def go_back(instance):
            self.manager.current = 'level3'  # تعديل اسم الكلاس
        back_button3.bind(on_press=go_back)  # تعديل اسم المتغير
        layout3.add_widget(back_button3)  # تعديل اسم المتغير

    def load_progress3(self):  # تعديل اسم الدالة
        if os.path.exists(self.save_file3):  # تعديل اسم المتغير
            with open(self.save_file3, 'r') as file:  # تعديل اسم المتغير
                data = json.load(file)
                self.coins3 = data.get('coins3', 0)  # تعديل اسم المتغير
                self.hearts3 = data.get('hearts3', 10)  # تعديل اسم المتغير
                self.current_question_index3 = data.get('current_question3', 0)  # تعديل اسم المتغير
                self.correct_answers3 = data.get('correct_answers3', self.generate_correct_answers3())  # تعديل اسم المتغير
        else:
            self.coins3 = 0  # تعديل اسم المتغير
            self.hearts3 = 10  # تعديل اسم المتغير
            self.current_question_index3 = 0  # تعديل اسم المتغير
            self.correct_answers3 = self.generate_correct_answers3()  # تعديل اسم المتغير

    def save_progress3(self):  # تعديل اسم الدالة
        data = {
            'coins3': self.coins3,  # تعديل اسم المتغير
            'hearts3': self.hearts3,  # تعديل اسم المتغير
            'current_question3': self.current_question_index3,  # تعديل اسم المتغير
            'correct_answers3': self.correct_answers3  # تعديل اسم المتغير
        }
        with open(self.save_file3, 'w') as file:  # تعديل اسم المتغير
            json.dump(data, file)

    def generate_correct_answers3(self):  # تعديل اسم الدالة
        correct_answers3 = []  # تعديل اسم المتغير
        for i in range(15):
            num1 = 65 + (i * 7)  # الأرقام الأكبر لتكون أكثر تحديًا
            num2 = 34 + (i * 6)
            correct_answers3.append(num1 + num2)  # تعديل اسم المتغير
        return correct_answers3

    def _update_rect3(self, instance, value):  # تعديل اسم الدالة
        self.rect3.pos = instance.pos  # تعديل اسم المتغير
        self.rect3.size = instance.size  # تعديل اسم المتغير

    def _update_rect_title3(self, instance, value):  # تعديل اسم الدالة
        self.rect_title3.pos = instance.pos  # تعديل اسم المتغير
        self.rect_title3.size = instance.size  # تعديل اسم المتغير

    def _update_rect_examples3(self, instance, value):  # تعديل اسم الدالة
        self.rect_examples3.pos = instance.pos  # تعديل اسم المتغير
        self.rect_examples3.size = instance.size  # تعديل اسم المتغير




# Screen Manager
class MyScreenManager(ScreenManager):
    pass


# Main Application Class
class CreativityCodeApp(App):
    def build(self):
        sm = MyScreenManager()

        sm.add_widget(DifficultyScreen(name='difficulty'))
        sm.add_widget(SignUpScreen(name='signup'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(AboutUsScreen(name='about_us'))
        sm.add_widget(HelpScreen(name='help'))
        #sm.add_widget(LessonsScreen(name='lessons'))
        sm.add_widget(FirstLevelScreen(name='level1'))
        sm.add_widget(AdditionScreen(name='addition'))
        sm.add_widget(SubtractionScreen(name='Subtraction'))
        sm.add_widget(MultiplicationScreen(name='Multiplication'))
        sm.add_widget(DivisionScreen(name='Division'))
        sm.add_widget(Level2Screen(name='level2'))
        sm.add_widget(AdditionScreen2(name='Addition2'))
        sm.add_widget(SubtractionScreen2(name='Subtraction2'))
        sm.add_widget(MultiplicationScreen2(name='multiplication2'))
        sm.add_widget(DivisionScreen2(name='division2'))
        sm.add_widget(Level3Screen(name='level3'))
        sm.add_widget(AdditionScreen3(name='Addition3'))
        sm.add_widget(SubtractionScreen3(name='Subtraction3'))
        sm.add_widget(MultiplicationScreen3(name='multiplication3'))
        sm.add_widget(DivisionScreen3(name='division3'))

        return sm

if __name__ == '__main__':
    CreativityCodeApp().run()