from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = defaultdict(SortedList)
        self.food_to_cuisine_map = {}
        self.food_to_rating_map = {}
        for (food, cuisine, rating) in zip(foods, cuisines, ratings):
            self.food_to_cuisine_map[food] = cuisine
            self.cuisines[cuisine].add((-rating, food))
            self.food_to_rating_map[food] = rating

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine_map[food]
        rating = self.food_to_rating_map[food]
        self.food_to_rating_map[food] = newRating
        self.cuisines[cuisine].remove((-rating, food))
        self.cuisines[cuisine].add((-newRating, food))
        

        return None

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][0][1]