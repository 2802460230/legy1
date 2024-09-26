def arithmetic_mode():
  expr = input("give me ze expression: ").replace(" ", "")

  plus_count = expr.count("+")
  minus_count = expr.count("-")
  multiply_count = expr.count("x")
  divide_count = expr.count("/")

  def evaluate(expression):
      while '/' in expression:
          for i in range(len(expression)):
              if expression[i] == '/':
                  left = i - 1
                  right = i + 1
                  result = float(expression[left]) / float(expression[right])
                  expression = expression[:left] + [str(result)] + expression[right+1:]
                  break

      while 'x' in expression:
          for i in range(len(expression)):
              if expression[i] == 'x':
                  left = i - 1
                  right = i + 1
                  result = float(expression[left]) * float(expression[right])
                  expression = expression[:left] + [str(result)] + expression[right+1:]
                  break

      while '-' in expression:
          for i in range(len(expression)):
              if expression[i] == '-':
                  left = i - 1
                  right = i + 1
                  result = float(expression[left]) - float(expression[right])
                  expression = expression[:left] + [str(result)] + expression[right+1:]
                  break

      while '+' in expression:
          for i in range(len(expression)):
              if expression[i] == '+':
                  left = i - 1
                  right = i + 1
                  result = float(expression[left]) + float(expression[right])
                  expression = expression[:left] + [str(result)] + expression[right+1:]
                  break

      return expression[0]

#this part was chatgpt-ed
  tokens = []
  num = ""
  for char in expr:
      if char.isdigit() or char == '.':
          num += char
      else:
          if num:
              tokens.append(num)
              num = ""
          tokens.append(char)
  if num:
      tokens.append(num)

  result = evaluate(tokens)
  print(f"Result: {result}")


def triangular_mode():
  a = float(input("Enter the length of side A: "))
  b = float(input("Enter the length of side B: "))
  c = float(input("Enter the length of side C: "))

    #this part is also chat gpt-ed
  s = (a + b + c) / 2

  area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

  print(f"The area of the triangle is: {area}")


def calculator():
  while True:
      mode = input("choose ze mode: [1] Arithmetic, [2] Triangular: ")

      if mode == "1":
          arithmetic_mode()
      elif mode == "2":
          triangular_mode()
      else:
          print("fk off")
      cont = input("more calculation yes? (y/n): ")
      if cont.lower() != "y":
          break

calculator()
