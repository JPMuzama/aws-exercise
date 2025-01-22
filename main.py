from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        # Créer un layout de type BoxLayout avec une orientation verticale
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Créer un label
        self.label = Label(text="Hello, Kivy!", font_size='20sp')

        # Créer un bouton
        self.button = Button(text="Cliquez-moi!", size_hint=(1, 0.5))

        # Lier l'événement on_press du bouton à la méthode on_button_click
        self.button.bind(on_press=self.on_button_click)

        # Ajouter le label et le bouton au layout
        layout.add_widget(self.label)
        layout.add_widget(self.button)

        return layout

    def on_button_click(self, instance):
        # Changer le texte du label lorsque le bouton est cliqué
        self.label.text = "Vous avez cliqué sur le bouton!"

# Lancer l'application
if __name__ == '__main__':
    SimpleApp().run()
