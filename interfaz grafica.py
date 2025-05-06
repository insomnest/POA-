import tkinter as tk
from tkinter import messagebox

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")
        self.root.configure(bg="#2E4053")  # Fondo oscuro

        # Etiquetas y entradas
        self.label1 = tk.Label(root, text="Número 1:", font=("Arial", 12), fg="white", bg="#2E4053")
        self.label1.pack(pady=5)
        self.num1_entry = tk.Entry(root, font=("Arial", 12))
        self.num1_entry.pack(pady=5)

        self.label2 = tk.Label(root, text="Número 2:", font=("Arial", 12), fg="white", bg="#2E4053")
        self.label2.pack(pady=5)
        self.num2_entry = tk.Entry(root, font=("Arial", 12))
        self.num2_entry.pack(pady=5)

        # Contenedor de botones
        self.botones_frame = tk.Frame(root, bg="#2E4053")
        self.botones_frame.pack(pady=10)

        self.botones = {
            "Suma": ("#58D68D", self.suma),
            "Resta": ("#EC7063", self.resta),
            "Multiplicación": ("#F4D03F", self.multiplicacion),
            "División": ("#5DADE2", self.division)
        }

        for nombre, (color, funcion) in self.botones.items():
            boton = tk.Button(self.botones_frame, text=nombre, font=("Arial", 12), bg=color, fg="black",
                              width=15, height=2, command=funcion)
            boton.pack(pady=5)

        # Botón de salir
        self.salir_boton = tk.Button(root, text="Salir", font=("Arial", 12), bg="#D35400", fg="white",
                                     width=15, height=2, command=root.quit)
        self.salir_boton.pack(pady=10)

    def obtener_valores(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
            return None

    def mostrar_resultado(self, resultado):
        messagebox.showinfo("Resultado", f"El resultado es: {resultado}")

    def suma(self):
        valores = self.obtener_valores()
        if valores:
            self.mostrar_resultado(valores[0] + valores[1])

    def resta(self):
        valores = self.obtener_valores()
        if valores:
            self.mostrar_resultado(valores[0] - valores[1])

    def multiplicacion(self):
        valores = self.obtener_valores()
        if valores:
            self.mostrar_resultado(valores[0] * valores[1])

    def division(self):
        valores = self.obtener_valores()
        if valores:
            if valores[1] == 0:
                messagebox.showerror("Error", "División por cero no permitida.")
            else:
                self.mostrar_resultado(valores[0] / valores[1])

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
