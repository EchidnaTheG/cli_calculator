class Calculator:
    def __init__(self, *numbers):
        self.numbers= list(numbers)
    
    def add(self):
        total = 0
        for number in range(len(self.numbers)):
            total += self.numbers[number] 
        return total
    
    def subtract(self):
        total = self.numbers[0]
        for number in range(1 ,len(self.numbers)):
            total -= self.numbers[number]
        return total
        
    def multiply(self):
        total = 1
        for number in range(len(self.numbers)):
            total *= self.numbers[number]
        return total
        
    def divide(self):
        total = self.numbers[0]
        for number in range(1,len(self.numbers)): 
            total /= self.numbers[number]
        return total
    
    def exponentiation(self):
        total = self.numbers[0]
        for number in range(1,len(self.numbers)): 
            total = total ** self.numbers[number]
        return total
    
    # 4 1 2