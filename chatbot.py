#DecodeLabs-Internship    -    AI.
#Name : Karim Khozam
# A rule-based fitness chatbot built with Python and NLTK that provides workout plans,
#  exercise recommendations, BMI calculation, protein intake estimation,
#  greeting handling, and typo correction using fuzzy matching.


import nltk
from nltk.tokenize import word_tokenize
from difflib import get_close_matches

# Download tokenizer once
nltk.download('punkt')


class GymChatBot:

    def __init__(self):

        # Exercise topics
        self.keywords = {

            "chest": (
                "Chest Exercises:\n"
                "- Bench Press\n"
                "- Push-ups\n"
                "- Cable Fly"
            ),

            "legs": (
                "Leg Exercises:\n"
                "- Squats\n"
                "- Lunges\n"
                "- Leg Press"
            ),

            "protein": (
                "Good Protein Sources:\n"
                "- Chicken\n"
                "- Eggs\n"
                "- Tuna"
            ),

            "motivation": (
                "Stay consistent "
            )
        }


        # Workout plans
        self.workout_plans = {

            "beginner": (
                "BEGINNER PLAN \n\n"

                "Monday:\n"
                "- Push-ups\n"
                "- Bodyweight Squats\n"
                "- Plank\n\n"

                "Wednesday:\n"
                "- Dumbbell Press\n"
                "- Lunges\n"
                "- Shoulder Press\n\n"

                "Friday:\n"
                "- Full Body Workout\n"
                "- Cardio 20 min"
            ),

            "intermediate": (
                "INTERMEDIATE PLAN \n\n"

                "Monday - Chest + Triceps\n"
                "- Bench Press\n"
                "- Incline Dumbbell Press\n"
                "- Cable Fly\n"
                "- Tricep Pushdown\n\n"

                "Tuesday - Back + Biceps\n"
                "- Pull-ups\n"
                "- Barbell Rows\n"
                "- Lat Pulldown\n"
                "- Dumbbell Curl\n\n"

                "Thursday - Legs\n"
                "- Squats\n"
                "- Romanian Deadlift\n"
                "- Leg Press\n"
                "- Calf Raises\n\n"

                "Friday - Shoulders\n"
                "- Overhead Press\n"
                "- Lateral Raises\n"
                "- Rear Delt Fly"
            ),

            "advanced": (
                "ADVANCED PLAN \n\n"

                "Monday - Push\n"
                "- Bench Press 5x5\n"
                "- Incline Press\n"
                "- Weighted Dips\n"
                "- Skull Crushers\n\n"

                "Tuesday - Pull\n"
                "- Deadlift\n"
                "- Weighted Pull-ups\n"
                "- Barbell Rows\n"
                "- Hammer Curls\n\n"

                "Wednesday - Legs\n"
                "- Heavy Squats\n"
                "- Bulgarian Split Squats\n"
                "- Leg Curl\n"
                "- Standing Calf Raises\n\n"

                "Thursday - Shoulders\n"
                "- Military Press\n"
                "- Arnold Press\n"
                "- Upright Rows\n\n"

                "Friday - Arms + Abs\n"
                "- Barbell Curl\n"
                "- Close Grip Bench\n"
                "- Hanging Leg Raises"
            )
        }



    # BMI calculator
    def bmi(self, weight, height):

        return round(weight / (height ** 2),2)


# Protein Intake Calculator
    def pic(self, weight):
        return round(weight )



    # Main chatbot function
    def chat(self, message):

        message = message.lower()

        words = word_tokenize(message)


        # Greetings
        if any(word in words for word in ["hi", "hello", "hey"]):
            return "Hello!  Welcome to the Gym Chatbot."

        # Exit
        elif any(word in words for word in ["bye", "exit", "quit"]):
            return "Goodbye!"



        # BMI
        elif "bmi" in words or "body mass index" in message:
            try:
                weight = float(input("Enter your weight (kg): "))
                height = float(input("Enter your height (m): "))

                result = self.bmi(weight, height)

                if result < 18.5:
                    return (
                        f"Your BMI is: {result}. You are underweight. "
                        "Consider a balanced diet and strength training."
                    )

                elif 18.5 <= result < 25:
                    return (
                        f"Your BMI is: {result}. Normal weight. "
                        "Keep maintaining a healthy lifestyle."
                    )

                elif 25 <= result < 30:
                    return (
                        f"Your BMI is: {result}. Overweight. "
                        "Try calorie deficit and regular exercise."
                    )

                else:
                    return (
                        f"Your BMI is: {result}. Obese category. "
                        "Consider consulting a healthcare professional."
                    )

            except ValueError:
                return "Invalid input. Please enter numbers only."


        # Protein intake calculator
        elif "pic" in words or "protein intake" in message:
            try:
                weight = float(input("Enter your weight (kg): "))

                result = self.pic(weight)
                result2 = self.pic(weight * 2)

                return (
                    f"Your Protein Intake Calculation is at least: "
                    f"{result} grams per day and at most: "
                    f"{result2} grams per day"
                )

            except ValueError:
                return "Invalid input."
        # Workout plans
        for level in self.workout_plans:

            if level in words:
                return self.workout_plans[level]



        # Exercise topics
        for keyword in self.keywords:

            if keyword in words:
                return self.keywords[keyword]



        # Misspelling correction
        all_keywords = list(self.keywords.keys()) + list(self.workout_plans.keys())

        for word in words:

            match = get_close_matches(
                word,
                all_keywords,
                n=1,
                cutoff=0.7
            )

            if match:

                matched_word = match[0]

                if matched_word in self.keywords:
                    return self.keywords[matched_word]

                elif matched_word in self.workout_plans:
                    return self.workout_plans[matched_word]

        return (
            "I don't understand.\n"
            "Try asking about:\n"
            "- chest\n"
            "- legs\n"
            "- protein\n"
            "- beginner plan\n"
            "- intermediate plan\n"
            "- advanced plan\n"
            "- bmi\n"
        )



# Create chatbot
bot = GymChatBot()


# Chat loop
while True:

    message = input("You: ")

    response = bot.chat(message)

    print("\nBot:", response)

    if response == "Goodbye!":
        break
