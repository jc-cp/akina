# In this file all helper functions not part of the main class should be included

# Helper function to convert NaN to 0, if there are any, and all other years to integers.
def convert_int(x):
    try:
        return int(x)
    except:
        return 0
