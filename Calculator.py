import math
class CalcOne():
    def __init__(self, a):
        self.a = a
    def root(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Square root of {self.a} is {math.sqrt(self.a)}') + '\n')
        return print(f'Output: Square root of {self.a} is {math.sqrt(self.a)}')
    def fact(self):
        fac = 1
        for i in range(self.a):
            fac = fac * (i + 1)
        with open("History.txt", "a") as file:
            file.write(str(f'Factorial of {self.a} is {fac}') + '\n')
        return print(f'Output: Factorial of {self.a} is {fac}')
    def absolute(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Absolute value of {self.a} is {abs(self.a)}') + '\n')
        return print(f'Output: Absolute value of {self.a} is {abs(self.a)}')
    def sin(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Sin of {self.a} degrees is {round(math.sin(self.a), 2)}') + '\n')
        return print(f'Output: Sin of {self.a} degrees is {round(math.sin(self.a), 2)}')
    def cos(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Cos of {self.a} degrees is {round(math.cos(self.a), 2)}') + '\n')
        return print(f'Output: Cos of {self.a} degrees is {round(math.cos(self.a), 2)}')
    def tan(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Tan of {self.a} degrees is {round(math.tan(self.a), 2)}') + '\n')
        return print(f'Output: Tan of {self.a} degrees is {round(math.tan(self.a), 2)}')
    def sec(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Cosine of {self.a} is {round(1 / math.sin(self.a), 2)}') + '\n')
        return print(f'Output: Cosine of {self.a} is {round(1 / math.sin(self.a), 2)}')
    def cosec(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Cosec of {self.a} degrees is {round(1 / math.cos(self.a), 2)}') + '\n')
        return print(f'Output: Cosec of {self.a} degrees is {round(1 / math.cos(self.a), 2)}')
    def cot(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Cot of {self.a} degrees is {round(1 / math.tan(self.a), 2)}') + '\n')
        return print(f'Output: Cot of {self.a} degrees is {round(1 / math.tan(self.a), 2)}')
    def log(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Log of {self.a} to the base 10 is {math.log(self.a, 10)}') + '\n')
        return print(f'Output: Log of {self.a} to the base 10 is {math.log(self.a, 10)}')
    def deg(self):
        with open("History.txt", "a") as file:
            file.write(str(f'{self.a} radians is {round(math.degrees(self.a), 2)} degrees') + '\n')
        return print(f'Output: {self.a} degrees is {round(math.radians(self.a), 2)} radians')
    def rad(self):
        with open("History.txt", "a") as file:
            file.write(str(f'{self.a} degrees is {round(math.radians(self.a), 2)} radians') + '\n')
        return print(f'Output: {self.a} radians is {round(math.degrees(self.a), 2)} degrees')
    def bin(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Binary Equivalent of {self.a} is {bin(self.a)}') + '\n')
        return print(f'Output: Binary Equivalent of {self.a} is {bin(self.a)}')
    def dec(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Decimal Equivalent of {self.a} is {int(self.a, 2)}') + '\n')
        return print(f'Output: Decimal Equivalent of {self.a} is {int(self.a, 2)}')
    def comroot(self):
        if (type(self.a) == complex):
            b = self.a
            d = (b.real * b.real)+ (b.imag * b.imag)
            print(d)
            with open("History.txt", "a") as file:
                file.write(str(f'Sqaure root of {self.a}is {round(math.sqrt(d), 2)}') + '\n')
        return print(f'Output: Sqaure root of {self.a} is {round(math.sqrt(d), 2)}')
class CalcTwo():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        with open("History.txt", "a") as file:
            file.write(str(f"Sum of {self.a} and {self.b} is {self.a + self.b}") + '\n')
        return print(f"Output: Sum of {self.a} and {self.b} is {self.a + self.b}")
    def diff(self):
        with open("History.txt", "a") as file:
            file.write(str(f"Difference between {self.a} and {self.b} is {self.a - self.b}") + '\n')
        return print(f"Output: Difference between {self.a} and {self.b} is {self.a - self.b}")
    def mul(self):
        with open("History.txt", "a") as file:
            file.write(str(f"Product of {self.a} and {self.b} is {self.a * self.b}") + '\n')
        return print(f"Output: Product of {self.a} and {self.b} is {self.a * self.b}")
    def div(self):
        with open("History.txt", "a") as file:
            file.write(str(f"Quotient of {self.a} and {self.b} is {round(self.a / self.b, 2)}") + '\n')
        return print(f"Output: Quotient of {self.a} and {self.b} is {round(self.a / self.b, 2)}")
    def rem(self):
        with open("History.txt", "a") as file:
            file.write(str(f"Remainder of {self.a} divided by {self.b} is {round(self.a % self.b, 2)}") + '\n')
        return print(f"Output: Remainder of {self.a} divided by {self.b} is {round(self.a % self.b, 2)}")
    def maxi(self):
        with open("History.txt", "a") as file:
            file.write(str(f"Maximum between {self.a} and {self.b} is {max(self.a, self.b)}") + '\n')
        return print(f"Output: Maximum between {self.a} and {self.b} is {max(self.a, self.b)}")
    def mini(self):
        with open("History.txt", "a") as file:
            file.write(str(f"Minimum between {self.a} and {self.b} is {min(self.a, self.b)}") + '\n')
        return print(f"Output: Minimum between {self.a} and {self.b} is {min(self.a, self.b)}")
    def power(self):
        with open("History.txt", "a") as file:
            file.write(str(f"{self.a} to the power {self.b} is {round(pow(self.a, self.b), 2)}") + '\n')
        return print(f"Output: {self.a} to the power {self.b} is {round(pow(self.a, self.b), 2)}")
    def log(self):
        with open("History.txt", "a") as file:
            file.write(str(f'Log of {self.a} to the base {self.b} is {round(math.log(self.a, self.b), 2)}') + '\n')
        return print(f'Output: Log of {self.a} to the base {self.b} is {round(math.log(self.a, self.b), 2)}')  
class Matrix():
    
    def add(self):
        matrix1 = []
        matrix2 = []
        r1 = int(input("Enter number of rows of first matrix: "))
        c1 = int(input("Enter number of columns of first matrix: "))
        r2 = int(input("Enter number of rows of second matrix: "))
        c2 = int(input("Enter number of columns of second matrix: "))
        if (r1 == r2 and c1 == c2):
            print("Enter elements of first matrix ")
            for i in range(r1):
                a = []
                for j in range(c1):
                    a.append(int(input("Enter element: ")))
                matrix1.append(a)
            print("First Matrix:", matrix1)
            print("Enter elements of second matrix")
            for i in range(r2):
                a = []
                for j in range(c2):
                    a.append(int(input("Enter element: ")))
                matrix2.append(a)
            print("Second Matrix:", matrix2)
            matrix = []
            for i in range(r1):
                a = []
                for j in range(c1):
                    a.append(matrix1[i][j] + matrix2[i][j])
                matrix.append(a)
            with open("History.txt", "a") as file:
                file.write(str(f"Resultant Matrix : {matrix}") + '\n')
            return matrix
        else:
            print("Matrix Addition not possible")
            return 0
        
    def sub(self):
        matrix1 = []
        matrix2 = []
        r1 = int(input("Enter number of rows of first matrix: "))
        c1 = int(input("Enter number of columns of first matrix: "))
        r2 = int(input("Enter number of rows of second matrix: "))
        c2 = int(input("Enter number of columns of second matrix: "))
        if (r1 == r2 and c1 == c2):
            print("Enter elements of first matrix")
            for i in range(r1):
                a = []
                for j in range(c1):
                    a.append(int(input("Enter element: ")))
                matrix1.append(a)
            print("First Matrix:", matrix1)
            print("Enter elements of second matrix")
            for i in range(r2):
                a = []
                for j in range(c2):
                    a.append(int(input("Enter element: ")))
                matrix2.append(a)
            print("Second Matrix:", matrix2)
            matrix = []
            for i in range(r1):
                a = []
                for j in range(c1):
                    a.append(matrix1[i][j] - matrix2[i][j])
                matrix.append(a)
            with open("History.txt", "a") as file:
                file.write(str(f"Resultant Matrix : {matrix}") + '\n')
            return matrix
        else:
            print("Matrix Subraction not possible")
            return 0
    
    def mul(self):
        matrix1 = []
        matrix2 = []
        r1 = int(input("Enter number of rows of first matrix: "))
        c1 = int(input("Enter number of columns of first matrix: "))
        r2 = int(input("Enter number of rows of second matrix: "))
        c2 = int(input("Enter number of columns of second matrix: "))
        if (r2 == c1):
            print("Enter elements of first matrix")
            for i in range(r1):
                a = []
                for j in range(c1):
                    a.append(int(input("Enter element: ")))
                matrix1.append(a)
            print("First Matrix:", matrix1)
            print("Enter elements of second matrix")
            for i in range(r2):
                a = []
                for j in range(c2):
                    a.append(int(input("Enter element: ")))
                matrix2.append(a)
            print("Second Matrix:", matrix2)
            matrix = [[0 for a in range(c2)] for a in range(r1)]
            for i in range(r1):
                for j in range(c2):
                    for k in range(c1):
                        matrix[i][j] += (matrix1[i][k] * matrix2[k][j])
            with open("History.txt", "a") as file:
                file.write(str(f"Resultant Matrix : {matrix}") + '\n')
            return matrix 
        else:
            print("Matrix Multiplication not possible ")
            return 0
class History():
    def recent(self):
        with open("History.txt", "r") as file:
            history = file.read()
            print("Recent History:")
            print(history)
    def clear(self):
        f = open("History.txt", "w")
        f.close()
        
print("Welcome to the Scientific Calculator")
while True:
    try:
        print("\nOperations List: ")
        print("1. One Variable Operations \n2. Two Variables Operations\n3. Matrix Operations\n4. History\n5. Exit")
        a = int(input("Select one of the following operations: "))
        match a:
            case 1:
                while True:
                    try:
                        print("One Variable Operations: ")
                        print("1. Square Root\n2. Square root of Complex Number\n3. Factorial\n4. Absolute\n5. Sin\n6. Cos\n7. Tan\n8. Sec\n9. Cosec\n10. Cot\n11. Log\n12. Degree to Radian\n13. Radian to Degree\n14. Binary Equivalent\n15. Decimal Equivalent\n16. BACK")
                        c = int(input("Choose of one of the operations: "))
                        if (c >= 5 and c <= 10 or c == 12):
                            n1 = eval(input("Enter degrees: "))
                        elif (c == 2):
                            n1 = eval(input("Enter complex number"))
                        elif (c <= 4 or c == 11 or c == 14):
                            n1 = eval(input("Enter number: "))
                        elif (c == 15):
                            n1 = input("Enter binary string: ")
                        elif (c == 13):
                            n1 = eval(input("Enter radians: "))
                        elif (c == 16):
                            n1 = 0
                            print('\n')
                        else:
                            print("Please Enter Valid Operation Number\n")
                            continue
                        res = CalcOne(n1)
                        match c:
                            case 1:
                                res.root()
                            case 2:
                                res.comroot()
                            case 3:
                                res.fact()
                            case 4:
                                res.absolute()
                            case 5:
                                res.sin()
                            case 6:
                                res.cos()
                            case 7:
                                res.tan()
                            case 8:
                                res.sec()
                            case 9:
                                res.cosec()
                            case 10:
                                res.cot()
                            case 11:
                                res.log()
                            case 12:
                                res.deg()
                            case 13:
                                res.rad()
                            case 14:
                                res.bin()
                            case 15:
                                res.dec()
                            case 16:
                                break
                        break
                    except:
                        print("Please Enter Valid Operation Number")

            case 2:
                while True:
                    try:
                        print("Two Variable Operations: ")
                        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder\n6. Find Maximum \n7. Find Minimum\n8. a to the power b\n9. Log\n10. BACK")
                        c = int(input("Choose one of the operations: "))
                        if (c <= 9):
                            n1 = float(input("Enter first number: "))
                            n2 = float(input("Enter second number: "))
                        if (c == 10):
                            print("\n")
                        elif (c > 10):
                            print("Please Enter Valid Operation Number")
                            continue
                        res = CalcTwo(n1, n2)
                        match c:
                            case 1:
                                res.add()
                            case 2:
                                res.diff()
                            case 3:
                                res.mul()
                            case 4:
                                res.div()
                            case 5:
                                res.rem()
                            case 6:
                                res.maxi()
                            case 7:
                                res.mini()
                            case 8:
                                res.power()
                            case 9:
                                res.log()
                            case 10:
                                break
                        break
                    except:
                        print("Please Enter Valid Operation Number")
            
            case 3:
                while True:
                    try:
                        flag = 1
                        print("Matrix Operations: ")
                        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. BACK")
                        c = int(input("Choose a Matrix Operation: "))
                        res = Matrix()
                        match c:
                            case 1:
                                matrix = res.add()
                                if (matrix != 0):
                                    print("Resultant Matrix: ", matrix)
                            case 2:
                                matrix = res.sub()
                                if (matrix != 0):
                                    print("resultant Matrix: ", matrix)
                            case 3:
                                matrix = res.mul()
                                if (matrix != 0):
                                    print("Resultant Matrix: ")
                                    for row in matrix:
                                        print(row)
                            case 4:
                                break
                            case default:
                                print("Please Enter Valid Operation Number")
                                flag = 0
                        if (flag == 1):
                            break
                    except:
                        print("Please Enter Valid Operation Number")
    
            case 4:
                while True:
                    try:
                        flag = 1
                        print("1. Recent History\n2. Clear History\n3. BACK")
                        b = int(input("Choose one of the following operations: "))
                        h = History()
                        match b:
                            case 1:
                                h.recent()
                            case 2:
                                h.clear()
                            case 3:
                                break
                            case default:
                                print("Please Enter Valid Operation Number")
                                flag = 0
                        if (flag == 1):
                            break
                    except:
                        print("Please Enter Valid Operation Number")

            case 5:
                h = History()
                h.clear()
                print("Scientific Calculator Swicthed OFF")
                break

            case default:
                print("Please Enter Valid Operation Number")
        if (a == 5):
            break
    except:
        print("Please Enter Valid Operation Number")
