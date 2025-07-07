import tkinter as tk

def scan_algorithm():
    disk_size = 200
    arr = [int(num) for num in numbers_entry.get().split()]
    head = int(head_entry.get())r
    direction = direction_var.get()

    seek_count = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []

    if direction == "Left":
        left.append(0)
    elif direction == "Right":
        right.append(disk_size - 1)

    for i in range(len(arr)):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    left.sort()
    right.sort()

    run = 2
    while run != 0:
        if direction == "Left":
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track

            direction = "Right"

        elif direction == "Right":
            for i in range(len(right)):
                cur_track = right[i]
                seek_sequence.append(cur_track)
                distance = abs(cur_track - head)
                seek_count += distance
                head = cur_track

            direction = "Left"

        run -= 1

    result_label.config(text=f"Total number of seek operations = {seek_count}\nSeek Sequence is\n{', '.join(map(str, seek_sequence))}")

# Create the main window
root = tk.Tk()
root.title("SCAN Algorithm")

# Create and place GUI elements
tk.Label(root, text="Enter request array (space-separated):").pack()
numbers_entry = tk.Entry(root)
numbers_entry.pack()

tk.Label(root, text="Enter initial head position:").pack()
head_entry = tk.Entry(root)
head_entry.pack()

direction_var = tk.StringVar(root)
direction_var.set("Left")  # Default value
tk.Label(root, text="Select initial direction:").pack()
direction_menu = tk.OptionMenu(root, direction_var, "Left", "Right")
direction_menu.pack()

search_button = tk.Button(root, text="Run SCAN Algorithm", command=scan_algorithm)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()