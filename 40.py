import tkinter as tk
import requests


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Information")

        self.api_key = "your_actual_api_key"  # Replace with your OpenWeatherMap API key

        self.cities = ["Kabul", "Herat", "Mazar", "Kandahar"]

        # Label for dropdown menu
        self.city_label = tk.Label(root, text="Select a City:")
        self.city_label.pack(pady=5)

        # Dropdown menu for city selection
        self.city_var = tk.StringVar(value=self.cities[0])
        self.city_menu = tk.OptionMenu(root, self.city_var, *self.cities)
        self.city_menu.pack(pady=5)

        # Button to fetch weather info
        self.fetch_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.fetch_button.pack(pady=10)

        # Text area to display results
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack(pady=5)

    def get_weather(self):
        city = self.city_var.get()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']

            weather_info = (f"Weather in {city}:\n"
                            f"Description: {weather_desc}\n"
                            f"Temperature: {temp} °C\n"
                            f"Feels Like: {feels_like} °C\n"
                            f"Humidity: {humidity}%\n")
        else:
            weather_info = f"Error: City '{city}' not found."

        self.result_text.delete(1.0, tk.END)  # Clear the text area
        self.result_text.insert(tk.END, weather_info)


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()