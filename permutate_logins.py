def generate_usernames(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            full_name = line.strip().split()
            if len(full_name) >= 2:
                first_name = full_name[0]
                last_name = full_name[-1]
                middle_names = full_name[1:-1]

                first_initial = first_name[0]
                last_initial = last_name[0]
                middle_initials = ''.join([name[0] for name in middle_names]) if middle_names else ''

                usernames = [
                    f"{first_initial.lower()}.{last_name.lower()}",
                    f"{first_initial.upper()}.{last_name.capitalize()}",
                    f"{first_name.capitalize()}.{last_name.capitalize()}",
                    f"{last_initial.lower()}.{first_name.lower()}",
                    f"{last_initial.upper()}.{first_name.lower()}",
                    f"{first_initial.lower()}{last_name.lower()}",
                    f"{first_name.lower()}{last_initial.lower()}",
                    f"{first_name.lower()}{last_name.lower()}",
                    f"{first_initial.lower()}{middle_initials.lower()}{last_name.lower()}",
                    f"{first_name.lower()}.{last_name.lower()}",
                    f"{last_name.lower()}{first_initial.lower()}",
                    f"{first_initial.lower()}{last_initial.lower()}",
                    f"{first_name[:3].lower()}{last_name[:3].lower()}",
                ]

                for username in usernames:
                    outfile.write(username + '\n')

input_file = 'names'
output_file = 'users'

generate_usernames(input_file, output_file)
