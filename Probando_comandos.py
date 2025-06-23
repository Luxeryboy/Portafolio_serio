travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],}

travel_log2 = {"lujo":"perro bomba"}

travel_log["France"] = travel_log2["lujo"]
print(type(travel_log))
print(travel_log)