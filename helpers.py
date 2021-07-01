import re

# Convert .env data into python dict structure which can be used to set environment variables as os.environ.update(dict)
#
# Based on https://stackoverflow.com/questions/40216311/reading-in-environment-variables-from-an-environment-file
# @see https://docs.python.org/3/library/re.html
# @see https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
def dot_env_vars(file):
    reg = re.compile(r"^([^=]+)\=(.*)$|$")

    with open('.env', 'r') as file:
        vars_dict = dict(
            tuple(reg.findall(line))[0]
                for line in file.readlines()
                    if not line.startswith('#') and (not len(line.strip()) == 0)
        )

    return vars_dict