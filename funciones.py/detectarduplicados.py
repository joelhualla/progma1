emails = {
    "user1": "correo@gmail.com",
    "user2": "test@yahoo.com",
    "user3": "correo@gmail.com",
    "user4": "otra@outlook.com"
}

comidos= set()

for user, email in emails.items():
    if email in comidos:
        print(f"{email}se repitio")
    else:
        comidos.add(email)

