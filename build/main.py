from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super(MyTextInput, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.text = ""
        return super(MyTextInput, self).on_touch_down(touch)
    
    def on_focus(self, instance, value):
        if not value and self.text == "":
            self.text = "0"

class MainApp(App):
    def build(self):
        fontSize = 80
        numberFontSize = 100
        main_layout = BoxLayout(orientation="vertical", padding=[50, 5])
        lengthLayout = BoxLayout(orientation="horizontal", padding = [0, 5], spacing = 20)
        lengthLabel = Label(text="Dĺžka (m)", font_size=fontSize, halign="left")
        self.length = MyTextInput(text="0", multiline=False, readonly=False, halign="right", font_size=numberFontSize)
        self.length.bind(on_touch_down=self.emptyText)
        dimensionLayout = BoxLayout(orientation="horizontal", padding = [0, 5], spacing = 20)
        dimensionsLabel = Label(text="Výška (mm)", font_size=fontSize, halign="left")
        self.dimensions = MyTextInput(text="0", multiline=False, readonly=False, halign="right", font_size=numberFontSize)
        quantityLayout = BoxLayout(orientation="horizontal", padding = [0, 5], spacing = 20)
        quantityLabel = Label(text="Počet etikiet", font_size=fontSize, halign="left")
        self.quantity = MyTextInput(text="0", multiline=False, readonly=False, halign="right", font_size=numberFontSize)
        productionLayout = BoxLayout(orientation="horizontal", padding = [0, 5], spacing = 20)
        productionLabel = Label(text="Produkcia", font_size=fontSize, halign="left")
        self.production = MyTextInput(text="1", multiline=False, readonly=False, halign="right", font_size=numberFontSize)
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
        if self.length.text != "" and self.dimensions.text != "" and self.quantity.text != "" and self.production .text != "":
            length = float(self.length.text)
            dimensions = float(self.dimensions.text)
            quantity = float(self.quantity.text)
            production = float(self.production.text)
            if production == 0:
                production = 1
                self.production.text = "1"
            if length and dimensions:
                result = (length/(dimensions/1000))*production
                self.quantity.text = str(round(result,2))
            elif dimensions and quantity:
                result = (dimensions*quantity)/production
                self.length.text = str(round(result/1000, 2))
            elif length and quantity:
                result = (length/quantity)*production
                self.dimensions.text = str(round(result*1000, 2))

    def emptyText(self, instance, text):
        text = ""

    def zeroValues(self, instance):
        self.length.text = "0"
        self.dimensions.text = "0"
        self.quantity.text = "0"
        self.production.text = "1"

if __name__ == "__main__":
    app = MainApp()
    app.run()