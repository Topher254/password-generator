import random

password = []
random.randint(0, 9)
password.append(random.randint(0, 9))
name = input("Enter your name: ")
password.append(name[random.randint(0, 4)])
alphabets = 'abcdefghijklmnopqrstuvwxyz'
password.append(alphabets[random.randint(0, 25)])
alphabets2 = 'qwertyuiopasdfghjklzxcvbnm'
password.append(alphabets2[random.randint(0, 25)])
alphabets3 = 'mnbvcxzlkjhgfdsapoiuytrewq'
password.append(alphabets3[random.randint(0, 25)])
alphabets4 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
password.append(alphabets4[random.randint(0, 25)])
alphabets5 = ',.//><:1234567890#$%%^&*(()_+{}":?><~'
password.append(alphabets5[random.randint(0, 25)])
alphabets6 = 'poiuytrewqlkjhgfdsamnbvcxzbackqwerty'
password.append(alphabets6[random.randint(0, 30)])
new_password = "%s%s%s%s%s%s%s%s" % (
    password[0], password[1], password[2], password[3], password[4], password[5], password[6], password[7])
print("Your password is", new_password)
