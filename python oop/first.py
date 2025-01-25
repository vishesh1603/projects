class MyClass:
    def __init__(self, _value):
        self._value = _value

    def square(self):
        num = self._value ** 2
        print(num)

s = MyClass(20)
print(s._value)
s.square()
