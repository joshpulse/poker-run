import csv
import random


def get_email_list():
    email_list = []
    with open('emails.csv') as email_csv:
        csv_reader = csv.reader(email_csv, delimiter=',')
        headers = next(csv_reader)
        for row in csv_reader:
            email_list.append(row)

        return headers, email_list


def build_deck(used_cards: list):
    # Standard 52 Card Deck
    card_list = []
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    types = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    for suit in suits:
        for card_type in types:
            card_name = f'{card_type} of {suit}'

            # Check if card name has already been used
            if card_name in used_cards:
                continue
            else:
                card_list.append(card_name)

    return card_list


def choose_card(card_list: list):
    card = random.choice(card_list)
    return card


def send_email(card):
    # Fill out with email logic
    pass


def update_email_list(headers, email_list):
    with open('emails.csv', 'w') as email_csv:
        csv_writer = csv.writer(email_csv)
        csv_writer.writerow(headers)
        csv_writer.writerows(email_list)


def main():
    # Create list to write updated details back to the file
    updated_emails_list = []

    # Get the email list and cards that have already been used
    headers, email_list = get_email_list()

    for person in email_list:
        # Build a deck excluding cards that have already been used
        used_cards = person[2:]
        card_list = build_deck(used_cards=used_cards)
        card = choose_card(card_list=card_list)

        # Build this function out, or send information manually
        # can route this output to a file. For now, printing to terminal.
        send_email(card)
        print(f'For {person[0]}, with the email address{person[1]}, I have selected {card}.')

        # Update the person's list with the used card
        # Later write the card that was used back to the file so that we can keep track of what has been used already
        person.append(card)
        updated_emails_list.append(person)

    update_email_list(headers=headers, email_list=updated_emails_list)
    print('Process was successful. Status Code: 200')


main()
