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

def test_num_sub_num():
    """"rr284 feb 27 function tests the subtraction of 2 numbers """
    data = [{
        "a":"8",
        "b":"5",
        "r":"3"
    },
    {
        "a":"7.5",
        "b":"6",
        "r":"1.5"
    },
    {
        "a":"-10",
        "b":"4",
        "r":"-14"
    },]
    for d in data:
        assert calc.sub(d["a"], d["b"]) == calc._as_num(d["r"])

def test_ans_sub_num():
    """"rr284 feb 27 - function tests the subtraction of 2 numbers
        ans is variable which contains the answer from a previous calculation"""
    data = [{
        "a":"ans",
        "b":"5",
        "r":"-19"
    },
    {
        "a":"ans",
        "b":"6.5",
        "r":"-25.5"
    },
    {
        "a":"ans",
        "b":"-5",
        "r":"-20.5"
    },]
    for d in data:
        assert calc.sub(d["a"], d["b"]) == calc._as_num(d["r"])

def test_num_mul_num():
    """"rr284 feb 27 -  function tests the multiplication of 2 numbers"""
    data = [{
        "a":"6.0",
        "b":"0",
        "r":"0"
    },
    {
        "a":"4",
        "b":"5",
        "r":"20"
    },
    {
        "a":"-3",
        "b":"4",
        "r":"-12"
    },]
    for d in data:
        assert calc.mul(d["a"], d["b"]) == calc._as_num(d["r"])

def test_ans_mul_num():
    """"rr284 feb 27 function tests the multiplication of 2 numbers
        ans is variable which contains the answer from a previous calculation"""
    data = [{
        "a":"ans",
        "b":"-2",
        "r":"24"
    },
    {
        "a":"ans",
        "b":"1.5",
        "r":"36.0"
    },
    {
        "a":"ans",
        "b":"0",
        "r":"0"
    },]
    for d in data:
        assert calc.mul(d["a"], d["b"]) == calc._as_num(d["r"])

def test_num_div_num():
    """"rr284 feb 27 function tests the Division of 2 numbers"""
    data = [{
        "a":"10",
        "b":"2.5",
        "r":"4"
    },
    {
        "a":"45",
        "b":"-3",
        "r":"-15"
    },
    {
        "a":"-9",
        "b":"-3",
        "r":"3"
    },
    # Dividing by zero will keep the same answer while throwing an error msg
    {
        "a":"3",
        "b":"0",
        "r":"3"
    },]
    for d in data:
        assert calc.div(d["a"], d["b"]) == calc._as_num(d["r"])

def test_ans_div_num():
    """"rr284 feb 27 function tests the Division of 2 numbers
        ans is variable which contains the answer from a previous calculation"""
    data = [{
        "a":"ans",
        "b":"0.25",
        "r":"12"
    },
    {
        "a":"ans",
        "b":"2",
        "r":"6"
    },
    {
        "a":"ans",
        "b":"-2",
        "r":"-3"
    },
    # Dividing by zero will keep the same answer while throwing an error msg
    {
        "a":"ans",
        "b":"0",
        "r":"-3"
    },]
    for d in data:
        assert calc.div(d["a"], d["b"]) == calc._as_num(d["r"])

