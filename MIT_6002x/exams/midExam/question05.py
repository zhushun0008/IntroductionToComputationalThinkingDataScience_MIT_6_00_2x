__author__ = 'zhushun0008'

import random
import pylab

def sampleQuizzes():
    '''
    You are taking a class that plans to assign final grades based on two midterm quizzes and a final exam.
    The final grade will be based on 25% for each midterm, and 50% for the final. You are told that the grades on the
    exams were each uniformly distributed integers:
        Midterm 1: 50 <= grade <= 80
        Midterm 2: 60 <= grade <= 90
        Final Exam: 55 <= grade <= 95

    Write a function called sampleQuizzes() that implements a Monte Carlo simulation that estimates the probability of
    a student having a final score >= 70 and <= 75. Assume that 10,000 trials are sufficient to provide an accurate
    answer.
    '''
    numTrials = 10000
    wantedNum = 0

    for i in range(numTrials):
        midScore1 = random.randint(50, 80)
        midScore2 = random.randint(60, 90)
        finalExamScore = random.randint(55, 95)
        finalScore = 0.25 * (midScore1 + midScore2) + 0.5 * finalExamScore
        if 70 <= finalScore <= 75:
            wantedNum += 1

    return float(wantedNum) / numTrials

##print sampleQuizzes() # question 5-1

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of
    the three exams, then calculates the final score and
    appends it to a list of scores.

    Returns: A list of numTrials scores.
    """

    finalScoreList = []

    for i in range(numTrials):
        midScore1 = random.randint(50, 80)
        midScore2 = random.randint(60, 90)
        finalExamScore = random.randint(55, 95)
        finalScoreList.append(finalExamScore)

    return finalScoreList

def plotQuizzes():

    numTrials = 10000
    finalScoreList = generateScores(numTrials)

    pylab.figure()
    pylab.hist(finalScoreList, bins=7)
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of trials')
    pylab.title('Distribution of Scores')
    pylab.show()

## plotQuizzes() # Question 5-2