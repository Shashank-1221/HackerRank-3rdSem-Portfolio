import math

def timeConversion(s):
    period = s[-2:]
    hour_val = int(s[:2])
    middle_time = s[2:-2]
    
    if period == "AM":
        if hour_val == 12:
            hour_val = 0
    else:
        if hour_val != 12:
            hour_val += 12
            
    return f"{hour_val:02d}{middle_time}"

if __name__ == '__main__':
    sample_time = "07:05:45PM"
    result = timeConversion(sample_time)
    print("24-Hour Converted Time:", result)