class MissingElementInTwoList:

    full_set = [4, 12, 9, 5, 6]
    partial_set = [4, 9, 12, 6]
    # Missing ele => 5

    def find_missing(full_set, partial_set):
        missing_items = set(full_set) - set(partial_set)
        assert(len(missing_items) == 1)
        return list(missing_items)[0]

    # Optimized

    def find_missing_xor(full_set, partial_set):
        xor_sum = 0
        for num in full_set:
            xor_sum ^= num
        for num in partial_set:
            xor_sum ^= num

        return xor_sum

    print(find_missing(full_set, partial_set))
    print(find_missing_xor(full_set, partial_set))