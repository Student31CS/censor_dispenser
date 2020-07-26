# These are the emails you will be censoring. The open() function is opening the
# text file that the emails are contained in and the .read() method is allowing
# us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# This function should 'censor' all instances of the phrase "learning algorithms"
# from Email email_one

def email_one_learning_algorithms(email):
    email_one_revised = ""
    email_one_revised = email.replace("learning algorithms", "----- -----")
    return email_one_revised

#Testing Function - uncomment to test
#print(email_one_learning_algorithms(email_one))

# This function should 'censor' a list of phrases defined in the Function
def email_two_list_censor(email):
    email_two_revised = email
    proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
    for word in proprietary_terms:
        if word in email_two_revised:
            email_two_revised = email_two_revised.replace(word, "-------")
    return email_two_revised

#Testing function - uncomment to test
#print(email_two_list_censor(email_two))

#This function should do the same as email_two_list_censor() and censor a list of words at the second or more occurence.
def email_three_censor(email):
    email_three_revised = email
    proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
    negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
    for word in proprietary_terms:
        if word in email_three_revised:
            email_three_revised = email_three_revised.replace(word, "-------")
    
    for word in negative_words
