class Calculate(object):
    def add(self, x, y):
        """
        Takes two integers and adds them together to produce the result.
        >>> c = Calculate()
        >>> c.add(1,1)
        2

        >>> c.add(25, 125)
        150

        >>> c.add(1.0, 1.0)
        Traceback (most recent call last):
        ...
        TypeError: Invalid type: <type 'float'> and <type 'float'>

        :param x:
        :param y:
        :return: :raise TypeError:
        """
        if type(x) == type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))


if __name__ == '__main__':  # pragma: no cover
    calc = Calculate()
    result = calc.add("Hello", "World")
    # print result
