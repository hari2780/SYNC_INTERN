import tkinter as tk
from tkinter import scrolledtext
import datetime

class SimpleChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")
        self.create_widgets()

    def create_widgets(self):
        self.master.geometry("600x500")
        self.master.configure(bg='#e6e6e6')
        self.chat_display = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=50, height=15, font=('Arial', 12))
        self.chat_display.pack(expand=True, fill='both', padx=10, pady=10)
        self.user_input_entry = tk.Entry(self.master, width=50, font=('Arial', 12), bg='#ffffff')
        self.user_input_entry.pack(pady=10, padx=10)
        self.send_button = tk.Button(self.master, text="Send", command=self.send_message, bg='#4CAF50', fg='white', bd=0, relief=tk.FLAT)
        self.send_button.pack(pady=5, padx=10)
        self.chat_display.insert(tk.END, "Bot: Hello! I'm your chatbot. Type 'bye' to exit.\n")

    def send_message(self):
        user_input = self.user_input_entry.get()
        self.chat_display.insert(tk.END, f"You: {user_input}\n")

        if user_input.lower() == 'bye':
            self.chat_display.insert(tk.END, "Bot: Goodbye! See you next time.\n")
            self.master.after(2000, self.master.destroy)  # Close the window after 2 seconds
        else:
            response = get_response(user_input)
            self.chat_display.insert(tk.END, f"Bot: {response}\n")
            self.user_input_entry.delete(0, tk.END)

def get_response(user_input):
    user_input = user_input.lower()
    greetings = ['hello', 'hi', 'hey', 'greetings']
    farewells = ['bye', 'goodbye', 'see you', 'farewell']
    weather_keywords = ['weather', 'temperature', 'forecast']
    information_keywords = ['tell me about', 'information on', 'what is']
    time_keywords = ['time', 'current time', 'what time is it']
    chatbot_keywords = ['who are you', 'tell me about yourself', 'chatbot']
    technology_keywords = ['technology', 'latest tech', 'tech news']
    tips_keywords = ['helpful tips', 'advice', 'tips']
    gratitude_keywords = ['thank you', 'thanks', 'appreciate']

    responses = {
        'how are you': 'I am fine, thank you!',
        'tell me a joke': 'Why don’t scientists trust atoms? Because they make up everything!',
        'default': 'I\'m sorry, I don\'t understand. Can you ask me something else?',
        'weather': 'I\'m just a text-based bot and don\'t have real-time weather information. You can check a weather website for the latest updates.',
        'information': 'I can provide information on a variety of topics. Please specify what you would like to know.',
        'time': f'The current time is {datetime.datetime.now().strftime("%H:%M")}.',
        'chatbot': 'I am a simple rule-based chatbot created for demo purposes. My main function is to respond to specific queries and engage in conversation.',
        'technology': 'For the latest in technology, I recommend checking reputable tech news websites or blogs.',
        'tips': 'Sure! Here\'s a random tip: Taking short breaks during work can improve productivity.',
        'gratitude': 'You\'re welcome! If you have more questions or need assistance, feel free to ask.'
    }
    if any(word in user_input for word in greetings):
        current_time = datetime.datetime.now().hour
        if 5 <= current_time < 12:
            return "Good morning! How can I assist you today?"
        elif 12 <= current_time < 17:
            return "Good afternoon! What can I do for you?"
        elif 17 <= current_time < 21:
            return "Good evening! How may I help you?"
        else:
            return "Hello! It's late, but I'm here to help if you need anything."
    elif any(word in user_input for word in farewells):
        return "Goodbye! Have a great day!"
    elif any(word in user_input for word in weather_keywords):
        return responses['weather']
    elif any(word in user_input for word in information_keywords):
        return responses['information']
    elif any(word in user_input for word in time_keywords):
        return responses['time']
    elif any(word in user_input for word in chatbot_keywords):
        return responses['chatbot']
    elif any(word in user_input for word in technology_keywords):
        return responses['technology']
    elif any(word in user_input for word in tips_keywords):
        return responses['tips']
    elif any(word in user_input for word in gratitude_keywords):
        return responses['gratitude']
    else:
        for key in responses:
            if key in user_input:
                return responses[key]
        return responses['default']

root = tk.Tk()
chatbot_gui = SimpleChatbotGUI(root)
root.mainloop()
