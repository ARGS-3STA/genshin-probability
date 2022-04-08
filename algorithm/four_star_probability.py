import random

FOUR_STAR_PROBABILITY = 0.051


def simulation(wish_amount: int) -> int:
    four_star_count = 0
    pity_counter = 0

    for _ in range(wish_amount):
        if random.random() < FOUR_STAR_PROBABILITY or pity_counter == 9:
            four_star_count += 1
            pity_counter = 0
        else:
            pity_counter += 1

    return four_star_count


def main() -> None:
    print(simulation(10000))


if __name__ == "__main__":
    main()
