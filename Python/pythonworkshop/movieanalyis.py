#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Haihong
#
# Created:     20/01/2018
# Copyright:   (c) Haihong 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def score_gen(review):

    review = review.lower()

    words = review.split()

    score = 0

    reviewlength = len(review)

    for i in range (0, reviewlength):
        if "awesome" in words:
            score += 1
        if "good" in words:
            score += 1
        if "excellent" in words:
            score += 1
        if "wonderful" in words:
            score += 1
        if "enjoyable" in words:
            score += 1
        if "loved" in words:
            score += 1
        if "satisfying" in words:
            score += 1
        if "engaging" in words:
            score += 1
        if "superb" in words:
            score += 1
        if "beautiful" in words:
            score += 1
        if "fantastic" in words:
            score += 1
        if "memorable" in words:
            score += 1
        if "best" in words:
            score += 1
        if "great" in words:
            score += 1
        if "inspiring" in words:
            score += 1
        if "inspires" in words:
            score += 1
        if "captivating" in words:
            score += 1
        if "interesting" in words:
            score += 1
        if "original" in words:
            score += 1
        if "competent" in words:
            score += 1
        if "competently" in words:
            score += 1
        if "laugh" in words:
            score += 1
        if "enjoy" in words:
            score += 1
        if "cool" in words:
            score += 1
        if "greatest" in words:
            score += 1
        if "suspenseful" in words:
            score += 1
        if "amazing" in words:
            score += 1
        if "breathtaking" in words:
            score += 1
        if "hilarious" in words:
            score += 1

        if "bad" in words:
            score -= 1
        if "lacks" in words:
            score -= 1
        if "soapy" in words:
            score -= 1
        if "depressing" in words:
            score -= 1
        if "lazy" in words:
            score -= 1
        if "lame" in words:
            score -= 1
        if "boring" in words:
            score -= 1
        if "garbage" in words:
            score -= 1
        if "low" in words:
            score -= 1
        if "shallow" in words:
            score -= 1
        if "awful" in words:
            score -= 1
        if "cliche" in words:
            score -= 1
        if "waste" in words:
            score -= 1
        if "cynical" in words:
            score -= 1
        if "obnoxious" in words:
            score -= 1
        if "cringe" in words:
            score -= 1
        if "creepy" in words:
            score -= 1
        if "cheesy" in words:
            score -= 1
        if "hurt" in words:
            score -= 1
        if "horrible" in words:
            score -= 1
        if "worse" in words:
            score -= 1
        if "corny" in words:
            score -= 1
        if "yikes" in words:
            score -= 1
        if "filler" in words:
            score -= 1
        if "terrible" in words:
            score -= 1
        if "bland" in words:
            score -= 1
        if "destroyed" in words:
            score -= 1
        if "worst" in words:
            score -= 1

    if "not" in words:
        score *= -1

    score /= reviewlength
    score *= 2
    score += 7

    return score


input = input("Your review goes here: ")
print(score_gen(input))

if score_gen(input) > 7:
    print("This is a positive review.")
elif score_gen(input) == 7:
    print("This is a neutral review.")
elif score_gen(input) < 7:
    print("This is a negative review.")
