import json
import random
import time

class QuizApp:
    def __init__(self, json_file):
        """Initialize the quiz with questions from a JSON file."""
        self.json_file = json_file
        self.questions = []
        self.score = 0
        self.total_questions = 0
        self.load_questions()
    
    def load_questions(self):
        """Load questions from JSON file."""
        try:
            with open(self.json_file, 'r') as f:
                data = json.load(f)
                self.questions = data.get('questions', [])
                self.total_questions = len(self.questions)
            print(f"✓ Found {self.total_questions} questions! Let's get started...\n")
            time.sleep(1)
        except FileNotFoundError:
            print(f"Oops! I couldn't find '{self.json_file}'. Make sure the file exists!")
        except json.JSONDecodeError:
            print(f"Hmm, something's wrong with the JSON format in {self.json_file}")
    
    def randomize_questions(self):
        """Randomize the order of questions."""
        random.shuffle(self.questions)
        print("🔀 Questions shuffled! No two quizzes will be the same.\n")
        time.sleep(1)
    
    def print_slow(self, text, delay=0.03):
        """Print text with a slight delay for dramatic effect."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def run_quiz(self):
        """Run the quiz and track score."""
        if not self.questions:
            print("No questions available! Please check your JSON file.")
            return
        
        print("\n" + "="*60)
        self.print_slow("🎯  WELCOME TO THE QUIZ!  🎯".center(60), 0.05)
        print("="*60 + "\n")
        
        print("Instructions:")
        print("  • Read each question carefully")
        print("  • Type the number of your answer")
        print("  • You'll get instant feedback after each question")
        print("  • Try your best and have fun! 😊\n")
        
        input("Press Enter when you're ready to begin...")
        print()
        
        for i, question in enumerate(self.questions, 1):
            print("\n" + "─"*60)
            print(f"📝 Question {i} of {self.total_questions}")
            print("─"*60)
            print(f"\n{question['question']}\n")
            
            # Display options with letters
            option_letters = ['A', 'B', 'C', 'D', 'E', 'F']
            for j, option in enumerate(question['options']):
                print(f"  {option_letters[j]}. {option}")
            
            # Get user answer
            while True:
                try:
                    answer_input = input("\n💭 Your answer (enter the number): ").strip()
                    answer = int(answer_input)
                    if 1 <= answer <= len(question['options']):
                        break
                    else:
                        print(f"⚠️  Please pick a number between 1 and {len(question['options'])}")
                except ValueError:
                    print("⚠️  That's not a valid number. Try again!")
                except KeyboardInterrupt:
                    print("\n\n👋 Quiz interrupted. See you next time!")
                    return
            
            # Check answer with dramatic pause
            print("\nChecking your answer", end="")
            for _ in range(3):
                time.sleep(0.3)
                print(".", end="", flush=True)
            print()
            time.sleep(0.3)
            
            if answer == question['correct_answer']:
                print("🎉 That's correct! Well done!")
                self.score += 1
            else:
                correct_option = question['options'][question['correct_answer'] - 1]
                correct_letter = option_letters[question['correct_answer'] - 1]
                print(f"❌ Not quite! The correct answer was: {correct_letter}. {correct_option}")
            
            # Show current score
            print(f"\n📊 Current score: {self.score}/{i}")
            
            if i < self.total_questions:
                time.sleep(1.5)
        
        self.show_final_result()
    
    def show_final_result(self):
        """Display the final score and result."""
        time.sleep(1)
        print("\n\n" + "="*60)
        self.print_slow("🏁  QUIZ COMPLETE!  🏁".center(60), 0.05)
        print("="*60 + "\n")
        
        time.sleep(0.5)
        
        percentage = (self.score / self.total_questions) * 100
        
        print(f"📈 Final Score: {self.score} out of {self.total_questions}")
        print(f"📊 Percentage: {percentage:.1f}%\n")
        
        time.sleep(0.5)
        
        # Personalized grade based on percentage
        if percentage == 100:
            grade = "🌟 PERFECT SCORE! You're a genius! 🧠"
            message = "Absolutely incredible! You got every single question right!"
        elif percentage >= 90:
            grade = "🏆 OUTSTANDING! Excellent work!"
            message = "You really know your stuff! Amazing job!"
        elif percentage >= 75:
            grade = "⭐ GREAT JOB! You did really well!"
            message = "Impressive performance! Keep it up!"
        elif percentage >= 60:
            grade = "👍 GOOD EFFORT! Solid performance!"
            message = "Nice work! You got more than half right!"
        elif percentage >= 50:
            grade = "✅ YOU PASSED! Not bad!"
            message = "You made it! With a bit more practice, you'll do even better!"
        else:
            grade = "📚 KEEP PRACTICING! Don't give up!"
            message = "Rome wasn't built in a day. Try again and you'll improve!"
        
        self.print_slow(f"🎖️  {grade}", 0.04)
        print(f"\n💬 {message}\n")
        
        # Fun stats
        questions_wrong = self.total_questions - self.score
        if questions_wrong > 0:
            print(f"💡 You got {questions_wrong} {'question' if questions_wrong == 1 else 'questions'} wrong.")
            print("   Review those topics and try again!\n")
        
        print("─"*60)
        print("Thanks for playing! Come back anytime to test your knowledge! 🚀")
        print("─"*60 + "\n")


# Main execution
if __name__ == "__main__":
    print("\n" + "🎓"*30)
    print("INTERACTIVE QUIZ APPLICATION".center(60))
    print("🎓"*30 + "\n")
    
    # Initialize the quiz with your JSON file
    quiz = QuizApp('questions.json')
    
    # Randomize questions
    quiz.randomize_questions()
    
    # Run the quiz
    quiz.run_quiz()