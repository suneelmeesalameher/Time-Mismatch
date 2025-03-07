from datetime import datetime, timedelta

EXPECTED_SCHEDULE = {
    "Monday": ("1:00 PM","6:00 PM"),
    "Tuesday": ("8:00 AM", "1:00 PM"),
    "Wednesday": ("1:00 PM", "6:00 PM"),
    "Thursday": (None,None),
    "Friday": ("8:00 AM","1:00 PM")
}

json_body ={
    #JSON BODY from the reports section of Time Clock Lite, Make sure to replace null with NONE
}
# Collect shifts data
shifts = json_body["shifts"]["shift_array"]
shift_dates = {datetime.strptime(shift["employee_clock_in_time"], "%B %d, %Y %I:%M %p").date(): shift for shift in shifts}

start_date = datetime.strptime(json_body["date_range_start"], "%Y-%m-%d %H:%M:%S")
end_date = datetime.strptime(json_body["date_range_end"], "%Y-%m-%d %H:%M:%S")

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
        
        if shift["employee_clock_out_time"] is None:
            # Missing clock-out
            reports.append(f"Missing clock-out on {day_name} {current_day.day}, {current_day.strftime('%B')} {current_day.year}")
        
        # Calculate actual work time
        shift_end_time = clock_in_time + timedelta(hours=int(shift["shift_sum"].split(":")[0]), minutes=int(shift["shift_sum"].split(":")[1]))
        expected_end_time = datetime.strptime(f"{current_day.strftime('%B')} {current_day.day}, {current_day.year} {expected_out}", "%B %d, %Y %I:%M %p") if expected_out else None
        
        # If shift clock-out exists and time mismatch detected
        if expected_end_time:
            if shift_end_time > expected_end_time:
                extra_time = shift_end_time - expected_end_time
                reports.append(f"Extra time worked on {day_name} {current_day.day}, {current_day.strftime('%B')} {current_day.year}: {extra_time}")
            elif shift_end_time < expected_end_time:
                less_time = expected_end_time - shift_end_time
                reports.append(f"Less time worked on {day_name} {current_day.day}, {current_day.strftime('%B')} {current_day.year}: {less_time}")
        
        # If there's a mismatch (e.g., incorrect clock-in or clock-out time)
        if shift["employee_clock_in_time"] != expected_in:
            reports.append(f"Time mismatch on {day_name} {current_day.day}, {current_day.strftime('%B')} {current_day.year}")

    # Move to the next day
    current_day += timedelta(days=1)
print(EXPECTED_SCHEDULE)
# Print reports
for report in reports:
    print(report)
