import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = '1 2 3\n4 5 6 7'
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
    assert len(main.main.shuffle) == 7
    assert main.main.shuffle[0] == 1
    assert main.main.shuffle[1] == 4
    assert main.main.shuffle[2] == 2
    assert main.main.shuffle[3] == 5
    assert main.main.shuffle[4] == 3
    assert main.main.shuffle[5] == 6
    assert main.main.shuffle[6] == 7


def test_main_2():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = '1 2 3 4 5\n6 7 8'
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
    assert len(main.main.shuffle) == 8
    assert main.main.shuffle[0] == 1
    assert main.main.shuffle[1] == 6
    assert main.main.shuffle[2] == 2
    assert main.main.shuffle[3] == 7
    assert main.main.shuffle[6] == 4
    assert main.main.shuffle[7] == 5
