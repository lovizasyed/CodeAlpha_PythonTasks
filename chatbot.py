import random
import re


class BasicChatbot:
    def __init__(self):
        """Initialize the chatbot with predefined responses"""
        self.name = "CodeBot"

        # Define response patterns and their corresponding replies
        self.responses = {
            # Greetings
            'greetings': {
                'patterns': [r'\b(hello|hi|hey|greetings|good morning|good afternoon|good evening)\b'],
                'replies': [
                    f"Hello! I'm {self.name}, your friendly chatbot! 👋",
                    f"Hi there! Nice to meet you! I'm {self.name}.",
                    "Hey! How can I help you today?",
                    "Hello! Welcome! How are you doing?"
                ]
            },

            # How are you
            'how_are_you': {
                'patterns': [r'\b(how are you|how do you do|how\'s it going|what\'s up)\b'],
                'replies': [
                    "I'm doing great, thank you for asking! How about you?",
                    "I'm fantastic! Thanks for asking. How are you?",
                    "I'm doing well! Ready to chat with you!",
                    "All good here! How's your day going?"
                ]
            },

            # Name questions
            'name': {
                'patterns': [r'\b(what is your name|your name|who are you|what are you called)\b'],
                'replies': [
                    f"I'm {self.name}, a simple chatbot created for CodeAlpha internship!",
                    f"My name is {self.name}! I'm here to chat with you.",
                    f"I'm {self.name}, your friendly AI assistant!",
                    f"Call me {self.name}! I'm a basic chatbot."
                ]
            },

            # Age questions
            'age': {
                'patterns': [r'\b(how old are you|your age|age)\b'],
                'replies': [
                    "I'm just a few lines of code old! 😄",
                    "Age is just a number for bots like me!",
                    "I was born when my creator wrote my first line of code!",
                    "I'm timeless in the digital world!"
                ]
            },

            # Help
            'help': {
                'patterns': [r'\b(help|what can you do|capabilities|commands)\b'],
                'replies': [
                    "I can chat with you about basic topics! Try asking me about my name, how I'm doing, or just say hello!",
                    "I'm a simple chatbot. I can respond to greetings, answer basic questions about myself, and have a friendly conversation!",
                    "I can help with basic conversation! Ask me how I'm doing, what my name is, or just chat casually!",
                    "My capabilities include: greeting you, answering basic questions, and being a friendly chat companion!"
                ]
            },

            # Goodbye
            'goodbye': {
                'patterns': [r'\b(bye|goodbye|see you|farewell|exit|quit|leave)\b'],
                'replies': [
                    "Goodbye! It was nice chatting with you! 👋",
                    "See you later! Have a great day!",
                    "Farewell! Thanks for the chat!",
                    "Bye! Come back anytime for a chat!"
                ]
            },

            # Thanks
            'thanks': {
                'patterns': [r'\b(thank you|thanks|thank|appreciate)\b'],
                'replies': [
                    "You're welcome! Happy to help! 😊",
                    "No problem at all!",
                    "You're very welcome!",
                    "Glad I could help! Anytime!"
                ]
            },

            # Weather (simple responses)
            'weather': {
                'patterns': [r'\b(weather|temperature|hot|cold|sunny|rainy|cloudy)\b'],
                'replies': [
                    "I can't check the actual weather, but I hope it's nice where you are!",
                    "I don't have access to weather data, but I hope you're having good weather!",
                    "Weather talk! I wish I could check the forecast for you!",
                    "I'm just a simple bot and can't check weather, but I hope it's pleasant outside!"
                ]
            },

            # Programming related
            'programming': {
                'patterns': [r'\b(programming|code|coding|python|software|developer)\b'],
                'replies': [
                    "Programming is awesome! I was created using Python for a CodeAlpha internship project!",
                    "I love programming talk! I'm actually a Python program myself!",
                    "Coding is great! I'm a simple example of what you can build with Python!",
                    "Programming rocks! I'm proof that even simple code can create something interactive!"
                ]
            }
        }

        # Default responses for unmatched input
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "That's interesting! Tell me more.",
            "I'm still learning. Can you ask me something else?",
            "Hmm, I don't quite get that. Try asking me how I'm doing or what my name is!",
            "I'm a simple bot, so I might not understand everything. What else would you like to chat about?",
            "Could you try asking me something different? I'm better with basic conversation!",
            "That's beyond my simple capabilities! Try greeting me or asking about my name!"
        ]

    def clean_input(self, user_input):
        """Clean and normalize user input"""
        return user_input.lower().strip()

    def find_response(self, user_input):
        """Find appropriate response based on user input"""
        cleaned_input = self.clean_input(user_input)

        # Check each category of responses
        for category, data in self.responses.items():
            for pattern in data['patterns']:
                if re.search(pattern, cleaned_input):
                    return random.choice(data['replies'])

        # Return default response if no pattern matches
        return random.choice(self.default_responses)

    def is_goodbye(self, user_input):
        """Check if user wants to end conversation"""
        goodbye_patterns = [r'\b(bye|goodbye|exit|quit|leave|end)\b']
        cleaned_input = self.clean_input(user_input)

        for pattern in goodbye_patterns:
            if re.search(pattern, cleaned_input):
                return True
        return False

    def chat(self):
        """Main chat loop"""
        print("🤖 " + "=" * 50)
        print(f"   Welcome to {self.name} - Your Friendly Chatbot!")
        print("   Type 'bye', 'quit', or 'exit' to end the conversation")
        print("=" * 50)
        print()

        print(f"{self.name}: Hello! I'm {self.name}, your friendly chatbot! How can I help you today?")

        while True:
            # Get user input
            user_input = input("\nYou: ").strip()

            # Check if user wants to quit
            if not user_input:
                print(f"{self.name}: Please say something! I'm here to chat!")
                continue

            if self.is_goodbye(user_input):
                response = self.find_response(user_input)
                print(f"\n{self.name}: {response}")
                break

            # Generate and display response
            response = self.find_response(user_input)
            print(f"\n{self.name}: {response}")

    def demo_conversation(self):
        """Run a demo conversation to show capabilities"""
        print("\n🎯 DEMO MODE - Sample Conversation:")
        print("-" * 40)

        demo_inputs = [
            "Hello",
            "How are you?",
            "What's your name?",
            "How old are you?",
            "What can you do?",
            "Tell me about programming",
            "Thank you",
            "Goodbye"
        ]

        for user_msg in demo_inputs:
            print(f"You: {user_msg}")
            response = self.find_response(user_msg)
            print(f"{self.name}: {response}")
            print()


def main():
    """Main function to run the chatbot"""
    chatbot = BasicChatbot()

    print("Choose an option:")
    print("1. Start chatting")
    print("2. See demo conversation")

    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == "2":
        chatbot.demo_conversation()

        start_chat = input("Would you like to start chatting now? (y/n): ").lower().strip()
        if start_chat in ['y', 'yes']:
            chatbot.chat()
    else:
        chatbot.chat()

    print("\nThanks for using the chatbot! 🤖✨")


if __name__ == "__main__":
    main()