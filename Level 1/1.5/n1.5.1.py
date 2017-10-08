def main():
    players = {'A', 'B', 'C'}
    injured_players = {'A'}
    print "active players:"
    for player in players - injured_players:
        print player,


if __name__ == '__main__':
    main()
