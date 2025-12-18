
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
from datetime import datetime
import os

class ProductManager:
    def __init__(self, db_manager):
        self._db_manager = db_manager  # PRIVATE: Internal database manager

    def fetch_all_products(self):
        try:
            connection = self._db_manager.get_connection()
            cursor = connection.cursor()
            query = """
                SELECT product_id, name, description, price, category, stock_quantity, image_url
                FROM Products
                ORDER BY category, name
            """
            cursor.execute(query)
            products = []

            for row in cursor.fetchall():
                products.append({
                    'product_id': row[0],
                    'name': row[1],
                    'description': row[2],
                    'price': float(row[3]),
                    'category': row[4],
                    'stock': row[5],
                    'image_url': row[6] if row[6] else None
                })

            cursor.close()
            return products
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to fetch products:\n{e}")
            return []

    def get_current_stock(self, product_id):
        try:
            connection = self._db_manager.get_connection()
            cursor = connection.cursor()
            query = "SELECT stock_quantity FROM Products WHERE product_id = %s"
            cursor.execute(query, (product_id,))
            result = cursor.fetchone()
            cursor.close()
            return result[0] if result else 0
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to get stock:\n{e}")
            return 0

    def update_stock(self, product_id, quantity_sold):
        try:
            connection = self._db_manager.get_connection()
            cursor = connection.cursor()
            query = """
                UPDATE Products
                SET stock_quantity = stock_quantity - %s
                WHERE product_id = %s
            """
            cursor.execute(query, (quantity_sold, product_id))
            connection.commit()
            cursor.close()
        except mysql.connector.Error as e:
            raise Exception(f"Failed to update stock: {e}")

