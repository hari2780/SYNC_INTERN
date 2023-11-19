import tkinter as tk
from tkinter import messagebox
import datetime

def set_alarm():
    alarm_time_str = entry.get()
    try:
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")
        return
    current_time = datetime.datetime.now()
    current_time = current_time.replace(year=alarm_time.year, month=alarm_time.month, day=alarm_time.day)
    time_difference = alarm_time - current_time
    time_difference_seconds = time_difference.total_seconds()
    if time_difference_seconds <= 0:
        messagebox.showerror("Error", "Please set a future time.")
        return
    root.after(int(time_difference_seconds * 1000), trigger_alarm)
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time_str}.")

def trigger_alarm():
    messagebox.showinfo("Alarm", "Time's up!")

def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=f"Current Time: {current_time}")
    root.after(1000, update_time)

root = tk.Tk()
root.title("Alarm Clock")
root.configure(bg='#3498db')

time_label = tk.Label(root, text="", bg='#3498db', fg='white', font=('Helvetica', 12))
time_label.pack(side=tk.TOP, pady=10)

label = tk.Label(root, text="Set Alarm Time (HH:MM):", bg='#3498db', fg='white', font=('Helvetica', 12))
label.pack()

entry = tk.Entry(root, bg='#ecf0f1', fg='#2c3e50', font=('Helvetica', 12))
entry.pack()

set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm, bg='#2ecc71', fg='white', font=('Helvetica', 12, 'bold'))
set_alarm_button.pack()

root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) // 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) // 2
root.geometry(f"+{x}+{y}")

root.after(1000, update_time)
root.mainloop()
