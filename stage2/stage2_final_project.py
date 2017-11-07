import sys


easy_string = """
        __1__ is better than ugly.
        __2__ is better than implicit.
        __3__ is better than complex.
        __4__ is better than complicated.
        __5__ is better than nested.
        __6__ is better than dense."""

medium_string = """
        __1__ counts.
        __2__ cases aren't special enough to break the rules.
        Although __3__ beats purity.
        Errors should never pass __4__.
        Unless explicitly __5__.
        In the face of __6__, refuse the temptation to guess."""

hard_string = """
        There should be one-- and preferably only one --__1__ way to do it.
        Although that way may not be obvious at first unless you're __2__.
        __3__ is better than never.
        Although __4__ is often better than *right* now.
        If the implementation is hard to explain, it's a __5__ idea.
        If the implementation is easy to explain, it may be a __6__ idea.
        __7__ are one honking great idea -- let's do more of those!"""

answers = {
    'easy' : [('__1__' , 'Beautiful'),
              ('__2__' , 'Explicit'),
              ('__3__' , 'Simple'),
              ('__4__' , 'Complex'),
              ('__5__' , 'Flat'),
              ('__6__' , 'Sparse')],

    'medium' : [('__1__' ,  'Readability'),
                ('__2__' ,  'Special'),
                ('__3__' , 'practicality'),
                ('__4__' , 'silently'),
                ('__5__' ,  'silenced'),
                ('__6__' ,  'ambiguity')],

    'hard' : [('__1__' ,  'obvious'),
              ('__2__' ,  'Dutch'),
              ('__3__' , 'Now'),
              ('__4__' , 'never'),
              ('__5__' ,  'bad'),
              ('__6__' ,  'good'),
              ('__7__' , 'Namespaces')]
}

def choose_level():
    # asks user to choose a level, num of attempts and returns that game path
    print "Please select a game difficulty by typing it in!"
    print "Possible choices include easy, medium, and hard."
    level_choice = raw_input("> ").lower()
    print "You've chosen {}!".format(level_choice)
    attempts = int(raw_input("How many attempts needed to solve the problem? "))
    print "You will have {} attempts per problem.".format(attempts)
    if level_choice == 'easy':
        return play_game(easy_string, 'easy', attempts)
    elif level_choice == 'medium':
        return play_game(medium_string, 'medium', attempts)
    elif level_choice == 'hard':
        return play_game(hard_string, 'hard', attempts)
    else:
        print "Sorry, that wasn't an option."
        return choose_level()


def play_game(string_choice, answer_key, attempts):
    # takes attempts, string_choice, answer_key from level_choice and executes game
    count = 0
    while count < attempts:
        for (blank, blank_value) in answers[answer_key]:
            while True:
                print "The current paragraph reads as such:\n" + string_choice
                user_answer = raw_input("\nWhat should be substituted for "
                + blank + " ? ")
                if user_answer == blank_value:
                    print 'Correct!\n'
                    string_choice = string_choice.replace(blank, blank_value)
                    break
                else:
                    count += 1
                    if count == attempts:
                        print 'Sorry. Game over. No attempts left.'
                        return play_again()
                    else:
                        print 'Incorrect. Try again. You have {} attempts '\
                        'remaining.'.format(attempts - count)
        print string_choice
        print 'Congratulations! You win.'
        return play_again()


def play_again():
    # asks player if they want to play again following game conclusion
    again = raw_input("Do you want to play again? Y/n ")
    if again != 'n':
        return choose_level()
    else:
        print "Bye! Thanks for playing."
        sys.exit

choose_level()
