def send_email(message, recipient, sender="university.help@gmail.com"):
    valid_domains = [".com", ".ru", ".net"]

    if "@" not in recipient or not any(recipient.endswith(domain) for domain in valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if "@" not in sender or not any(sender.endswith(domain) for domain in valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на {recipient}")
    else:
        print(f"Нестандартный отправитель! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email("Привет!", "student@example.com")
send_email("Привет!", "studentexample.com")
send_email("Привет!", "student@example.com", "student@example.com")
send_email("Привет!", "student@example.com", "custom.sender@gmail.com")
