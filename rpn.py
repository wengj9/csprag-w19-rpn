#!/usr/bin/env python3

import operator
import readline
import math


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
    '!': math.factorial,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
}

one_operators = ['!', 'sin', 'cos', 'tan']

constants = {
    'pi': math.pi,
    'e': math.e,
}

def calculate(myarg):
        stack = list()
        for token in myarg.split():
            try:
                token = int(token)
                stack.append(token)
            except ValueError:
                if (token in constants):
                    token = constants[token]
                    stack.append(token)
                elif (token in one_operators):
                    function = operators[token]
                    arg1 = stack.pop()
                    result = function(arg1)
                    stack.append(result)
                else:
                    function = operators[token]
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    result = function(arg1, arg2)
                    stack.append(result)
        if len(stack) != 1:
            raise TypeError("Too many parameters")
        return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
