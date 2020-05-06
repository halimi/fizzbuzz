
class FizzBuzz:
    """FizzBuzz"""

    def run(self, start, stop):
        """Run the game"""
        result = []
        for i in range(start, stop):
            if i % 3 == 0:
                result.append("Fizz")
            else:
                result.append(str(i))
        return ", ".join(result)
