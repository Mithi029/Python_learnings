sentence = 'what is the Airspeed velocity of an unladen swallow?'

stripped = sentence.split(' ')

result = {word: len(word) for word in stripped}

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
weather_f = {k: ((int(v) * 9/5) + 32) for k, v in weather_c.items()}

print(weather_f)
