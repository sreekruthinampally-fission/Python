i = 1
while i <=10:
    print(i)
    i+=1
print("Done with the loop")

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

for i in range(11):
    if i % 2 == 0:
        print(f"Even number {i} found")
        continue 
    print(f"Odd number {i} found")  

secret_word = "Mount"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter a word:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses :
    print("You are out of Guesses. YOU LOSE!")
else :
    print("You win!")
