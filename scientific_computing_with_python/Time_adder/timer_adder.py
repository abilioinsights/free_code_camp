def add_time(start, duration, day_of_week=None):
    # Dictionary for days of the week and their indices
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Validate input
    def validate_input(start_hour, start_minute, duration_hour, duration_minute, day_of_week):
        if start_hour < 0 or start_hour > 12 or start_minute < 0 or start_minute > 59:
            raise ValueError("Horário inicial inválido.")
        if duration_hour < 0 or duration_minute < 0 or duration_minute > 59:
            raise ValueError("Duração inválida.")
        if day_of_week and day_of_week.capitalize() not in days_of_week:
            raise ValueError("Dia da semana inválido.")
    
    # Convert to 24-hour format
    def convert_to_24_hour_format(time, period):
        if period == 'PM' and time != 12:
            return time + 12
        elif period == 'AM' and time == 12:
            return 0
        return time
    
    # Convert to 12-hour format
    def convert_to_12_hour_format(time):
        if time == 0:
            return 12, 'AM'
        elif time < 12:
            return time, 'AM'
        elif time == 12:
            return 12, 'PM'
        else:
            return time - 12, 'PM'
    
    # Calculate new day of the week
    def calculate_new_day(start_day, days_later):
        if not start_day:
            return None
        day_index = days_of_week.index(start_day.capitalize())
        return days_of_week[(day_index + days_later) % 7]
    
    # Format the final result
    def format_result(end_hour, end_minute, period, new_day, days_later):
        new_time = f'{end_hour}:{end_minute:02d} {period}'
        if new_day:
            new_time += f', {new_day}'
        if days_later == 1:
            new_time += ' (next day)'
        elif days_later > 1:
            new_time += f' ({days_later} days later)'
        return new_time
    
    # Splitting start time into hour, minute, and period (AM/PM)
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Splitting duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Validate input
    validate_input(start_hour, start_minute, duration_hour, duration_minute, day_of_week)
    
    # Convert to 24-hour format
    start_hour = convert_to_24_hour_format(start_hour, period)
    
    # Adding duration minutes to start minutes
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + end_minute // 60
    end_minute %= 60
    
    # Calculating how many days passed
    days_later = end_hour // 24
    end_hour %= 24
    
    # Convert back to 12-hour format
    end_hour, period = convert_to_12_hour_format(end_hour)
    
    # Calculate new day of the week
    new_day = calculate_new_day(day_of_week, days_later)
    
    # Format and return the result
    return format_result(end_hour, end_minute, period, new_day, days_later)

# Example calls
print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('6:30 PM', '205:12'))
