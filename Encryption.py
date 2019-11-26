from random import choice, randint

class EncryptionStructure:

    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.length = len(self.alphabet)
        self.equivalents = []
        self.equivalents_lengths = []
        self.prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
        self.prime_numbers_length = len(self.prime_numbers)

    def find_equivalents_length(self, number):

        random_prime = 0

        if number == 2:
            self.equivalents_lengths.append(number)
            return

        for i in range(self.prime_numbers_length - 1, -1, -1):
            rem = number - self.prime_numbers[i]

            if rem > 0 and i - 1 >= 0 and random_prime == 0:
                random_prime = i-1

            if rem in self.prime_numbers:
                #print("Found")
                self.equivalents_lengths.append(rem)
                self.equivalents_lengths.append(self.prime_numbers[i])
                return

        #print(random_prime)
        random_prime = self.prime_numbers[randint(0, random_prime)]
        self.equivalents_lengths.append(random_prime)
        self.find_equivalents_length(number - random_prime)

    def print_equivalents(self):
        print(self.equivalents_lengths)

    def create_equivalents(self):
        pass


alphabet = ['a', 'c', 'e', 'g', 'i', 'm', 'o']
encryption_machine = EncryptionStructure(alphabet)

encryption_machine.find_equivalents_length(len(alphabet))
encryption_machine.print_equivalents()
