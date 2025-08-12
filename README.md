# Web Scraping with Selenium

Welcome to the SICSS Web Scraping Workshop! In this exercise, you'll learn how to use Selenium to automate web browsers and extract data from websites. This repository contains all the code and instructions you'll need to get started.

## Prerequisites

Before you begin, make sure you have:
- Python 3.10 or newer installed
- Google Chrome browser installed
- Git installed (to clone the repository)

## Getting Started

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/sicss-web-scraping.git
   cd sicss-web-scraping
   ```

2. **Set up the virtual environment**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   # python -m venv venv
   # venv\Scripts\activate
   ```

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```
   
   This will automatically install:
   - Selenium for web automation
   - WebDriver Manager for handling ChromeDriver
   - Pandas for data manipulation
   - BeautifulSoup for HTML parsing

4. **Run the example script**
   ```bash
   python scrape.py
   ```
   
   The script will prompt you to enter a search query and then display the top search results from Google.

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
