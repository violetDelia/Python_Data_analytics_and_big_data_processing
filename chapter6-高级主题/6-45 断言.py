

def assert_test(param):
    assert param == "hello"
    return param + ",world"


try:
    result = assert_test("hello1")
    print("结果是：", result)
except AssertionError as e:
    print(e.__dict__)


