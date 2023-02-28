from MyCalc import MyCalc
import pytest 

calc = MyCalc()
def test_num_add_num():
    """"rr284 feb 27 - function tests addition of two numbers"""
    data = [{
        "a":"2",
        "b":"3",
        "r":"5"
    },
    {
        "a":"10.0",
        "b":"8",
        "r":"18.0"
    },
    {
        "a":"-5",
        "b":"8",
        "r":"3"
    },]
    for d in data:
        assert calc.add(d["a"], d["b"]) == calc._as_num(d["r"])

def test_ans_add_num():
    """"rr284 feb 27 function tests addition of 2 numbers
        ans is variable which contains the answer from a previous calculation"""
    data = [{
        "a":"ans",
        "b":"3",
        "r":"6"
    },
    {
        "a":"ans",
        "b":"2.5",
        "r":"8.5"
    },
    {
        "a":"ans",
        "b":"-5",
        "r":"3.5"
    },]
    for d in data:
        assert calc.add(d["a"], d["b"]) == calc._as_num(d["r"])

