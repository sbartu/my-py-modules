class Memoize:
    """A class decorator for memoizing functions."""

    def __init__(self, fn):
        """
        Store given function fn and create 
        an empty dictionary for memoization.
        """
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        """
        Check if result exists in dict. If its not,
        store the output with args as key.
        """
        if args not in self.memo:
            self.memo[args] = self.fn(*args)

        return self.memo[args]
