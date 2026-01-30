def calcular_BMI(peso_lb: float, altura_inch: float)->float:
    peso_kg=peso_lb*0.45
    altura_mts=altura_inch*0.025
    BMI=round((peso_kg)/(altura_mts**2),2)
    return BMI
