\# Hash Cracker (Educational)



A simple password hash cracker to understand why weak passwords fail.



\*\*⚠️ For educational purposes only. Do not use for unauthorized access.\*\*



\## What It Does



\- Takes a hashed password (MD5 or SHA256)

\- Attempts to crack it using a wordlist (e.g., rockyou.txt)

\- Shows how quickly weak passwords can be cracked



\## Why This Matters



\- Demonstrates why simple passwords are vulnerable

\- Shows how dictionary attacks work

\- Explains why salting and strong hashing algorithms matter



\## How Hashing Works

```

password123 → MD5 → 482c811da5d5b4bc6d497ffa98491e38

password123 → SHA256 → ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f

```



Hashing is one-way — you can't reverse it. But you can hash common passwords and compare.



\## Usage

```bash

python cracker.py <hash> <algorithm>

```



Examples:

```bash

\# Crack an MD5 hash

python cracker.py 482c811da5d5b4bc6d497ffa98491e38 md5



\# Crack a SHA256 hash

python cracker.py ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f sha256

```



\## Setup



1\. Clone the repo

2\. Download `rockyou.txt` and place in `data/` folder

3\. Run the cracker



\## Project Structure

```

hash-cracker/

├── data/

│   └── rockyou.txt    (not included - download separately)

├── cracker.py

├── README.md

├── requirements.txt

├── LICENSE

└── .gitignore

```



\## What You Learn



\- MD5 and SHA256 hashing algorithms

\- Dictionary attacks and brute force concepts

\- Why password complexity matters

\- Why salting hashes is important



\## Tech Stack



\- Python (standard library only)

\- hashlib module



\## Legal Disclaimer



This tool is for educational purposes only. Only use on systems you own or have explicit permission to test. Unauthorized access to computer systems is illegal.

