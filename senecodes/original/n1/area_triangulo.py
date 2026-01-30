def area_triangulo(s1:float, s2:float, s3:float)->float:
    import math
    s=(s1+s2+s3)/2
    expresion=(s*(s-s1)*(s-s2)*(s-s3))
    area=math.sqrt(expresion)
    area=round(area,1)
    return(area)