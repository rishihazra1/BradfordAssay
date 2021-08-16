import numpy as np
def get_best_fit_line(x_terms, y_terms):
    x = np.array(x_terms)
    y = np.array(y_terms)
    a, b, c = np.polyfit(x, y, 2)
    return a, b, c
