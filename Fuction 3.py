def bio_data(name, gender):
    if gender == 'male':
        title: str = 'Mr '
    else:
        title: str = 'Miss '
    greeting = 'Hello, ' + title + name
    return greeting


bio = bio_data ('bismarck', 'male')
print (bio)

# Using keyword argument so that when interchanged they will return same value

bio = bio_data (name='bismarck', gender='male')
print (bio)
print ('*' * 120)

bio = bio_data (gender='male', name='bismarck')
print (bio)
print ('*' * 120)
