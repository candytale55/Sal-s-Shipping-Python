"""
The program will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers options:
- Ground shipping, which is a small flat charge (gr_flat) plus a rate based on the weight of your package.
- Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. 
- Drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
"""

# the price of premium ground shipping does not change with the weight of the package.
premium_ground_flat_rate = 125.00


# ship_ground(weight):  take weight, and return the cost of shipping a package of that weight.
def ship_ground(weight):
  ground_flat_rate = 20.0
  if weight <= 2.0 :
    return 1.50 * weight + ground_flat_rate
  elif weight > 2.0 and weight <=6.0:
    return 3.0 * weight + ground_flat_rate
  elif weight > 6.0 and weight <= 10.0:
    return 4.0 * weight + ground_flat_rate
  else: # weight is over 10 lbs
    return 4.75 * weight + ground_flat_rate


# ship_drone(weight):  take weight, and return the cost of shipping a package of that weight.
def ship_drone(weight):
  drone_flat_rate = 0.0
  if weight <= 2.0 :
    return 4.50 * weight + drone_flat_rate
  elif weight > 2.0 and weight <=6.0:
    return 9.0 * weight + drone_flat_rate
  elif weight > 6.0 and weight <= 10.0:
    return 12.0 * weight + drone_flat_rate
  else: # weight is over 10 lbs
    return 14.25 * weight + drone_flat_rate



print(ship_ground(8.4)) # 53.60
print(ship_drone(1.5))  # 6.75

def what_is_cheapest(weight):
  cost_ground = ship_ground(weight)
  cost_premium_ground = premium_ground_flat_rate
  cost_drone = ship_drone(weight)
  if (cost_drone <= cost_premium_ground) and (cost_drone <= cost_ground):
    string =  "The cheapest shipping method is drone shipping at $" + str(cost_drone) + ". Premium Ground is  $" + str(cost_premium_ground) + ". And ground shipping is $" + str(cost_ground)
  elif (cost_premium_ground <= cost_ground) and (cost_premium_ground <= cost_drone):
    string =  "The cheapest shipping method is Premium Ground shipping at $" + str(cost_premium_ground) + ". Ground shipping is  $" + str(cost_ground) + ". And drone shipping is $" + str(cost_drone)
  else:
    string =  "The cheapest shipping method is Ground shipping at $" + str(cost_ground) + " . Premium Ground is $" + str(cost_premium_ground) + ". And drone shipping is $" + str(cost_drone) 
  return string


# TESTS
#print(what_is_cheapest(1))
#print(what_is_cheapest(.5))
#print(what_is_cheapest(10))
#print(what_is_cheapest(5))
#print(what_is_cheapest(500))

print(what_is_cheapest(4.8))   # ground
print(what_is_cheapest(41.5))  # premium ground
