def get_valid_input_float(input_prompt):
    while True:
        input_holder = input(input_prompt)
        print(type(input_holder))
        try:
            input_holder = float(input_holder)
            return input_holder
        except:
            ValueError
            print("Invalid input. Enter valid input of type: " + "float" + "\n") 

def get_valid_input_int(input_prompt):
    while True:
        input_holder = input(input_prompt)
        print(type(input_holder))
        try:
            input_holder = int(input_holder)
            return input_holder
        except:
            ValueError
            print("Invalid input. Enter valid input of type: " + "int" + "\n")
            
def get_valid_input_y_or_n(input_prompt):
    while True:
        inupt_holder = input(input_prompt + " (y/n)\n")
        if inupt_holder == "y" or inupt_holder == "n":
            break
        else:
            print("Invalid input. Enter y or n.")
    return inupt_holder

