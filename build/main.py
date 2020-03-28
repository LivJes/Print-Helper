from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        fontSize = 80
        numberFontSize = 120
        main_layout = BoxLayout(orientation="vertical", padding=[50, 5])
        lengthLayout = BoxLayout(orientation="horizontal", padding = [0, 5], spacing = 20)
        lengthLabel = Label(text="Dĺžka (m)", font_size=fontSize, halign="left")
        self.length = TextInput(text="0", multiline=False, readonly=False, halign="right", font_size=numberFontSize)
        dimensionLayout = BoxLayout(orientation="horizontal", padding = [0, 5], spacing = 20)
        dimensionsLabel = Label(text="Výška (mm)", font_size=fontSize, halign="left")
        self.dimensions = TextInput(text="0", multiline=False, readonly=False, halign="right", font_size=numberFontSize)
        quantityLayout = BoxLayout(orientation="horizontal", padding = [0, 5], spacing = 20)
        quantityLabel = Label(text="Počet etikiet", font_size=fontSize, halign="left")
        self.quantity = TextInput(text="0", multiline=False, readonly=False, halign="right", font_size=numberFontSize)
        productionLayout = BoxLayout(orientation="horizontal", padding = [0, 5], spacing = 20)
        productionLabel = Label(text="Produkcia", font_size=fontSize, halign="left")
        self.production = TextInput(text="1", multiline=False, readonly=False, halign="right", font_size=numberFontSize)
        lengthLayout.add_widget(lengthLabel)
        lengthLayout.add_widget(self.length)
        main_layout.add_widget(lengthLayout)
        dimensionLayout.add_widget(dimensionsLabel)
        dimensionLayout.add_widget(self.dimensions)
        main_layout.add_widget(dimensionLayout)
        quantityLayout.add_widget(quantityLabel)
        quantityLayout.add_widget(self.quantity)
        main_layout.add_widget(quantityLayout)
        productionLayout.add_widget(productionLabel)
        productionLayout.add_widget(self.production)
        main_layout.add_widget(productionLayout)
        buttonBox = BoxLayout(orientation="horizontal", padding = [0, 5], spacing = 20)
        equalsButton = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=fontSize)
        equalsButton.bind(on_press=self.onButtonClick)
        buttonBox.add_widget(equalsButton)
        zeroButton = Button(text="C", pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=fontSize)
        zeroButton.bind(on_press=self.zeroValues)
        buttonBox.add_widget(zeroButton)
        main_layout.add_widget(buttonBox)
        return main_layout

    def onButtonClick(self, instance):
        length = int(self.length.text)
        dimensions = int(self.dimensions.text)
        quantity = int(self.quantity.text)
        production = int(self.production.text)
        if length and dimensions:
            result = str((length/(dimensions/1000))*production)
            self.quantity.text = result
        elif dimensions and quantity:
            result = str((dimensions*quantity)/production)
            self.length.text = result/1000
        elif length and quantity:
            result = str((length/quantity)*production)
            self.dimensions.text = result*1000
    
    def zeroValues(self, instance):
        self.length.text = "0"
        self.dimensions.text = "0"
        self.quantity.text = "0"
        self.production.text = "1"

if __name__ == "__main__":
    app = MainApp()
    app.run()