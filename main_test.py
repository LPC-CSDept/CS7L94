import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    emp_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New York"}
    main.printDict(emp_dict)
    org_keyval = 'city'
    new_keyval = 'location'
    main.changeKey(emp_dict, org_keyval, new_keyval)
    main.printDict(emp_dict)

    assert len(emp_dict) == 4
    assert emp_dict['location'] == 'New York'
    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
