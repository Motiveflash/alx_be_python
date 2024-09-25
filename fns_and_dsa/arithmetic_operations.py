def perform_operation(num1, num2, operation ):
  
  match operation:
    case "+":
      return num1 + num2
    case "-":
      return num1 - num2
    case "*":
      return num1 * num2
    case "/":
      if num2 == 0:
        print("Zero(0) division error")
      else:
        return num1 / num2
    case _:
      print("Enter a valid operator")