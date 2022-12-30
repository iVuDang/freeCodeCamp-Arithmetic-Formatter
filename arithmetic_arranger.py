problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
problems_2 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

problems_six = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "1 + 1", "2 - 1"]
problems_signs = ["32 + 8", "1 - 3801", "9999 + 9999", "523 * 49"]
problems_non_digit = ["hi + 8", "1 - 3801", "9999 + 9999", "523 + 49"]
problems_five = ["32222 + 8", "1 - 3801", "9999 + 9999", "523 + 49"]

def arithmetic_arranger(problems: list, calc = False) -> str:
# 'calc = False' 'is setting a default parameter  
    arranged_problems = ''
  
    # The limit is five, anything more will return: Error: Too many problems.
    if (len(problems) > 5): 
      return 'Error: Too many problems.'
      
    list_of_lists = []
    # [['32', '+', '8'], ['1', '-', '3801'], ['9999', '+', '9999'], ['523', '-', '49']]
  
    for problem_strings in problems:
      lists = problem_strings.split(' ')
      list_of_lists.append(lists)

    list_of_numbers = []
    list_of_operators = []
    # ['+', '-', '+', '-']


    for item in list_of_lists:
      list_of_numbers.append(item[0])
      list_of_operators.append(item[1])
      list_of_numbers.append(item[2])

    # Multiplication and division will return an error: Error: Operator must be '+' or '-'.
    for operators in list_of_operators:
      if (operators not in ['+', '-']):
        return "Error: Operator must be '+' or '-'."
    
    # Each number (operand) should only contain digits, or: Error: Numbers must only contain digits.
    # Each operand has a max of four digits or: Error: Numbers cannot be more than four digits.
    for operands in list_of_numbers:
      if (not operands.isdigit()):
        return "Error: Numbers must only contain digits."
      if (len(operands) > 4):
        return "Error: Numbers cannot be more than four digits."

    # String Accumulator variables 
    first_row_operand = ""
    second_row_operator_operand = ""
    third_row_dashes = ""
    fourth_row_solution = ""

    for item in list_of_lists:
      # Determine distance between blocks, by taking the longest operand
      width_between_operands = max(len(item[0]), len(item[2])) # -> integer

      # By finding the longest operand, we can use this as the fixed width 
      # We need to + 2, because the second row has a operator and a space
      first_row_operand += f"{item[0].rjust(width_between_operands + 2)}    "
      second_row_operator_operand += f"{item[1]} {item[2].rjust(width_between_operands)}    "
      third_row_dashes += (width_between_operands + 2) * '-' + '    '

      if (item[1] == '+'):
        solution = int(item[0]) + int(item[2])
      else:
        solution = int(item[0]) - int(item[2])
        
      fourth_row_solution += f"{str(solution).rjust(width_between_operands + 2)}    "

    # Remove the trailing spaces for the last item. 
    # Needs to be '123\n', not '123    \n'
    first_row_operand = first_row_operand.rstrip()
    second_row_operator_operand = second_row_operator_operand.rstrip()
    third_row_dashes = third_row_dashes.rstrip()
    fourth_row_solution = fourth_row_solution.rstrip()
  
    if (calc == True): 
      arranged_problems = first_row_operand + "\n" + second_row_operator_operand + "\n"  + third_row_dashes + '\n' + fourth_row_solution
    else: 
      arranged_problems = first_row_operand + "\n" + second_row_operator_operand + "\n"  + third_row_dashes
  
    return arranged_problems
      

print(arithmetic_arranger(problems, True))
print("\n")
print(arithmetic_arranger(problems_2, True))

"""
# TESTS
print(arithmetic_arranger(problems))
print(arithmetic_arranger(problems, True))
print(arithmetic_arranger(problems_six))
print(arithmetic_arranger(problems_signs))
print(arithmetic_arranger(problems_non_digit))
print(arithmetic_arranger(problems_five))
"""