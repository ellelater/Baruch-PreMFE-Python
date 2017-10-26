def main():
    a = range(1000)
    a_rever_iter = iter(reversed(a))
    for i in a_rever_iter:
        print i


if __name__ == "__main__":
    main()
