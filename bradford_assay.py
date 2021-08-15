from set_baseline import set_default_baseline
from input_validation import get_y_or_no, get_float, get_int
path = set_default_baseline()
use_default = get_y_or_no("Use default baselines?")
if use_default == "n":
    print("Program terminated.\n Edit baselines here: " + path)
    quit()
print("Protein used: 5µL\n" + "Dilution of protein solution: 0.1\n")
info_correct = get_y_or_no("Is the above information correct?")
if info_correct == "n":
    protein_used = get_float("Enter the amount of protein used (in µL).\n")    
    dilution = get_float("Enter the dilution.\n")
else:
    protein_used = 5
    dilution = 0.1
dilution_factor = (protein_used/20)*dilution
print("dilution factor: " + str(dilution_factor))
absorption = get_float("Enter absorption.\n")


