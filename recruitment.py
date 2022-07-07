def get_skills():
    # Add at least 3 random skills for the user to select from
    skills = ["Python", "C++", "Javascript", "Juggling", "Running", "Eating"]
    return skills


def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    for index, value in enumerate(skills):
        print(str(index+1) + ".", value)
9



def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here

    UserSkills = []
    skill11 = int(input("Choose a skill by entering its number: "))
    skill12 = int(input("Choose another skill by entering its number: "))
    getSkills = get_skills()
    for i in range(len(skills)):
        if i+1 == skill11:
            UserSkills.append(skills[i])
        if i+1 == skill12:
            UserSkills.append(skills[i])
    return UserSkills

def get_user_cv(skills):
    # Get the users CV from their inputs
    # Write your code here
    cv = {}
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    experience = int(input("How many years of experience do you have? "))
    show_skills(get_skills())
    userSkills = get_user_skills(skills)

    cv = {"name": name, "age": age, "experience": experience, "skills": userSkills}
    print(cv)
    return cv



def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    # cv = get_user_cv(cv)
    print(cv["skills"])
    cv.values()
    if (cv.get("age") >= 25 and cv.get("age") <= 40 and cv.get("experience") > 3 and (desired_skill in cv["skills"])) :
        return True
    else:
        return False


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    x = []
    print("Welcome to the special recruitment program, please answer the following questions: ")

    getSkills = get_skills()
    CV = get_user_cv(getSkills)
    check = check_acceptance(CV, "JavaScript")
    name = CV.get("name")
    if check:
        print(f"You have been accepted, {name}.")
    else:
        print(f"You have been rejected, {name}.")




if __name__ == "__main__":
    main()
