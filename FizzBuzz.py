# tout les nombres de 1 à N
# divisible par 3 -> fizz
# divisible par 5 -> buzz
# divisible par 3 et par 5 -> fizzbuzz

limite = 20

ok3 = False
ok5 = False
ma_chaine = ""
print ("")

for num in range(limite+1):
    ma_chaine = ""
    ok3 = (num%3 == 0)
    ok5 = (num%5 == 0)
    if ok3:
        ma_chaine=ma_chaine+"fizz"
    if ok5:
        ma_chaine=ma_chaine+"buzz"
    if ok3 or ok5:
        print(f'{num} = {ma_chaine}')

print ("")

