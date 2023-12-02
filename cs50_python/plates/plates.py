def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if s[0].isdigit():
        return False
    elif s[0:2].isalpha():
        return True
    elif s[0:5].strip().set(""):
        return False
    else:
        return True



main()
