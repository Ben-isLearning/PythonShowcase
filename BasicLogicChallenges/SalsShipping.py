
weight = 41.5

# Ground Shipping
if weight > 10:
    price = (weight * 4.75) + 20
elif weight >= 6:
    price = (weight * 4.00) + 20
elif weight >= 2:
    price = (weight * 3.00) + 20
elif weight < 2:
    price = (weight * 1.50) + 20
else:
    price = "Please enter a valid number from 0 to 999"

print("Your package weighs ", weight,
      "lbs. \n It will cost $", price, " to ship by Standard ground.\n It will cost $ 125.00 to ship by Express ground.")


# Drone Shipping
if weight > 10:
    drone_price = (weight * 14.25)
elif weight >= 6:
    drone_price = (weight * 12.00)
elif weight >= 2:
    drone_price = (weight * 9.00)
elif weight < 2:
    drone_price = (weight * 4.50)
else:
    drone_price = "Please enter a valid number from 0 to 999"

print("Your package weighs ", weight,
      "lbs. \n It will cost $", round(drone_price, 2), " to ship by standard drone.")
