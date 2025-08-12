# Web Scraping with Selenium

Welcome to the SICSS Web Scraping Workshop! In this exercise, you'll learn how to use Selenium to automate web browsers and extract data from websites. This repository contains all the code and instructions you'll need to get started.

## Prerequisites

### 1. Install Python 3.10 or Newer

You'll need Python installed to run the web scraping script.

#### macOS

##### Option A — Direct from Python.org

1. Download the latest Python from [python.org/downloads/macos/](https://www.python.org/downloads/macos/)
2. Run the installer with default settings
3. Verify installation in Terminal:
   ```bash
   python3 --version
   ```
   Should show: `Python 3.x.x`

##### Option B — Using Homebrew
   ```bash
brew install python
python3 --version
```

#### Windows

1. Download Python from [python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Verify in Command Prompt:
   ```cmd
   python --version
   ```

   You should see:

   ```
   Python 3.12.5
   ```

   If you get an error like “python is not recognized,” the PATH step was missed — reinstall and make sure **Add Python to PATH** is checked.


### Linux (Debian/Ubuntu)

   ```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version
```

You should see something like:

```
Python 3.12.5
```

## 2) Create a Project Folder

We’ll keep all files for this project in one place.

```bash
mkdir selenium-scraping
cd selenium-scraping
```

---

## 3) Create & Activate a Virtual Environment

A **virtual environment** keeps the project’s packages separate from the rest of your computer.

```bash
python3 -m venv .venv
```

### Activate the virtual environment:

* **macOS / Linux**

  ```bash
  source .venv/bin/activate
  ```

  Your prompt should now show `(.venv)` at the start.

* **Windows (PowerShell)**

  ```powershell
  .venv\Scripts\Activate.ps1
  ```

  Your prompt should now show `(.venv)` at the start.

If activation fails on Windows with a “running scripts is disabled” error:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then run the activation command again.

---

## 4) Install Selenium

```bash
python -m pip install --upgrade pip
pip install selenium
```

To confirm Selenium is installed:

```bash
pip show selenium
```

You should see something like:

```
Name: selenium
Version: 4.23.1
```

---

## 5) Test Selenium with Chrome (Headless)

1. Create a file called `test_selenium.py` in your project folder.
2. Paste this code:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")  # run without opening a browser window
driver = webdriver.Chrome(options=options, service=Service())

driver.get("https://example.org")
print("Page title:", driver.title)

driver.quit()
```

3. Run it:

```bash
python test_selenium.py
```

You should see:

```
Page title: Example Domain
```
