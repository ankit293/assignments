''' Write a function which takes a positive integer number n and prints [1 2 FIZZ 4 BUZZ FIZZ 7 8 FIZZ BUZZ 11 FIZZ 13 14 FIZZBUZZ … n] 
    where multiples of 3 are replaced by FIZZ, multiples of 5 are replaced by BUZZ and multiples of both are aaareplaced by FIZZBUZZ.'''

def fizzbuzz(n):
    if n < 1:
        raise ValueError("Input n should be greater than or equal to 1")
    result = []
    for i in range(1, n+1):
        if i%3 == 0 and i%5 ==0:
            result.append("FIZZBUZZ")
        elif i%3 == 0:
            result.append("FIZZ")
        elif i%5 == 0:
            result.append("BUZZ")
        else:
            result.append(i)
    return result


'''Write a function which takes a positive integer number n and prints the Fibonacci sequence [1 1 2 3 5 8 13 … ] upto n.'''

def fibonacci(n):
    fib_sequence = [0, 1]
    if n < 0:
        raise ValueError("Input n should be greater than or equal to 0")
    if n < 2:
        return fib_sequence[:n+1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1]+fib_sequence[i-2])
    return fib_sequence


'''Write a function which takes a string s as input and prints the frequencies of all the words in the string. 
    Example: quick fox lazy dog quick donkey fire fox input returns {quick: 2, fox: 2, lazy: 1, dog: 1, donkey: 1, fire: 1}.
    Use <space>  as the delimiter to identify what a word is.'''

def word_frequency(sentence):
    frequencies = {}
    sentence = sentence.strip()
    if not sentence:
        raise ValueError("Please enter a valid sentence")
    words = sentence.split(" ")
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies