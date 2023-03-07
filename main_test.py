import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = '1 2 3\n4 5 6 7 8'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
    assert len(main.main.merged) == 8
    assert main.main.merged[0] == 1
    assert main.main.merged[2] == 3
    assert main.main.merged[6] == 7
    assert main.main.merged[7] == 8


def test_main_2():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = '10 5 25 75 85\n55 60 45'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
    assert len(main.main.merged) == 8
    assert main.main.merged[0] == 55
    assert main.main.merged[2] == 45
    assert main.main.merged[6] == 75
    assert main.main.merged[7] == 85
