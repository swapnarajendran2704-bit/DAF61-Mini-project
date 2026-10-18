
# Feedback Analysis Project

# Step 1: Preloaded feedbacks

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# Step 2: Add more feedbacks

n = int(input("How many feedbacks do you want to add? "))

for i in range(n):
    name = input("Enter name: ")
    feedback = input("Enter feedback: ")
    rating = int(input("Enter rating from 1 to 5: "))

    while rating < 1 or rating > 5:
        print("Please enter a rating between 1 and 5.")
        rating = int(input("Enter rating: "))

    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)


# Step 3: Clean the feedbacks

for i in range(len(feedback_data['Feedback'])):
    feedback = feedback_data['Feedback'][i]

    feedback = feedback.lower()
    feedback = feedback.replace('.', '')
    feedback = feedback.replace(',', '')
    feedback = feedback.replace('!', '')
    feedback = feedback.replace('?', '')
    feedback = ' '.join(feedback.split())

    feedback_data['Feedback'][i] = feedback


# Step 4: Count feedbacks containing a word

def count_word_in_feedbacks(word):
    count = 0

    for feedback in feedback_data['Feedback']:
        words = feedback.split()

        if word.lower() in words:
            count = count + 1

    return count


print("\nFeedbacks containing good:", count_word_in_feedbacks('good'))
print("Feedbacks containing poor:", count_word_in_feedbacks('poor'))
print("Feedbacks containing excellent:", count_word_in_feedbacks('excellent'))


# Step 5: Display the cleaned feedback data

print("\nCleaned Feedback Data:")
print(feedback_data)


# Calculate the average rating

total = sum(feedback_data['Rating'])
number = len(feedback_data['Rating'])
average = total / number

print("\nAverage rating:", round(average, 2))


# Find the longest feedback

longest_feedback = ""
longest_count = 0

for feedback in feedback_data['Feedback']:
    words = feedback.split()

    if len(words) > longest_count:
        longest_count = len(words)
        longest_feedback = feedback

print("\nLongest feedback:", longest_feedback)
print("Number of words:", longest_count)


# Find unique words in all feedbacks

unique_words = []

for feedback in feedback_data['Feedback']:
    words = feedback.split()

    for word in words:
        if word not in unique_words:
            unique_words.append(word)

print("\nUnique words:")
print(sorted(unique_words))


# Optional: Sort feedbacks by rating

feedback_list = list(zip(
    feedback_data['S_No'],
    feedback_data['Name'],
    feedback_data['Feedback'],
    feedback_data['Rating']
))

feedback_list = sorted(feedback_list, key=lambda x: x[3], reverse=True)

print("\nFeedbacks sorted by rating:")

for item in feedback_list:
    print(item)
