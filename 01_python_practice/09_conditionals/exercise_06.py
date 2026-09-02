person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person:
    print(person["skills"][len(person["skills"]) // 2])

if "skills" in person:
    if "Python" in person["skills"]:
        print("Python")

if "skills" in person:
    if ("React" in person["skills"] and "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]):
        print("He is a fullstack developer")
    elif ("JavaScript" in person["skills"] and "React" in person["skills"]):
        print("He is a front end developer")
    elif ("Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]):
        print("He is a backend developer")
    else:
        print("unknown title")

if person["is_married"] and person["country"]:
    if person["country"] == "Finland" and person["is_married"]:
        print("Asabeneh Yetayeh lives in Finland. He is married.")

        print("He is a married developer")