


#  DripFile

**DripFile** is a lightweight Flask web app for quick, temporary file sharing.  
Users can upload a file and instantly get a sharable download link that automatically expires after 15 minutes.  

>  Built with Flask · Deployed on PythonAnywhere

---

##  Demo

**Live App:** [https://nilanshucodes.pythonanywhere.com](https://nilanshucodes.pythonanywhere.com)  


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
- **Server:** PythonAnywhere (WSGI)

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

## ☁️ Deployment (PythonAnywhere)

1. Upload project files (`app.py`, `templates/`, `requirements.txt`, `uploads/`)
2. Create a **virtual environment** in Bash console:

   ```bash
   cd ~/DripFile
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Go to **Web tab → Add a new web app → Manual configuration → Python 3.x**
4. Edit the **WSGI file** to point to your app:

   ```python
   import sys
   path = '/home/yourusername/DripFile'
   if path not in sys.path:
       sys.path.append(path)

   from app import app as application
   ```
5. Reload your web app — done 

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

MIT License © 2025 Drip-File





