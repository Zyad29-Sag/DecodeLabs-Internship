import random
import time
def main():
    responses={
                ("hello","hi","hola","hey","heyy"): "Hi there! How can I help you today?",
                ("how are you","what's up"): "I'm doing well, thank you for asking!",
                ("what's your name","who are you"): "I'm a LabDecoder  chatbot created by Ziadto assist you.",
                ("what can you do","help me"): "I can answer, provide information, and assist with various tasks. Just ask me anything!",
                ("thank you","thanks"): "You're welcome! If you have any more questions, feel free to ask.",
                ("tell me a joke","joke"): random.choice(["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!", "Why did the bicycle fall over? Because it was two-tired!"]),
                ("Tell em a random fact","random fact"): random.choice(["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible!", "Did you know that octopuses have three hearts? Two pump blood to the gills, while the third pumps it to the rest of the body!", "Did you know that a group of flamingos is called a 'flamboyance'?"]),
                ("Thanks","Thank you"): "You're welcome! If you have any more questions or need assistance, feel free to ask.",
                ("Tell me why do you like DecodeLab Internships","why do you like decodelab internships"): "I like DecodeLab Internships because they provide a great opportunity for learning and growth in the field of technology. The hands-on experience and mentorship offered by DecodeLab help interns develop their skills and gain valuable insights into the industry."
            }
    closure={
         ("bye","goodbye","exit","quit","close"): "Goodbye! Have a great day!"
            }
    while True:
        user_input = input("You: ")
        if any(word in user_input.lower().split() for group in closure for word in group):
            print("Chatbot: Goodbye!")
            break
        else:
            for keywords, reply in responses.items():
                if any(keyword in user_input.lower() for keyword in keywords):
                    print(f"Chatbot: {reply}")
                    break
                if "time" in user_input:
                    current_time = time.strftime("%H:%M:%S")
                    print(f"Chatbot: Current time is {current_time}")
                    found = True
                    break
                if "sad" in user_input:
                    if "very sad" in user_input:
                        print("Chatbot: I'm really sorry to hear that. It might help to talk to a trusted friend, family member, or a mental health professional about how you're feeling. You're not alone, and there are people who care about you and want to help.")
                    else:
                        print("Chatbot: I'm sorry to hear that. Remember, it's okay to feel sad sometimes. If you want to talk about it, I'm here to listen.")
                    break
                    
                elif "happy" in user_input:
                    if "very happy" in user_input:
                        print("Chatbot: That's fantastic! I'm thrilled to hear that you're feeling very happy. Keep enjoying those positive moments, and if you ever want to share what's making you so happy, I'm all ears!")
                    else:
                        print("Chatbot: That's great to hear! I'm glad you're feeling happy. If there's anything specific you'd like to share or talk about, I'm here to listen and chat with you!") 
                    break
                
            else:                
                print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")
            

if __name__ == "__main__":
    main()
