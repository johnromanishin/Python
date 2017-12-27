import time

test_test = {}

test_test["banana"] = 56

while(1):
    time.sleep(3)
    test_test[time.time()] = "APPLE"
    print(test_test)
