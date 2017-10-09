"""
This program demonstrates the use of zip as a filter in comprehension
"""


def main():
    actors = ['Ian Mckellen', 'Patrick Stewart', 'Hugh Jackman', 'Dafne Keen',
              'Stephen Merchant', 'Richard Grant', 'Boyd Holbrook']
    ages = [78, 77, 48, 12, 42, 60, 36]

    # 9a printing the result of zipping the names and ages
    print zip(actors, ages)

    # 9b list of actors with age > 18 using comprehension and zip
    old_actors = [name for (name, age) in zip(actors, ages) if age > 18]
    # print old_actors

    # same list but without zip
    old_actors2 = [actors[i] for i in range(len(ages)) if ages[i] > 18]
    # print old_actors2
    """ 
    Comprehension without zip is better because it accesses the ages with index
    therefore saves the cost of creating another list.
    """


if __name__ == "__main__":
    main()
