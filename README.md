# Morse Code Converter and Inverter

A web application built with Flask that allows users to convert text to Morse code and invert Morse code back to text.

## Features

* Convert text to Morse code
* Invert Morse Code back to text
* User-friendly web interface

## Screenshoots

## Getting Started

Follow these instructions to set up and run the project locally on your machine.

### Prequisites

Ensure you have the following installed:
- Python 3.8.19
- or install the **requirements.txt**

### Installation
1. **Clone the repository**:

    ```bash
    git clone https://github.com/kelvinjuliusarmandoh/morse-code-converter.git
    cd morse-code-converter
    ```
2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```
### Running the Application

1. **Set the FLASK_APP environment variable**:

    ```bash
    export FLASK_APP=app.py  # On Windows use `set FLASK_APP=app.py`
    ```
    
2. **Run the Flask application**:

    ```bash
    flask run
    ```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the application.
   
## Usage

1. Navigate to the home page.
2. Enter the text you want to convert to Morse code or the Morse code you want to invert.
3. Click the appropriate button to get the result.

## Project Structure
```
morse-code-converter/
├── app.py # Main application file
├── requirements.txt # Python dependencies
├── templates/ # HTML templates
│ ├── base.html
│ ├── index.html
├── static/ # Static files (CSS, JS, images)
│ ├── css/
│ │ └── styles.css
│ ├── js/
│ │ └── scripts.js
├── screenshots/ # Screenshots for README
│ └── home_page.png
└── README.md # Project README file
```
