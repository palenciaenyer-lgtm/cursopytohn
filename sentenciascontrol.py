num = int(input("ingrese un numero: "))

if num != 0:
     if num > 0:
        if num % 2 == 0: 
            print(f"el numero {num} es par positivo")
        else:
            print(f"el numero {num} es impar negativo")
     else:
         if num % 2 == 0: 
            print(f"el numero {num} es par negativo")
         else:
            print(f"el numero {num} es impar positivo")       
else:
    print(f"el numero {num} es neutro")