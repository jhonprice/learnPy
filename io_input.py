def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)



something = input("input:")

if is_palindrome(something):
    print("palindrome")
else:
    print("not palindrome")
