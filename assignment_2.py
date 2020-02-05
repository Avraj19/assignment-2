# section 1
hero_name = input('Enter hero name: ').capitalize().strip()
villain_name = input('Enter villain name: ').capitalize().strip()

name_dict = {
    'Hero': hero_name,
    'villain': villain_name,
    'Beginning': 'In the beginning there was a hero but '
                 'he called himself '+ hero_name,
    'Middle': 'Life was good, what felt like forever.'
              'As our hore was having this though a villian '
              'was born at the same time and his name was' + villain_name,
    'End': 'Some time had passed, the villain grow up and the hero became old.'
           'when they first meat a fight broke out, one instantly understanding the other.'
           'In the end they no one won this meaning less fight.'
}

# section2
print(name_dict)