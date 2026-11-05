"""build a dynamic array"""

class DynamicArray:
    def __init__(self):
        self.capacity = 1 # capacity: number of memory blocks allocated to the array
        self._data = [None] * self.capacity # the underlying structure has a number of blocks 
        self.size = 0 
        self.copies = 0

    def __len__(self):
        """the number of items stored, not the capacity"""
        return self.size

    def append(self, item):
        # if block is full
        if len(self) == self.capacity:
            # make the block twice as big, and track the number of copies
            self.capacity *= 2

            # copy the items over 1 at a time
            tmp = [None] * self.capacity
            for idx in range(self.size):
                tmp[idx] = self._data[idx]
                self.copies+=1
            self._data = tmp

        # find the first index that is not none, and assign item to it
        self._data[self.size] = item
        self.size += 1

    def __getitem__(self, i):
        # return item i for 0 ≤ i < len, and otherwise raise IndexError.
        if i >= 0  and i < self.size:
            return self._data[i]
        else:
            raise IndexError

if __name__ == "__main__":
    a = DynamicArray()

    # TEST 1: check empty array is length 0
    assert len(a) == 0; print("Empty array is length 0")

    # TEST 2: append 0 through 16, check capacity, copies, etc.
    for i in range(17):
        a.append(i)

    assert all(a[i] == i for i in range(17))
    assert len(a) == 17; print(f"len(a)={len(a)}")
    assert a.capacity == 32; print(f"a.capacity={a.capacity}")
    assert a.copies == 31; print(f"a.copies={a.copies}")
    try:
        a[17]
        assert False, "expected IndexError"
    except IndexError:
        print("IndexError correctly thrown")
        pass

    a = DynamicArray()
    for n in range(10**5+1):
        a.append(n)
        if n in (10**3, 10**4, 10**5):
            assert a.copies / n < 2; print(f"a.copies / {n} < 2")

        


    



