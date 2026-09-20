from countries_data import countries_data


# 1. total no of languages spoken

language_count ={}

for country in countries_data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1
print(language_count)