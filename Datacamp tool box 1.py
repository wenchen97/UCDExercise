def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word="congratulations"+"!!!"

    # Print shout_word
    print(shout_word)

# Call shout
shout()

# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout("congratulations")

# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word=word+"!!!"

    # Replace print with return
    return(shout_word)

    # Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1=word1+"!!!"

    # Concatenate word2 with '!!!': shout2
    shout2=word2+"!!!"

    # Concatenate shout1 with shout2: new_shout
    new_shout=shout1+shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell=shout("congratulations", "you")

# Print yell
print(yell)

def shout_all(word1, word2):

    # Concatenate word1 with '!!!': shout1
    shout1=word1+"!!!"


    # Concatenate word2 with '!!!': shout2
    shout2=word2+"!!!"

    # Construct a tuple with shout1 and shout2: shout_words
    shout_words=(shout1,shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1,yell2=shout_all("congratulations","you")

# Print yell1 and yell2
print(yell1)
print(yell2)