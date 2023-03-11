basic_numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19
}

special_numbers_add = {
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90
}

special_numbers_multiply = {
    "hundred": 100
}

operators = {
    "plus": '+',
    "substract": '-',
    "multiple": '*',
    "division": '/',
    "equals": '='
}


# Python3 program to evaluate a given
# expression where tokens are
# separated by space.

# Function to find precedence
# of operators.
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


# Function to perform arithmetic
# operations.
def applyOp(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b


def evaluate(tokens):
    values = []

    ops = []
    i = 0

    while i < len(tokens):
        if tokens[i] == ' ':
            i += 1
            continue

        elif tokens[i] == '(':
            ops.append(tokens[i])

        elif tokens[i].isdigit():
            val = 0

            while (i < len(tokens) and
                   tokens[i].isdigit()):
                val = (val * 10) + int(tokens[i])
                i += 1

            values.append(val)
            i -= 1

        elif tokens[i] == ')':

            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))

            # pop opening brace.
            ops.pop()

        # Current token is an operator.
        else:
            while len(ops) != 0 and precedence(ops[-1]) >= precedence(tokens[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))

            # Push current token to 'ops'.
            ops.append(tokens[i])

        i += 1

    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()

        values.append(applyOp(val1, val2, op))

    return values[-1]


def make_proper_format(s: str):
    s = s.split()
    ans = ""
    val = 0
    for ind, word in enumerate(s):

        # if number is number
        if word.isnumeric():
            val = int(word)
            ans += word
        # "and" is encountered
        elif word == "and":
            ans = ans[:-1]
        # if word is hundred
        elif word in special_numbers_multiply:
            val *= special_numbers_multiply[word]
        # if word is twenty, thirty, ...
        elif word in special_numbers_add:
            val += special_numbers_add[word]
        # if word is one, two, ...
        elif word in basic_numbers:
            val += basic_numbers[word]
            word = basic_numbers[word]
            ans += str(val)
        # if word is operator in words
        elif word in ("plus", "substract", "multiple", "division", "equals"):
            val = 0
            word = operators[word]
            ans += str(word)
        # if word is operator
        elif word in ('+', '-', '*', '/', '='):
            val = 0
            ans += str(word)
        # if word is float number
        else:
            ans += str(word)

        # ans += str(word)

        # if not word.isnumeric():
        #     if word in basic_numbers:
        #         word = basic_numbers[word]
        #     elif word in ("plus", "substract", "multiple", "division", "equals"):
        #         word = operators[word]
        #     ans += str(word)
        # else:
        #     ans += str(word)
    return ans


if __name__ == "__main__":
    inp = open("TMW_small.txt", "r")
    out = open("TMW_small_output.txt", "w")

    data = inp.readlines()

    r = 0
    T = int(data[r])
    r += 1

    # print(make_proper_format("seven hundred and ninety eight substract 4 / thirty eight * one = 20701"))

    for i in range(T):
        formula = data[r]
        r += 1

        # collect data in proper format
        formula = make_proper_format(formula)

        left, right = formula.split('=')
        if evaluate(left) == float(right):
            out.write("Case #{0}: true\n".format(i + 1))
        else:
            out.write("Case #{0}: false\n".format(i + 1))
