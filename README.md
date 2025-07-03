# Password Cracker - Created by Suvam

This project is a **Graphical User Interface (GUI) tool to brute-force protected files using a wordlist.**
It supports cracking passwords for:
- `.zip`
- `.pdf`
- `.docx` and `.xlsx`
- `.7z`

It displays live progress, logs each attempted password, and shows the found password with a convenient copy-to-clipboard option.

---

## 📦 Features
✅ Supports multiple formats: ZIP, PDF, DOCX/XLSX, 7Z  
✅ Easy-to-use GUI built with `tkinter`  
✅ Live progress bar and log  
✅ Copy cracked password to clipboard  
✅ Status messages for success and failure  
✅ Designed & Created by Suvam

---

## 🧰 Libraries Used
- `tkinter` (standard Python GUI library)
- `threading` & `queue` (standard Python)
- `pyzipper` — for AES-encrypted ZIP files
- `pikepdf` — for PDF files
- `msoffcrypto` — for MS Office DOCX/XLSX files
- `py7zr` — for 7-Zip archives

---

## 🚀 Installation

### 1️⃣ Clone or download this repository
```
https://github.com/Ninja-Atmos/Password-Cracker.git
```

### 2️⃣ Install Python dependencies
Ensure you have Python 3.x installed. Then run each of the following commands one by one:
```
pip install pyzipper
```
```
pip install pikepdf
```
```
pip install msoffcrypto-tool
```
```
pip install py7zr
```
### 3️⃣ Run the program
```
python password_cracker.py
```

---

## 📄 How to Use
✅ Run the program — a clean, user-friendly GUI window will open. You don’t need to type commands in the terminal after this.

✅ In the GUI, click the `Browse` button next to **Protected File** and select the file you want to crack (.zip, .pdf, .docx, .xlsx, or .7z).

✅ Next, click the `Browse` button next to **Wordlist File** and select your wordlist text file (should contain one possible password per line).

✅ Click the `Start Cracking` button. The program will begin trying each password in your wordlist.

✅ While scanning, the **log window** will show each password being tried, and the **progress bar** below it will fill as it goes through the wordlist.

✅ Once the correct password is found, a popup will appear showing the password, with a button you can click to copy it directly to your clipboard.

✅ If no password is found after scanning all words, an error popup will inform you.

---

## 🔗 Notes
- The cracking is **wordlist-based**: it can only find passwords that exist in your wordlist.
- `.rar` is currently **not supported** — you can extend it later.
- For better results, use a large wordlist (like `rockyou.txt`) open this link and download the rockyou.txt 👇👇
---
---
https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt
---



✅ Created with ❤️ by **Suvam**  
Feel free to contribute & improve!
