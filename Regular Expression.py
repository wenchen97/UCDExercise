# Find characters in movie variable
length_string = print(len(movie))

# Get the word
movie_title = movie[11:30]

# Obtain the palindrome
palindrome = movie_title[::-1]

# Print the word if it's a palindrome
if movie_title == palindrome:
	print(movie_title)

# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Remove specified character and print the result
movie_no_sign = movie.strip("$")
print(movie_no_sign)


# Split the string into substrings and print the result
movie_split = movie_no_sign.split()
print(movie_split)

# Select root word and print the result
word_root = movie_split[1][:-1]
print(word_root)

# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(",")
print(movie_no_comma)

# Join back together and print results
movie_join = " ".join(movie_no_comma)
print(movie_join)

# Split string at line boundaries
file_split = file.splitlines()

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(sep=',',)
    print(substring_split)

for movie in movies:
  	# Find if actor occurrs between 37 and 41 inclusive
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two by one
    elif movie.count("actor") == 2:
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences by one
        print(movie.replace("actor actor actor", "actor"))

for movie in movies:
  # Find the first occurrence of word
  print(movie.find("money", 12, 51))

for movie in movies:
  try:
    # Find the first occurrence of word
  	print(movie.index("money", 12, 51))
  except ValueError:
    print("substring not found")

# Replace negations
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)

# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()
# Define string with placeholders
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")

# Use format to print strings
for my_string in my_list:
  	print(my_string.format(first_pos, second_pos))

# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }

# Complete the placeholders accessing elements of field and tool keys in the data dictionary
my_message = "If you are interested in {data[field]} , you can take the course related to {data[tool]}"

# Use the plan dictionary to replace placeholders
print(my_message.format(data=plan))


# Import datetime
from datetime import datetime

# Assign date to get_date
get_date = print(datetime.now())

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Format date
print(message.format(today=get_date)

# Complete the f-string
print(f"Data science is considered {field1!r} in the {fact1:d}st century")
# Complete the f-string
print(f"About {fact2:e} of {field2} in the world")
# Complete the f-string
print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")

# Include both variables and the result of dividing them
print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1/number2:.1f} tweets per min")
# Replace the substring https by an empty string
print(f"{string1.replace('https', '')}")
# Divide the length of list by 120 rounded to two decimals
print(f"Only {len(list_links)*100/120:.2f}% of the posts contain links"

# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")
# Access values of date and price in west dictionary
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")

# Import Template
from string import Template

# Create a template
wikipedia = Template("$tool is a $description")

# Substitute variables in template
print(wikipedia.substitute(tool=tool1, description=description1))
print(wikipedia.substitute(tool=tool2, description=description2))
print(wikipedia.substitute(tool=tool3, description=description3))

# Import template
from string import Template

# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template("We are offering a 3-month beginner course on $tool just for $$ $fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))

# Import template
from string import Template

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use safe_substitute to replace identifiers
try:
    print(the_answers.safe_substitute(answers))
except KeyError:
    print("Missing information")

# Write a regex to obtain user mentions
print(re.findall(r"User_mentions:\d", sentiment_analysis))

# Write a regex to obtain number of likes
print(re.findall(r"likes:\s\d", sentiment_analysis))
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))

regex_sentence = r"\W\dbreak\W"
# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)
# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"
# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, " ", sentiment_sub)
print(sentiment_final)

# Import re module
import re

for tweet in sentiment_analysis:
	# Write regex to match http links and print out result
	print(re.findall(r"http\S+", tweet))

	# Write regex to match user mentions and print out result
	print(re.findall(r"@\w+", tweet))

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\s\w+\sago", date))

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1:2}\w{2}\s\w+\s\d{4}", date))

	print(re.findall(r"\d{1,2}\w{2}\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

# Get tokens by splitting text
print(re.split(r"\s+",no_hashtag ))

egex = r"[a-zA-Z]+\d+\W+@\w+\.com"


# Write a regex to match a valid email address
regex = r"[a-zA-Z]+[0-9]+[!#\%&*$\.]+@\w+\.com"

for example in emails:
  	# Match the regex to the string
    if re.match(regex, emails):
        # Complete the format method to print out the result
      	print("The email {email_example} is a valid email".format(email_example=example))
    else:
      	print("The email {email_example} is invalid".format(email_example=example))


# Write a regex to match a valid password
regex = r"[a-zA-Z0-9*#\$%!&\.]{8:20}"
        r"[A-Za-z0-9!#%&*\$\.]{8,20}"

for example in passwords:
  	# Scan the strings to find a match
    if re.match(regex, passwords):
        # Complete the format method to print out the result
      	print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      	print("The password {pass_example} is invalid".format(pass_example=example))


# Import re
import re

# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", " ", string)

# Print out the result
print(string_notags)

# Write a greedy regex expression
numbers_found_greedy = re.findall(r"\d+?", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)

# Write a regex that matches email
regex_email = r"([A-Za-z]+)([0-9]+)(\S+)@"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(tweet))

# Write a greedy regex expression to match
sentences_found_greedy = re.findall(r"\(.+\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.+?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)

# Import re
import re

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)

# Import re
import re

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)

# Print the matches
print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))

# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
    # Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)

    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))

# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
	"day": dates.group(2),
	"month": dates.group(1),
	"year": dates.group(3)
}

# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
	"day": dates.group(2),
	"month": dates.group(1),
	"year": dates.group(3)
}
# Complete the format method to print-out
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))

for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag = re.match(r"<(\w+)>.*?</\1>", html_tags)

    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1)))
    else:
        # If it doesn't match capture only the tag
        notmatch_tag = re.match(r"<(\w+)>", match_tag)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))

# Complete the regex to match an elongated word
regex_elongated = r"\w+(\w+)\1\w*"
regex_elongated = r"\w*(\w)\1\w*"

for tweet in sentiment_analysis:
    # Find if there is a match in each tweet
    match_elongated = re.search(regex_elongated, tweet)

    if match_elongated:
        # Assign the captured group zero
        elongated_word = match_elongated.group(0)

        # Complete the format method to print the word
        print("Elongated word found: {word}".format(word=regex_elongated))
    else:
        print("No elongated word found")

for phone in cellphones:
	# Get all phone numbers not preceded by area code
	number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
	print(number)