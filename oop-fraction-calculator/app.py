
class Fraction:

    def __init__(self, numerator, denominator): #parameterized constructor
        self.numerator = numerator
        self.denominator = denominator



    def __str__(self): #if we want to see the object, like how it sees #readable
        return f'{self.numerator}/{self.denominator}'
    

    def __add__(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_deno = self.denominator * other.denominator

        return f'{new_num}/{new_deno}'



    def __sub__(self, other):

        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_deno = self.denominator * other.denominator

        return f'{new_num}/{new_deno}'


    def __mul__(self, other):

        new_num = self.numerator * other.numerator 
        new_deno = self.denominator * other.denominator

        return f'{new_num}/{new_deno}'


    def __truediv__(self, other):
            
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero fraction")
        
            new_num = self.numerator * other.denominator
            new_deno = self.denominator * other.numerator
            
            return Fraction(new_num, new_deno)




if __name__ == "__main__":

    fraction1 = Fraction(3, 4)
    fraction2 = Fraction(1, 2)

    print(fraction1, fraction2)

    print(fraction1 + fraction2)
    
    print(fraction1 - fraction2)
    
    print(fraction1 * fraction2)
    
    print(fraction1 / fraction2)



