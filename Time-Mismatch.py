from datetime import datetime, timedelta

EXPECTED_SCHEDULE = {
    #Make sure to mention each day, and if the employee doesnt have a scheduled work on the day mention with (None, None)
    "Monday": (None,None),
    "Tuesday": (None, None),
    "Wednesday": ("9:00 AM", "5:00 PM"),
    "Thursday": ("9:00 AM", "5:00 PM"),
    "Friday": ("9:00 AM", "1:00 PM")
}

json_body ={
  "response": "success",
  "employee": 156,
  "date_range_start": "2025-02-11 00:00:00",
  "date_range_end": "2025-04-11 22:00:00",
  "report_action": "generate_report",
  "shifts": {
    "response": "success",
    "shift_count": 31,
    "shift_total_time": "161:33",
    "wage_total": "0.00",
    "shift_array": [
      {
        "shift_id": 28737,
        "employee_clock_in_time": "April 11, 2025 9:00 am",
        "employee_clock_out_time": None,
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28695,
        "employee_clock_in_time": "April 10, 2025 9:01 am",
        "employee_clock_out_time": None,
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28670,
        "employee_clock_in_time": "April 9, 2025 9:00 am",
        "employee_clock_out_time": None,
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 28511,
        "employee_clock_in_time": "April 4, 2025 9:00 am",
        "employee_clock_out_time": "April 4, 2025 1:02 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "4:02"
      },
      {
        "shift_id": 28487,
        "employee_clock_in_time": "April 3, 2025 9:05 am",
        "employee_clock_out_time": "April 3, 2025 5:07 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:01"
      },
      {
        "shift_id": 28448,
        "employee_clock_in_time": "April 2, 2025 9:03 am",
        "employee_clock_out_time": "April 2, 2025 5:07 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:03"
      },
      {
        "shift_id": 28321,
        "employee_clock_in_time": "March 28, 2025 9:02 am",
        "employee_clock_out_time": "March 28, 2025 1:02 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "3:59"
      },
      {
        "shift_id": 28292,
        "employee_clock_in_time": "March 27, 2025 9:04 am",
        "employee_clock_out_time": "March 27, 2025 5:03 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "7:59"
      },
      {
        "shift_id": 28251,
        "employee_clock_in_time": "March 26, 2025 9:00 am",
        "employee_clock_out_time": "March 26, 2025 5:01 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:01"
      },
      {
        "shift_id": 28106,
        "employee_clock_in_time": "March 20, 2025 9:00 am",
        "employee_clock_out_time": "March 20, 2025 5:00 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:00"
      },
      {
        "shift_id": 28071,
        "employee_clock_in_time": "March 21, 2025 9:00 am",
        "employee_clock_out_time": "March 21, 2025 1:03 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "4:02"
      },
      {
        "shift_id": 28024,
        "employee_clock_in_time": "March 19, 2025 9:00 am",
        "employee_clock_out_time": "March 19, 2025 5:01 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:01"
      },
      {
        "shift_id": 27963,
        "employee_clock_in_time": "March 13, 2025 9:00 am",
        "employee_clock_out_time": "March 13, 2025 5:00 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:00"
      },
      {
        "shift_id": 27903,
        "employee_clock_in_time": "March 14, 2025 9:00 am",
        "employee_clock_out_time": "March 14, 2025 1:00 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "4:00"
      },
      {
        "shift_id": 27888,
        "employee_clock_in_time": "March 13, 2025 9:06 am",
        "employee_clock_out_time": None,
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "00:00"
      },
      {
        "shift_id": 27834,
        "employee_clock_in_time": "March 12, 2025 9:00 am",
        "employee_clock_out_time": "March 12, 2025 5:00 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:00"
      },
      {
        "shift_id": 27729,
        "employee_clock_in_time": "March 7, 2025 9:00 am",
        "employee_clock_out_time": "March 7, 2025 1:00 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "4:00"
      },
      {
        "shift_id": 27702,
        "employee_clock_in_time": "March 6, 2025 9:00 am",
        "employee_clock_out_time": "March 6, 2025 5:01 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:01"
      },
      {
        "shift_id": 27654,
        "employee_clock_in_time": "March 5, 2025 9:00 am",
        "employee_clock_out_time": "March 5, 2025 5:17 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:17"
      },
      {
        "shift_id": 27516,
        "employee_clock_in_time": "February 28, 2025 9:00 am",
        "employee_clock_out_time": "February 28, 2025 1:01 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "4:01"
      },
      {
        "shift_id": 27461,
        "employee_clock_in_time": "February 27, 2025 9:00 am",
        "employee_clock_out_time": "February 27, 2025 5:01 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:01"
      },
      {
        "shift_id": 27402,
        "employee_clock_in_time": "February 26, 2025 9:00 am",
        "employee_clock_out_time": "February 26, 2025 5:01 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "8:01"
      },
      {
        "shift_id": 27221,
        "employee_clock_in_time": "February 21, 2025 9:00 am",
        "employee_clock_out_time": "February 21, 2025 4:01 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "7:01"
      },
      {
        "shift_id": 27168,
        "employee_clock_in_time": "February 20, 2025 9:00 am",
        "employee_clock_out_time": "February 20, 2025 4:01 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "7:00"
      },
      {
        "shift_id": 27132,
        "employee_clock_in_time": "February 11, 2025 1:00 pm",
        "employee_clock_out_time": "February 11, 2025 6:00 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 27131,
        "employee_clock_in_time": "February 12, 2025 1:00 pm",
        "employee_clock_out_time": "February 12, 2025 6:00 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "5:00"
      },
      {
        "shift_id": 27100,
        "employee_clock_in_time": "February 19, 2025 9:01 am",
        "employee_clock_out_time": "February 19, 2025 4:01 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "6:59"
      },
      {
        "shift_id": 27022,
        "employee_clock_in_time": "February 14, 2025 1:00 pm",
        "employee_clock_out_time": "February 14, 2025 6:01 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "5:01"
      },
      {
        "shift_id": 26993,
        "employee_clock_in_time": "February 13, 2025 1:00 pm",
        "employee_clock_out_time": "February 13, 2025 6:03 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "5:03"
      },
      {
        "shift_id": 26969,
        "employee_clock_in_time": "February 12, 2025 6:04 pm",
        "employee_clock_out_time": "February 12, 2025 6:04 pm",
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "0:00"
      },
      {
        "shift_id": 26937,
        "employee_clock_in_time": "February 12, 2025 1:04 pm",
        "employee_clock_out_time": None,
        "first_name": "Samyukta",
        "last_name": "Padmanabhuni",
        "shift_sum": "00:00"
      }
    ]
  }
}

