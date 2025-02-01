'''A PROGRAM THAT REVERSE THE CHARACTERS OF A STRING'''


def reverse(str_cha):
#Getting the lenght of the word
    num = len(str_cha)
    character = ''

    while num >= 0:

        if num == 0:
            print('THE STRING HAS BEEN REVERSED')
            print(f"NEW STRING: {character}")
            break

        new_str = str_cha[num-1]

        character = character + new_str

        num = num - 1


typing = input("ENTER YOUR WORD: ")
reverse(typing)