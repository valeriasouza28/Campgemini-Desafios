import re 
password = input("Digite senha: ")
flag = 0


while True:   
    if (len(password)<6): 
        flag = -1
        print("\n ⚠ Senha precisa de minimo de 6 caracteres\n")
        break
    elif not re.search("[a-z]", password): 
        flag = -1
        print("⚠ Falta minuscula")
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        print("⚠ Falta maiúscula")
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        print("⚠Falta números")
        break
    elif not re.search("[!@#$%^&*()]", password): 
        flag = -1
        print("⚠Falta símbolos")
        break
    elif re.search("\s", password): 
        flag = -1
        break 
    else:
      
        flag = 0
        print("Senha Válida ✅") 
        break
  
if flag ==-1: 
   
    
    print("\nPara ser válida, a senha necessita de:\n")
    print("\n ▪ Necessita de caracter minúsculo\n")
    print(" ▪ Necessita de caracter maiúsculo\n")
    print(" ▪ Necessita de um número\n")
    print(" ▪ Necessita de  um simbolo\n")
