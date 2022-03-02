answer = input("Who would you rather be: Ted Lasso or Dracula? ")

def conversation(answer):
    if answer.title() == "Ted Lasso" or answer.title() == "Ted" or answer.title() == "Lasso":
        nxtq = input("Do you like his optimism or his courage? ")
        if nxtq.lower() == "optimism":
            nxtq2 = input("Yeah. I love that too. Do you want to be more like him too? ")
            if nxtq2.title() == "Yes" or nxtq2.title() == "Yeah":
                return "I told my mom I wasn't the only one..."
            else:
                return "Ok. See, this is where you're wrong."
        else:
             return "No, you're wrong. His optimism is what's best about him. "
    elif answer.title() == "Dracula":
        drcnxtq = input("Why? Do you think Dracula is sexy or creepy? ")
        if drcnxtq.lower() == "sexy":
            nq = input("Same. I use to fantasize about him all the time. I'm real messed up. You messed up too? lol ")
            if nq != None:
                return "Life sure is something, isn't it? "
        else:
            return "You're definitely thinking about the book version of Dracula."
    else:
        upset = input("Um, excuse me, did you not see the question? ")
        if upset.lower() == "no" or upset.lower() == "nah":
            return "Then read the question, dumb ass. Seriously, it's like why should I even try anymore..."
        else:
            return "Sigh. The disappointment I feel is disgusting."

print(conversation(answer))