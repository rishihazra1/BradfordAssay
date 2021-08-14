from set_baseline import set_default_baseline
import input_validation
path = set_default_baseline()
use_default = input_validation.get_valid_input_y_or_n("Use default baselines?")
if use_default == "n":
    print("Program terminated.\n Edit baselines here: " + path)
    quit()
print("Protein used: 5µL\n" + "Dilution of protein solution: 0.1\n")
info_correct = input_validation.get_valid_input_y_or_n("Is the above information correct?")
if info_correct == "n":
    protein_used = input_validation.get_valid_input_float("Enter the amount of protein used (in µL).\n")    
    dilution = input_validation.get_valid_input_float("Enter the dilution.")
else:
    protein_used = 5
    dilution = 0.1
dilution_factor = (protein_used/20)*dilution
print("dilution factor: " + dilution_factor)
absorption = input_validation.get_valid_input_float("Enter absorption.\n")


