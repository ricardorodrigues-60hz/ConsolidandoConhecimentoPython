import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]
yellow = [1, 1, 0, 1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding = 10)
        colors = [red, green, blue, purple, yellow]

        for i in range(5):
            btn = Button(text = f"Button {i+1}", background_color = random.choice(colors))
            layout.add_widget(btn)

        return layout

class MainApp(App):
    def build(self):
        btn = Button(text="Press Me", 
                     size_hint=(.5, .5),
                     pos_hint={'center_x': .5, 'center_y': .5})
        btn.bind(on_press=self.on_press)
        return btn

    def on_press(self, instance):
        print("Button Pressed!")


if __name__ == "__main__":
    app = MainApp()
    app.run()


