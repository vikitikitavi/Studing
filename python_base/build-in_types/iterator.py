class MyIterator:

    def __init__(self, *args, stopper=False, stop_object_value=None, stop_object_type=None):
        self.args = args
        self.index = 0
        self.stopper = stopper
        self.stop_object = stop_object_value
        self.stop_object_type = stop_object_type
        print(self.args)

    def __iter__(self):
        return self

    def __next__(self):
        if not len(self.args) <= self.index:
            result = self.args[self.index]
            self.index += 1
            self._iterator_should_continue(result)
            return result
        else:
            self.index = 0
            raise StopIteration

    def _iterator_should_continue(self, result):
        if not self.stopper:
            return
        if isinstance(result, self.stop_object_type):
            print("Iterator was stopped")
            raise StopIteration
        if result == self.stop_object:
            print("Iterator was stopped")
            raise StopIteration


iteration_set = [1, 2, 3, 4, 5, 6, "stopIterHere", 7, 8]
d = MyIterator(*iteration_set, stopper=True, stop_object_type=str)

for item in d:
    print(item)

for further_item in d:
    print(further_item)
