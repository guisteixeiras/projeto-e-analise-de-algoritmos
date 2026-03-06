def inverter_string(s): #função recursiva
    if s == "":
        return ""
    
    return inverter_string(s[1:]) + s[0]

texto = "python"
print(inverter_string(texto))