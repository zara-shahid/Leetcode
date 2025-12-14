class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        
        # Keep consuming fuel while there is fuel in the main tank
        while mainTank > 0:
            if mainTank >= 5:
                # Consume 5 liters
                mainTank -= 5
                distance += 5 * 10  # 10 km per liter

                # Transfer 1 liter if additional tank has fuel
                if additionalTank > 0:
                    mainTank += 1
                    additionalTank -= 1
            else:
                # Consume the remaining fuel
                distance += mainTank * 10
                mainTank = 0

        return distance
