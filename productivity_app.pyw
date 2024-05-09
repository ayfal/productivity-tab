import time
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


def main():
    seconds = simpledialog.askinteger("Timer", "Enter the number of minutes for the timer: ", initialvalue=10) * 60
    task_list = simpledialog.askstring("Tasks", "Enter a list of tasks (separated by commas): ").split(",")
    alert = tk.Tk() # create a root window
    alert.withdraw()  # Hide the root window

    # Create a progress window
    progress = tk.Tk()
    progress.withdraw()
    progress_window = tk.Toplevel(progress)
    progress_window.title("Progress")
    progress_label = tk.Label(progress_window)
    progress_label.pack()

    # Update the progress label every second for each task
    while True:
        for task in task_list:
            for i in range(seconds):
                progress_label.config(text=f"Task: {task}\nTime remaining: {(seconds-i) // 60}:{(seconds-i) % 60} minutes")
                progress.update()
                time.sleep(1)

            # Show a message box when each task's timer is done
            messagebox.showinfo("Timer", f"Task: {task}\nTime's up!", parent=alert)
            alert.attributes('-topmost', True)  # Make messagebox appear on top


if __name__ == "__main__":
    main()
