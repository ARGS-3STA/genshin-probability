from graph import Histogram
from utils.do_simulations import do_simulations


def main() -> None:
    WISHES = 100
    SIMULATION_COUNT = 100000
    values = do_simulations(SIMULATION_COUNT, WISHES)
    hist = Histogram(values)
    print(hist.calculate_average_value())
    print(hist.average_four_star_per_simulation(WISHES))
    hist.show()


if __name__ == "__main__":
    main()
