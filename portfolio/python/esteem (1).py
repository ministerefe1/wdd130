# class SelfEsteemScale:
#     SCALE = [
#         "I feel that I am a person of worth, at least on an equal plane with others.",
#         "I feel that I have a number of good qualities.",
#         "All in all, I am inclined to feel that I am a failure.",
#         "I am able to do things as well as most other people.",
#         "I feel I do not have much to be proud of.",
#         "I take a positive attitude toward myself.",
#         "On the whole, I am satisfied with myself.",
#         "I wish I could have more respect for myself.",
#         "I certainly feel useless at times.",
#         "At times I think I am no good at all.",
#     ]

#     def __init__(self):
#         self.responses = self.new_method()

#     def new_method(self):
#         return []

#     def calculate_score(self):
#         if len(self.responses) != len(self.SCALE):
#             return "Invalid number of responses. Please provide responses for all statements."

#         total_score = 0
#         for response in self.responses:
#             if response == "D":
#                 total_score += 3
#             elif response == "d":
#                 total_score += 2
#             elif response == "a":
#                 total_score += 1
#             elif response == "A":
#                 total_score += 0

#         if total_score < 0:
#             total_score = 0
#         return total_score

#     def print_intro(self):
#         print("Rosenberg Self-Esteem Scale")
#         print("Please respond to each of the following statements with D, d, a, or A:")
#         print("D - Strongly Disagree")
#         print("d - Disagree")
#         print("a - Agree")
#         print("A - Strongly Agree")

#     def main(self):
#         self.print_intro()
#         for statement in self.SCALE:
#             while True:
#                 response = input(f"{statement}\nYour response: ")
#                 if response in ["D", "d", "a", "A"]:
#                     self.responses.append(response)
#                     break
#                 else:
#                     print("Invalid response. Please enter D, d, a, or A.")
#         total_score = self.calculate_score()
#         print(f"Your total score is: {total_score}")

# if __name__ == "__main__":
#     scale = SelfEsteemScale()
#     scale.main()

class SelfEsteem:
    SCALE = {
        "D": 0,
        "d": 1,
        "A": 2,
        "A": 3,
    }

    POSITIVE_STATEMENTS = [
        "I feel that I am a person of worth, at least on an equal plane with others.",
        "I feel that I have a number of good qualities.",
        "I am able to do things as well as most other people.",
        "I take a positive attitude toward myself.",
        "On the whole, I am satisfied with myself.",
    ]

    NEGATIVE_STATEMENTS = [
        "All in all, I am inclined to feel that I am a failure.",
        "I feel I do not have much to be proud of.",
        "I wish I could have more respect for myself.",
        "I certainly feel useless at times.",
        "At times I think I am no good at all.",
    ]

    def __init__(self):
        self.responses = []

    def gather_responses(self):
        print("Please respond to the following statements:")
        for i, statement in enumerate(self.POSITIVE_STATEMENTS):
            response = input(f"{i+1}. {statement}\nChoose one: D, d, A, or A: ")
            self.responses.append(response)

        for i, statement in enumerate(self.NEGATIVE_STATEMENTS):
            response = input(f"{i+6}. {statement}\nChoose one: D, d, A, or A: ")
            self.responses.append(response)

    def calculate_score(self):
        if len(self.responses) != len(self.SCALE):
            return "Invalid number of responses. Please provide responses for all statements."

        total_score = 0
        for response in self.responses:
            if response not in self.SCALE:
                return "Invalid response. Please use D, d, A, or A for each statement."
            total_score += self.SCALE[response]

        return total_score

    def interpret_score(self, score):
        if score < 15:
            return "Your self-esteem may be problematic."
        elif score <= 15 or score <= 25:
            return "Your self-esteem is moderate."
        else:
            return "You have a healthy self-esteem."

if __name__ == "__main__":
    selfesteem = SelfEsteem()
    selfesteem.gather_responses()
    score = selfesteem.calculate_score()
    interpretation = selfesteem.interpret_score(score)
    print(f"Your total score is {score}. {interpretation}")
