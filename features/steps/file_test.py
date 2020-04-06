from behave import given, then, when
from time import sleep
# import pandas as pd


@given("Open file")
def open_file(context):
    count = 0
    for i in range(6):
        reader = open("test.txt", "a+")
        reader.write('liza' + str(count) + '\n')
        count += 1
        print(reader.readline())
    reader.close()
    # filepath = "test.txt"
    # with open(filepath) as fp:
    #     line = fp.readline()
    #     cnt = 1
    #     while line:
    #         print("Line {}: {}".format(cnt, line.strip()))
    #         line = fp.readline()
    #         cnt += 1
