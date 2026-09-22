# How do we keep track of both the language and its count while finding the highest count?

from countries_data import countries_data

language_count ={}
highest_count = 0
highest_language = ""

for country in countries_data:
    for language in country["languages"]:
        if language not in language_count:
            language_count[language] = 0
        language_count[language] += 1

for language in language_count:
    count = language_count[language]

    if count > highest_count:
        highest_count = count
        highest_language = language

# print(f" {highest_language} : {highest_count}")

# A method to effective call both the key and value

# for language, count in language_count.items():
#     print(language, count)

# sorted Uses
# sorted( dict variable , key = lambda item : item[1]
# item[0]   # "English"
# item[1]   # 91
# Basically takes the item and fetched the element at  that position

# reverse = True. Reverses the order of the items.

sorted_languages = sorted(language_count.items(), key = lambda item : item[1], reverse = True)

# [:10] takes the first 10 entries.
for language,count in sorted_languages[:10]:
    print(language, count)