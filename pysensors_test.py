import sensors
temps = []
cores = []
for sensor in sensors.get_detected_chips():
    if sensor.prefix == "coretemp":
        cores.append(sensor)
for core in cores:
    for feature in core.get_features():
        for subfeature in core.get_all_subfeatures(feature):
            if subfeature.name.endswith("_input"):
                temps.append(core.get_value(subfeature.number))
                        
print(temps)
