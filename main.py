capitals = {
    "California":"Sacramento", 
    "Pennsylvania":"Harrisburg",
    "Delaware" : "Wilmington",
    "West Virginia" : "Charleston"
}

### Add your code here: ###

capitals["Virginia"] = "Richmond"
capitals["Maryland"] = "Annapolis"

capitals.pop("California")

capitals["Delaware"] = "Dover"

### Add your code above: ###

for key, value in capitals.items():
  print(f"State: {key}, Capital: {value}")