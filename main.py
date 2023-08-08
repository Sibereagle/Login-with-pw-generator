import random
import string


def password_generator():
    usr_inp = user_input()
    while True:
        password_result = """"""
        letters = string.ascii_letters
        letter_count = random.randint(0, usr_inp[0] - (usr_inp[1] + usr_inp[2]))
        spec_count = random.randint(usr_inp[1], usr_inp[0] - letter_count - usr_inp[2])
        num_count = usr_inp[0] - letter_count - spec_count
        result_str = ''.join(random.choice(letters) for i in range(letter_count))
        result_spec = """""".join(random.choice(string.punctuation) for i in range(spec_count))
        result_num = ''.join(random.choice(string.digits) for i  in range(num_count))
        password_result += result_str + result_spec + result_num
        shuffled = """""".join(random.sample(password_result, len(password_result)))
        fin_shuffle = """""".join(random.sample(shuffled, len(shuffled)))
        print(fin_shuffle)
        end_code = input("Is this password satisfactory? (y/n): ")
        if end_code == "y":
            break



# def user_input():
#     pass_len = int(input("Password length?: "))
#     spec_count = int(input("Minimum special character count?: "))
#     num_count = int(input("Minimum integer character count?: "))
#     print("Thanks! Generating Password...")
#     return pass_len, spec_count, num_count


def randomNum(min, max):
    return random.randint(min, max)

print(randomNum(1, 100))


class PassGen:
    def __init__(self):
        self.password = """"""

    def get_user_input(self):
        pass_len = int(input)

