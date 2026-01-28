# Password Generator

This is a Python program that generates passwords using a word and a 2-digit number from the user.

The program works like this:  
1. It asks the user to enter a word. Any spaces are removed.  
2. It asks for a 2-digit number. The number is formatted with `zfill` to make it 3 digits.  
3. The letters in the word are randomly turned into uppercase or lowercase.  
4. Two symbols are randomly chosen and shuffled with the number digits.  
5. Some of the symbols and numbers are placed before the word, the rest after, to form the password.  
6. The final password is printed directly.

The program uses the `random` module and string methods like `replace()`, `zfill()`, `upper()`, `lower()`, and `isdigit()`.  

While building it, I ran into problems with input validation, randomizing the word, and formatting the password.  
I fixed them step by step, which helped me understand randomness and string handling in Python better.

To run:  
- Run the Python file  
- Enter a word  
- Enter a 2-digit number  
- See the generated password
