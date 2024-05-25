class tf:
    @staticmethod
    def _split_number(num):
        num_str = f"{num:.15f}".rstrip('0').rstrip('.')
        if '.' in num_str:
            num1a, num1b = num_str.split('.')
            return int(num1a), int(num1b), len(num1b)
        else:
            return int(num_str), 0, 0

    @staticmethod
    def _align_numbers(num1, num2):
        num1a, num1b, num1d = tf._split_number(num1)
        num2a, num2b, num2d = tf._split_number(num2)
        if num1d > num2d:
            num2b *= 10 ** (num1d - num2d)
        elif num1d < num2d:
            num1b *= 10 ** (num2d - num1d)
        num1c = int(f"{num1a}{num1b}")
        num2c = int(f"{num2a}{num2b}")
        scale_factor = 10 ** max(num1d, num2d)
        return num1c, num2c, scale_factor

    @staticmethod
    def plus(num1, num2):
        num1c, num2c, scale_factor = tf._align_numbers(num1, num2)
        result = (num1c + num2c) / scale_factor
        return result

    @staticmethod
    def minus(num1, num2):
        num1c, num2c, scale_factor = tf._align_numbers(num1, num2)
        result = (num1c - num2c) / scale_factor
        return result

    @staticmethod
    def multiply(num1, num2):
        num1a, num1b, num1d = tf._split_number(num1)
        num2a, num2b, num2d = tf._split_number(num2)
        num1c = int(f"{num1a}{num1b}")
        num2c = int(f"{num2a}{num2b}")
        result = (num1c * num2c) / (10 ** (num1d + num2d))
        return result

    @staticmethod
    def division(num1, num2):
        return num1 / num2
