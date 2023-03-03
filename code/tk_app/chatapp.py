import socket
import threading
import tkinter as tk

def send_message():
    message = message_box.get()
    message_box.delete(0, tk.END)
    client_socket.send(message.encode())

def receive_message():
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                message_listbox.insert(tk.END, message.decode())
        except:
            break
    client_socket.close()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8080))

root = tk.Tk()
root.title("Chat App")

message_listbox = tk.Listbox(root, width=50, height=20)
message_listbox.pack()

message_frame = tk.Frame(root)
message_frame.pack(side=tk.BOTTOM)

message_box = tk.Entry(message_frame, width=50)
message_box.pack(side=tk.LEFT)

send_button = tk.Button(message_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

root.mainloop()
