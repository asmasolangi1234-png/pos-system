import tkinter as tk 
from PIL import Image, ImageTk
from datetime import datetime
import random

window = tk.Tk()

window.title("Drinkster POS")
window.geometry("1200x700")
window.configure(bg="#d9c7a7")
left_frame = tk.Frame(window, bg="#d9c7a7")
left_frame.pack(side="left", padx=20, pady=20)

right_frame = tk.Frame(window, bg="#d9c7a7")
right_frame.pack(side="right", padx=20, pady=20)

menu_frame = tk.Frame(left_frame, bg="#d9c7a7")
menu_frame.pack()



title = tk.Label(
    window,
    text="DRINKSTER CAFE",
    font=("Arial", 22, "bold"),
    bg="#d9c7a7",
    fg="#3b2f2f"
)
tagline = tk.Label(
    window,
    text="Coffee • Tea • Cold Drinks",
    font=("Arial", 12),
    bg="#d9c7a7",
    fg="#5c4033"
)

tagline.pack()

title.pack(pady=20)



name_label = tk.Label(
    right_frame,
    text="Customer Name",
    bg="#d9c7a7",
    font=("Arial", 12, "bold")
)



name_entry = tk.Entry(right_frame, width=30)

name_label.pack()
name_entry.pack(pady=5)
quantity_label = tk.Label(
    right_frame,
    text="Quantity",
    bg="#d9c7a7",
    font=("Arial", 12, "bold")
)

quantity_label.pack()

quantity_entry = tk.Entry(right_frame, width=10)
quantity_entry.pack(pady=5)

quantity_entry.insert(0, "1")
discount_label = tk.Label(
    right_frame,
    text="Discount %",
    bg="#d9c7a7",
    font=("Arial", 12, "bold")
)

discount_label.pack()

discount_entry = tk.Entry(right_frame, width=10)
discount_entry.pack(pady=5)

discount_entry.insert(0, "0")
cash_label = tk.Label(
    right_frame,
    text="Cash Received",
    bg="#d9c7a7",
    font=("Arial", 12, "bold")
)

cash_label.pack()

cash_entry = tk.Entry(right_frame, width=10)
cash_entry.pack(pady=5)

cash_entry.insert(0, "0")


bill_text = tk.Text(
    right_frame,
    height=18,
    width=35,
    bg="#fff8ee",
    font=("Courier New", 11)
)

bill_label = tk.Label(
    right_frame,
    text="Customer Bill",
    font=("Arial", 14, "bold"),
    bg="#d9c7a7"
)

bill_label.pack()
bill_text.pack()

americano_img = Image.open("americano.jpg")
americano_img = americano_img.resize((40, 40))

americano_photo = ImageTk.PhotoImage(americano_img)
tea_img = Image.open("tea.png")
tea_img = tea_img.resize((40, 40))

tea_photo = ImageTk.PhotoImage(tea_img)

cappuccino_img = Image.open("CAPP.jfif")
cappuccino_img = cappuccino_img.resize((40, 40))

cappuccino_photo = ImageTk.PhotoImage(cappuccino_img)

latte_img = Image.open("LATTE.jfif")
latte_img = latte_img.resize((40, 40))

latte_photo = ImageTk.PhotoImage(latte_img)

logo_img = Image.open("LOGO.jfif")
logo_img = logo_img.resize((120, 120))

logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(window, image=logo_photo, bg="#d9c7a7")
logo_label.pack(pady=10)



total = 0
items = []
daily_sales = 0


def add_latte():
    global total

    qty = int(quantity_entry.get())

    price = 600 * qty

    total += price

    bill_text.insert(tk.END, f"Latte x{qty} - {price}\n")
    items.append(("Latte", qty, price))

    discount = float(discount_entry.get())
    final_total = total - (total * discount / 100)
    total_label.config(text=f"Total: {final_total}")
    cash = float(cash_entry.get())
    change = cash - final_total
    return_label.config(text=f"Return: {change}")


def add_cappuccino():
    global total

    qty = int(quantity_entry.get())

    price = 700 * qty

    total += price

    bill_text.insert(tk.END, f"Cappuccino x{qty} - {price}\n")
    items.append(("Cappuccino", qty, price))

    discount = float(discount_entry.get())
    final_total = total - (total * discount / 100)
    total_label.config(text=f"Total: {final_total}")
    cash = float(cash_entry.get())
    change = cash - final_total
    return_label.config(text=f"Return: {change}")

def add_tea():
    global total

    qty = int(quantity_entry.get())

    price = 300 * qty

    total += price

    bill_text.insert(tk.END, f"Tea x{qty} - {price}\n")
    items.append(("Tea", qty, price))

    discount = float(discount_entry.get())
    final_total = total - (total * discount / 100)
    total_label.config(text=f"Total: {final_total}")
    cash = float(cash_entry.get())
    change = cash - final_total
    return_label.config(text=f"Return: {change}")

