


#  DripFile

**DripFile** is a lightweight Flask web app for quick, temporary file sharing.  
Users can upload a file and instantly get a sharable download link that automatically expires after 15 minutes.  

>  Built with Flask · Deployed on Vercel

---

##  Demo

**Live App:** [https://dripfile.vercel.app/](https://dripfile.vercel.app/)  


---

##  Features

-  Upload files up to **25 MB**
-  Instantly generates a **unique shareable link**
-  Links automatically expire after **15 minutes**
-  Background thread **cleans up expired files**
-  Simple, modern UI with responsive design

---

##  Project Structure

```

DripFile/
├── app.py               # Flask backend
├── requirements.txt     # Dependencies
├── templates/
│   └── index.html       # Upload page
└── venv/                # Virtual environment (optional)

````

---

##  Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (Vanilla)
- **Server:** Vercel (WSGI)

---
## Screenshots
<img width="1704" height="956" alt="Screenshot 2025-11-10 at 01 07 37" src="https://github.com/user-attachments/assets/b21a604b-a5df-495e-b5cd-032948b71041" />

---

## Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/DripFile.git
cd DripFile
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app locally

```bash
python app.py
```

Then open:  `http://127.0.0.1:5000/`

---



##  How It Works

1. User uploads a file → stored in `uploads/`
2. Server generates a random 8-character ID
3. Temporary link is returned (e.g. `/aB7x2YkP`)
4. Background thread deletes expired files every 60 seconds

---

##  Cleanup Mechanism

A daemon thread runs in the background and removes:

* Files older than `15 minutes`
* Corresponding entries from the in-memory `file_links` dictionary

This ensures the app stays lightweight and clean.

---

##  License

MIT License © 2025 DripFile





