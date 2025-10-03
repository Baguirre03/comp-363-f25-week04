class Museum:
    def __init__(self, values, weights, c_max):
        self.values: list[int | None] = values
        self.weights: list[int | None] = weights
        self.c_max: int = c_max
        self._table: list[list[list[int, set]]] = [
            [[0, set()] for _ in range(self.c_max + 1)]
            for _ in range(len(self.weights))
        ]
        self.LENGTH_OF_MATRIX = len(self._table) * len(self._table[0])
        # Our dynamic programming table will hold [price, items]
        # that will enable us tlet us know
        # which items we are using for the price and then the price for comparisons

    def solve(self):
        """
        Finds the optimal subset for among all items whose weights and values were given,
        Prints the following information:
        1. How many subsets were theoretically possible :check:
        2. What was the size of matrix `S` :check:
        3. How many items are in the optimal subset :check:
        4. What is their total weight, :check:
        5. How does it compare to the capacity restriction `c_max` :check:
        6. What is the total value of all the items in the subset. :check:
        """
        # DP table
        self._build_dp_table()
        # problems form question
        self._print_valid_subsets()  # 1
        self._print_line()
        self._print_size_of_matrix()  # 2
        self._print_line()
        self._print_optimal_subset_item_count()  # 3
        self._print_line()
        self._print_optimal_weight()  # 4
        self._print_line()
        self._print_capacity_comparison()  # 5
        self._print_line()
        self._print_optimal_value()  # 6

    def _build_dp_table(self):
        n: int = len(self._table)
        m: int = len(self._table[0])
        for i in range(1, n):
            weight = self.weights[i]
            for j in range(m):
                above_cell = self._table[i - 1][j]
                if j - weight >= 0:
                    best_money, best_set = self._table[i - 1][j - weight]
                    value = self.values[i]
                    if above_cell[0] > best_money + value:
                        self._table[i][j] = above_cell
                    else:
                        self._table[i][j][0] = best_money + value
                        self._table[i][j][1].update(best_set)
                        self._table[i][j][1].add(i)
                else:
                    self._table[i][j] = above_cell

    def _print_valid_subsets(self) -> None:
        """
        Goes through the dp table and checks the indices in the subset we have created at the point
        in the table and adds it to a set with the total value + indices that we took for that subset
        since weights can be duplicate we instead store the weight_indice in our DP table
        """
        subsets: set[tuple[int, tuple[int, ...]]] = set()
        for row in self._table:
            for value, indices in row:
                if indices:  # non-empty
                    subsets.add((value, tuple(indices)))

        print("Possible Theoretical Subsets:")
        for value, indices in subsets:
            print(f"values: {value}, possible with weight indices: {list(indices)}")

    def _print_size_of_matrix(self):
        """
        Takes the length of information provided and prints the size of the matrix
        """
        print(
            f"Size of matrix S: {self.LENGTH_OF_MATRIX}; Rows: {len(self._table)}, Cols: {len(self._table[0])}"
        )

    def _print_optimal_subset_item_count(self) -> None:
        """
        grabs the optimal subset in the bottom right corner of table and prints length
        """
        optimal_subset: set[int] = self._table[-1][-1][1]
        print(f"Length of optimal subset: {len(optimal_subset)}")

    def _print_optimal_weight(self) -> None:
        """
        Grabs optimal subset in bottom right corner and prints total weight
        """
        optimal_subset: set[int] = self._table[-1][-1][1]
        total_weight = sum(self.weights[i] for i in optimal_subset)
        print(f"Total weight of optimal subset: {total_weight}")

    def _print_capacity_comparison(self) -> None:
        """
        Compares weight of optmal subset to c_max
        """
        total_weight: int = sum(self.weights[i] for i in self._table[-1][-1][1])
        print(
            f"c_max: {self.c_max}, Weight of optimal subset: {total_weight}, Difference: {self.c_max - total_weight}"
        )

    def _print_optimal_value(self) -> None:
        """
        Prints the value of the optimal subset
        """
        value: int = self._table[-1][-1][0]
        print(f"Value of optimal subset: {value} (we stole this much!)")

    def _print_line(self) -> None:
        print("-----------------------")


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
