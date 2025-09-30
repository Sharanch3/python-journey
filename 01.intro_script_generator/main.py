import datetime

current_date = datetime.date.today().isoformat()


print("-----------SELF INTRO SCRIPT GENERATOR---------")


name = input("What is your name? ").strip().title()
age = int(input("How old are you? "))
city = input("Which city do you live in? ").strip().title()
profession = input("What is your profession? ").strip().title()
hobby = input("What is your favourite hobby? ").strip()


script = f"""  
Hello! My name is {name}. I'm {age} years old and live in {city}. I work as a {profession} and I absolutely enjoy {hobby} in my free time. Nice to meet you!\n
Logged on: {current_date}
"""

stars = "*" * 100


print(stars)
print(script)
print(stars)
