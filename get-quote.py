import datetime
import random


def get_random_quote(quotes):
    rnd = random.randint(0, len(quotes) - 1)
    return quotes[rnd].rstrip("\n")


def entry():
    # print("Keep it logically awesome.")

    f = open("quotes.txt", "r+")
    f.write("Dynamic quote at {0}\n".format(datetime.date.today().strftime("%c")))
    quotes = f.readlines()
    f.close()
    print(get_random_quote(quotes))
    print(get_random_quote(quotes))


if __name__ == "__main__":
    entry()
