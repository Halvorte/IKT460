import tkinter as tk
from PIL import Image, ImageTk

class ImageSelection:
    def __init__(self, master, image1_path, image2_path):
        self.master = master
        self.image1_path = image1_path
        self.image2_path = image2_path
        self.selected_image = None

        # Load images
        self.image1 = Image.open(image1_path)
        self.image2 = Image.open(image2_path)

        # Resize images to fit the window
        self.image1 = self.image1.resize((200, 200), Image.ANTIALIAS)
        self.image2 = self.image2.resize((200, 200), Image.ANTIALIAS)

        # Convert images to Tkinter format
        self.image1_tk = ImageTk.PhotoImage(self.image1)
        self.image2_tk = ImageTk.PhotoImage(self.image2)

        # Create labels for images
        self.label1 = tk.Label(self.master, image=self.image1_tk)
        self.label2 = tk.Label(self.master, image=self.image2_tk)

        # Bind click events to labels
        self.label1.bind("<Button-1>", self.select_image1)
        self.label2.bind("<Button-1>", self.select_image2)

        # Pack labels
        self.label1.pack(side="left", padx=10, pady=10)
        self.label2.pack(side="right", padx=10, pady=10)

    def select_image1(self, event):
        self.selected_image = self.image1_path
        self.master.quit()

    def select_image2(self, event):
        self.selected_image = self.image2_path
        self.master.quit()

    def run(self):
        self.master.mainloop()




if __name__ == '__main__':

    # Example usage
    root = tk.Tk()
    app = ImageSelection(root, 'images/die_hard.jpg', 'images/john_wick_2.jpg') #'"image1.jpg", "image2.jpg")
    app.run()

    # The selected image path is stored in the `selected_image` attribute
    print("Selected image:", app.selected_image)
