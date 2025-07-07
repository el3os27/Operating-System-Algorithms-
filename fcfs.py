import tkinter as tk
from tkinter import ttk

def find_waiting_time(processes, n, bt, wt, at):  
    service_time = [0] * n  
    service_time[0] = 0
    wt[0] = 0

    for i in range(1, n):  
        service_time[i] = (service_time[i - 1] + bt[i - 1])  
        wt[i] = service_time[i] - at[i]  
        if wt[i] < 0: 
            wt[i] = 0

def find_turn_around_time(processes, n, bt, wt, tat):  
    for i in range(n): 
        tat[i] = bt[i] + wt[i]  

def find_avg_time(processes, n, bt, at):  
    wt = [0] * n 
    tat = [0] * n  
    find_waiting_time(processes, n, bt, wt, at)  
    find_turn_around_time(processes, n, bt, wt, tat)  

    result_text.delete(1.0, tk.END)  # Clear previous results
    result_text.insert(tk.END, "Processes   Burst Time   Arrival Time     Waiting Time   Turn-Around Time  Completion Time\n") 
    total_wt = 0
    total_tat = 0
    for i in range(n): 
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        compl_time = tat[i] + at[i]  
        result_text.insert(tk.END, f"  {i + 1}\t\t{bt[i]}\t\t{at[i]}\t\t{wt[i]}\t\t{tat[i]}\t\t{compl_time}\n")

    avg_wt = total_wt / n
    avg_tat = total_tat / n
    result_text.insert(tk.END, f"\nAverage waiting time = {avg_wt:.5f}\nAverage turn around time = {avg_tat}")

def run_fcfs():
    try:
        processes_values = [int(x) for x in processes_entry.get().split(",")]
        n_value = len(processes_values)
        burst_time_values = [int(x) for x in burst_time_entry.get().split(",")]
        arrival_time_values = [int(x) for x in arrival_time_entry.get().split(",")]
        find_avg_time(processes_values, n_value, burst_time_values, arrival_time_values)
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter valid numerical values.")

# GUI setup
root = tk.Tk()
root.title("FCFS Scheduling Algorithm")

# Processes entry
processes_label = tk.Label(root, text="Enter Process IDs:")
processes_entry = tk.Entry(root, width=30)
processes_label.pack()
processes_entry.pack()

# Burst time entry
burst_time_label = tk.Label(root, text="Enter Burst Times:")
burst_time_entry = tk.Entry(root, width=30)
burst_time_label.pack()
burst_time_entry.pack()

# Arrival time entry
arrival_time_label = tk.Label(root, text="Enter Arrival Times:")
arrival_time_entry = tk.Entry(root, width=30)
arrival_time_label.pack()
arrival_time_entry.pack()

# Button to run FCFS
run_button = tk.Button(root, text="Run FCFS", command=run_fcfs)
run_button.pack()

# Result display text
result_text = tk.Text(root, height=15, width=60)
result_text.pack()

root.mainloop()