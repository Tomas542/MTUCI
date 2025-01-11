def countGoodStrings(low: int = 2, high: int = 3, zero: int = 1, one: int = 2) -> int:
      only_zeroes = 0
      only_ones = 0
      i = low // zero
      while i <= high:
            if zero * i <= high:
                  only_zeroes += 1
            i += 1

      i = low // one
      while i <= high:
            if one * i <= high:
                  only_ones += 1
                  
            i += 1

      print(only_zeroes + only_ones)
      
countGoodStrings()