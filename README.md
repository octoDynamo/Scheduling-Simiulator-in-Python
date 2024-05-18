# Process Scheduling Application

This is a Python application that demonstrates various process scheduling algorithms with a graphical user interface (GUI) built using Tkinter.

## Features

- Supports the following process scheduling algorithms:
  - First-Come, First-Served (FCFS)
  - Shortest Job First (SJF)
  - Round-Robin
  - Priority Scheduling
- Allows users to select a configuration file containing process data.
- Displays the scheduling results in the GUI.
- Handles common error cases gracefully, such as invalid input files or selections.

## Usage

1. Install Python if you haven't already. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository:
'git clone https://github.com/octoDynamo/Scheduling-Simiulator-in-Python'

3. Navigate to the project directory:
'cd Scheduling-Simiulator-in-Python'

4. Run the application:
'python app.py'

5. Select a configuration file containing process data when prompted.

6. Choose the scheduling algorithm you want to use from the dropdown menu.

7. Click the "Run" button to execute the selected algorithm.

8. View the scheduling results displayed in the application window.

## Configuration File Format

The configuration file should be a plain text file with each line representing a process. Each line should contain three space-separated values:
- Process name
- Arrival time
- Burst time

Example:
'Process1 0 5
Process2 2 3
Process3 4 7'

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)

###### rr3ed