# Helper function to calculate the time difference
def calculate_time_diff(start_time, end_time):
    # Calculate time difference
    time_diff = end_time - start_time
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds


# Collect shifts data
shifts = json_body["shifts"]["shift_array"]
shift_dates = {datetime.strptime(shift["employee_clock_in_time"], "%B %d, %Y %I:%M %p").date(): shift for shift in shifts}

start_date = datetime.strptime(json_body["date_range_start"], "%Y-%m-%d %H:%M:%S")
end_date = datetime.strptime(json_body["date_range_end"], "%Y-%m-%d %H:%M:%S")

shift_total_time_str = json_body["shifts"]["shift_total_time"]
# Generate missing clock-in or time mismatch reports
reports = []

# Loop through each day in the date range
current_day = start_date
while current_day <= end_date:
    # Get the day name (e.g., "Monday")
    day_name = current_day.strftime('%A')
    
    # Check if the employee should have worked on this day according to the schedule
    expected_in, expected_out = EXPECTED_SCHEDULE.get(day_name, (None, None))

    # If no work is expected on this day, move to the next day
    if expected_in is None and expected_out is None:
        # Check if the employee has worked on this day
        if current_day.date() in shift_dates:
            reports.append(f"Worked on {day_name} {current_day.day}, {current_day.strftime('%B')} {current_day.year} when not scheduled.")
        current_day += timedelta(days=1)
        continue
    
    # Check if the employee has a shift for this day
    if current_day.date() not in shift_dates:
        # If no shift found for this day, report "Didn't clock in"
        reports.append(f"Didn't clock in on {day_name} {current_day.day}, {current_day.strftime('%B')} {current_day.year}")
    else:
        shift = shift_dates[current_day.date()]
        clock_in_time = datetime.strptime(shift["employee_clock_in_time"], "%B %d, %Y %I:%M %p")
        clock_out_time = shift["employee_clock_out_time"]

        if clock_out_time is not None:
            clock_out_time = datetime.strptime(clock_out_time, "%B %d, %Y %I:%M %p")

        # Check if the employee clock-in matches the expected clock-in time
        expected_in_time = datetime.strptime(f"{current_day.strftime('%B')} {current_day.day}, {current_day.year} {expected_in}", "%B %d, %Y %I:%M %p")
        
        if clock_in_time != expected_in_time:
            # Calculate time difference for late/early clock-in
            if clock_in_time > expected_in_time:
                hours, minutes, seconds = calculate_time_diff(expected_in_time, clock_in_time)
                reports.append(f"Time mismatch on {day_name} {current_day.day}, {current_day.strftime('%B')} {current_day.year}: Clocked in late by {hours} hrs {minutes} mins {seconds} secs.")
            elif clock_in_time < expected_in_time:
                hours, minutes, seconds = calculate_time_diff(clock_in_time, expected_in_time)
                reports.append(f"Time mismatch on {day_name} {current_day.day}, {current_day.strftime('%B')} {current_day.year}: Clocked in early by {hours} hrs {minutes} mins {seconds} secs.")
        if clock_out_time is None:
            # Report that no clock-out time was registered
            reports.append(f"Didn't clock-out on {day_name} {current_day.day}, {current_day.strftime('%B')} {current_day.year}.") 
        # Check for clock-out mismatch (if exists)
        if clock_out_time:
            expected_out_time = datetime.strptime(f"{current_day.strftime('%B')} {current_day.day}, {current_day.year} {expected_out}", "%B %d, %Y %I:%M %p")
            
            if clock_out_time != expected_out_time:
                if clock_out_time > expected_out_time:
                    hours, minutes, seconds = calculate_time_diff(expected_out_time, clock_out_time)
                    reports.append(f"Time mismatch on {day_name} {current_day.day}, {current_day.strftime('%B')} {current_day.year}: Clocked out late by {hours} hrs {minutes} mins {seconds} secs.")
                elif clock_out_time < expected_out_time:
                    hours, minutes, seconds = calculate_time_diff(clock_out_time, expected_out_time)
                    reports.append(f"Time mismatch on {day_name} {current_day.day}, {current_day.strftime('%B')} {current_day.year}: Clocked out early by {hours} hrs {minutes} mins {seconds} secs.")
    # Move to the next day
    current_day += timedelta(days=1)

# Print reports
for report in reports:
    print(report)
print(f"Total time worked:")
print(shift_total_time_str)