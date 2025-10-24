"""
Look up how to use the argv module in python
Run this program as command line and use the argv module to indicate the logging level
Write your logging code to have all the levels of severity
Practice using the different levels of severity on your dog code below. be creative!

"""
import argparse
import logging

def helpDoc():
    return """
    This program demonstrates logging levels using a Dog class.
    You can set the logging level using the --log argument.
    Example usage:
        python 07_02_log_the_dog.py --log DEBUG
    Available logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    """

parser = argparse.ArgumentParser(description="Set the logging level.")
parser.add_argument(
    "--log",
    type=int,
    default="WARNING",
    help="Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
)
args = parser.parse_args()
levels=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
logging.basicConfig(level=levels[args.log-1]C, format='%(asctime)s - %(levelname)s - %(message)s')

class Dog:
    def __init__(self, limbs=None, eyes=None, color=None, kindness=None):
        self.limbs = limbs
        self.eyes = eyes
        self.color = color
        self.kindness = kindness  # nice, mean, angry, sad, lonely
        logging.debug(f"Creating a dog with {self.limbs} limbs, {self.eyes} eyes, color {self.color}, kindness {self.kindness}")
        ## write some logging code in here
        ## if limbs < 4 -- log a warning! dog needs help (it's missing legs!)
        if self.limbs is not None and self.limbs < 4:
            logging.warning("Dog has less than 4 limbs! It might need help.")
        ## if kindness is sad or lonely, log a warning. If it's mean or angry it's critical! we must be careful
        if self.kindness.lower() in ["sad", "lonely"]:
            logging.warning(f"Dog is feeling {self.kindness}. It might need some attention.")
        elif self.kindness.lower() in ["mean", "angry"]:
            logging.critical(f"Dog is feeling {self.kindness}. It might be dangerous!")

if __name__ == "__main__":
    a = Dog(limbs=3, eyes=1, color="red", kindness="nice")
    b = Dog(limbs=4, eyes=2, color="blue", kindness="mean")
    c = Dog(limbs=2, eyes=2, color="green", kindness="sad")
    d = Dog(limbs=4, eyes=2, color="yellow", kindness="angry")
    e = Dog(limbs=4, eyes=2, color="purple", kindness="lonely")
    f = Dog(limbs=4, eyes=2, color="black", kindness="happy") 

