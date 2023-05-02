# poker-run
Repo for testing out a program to play poker where someone is emailed one card per day.

## To run:
- Run the poker_run.py Python file somehow, such as "python ./poker_run.py"

## To configure:
- You can add people to the game by adding their details into the emails.csv list. Do not put real emails in this list and push back to GitHub. Only run with real emails if you fork this and make private, or if running only locally. 
- For example, you can add someone new using this format: "Bob,fakeemail". And that's it! The script will keep track of which cards have been used in that same file.

## Implementation Details:
- The game will keep track of what used cards you have by taking everything in column #2 on (using 0 indexing)
- If there is desire to send out emails, that will have to be customized to your scenario. Could likely use Outlook/Gmail APIs to format and send as an email.
- This is a very basic implementation of a poker run. If updates become more complicated, it could be worth it to switch to Pandas for reading/writing csvs.
