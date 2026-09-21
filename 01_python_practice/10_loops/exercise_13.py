from countries_data import countries_data

# 1. Total number of languages in the data

language_count = set()

for country in countries_data:
    for language in country["languages"]:
        language_count.add(language)
print(len(language_count))