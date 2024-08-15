from faker import Faker

#   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
#  ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
#  ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
#  ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌
#  ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
#  ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
#  ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀
#  ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌  ▐░▌          ▐░▌     ▐░▌
#  ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌
#  ▐░░░░░░░░░░▌ ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
#   ▀▀▀▀▀▀▀▀▀▀   ▀         ▀       ▀       ▀         ▀       ▀            ▀         ▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀
#

def create_faker_instance(locale='en_US'):
    return Faker(locale)

def get_user_locale():
    # Prompt the user to enter a locale
    locale = input("Enter the locale (e.g., 'en_US', 'id_ID', 'fr_FR'): ")
    return locale

# Get locale from user input
locale = get_user_locale()
fake = create_faker_instance(locale)

# Generate fake data
def generate_fake_data():
    return {
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'date_of_birth': fake.date_of_birth(minimum_age=17, maximum_age=70).strftime('%Y-%m-%d'),
        'job': fake.job(),
        'company': fake.company()
    }

# Generate and print fake data
fake_data = generate_fake_data()
for key, value in fake_data.items():
    print(f"{key}: {value}")
