def make_periodic_table(periodic_table_list):
    return periodic_table_list


def main():
    periodic_table_list = [
        # [symbol, name, atomic_mass]
        ["Ac", "Actinium", 227],
        ["Ag", "Silver", 107.8682],
        ["Al", "Aluminum", 26.9815386],
        ["Ar", "Argon", 39.948],
        ["As", "Arsenic", 74.9216],
        ["At", "Astatine", 210],
        ["Au", "Gold", 196.966569],
        ["B", "Boron", 10.811],
        ["Ba", "Barium", 137.327],
        ["Be", "Beryllium", 9.012182],
        ["Zr", "Zirconium", 91.224],
    ]

    # periodic_table = PeriodicCalculator()
    table_list = make_periodic_table(periodic_table_list)

    for element in table_list:
        symbol, name, atomic_mass = element[0], element[1], element[2]
        print(f"{name} {atomic_mass}")


if __name__ == "__main__":
    main()
