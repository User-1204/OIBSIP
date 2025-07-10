# Random-Password-Generator

A standalone, user-friendly desktop application built with Python and Tkinter. This tool empowers users to create secure and customizable passwords tailored to individual requirements. Designed with an emphasis on simplicity, reliability, and clear design, it combines practical password generation logic with an intuitive graphical interface.

## Overview

This application allows users to generate random passwords by configuring length and character types (letters, digits, symbols) and by controlling character repetition. Built as a lightweight utility, it is especially suited for anyone seeking to improve password hygiene quickly and easily.

## Key Features

- Adjustable password length to suit different security needs
- Toggle options to include:
  - Uppercase and lowercase letters (AZ-az)
  - Digits (0–9)
  - Special characters (`!@#$%^&*` and more)
- Enable or disable character repetition:
  - When disabled, ensures unique characters up to the maximum feasible length
- Guarantees inclusion of at least one character from each selected category
- One-click copy to clipboard functionality
- Dialog-based feedback and validation for incorrect configurations
- Minimalist, responsive interface designed with a soft color palette and clear typography

## Installation

Make sure you have Python installed (recommended: version 3.6 or higher).

Install the required dependency:

```bash
pip install pyperclip
````

> Note: `tkinter` is included in the standard Python library, so no additional installation is typically required.

## Usage

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run:

```bash
python Code.py
```

4. In the application window:

   * Set your desired password length.
   * Choose which character types to include.
   * Specify whether repetition should be allowed.
   * Click **Generate Password** to produce a password.
   * Click **Copy to Clipboard** to copy it for immediate use.

## Technical Overview

* **Password Logic**: Combines random sampling with validation to ensure all selected character types are represented.
* **Repetition Control**: Detects conflicts when requested length exceeds the unique characters available.
* **Validation**: Uses clear dialog messages to guide users when input is invalid or conflicting.
* **Design**: Built with consistent fonts and a calm pastel background for a pleasant user experience.

## Project Structure

```plaintext
password-generator/
├── Code.py                # Main application file
└── README.md              # Project documentation
```

## Design Principles

* **Clarity**: Simple, guided interface helps avoid user mistakes.
* **Security**: Ensures generated passwords meet chosen criteria.
* **Portability**: No external configuration or database required.
* **Responsiveness**: Immediate feedback on user input and errors.

## Preview


## Future Enhancements

* Dark mode or additional themes
* Option to generate passphrases (multiple words)
* Export generated passwords to a local file
* Additional advanced password policies (e.g., exclude similar characters)
