import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

class KisanMitraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KisanMitra")
        self.root.geometry("600x400")
        self.root.configure(bg="#E8F5E9")

        # Title
        self.title_label = tk.Label(
            root, text="KisanMitra", font=("Arial", 24, "bold"), fg="#2E7D32", bg="#E8F5E9"
        )
        self.title_label.pack(pady=20)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg="#E8F5E9")
        self.button_frame.pack(pady=10)

        # Buttons
        self.weather_button = tk.Button(
            self.button_frame, text="Weather", font=("Arial", 14), bg="#FFCA28", fg="black",
            command=self.fetch_weather_advice
        )
        self.weather_button.grid(row=0, column=0, padx=10, pady=10)

        self.soil_button = tk.Button(
            self.button_frame, text="Soil", font=("Arial", 14), bg="#FFCA28", fg="black",
            command=self.fetch_soil_advice
        )
        self.soil_button.grid(row=0, column=1, padx=10, pady=10)

        self.crop_button = tk.Button(
            self.button_frame, text="Crop", font=("Arial", 14), bg="#FFCA28", fg="black",
            command=self.fetch_crop_advice
        )
        self.crop_button.grid(row=1, column=0, padx=10, pady=10)

        self.pest_button = tk.Button(
            self.button_frame, text="Pest", font=("Arial", 14), bg="#FFCA28", fg="black",
            command=self.fetch_pest_advice
        )
        self.pest_button.grid(row=1, column=1, padx=10, pady=10)

        # Result Area
        self.result_text = tk.Text(
            root, height=8, width=50, font=("Arial", 12), bg="#C8E6C9", fg="#1B5E20", wrap=tk.WORD
        )
        self.result_text.pack(pady=20, padx=20)
        self.result_text.insert(tk.END, "Click a button to get advice")
        self.result_text.config(state='disabled')

        # Base URL for backend (Updated to 127.0.0.1)
        self.base_url = "http://127.0.0.1:5000"

    def update_result(self, text):
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)
        self.result_text.config(state='disabled')

    def fetch_weather_advice(self):
        try:
            response = requests.get(f"{self.base_url}/weather")
            data = response.json()
            advice = data.get("advice", data.get("error", "Error fetching weather advice"))
            self.update_result(advice)
        except Exception as e:
            self.update_result(f"Error: {str(e)}")

    def fetch_soil_advice(self):
        try:
            payload = {"crop": "Tomato"}
            response = requests.post(f"{self.base_url}/soil", json=payload)
            data = response.json()
            advice = data.get("advice", data.get("error", "Error fetching soil advice"))
            self.update_result(advice)
        except Exception as e:
            self.update_result(f"Error: {str(e)}")

    def fetch_crop_advice(self):
        try:
            payload = {"land_size": "2 acres"}
            response = requests.post(f"{self.base_url}/crop", json=payload)
            data = response.json()
            advice = data.get("advice", data.get("error", "Error fetching crop advice"))
            self.update_result(advice)
        except Exception as e:
            self.update_result(f"Error: {str(e)}")

    def fetch_pest_advice(self):
        try:
            payload = {"pest_desc": "Small insects"}
            response = requests.post(f"{self.base_url}/pest", json=payload)
            data = response.json()
            advice = data.get("advice", data.get("error", "Error fetching pest advice"))
            self.update_result(advice)
        except Exception as e:
            self.update_result(f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KisanMitraApp(root)
    root.mainloop()