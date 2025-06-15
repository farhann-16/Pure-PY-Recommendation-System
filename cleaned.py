import json

def clean_data(data):

    # To remove user with missing names
    data['user'] = [user for user in data['users'] if user['name'].strip()]

    # To remove duplicate freinds
    for user in data['users']:
        user['freinds'] = list(set(user['freinds']))

    # To remove inactive user
    data['user'] = [user for user in data['users'] if user['freinds'] or user['liked_pages']]

    # Remove duplicate pages
    unique_pages = {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())
    return data


data = json.load(open("user_data.json"))
print(data)
print(clean_data)
json.dump(data, open("cleaned_data.json", "w"), indent = 4)
print("Data cleaned successfully")
