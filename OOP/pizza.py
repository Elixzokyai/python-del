import math

# Delivery locations (south, east)
deliveries = [
    (2, 3.2),  # Delivery 1: 2 miles south and 3.2 miles east
    (0, 2.1),  # Delivery 2: 2.1 miles due east
    (3, -1.6)  # Delivery 3: 3 miles south and 1.6 miles west (considering west as negative east)
]

# Constants
speed_mph = 30  # miles per hour
drop_off_time_per_delivery = 2  # minutes
num_deliveries = len(deliveries)

# Calculate total driving distance and time
total_distance = 0

for south, east in deliveries:
    # Calculate distance to delivery
    distance_to_delivery = math.sqrt(south ** 2 + east ** 2)

    # Add return distance to pizza parlor
    total_distance += 2 * distance_to_delivery  # round trip

# Calculate driving time in minutes
driving_time_minutes = (total_distance / speed_mph) * 60

# Calculate total drop-off time
total_drop_off_time = num_deliveries * drop_off_time_per_delivery

# Total time required
total_time = driving_time_minutes + total_drop_off_time

# Print the total time
print(f"The least amount of time required is {total_time:.2f} minutes.")
