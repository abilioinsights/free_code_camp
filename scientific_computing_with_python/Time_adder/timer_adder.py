def add_time(start, duration, day_of_week=None):
    # Dictionary for days of the week and their indices
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Splitting start time into hour, minute, and period (AM/PM)
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Splitting duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Converting to 24-hour format to simplify calculations
    if period == 'PM' and start_hour != 12:  # If PM and not 12, add 12 hours
        start_hour += 12
    elif period == 'AM' and start_hour == 12:  # If AM and 12 o'clock, it's 0 (midnight)
        start_hour = 0
    
    # Adding duration minutes to start minutes
    end_minute = start_minute + duration_minute
    
    # If minutes exceed 60, convert the excess into hours
    end_hour = start_hour + duration_hour + end_minute // 60
    
    # Keeping only the remaining minutes (if they exceed 60)
    end_minute %= 60
    
    # Calculating how many days passed based on the total number of hours
    days_later = end_hour // 24
    
    # Keeping only the remaining hours (after removing excess days)
    end_hour %= 24
    
    # Converting back to 12-hour format
    if end_hour == 0:
        period = 'AM'
        end_hour = 12  # If it's midnight in 24-hour format, convert to 12 AM
    elif end_hour < 12:
        period = 'AM'  # AM period if hours are below 12
    elif end_hour == 12:
        period = 'PM'  # Exactly 12 hours in 24-hour format is 12 PM
    else:
        period = 'PM'
        end_hour -= 12  # Converting back to 12-hour format
    
    # Determining the resulting day of the week, if provided
    if day_of_week:
        day_index = days_of_week.index(day_of_week.capitalize())
        new_day = days_of_week[(day_index + days_later) % 7]  # Calculating the new day of the week
    
    # Building the string for the new time
    new_time = f'{end_hour}:{end_minute:02d} {period}'
    
    # If there's a day of the week, add it to the result
    if day_of_week:
        new_time += f', {new_day}'
    
    # Adding "(next day)" or "(n days later)" if applicable
    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'
    
    return new_time
