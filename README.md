# Edge Search Bot

## Overview

Edge Search Bot is a powerful tool designed to help you mine Microsoft Rewards using Edge on Windows and Linux. Automate your searches and maximize your rewards effortlessly!

## Installation

To get started, install the required dependency:

```bash
pip install selenium
```

## Usage
### native 
Follow these simple steps to run the bot:

1. **Generate Random Search Prompt:**
    Run the following script to create a random search prompt:
    ```bash
    python py_random.py
    ```

2. **Execute the Bot:**
    Run the bot using the script below:
    ```bash
    python test_webdriver.py
    ```

### docker 
1. **Generate Random Search Prompt:**
    Run the following script to create a random search prompt:
    ```bash
    python py_random.py
    ```

2. **Run The Docker File:**
    Run the docker compose:
    ```bash
    docker compose up -d
    ```
    
3. **Execute the Bot:**
    Run the bot using the script below:
    ```bash
    python bot_main_docker.py
    ```

    - live browser no vnc : http://localhost:7900 (pw : secret)
    - live server docker selenium : http://localhost:4444

## Features

- **Automated Searches:** Save time by automating your search tasks.
- **Random Prompts:** Generate random search prompts to keep your searches unique.
- **Easy to Use:** Simple scripts to get you started quickly.

## Contributing

We welcome contributions! Feel free to submit issues or pull requests to improve the bot.

