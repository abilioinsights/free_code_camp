# Time Adder

This Python program adds a specified duration to a given start time in the 12-hour clock format. It also handles optional parameters such as the starting day of the week and displays the resulting time with the correct day and format.

## Features:
- Adds duration to a 12-hour format time.
- Handles AM/PM conversion and day of the week.
- Returns the result in a readable format with optional information on the day of the week and how many days later the result occurs.
- Allows for multi-day calculations.

## Function: `add_time(start, duration, day_of_week=None)`

### Parameters:
1. **start (str)**: The start time in 12-hour format (e.g., "3:00 PM").
2. **duration (str)**: The duration in hours and minutes (e.g., "2:30").
3. **day_of_week (str, optional)**: The starting day of the week, case insensitive (e.g., "Monday").

### Returns:
The result in the format:
- `HH:MM AM/PM, Day (x days later)` if days have passed.

### Examples:

```python
print(add_time('3:00 PM', '3:10'))  
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))  
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))  
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))  
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))  
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))  
# Returns: 7:42 AM (9 days later)
```

## How to Run:
Clone or download the repository.
Run the script in Python 3.x using:

```py
python time_adder.py
```
## License:
This project is open source and available under the MIT License.
