import time
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


def main():
    root = tk.Tk()
    root.withdraw()
    seconds = simpledialog.askinteger("Timer", "Enter the number of minutes for the timer: ", initialvalue=10) * 60
    task_list = simpledialog.askstring("Tasks", "Enter a list of tasks (separated by commas): ").split(",")
    
    # Create a new window
    progress_window = tk.Toplevel(root)
    progress_window.title("Progress")
    progress_label = tk.Label(progress_window, text="Timer in progress...")
    progress_label.pack()

    # Update the progress label every second for each task
    while True:
        for task in task_list:
            for i in range(seconds):
                progress_label.config(text=f"Task: {task}\nTime remaining: {seconds-i} seconds")
                root.update()
                time.sleep(1)

            # Show a message box when each task's timer is done
            messagebox.showinfo("Timer", f"Task: {task}\nTime's up!")


if __name__ == "__main__":
    main()
