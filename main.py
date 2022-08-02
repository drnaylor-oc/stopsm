#!/usr/bin/python3add 
import subprocess
import re

result = subprocess.run(["sm", "--status"], capture_output=True, encoding="UTF-8")
stdout = result.stdout
services = map(lambda x: x, re.findall("\|\s+(?P<service>[A-Z_]+)\s+\|", stdout))
result = subprocess.run(["sm", "--stop"] + list(services))