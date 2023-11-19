import tkinter as tk
from tkinter import ttk
from pyshorteners import Shortener

class URLShortenerApp:
    def __init__(self, master):
        self.master = master
        master.title("URL Shortener")
        master.geometry("400x200") 
        window_width = master.winfo_reqwidth()
        window_height = master.winfo_reqheight()
        position_right = int(master.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(master.winfo_screenheight() / 2 - window_height / 2)
        master.geometry("+{}+{}".format(position_right, position_down))

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.label = ttk.Label(master, text="Enter URL:")
        self.label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.url_entry = ttk.Entry(master, width=30)
        self.url_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        self.shorten_button = ttk.Button(master, text="Shorten", command=self.shorten_url)
        self.shorten_button.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        self.shortened_url_label = ttk.Label(master, text="")
        self.shortened_url_label.grid(row=1, column=0, columnspan=3, pady=10, padx=10, sticky="w")
        for i in range(2):
            master.grid_rowconfigure(i, weight=1)
        for i in range(3):
            master.grid_columnconfigure(i, weight=1)

    def shorten_url(self):
        original_url = self.url_entry.get()

        if original_url:
            s = Shortener()
            shortened_url = s.tinyurl.short(original_url)

            self.shortened_url_label.config(text="Shortened URL: " + shortened_url)
        else:
            self.shortened_url_label.config(text="Please enter a URL.")

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortenerApp(root)
    root.mainloop()
