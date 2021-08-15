import baseline
from input_validation import get_y_or_no, get_float, get_int
'''
path = baseline.set_default_baseline()
use_default = get_y_or_no("Use default baselines?")
if use_default == "n":
    print("Program terminated.\n Edit baselines here: " + path)
    quit()
'''
baselines = [['20', '0', '1.000', '1.258', '1.155'], ['15', '5', '0.750', '1.083', '1.098'], ['10', '10', '0.500', '0.728', '0.713'], ['5', '15', '0.250', '0.422', '0.402'], ['2.5', '17.5', '0.125', '0.223', '0.214'], ['0', '20', '0.000', '0', '-0.005']]
print("baselines: " + str(baselines))
x_terms, y_terms = baseline.calculate_baselines(baselines)
print(x_terms, y_terms)

print("\nProtein used: 5µL\n" + "Dilution of protein solution: 0.1")
info_correct = get_y_or_no("Is the above information correct?\n")
if info_correct == "n":
    protein_used = get_float("Enter the amount of protein used (in µL).\n")    
    dilution = get_float("Enter the dilution.\n")
else:
    protein_used = 5
    dilution = 0.1
dilution_factor = (protein_used/20)*dilution
print("dilution factor: " + str(dilution_factor))
absorption = get_float("Enter absorption.\n")

