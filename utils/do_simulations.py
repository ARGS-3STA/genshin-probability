from algorithm import four_star_probability


def do_simulations(amount: int, wishes: int) -> list[int]:
    four_stars_from_simulations = []

    for _ in range(amount):
        four_stars_from_simulations.append(four_star_probability.simulation(wishes))

    return four_stars_from_simulations
