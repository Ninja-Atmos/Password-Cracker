import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import queue
import pyzipper
import pikepdf
import msoffcrypto
import py7zr

log_queue = queue.Queue()

progress_var = None
progress_bar = None

def update_log_window():
    while not log_queue.empty():
        msg = log_queue.get()
        log_text.insert(tk.END, msg + '\n')
        log_text.see(tk.END)
    root.after(100, update_log_window)

def crack_generic(extract_fn, desc, path, wordlist):
    total = len(wordlist)
    for idx, pwd in enumerate(wordlist, 1):
        log_queue.put(f"Trying: {pwd}")
        progress_var.set(int((idx/total)*100))
        progress_bar.update()
        try:
            extract_fn(path, pwd)
            show_success_popup(pwd)
            return
        except:
            continue
    messagebox.showerror("Failed", f"❌ {desc}: Password not found.")

def show_success_popup(password):
    popup = tk.Toplevel(root)
    popup.title("Password Found")
    tk.Label(popup, text=f"✅ Password found: {password}").pack(pady=10)
    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    tk.Button(popup, text="Copy Password", command=copy_to_clipboard).pack(pady=10)

def crack_zip(path, wordlist):
    def extractor(p, pwd):
        with pyzipper.AESZipFile(p) as zf:
            zf.extractall(pwd=pwd.encode())
    crack_generic(extractor, "ZIP", path, wordlist)

def crack_pdf(path, wordlist):
    def extractor(p, pwd):
        pikepdf.open(p, password=pwd)
    crack_generic(extractor, "PDF", path, wordlist)

def crack_docx(path, wordlist):
    def extractor(p, pwd):
        with open(p, "rb") as f:
            office = msoffcrypto.OfficeFile(f)
            office.load_key(password=pwd)
            with open("decrypted.docx", "wb") as out:
                office.decrypt(out)
    crack_generic(extractor, "DOCX", path, wordlist)

def crack_7z(path, wordlist):
    def extractor(p, pwd):
        with py7zr.SevenZipFile(p, mode='r', password=pwd) as archive:
            archive.extractall()
    crack_generic(extractor, "7Z", path, wordlist)

def start_cracking(file_path, wordlist_path):
    with open(wordlist_path, "r", encoding="latin-1") as f:
        wordlist = [w.strip() for w in f]
    progress_var.set(0)
    progress_bar.update()
    if file_path.endswith(".zip"):
        crack_zip(file_path, wordlist)
    elif file_path.endswith(".pdf"):
        crack_pdf(file_path, wordlist)
    elif file_path.endswith(".docx") or file_path.endswith(".xlsx"):
        crack_docx(file_path, wordlist)
    elif file_path.endswith(".7z"):
        crack_7z(file_path, wordlist)
    else:
        messagebox.showerror("Error", "❌ Unsupported file type.")

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def run():
    file_path = file_entry.get()
    wordlist_path = wordlist_entry.get()
    if not file_path or not wordlist_path:
        messagebox.showwarning("Input Required", "Please select both file and wordlist.")
        return
    log_text.delete(1.0, tk.END)
    threading.Thread(target=start_cracking, args=(file_path, wordlist_path), daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Cracker - Created by Suvam")
    root.geometry("600x480")
    root.resizable(False, False)

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    file_label = tk.Label(frame, text="Protected File:")
    file_label.grid(row=0, column=0, sticky="e")
    file_entry = tk.Entry(frame, width=50)
    file_entry.grid(row=0, column=1, padx=5)
    file_button = tk.Button(frame, text="Browse", command=lambda: browse_file(file_entry))
    file_button.grid(row=0, column=2)

    wordlist_label = tk.Label(frame, text="Wordlist File:")
    wordlist_label.grid(row=1, column=0, sticky="e")
    wordlist_entry = tk.Entry(frame, width=50)
    wordlist_entry.grid(row=1, column=1, padx=5)
    wordlist_button = tk.Button(frame, text="Browse", command=lambda: browse_file(wordlist_entry))
    wordlist_button.grid(row=1, column=2)

    start_button = tk.Button(root, text="Start Cracking", command=run, bg="green", fg="white", padx=10, pady=5)
    start_button.pack(pady=10)

    progress_var = tk.IntVar()
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate", variable=progress_var)
    progress_bar.pack(pady=10)

    log_frame = tk.LabelFrame(root, text="Progress Log", padx=5, pady=5)
    log_frame.pack(fill="both", expand=True, padx=10, pady=10)

    log_text = tk.Text(log_frame, height=10)
    log_text.pack(fill="both", expand=True)

    footer = tk.Label(root, text="Created by Suvam", fg="gray")
    footer.pack(side="bottom", pady=5)

    root.after(100, update_log_window)
    root.mainloop()