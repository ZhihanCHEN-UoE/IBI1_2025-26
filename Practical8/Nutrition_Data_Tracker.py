class food_item:
    """Class to represent a food item with core nutritional values"""
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

    def get_nutrition(self):
        """Return nutritional information as a dictionary"""
        return {
            "Name": self.name,
            "Calories": self.calories,
            "Protein (g)": self.protein,
            "Carbs (g)": self.carbs,
            "Fat (g)": self.fat
        }


def track_daily_nutrition(consumed_items):
    """Calculate 24-hour nutrition totals and print health alerts"""
    total_calories = 0.0
    total_protein = 0.0
    total_carbs = 0.0
    total_fat = 0.0

    # Sum all nutritional values
    for food in consumed_items:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat

    # Print total nutrition summary
    print("=== 24-HOUR NUTRITION SUMMARY ===")
    print(f"Total Calories: {total_calories} kcal")
    print(f"Total Protein: {total_protein} g")
    print(f"Total Carbohydrates: {total_carbs} g")
    print(f"Total Fat: {total_fat} g")

    # Health threshold warnings
    print("\n=== HEALTH ALERTS ===")
    warnings = []
    if total_calories > 2500:
        warnings.append(f"⚠️ Calories exceed 2500 kcal (Current: {total_calories} kcal)")
    if total_fat > 90:
        warnings.append(f"⚠️ Fat exceeds 90g (Current: {total_fat} g)")
    
    if warnings:
        for warning in warnings:
            print(warning)
    else:
        print("Nutrition intake is within healthy limits!")
    return {
        "calories": total_calories,
        "protein": total_protein,
        "carbs": total_carbs,
        "fat": total_fat
    }



apple = food_item("Apple", 60, 0.3, 15, 0.5)
chicken_breast = food_item("Chicken Breast", 165, 31, 0, 3.6)
rice = food_item("White Rice (1 bowl)", 250, 5.2, 58, 0.6)
nuts = food_item("Mixed Nuts (30g)", 170, 4.3, 6.1, 14.2)

# List of consumed food
daily_intake = [apple, chicken_breast, rice, nuts]

# Track and display results
track_daily_nutrition(daily_intake)