cursos={"PCEP01":"Python-001","PCEP02":"Python-002"}

#print(cursos["PCEP02"])

try:
    clave=input("Ingrese la Clave:")
    print(cursos[clave])
except KeyError as msg_error:
    print(f"Lo siento  {msg_error} no es una clave valida!")    