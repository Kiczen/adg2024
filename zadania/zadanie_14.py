def decimal_to_dms(decimal_degrees, coord_type):

    if coord_type == 'lat':
        direction = 'N' if decimal_degrees >= 0 else 'S'
    elif coord_type == 'lon':
        direction = 'E' if decimal_degrees >= 0 else 'W'

    decimal_degrees = abs(decimal_degrees)
   
    degrees = int(decimal_degrees)
    minutes_float = (decimal_degrees - degrees) * 60
    minutes = int(minutes_float)
    seconds = round(((minutes_float - minutes) * 60 - minutes) * 60, 2)

    seconds = round(seconds, 2)

    return f"{degrees}°{minutes}'{seconds}\" {direction}"

print(decimal_to_dms(25.98519, 'lat'))
print(decimal_to_dms(-97.18724, 'lon'))





