capitals = {
    "California":"Sacramento", 
    "Pennsylvania":"Harrisburg",
    "Delaware" : "Wilmington",
    "West Virginia" : "Charleston"
}

capitals["Virginia"] = "Richmond"
capitals["Maryland"] = "Annapolis"
capitals["Georgia"] = "Atlanta"

capitals.pop("California")

capitals["Delaware"] = "Dover"

for key, value in capitals.items():
  print(f"State: {key}, Capital: {value}")