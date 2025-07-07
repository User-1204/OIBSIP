# BMI Calculator

This project is a desktop-based Body Mass Index (BMI) Calculator developed using Python's `tkinter` library. It allows users to input their name, weight, and height to calculate their BMI, classify the result into health categories, and receive basic health advice. The application also stores historical data locally in a JSON file and includes an option to export records to a CSV file.


## Features

- Calculates BMI using user input for weight and height.
- Categorizes BMI into health ranges: Underweight, Normal weight, Overweight, Obese.
- Provides relevant health suggestions based on BMI category.
- Stores BMI records locally in a JSON file.
- Displays the five most recent entries for each user.
- Allows exporting a user’s BMI history to a `.csv` file.
- Clean and responsive GUI built with Tkinter.


## How BMI is Calculated

BMI is calculated using the following formula:

```python
BMI = weight (kg) / (height (m) × height (m))
```

### BMI Classification Table

| BMI Range    | Category      |
| ------------ | ------------- |
| Below 18.5   | Underweight   |
| 18.5 – 24.9  | Normal weight |
| 25 – 29.9    | Overweight    |
| 30 and above | Obese         |


## GUI Preview

Below is a screenshot of the application interface:

![BMI Calculator Screenshot](https://github.com/user-attachments/assets/15fc62bd-3bf5-4a2f-8282-14e551da9407)


## Sample Output

```
Name: Alex
Weight: 72.0 kg
Height: 1.75 m

BMI: 23.51
Category: Normal weight

Great job. Maintain your healthy habits.

Recent Entries:
Jul 07, 07:02 PM: BMI 23.51 (Normal weight)
Jul 07, 06:50 PM: BMI 26.43 (Overweight)
Jul 07, 06:32 PM: BMI 19.85 (Normal weight)
Jul 07, 06:14 PM: BMI 17.92 (Underweight)
Jul 07, 05:58 PM: BMI 30.76 (Obese)
```


## Requirements

- Python 3.6 or higher
- Tkinter (included by default with most Python installations)


## How to Run

1. Clone or download this repository.

2. Open a terminal and navigate to the project folder.

3. Run the application with:

```bash
python Code.py
```

4. Enter your name, weight (in kilograms), and height (in meters).

5. Click on **Calculate BMI** to view your result and save the record.

6. Use **Export to CSV** to generate a file like `bmi_export_<yourname>.csv`.


## File Descriptions

| File                    | Description                                        |
| ----------------------- | -------------------------------------------------- |
| `Code.py`               | Main Python script containing the application code |
| `bmi_data.json`         | Local JSON storage for user BMI history            |
| `bmi_export_<name>.csv` | CSV file generated on export                       |


## Notes

- Input height in **meters** (e.g., `1.62`) not centimeters.
- Valid weight range is 10–300 kg; valid height range is 0.5–2.5 meters.
- All data is stored locally. No internet connection is required.
