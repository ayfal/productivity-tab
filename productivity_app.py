import time
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


def start_timer(minutes, task_list):
    seconds = minutes * 60
    root = tk.Tk()
    root.withdraw()

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


def main():
    root = tk.Tk()
    root.withdraw()
    minutes = simpledialog.askinteger("Timer", "Enter the number of minutes for the timer: ")
    root.withdraw()
    # Get a list of tasks from the user
    tasks = simpledialog.askstring("Tasks", "Enter a list of tasks (separated by commas): ")
    task_list = tasks.split(",")
    start_timer(minutes, task_list)


if __name__ == "__main__":
    main()
