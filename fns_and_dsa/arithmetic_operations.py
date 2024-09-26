# def perform_operation(num1, num2, operation):
#   match operation:
#     case 'add':
#       return num1 + num2
#     case 'subtract':
#       return num1 - num2
#     case 'multiply':
#       return num1 * num2
#     case 'divide':
#       if num2 == 0:
#         print("Zero(0) division error")
#       else:
#         return num1 / num2
#     case _:
#       print("Enter a valid operator")


def perform_operation(num1, num2, operation):
  if operation == 'add':
    return num1 + num2
  elif operation == 'subtract':
    return num1 - num2
  elif operation == 'multiply':
    return num1 * num2
  elif operation == 'divide':
    if num2 == 0:
      print("Zero(0) division error")
    else:
      return num1 / num2
  else:
    print("Enter a valid operator")


