#!/usr/bin/python3
import subprocess
import re

print("Searching for services to stop...")
result = subprocess.run(["sm", "--status"], capture_output=True, encoding="UTF-8")

# When there is a group in the regex, findall will return a list of tuples of the groups,
# in this case, because there is only one group, it would be a tuple of 1, so it's just
# a list of matches
services = map(lambda x: x, re.findall(r"\|\s+(?P<service>[A-Z_]+)\s+\|", result.stdout))

listOfServices = list(services)
if len(listOfServices) > 0:
    subprocess.run(["sm", "--stop"] + listOfServices)
else:
    print("No services are running.")
