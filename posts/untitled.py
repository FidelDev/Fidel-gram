from datetime import date

users = [
    {
        'email': 'cvander@gmail.com',
        'first_name': 'Christian',
        'last_name': 'Van der Henst',
        'password': '1234567',
        'is_admin': True
    },
    {
        'email': 'freddier@gmail.com',
        'first_name': 'Freddy',
        'last_name': 'Vega',
        'password': '987654321'
    },
    {
        'email': 'yesica@gmail.com',
        'first_name': 'Yésica',
        'last_name': 'Cortés',
        'password': 'qwerty',
        'birthdate': date(1990, 12, 19)
    },
    {
        'email': 'arturo@gmail.com',
        'first_name': 'Arturo',
        'last_name': 'Martínez',
        'password': 'msicomputer',
        'is_admin': True,
        'birthdate': date(1981, 11, 6),
        'bio': "The path of the righteous man is beset on all sides by the iniquities of the selfish and the"
    },
    {
        'email': 'Fidel@gmail.com',
        'first_name': 'Fidel',
        'last_name': 'Rosales',
        'password': 'msicomputer',
        'is_admin': True,
        'birthdate': date(1981, 11, 6),
        'bio': "The path of the righteous man is beset on all sides by the iniquities of the selfish and the"    
    }
]

from posts.models import User

for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk, ':', obj.email)