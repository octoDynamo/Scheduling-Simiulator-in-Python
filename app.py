import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import csv
import operator

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)

def read_processes(filename):
    processes = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=' ')
            for row in reader:
                if len(row) == 3 and all(row):
                    processes.append(Process(row[0], row[1], row[2]))
                else:
                    messagebox.showerror("Erreur", "Fichier de configuration invalide.")
                    return None
        return processes
    except FileNotFoundError:
        messagebox.showerror("Erreur", f"Fichier {filename} introuvable.")
        return None

def fcfs_scheduling(processes):
    time = 0
    result = []
    for process in processes:
        if process.arrival_time > time:
            time = process.arrival_time
        result.append((process.name, time, time + process.burst_time))
        time += process.burst_time
    return result

def sjf_scheduling(processes):
    sorted_processes = sorted(processes, key=operator.attrgetter('arrival_time', 'burst_time'))
    return fcfs_scheduling(sorted_processes)

def round_robin_scheduling(processes, quantum):
    remaining = [process.burst_time for process in processes]
    time = 0
    result = []
    while True:
        all_done = True
        for i, process in enumerate(processes):
            if remaining[i] > 0:
                all_done = False
                if process.arrival_time > time:
                    time = process.arrival_time
                burst = min(quantum, remaining[i])
                result.append((process.name, time, time + burst))
                time += burst
                remaining[i] -= burst
        if all_done:
            break
    return result

def priority_scheduling(processes):
    sorted_processes = sorted(processes, key=operator.attrgetter('arrival_time', 'priority'))
    return fcfs_scheduling(sorted_processes)

def choose_file():
    filename = filedialog.askopenfilename()
    if filename:
        processes = read_processes(filename)
        if processes:
            file_entry.delete(0, tk.END)
            file_entry.insert(0, filename)

def run_algorithm():
    filename = file_entry.get()
    processes = read_processes(filename)
    if processes:
        choice = algorithm_choice.get()
        if choice == 1:
            result = fcfs_scheduling(processes)
        elif choice == 2:
            result = sjf_scheduling(processes)
        elif choice == 3:
            quantum = int(quantum_entry.get())
            result = round_robin_scheduling(processes, quantum)
        elif choice == 4:
                result = priority_scheduling(processes)
        
        result_text.delete(1.0, tk.END)
        for item in result:
            result_text.insert(tk.END, f"Processus: {item[0]}, Temps de début: {item[1]}, Temps de fin: {item[2]}\n")

# GUI setup
root = tk.Tk()
root.title("Ordonnancement des processus")

file_label = tk.Label(root, text="Choisir un fichier de configuration:")
file_label.grid(row=0, column=0, sticky="w")

file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=5, pady=5)

file_button = tk.Button(root, text="Parcourir", command=choose_file)
file_button.grid(row=0, column=2, padx=5, pady=5)

algorithm_label = tk.Label(root, text="Choisir un algorithme:")
algorithm_label.grid(row=1, column=0, sticky="w")

algorithm_choice = tk.IntVar()
algorithm_choice.set(1)

fcfs_radio = tk.Radiobutton(root, text="FCFS", variable=algorithm_choice, value=1)
fcfs_radio.grid(row=1, column=1, sticky="w")

sjf_radio = tk.Radiobutton(root, text="SJF (Shortest Job First)", variable=algorithm_choice, value=2)
sjf_radio.grid(row=2, column=1, sticky="w")

rr_radio = tk.Radiobutton(root, text="Round-Robin", variable=algorithm_choice, value=3)
rr_radio.grid(row=3, column=1, sticky="w")

quantum_label = tk.Label(root, text="Quantum :")
quantum_label.grid(row=3, column=2, sticky="w")

quantum_entry = tk.Entry(root, width=10)
quantum_entry.grid(row=3, column=3, padx=5, pady=5)

run_button = tk.Button(root, text="Exécuter", command=run_algorithm)
run_button.grid(row=5, column=1, padx=5, pady=10)

result_text = tk.Text(root, height=10, width=60)
result_text.grid(row=6, columnspan=3, padx=5, pady=5)

priority_radio = tk.Radiobutton(root, text="Priorité", variable=algorithm_choice, value=4)
priority_radio.grid(row=4, column=1, sticky="w")

root.mainloop()