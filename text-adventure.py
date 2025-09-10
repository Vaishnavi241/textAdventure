import tkinter as tk
from tkinter import messagebox

rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dining Room'
    }
}

inventory = []
current_room = 'Hall'

def show_status():
    status = f"You are in the {current_room}\n"
    status += f"Inventory: {', '.join(inventory) if inventory else 'Empty'}\n"
    if "item" in rooms[current_room]:
        status += f"You see a {rooms[current_room]['item']}\n"
    return status

def process_command():
    global current_room
    command = entry.get().lower().split()
    output = ""

    if len(command) < 2:
        output = "Invalid command. Use 'go [direction]' or 'get [item]'."
    else:
        action, target = command[0], command[1]

        if action == 'go':
            if target in rooms[current_room]:
                current_room = rooms[current_room][target]
            else:
                output = "You can't go that way!"

        elif action == 'get':
            if "item" in rooms[current_room] and rooms[current_room]['item'] == target:
                inventory.append(target)
                output = f"{target} picked up!"
                del rooms[current_room]['item']
            else:
                output = f"Can't get {target}!"

        elif action == 'quit':
            root.quit()
    if "item" in rooms[current_room] and rooms[current_room]["item"] == "monster":
        messagebox.showerror("Game Over", "A monster got you! Game Over!")
        root.quit()

    if current_room == "Garden" and "key" in inventory and "potion" in inventory:
        messagebox.showinfo("Victory", "You escaped the house with the key and potion... YOU WIN!")
        root.quit()
    status_label.config(text=show_status() + "\n" + output)
    entry.delete(0, tk.END)
root = tk.Tk()
root.title("🧭 textAdventure")
root.geometry("600x300")
root.configure(bg="#1e1e2f")
title = tk.Label(root, text="Text Adventure Game", font=("Courier", 18, "bold"), fg="lightgreen", bg="#1e1e2f")
title.pack(pady=10)
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10, padx=10, fill="both", expand=True)
status_label = tk.Label(frame, text=show_status(), justify="left", font=("Courier", 12), bg="#1e1e2f", fg="white", anchor="w")
status_label.pack(fill="both", pady=5)
entry = tk.Entry(root, width=50, font=("Courier", 12))
entry.pack(pady=5)
submit_btn = tk.Button(root, text="Submit Command", command=process_command, font=("Courier", 12), bg="#2d2d3c", fg="white")
submit_btn.pack(pady=10)
root.mainloop()
