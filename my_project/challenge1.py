def convert_to_24_hour(hour, minute, period):
    
    if period == "pm" and hour != 12:
        hour += 12
    
   
    if period == "am" and hour == 12:
        hour = 0
    
   
    time_24_hour = f"{hour:02d}{minute:02d}"
    
    return time_24_hour


hour = 8
minute = 30
period = "am"

result = convert_to_24_hour(hour, minute, period)
print(f"The 12-hour time {hour}:{minute} {period} in 24-hour format is: {result}")
