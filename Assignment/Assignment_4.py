print("-------------------------------Question 1------------------------------")

import csv

data = [
    ["Name","Address","Mobile","email"],
    ["mohit","ABC","9863281908","gdsvw@gmail.com"],
    ["mohan","DEF","8862545183","fbcxhva@gmail.com"],
    ["manish","GHI","9197346393","vjbwrw@gmail.com"],
]

with open("account.csv","w")as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

print("-------------------------------Question 2------------------------------")

import requests

def weather_details(city,api_key):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    final_url = f"{url}q={city}&appid={api_key}&units=metric"
    print(final_url)

    try:
        requests.get(final_url)
        response = requests.get(final_url)
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]

        print(f"Weather is {city}:")
        print(f"Temperature: {temperature}C(feels like: {feels_like}C")
        print(f"Humidity: {humidity}%")
        print(f"Descrition: {data["weather"][0]["description"].capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

api_key ="30f5f498611580da50a52d18563261b6"
city = input("enter city name:")

weather_details(city,api_key)

print("\n-------------------------------Question 3------------------------------\n")

import sqlite3

conn = sqlite3.connect("college.db")

conn.execute("""
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    city TEXT
)
""")

conn.execute("""
CREATE TABLE Courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    duration TEXT
)
""")

#inserting data in student table
conn.execute("INSERT INTO Students (name, age, city) VALUES ('lakshay', 20, 'Jaipur')")
conn.execute("INSERT INTO Students (name, age, city) VALUES ('shivam', 22, 'Delhi')")
conn.execute("INSERT INTO Students (name, age, city) VALUES ('suchitra', 21, 'Mumbai')")

#inserting data in courses table
conn.execute("INSERT INTO Courses (course_name, duration) VALUES ('Python Programming', '3 months')")
conn.execute("INSERT INTO Courses (course_name, duration) VALUES ('Data Structures', '2 months')")

#using Select Operations
print("\nAll Students:")
data=conn.execute("SELECT * FROM Students")
for row in data:
    print(row)

print("\nStudents from Jaipur:")
data=conn.execute("SELECT * FROM Students WHERE city = 'Jaipur'")
for row in data:
    print(row)

print("\nAll Courses:")
data=conn.execute("SELECT * FROM Courses")
for row in data:
    print(row)

#Updating Record
conn.execute("UPDATE Students SET city = 'Bangalore' WHERE name = 'suchitra'")

#updated data
print("\nAfter Update:")
data=conn.execute("SELECT * FROM Students")
for row in data:
    print(row)

# Deleting a Record
conn.execute("DELETE FROM Students WHERE name = 'lakshay'")

print("\nAfter Deletion:")
data=conn.execute("SELECT * FROM Students")
for row in data:
    print(row)

conn.commit()
conn.close()
