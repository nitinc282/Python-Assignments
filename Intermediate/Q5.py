def temperature_readings(t):

    Average_Temperature=sum(t)/len(t)
    highest_temperature = max(t)
    lowest_temperature = min(t)
    return Average_Temperature, highest_temperature, lowest_temperature

t = [25, 28, 21, 24, 27]

a,b,c=temperature_readings(t)
print("Average Temperature:", a)
print("Highest Temperature:", b)
print("Lowest Temperature:", c)


