# 📱 Appium Android Automation – Eeki Foods

This project automates form submissions on the Eeki Foods Android application using Appium with Python. The script launches the app, navigates to a specific section ("Media Moisture"), and inputs 50 sets of values into the form fields.

---

## 🚀 Features

- Connects to Android devices using Appium
- Automatically fills:
  - Dome
  - Section
  - EC
  - Moisture
  - Temperature
- Submits the form once after 50 entries
- Includes smart waits and error handling

---

## 🧰 Tech Stack

- [Appium](https://appium.io/)
- [Selenium](https://www.selenium.dev/)
- Python 3.8+

---

## 🖥️ Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
Create requirements.txt using:

bash
Copy
Edit
pip freeze > requirements.txt
📲 How to Use
Ensure Appium server is running
You can use Appium Server GUI or start via CLI:

bash
Copy
Edit
appium
Connect Android device via USB and enable developer mode + USB debugging.

Run the script from your virtual environment:

bash
Copy
Edit
python script.py
🧪 Script Behavior
Navigates to Media Moisture section

Clicks on + button

Fills the form 50 times with incrementing values

Submits the final record

Waits between steps to ensure app responsiveness

📂 File Structure
bash
Copy
Edit
├── script.py              # Main Appium test script
├── requirements.txt       # Python dependencies
├── README.md              # You're reading it!
└── .gitignore             # Ignore venv, __pycache__, etc.
📝 Author
Dnyaneshwar Karad
✉️ GitHub Profile

🛠️ Notes
Make sure the device screen is on and unlocked.

App package and activity names may need updating if the app changes.

XPath values were used due to lack of stable resource IDs.

