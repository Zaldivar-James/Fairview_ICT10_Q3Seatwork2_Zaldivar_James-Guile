from pyscript import display, document

def sign_up(e):
    # Resetting the values
    document.getElementById('team-output').innerHTML = ''

    # Adding the registration and clearance variables
    register_true = document.getElementById('yes_reg').checked
    register_false = document.getElementById('not_registered').checked
    registration = 'yes' if register_true else 'no' if register_false else ''

    clearance_true = document.getElementById('yes_med').checked
    clearance_false = document.getElementById('no_med').checked
    clearance = 'yes' if clearance_true else 'no' if clearance_false else ''

    grade_level = int(document.getElementById('grade_level').value)
    section = document.getElementById('section').value

    if registration == 'yes':
            if clearance == 'yes':
                    if section == 'emerald':
                        display("team 1", target='team-output')
                    elif section == 'ruby':
                        display("team 2", target='team-output')
                    elif section == 'sapphire':
                        display("team 3", target='team-output')
                    elif section == 'topaz':
                        display("team 4", target='team-output')
                    else:
                        display("invalid section.", target='team-output')
            else:
                display("Go to clinic, NOW.", target='team-output')
    else:
            display("register online pls.", target='team-output')