class OrderManager:
    def __init__(self, db_manager, product_manager):
        self._db_manager = db_manager
        self._product_manager = product_manager

    def create_order(self, customer_id, total_amount, cart_items):
        try:
            connection = self._db_manager.get_connection()
            cursor = connection.cursor()
            order_query = """
                INSERT INTO Orders (customer_id, total_amount, status)
                VALUES (%s, %s, 'Completed')
            """
            cursor.execute(order_query, (customer_id, total_amount))
            order_id = cursor.lastrowid

            for item in cart_items:
                product = item['product']
                quantity = item['quantity']

                item_query = """
                    INSERT INTO Order_Items (order_id, product_id, quantity, price)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(item_query, (order_id, product['product_id'], quantity, product['price']))

                self._product_manager.update_stock(product['product_id'], quantity)

            connection.commit()
            cursor.close()
            return order_id

        except mysql.connector.Error as e:
            connection.rollback()
            messagebox.showerror("Database Error", f"Failed to create order:\n{e}")
            return None
class ShoppingCart:
    def __init__(self, product_manager):
        self._cart_items = []
        self._product_manager = product_manager

    def add_item(self, product, quantity):
        # Validate current stock
        current_stock = self._product_manager.get_current_stock(product['product_id'])
        product['stock'] = current_stock

        if quantity > current_stock:
            messagebox.showerror("Error", f"Only {current_stock} items available!")
            return False

        # Check if product already in cart
        for item in self._cart_items:
            if item['product']['product_id'] == product['product_id']:
                if item['quantity'] + quantity > current_stock:
                    messagebox.showerror("Error", f"Only {current_stock} items available!")
                    return False
                item['quantity'] += quantity
                return True

        # Add new item to cart
        self._cart_items.append({'product': product, 'quantity': quantity})
        return True

    def get_items(self):
        return self._cart_items.copy()

    def get_total(self):
        return sum(item['product']['price'] * item['quantity'] for item in self._cart_items)

    def clear(self):
        self._cart_items = []

    def is_empty(self):
        return len(self._cart_items) == 0

    def remove_item(self, item_index):
        if 0 <= item_index < len(self._cart_items):
            self._cart_items.pop(item_index)
            return True
        return False

class ImageLoader:
    def __init__(self):
        self._image_cache = []  # PRIVATE: Cache to prevent garbage collection
        self._bread_folder = self._get_bread_folder_path()

    def _get_bread_folder_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, "BREAD FOLDER")

    def load_product_image(self, product_name, size=(90, 90)):
        try:
            print(f"\n--- Loading image for: {product_name} ---")

            # Generate possible filenames
            possible_files = [
                f"{product_name}.jpg",
                f"{product_name}.png",
                f"{product_name.replace(' ', '-')}.jpg",
            ]

            for filename in possible_files:
                image_path = os.path.join(self._bread_folder, filename)

                if os.path.exists(image_path):
                    print(f"✓✓✓ FOUND: {filename}")

                    # Load and resize image
                    from PIL import Image as PILImage
                    pil_img = PILImage.open(image_path)
                    pil_img = pil_img.resize(size, PILImage.LANCZOS)
                    tk_img = ImageTk.PhotoImage(pil_img)

                    # Cache to prevent garbage collection
                    self._image_cache.append(tk_img)

                    print(f"✓✓✓ IMAGE LOADED!")
                    return tk_img

            print(f"✗✗✗ NO IMAGE FOUND for {product_name}")
            return None

        except Exception as e:
            print(f"✗✗✗ EXCEPTION: {str(e)}")
            return None

class CustomerAddressManager:
    def __init__(self, db_manager, customer_session):
        self._db_manager = db_manager
        self._customer_session = customer_session

    def update_address(self, address):
        try:
            connection = self._db_manager.get_connection()
            cursor = connection.cursor()

            customer_id = self._customer_session.get_customer_id()

            query = "UPDATE Customers SET address = %s WHERE customer_id = %s"
            cursor.execute(query, (address, customer_id))
            connection.commit()
            cursor.close()

            # Update session
            self._customer_session.set_address(address)

            return True

        except Exception as e:
            print(f"Error updating address: {e}")
            messagebox.showerror("Error", f"Failed to update address: {e}")
            return False

class UIComponentFactory:
    # CLASS CONSTANTS: UI color scheme
    COLOR_HEADER_BG = "#D4A574"
    COLOR_HEADER_SHADOW = "#B8935E"
    COLOR_BG_MAIN = "#F5E6D3"
    COLOR_BG_CARD = "#FFF8E7"
    COLOR_BG_CART = "#FFF8E7"
    COLOR_TEXT_PRIMARY = "#3E2723"
    COLOR_TEXT_SECONDARY = "#5D4037"
    COLOR_ACCENT = "#D4A574"
    COLOR_BTN_GREEN = "#6B8E23"
    COLOR_BTN_GREEN_HOVER = "#5A7A1F"
    COLOR_BTN_RED = "#C0504D"
    COLOR_BTN_RED_HOVER = "#A04340"

    @staticmethod
    def create_header_frame(parent):
        header_frame = Frame(parent, bg=UIComponentFactory.COLOR_HEADER_BG,
                             height=100, bd=0)
        header_frame.pack(fill=X, pady=0)
        header_frame.pack_propagate(False)

        # Shadow effect
        shadow = Frame(parent, bg=UIComponentFactory.COLOR_HEADER_SHADOW,
                       height=3, bd=0)
        shadow.pack(fill=X)

        return header_frame

    @staticmethod
    def create_styled_button(parent, text, command, color_scheme="green"):
        colors = {
            "green": (UIComponentFactory.COLOR_BTN_GREEN, UIComponentFactory.COLOR_BTN_GREEN_HOVER),
            "red": (UIComponentFactory.COLOR_BTN_RED, UIComponentFactory.COLOR_BTN_RED_HOVER),
            "gray": ("#95A5A6", "#7F8C8D")
        }

        bg_color, hover_color = colors.get(color_scheme, colors["green"])

        btn = Button(parent,
                     text=text,
                     font=("Segoe UI", 12, "bold"),
                     fg="#FFFFFF",
                     bg=bg_color,
                     activebackground=hover_color,
                     activeforeground="#FFFFFF",
                     bd=0,
                     relief="flat",
                     cursor="hand2",
                     command=command)

        # Add hover effects
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))

        return btn
class BakeryMenu:
    def __init__(self, app_controller):
        # INJECT DEPENDENCIES
        self.app_controller = app_controller
        self._db_manager = app_controller.get_db_manager()
        self._customer_session = app_controller.get_customer_session()

        # INITIALIZE SUBSYSTEMS (Composition over Inheritance)
        self._product_manager = ProductManager(self._db_manager)
        self._order_manager = OrderManager(self._db_manager, self._product_manager)
        self._shopping_cart = ShoppingCart(self._product_manager)
        self._image_loader = ImageLoader()
        self._address_manager = CustomerAddressManager(self._db_manager, self._customer_session)
        self._ui_factory = UIComponentFactory()

        # UI REFERENCES
        self._root = None
        self._cart_text = None
        self._total_label = None
        self._products = []

        # Initialize UI
        self._initialize_window()
        self._check_database_connection()
        self._load_products()
        self._create_ui()

        # Start main loop
        self._root.mainloop()

    def _initialize_window(self):
        self._root = Tk()
        self._root.title("WeirDoughs Bakery - Menu")
        self._root.state('zoomed')
        self._root.resizable(True, True)
        self._root.config(bg=UIComponentFactory.COLOR_BG_MAIN)

        # Set icon
        try:
            logo_path = r"no bg llogo.png"
            if os.path.exists(logo_path):
                logo = PhotoImage(file=logo_path)
                self._root.iconphoto(False, logo)
        except Exception as e:
            print(f"Could not load icon: {e}")

        # Handle window close
        self._root.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _check_database_connection(self):
        if not self._db_manager.is_connected():
            messagebox.showerror("Error", "Database connection lost!")
            self._root.destroy()
            raise Exception("Database not connected")

    def _load_products(self):
        self._products = self._product_manager.fetch_all_products()

        if not self._products:
            messagebox.showwarning("Warning", "No products found in database!")

        print(f"\n=== LOADED {len(self._products)} PRODUCTS ===")

    def _on_closing(self):
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
            self.app_controller.close_application()
            self._root.destroy()

    def _create_ui(self):
        self._create_header()
        self._create_main_container()

    def _create_header(self):
        header_frame = self._ui_factory.create_header_frame(self._root)
        header_content = Frame(header_frame, bg=UIComponentFactory.COLOR_HEADER_BG)
        header_content.pack(expand=True, fill=BOTH)

        # Title
        Label(header_content,
              text="WEIRDOUGHS BAKERY",
              font=("Segoe UI", 28, "bold"),
              fg=UIComponentFactory.COLOR_TEXT_PRIMARY,
              bg=UIComponentFactory.COLOR_HEADER_BG).pack(side=LEFT, padx=40, pady=20)

        # Welcome message
        customer_name = self._customer_session.get_name()
        Label(header_content,
              text=f"Welcome, {customer_name}!",
              font=("Segoe UI", 13, "bold"),
              fg=UIComponentFactory.COLOR_TEXT_SECONDARY,
              bg=UIComponentFactory.COLOR_HEADER_BG).pack(side=LEFT, padx=200)

        #Exit button - SMALLER SIZE
        exit_btn = self._ui_factory.create_styled_button(
            header_content, "Exit", self._on_closing, "red"
        )
        exit_btn.pack(side=RIGHT, padx=100, pady=0, ipadx=15, ipady=3)

    def _create_main_container(self):
        main_container = Frame(self._root, bg=UIComponentFactory.COLOR_BG_MAIN)
        main_container.pack(fill=BOTH, expand=True, padx=0, pady=5)

        # Create products section
        self._create_products_section(main_container)

        # Create cart section
        self._create_cart_section(main_container)

    def _create_products_section(self, parent):
        products_container = Frame(parent, bg=UIComponentFactory.COLOR_BG_MAIN)
        products_container.pack(side=LEFT, fill=BOTH, expand=True)

        # FIXED EQUAL WIDTH for both columns - 600px each
        column_width = 600

        # Create left column (Breads) with FIXED WIDTH
        left_container = Frame(products_container, bg=UIComponentFactory.COLOR_BG_MAIN, width=column_width)
        left_container.pack(side=LEFT, fill=Y)
        left_container.pack_propagate(False)
        left_frame = self._create_product_column(left_container, "Breads", "left")

        # Add vertical border separator between columns - THICKER
        separator = Frame(products_container, bg="#B8935E", width=6)
        separator.pack(side=LEFT, fill=Y, padx=10)

        # Create right column (Cakes) with FIXED WIDTH
        right_container = Frame(products_container, bg=UIComponentFactory.COLOR_BG_MAIN, width=column_width)
        right_container.pack(side=LEFT, fill=Y)
        right_container.pack_propagate(False)
        right_frame = self._create_product_column(right_container, "Cakes", "right")

        # Populate products
        self._populate_products(left_frame, right_frame)

    def _create_product_column(self, parent, title, side):
        column_frame = Frame(parent, bg=UIComponentFactory.COLOR_BG_MAIN)
        column_frame.pack(fill=BOTH, expand=True)

        # Header
        Label(column_frame,
              text=title,
              font=("Segoe UI", 20, "bold"),
              fg=UIComponentFactory.COLOR_TEXT_PRIMARY,
              bg=UIComponentFactory.COLOR_BG_MAIN,
              anchor="w").pack(fill=X, pady=(0, 10), padx=15)

        # Canvas and scrollbar
        canvas = Canvas(column_frame, bg=UIComponentFactory.COLOR_BG_MAIN,
                        highlightthickness=0)
        scrollbar = Scrollbar(column_frame, orient=VERTICAL, command=canvas.yview,
                              bg=UIComponentFactory.COLOR_BG_MAIN)
        scrollable_frame = Frame(canvas, bg=UIComponentFactory.COLOR_BG_MAIN)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Add padding to scrollable_frame - THIS controls space between content and scrollbar
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack canvas and scrollbar
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y, padx = (0,8))

        # Mouse wheel binding
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", on_mousewheel))
        scrollable_frame.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", on_mousewheel))

        return scrollable_frame

    def _populate_products(self, left_frame, right_frame):
        for idx, product in enumerate(self._products):
            category = product['category'].lower() if product['category'] else 'unknown'

            if 'bread' in category.lower():
                self._create_product_card(left_frame, product)
            elif 'cake' in category.lower():
                self._create_product_card(right_frame, product)
            else:
                self._create_product_card(left_frame, product)

        self._root.update_idletasks()
        print("\n=== FINISHED LOADING UI ===\n")

    def _create_product_card(self, parent, product):
        card_frame = Frame(parent, bg=UIComponentFactory.COLOR_BG_CARD, bd=0, relief=FLAT)
        card_frame.pack(fill=X, padx=10, pady=8)  # Added back padding for spacing

        # Shadow effect
        shadow_frame = Frame(parent, bg="#E0D4C0", bd=0)
        shadow_frame.place(in_=card_frame, relx=0.01, rely=0.01, relwidth=1, relheight=1)
        shadow_frame.lower()

        # Product image
        self._create_product_image(card_frame, product)

        # Product info
        self._create_product_info(card_frame, product)

        # Action buttons
        self._create_product_actions(card_frame, product)

    def _create_product_image(self, parent, product):
        img_canvas = Canvas(parent, bg=UIComponentFactory.COLOR_BG_MAIN,
                            width=90, height=90, bd=0, highlightthickness=0)
        img_canvas.pack(side=LEFT, padx=12, pady=12)

        # Load image
        tk_img = self._image_loader.load_product_image(product['name'])

        if tk_img:
            img_canvas.create_image(45, 45, image=tk_img)
            img_canvas.image = tk_img
        else:
            # Placeholder
            img_canvas.create_rectangle(5, 5, 85, 85, fill="#E0E0E0", outline="#999")
            img_canvas.create_text(45, 45, text="No\nImage",
                                   font=("Arial", 8, "bold"), fill="#666", justify="center")

    def _create_product_info(self, parent, product):
        info_frame = Frame(parent, bg=UIComponentFactory.COLOR_BG_CARD)
        info_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=12, pady=12)

        # Name
        Label(info_frame,
              text=product['name'],
              font=("Segoe UI", 14, "bold"),
              fg=UIComponentFactory.COLOR_TEXT_PRIMARY,
              bg=UIComponentFactory.COLOR_BG_CARD,
              anchor=W).pack(fill=X)

        # Description
        Label(info_frame,
              text=product['description'],
              font=("Segoe UI", 9),
              fg=UIComponentFactory.COLOR_TEXT_SECONDARY,
              bg=UIComponentFactory.COLOR_BG_CARD,
              anchor=W,
              wraplength=400).pack(fill=X, pady=(2, 4))

        # Price
        Label(info_frame,
              text=f"PHP {product['price']:.2f}",
              font=("Segoe UI", 13, "bold"),
              fg=UIComponentFactory.COLOR_ACCENT,
              bg=UIComponentFactory.COLOR_BG_CARD,
              anchor=W).pack(fill=X)

        # Stock
        stock_color = "#6B8E23" if product['stock'] > 10 else "#E67E22" if product['stock'] > 0 else "#C0504D"
        Label(info_frame,
              text=f"Stock: {product['stock']} available",
              font=("Segoe UI", 9, "bold"),
              fg=stock_color,
              bg=UIComponentFactory.COLOR_BG_CARD,
              anchor=W).pack(fill=X)

    def _create_product_actions(self, parent, product):
        action_frame = Frame(parent, bg=UIComponentFactory.COLOR_BG_CARD)
        action_frame.pack(side=RIGHT, padx=16)

        Label(action_frame,
              text="Quantity",
              font=("Segoe UI", 9, "bold"),
              fg=UIComponentFactory.COLOR_TEXT_SECONDARY,
              bg=UIComponentFactory.COLOR_BG_CARD).pack()

        qty_var = IntVar(value=1)
        Spinbox(action_frame,
                from_=1,
                to=max(1, product['stock']),
                textvariable=qty_var,
                width=12,
                font=("Segoe UI", 9),
                bd=2,
                relief="solid",
                buttonbackground=UIComponentFactory.COLOR_BG_MAIN).pack(pady=4)

        add_btn = Button(action_frame,
                         text="Add to Cart",
                         font=("Segoe UI", 10, "bold"),
                         fg="#FFFFFF",
                         bg=UIComponentFactory.COLOR_ACCENT,
                         activebackground="#C89963",
                         activeforeground="#FFFFFF",
                         bd=0,
                         relief="flat",
                         cursor="hand2",
                         command=lambda p=product, q=qty_var: self._add_to_cart(p, q.get()))
        add_btn.pack(pady=4, ipadx=6, ipady=3)
        add_btn.bind("<Enter>", lambda e: e.widget.config(bg="#C89963"))
        add_btn.bind("<Leave>", lambda e: e.widget.config(bg=UIComponentFactory.COLOR_ACCENT))

    def _create_cart_section(self, parent):
        cart_frame = Frame(parent, bg=UIComponentFactory.COLOR_BG_CART,
                           bd=0, relief=FLAT, width=320)
        cart_frame.pack(side=RIGHT, fill=Y, padx=0)
        cart_frame.pack_propagate(False)

        # Shadow
        cart_shadow = Frame(parent, bg="#E0D4C0", width=326)
        cart_shadow.place(in_=cart_frame, relx=0.003, rely=0.003,
                          relwidth=1, relheight=1)
        cart_shadow.lower()

        # Title
        Label(cart_frame,
              text="Shopping Cart",
              font=("Segoe UI", 18, "bold"),
              fg=UIComponentFactory.COLOR_TEXT_PRIMARY,
              bg=UIComponentFactory.COLOR_BG_CART).pack(pady=15)

        # Cart items display
        self._cart_text = Text(cart_frame,
                               height=18,
                               width=35,
                               font=("Segoe UI", 10),
                               bg="#FFFBF0",
                               fg=UIComponentFactory.COLOR_TEXT_PRIMARY,
                               state=DISABLED,
                               bd=0,
                               relief=FLAT,
                               padx=12,
                               pady=8)
        self._cart_text.pack(padx=15, pady=8)

        # Total label
        self._total_label = Label(cart_frame,
                                  text="Total: PHP 0.00",
                                  font=("Segoe UI", 18, "bold"),
                                  fg=UIComponentFactory.COLOR_TEXT_PRIMARY,
                                  bg=UIComponentFactory.COLOR_BG_CART)
        self._total_label.pack(pady=12)

        # Cart buttons
        self._create_cart_buttons(cart_frame)

    def _create_cart_buttons(self, parent):
        button_frame = Frame(parent, bg=UIComponentFactory.COLOR_BG_CART)
        button_frame.pack(pady=8, padx=15, fill=X)

        # Checkout button
        checkout_btn = Button(button_frame,
                              text="Checkout",
                              font=("Segoe UI", 13, "bold"),
                              fg="white",
                              bg= "green",
                              activebackground="#C89963",
                              activeforeground="#FFFFFF",
                              bd=0,
                              relief="flat",
                              cursor="hand2",
                              command=self._checkout)
        checkout_btn.pack(fill=X, pady=3)

        # Clear cart button
        clear_btn = Button(button_frame,
                           text="Clear Cart",
                           font=("Segoe UI", 12, "bold"),
                           fg=UIComponentFactory.COLOR_TEXT_SECONDARY,
                           bg="#E8D5C4",
                           activebackground="#D4C0B0",
                           activeforeground=UIComponentFactory.COLOR_TEXT_SECONDARY,
                           bd=0,
                           relief="flat",
                           cursor="hand2",
                           command=self._clear_cart)
        clear_btn.pack(fill=X, pady=5)
        clear_btn.bind("<Enter>", lambda e: clear_btn.config(bg="#D4C0B0"))
        clear_btn.bind("<Leave>", lambda e: clear_btn.config(bg="#E8D5C4"))

        # Refresh button
        refresh_btn = Button(button_frame,
                             text="Refresh Stock",
                             font=("Segoe UI", 12, "bold"),
                             fg="#FFFFFF",
                             bg="#5B8FA3",
                             activebackground="#4A7589",
                             activeforeground="#FFFFFF",
                             bd=0,
                             relief="flat",
                             cursor="hand2",
                             command=self._refresh_products)
        refresh_btn.pack(fill=X, pady=5)
        refresh_btn.bind("<Enter>", lambda e: refresh_btn.config(bg="#4A7589"))
        refresh_btn.bind("<Leave>", lambda e: refresh_btn.config(bg="#5B8FA3"))

    def _add_to_cart(self, product, quantity):
        if self._shopping_cart.add_item(product, quantity):
            self._update_cart_display()
            messagebox.showinfo("Success", f"Added {quantity} x {product['name']} to cart!")

    def _update_cart_display(self):
        self._cart_text.config(state=NORMAL)
        self._cart_text.delete(1.0, END)

        cart_items = self._shopping_cart.get_items()
        total = self._shopping_cart.get_total()

        for idx, item in enumerate(cart_items):
            product = item['product']
            qty = item['quantity']
            subtotal = product['price'] * qty

            self._cart_text.insert(END, f"{product['name']}\n", "product_name")
            self._cart_text.insert(END, f"  {qty} × PHP {product['price']:.2f}\n", "details")
            self._cart_text.insert(END, f"  Subtotal: PHP {subtotal:.2f} ", "subtotal")

            # Add remove button
            self._cart_text.insert(END, "[Remove]\n\n", f"remove_{idx}")
            self._cart_text.tag_config(f"remove_{idx}", foreground="#C0504D",
                                      font=("Segoe UI", 9, "bold underline"))
            self._cart_text.tag_bind(f"remove_{idx}", "<Button-1>",
                                    lambda e, i=idx: self._remove_cart_item(i))
            self._cart_text.tag_bind(f"remove_{idx}", "<Enter>",
                                    lambda e, tag=f"remove_{idx}": self._cart_text.tag_config(tag, foreground="#A04340"))
            self._cart_text.tag_bind(f"remove_{idx}", "<Leave>",
                                    lambda e, tag=f"remove_{idx}": self._cart_text.tag_config(tag, foreground="#C0504D"))

        self._cart_text.tag_config("product_name", font=("Segoe UI", 11, "bold"),
                                   foreground=UIComponentFactory.COLOR_TEXT_PRIMARY)
        self._cart_text.tag_config("details", font=("Segoe UI", 9),
                                   foreground=UIComponentFactory.COLOR_TEXT_SECONDARY)
        self._cart_text.tag_config("subtotal", font=("Segoe UI", 10, "bold"),
                                   foreground=UIComponentFactory.COLOR_ACCENT)

        self._cart_text.config(state=DISABLED, cursor="arrow")
        self._total_label.config(text=f"Total: PHP {total:.2f}")

    def _clear_cart(self):
        if not self._shopping_cart.is_empty():
            if messagebox.askyesno("Confirm", "Clear all items from cart?"):
                self._shopping_cart.clear()
                self._update_cart_display()

    def _remove_cart_item(self, item_index):
        cart_items = self._shopping_cart.get_items()
        if 0 <= item_index < len(cart_items):
            item = cart_items[item_index]
            product_name = item['product']['name']

            if messagebox.askyesno("Remove Item", f"Remove {product_name} from cart?"):
                # Use proper method to remove item
                if self._shopping_cart.remove_item(item_index):
                    self._update_cart_display()
                    messagebox.showinfo("Removed", f"{product_name} removed from cart!")

    def _refresh_products(self):
        self._load_products()
        messagebox.showinfo("Success", "Product list refreshed!")

        # Rebuild UI
        for widget in self._root.winfo_children():
            widget.destroy()
        self._create_ui()

    def _checkout(self):
        if self._shopping_cart.is_empty():
            messagebox.showwarning("Empty Cart", "Your cart is empty!")
            return

        self._show_address_window()

    def _show_address_window(self):
        """Show address collection window"""
        address_window = Toplevel(self._root)
        address_window.title("Delivery Address")
        address_window.geometry("450x300")
        address_window.config(bg="#FFFFFF")
        address_window.resizable(False, False)
        address_window.grab_set()

        # Center window
        self._center_window(address_window, 450, 300)

        # Title
        Label(address_window,
              text="Delivery Address",
              font=("Segoe UI", 20, "bold"),
              fg=UIComponentFactory.COLOR_TEXT_PRIMARY,
              bg="#FFFFFF").pack(pady=20)

        # Instruction
        Label(address_window,
              text="Please enter your delivery address:",
              font=("Segoe UI", 11),
              fg=UIComponentFactory.COLOR_TEXT_SECONDARY,
              bg="#FFFFFF").pack(pady=5)

        # Address entry
        address_frame = Frame(address_window, bg="#FFFFFF")
        address_frame.pack(pady=15, padx=40)

        address_entry = Text(address_frame,
                             font=("Segoe UI", 11),
                             width=35,
                             height=4,
                             bd=2,
                             relief="solid",
                             wrap=WORD)
        address_entry.pack()
        address_entry.focus_set()

        def proceed_to_payment():
            address = address_entry.get("1.0", END).strip()

            if not address:
                messagebox.showwarning("Address Required",
                                       "Please enter your delivery address!")
                return

            # Update address
            if self._address_manager.update_address(address):
                address_window.destroy()
                self._show_payment_window()

        # Continue button
        continue_btn = self._ui_factory.create_styled_button(
            address_window, "Continue", proceed_to_payment, "green"
        )
        continue_btn.config(font=("Segoe UI", 13, "bold"))
        continue_btn.pack(pady=20, ipadx=40, ipady=12)

    def _show_payment_window(self):
        total = self._shopping_cart.get_total()

        payment_window = Toplevel(self._root)
        payment_window.title("Payment")
        payment_window.geometry("500x450")
        payment_window.config(bg="#FFFFFF")
        payment_window.resizable(False, False)
        payment_window.grab_set()

        # Center window
        self._center_window(payment_window, 500, 450)

        # Title
        Label(payment_window,
              text="Payment",
              font=("Segoe UI", 28, "bold"),
              fg=UIComponentFactory.COLOR_TEXT_PRIMARY,
              bg="#FFFFFF").pack(pady=30)

        # Total amount
        Label(payment_window,
              text=f"Total Amount: PHP {total:.2f}",
              font=("Segoe UI", 20, "bold"),
              fg=UIComponentFactory.COLOR_BTN_RED,
              bg="#FFFFFF").pack(pady=20)

        # Payment amount label
        Label(payment_window,
              text="Enter Payment Amount:",
              font=("Segoe UI", 13),
              fg=UIComponentFactory.COLOR_TEXT_SECONDARY,
              bg="#FFFFFF").pack(pady=15)

        # Payment entry
        payment_entry = Entry(payment_window,
                              font=("Segoe UI", 18),
                              width=20,
                              bd=2,
                              relief="solid",
                              justify="center")
        payment_entry.pack(pady=15, ipady=10)
        payment_entry.focus_set()

        def process_payment():
            try:
                payment = float(payment_entry.get())
                if payment < total:
                    messagebox.showerror("Error", "Insufficient payment!")
                    return

                change = payment - total

                # Create order
                customer_id = self._customer_session.get_customer_id()
                cart_items = self._shopping_cart.get_items()
                order_id = self._order_manager.create_order(customer_id, total, cart_items)

                if not order_id:
                    return

                payment_window.destroy()
                self._show_receipt(total, payment, change, order_id)

            except ValueError:
                messagebox.showerror("Error", "Invalid payment amount!")

        # Pay Now button
        pay_btn = self._ui_factory.create_styled_button(
            payment_window, "Pay Now", process_payment, "green"
        )
        pay_btn.config(font=("Segoe UI", 14, "bold"))
        pay_btn.pack(pady=30, ipadx=50, ipady=15)

        # Bind Enter key
        payment_entry.bind('<Return>', lambda e: process_payment())

    def save_receipt_to_file(self, total, payment, change, order_id):
        try:
            with open("Customer.txt", "w", encoding="utf-8") as file:
                # Header
                file.write("=" * 70 + "\n")
                file.write("                    WEIRDOUGHS BAKERY\n")
                file.write("                        RECEIPT\n")
                file.write("=" * 70 + "\n\n")

                # Order Details
                file.write(f"Order #: {order_id}\n")
                file.write(f"Customer: {self._customer_session.get_name()}\n")
                file.write(f"Email: {self._customer_session.get_email()}\n")
                file.write(f"Phone: {self._customer_session.get_phone()}\n")
                address = self._customer_session.get_address() or 'N/A'
                file.write(f"Address: {address}\n")
                file.write(f"Date: {datetime.now().strftime('%B %d, %Y - %I:%M %p')}\n")
                file.write("\n" + "-" * 70 + "\n\n")

                # Items Header
                file.write(f"{'Item':<35} {'Qty':>5} {'Price':>12} {'Total':>12}\n")
                file.write("-" * 70 + "\n")

                # Cart Items
                cart_items = self._shopping_cart.get_items()
                for item in cart_items:
                    product = item['product']
                    qty = item['quantity']
                    price = product['price']
                    subtotal = price * qty

                    name = product['name'][:30] + "..." if len(product['name']) > 33 else product['name']
                    file.write(f"{name:<35} {qty:>5} {price:>12.2f} {subtotal:>12.2f}\n")

                file.write("-" * 70 + "\n\n")

                # Payment Summary
                file.write(f"{'TOTAL AMOUNT:':<50}{total:>15.2f}\n")
                file.write(f"{'AMOUNT PAID:':<50}{payment:>15.2f}\n")
                file.write(f"{'CHANGE:':<50}{change:>15.2f}\n")
                file.write("\n" + "=" * 70 + "\n")
                file.write("           Thank you for your purchase!\n")
                file.write("                Visit us again!\n")
                file.write("=" * 70 + "\n")

            messagebox.showinfo("Success", "Receipt saved to Customer.txt successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save receipt:\n{e}")

    def _show_receipt(self, total, payment, change, order_id):
        receipt_window = Toplevel(self._root)
        receipt_window.title("Receipt")
        receipt_window.geometry("600x850")  # ← CHANGED: Increased height for buttons
        receipt_window.config(bg="#F8F9FA")
        receipt_window.resizable(False, False)

        # Center window
        self._center_window(receipt_window, 600, 850)  # ← CHANGED: Updated height

        # Receipt container
        receipt_container = Frame(receipt_window, bg="#FFFFFF", bd=0)
        receipt_container.pack(pady=30, padx=30, fill=BOTH, expand=True)

        # Header
        Label(receipt_container,
              text="WEIRDOUGHS BAKERY",
              font=("Segoe UI", 22, "bold"),
              fg="#2C3E50",
              bg="#FFFFFF").pack(pady=(20, 5))

        Label(receipt_container,
              text="RECEIPT",
              font=("Segoe UI", 18, "bold"),
              fg="#7F8C8D",
              bg="#FFFFFF").pack(pady=5)

        # Order details
        self._create_receipt_details(receipt_container, order_id)

        # Separator
        Frame(receipt_container, bg="#E0E0E0", height=2).pack(fill=X, padx=20, pady=10)

        # Receipt items
        self._create_receipt_items(receipt_container, total, payment, change)

        # Thank you message
        Label(receipt_container,
              text="Thank you for your purchase!",
              font=("Segoe UI", 13, "bold"),
              fg=UIComponentFactory.COLOR_ACCENT,
              bg="#FFFFFF").pack(pady=15)

        button_frame = Frame(receipt_container, bg="#FFFFFF")
        button_frame.pack(pady=15)

        # Print Receipt button (LEFT)
        print_btn = Button(button_frame,
                           text="Print Receipt",
                           font=("Segoe UI", 11, "bold"),
                           fg="#FFFFFF",
                           bg="#5B8FA3",
                           activebackground="#4A7589",
                           activeforeground="#FFFFFF",
                           bd=0,
                           relief="flat",
                           cursor="hand2",
                           command=lambda: self.save_receipt_to_file(total, payment, change, order_id))
        print_btn.pack(side=LEFT, padx=10, ipadx=30, ipady=10)

        # Hover effects for print button
        print_btn.bind("<Enter>", lambda e: print_btn.config(bg="#4A7589"))
        print_btn.bind("<Leave>", lambda e: print_btn.config(bg="#5B8FA3"))

        # Close button (RIGHT)
        close_btn = Button(button_frame,
                           text="Close",
                           font=("Segoe UI", 11, "bold"),
                           fg="#FFFFFF",
                           bg="#95A5A6",
                           activebackground="#7F8C8D",
                           activeforeground="#FFFFFF",
                           bd=0,
                           relief="flat",
                           cursor="hand2",
                           command=lambda: self._close_receipt(receipt_window))
        close_btn.pack(side=LEFT, padx=10, ipadx=30, ipady=10)

        # Hover effects for close button
        close_btn.bind("<Enter>", lambda e: close_btn.config(bg="#7F8C8D"))
        close_btn.bind("<Leave>", lambda e: close_btn.config(bg="#95A5A6"))

    def _create_receipt_details(self, parent, order_id):
        details_frame = Frame(parent, bg="#F8F9FA", bd=0)
        details_frame.pack(fill=X, padx=20, pady=15)

        # Order number
        Label(details_frame,
              text=f"Order #: {order_id}",
              font=("Segoe UI", 11, "bold"),
              fg="#2C3E50",
              bg="#F8F9FA",
              anchor="w").pack(fill=X, padx=10, pady=2)

        # Customer info
        Label(details_frame,
              text=f"Customer: {self._customer_session.get_name()}",
              font=("Segoe UI", 11, "bold"),
              fg="#2C3E50",
              bg="#F8F9FA",
              anchor="w").pack(fill=X, padx=10, pady=2)

        Label(details_frame,
              text=f"Email: {self._customer_session.get_email()}",
              font=("Segoe UI", 10),
              fg="#2C3E50",
              bg="#F8F9FA",
              anchor="w").pack(fill=X, padx=10, pady=2)

        Label(details_frame,
              text=f"Phone: {self._customer_session.get_phone()}",
              font=("Segoe UI", 10),
              fg="#2C3E50",
              bg="#F8F9FA",
              anchor="w").pack(fill=X, padx=10, pady=2)

        address = self._customer_session.get_address() or 'N/A'
        Label(details_frame,
              text=f"Address: {address}",
              font=("Segoe UI", 10),
              fg="#2C3E50",
              bg="#F8F9FA",
              anchor="w",
              wraplength=550,
              justify="left").pack(fill=X, padx=10, pady=2)

        Label(details_frame,
              text=datetime.now().strftime("%B %d, %Y - %I:%M %p"),
              font=("Segoe UI", 10),
              fg="#7F8C8D",
              bg="#F8F9FA",
              anchor="w").pack(fill=X, padx=10, pady=2)

    def _create_receipt_items(self, parent, total, payment, change):
        receipt_text = Text(parent,
                            height=16,
                            width=70,
                            font=("Consolas", 10),
                            bg="#FFFFFF",
                            fg="#2C3E50",
                            bd=0,
                            relief=FLAT,
                            padx=15,
                            pady=10)
        receipt_text.pack(padx=20, pady=10)

        # Header
        receipt_text.insert(END, f"{'Item':<35} {'Qty':>5} {'Price':>12} {'Total':>12}\n")
        receipt_text.insert(END, "-" * 70 + "\n")

        # Items
        cart_items = self._shopping_cart.get_items()
        for item in cart_items:
            product = item['product']
            qty = item['quantity']
            price = product['price']
            subtotal = price * qty

            name = product['name'][:30] + "..." if len(product['name']) > 33 else product['name']
            receipt_text.insert(END, f"{name:<35} {qty:>5} {price:>12.2f} {subtotal:>12.2f}\n")

        receipt_text.insert(END, "-" * 70 + "\n\n")

        # Summary - labels left, numbers right with enough space
        receipt_text.insert(END, f"{'TOTAL AMOUNT:':<50}{total:>15.2f}\n")
        receipt_text.insert(END, f"{'AMOUNT PAID:':<50}{payment:>15.2f}\n")
        receipt_text.insert(END, f"{'CHANGE:':<50}{change:>15.2f}\n")

        receipt_text.config(state=DISABLED)

    def _close_receipt(self, window):
        self._shopping_cart.clear()
        self._update_cart_display()
        window.destroy()
        messagebox.showinfo("Success", "Transaction completed successfully!")
        self._refresh_products()

    def _center_window(self, window, width, height):
        window.update_idletasks()
        screen_width = self._root.winfo_screenwidth()
        screen_height = self._root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

    def close(self):
        try:
            self._root.destroy()
        except:
            pass