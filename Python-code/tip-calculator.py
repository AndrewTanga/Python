def get_final_tips(total2, tip2, people2):
  grand_total = tip2 / 100 * total2 + total2
  each_person = grand_total / people2
  final_amount = round(each_person, 2)
  print(f"Each person should pay: ${final_amount}")
 
def calculator():
  def get_valid_input_number(user_message, type_of_number):
    user_input = input(user_message)
    if user_input.isdigit():
      if type_of_number == "decimal":
        return float(user_input)
      if type_of_number == "integer":
        return int(user_input)
    else:
      print("Please enter digits only!")
      return get_valid_input_number(user_message, type_of_number)
      
  print("Welcome to the tip calculator ver2")
  total_bill = get_valid_input_number("What was the total bill: $", "decimal")
  tip_amount = get_valid_input_number("What percentage do you want to give? ", "integer")
  people_number = get_valid_input_number("How many people to split ", "integer")
  get_final_tips(total_bill, tip_amount, people_number)
  
print("Program starting...")
calculator()
print("Program ending...")