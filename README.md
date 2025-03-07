# Time-Mismatch

Employee Time Mismatch

Employee Shift Compliance Report Generator
Overview
The Python script processes employee shift data to determine compliance with an expected work schedule. The script cross-references actual clock-in and clock-out times against the predefined schedule and generates reports on irregularities such as missing shifts, extra or insufficient work hours, and unexpected attendance.

Key Components of the Code

1. Expected Work Schedule (EXPECTED_SCHEDULE)
   A dictionary that defines the expected work hours for each weekday. If an employee is not scheduled to work on certain days, the value is set to (None, None).
2. JSON Shift Data (json_body)
   A JSON object containing the following key details:
   The date range for which the report is generated (date_range_start, date_range_end).
   The employee's shift records under the "shift_array" key, including:
   shift_id: Unique shift identifier.
   employee_clock_in_time: The recorded clock-in time.
   employee_clock_out_time: The recorded clock-out time (may be None if missing).
   shift_sum: Total time worked during the shift.

3. Processing Logic
   Step 1: Extract Shift Data
   The script converts employee_clock_in_time from string format ("February 26, 2025 10:01 am") to a Python datetime.date object for easy lookup.
   A dictionary shift_dates is created, mapping each date to its corresponding shift details.
   Step 2: Iterate Through the Date Range
   The script loops from start_date (2025-02-01) to end_date (2025-02-28), checking each day against the expected schedule.
   The weekday name (e.g., "Monday") is used to determine expected working hours.
   Step 3: Determine Compliance
   For each day:
   If no work is expected but a shift exists → Report unexpected work.
   If work is expected but no shift exists → Report missing clock-in.
   If a shift exists:
   Check for missing clock-out.
   Check for extra or insufficient work time by comparing shift_sum against expected hours.
   Check for time mismatches, such as incorrect clock-in time.
   Step 4: Generate Reports
   Reports are stored in a list of reports with details about each non-compliance issue.
   Finally, the reports are printed.

Potential Issues Detected by the Script
The script flags the following discrepancies:
Unscheduled Work → Employee worked on a day they were not scheduled.
Missed Shifts → Employee did not clock in on a scheduled workday.
Missing Clock-Out → Employee failed to clock out.
Overtime or Underworked Hours → Employee worked more or less than expected.
Time Mismatch → Employee clocked in at a different time than scheduled.

Example Output
For an employee working from 10:00 AM to 2:00 PM on Mondays to Wednesdays, possible outputs might look like:
Worked on Thursday 14, February 2025 when not scheduled.  
Didn't clock in on Monday 17, February 2025  
Missing clock-out on Tuesday 18, February 2025  
Extra time worked on Wednesday 19, February 2025: 15 minutes  
Time mismatch on Monday 24, February 2025

Conclusion
This script effectively validates employee shift data against a predefined schedule, identifying inconsistencies in attendance records. The generated report provides actionable insights for payroll management and HR compliance.