def add_americano():
    global total

    qty = int(quantity_entry.get())

    price = 500 * qty

    total += price

    bill_text.insert(tk.END, f"Americano x{qty} - {price}\n")
    items.append(("Americano", qty, price))


    discount = float(discount_entry.get())
    final_total = total - (total * discount / 100)
    total_label.config(text=f"Total: {final_total}")
    cash = float(cash_entry.get())
    change = cash - final_total
    return_label.config(text=f"Return: {change}")
    
def remove_last_item():
    global total

    if len(items) > 0:

        last_item = items.pop()

        total -= last_item[2]

        bill_text.delete(1.0, tk.END)

        for item in items:
            bill_text.insert(
                tk.END,
                f"{item[0]} x{item[1]} - {item[2]}\n"
            )

        total_label.config(text=f"Total: {total}")
def clear_bill():
    global total, items

    total = 0
    items.clear()

    bill_text.delete(1.0, tk.END)
    total_label.config(text="Total: 0")

def generate_receipt():
    global daily_sales, total

    customer = name_entry.get()
    now = datetime.now()
    date_time = now.strftime("%d-%m-%Y  %H:%M:%S")

    receipt = "\n===== DRINKSTER CAFE =====\n"
    receipt += f"Customer: {customer}\n"
    receipt += f"Date: {date_time}\n\n"
    receipt_items = ""

    for item in items:
        name = item[0]
        qty = item[1]
        total_price = item[2]

        unit_price = total_price // qty

        receipt_items += f"{name} x{qty} × {unit_price} = {total_price}\n"

    receipt += receipt_items
    discount = float(discount_entry.get())

    final_total = total - (total * discount / 100)

    receipt += f"\nSubtotal = {total}"
    receipt += f"\nDiscount = {discount}%"
    receipt += f"\nFinal Total = {final_total}"
    cash = float(cash_entry.get())
    change = cash - final_total
    receipt += f"\nCash Received = {cash}"
    receipt += f"\nReturn = {change}"

    receipt_window = tk.Toplevel(window)
    receipt_window.title("Receipt")

    receipt_text = tk.Text(receipt_window, width=40, height=20)
    receipt_text.pack()
    receipt_text.insert(tk.END, receipt)

    receipt_number = random.randint(1000, 9999)
    with open(f"receipt_{receipt_number}.txt", "w") as file:
        file.write(receipt)

    daily_sales += total
    sales_label.config(text=f"Today's Sales: Rs. {daily_sales}")


coffee_label = tk.Label(
    left_frame,
    text="COFFEE",
    font=("Arial", 14, "bold"),
    bg="#d9c7a7",
    fg="#3b2f2f"
)

coffee_label.pack(pady=5)

latte_button = tk.Button(menu_frame,
    text=" Latte",
    image=latte_photo,
    compound="left",
    width=220,
    height=50,
    bg="#6f4e37",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    command=add_latte
)
latte_button.grid(row=0, column=0, padx=10, pady=10)

cappuccino_button = tk.Button(menu_frame,
    text=" Cappuccino",
    image=cappuccino_photo,
    compound="left",
    width=220,
    height=50,
    bg="#6f4e37",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    command=add_cappuccino
)
cappuccino_button.grid(row=0, column=1, padx=10, pady=10)

tea_label = tk.Label(
    left_frame,
    text="TEA",
    font=("Arial", 14, "bold"),
    bg="#d9c7a7",
    fg="#3b2f2f"
)

tea_label.pack(pady=5)

tea_button = tk.Button(
    menu_frame,
    text=" Tea",
    image=tea_photo,
    compound="left",
    width=220,
    height=50,
    bg="#8b5a2b",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    command=add_tea
)

tea_button.grid(row=1, column=0, padx=10, pady=10)

americano_button = tk.Button(
    menu_frame,
    text=" Americano",
    image=americano_photo,
    compound="left",
    width=220,
    height=50,
    bg="#5c4033",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    command=add_americano
)
americano_button.grid(row=1, column=1, padx=10, pady=10)


receipt_button = tk.Button(
    window,
    text="Generate Slip",
    width=20,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    command=generate_receipt
)
receipt_button.pack(pady=5)
remove_button = tk.Button(
    window,
    text="Remove Last Item",
    width=20,
    bg="orange",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    command=remove_last_item
)

remove_button.pack(pady=5)

total_label = tk.Label(
    right_frame,
    text="Total: 0",
    font=("Arial", 16, "bold"),
    bg="#d9c7a7",
    fg="green"
)
total_label.pack(pady=10)
sales_label = tk.Label(
    right_frame,
    text="Today's Sales: Rs. 0",
    font=("Arial", 14, "bold"),
    bg="#d9c7a7",
    fg="blue"
)
sales_label.pack(pady=10)
return_label = tk.Label(
    right_frame,
    text="Return: 0",
    font=("Arial", 14, "bold"),
    bg="#d9c7a7",
    fg="purple"
)

return_label.pack(pady=10)



clear_button = tk.Button(
    window,
    text="Clear Bill",
    width=20,
    bg="red",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    command=clear_bill
)
clear_button.pack(pady=5)

window.mainloop()

