class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_pop = 0
        ans_year = 1950

        for year in range(1950, 2051):
            population = 0

            for birth, death in logs:
                if birth <= year < death:
                    population += 1

            if population > max_pop:
                max_pop = population
                ans_year = year

        return ans_year