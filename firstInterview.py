# Interview question:
# Write a function that parses and evaluates an arithmetic string
# The function should mimic "eval": return the same value, but your own code
# Ex. "1+2" = 3
#     "34-5*100" = -466
#     "10-20*30+40/50" = -589.2
#     "10*30/2*30+5" = 4505
# Positive integers separated by +, -, * or /. No parentheses
# You must respect the order of operations: *, / take precedence over +, -
# *, / are the same priority, so go left-to-right. Likewise for +, -
# Do not use "eval" or 3rd party libraries.


"34-5*100"

[34, 5, 100]
['-', '*']

operators = ["+", "-", "*", "/"]
test = "10*30/2*30+5"

def split(string):
    nums = []
    ops = []
    temp = 0
    for val in string:
        # val is an operator
        if val in operators:
            ops.append(val)
            nums.append(temp)
            temp = 0

        # val is a number
        else:
            temp = temp * 10 + int(val)
    nums.append(temp)
    return nums, ops


# ([1,2,3,4,5,6,7], ['+', '*', '/', '*', '*', '*'])
# ([1,6], ['+'])
def mulDiv(nums, ops):
    newNums = [nums[0]]
    newOps = []
    for i, op in enumerate(ops):
        if op == '*':
            newNums[-1] = newNums[-1] * nums[i+1]
        elif op == '/':
            newNums[-1] = newNums[-1] / nums[i+1]
        else:
            newNums.append(nums[i + 1])
            newOps.append(op)
            
    return newNums, newOps

# ([1,6], ['+'])
def addSub(nums, ops):
    result = nums[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += nums[i+1]
        elif op == '-':
            result -= nums[i+1]

    return result

def evalString(string):
    nums, ops = split(string)
    print(nums, ops)
    nums, ops = mulDiv(nums, ops)
    print(nums, ops)
    return addSub(nums, ops)

print(evalString(test))