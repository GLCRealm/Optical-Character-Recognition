import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import customtkinter as ctk
from customtkinter import CTkImage
from ocr6 import ocr_image

class OCRApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Project OCR")
        self.geometry("1000x800")

        self.image_path = None
        self.ctk_img = None  # Reference to hold the CTkImage object

        # Create a frame for image display
        self.image_frame = ctk.CTkFrame(self, width=350, height=400, corner_radius=30)
        self.image_frame.pack(side="left", padx=20, pady=20)

        # Label to show the image
        self.image_label = ctk.CTkLabel(self.image_frame, text="IMPORT IMAGE", compound='center',
                                        font=('Times New Roman', 30), width=300, height=300,
                                        corner_radius=30, fg_color="#1f1f1f", anchor="center")
        self.image_label.pack(padx=10, pady=20)

        # Create a frame for text display
        self.text_frame = ctk.CTkFrame(self, width=300, height=300, corner_radius=30)
        self.text_frame.pack(side="right", padx=10, pady=20)

        # Text box to show the OCR result
        self.text_box = ctk.CTkTextbox(self.text_frame, width=300, height=300, corner_radius=10, fg_color="#1f1f1f",
                                       font=('Times New Roman', 30))
        self.text_box.pack(padx=10, pady=20)

        # Buttons
        self.button_frame = ctk.CTkFrame(self, corner_radius=0)
        self.button_frame.pack(side="bottom", anchor="w", padx=10, pady=20)

        self.predict_button = ctk.CTkButton(self.button_frame, text="Predict", command=self.predict, corner_radius=20)
        self.predict_button.pack(side="left", padx=20, pady=30)

        self.clear_button = ctk.CTkButton(self.button_frame, text="Cancel", command=self.clear_image, corner_radius=20)
        self.clear_button.pack(side="left", padx=20, pady=30)

        # Set up drag and drop
        self.image_label.bind("<Button-1>", self.select_image)

    def select_image(self, event=None):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.display_image(self.image_path)

    def display_image(self, path):
        img = Image.open(path)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        self.ctk_img = CTkImage(light_image=img, dark_image=img, size=(300, 300))
        self.image_label.configure(image=self.ctk_img, text="", font=('Times New Roman', 20), compound='center')
        self.image_label.image = self.ctk_img  # Keep a reference to avoid garbage collection

    def clear_image(self):
        self.image_path = None
        self.image_label.configure(image=None, text="IMPORT IMAGE")
        self.image_label.image = None  # Clear the image reference
        self.text_box.delete(1.0, tk.END)

    def predict(self):
        if self.image_path:
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, "Please wait, while the model is making a prediction...\n")
            self.update()
            predicted_sentence = ocr_image(self.image_path)
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, predicted_sentence)
        else:
            messagebox.showwarning("Warning", "Please select an image first")

if __name__ == "__main__":
    app = OCRApp()
    app.mainloop()
