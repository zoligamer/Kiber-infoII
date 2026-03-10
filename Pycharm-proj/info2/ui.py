import tkinter as tk

import socket
import threading


class Connection:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_connected = False

    def connect(self):
        try:
            self.sock.connect((self.ip, self.port))
            self.is_connected = True
            print(f"Connected to {self.ip}:{self.port}")
        except Exception as e:
            print(f"Connection failed: {e}")

    def send(self, msg):
        if self.is_connected:
            # Strings must be encoded to bytes before sending
            self.sock.sendall(msg.encode('utf-8'))

    def recv(self, callback):
        """Starts a background thread to listen for data."""

        def listen():
            while self.is_connected:
                try:
                    # Buffer size 1024 bytes
                    data = self.sock.recv(1024)
                    if not data:
                        break

                    # Decode bytes to string and trigger the callback
                    decoded_msg = data.decode('utf-8')
                    callback(decoded_msg)
                except Exception as e:
                    print(f"Receive error: {e}")
                    break

            self.is_connected = False
            self.sock.close()

        # daemon=True ensures the thread dies when the main program exits
        thread = threading.Thread(target=listen, daemon=True)
        thread.start()


# --- Example Usage ---
def handle_response(text):
    print(f"Server says: {text}")


if __name__ == "__main__":
    # Note: You'll need an active server at this address to test
    conn = Connection("127.0.0.1", 8080)
    conn.connect()

    # Start listening
    conn.recv(handle_response)

    # Send a message
    conn.send("Hello Server!")

import tkinter as tk
from tkinter import ttk, scrolledtext


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Alapbeállítások
        self.title("Socket Tester v1.0")
        self.geometry("500x600")
        self.configure(padx=10, pady=10)

        self._init_ui()

    def _init_ui(self):
        # 1. CSATLAKOZÁS SZEKCIÓ (Connection)
        conn_frame = tk.LabelFrame(self, text=" Csatlakozás ", padx=10, pady=10)
        conn_frame.pack(fill="x", pady=5)

        tk.Label(conn_frame, text="IP:").grid(row=0, column=0, sticky="w")
        self.ip_entry = tk.Entry(conn_frame)
        self.ip_entry.insert(0, "127.0.0.1")
        self.ip_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(conn_frame, text="Port:").grid(row=0, column=2, sticky="w")
        self.port_entry = tk.Entry(conn_frame, width=10)
        self.port_entry.insert(0, "8080")
        self.port_entry.grid(row=0, column=3, padx=5, pady=2)

        self.connect_btn = tk.Button(conn_frame, text="Kapcsolódás", bg="#4CAF50", fg="white", command=self.on_connect)
        self.connect_btn.grid(row=0, column=4, padx=10)

        # 2. ÜZENETKÜLDÉS SZEKCIÓ (Sending)
        send_frame = tk.LabelFrame(self, text=" Üzenet küldése ", padx=10, pady=10)
        send_frame.pack(fill="x", pady=5)

        self.msg_entry = tk.Entry(send_frame)
        self.msg_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        send_btn = tk.Button(send_frame, text="Küldés", width=10, command=self.on_send)
        send_btn.pack(side="right")

        # 3. NAPLÓ/VÁLASZOK (Logs/Receiver)
        log_frame = tk.LabelFrame(self, text=" Log / Beérkező adatok ", padx=10, pady=10)
        log_frame.pack(fill="both", expand=True, pady=5)

        self.log_area = scrolledtext.ScrolledText(log_frame, state='disabled', height=10)
        self.log_area.pack(fill="both", expand=True)

        # Státuszsor
        self.status_label = tk.Label(self, text="Állapot: Nincs kapcsolódva", bd=1, relief="sunken", anchor="w")
        self.status_label.pack(fill="x", side="bottom", pady=(5, 0))

    def log(self, message):
        """Segédfüggvény a naplózáshoz"""
        self.log_area.configure(state='normal')
        self.log_area.insert(tk.END, f"{message}\n")
        self.log_area.configure(state='disabled')
        self.log_area.see(tk.END)

    def on_connect(self):
        # Ide jön majd a Connection class hívása
        self.log(f"Csatlakozás megkísérelve: {self.ip_entry.get()}:{self.port_entry.get()}")
        self.status_label.config(text="Állapot: Kapcsolódás...")

    def on_send(self):
        msg = self.msg_entry.get()
        if msg:
            self.log(f"Saját: {msg}")
            self.msg_entry.delete(0, tk.END)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()