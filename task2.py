import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
from dotenv import load_dotenv
import os
load_dotenv() 
pwd=os.getenv("password")
class OTPVerificationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("OTP Verification")
        self.master.geometry("300x200")
        self.master.configure(bg="#e1d8b9")

        self.style = ThemedStyle(self.master)
        self.style.set_theme("plastik")

        self.email_label = ttk.Label(self.master, text="Enter your email:", background="#e1d8b9")
        self.email_label.pack(pady=5)

        self.email_entry = ttk.Entry(self.master, width=25)
        self.email_entry.pack(pady=5)

        self.send_otp_button = ttk.Button(self.master, text="Send OTP", command=self.send_otp)
        self.send_otp_button.pack(pady=10)

        self.otp_label = ttk.Label(self.master, text="Enter OTP:", background="#e1d8b9")
        self.otp_label.pack(pady=5)

        self.otp_entry = ttk.Entry(self.master, width=25)
        self.otp_entry.pack(pady=5)

        self.verify_button = ttk.Button(self.master, text="Verify OTP", command=self.verify_otp)
        self.verify_button.pack(pady=10)

    def generate_otp(self):
        return str(random.randint(100000, 999999))

    def send_email(self, receiver_email, otp):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'h85316085@gmail.com'
        smtp_password = pwd #use your email password

        subject = 'OTP Verification'
        body = f'Your OTP is: {otp}'
        message = MIMEMultipart()
        message['From'] = smtp_username
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, receiver_email, message.as_string())

    def send_otp(self):
        user_email = self.email_entry.get()
        if user_email:
            self.otp = self.generate_otp()
            self.send_email(user_email, self.otp)
            messagebox.showinfo("OTP Sent", "An OTP has been sent to your email.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter your email.")

    def verify_otp(self):
        user_input_otp = self.otp_entry.get()
        if user_input_otp == self.otp:
            messagebox.showinfo("OTP Verified", "OTP verification successful.")
        else:
            messagebox.showerror("OTP Verification Failed", "OTP verification failed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = OTPVerificationApp(root)
    root.mainloop()
