
class FizzBuzz:
    """FizzBuzz"""

    def run(self, start, stop):
        """Run the game"""
        result = ""
        for i in range(start, stop):
            result += str(i)
        return result
