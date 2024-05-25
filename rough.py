dict = {
    "Mon" : 12,
    "Tue" : 14,
    "wed" : 15
}

weather_f = { (days,tem*9/5+32) for (days,tem) in dict.items() }

print(weather_f)f