def calcular_iva_propina_total_factura(costo_factura: int)->str:
    i=0.19*costo_factura
    p=0.1*costo_factura
    t=i+p+costo_factura
    istr=str(round(i))
    pstr=str(round(p))
    tstr=str(round(t))
    return istr+","+pstr+","+tstr

