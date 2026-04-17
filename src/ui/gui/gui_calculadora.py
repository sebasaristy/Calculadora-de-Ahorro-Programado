import sys
sys.path.append("src")


from core.logica import (
    AhorroProgramado,
    ErrorMetaInvalida,
    ErrorPlazoInvalido,
    ErrorAbonoInvalido,
    ErrorAbonoSuperaMeta,
    ErrorMesExtraFueraDeRango
)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class CalculadoraAhorroGUI(App):
    def build(self):
        layout = GridLayout(cols=2, spacing = 10, padding = 10)

        self.layout = layout
        self.title = "Calculadora de Ahorro Programado"
        
        self.layout.add_widget(Label(text="Meta de ahorro:"))
        self.meta_input = TextInput(hint_text="Meta de ahorro")
        self.layout.add_widget(self.meta_input)
        
        self.layout.add_widget(Label(text="Plazo en meses:"))
        self.plazo_input = TextInput(hint_text="Plazo en meses")
        self.layout.add_widget(self.plazo_input)

        self.layout.add_widget(Label(text="Abono extra:"))
        self.abono_input = TextInput(hint_text="Abono extra (0 si no hay)")
        self.layout.add_widget(self.abono_input)

        self.layout.add_widget(Label(text="Mes de abono extra:"))
        self.mes_abono_input = TextInput(hint_text="Mes de abono extra (0 si no hay)")
        self.layout.add_widget(self.mes_abono_input)

        self.resultado1_label = Label(text="Ahorro mensual necesario:")
        self.layout.add_widget(self.resultado1_label)

        self.resultado_label = Label(text="")
        self.layout.add_widget(self.resultado_label)

        boton = Button(text="Calcular Ahorro")
        boton.bind(on_press=self.calcular_ahorro)
        self.layout.add_widget(boton)

        self.informacion_label = Label(text="Esta aplicacion permite que el usuario calcule\n el ahorro mensual necesario para alcanzar la meta\n de ahorro deseada en el plazo establecido, teniendo\n en cuenta un abono extra opcional")
        self.layout.add_widget(self.informacion_label)

        return layout
    
    def calcular_ahorro(self, sender):
        try:
            meta = float(self.meta_input.text)
            plazo = int(self.plazo_input.text)
            abono_extra = float(self.abono_input.text)
            mes_abono = int(self.mes_abono_input.text)

            ahorro = AhorroProgramado(meta=meta, plazo=plazo, abono_extra=abono_extra, mes_abono_extra=mes_abono)
            resultado = ahorro.calcular_cuota_mensual()

            self.resultado_label.text = f"{resultado}"
        except ValueError:
            self.resultado_label.text = "Error: Por favor, ingrese valores numéricos válidos."
        except (ErrorMetaInvalida, ErrorPlazoInvalido, ErrorAbonoInvalido, ErrorAbonoSuperaMeta, ErrorMesExtraFueraDeRango) as e:
            self.resultado_label.text = f"Error: {str(e)}"

if __name__ == "__main__":
    CalculadoraAhorroGUI().run()