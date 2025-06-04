# 🕵️ IP Logger Flask App

A minimal Python Flask application to demonstrate the Ip logging that logs information about incoming visitors such as their IP address, user-agent, referrer, and access time.

## 🚀 Features

- Logs the visitor’s:
  - IP Address
  - User-Agent
  - Referrer (if available)
  - Access Timestamp
- Simple HTML response page
- Logs are saved to `log.txt`
- Modular class-based design.

## 📁 Project Structure
```
.
├── iplogger.py          # Main application
├── log.txt              # File where logs are saved (auto-created)
└── templates/
    └── index.html       # HTML page served on visiting /

```

## 🛠️ Requirements

- Python 3.x
- Flask
  
## 🛠️Installation 
- Step 1:
- Clone the repo
```
git clone https://github.com/pevinkumar10/ip-logger.git
```
- Step 2:
- Go to the directory:
```
cd ip-logger
```
- Step 3:
- Install requirements 
```
pip3 install flask
```
or 

```
pip3 install -r requirements.txt
```
## 🧪 Usage:

```bash

python3 iplogger.py

```
Visit: http://localhost:5000

Each time you refresh the page or open the page your information will be appended to log.txt like this:

```yaml

[2025-06-04 00:15:22] IP: 127.0.0.1, User-Agent: Mozilla/5.0 ..., Referrer: No Referrer
```

## ⚠️ Disclaimer

This tool is for educational purpose only and can be used to understand how the ip loggers works and not for any other purpose.

## 📄 License

[MIT](./LICENSE)
