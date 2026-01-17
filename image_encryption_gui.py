from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

class ImageEncryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")
        self.root.geometry("600x700")
        self.root.configure(bg='#2b2b2b')
        
        # Variables
        self.image_path = None
        self.original_image = None
        self.encrypted_image = None
        
        # Colors
        self.bg_color = '#2b2b2b'
        self.fg_color = '#ffffff'
        self.accent_color = '#4CAF50'
        self.secondary_color = '#3c3c3c'
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = tk.Label(
            self.root, 
            text="Image Encryption Tool", 
            font=('Arial', 24, 'bold'),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title.pack(pady=20)
        
        # Description
        desc = tk.Label(
            self.root,
            text="Encrypt/Decrypt images using pixel manipulation techniques",
            font=('Arial', 11),
            bg=self.bg_color,
            fg=self.fg_color
        )
        desc.pack(pady=(0, 20))
        
        # Image display frame
        img_frame = tk.Frame(self.root, bg=self.secondary_color)
        img_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Original image label
        self.original_label = tk.Label(
            img_frame,
            text="Original Image\n(Will appear here)",
            font=('Arial', 10),
            bg=self.secondary_color,
            fg=self.fg_color,
            relief='ridge',
            width=25,
            height=10
        )
        self.original_label.grid(row=0, column=0, padx=10, pady=10)
        
        # Encrypted image label
        self.encrypted_label = tk.Label(
            img_frame,
            text="Encrypted/Decrypted Image\n(Will appear here)",
            font=('Arial', 10),
            bg=self.secondary_color,
            fg=self.fg_color,
            relief='ridge',
            width=25,
            height=10
        )
        self.encrypted_label.grid(row=0, column=1, padx=10, pady=10)
        
        # Control panel
        control_frame = tk.Frame(self.root, bg=self.bg_color)
        control_frame.pack(pady=20, padx=20, fill='x')
        
        # Load image button
        load_btn = tk.Button(
            control_frame,
            text="Load Image",
            command=self.load_image,
            bg=self.accent_color,
            fg=self.fg_color,
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            relief='raised',
            cursor='hand2'
        )
        load_btn.grid(row=0, column=0, padx=10, pady=10)
        
        # Encryption method selection
        method_label = tk.Label(
            control_frame,
            text="Encryption Method:",
            font=('Arial', 11),
            bg=self.bg_color,
            fg=self.fg_color
        )
        method_label.grid(row=0, column=1, padx=10, pady=10)
        
        self.method_var = tk.StringVar(value="swap")
        methods = ["swap", "xor", "add", "reverse"]
        method_menu = ttk.Combobox(
            control_frame,
            textvariable=self.method_var,
            values=methods,
            state="readonly",
            width=15
        )
        method_menu.grid(row=0, column=2, padx=10, pady=10)
        
        # Key input
        key_label = tk.Label(
            control_frame,
            text="Encryption Key (0-255):",
            font=('Arial', 11),
            bg=self.bg_color,
            fg=self.fg_color
        )
        key_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.key_var = tk.IntVar(value=128)
        key_entry = tk.Entry(
            control_frame,
            textvariable=self.key_var,
            font=('Arial', 11),
            width=10
        )
        key_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        # Encrypt button
        encrypt_btn = tk.Button(
            button_frame,
            text="Encrypt Image",
            command=self.encrypt_image,
            bg='#2196F3',
            fg=self.fg_color,
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            relief='raised',
            cursor='hand2'
        )
        encrypt_btn.grid(row=0, column=0, padx=10)
        
        # Decrypt button
        decrypt_btn = tk.Button(
            button_frame,
            text="Decrypt Image",
            command=self.decrypt_image,
            bg='#FF9800',
            fg=self.fg_color,
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            relief='raised',
            cursor='hand2'
        )
        decrypt_btn.grid(row=0, column=1, padx=10)
        
        # Save button
        save_btn = tk.Button(
            button_frame,
            text="Save Result",
            command=self.save_image,
            bg='#9C27B0',
            fg=self.fg_color,
            font=('Arial', 11, 'bold'),
            padx=20,
            pady=10,
            relief='raised',
            cursor='hand2'
        )
        save_btn.grid(row=0, column=2, padx=10)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to load an image")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=('Arial', 10),
            bg=self.secondary_color,
            fg=self.fg_color,
            relief='sunken',
            anchor='w'
        )
        status_bar.pack(side='bottom', fill='x', padx=0, pady=0)
    
    def load_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        
        if file_path:
            try:
                self.image_path = file_path
                self.original_image = Image.open(file_path)
                
                # Convert to RGB if necessary
                if self.original_image.mode != 'RGB':
                    self.original_image = self.original_image.convert('RGB')
                
                # Display image
                self.display_image(self.original_image, self.original_label)
                
                # Update status
                filename = os.path.basename(file_path)
                self.status_var.set(f"Loaded: {filename} ({self.original_image.size[0]}x{self.original_image.size[1]})")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def display_image(self, image, label):
        # Resize image for display
        display_size = (200, 200)
        img_display = image.copy()
        img_display.thumbnail(display_size, Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage
        from PIL import ImageTk
        img_tk = ImageTk.PhotoImage(img_display)
        
        # Update label
        label.configure(image=img_tk, text="")
        label.image = img_tk  # Keep a reference
    
    def encrypt_image(self):
        if not self.original_image:
            messagebox.showwarning("No Image", "Please load an image first!")
            return
        
        try:
            method = self.method_var.get()
            key = self.key_var.get()
            
            # Convert image to numpy array
            img_array = np.array(self.original_image)
            
            # Apply selected encryption method
            if method == "swap":
                encrypted_array = self.swap_pixels(img_array)
            elif method == "xor":
                encrypted_array = self.xor_pixels(img_array, key)
            elif method == "add":
                encrypted_array = self.add_pixels(img_array, key)
            elif method == "reverse":
                encrypted_array = self.reverse_pixels(img_array)
            else:
                encrypted_array = img_array
            
            # Convert back to image
            self.encrypted_image = Image.fromarray(encrypted_array)
            
            # Display encrypted image
            self.display_image(self.encrypted_image, self.encrypted_label)
            
            # Update status
            self.status_var.set(f"Image encrypted using {method} method with key {key}")
            
        except Exception as e:
            messagebox.showerror("Encryption Error", f"Failed to encrypt image: {str(e)}")
    
    def decrypt_image(self):
        if not self.original_image:
            messagebox.showwarning("No Image", "Please load an image first!")
            return
        
        try:
            method = self.method_var.get()
            key = self.key_var.get()
            
            # If we have an encrypted image, decrypt it
            if self.encrypted_image:
                img_array = np.array(self.encrypted_image)
            else:
                # Otherwise, assume the original is encrypted
                img_array = np.array(self.original_image)
            
            # Apply the inverse of the selected encryption method
            if method == "swap":
                # Swap is its own inverse
                decrypted_array = self.swap_pixels(img_array)
            elif method == "xor":
                # XOR is its own inverse
                decrypted_array = self.xor_pixels(img_array, key)
            elif method == "add":
                # For addition, we subtract the key
                decrypted_array = self.subtract_pixels(img_array, key)
            elif method == "reverse":
                # Reverse is its own inverse
                decrypted_array = self.reverse_pixels(img_array)
            else:
                decrypted_array = img_array
            
            # Convert back to image
            self.encrypted_image = Image.fromarray(decrypted_array)
            
            # Display decrypted image
            self.display_image(self.encrypted_image, self.encrypted_label)
            
            # Update status
            self.status_var.set(f"Image decrypted using {method} method with key {key}")
            
        except Exception as e:
            messagebox.showerror("Decryption Error", f"Failed to decrypt image: {str(e)}")
    
    def save_image(self):
        if not self.encrypted_image:
            messagebox.showwarning("No Result", "No encrypted/decrypted image to save!")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Save Image",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                self.encrypted_image.save(file_path)
                self.status_var.set(f"Image saved to: {file_path}")
                messagebox.showinfo("Success", f"Image saved successfully to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Save Error", f"Failed to save image: {str(e)}")
    
    # Pixel manipulation methods
    def swap_pixels(self, img_array):
        """Swap red and blue channels of the image"""
        swapped = img_array.copy()
        swapped[:, :, 0], swapped[:, :, 2] = img_array[:, :, 2], img_array[:, :, 0]
        return swapped
    
    def xor_pixels(self, img_array, key):
        """Apply XOR operation to each pixel with the key"""
        # Ensure key is within 0-255 range
        key = key % 256
        return np.bitwise_xor(img_array, key)
    
    def add_pixels(self, img_array, key):
        """Add key value to each pixel (with wrap-around)"""
        key = key % 256
        result = img_array.astype(np.uint16) + key
        result = np.clip(result, 0, 255).astype(np.uint8)
        return result
    
    def subtract_pixels(self, img_array, key):
        """Subtract key value from each pixel (with wrap-around)"""
        key = key % 256
        result = img_array.astype(np.int16) - key
        result = np.clip(result, 0, 255).astype(np.uint8)
        return result
    
    def reverse_pixels(self, img_array):
        """Reverse the order of pixels in each row"""
        return img_array[:, ::-1, :]

def main():
    root = tk.Tk()
    app = ImageEncryptionTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()