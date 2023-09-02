import tkinter as tk
from forex_python.converter import CurrencyRates

# Define your API key (not needed for forex-python)
API_KEY = ''  # Not used with forex-python

def convert_currency():
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()
    amount = float(amount_entry.get())

    c = CurrencyRates()

    try:
        exchange_rate = c.get_rate(base_currency, target_currency)
        converted_amount = amount * exchange_rate
        result_label.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}", font=("Helvetica", 14, "bold"))
    except Exception as e:
        result_label.config(text=str(e), font=("Helvetica", 14, "bold"))

# Create a Tkinter window
window = tk.Tk()
window.title("Currency Converter")

# Disable maximize button
window.resizable(False, False)

# Label for instructions
instructions_label = tk.Label(window, text="Enter the amount, base currency, and target currency:", font=("Helvetica", 14))
instructions_label.pack()

# Entry for amount
amount_entry = tk.Entry(window, font=("Helvetica", 14))
amount_entry.pack()

# Dropdown for base currency
base_currency_var = tk.StringVar()
base_currency_label = tk.Label(window, text="Base Currency:", font=("Helvetica", 14))
base_currency_label.pack()
base_currency_dropdown = tk.OptionMenu(window, base_currency_var, "USD", "EUR", "GBP", "JPY")
base_currency_dropdown.config(font=("Helvetica", 14))
base_currency_dropdown.pack()

# Dropdown for target currency
target_currency_var = tk.StringVar()
target_currency_label = tk.Label(window, text="Target Currency:", font=("Helvetica", 14))
target_currency_label.pack()
target_currency_dropdown = tk.OptionMenu(window, target_currency_var, "USD", "EUR", "GBP", "JPY")
target_currency_dropdown.config(font=("Helvetica", 14))
target_currency_dropdown.pack()

# Button to perform conversion
convert_button = tk.Button(window, text="Convert", command=convert_currency, font=("Helvetica", 14))
convert_button.pack()

# Label to display result
result_label = tk.Label(window, text="", font=("Helvetica", 14, "bold"))
result_label.pack()

# Run the Tkinter main loop
window.mainloop()
