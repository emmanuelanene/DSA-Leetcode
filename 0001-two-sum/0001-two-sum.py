class Solution(object):
    # The goal of this method is to find 2 numbers in the list (i.e. nums) that add up to the target (i.e. target)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]       -> This is the Array
        :type target: int      -> This is the target value
        :return type: List[int]
        """

        """
            Initially, previousMap is an empty dictionary.

                *********
                    for i, n in enumerate(nums):
                    difference = target - n
                    if difference in previousMap:
                        return [previousMap[difference], i]
                    previousMap[n] = i
                *********

            HashMap update process 
            First Iteration
                        When you first encounter a number in the list, difference is calculated based on the target and the current number.
                        Since previousMap is empty initially, the difference will not be found.
                        Since the difference value was not found in the hashMap, it will automatically skip the if statement and then adds the current number and its index to previousMap.

                        ANALOGY ->
                        If nums is [2, 7, 11, 15] and target is 9, and we start with i = 0 and n = 2, then difference = 9 - 2 = 7.
                        previousMap is {} (empty), so 7 is not found in it.
                        We then add 2 to previousMap, resulting in previousMap = {2: 0}.


            Subsequent Iterations
                        In the next iteration, the code checks the updated previousMap to see if the difference is present. If yes, the "if" statement will run
                        
                        ANALOGY ->
                        In the second iteration, i = 1 and n = 7, so difference = 9 - 7 = 2.
                        Now previousMap contains {2: 0}, so 2 is found in it.
                        The code then returns [previousMap[2], 1], which is [0, 1], because 2 was at index 0 and 7 is at index 1.

        """
        # HashMap to hold values. It's empty at the start. 
        previousMap = {}
        
        """
        enumerate(nums) is a built-in function that returns both the index (i) and the value (n) of each element in the list nums.
       
        i is the index of the current element.
        n is the value of the current element.

        enumerate() helps you access both the position (index) and the value of each element in the list in one go.
        """
        for i, n in enumerate(nums):

            # Here, difference is the number we need to find in the previousMap to make the sum equal to target. 
            # For example, if target is 9 and n is 3, difference would be 6.
            difference = target - n

            """
            This checks if the required number (the difference) is already in the previousMap. 
            If it is, then we have found two numbers that sum up to target. The indices of these numbers are previousMap[difference] and i.

            "difference" is a number we need to find to complete the pair that sums up to the target.
            "previousMap" is a dictionary where keys are numbers from the nums list, and values are their indices.
            
            This line checks if difference (a number we need) is already in previousMap.
            For example, if target is 9, and we are currently at the number 3, then difference would be 9 - 3 = 6. 
            We are checking if 6 is already in previousMap.
            """
            if difference in previousMap:
                """
                If difference (6) is in previousMap, it means we have already seen a number that, when added to the current number n, equals the target.
                
                previousMap[difference] gives us the INDEX of the previously seen number (i.e. 6) that, along with the current number (3), adds up to target.
                i is the current index of the number in the list (3).
                """
                return [previousMap[difference], i]     # THIS IS WHAT YOU SEE IN THE CONSOLE/OUTPUT/EXPECTED
            

            # THis is an array not a dictionary. Don't get confused. In a dictionary the item you add in the position of [n] is actually the KEY and the item you add in i is the VALUE
            # Don't confuse this with arrays whereby the "Array(0) = 1" -> 0 is the index && 1 is the value. THERE IS A DIFFERENCE
            previousMap[n] = i


        # If the loop completes and no pair is found that sums up to target, the method returns an empty list.
        return []