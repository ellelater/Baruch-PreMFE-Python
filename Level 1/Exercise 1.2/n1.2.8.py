"""
This program demonstrates list difference using comprehension.
"""


def main():
    players = ["Anna", "Bob", "Carlo", "David", "Elle",
               "Frank", "Garry", "Hans", "Ian", "Jack"]
    injured_players = ["Anna", "Bob", "Carlo", "David", "Frank",
                       "Garry", "Hans", "Ian", "Jack"]

    # list that contains all active players
    active_player = [player for player in players if player not in injured_players]
    # print active_player

if __name__ == "__main__":
    main()
