#2. write a program to input any alphabet and check whether it is vowel or consonant.

ch = input('Enter any alphabet:')

if ch.lower()in 'a e i o u':
    print('It is a Vowel')
else:
    print('It is a Consonant')
        
