from random import choice, randint


class AlphabetNode:
    def __init__(self, number, start):
        self.start = start
        self.number = number
        self.lookup_table = []

        for i in range(self.number - 1):
            self.lookup_table.append(0)

    def fill_lookup_table(self):

        self.lookup_table[0] = 1

        for i in range(1, self.number):

            count_values = 1
            value = i

            while value != 1:
                # print(i, count_values)
                self.lookup_table[count_values] = value
                value = (value * i) % self.number
                count_values += 1

            if count_values + 1 == self.number:
                # print("Generatorul este", i)
                return i


class EncryptionStructure:

    def __init__(self, alphabet_read):
        self.alphabet = alphabet_read
        self.length = len(self.alphabet)
        self.equivalents = []
        self.equivalents_lengths = []
        self.prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
        self.prime_numbers_length = len(self.prime_numbers)

    def find_equivalents_length(self, number):

        random_prime = 0

        if number == 2:
            self.equivalents_lengths.append(3)
            return

        for i in range(self.prime_numbers_length - 1, -1, -1):
            rem = number - self.prime_numbers[i]

            if rem > 0 and i - 1 >= 0 and random_prime == 0:
                random_prime = i-1

            if rem in self.prime_numbers:
                # print("Found")
                self.equivalents_lengths.append(rem)
                self.equivalents_lengths.append(self.prime_numbers[i])
                self.equivalents_lengths.append(3)
                return

        # print(random_prime)
        random_prime = self.prime_numbers[randint(0, random_prime)]
        self.equivalents_lengths.append(random_prime)
        self.find_equivalents_length(number - random_prime + 1)

    def print_equivalent_lengths(self):
        sum = 0
        cnt =0
        for elem in self.equivalents_lengths:
            sum += elem
            cnt += 1

        print(sum - cnt)
        #print(sum - cnt)
        print(self.equivalents_lengths)

    def create_equivalents(self):
        current_position = 0

        for i in range(len(self.equivalents_lengths)):
            node = AlphabetNode(self.equivalents_lengths[i], current_position)
            node.fill_lookup_table()
            self.equivalents.append(node)

            current_position += self.equivalents_lengths[i] - 1

    def print_equivalents(self):

        for elem in self.equivalents:
            print(elem.start, elem.lookup_table)


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
encryption_machine = EncryptionStructure(alphabet)

encryption_machine.find_equivalents_length(len(alphabet))
encryption_machine.print_equivalent_lengths()
encryption_machine.create_equivalents()
encryption_machine.print_equivalents()