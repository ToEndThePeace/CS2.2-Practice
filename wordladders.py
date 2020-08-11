# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
import string


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


word_set = set()
with open("words.txt") as f:
    for word in f:
        word_set.add(word.strip().lower())


def get_neighbors(word):
    word_letters = list(word)
    neighbors = set()

    for i in range(len(word_letters)):
        for letter in string.ascii_lowercase:
            cur_word = list(word_letters)
            cur_word[i] = letter
            cur_word = "".join(cur_word)
            if cur_word in word_set and cur_word != word:
                neighbors.add(cur_word)

    return neighbors


def find_word_ladder(begin_word, end_word):  # BFS across the graph
    visited = set()
    q = Queue()
    q.enqueue([begin_word])
    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return None


print(find_word_ladder("sail", "boat"))
