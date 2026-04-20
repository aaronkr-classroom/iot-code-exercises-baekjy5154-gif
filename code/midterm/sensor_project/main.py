# Part 1: 클래스만들기
from lib.room_sensor import RoomSensor

sensor1 = RoomSensor("Living Room", 26, 55, 420)

sensor1.show_info()
print(sensor1.comfort_level())
print(sensor1.light_status())

sensor1 = RoomSensor("Kitchen", 24, 50, 300)
sensor2 = RoomSensor("Bedroom", 28, 65, 150)
sensor3 = RoomSensor("Balcony", 30, 70, 500)

sensors = [sensor1, sensor2, sensor3]

for s in sensors:
    s.show_info()
    print(s.comfort_level())
    print(s.light_status())
    print("-----")

for s in sensors:
    print(f"Sensor: {s.name}")
    print(f"Temperature: {s.temperature}")
    print(f"Humidity: {s.humidity}")
    print(f"Light: {s.light}")
    print(f"Comfort Level: {s.comfort_level()}")
    print(f"Light Status: {s.light_status()}")
    print()
    
comfortable_count = 0
normal_count = 0
warning_count = 0

for s in sensors:
    level = s.comfort_level()

    if level == "Comfortable":
        comfortable_count += 1
    elif level == "Warning":
        warning_count += 1
    else:
        normal_count += 1
        
print(f"Comfortable: {comfortable_count}")
print(f"Normal: {normal_count}")
print(f"Warning: {warning_count}")