
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import mysql.connector
import os
import shutil


class DatabaseManager:
    def __init__(self):
        self.__connection = None
        self.__host = "localhost"
        self.__user = "root"
        self.__password = ""
        self.__database = "bakerydb"

    def connect(self):
        try:
            self.__connection = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database
            )
            return True
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to connect:\n{e}")
            return False

    def disconnect(self):
        if self.__connection and self.__connection.is_connected():
            self.__connection.close()

    def get_connection(self):
        return self.__connection

    def is_connected(self):
        return self.__connection and self.__connection.is_connected()


class ProductManager:
    def __init__(self, db_manager):
        self._db_manager = db_manager

    def add_product(self, name, description, price, category, stock, image_filename):
        try:
            connection = self._db_manager.get_connection()
            cursor = connection.cursor()

            query = """
                INSERT INTO Products (name, description, price, category, stock_quantity, image_url)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, description, price, category, stock, image_filename))
            connection.commit()

            product_id = cursor.lastrowid
            cursor.close()
            return product_id

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to add product:\n{e}")
            return None

    def get_all_products(self):
        try:
            connection = self._db_manager.get_connection()
            cursor = connection.cursor()

            query = """
                SELECT product_id, name, description, price, category, stock_quantity, image_url
                FROM Products
                ORDER BY product_id DESC
            """
            cursor.execute(query)
            products = cursor.fetchall()
            cursor.close()
            return products

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to fetch products:\n{e}")
            return []

    def update_product(self, product_id, name, description, price, category, stock, image_filename):
        try:
            connection = self._db_manager.get_connection()
            cursor = connection.cursor()

            query = """
                UPDATE Products
                SET name = %s, description = %s, price = %s, category = %s, 
                    stock_quantity = %s, image_url = %s
                WHERE product_id = %s
            """
            cursor.execute(query, (name, description, price, category, stock, image_filename, product_id))
            connection.commit()
            cursor.close()
            return True

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to update product:\n{e}")
            return False

    def delete_product(self, product_id):
        try:
            connection = self._db_manager.get_connection()
            cursor = connection.cursor()

            query = "DELETE FROM Products WHERE product_id = %s"
            cursor.execute(query, (product_id,))
            connection.commit()
            cursor.close()
            return True

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to delete product:\n{e}")
            return False


class ImageManager:

    def __init__(self):
        self._bread_folder = self._get_bread_folder_path()
        self._ensure_folder_exists()

    def _get_bread_folder_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, "BREAD FOLDER")

    def _ensure_folder_exists(self):
        if not os.path.exists(self._bread_folder):
            os.makedirs(self._bread_folder)
            print(f"Created folder: {self._bread_folder}")

    def save_image(self, source_path, product_name):
        try:
            # Get file extension
            _, ext = os.path.splitext(source_path)
            if ext.lower() not in ['.jpg', '.jpeg', '.png']:
                messagebox.showerror("Error", "Only JPG and PNG images are supported!")
                return None

            # Create filename from product name
            filename = f"{product_name}{ext}"
            destination = os.path.join(self._bread_folder, filename)

            # Copy file
            shutil.copy2(source_path, destination)
            print(f"Image saved: {destination}")
            return filename

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image:\n{e}")
            return None

    def delete_image(self, filename):
        try:
            if filename:
                image_path = os.path.join(self._bread_folder, filename)
                if os.path.exists(image_path):
                    os.remove(image_path)
                    print(f"Image deleted: {image_path}")
        except Exception as e:
            print(f"Failed to delete image: {e}")


class AdminWindow:
    def __init__(self):
        # Initialize managers
        self.db_manager = DatabaseManager()
        self.product_manager = ProductManager(self.db_manager)
        self.image_manager = ImageManager()

        # UI variables
        self.selected_image_path = None
        self.product_listbox = None
        self.products_data = []

        # Initialize window
        self._initialize_window()

        # Connect to database
        if not self.db_manager.connect():
            messagebox.showerror("Error", "Cannot connect to database!")
            self.window.destroy()
            return

        self._create_ui()
        self._load_products()

        # Handle window close
        self.window.protocol("WM_DELETE_WINDOW", self._on_closing)

        # Start mainloop
        self.window.mainloop()

    def _initialize_window(self):
        self.window = Tk()
        self.window.title("WeirDoughs Bakery - Admin Panel")
        self.window.geometry("1200x700")
        self.window.resizable(True, True)
        self.window.config(bg="#F5F5F5")

        # Center window
        self.window.update_idletasks()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - 1200) // 2
        y = (screen_height - 700) // 2
        self.window.geometry(f"1200x700+{x}+{y}")

        # Set icon
        try:
            logo = PhotoImage(file="no bg llogo.png")
            self.window.iconphoto(False, logo)
        except:
            print("Logo file not found")

    def _create_ui(self):
        # Header
        self._create_header()

        # Main container
        main_container = Frame(self.window, bg="#F5F5F5")
        main_container.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Left side - Add/Edit Product Form
        self._create_product_form(main_container)

        # Right side - Product List
        self._create_product_list(main_container)

    def _create_header(self):
        header = Frame(self.window, bg="#D4A574", height=80)
        header.pack(fill=X)
        header.pack_propagate(False)

        Label(header,
              text="ADMIN PANEL - PRODUCT MANAGEMENT",
              font=("Segoe UI", 24, "bold"),
              fg="#2C3E50",
              bg="#D4A574").pack(pady=20)

        # Shadow
        Frame(self.window, bg="#B8935E", height=3).pack(fill=X)

    def _create_product_form(self, parent):
        form_frame = Frame(parent, bg="#FFFFFF", bd=0, relief=FLAT)
        form_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

        # Shadow effect
        shadow = Frame(parent, bg="#E0E0E0", bd=0)
        shadow.place(in_=form_frame, relx=0.01, rely=0.01, relwidth=1, relheight=1)
        shadow.lower()

        # Title
        Label(form_frame,
              text="Add New Product",
              font=("Segoe UI", 18, "bold"),
              fg="#2C3E50",
              bg="#FFFFFF").pack(pady=20)

        # Form fields container
        fields_container = Frame(form_frame, bg="#FFFFFF")
        fields_container.pack(fill=BOTH, expand=True, padx=30)

        # Product Name
        Label(fields_container,
              text="Product Name",
              font=("Segoe UI", 11, "bold"),
              fg="#2C3E50",
              bg="#FFFFFF",
              anchor="w").pack(fill=X, pady=(10, 5))

        self.name_entry = Entry(fields_container,
                                font=("Segoe UI", 11),
                                bg="#F8F9FA",
                                bd=2,
                                relief="solid")
        self.name_entry.pack(fill=X, ipady=8)

        # Description
        Label(fields_container,
              text="Description",
              font=("Segoe UI", 11, "bold"),
              fg="#2C3E50",
              bg="#FFFFFF",
              anchor="w").pack(fill=X, pady=(15, 5))

        self.description_text = Text(fields_container,
                                     font=("Segoe UI", 10),
                                     bg="#F8F9FA",
                                     bd=2,
                                     relief="solid",
                                     height=3,
                                     wrap=WORD)
        self.description_text.pack(fill=X)

        # Price and Stock (side by side)
        price_stock_frame = Frame(fields_container, bg="#FFFFFF")
        price_stock_frame.pack(fill=X, pady=(15, 0))

        # Price
        price_frame = Frame(price_stock_frame, bg="#FFFFFF")
        price_frame.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))

        Label(price_frame,
              text="Price (PHP)",
              font=("Segoe UI", 11, "bold"),
              fg="#2C3E50",
              bg="#FFFFFF",
              anchor="w").pack(fill=X, pady=(0, 5))

        self.price_entry = Entry(price_frame,
                                 font=("Segoe UI", 11),
                                 bg="#F8F9FA",
                                 bd=2,
                                 relief="solid")
        self.price_entry.pack(fill=X, ipady=8)

        # Stock
        stock_frame = Frame(price_stock_frame, bg="#FFFFFF")
        stock_frame.pack(side=LEFT, fill=X, expand=True)

        Label(stock_frame,
              text="Stock Quantity",
              font=("Segoe UI", 11, "bold"),
              fg="#2C3E50",
              bg="#FFFFFF",
              anchor="w").pack(fill=X, pady=(0, 5))

        self.stock_entry = Entry(stock_frame,
                                 font=("Segoe UI", 11),
                                 bg="#F8F9FA",
                                 bd=2,
                                 relief="solid")
        self.stock_entry.pack(fill=X, ipady=8)

        # Category
        Label(fields_container,
              text="Category",
              font=("Segoe UI", 11, "bold"),
              fg="#2C3E50",
              bg="#FFFFFF",
              anchor="w").pack(fill=X, pady=(15, 5))

        self.category_var = StringVar(value="Bread")
        category_frame = Frame(fields_container, bg="#FFFFFF")
        category_frame.pack(fill=X)

        Radiobutton(category_frame,
                    text="Bread",
                    variable=self.category_var,
                    value="Bread",
                    font=("Segoe UI", 10),
                    bg="#FFFFFF",
                    activebackground="#FFFFFF").pack(side=LEFT, padx=(0, 20))

        Radiobutton(category_frame,
                    text="Cake",
                    variable=self.category_var,
                    value="Cake",
                    font=("Segoe UI", 10),
                    bg="#FFFFFF",
                    activebackground="#FFFFFF").pack(side=LEFT)

        # Image upload
        Label(fields_container,
              text="Product Image",
              font=("Segoe UI", 11, "bold"),
              fg="#2C3E50",
              bg="#FFFFFF",
              anchor="w").pack(fill=X, pady=(15, 5))

        image_frame = Frame(fields_container, bg="#FFFFFF")
        image_frame.pack(fill=X)

        self.image_label = Label(image_frame,
                                 text="No image selected",
                                 font=("Segoe UI", 9),
                                 fg="#7F8C8D",
                                 bg="#FFFFFF",
                                 anchor="w")
        self.image_label.pack(side=LEFT, fill=X, expand=True)

        Button(image_frame,
               text="Browse",
               font=("Segoe UI", 10, "bold"),
               fg="#FFFFFF",
               bg="#5B8FA3",
               activebackground="#4A7589",
               bd=0,
               relief="flat",
               cursor="hand2",
               command=self._browse_image).pack(side=RIGHT, padx=5, ipadx=15, ipady=5)

        # Buttons
        button_frame = Frame(fields_container, bg="#FFFFFF")
        button_frame.pack(fill=X, pady=30)

        # Add Product button
        self.add_btn = Button(button_frame,
                              text="Add Product",
                              font=("Segoe UI", 12, "bold"),
                              fg="#FFFFFF",
                              bg="#27AE60",
                              activebackground="#229954",
                              bd=0,
                              relief="flat",
                              cursor="hand2",
                              command=self._add_product)
        self.add_btn.pack(side=LEFT, fill=X, expand=True, padx=(0, 5), ipady=10)

        # Clear button
        Button(button_frame,
               text="Clear Form",
               font=("Segoe UI", 12, "bold"),
               fg="#FFFFFF",
               bg="#95A5A6",
               activebackground="#7F8C8D",
               bd=0,
               relief="flat",
               cursor="hand2",
               command=self._clear_form).pack(side=LEFT, fill=X, expand=True, padx=(5, 0), ipady=10)

    def _create_product_list(self, parent):
        list_frame = Frame(parent, bg="#FFFFFF", bd=0, relief=FLAT)
        list_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        # Shadow effect
        shadow = Frame(parent, bg="#E0E0E0", bd=0)
        shadow.place(in_=list_frame, relx=0.01, rely=0.01, relwidth=1, relheight=1)
        shadow.lower()

        # Title
        Label(list_frame,
              text="Product List",
              font=("Segoe UI", 18, "bold"),
              fg="#2C3E50",
              bg="#FFFFFF").pack(pady=20)

        # Search bar
        search_frame = Frame(list_frame, bg="#FFFFFF")
        search_frame.pack(fill=X, padx=20, pady=(0, 10))

        Label(search_frame,
              text="Search:",
              font=("Segoe UI", 10),
              fg="#2C3E50",
              bg="#FFFFFF").pack(side=LEFT, padx=(0, 10))

        self.search_entry = Entry(search_frame,
                                  font=("Segoe UI", 10),
                                  bg="#F8F9FA",
                                  bd=2,
                                  relief="solid")
        self.search_entry.pack(side=LEFT, fill=X, expand=True, ipady=5)
        self.search_entry.bind('<KeyRelease>', lambda e: self._filter_products())

        # Listbox with scrollbar
        list_container = Frame(list_frame, bg="#FFFFFF")
        list_container.pack(fill=BOTH, expand=True, padx=20)

        scrollbar = Scrollbar(list_container)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.product_listbox = Listbox(list_container,
                                       font=("Consolas", 10),
                                       bg="#F8F9FA",
                                       bd=2,
                                       relief="solid",
                                       yscrollcommand=scrollbar.set,
                                       selectmode=SINGLE)
        self.product_listbox.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.config(command=self.product_listbox.yview)

        # Bind selection
        self.product_listbox.bind('<<ListboxSelect>>', self._on_product_select)

        # Action buttons
        action_frame = Frame(list_frame, bg="#FFFFFF")
        action_frame.pack(fill=X, padx=20, pady=20)

        Button(action_frame,
               text="Edit Selected",
               font=("Segoe UI", 11, "bold"),
               fg="#FFFFFF",
               bg="#3498DB",
               activebackground="#2980B9",
               bd=0,
               relief="flat",
               cursor="hand2",
               command=self._edit_product).pack(side=LEFT, fill=X, expand=True, padx=(0, 5), ipady=8)

        Button(action_frame,
               text="Delete Selected",
               font=("Segoe UI", 11, "bold"),
               fg="#FFFFFF",
               bg="#E74C3C",
               activebackground="#C0392B",
               bd=0,
               relief="flat",
               cursor="hand2",
               command=self._delete_product).pack(side=LEFT, fill=X, expand=True, padx=(5, 0), ipady=8)

    def _browse_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Product Image",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png"), ("All Files", "*.*")]
        )

        if file_path:
            self.selected_image_path = file_path
            filename = os.path.basename(file_path)
            self.image_label.config(text=filename, fg="#27AE60")

    def _add_product(self):
        # Get form data
        name = self.name_entry.get().strip()
        description = self.description_text.get("1.0", END).strip()
        price = self.price_entry.get().strip()
        stock = self.stock_entry.get().strip()
        category = self.category_var.get()

        # Validate inputs
        if not name or not description or not price or not stock:
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number and stock must be an integer!")
            return

        if price <= 0 or stock < 0:
            messagebox.showerror("Error", "Price must be positive and stock must be non-negative!")
            return

        # Handle image
        image_filename = None
        if self.selected_image_path:
            image_filename = self.image_manager.save_image(self.selected_image_path, name)
            if not image_filename:
                return

        # Add to database
        product_id = self.product_manager.add_product(name, description, price, category, stock, image_filename)

        if product_id:
            messagebox.showinfo("Success", f"Product '{name}' added successfully!")
            self._clear_form()
            self._load_products()

    def _edit_product(self):
        selection = self.product_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a product to edit!")
            return

        # Get selected product data
        index = selection[0]
        product = self.products_data[index]
        product_id = product[0]

        # Populate form with existing data
        self.name_entry.delete(0, END)
        self.name_entry.insert(0, product[1])

        self.description_text.delete("1.0", END)
        self.description_text.insert("1.0", product[2])

        self.price_entry.delete(0, END)
        self.price_entry.insert(0, str(product[3]))

        self.stock_entry.delete(0, END)
        self.stock_entry.insert(0, str(product[5]))

        self.category_var.set(product[4])

        if product[6]:
            self.image_label.config(text=product[6], fg="#3498DB")

        # Change button to Update
        self.add_btn.config(text="Update Product",
                            bg="#3498DB",
                            command=lambda: self._update_product(product_id, product[6]))

    def _update_product(self, product_id, old_image):
        # Get form data
        name = self.name_entry.get().strip()
        description = self.description_text.get("1.0", END).strip()
        price = self.price_entry.get().strip()
        stock = self.stock_entry.get().strip()
        category = self.category_var.get()

        # Validate
        if not name or not description or not price or not stock:
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            messagebox.showerror("Error", "Price must be a number and stock must be an integer!")
            return

        # Handle image
        image_filename = old_image
        if self.selected_image_path:
            # Delete old image if exists
            if old_image:
                self.image_manager.delete_image(old_image)
            # Save new image
            image_filename = self.image_manager.save_image(self.selected_image_path, name)

        # Update database
        if self.product_manager.update_product(product_id, name, description, price, category, stock, image_filename):
            messagebox.showinfo("Success", f"Product '{name}' updated successfully!")
            self._clear_form()
            self._load_products()
            # Reset button
            self.add_btn.config(text="Add Product", bg="#27AE60", command=self._add_product)

    def _delete_product(self):
        selection = self.product_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a product to delete!")
            return

        # Get selected product
        index = selection[0]
        product = self.products_data[index]
        product_id = product[0]
        product_name = product[1]
        image_filename = product[6]

        # Confirm deletion
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{product_name}'?"):
            # Delete from database
            if self.product_manager.delete_product(product_id):
                # Delete image if exists
                if image_filename:
                    self.image_manager.delete_image(image_filename)

                messagebox.showinfo("Success", f"Product '{product_name}' deleted successfully!")
                self._load_products()

    def _load_products(self):
        self.products_data = self.product_manager.get_all_products()
        self._display_products(self.products_data)

    def _display_products(self, products):
        self.product_listbox.delete(0, END)

        if not products:
            self.product_listbox.insert(END, "No products found")
            return

        # Header
        self.product_listbox.insert(END, f"{'ID':<6} {'Name':<25} {'Category':<10} {'Price':<10} {'Stock':<8}")
        self.product_listbox.insert(END, "-" * 70)

        # Products
        for product in products:
            product_id = product[0]
            name = product[1][:22] + "..." if len(product[1]) > 25 else product[1]
            category = product[4]
            price = f"₱{product[3]:.2f}"
            stock = product[5]

            line = f"{product_id:<6} {name:<25} {category:<10} {price:<10} {stock:<8}"
            self.product_listbox.insert(END, line)

    def _filter_products(self):
        search_term = self.search_entry.get().strip().lower()

        if not search_term:
            self._display_products(self.products_data)
            return

        filtered = [p for p in self.products_data
                    if search_term in p[1].lower() or search_term in p[4].lower()]
        self._display_products(filtered)

    def _on_product_select(self, event):
        pass  # Can add preview functionality here

    def _clear_form(self):
        self.name_entry.delete(0, END)
        self.description_text.delete("1.0", END)
        self.price_entry.delete(0, END)
        self.stock_entry.delete(0, END)
        self.category_var.set("Bread")
        self.selected_image_path = None
        self.image_label.config(text="No image selected", fg="#7F8C8D")
        self.add_btn.config(text="Add Product", bg="#27AE60", command=self._add_product)

    def _on_closing(self):
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
            self.db_manager.disconnect()
            self.window.destroy()


if __name__ == "__main__":
    app = AdminWindow()