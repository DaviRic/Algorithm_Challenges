def timeConversion(s):
    hora = int(s[:2])
    if "AM" in s:
        if hora == 12:
            nova_hora = "00" + s[2:8]
        else:
            nova_hora = s[:8]
    else:  # PM
        if hora != 12:
            hora += 12
        nova_hora = str(hora).zfill(2) + s[2:8]
    return nova_hora
