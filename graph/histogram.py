import matplotlib.pyplot as plt
from utils.math import average


class Histogram:
    def __init__(self, values: list[int]):
        self.values = values

    def show(self) -> None:
        plt.hist(self.values)
        plt.show()

    def calculate_average_value(self) -> float:
        return average(self.values)

    def average_four_star_per_simulation(self, wishes: int) -> float:
        return average(self.values) / wishes


def main() -> None:
    hist = Histogram(1, 1, 1, 1, 3, 3, 3, 3)
    hist.show()


if __name__ == "__main__":
    main()
