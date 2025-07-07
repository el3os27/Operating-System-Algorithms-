import tkinter as tk
from tkinter import ttk

class NaryTree:
    def __init__(self):
        self.isLock = False
        self.isLockable = True
        self.parent = None
        self.children = []

    def is_locked(self):
        return self.isLock

    def lock(self, node):
        if node.isLockable is False:
            return
        T = node
        flag = False
        while T is not None:
            if T.isLock is True:
                flag = True
                break
            T = T.parent
        if flag:
            return
        else:
            node.isLock = True
            T = node
            while T is not None:
                T.isLockable = False
                T = T.parent

    def unlock(self, node):
        if node.isLock is False:
            return
        T = node
        node.isLock = False
        while T is not None:
            T.isLockable = True
            T = T.parent

# Create the main window
root = tk.Tk()
root.title("Nary Tree Locking")

# Create and place GUI elements
tree = NaryTree()

# Create a tree structure similar to the provided example
t1 = NaryTree()
t1.parent = tree
t2 = NaryTree()
t2.parent = tree
t3 = NaryTree()
t3.parent = tree

tree.children.append(t1)
tree.children.append(t2)
tree.children.append(t3)

t5 = NaryTree()
t5.parent = tree.children[0]
tree.children[0].children.append(t5)
t4 = NaryTree()
t4.parent = tree.children[1]
tree.children[1].children.append(t4)

# Function to handle button click and lock/unlock the selected node
def handle_lock_unlock():
    selected_node = tree_combobox.get()
    if selected_node:
        selected_node = eval(selected_node)  # Convert the string to the actual object
        if lock_unlock_var.get() == "Lock":
            tree.lock(selected_node)
        elif lock_unlock_var.get() == "Unlock":
            tree.unlock(selected_node)
        update_lock_status(selected_node)

# Function to update the lock status label
def update_lock_status(node):
    lock_status_label.config(text=f"{node} is locked: {node.is_locked()}")

# Create a ComboBox to select a node
tk.Label(root, text="Select Node:").pack()
tree_combobox = ttk.Combobox(root, values=["tree", "t1", "t2", "t3", "t4", "t5"])
tree_combobox.pack()

# Create a ComboBox to select lock or unlock
tk.Label(root, text="Select Action:").pack()
lock_unlock_var = tk.StringVar(root)
lock_unlock_var.set("Lock")  # Default value
lock_unlock_menu = ttk.Combobox(root, textvariable=lock_unlock_var, values=["Lock", "Unlock"])
lock_unlock_menu.pack()

# Button to trigger the lock/unlock action
lock_unlock_button = tk.Button(root, text="Lock/Unlock", command=handle_lock_unlock)
lock_unlock_button.pack()

# Label to display lock status
lock_status_label = tk.Label(root, text="")
lock_status_label.pack()

root.mainloop()
