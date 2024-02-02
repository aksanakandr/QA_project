# Python Selenium Automation Project

This project uses Selenium  and Python, Pytest

## Table of Contents

1. Prerequisites
2. Setup and Installation
3. Running Tests
4. Changing browsers

## Prerequisites <a name="prerequisites"></a>

Ensure you have the following installed on your local machine:

- Python (3.6 or higher)
- pip (Python package installer)

## Setup and Installation <a name="setup-and-installation"></a>

Follow these steps to set up and run the project:

1. **Environment Setup**:
   If you're using an IDE that handles virtual environments, you can skip this step. If not, you'll need to set up a Python virtual environment. Here's how you can do it:

   ```bash
   python3 -m venv env
   source env/bin/activate
2. **Setup and Installation**:
   Use pip to install the required packages. Run the following command:
    ```bash
   pip install -r requirements.txt
3. **Running tests**:
   Use pytest to run the tests. Here’s the command:
   ```bash
    pytest .\tests
4. **Changing browsers**: 
   In the `base_test.py` file, you need to modify the `browser` variable according to your preference. You have two options:

   1. **Chrome**: If you want to use Google Chrome for your tests, set the `browser` variable to 'Chrome'.
   2. **Firefox**: If you prefer using Mozilla Firefox, set the `browser` variable to 'Firefox'.
