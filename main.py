import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound

class Timer:
    def __init__(self, minutes, event_name):
        self.minutes = minutes
        self.event_name = event_name
    
    def update_time(self):            
        total_seconds = self.minutes * 60
        while total_seconds > 0:    
            #timer = datetime.timedelta(seconds = total_seconds) 
            time.sleep(1)
            total_seconds -= 1
            if total_seconds == 0:
                self.play_alarm()
                messagebox.showinfo(self.event_name.upper(),self.event_name.upper())
    
    def play_alarm(self):
        freq = 2000	
        dur = 500                    
        winsound.Beep(freq, dur)
        winsound.Beep(freq, dur)
        winsound.Beep(freq, dur)
        winsound.Beep(freq, dur)
                
class Application(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.build_interface()
        self.row_ = 3

    def build_interface(self):
        self.lbl1 = tk.Label(self, text="Event Name")
        self.lbl1.grid(row=0, column=0)
        
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.grid(row=0, column=1)
        
        self.lbl2 = tk.Label(self, text="Time(minutes)")
        self.lbl2.grid(row=1, column=0)        
        self.time_entry = tk.Entry(self, width=30)
        self.time_entry.grid(row=1, column=1)
        
        self.add_button = tk.Button(self, text="Add", command=lambda: self.add_timer(self.time_entry.get()))
        self.add_button.place(x=125,y=50)
        
    def add_timer(self, minutes):
        minutes = int(minutes)
        event_name = self.name_entry.get()
        self.row_+=1
        my_timer = Timer(minutes, event_name)
        t = threading.Thread(target=my_timer.update_time)
        t.daemon = True
        t.start()
        t.join
        self.name_entry.delete(0, 'end')
        self.time_entry.delete(0, 'end')
        messagebox.showinfo("Saved.","Saved.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("TIMER")
    root.geometry('280x90')
    root.resizable(0,0)
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
    