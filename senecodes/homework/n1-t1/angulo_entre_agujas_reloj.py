def angulo_entre_agujas_reloj(hora: int, minutos: int)->float:
    degrees_per_minute = 360 / 60
    minute_hand_degrees = minutos * degrees_per_minute
    
    degrees_per_hour = 360 / 12
    degrees_per_hour_with_minute_offset = degrees_per_hour / 60
    hour_hand_degrees = hora * degrees_per_hour + minutos * degrees_per_hour_with_minute_offset
    
    inter_hands_angle = abs(minute_hand_degrees - hour_hand_degrees)
    minimum_angle = min(inter_hands_angle, 360 - inter_hands_angle)
    return minimum_angle