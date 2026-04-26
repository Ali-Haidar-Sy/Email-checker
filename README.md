<p align="center">
  <pre>
██████╗  █████╗ ██████╗ ██╗██████╗     ███████╗███╗   ███╗ █████╗ ██╗██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗    ██╔════╝████╗ ████║██╔══██╗██║██║
██████╔╝███████║██████╔╝██║██║  ██║    █████╗  ██╔████╔██║███████║██║██║
██╔══██╗██╔══██║██╔══██╗██║██║  ██║    ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║
██████╔╝██║  ██║██║  ██║██║██████╔╝    ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝     ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
      ███████╗███╗   ███╗ █████╗ ██╗██╗         ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
      ██╔════╝████╗ ████║██╔══██╗██║██║        ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
      █████╗  ██╔████╔██║███████║██║██║        ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
      ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║        ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
      ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗   ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
      ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
  </pre>
</p>

<h1 align="center">📬 Barid Email Checker</h1>

<p align="center">
  <strong>Simple Python script that checks if an email exists on the <code>barid.site</code> temporary mail service.</strong><br>
  <em>Educational project – learn about API interaction and email verification.</em>
</p>

<p align="center">
  <a href="https://github.com/Ali-Haidar-Sy/Email-checker/stargazers"><img src="https://img.shields.io/github/stars/Ali-Haidar-Sy/Email-checker?style=for-the-badge&color=yellow"></a>
  <a href="https://github.com/Ali-Haidar-Sy/Email-checker/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Ali-Haidar-Sy/Email-checker?style=for-the-badge&color=blue"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="https://t.me/P33_9"><img src="https://img.shields.io/badge/Telegram-@P33_9-2CA5E0?style=for-the-badge&logo=telegram"></a>
  <a href="https://www.instagram.com/_ungn"><img src="https://img.shields.io/badge/Instagram-@_ungn-E4405F?style=for-the-badge&logo=instagram"></a>
  <a href="https://github.com/Ali-Haidar-Sy"><img src="https://img.shields.io/badge/GitHub-Ali--Haidar--Sy-181717?style=for-the-badge&logo=github"></a>
</p>

---

## 📧 What It Does

- Displays a colourful table of **temporary email domains** supported by the service.
- Asks you to enter an **email address** (e.g., `someone@guns.lat`).
- Hits the `api.barid.site` endpoint to check if that email exists / has messages.
- Prints whether the email is **valid (Good ✅)** or **not (Bad ❌)**.

---

## ⚡ Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Ali-Haidar-Sy/Email-checker.git
cd Email-checker

# 2. Install requirements (only termcolor is needed – script will auto‑install it)
pip install termcolor

# 3. Run the script
python barid_checker.py
Then, when prompted, enter a full email address (e.g., test@leala.site) – the tool will immediately tell you if it exists on the service.

📦 Dependencies
Library	Purpose
requests	HTTP requests to the API
termcolor	Coloured terminal output
os, json	Standard library (system calls, JSON parsing)
Note: The script attempts to install termcolor automatically using os.system('pip install termcolor'). On some systems you may need to run pip install termcolor manually first.

🔎 How It Works
Domain Table – prints a formatted box with all known domains used by barid.site.

User Input – waits for you to type an email.

API Request – calls https://api.barid.site/emails/{email} with the necessary headers and parameters.

Response Parsing – checks if success is True in the JSON response.

Result – shows Good Email ✅ or Bad Email ❌.

⚠️ Ethical & Legal Notice
This tool interacts with a third‑party temporary email service.

Do not use it to spam, harass, or violate any platform’s Terms of Service.

It is provided for educational purposes only – to understand how APIs work and how email verification can be performed.

The author is not responsible for any misuse.

🛡️ Disclaimer
text
This project is not affiliated with barid.site or any associated services.
All trademarks belong to their respective owners.
🤝 Contributing
Pull requests are welcome! If you find a bug or have a suggestion, open an issue first to discuss what you would like to change.

📞 Connect With Me
Platform	Handle
GitHub	Ali-Haidar-Sy
Telegram	@P33_9
Instagram	@_ungn
<p align="center"> <strong>📬 Simple, fast, educational. Star it if it helped you!</strong> </p> ```
---

## ⚡ Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/barid-email-checker.git
cd barid-email-checker

# 2. Install requirements (only termcolor is needed)
pip install termcolor

# 3. Run the script
python barid_checker.py
Then, when prompted, enter a full email address (e.g., test@leala.site) – the tool will immediately tell you if it exists on the service.

📦 Dependencies
Python 3.7+

termcolor (for coloured terminal output)

requests

Note: The script will attempt to install termcolor automatically using os.system('pip install termcolor'). On some systems you may need to run it manually first.

🔎 How It Works
Domain Table – prints a formatted box with all known domains used by barid.site.

User Input – waits for you to type an email.

API Request – calls https://api.barid.site/emails/{email} with the necessary headers and parameters.

Response Parsing – checks if success is True in the JSON response.

Result – shows Good Email ✅ or Bad Email ❌.

⚠️ Ethical & Legal Notice
This tool interacts with a third‑party temporary email service.

Do not use it to spam, harass, or violate any platform’s Terms of Service.

It is provided for educational purposes only – to understand how APIs work and how email verification can be performed.

The author is not responsible for any misuse.

🛡️ Disclaimer
text
This project is not affiliated with barid.site or any associated services.
All trademarks belong to their respective owners.
🤝 Contributing
Pull requests are welcome! If you find a bug or have a suggestion, open an issue first to discuss what you would like to change.

📞 Connect With Me
Platform	Handle
GitHub	Ali-Haidar-Sy
Telegram	@P33_9
Instagram	@_ungn
<p align="center"> <strong>📬 Simple, fast, educational. Star it if it helped you!</strong> </p> ```
