import random

# Generate 10 random geographical coordinates (latitude, longitude)
lucky_count = 0
for i in range(10):
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    print(f"Coordinate {i+1}: (Latitude: {latitude:.6f}, Longitude: {longitude:.6f})")
    if latitude > 60:
        print("You are lucky! (High northern latitude)")
        lucky_count += 1
print(f"\nNumber of times you were lucky (latitude > 60): {lucky_count} out of 10")
