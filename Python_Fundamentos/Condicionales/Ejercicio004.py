def msj_calificacion(grade):
    if grade == 'A':
        return "Excelente"
    elif grade == 'B':
        return "Buen Trabajo"
    elif grade =='C':
        return "Regular"
    elif grade =='D':
        return "Intentalo"
    else:
        return "No Existe el Grado"
    
def msj_calificacion_case(grade):
    match grade:
     case 'A':
        return "Excelente"
     case 'B':
        return "Buen Trabajo"
     case 'C':
        return "Regular"
     case 'D':
        return "Intentalo"
     case _:
        return "No Existe el Grado"    
    
print(msj_calificacion_case('B'))
#print(msj_calificacion("A"))