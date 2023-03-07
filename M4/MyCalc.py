class MyCalc:   
    ans = 0
    
    def _is_int(self, val):
        """rr284 feb 27 - function checks if the input is an Integer"""
        try:
            val = int(val)
            return True
        except:
            return False
    
    def _is_float(self, val):
        """rr284 feb 27 - function checks if the input is a float"""
        try:
            val = float(val)
            return True
        except:
            return False
    
    def _as_num(self, val):
        """rr284 - function converts inputs to numbers"""
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("Input isn't a number")
            
    def add(self, num1, num2):
        """rr284 feb 27 - Function adds two numbers"""
        if num1 == "ans":
            return self.add(str(self.ans), num2)
        else:
            num1 = self._as_num(num1)
            num2 = self._as_num(num2)
            self.ans = num1 + num2
        return self.ans
    
    def sub(self, num1, num2):
        """rr284 feb 27 - function subtracts two numbers"""
        if num1 == "ans":
            return self.sub(str(self.ans), num2)
        else:
            num1 = self._as_num(num1)
            num2 = self._as_num(num2)
            self.ans = num1 - num2
        return self.ans
    
    def mul(self, num1, num2):
        """rr284 feb 27 - The function multiplies two numbers given as input"""
        if num1 == "ans":
            return self.mul(str(self.ans), num2)
        else:
            num1 = self._as_num(num1)
            num2 = self._as_num(num2)
            self.ans = num1 * num2
        return self.ans
    
    def div(self, num1, num2):
        """rr284 feb 27 - The function divides two numbers given as input"""
        if num1 == "ans":
            return self.div(str(self.ans), num2)
        else:
            num1 = self._as_num(num1)
            num2 = self._as_num(num2)
            if num2 == 0:
                print(f"{num1}Cannot be divided by zero")
            else:
                self.ans = num1 / num2
        return self.ans
     
if __name__ == "__main__":
    calc = MyCalc()
    is_running = True
    
    prompt = input("Are you ready? ")
    
    if prompt == "yes" or prompt == "y":
        while is_running:
            prompt = input("Enter your equation: ")
            if prompt == "quit" or prompt == "q":
                is_running = False
            else:
                print("Your equation was " + str(prompt))
                if "+" in prompt:
                    nums = prompt.split("+")
                    output = calc.add(nums[0].strip(), nums[1].strip())
                    print("Ans is " + str(output))
                
                # must be done before - check to handle negative values    
                elif "/" in prompt:
                    nums = prompt.split("/")
                    output = calc.div(nums[0].strip(), nums[1].strip())
                    print("Ans is " + str(output))
                
                elif "*" in prompt or "x" in prompt:
                    nums = prompt.split("*") if "*" in prompt else prompt.split("x")
                    output = calc.mul(nums[0].strip(), nums[1].strip())
                    print("Ans is " + str(output))
                
                # must be done last so negative numbers work
                elif "-" in prompt:
                    nums = prompt.split("-")
                    output = calc.sub(nums[0].strip(), nums[1].strip())
                    print("Ans is " + str(output))
    
    else:
        print("Adios")
        is_running = False