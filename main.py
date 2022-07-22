# Main script of the recommendation engine.

# Packages
import numpy
import matplotlib as plt
import seaborn as sns

# Files
from preprocessing import Preprocessing
from helper_functions import HelperFunctions
# from tco import TCO
from kNN import kNN


def main():
    # Initialize classes
    pp = Preprocessing()
    hf = HelperFunctions()

    # Run the main class f
    pp.run()
    hf.run()

if __name__ == '__main__':
    main()
