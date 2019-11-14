terms = ''

def call_model(string):
    if type(string) == str:
        temp = ''
        temp = string[0:10]
        return "test passed, input was a string that started with: ", temp
    else:
        return "test failed, input was not a string"

print(call_model('testing123123123123'))