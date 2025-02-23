from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:

        if not strings or not all(isinstance(s, str) for s in strings):
            print("Некоректні вхідні дані.")
            return ""

        for word in strings:
            self.put(word)

        node = self.root
        prefix = ""

        while node and len(node.children) == 1:
            for char, child_node in node.children.items():
                prefix += char
                node = child_node

        if prefix:
            print(f"Найдовший спільний префікс: {prefix}")
        else:
            print("Спільного префікса немає.")

        return prefix


if __name__ == "__main__":

    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    print("Тест 1: ", strings)
    result = trie.find_longest_common_word(strings)
    if result:
        print(f"Результат: {result}\n")

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print("Тест 2: ", strings)
    result = trie.find_longest_common_word(strings)
    if result:
        print(f"Результат: {result}\n")

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    print("Тест 3: ", strings)
    result = trie.find_longest_common_word(strings)
    if result:
        print(f"Результат: {result}\n")
