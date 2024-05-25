from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class CalculatorApp(App):
    def build(self):
        # Создание главного контейнера
        layout = GridLayout(cols=1, spacing=10, padding=10)

        # Создание метки для вывода результата
        self.result_label = Label(text='0', font_size=40, size_hint=(1, 0.3))
        layout.add_widget(self.result_label)

        # Создание контейнеров для кнопок
        buttons_layout = GridLayout(cols=4, spacing=10, padding=10)
        layout.add_widget(buttons_layout)

        # Создание кнопок для цифр и операций
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for button_text in buttons:
            button = Button(text=button_text, font_size=30)
            button.bind(on_release=self.on_button_press)

            if button_text.isdigit():
                # Цифры располагаются по центру
                button.halign = 'center'
                button.valign = 'middle'
            else:
                # Знаки операций располагаются справа, снизу и сверху
                button.halign = 'right'
                button.valign = 'bottom'

            buttons_layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        # Обработка нажатия кнопки
        button_text = instance.text
        current_text = self.result_label.text

        if button_text == '=':
            try:
                result = str(eval(current_text))
                self.result_label.text = result
            except Exception:
                self.result_label.text = 'Error'
        else:
            if current_text == '0':
                self.result_label.text = button_text
            else:
                self.result_label.text += button_text


if __name__ == '__main__':
    CalculatorApp().run()