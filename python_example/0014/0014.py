import json
import xlwt
# jsonstr to python dict data
with open('student.txt') as f:
    f = f.read()
    d=json.load(f)
    print(d)


