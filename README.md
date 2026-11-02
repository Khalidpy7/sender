<div align="center">

# ✉️ SENDER

**A simple Python-based Gmail email sender**

[![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)](https://github.com/Khalidpy7/sender)
[![Language](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-green?style=for-the-badge)](https://github.com/Khalidpy7/sender)

*A lightweight command-line project for sending an email through Gmail's SMTP server.*

[Repository](https://github.com/Khalidpy7/sender) · [Report an issue](https://github.com/Khalidpy7/sender/issues)

</div>

---

## Description

**SENDER** is a command-line email-sending tool written in Python. It uses Python's built-in `smtplib` and `email.message` modules to connect securely to Gmail over SMTP SSL, then sends a message to one specified recipient.

The project includes:
- A Python sender program (`sender.py`).
- A Bash launcher (`main.sh`) that checks for Python, installs the listed Python requirements, and starts the program.
- A colored terminal interface powered by `termcolor`.

> **Note:** Despite the “SMS SENDER” startup text in the current script, this project sends **email**, not SMS messages. It sends one email to the recipient entered during a run; it is not a bulk-mailing tool.

## File system

```text
sender/
├── main.sh           # Bash launcher and dependency setup
├── sender.py         # Main Python email-sending program
├── requirements.txt  # Python package dependencies
└── README.md         # Project documentation
```

## Requirements

- Python 3
- Bash
- `pip`
- `termcolor` Python package
- A Gmail account with 2-Step Verification enabled
- A Gmail App Password

### `requirements.txt`

Create a file named `requirements.txt` in the project root:

```text
termcolor
```

`time`, `smtplib`, `email.message`, and `os` are part of Python's standard library, so they should **not** be installed with `pip`.

## Gmail setup

The program authenticates using a Gmail App Password.

1. Enable 2-Step Verification on the Google account you control.
2. Create an App Password in your Google Account security settings, if your account is eligible.
3. Use that App Password when the program prompts for it.

**Security:** Never share your App Password, commit it to GitHub, or paste it into an issue or public chat. Use the tool only with an account you own or are authorized to use, and send messages only to recipients who expect or have agreed to receive them.

## Installation

### Termux (Android)

Clone the repository and enter its directory:

```bash
git clone https://github.com/Khalidpy7/sender.git
cd sender
```

Install the required system packages:

```bash
pkg update
pkg install python git
```

Install the Python dependency:

```bash
pip install -r requirements.txt
```

### Linux

```bash
git clone https://github.com/Khalidpy7/sender.git
cd sender
```

Install Python, pip, and Bash using your distribution's package manager, then run:

```bash
python3 -m pip install -r requirements.txt
```

> `main.sh` currently uses Termux-style `pkg` commands and `dpkg` checks. It is designed around a Termux/Debian-like environment and may need adapting on other Linux distributions.

## How to run

From the project directory:

```bash
bash main.sh
```

Or run the Python program directly:

```bash
python sender.py
```

On some Linux systems, use:

```bash
python3 sender.py
```

### Running the tool

The program asks for:

1. **Gmail App Password** — the App Password for the sender account.
2. **Mail subject** — the subject line.
3. **Sender Gmail** — the Gmail address used to authenticate.
4. **Receiver Gmail** — the intended recipient's email address.
5. **Message** — the body of the email.

After successful SMTP login and sending, the program prints a confirmation message.

## Google Cloud Shell

<a href="https://shell.cloud.google.com/?cloudshell_git_repo=https://github.com/Khalidpy7/sender" target="_blank">
  <img src="https://github.com/Khalidpy7/sender" alt="Open the SENDER GitHub repository in Google Cloud Shell" />
</a>

Open the project in [Google Cloud Shell](https://shell.cloud.google.com/?cloudshell_git_repo=https://github.com/Khalidpy7/sender). Once the repository is cloned in the Cloud Shell terminal, install the dependency and run:

```bash
cd sender
python3 -m pip install -r requirements.txt
python3 sender.py
```

If the repository is already open in Cloud Shell, do not clone it a second time.

## How it works

1. `main.sh` checks whether Python is installed.
2. The launcher installs Python dependencies from `requirements.txt`.
3. `sender.py` displays the banner and usage instructions.
4. The program collects the sender, recipient, subject, App Password, and message.
5. It creates an `EmailMessage` object and fills in its headers and body.
6. It opens an SSL connection to Gmail's SMTP server at `smtp.gmail.com` on port `465`.
7. It logs in and sends the email.

## Important code from `sender.py`

The following is the core email-building and SMTP-sending section from the current project:

```python
from email.message import EmailMessage
import smtplib

# Create the email message
msg = EmailMessage()

# Set the email headers
msg["Subject"] = subject
msg["From"] = sender
msg["To"] = receiver

# Add the message body
msg.set_content(message_to_receiver)

# Connect securely to Gmail SMTP and send
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, APP_PASSWORD)
    server.send_message(msg)
```

The terminal colors are provided by `termcolor`:

```python
from termcolor import colored as cd

print(cd("[*] EMAIL SENDER STARTING.", "yellow", attrs=["bold"]))
```

## Troubleshooting

| Problem | What to check |
|---|---|
| `ModuleNotFoundError: No module named 'termcolor'` | Run `python -m pip install -r requirements.txt`. |
| `python: command not found` | Install Python and try `python3 sender.py` on Linux. |
| Gmail authentication error | Check the sender address and App Password. Do not use your normal Gmail password. |
| Connection error | Check your internet connection and whether SMTP access is available on the network. |
| `pkg: command not found` | `main.sh` uses Termux's `pkg` command; install dependencies manually on that system or adapt the launcher. |

## Current project notes

- The current program sends email through Gmail SMTP; it does not send SMS.
- The script handles one recipient per execution.
- The App Password is currently read with `input()`, so it may be visible while typing. Avoid running it where others can see the terminal. A future improvement would be to use Python's `getpass` module.
- The launcher expects `requirements.txt` to exist in the same directory as `main.sh` and `sender.py`.

## Disclaimer

This project is provided for learning and personal, authorized use. Do not use it for spam, unsolicited bulk messaging, impersonation, or any activity that violates Gmail's terms or applicable laws. You are responsible for how you use the software.

## Author

**Khalid Saif**

- GitHub: [@Khalidpy7](https://github.com/Khalidpy7)
- Project: [sender](https://github.com/Khalidpy7/sender)

---

<div align="center">

**SENDER · Version 1.0.0**

*Built for learning Python, Bash, and SMTP.*

</div>
