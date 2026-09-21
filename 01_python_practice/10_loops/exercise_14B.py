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

print(f" {highest_language} : {highest_count}")