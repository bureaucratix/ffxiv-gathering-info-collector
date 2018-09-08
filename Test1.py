import datetime

iteminfo = {
    "gold ore": {
        "time_interval": 70,
        "start_time": "???",
        "map": "Eastern Thanalan",
        "coord": [28, 22],
        "slot": 6
    },
    "darksteel ore": {
        "time_interval": 35,
        "start_time": "???",
        "map": "Coerthas Central Highland",
        "coord": [27, 19],
        "slot": 3
    }
}

item = input("What would you like info on?")

print(item.capitalize() + " spawns in " + iteminfo[item]["map"] + " at X " + str(iteminfo[item]["coord"][0]) + " Y " +
      str(iteminfo[item]["coord"][1]) + ", in slot " + str(iteminfo[item]["slot"]) + ".")

