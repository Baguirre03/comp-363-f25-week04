class Museum:
    def __init__(self, values, weights, c_max):
        self.values: list[int | None] = values
        self.weights: list[int | None] = weights
        self.c_max: int = c_max
        self._table: list[list[list[int, set]]] = [
            [[0, set()] for _ in range(self.c_max + 1)]
            for _ in range(len(self.weights) + 1)
        ]
        # results
        self.optimal_subset: set[int] = None
        self.optimal_weight: int = None
        self.optimal_value: int = None
        self._MULTIPLIER = 2
        self.LENGTH_OF_MATRIX = len(self._table) * len(self._table[0])
        # Our dynamic programming table will hold [price, items]
        # that will enable us tlet us know
        # which items we are using for the price and then the price for comparisons

    def solve(self):
        """
        Finds the optimal subset for among all items whose weights and values were given,
        Prints the following information:
        1. How many subsets were theoretically possible
        2. What was the size of matrix `S`
        3. How many items are in the optimal subset
        4. What is their total weight,
        5. How does it compare to the capacity restriction `c_max`
        6. What is the total value of all the items in the subset.
        """
        self._build_subsets()
        self._print_size_of_matrix()
        self._find_optimal_subset()
        for row in self._table:
            print(row)

    def _find_optimal_subset(self):
        n: int = len(self._table)
        m: int = len(self._table[0])
        for i in range(n):
            weight = self.weights[i - 1] or 0
            for j in range(m):
                above_cell = self._table[i - 1][j]
                if j - weight >= 0:
                    best_money, best_set = self._table[i - 1][j - weight]
                    value = self.values[i - 1] if self.values[i - 1] else 0
                    if above_cell[0] > best_money + value:
                        self._table[i][j] = above_cell
                    else:
                        self._table[i][j][0] = best_money + value
                        print(best_set, weight)
                        self._table[i][j][1].update(best_set)
                        self._table[i][j][1].add(weight)
                        print(self._table[i][j][1])
                else:
                    self._table[i][j] = above_cell

    def _build_subsets(self):
        POSSIBLE_SUBSETS = self._MULTIPLIER ** (len(self.values) - 1)
        print(f"Possible amount of subsets: {POSSIBLE_SUBSETS}")

    def _print_size_of_matrix(self):
        print(
            f"Size of matrix S: {self.LENGTH_OF_MATRIX}; Rows: {len(self._table)}, Cols: {len(self._table[0])}"
        )

    def _optimal_subset_weight(self):
        pass

    def _capacity_resction(self):
        pass


if __name__ == "__main__":
    ms = Museum(
        [None, 10, 5, 16, 11],
        [
            None,
            3,
            2,
            4,
            4,
        ],
        10,
    )

    ms.solve()
