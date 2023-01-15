class SomeClass:

    def method_one(self):
        x = 23
        print('method_one', x)

    def method_two(self):
        x = 34
        def func_one():
            # x = 56
            print('func_one', x)
        func_one()
        print('method_two', x)


x = 12
obj = SomeClass()
obj.method_one()
obj.method_two()
print('global', x)