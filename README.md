# Employee Shift Report

This script processes an employee's work schedule, comparing their clock-in and clock-out times with the expected schedule. It generates reports for any discrepancies, such as missing clock-ins, clock-out times, and time mismatches.

## Requirements

- Python 3.x
- `datetime` library (usually comes pre-installed with Python)

## How It Works

1. **Input Schedule**: The `EXPECTED_SCHEDULE` dictionary contains the expected clock-in and clock-out times for each day of the week.
   - If an employee is not scheduled to work on a particular day, the value is set to `(None, None)`.

2. **Shift Data**: The script uses shift data from a JSON structure, with clock-in and clock-out times for each shift.
   - Each shift is linked to a date, and it contains information like the employee's first and last names, shift ID, and hours worked.
   - Important: In the json_body, if there is any occurrence of null, replace it with None (Python's equivalent of null).

3. **Date Range**: The script checks for shifts between a given start and end date (`date_range_start` and `date_range_end`).

4. **Shift Validation**:
   - For each day in the date range, it checks if the employee was expected to work.
   - If the employee worked on a day they weren't scheduled to, it generates a report.
   - If the employee didn't clock in on a scheduled day, it generates a report.
   - It checks for time mismatches in clock-in and clock-out times, and reports late/early arrivals and departures.

## Functions

### `calculate_time_diff(start_time, end_time)`

Calculates the time difference between two datetime objects and returns the difference in hours, minutes, and seconds.

**Parameters:**
- `start_time`: A datetime object representing the start time.
- `end_time`: A datetime object representing the end time.

**Returns:**
- A tuple `(hours, minutes, seconds)` representing the difference between the two times.

## Main Script Logic

The script compares the actual clock-in and clock-out times for each day within a given date range against the `EXPECTED_SCHEDULE`. It checks the following conditions:

- If the employee worked on a day that is scheduled as off (`None, None`), it generates a report.
- If the employee missed a clock-in or clock-out time, it generates a report.
- If there is a mismatch in clock-in or clock-out times, it calculates the time difference and adds the report accordingly.

### Date Range:

The `start_date` and `end_date` are derived from the `date_range_start` and `date_range_end` fields in `json_body`.

### Shift Checking:

The script iterates through each day in the date range and checks the shift data for that day. If the employee’s clock-in or clock-out time deviates from the expected schedule, a report is generated.

## Usage

1. Clone or download this repository.
2. Ensure Python 3.x is installed.
3. Modify the `EXPECTED_SCHEDULE` and `json_body` as needed for the employee and date range.
4. Run the script:

    ```bash
    python Time-Mismatch.py
    ```

## Output

The script will print the generated reports to the console, highlighting any mismatches or missed clock-in/out actions, as well as identifying if the employee worked on a scheduled off day.

### Example Output:

    
    Worked on Tuesday 11, February 2025 when not scheduled.
    Time mismatch on Wednesday 12, February 2025: Clocked in late by 4 hrs 59 mins 0 secs.
    Time mismatch on Wednesday 12, February 2025: Clocked out late by 2 hrs 0 mins 0 secs.
    Didn't clock in on Monday 17, February 2025
    Worked on Thursday 27, February 2025 when not scheduled.
    Didn't clock in on Friday 28, February 2025
    Didn't clock-out on Friday 7, March 2025.
    

## Customization

- You can modify the `EXPECTED_SCHEDULE` to match your organization's work schedule.
- You can update the `json_body` with the actual shift data.
- The date range in `date_range_start` and `date_range_end` can be adjusted as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

