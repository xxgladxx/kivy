from kivy.app import App
from kivy.uix.button import Button


class SimpleKivyApp(App):
    def build(self):
        # Create a button
        button = Button(text="Click me!")
        
        # Bind the button click event to the on_button_click method
        button.bind(on_press=self.on_button_click)
        
        # Return the button as the root widget of the app
        return button

    def on_button_click(self, instance):
        # Method to be called when the button is clicked
        print("Button clicked!")


# Run the Kivy app
if __name__ == '__main__':
    SimpleKivyApp().run()
