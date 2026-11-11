#AI Study Buddy (Rule - Based Chat Assistant in Python)
import datetime
import time

userName = input("Enter Your Name : ")
presentTime = datetime.datetime.now().hour
if 1<=presentTime<=11 :
    print("Good Morning ",userName)
elif 12<=presentTime<=16 :
    print("Good Afternoon", userName)
elif 17<=presentTime<=20 :
    print("Good Evening", userName)
else :
    print("Good Time to see you ", userName)

print("Hey",userName,"I'm ChetanAI an AI Chatbot ")
print("You can talk to me and ask any queries ")
print("Wherever you want to Exit conversation you can say bye")

#Creating a Memory for the chetanAI

memory = {
    "hello" :  "Hello, How can i help you!",
    "how are you" : "I'm fine. What about you ?",
    "who are you" : "I'm ChetanAI, I'm here to help you ",
    "can you help me" : "yes tell me how can i help you",
    "motivate me" : "You can do anything , Nothing is Happen to you , Everything Happens for YOU",
    "happy" : "Great, Be Like this ",
    "sad" : "Don't, Worry no buddy can beat you ",
    "who made you" : "Chirag Maheshwari Made me to Help you ",
    "how you are working" : "I'm working on the Principle and basics of Python",

}

def getResponse(userquestion):
    userquestion= userquestion.lower()
    for eachkeys in memory:
        if "sad" in userquestion :
                    return "why"
        if "happy" in userquestion :
             return "woo hooo"
        if eachkeys in userquestion:
            return memory[eachkeys]
        
    return "I'll learn Everything very soon"

while True:
    inputUser = input("\n How can i help you:  ")
    time.sleep(1)
    reply = getResponse(inputUser)
    print("Bot Response : " , reply)

    if "bye" in inputUser.lower():
        break