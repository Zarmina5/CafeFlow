import tkinter as tk
from tkinter import messagebox

class CafeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("850x550")
        self.root.configure(bg="#2c3e50")

        # Title Label
        title_label = tk.Label(self.root, text="☕ Welcome to the Cafe ☕", font=("Helvetica", 32, "bold"), bg="#2c3e50", fg="#ecf0f1")
        title_label.pack(pady=15)

        # Menu Items and Prices
        self.menu = {
            "Coffee": 50,
            "Tea": 30,
            "Sandwich": 100,
            "Burger": 150,
            "Pizza": 300,
            "Fries": 80,
            "Cold Drink": 40,
            "Cake": 120
        }

        # Variables to store quantities entered by the user
        self.item_vars = {}
        for item in self.menu:
            self.item_vars[item] = tk.StringVar(value="0")

        # Main Container Frame
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # --- Menu Frame (Left Side) ---
        menu_frame = tk.LabelFrame(main_frame, text="Menu", font=("Helvetica", 16, "bold"), bg="#34495e", fg="#ecf0f1", padx=20, pady=20)
        menu_frame.pack(side="left", fill="both", expand=True, padx=10)

        # Headers for Menu
        tk.Label(menu_frame, text="Item Name", font=("Helvetica", 14, "bold"), bg="#34495e", fg="#f1c40f").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(menu_frame, text="Price", font=("Helvetica", 14, "bold"), bg="#34495e", fg="#f1c40f").grid(row=0, column=1, padx=10, pady=5, sticky="w")
        tk.Label(menu_frame, text="Quantity", font=("Helvetica", 14, "bold"), bg="#34495e", fg="#f1c40f").grid(row=0, column=2, padx=10, pady=5, sticky="w")
        
        # Populate Menu Items dynamically
        row = 1
        for item, price in self.menu.items():
            tk.Label(menu_frame, text=item, font=("Helvetica", 12), bg="#34495e", fg="#ecf0f1").grid(row=row, column=0, padx=10, pady=5, sticky="w")
            tk.Label(menu_frame, text=f"Rs. {price}", font=("Helvetica", 12), bg="#34495e", fg="#ecf0f1").grid(row=row, column=1, padx=10, pady=5, sticky="w")
            
            # Entry for Quantity
            entry = tk.Entry(menu_frame, textvariable=self.item_vars[item], font=("Helvetica", 12), width=5, justify="center")
            entry.grid(row=row, column=2, padx=10, pady=5)
            row += 1

        # Buttons Frame (Inside Menu Frame at the bottom)
        btn_frame = tk.Frame(menu_frame, bg="#34495e")
        btn_frame.grid(row=row, column=0, columnspan=3, pady=25)

        generate_btn = tk.Button(btn_frame, text="Generate Bill", font=("Helvetica", 12, "bold"), bg="#27ae60", fg="white", width=12, command=self.generate_bill)
        generate_btn.grid(row=0, column=0, padx=10)

        clear_btn = tk.Button(btn_frame, text="Clear", font=("Helvetica", 12, "bold"), bg="#f39c12", fg="white", width=12, command=self.clear_all)
        clear_btn.grid(row=0, column=1, padx=10)

        exit_btn = tk.Button(btn_frame, text="Exit", font=("Helvetica", 12, "bold"), bg="#c0392b", fg="white", width=12, command=self.root.quit)
        exit_btn.grid(row=0, column=2, padx=10)

        # --- Receipt/Bill Frame (Right Side) ---
        bill_frame = tk.LabelFrame(main_frame, text="Receipt", font=("Helvetica", 16, "bold"), bg="#34495e", fg="#ecf0f1", padx=10, pady=10)
        bill_frame.pack(side="right", fill="both", expand=True, padx=10)

        # Text Area to Display the Bill
        self.receipt_text = tk.Text(bill_frame, font=("Courier", 12), width=35, height=20)
        self.receipt_text.pack(fill="both", expand=True)
        self.welcome_receipt()

    def welcome_receipt(self):
        """Clears the receipt area and prints the header."""
        self.receipt_text.delete('1.0', tk.END)
        self.receipt_text.insert(tk.END, "\t  CAFE RECEIPT\n")
        self.receipt_text.insert(tk.END, "-"*35 + "\n")
        self.receipt_text.insert(tk.END, " Item\t\tQty\tPrice\n")
        self.receipt_text.insert(tk.END, "-"*35 + "\n")

    def generate_bill(self):
        """Calculates the total and prints the ordered items."""
        self.welcome_receipt()
        total_price = 0
        ordered_items = 0

        for item, price in self.menu.items():
            qty_str = self.item_vars[item].get()
            
            # Basic validation
            if not qty_str.isdigit():
                continue
                
            qty = int(qty_str)
                
            if qty > 0:
                ordered_items += 1
                item_total = price * qty
                total_price += item_total
                
                # Format item name to fit alignment
                item_name = item[:10] + ".." if len(item) > 12 else item
                self.receipt_text.insert(tk.END, f" {item_name.ljust(15)}{qty}\tRs.{item_total}\n")

        if ordered_items == 0:
            messagebox.showwarning("Warning", "Please select at least one item by entering a quantity!")
            self.welcome_receipt()
            return

        self.receipt_text.insert(tk.END, "-"*35 + "\n")
        self.receipt_text.insert(tk.END, f" TOTAL AMOUNT:\t\tRs.{total_price}\n")
        self.receipt_text.insert(tk.END, "-"*35 + "\n")
        self.receipt_text.insert(tk.END, "\tThank you! Visit Again\n")

    def clear_all(self):
        """Resets all quantities to 0 and clears the bill."""
        for item in self.menu:
            self.item_vars[item].set("0")
        self.welcome_receipt()

if __name__ == "__main__":
    root = tk.Tk()
    app = CafeManagementSystem(root)
    root.mainloop()
