#!/usr/bin/env python3
import random
import argparse


class Door:
    car: bool = False

class MontyHall:
    def __init__(self, *, switch) -> None:
        self.switch = switch

    def simulate(self) -> bool:
        """
        Runs MontyHall simulation and returns true if a door with a car was chosen.
        Otherwise, it returns false.
        """
        # Create a list of 2 empty doors and one with a car
        doors = [Door(), Door(), Door()]
        car_door_idx = random.randint(0, 2)
        doors[car_door_idx].car = True

        # Choose a door
        first_choice_idx = random.randint(0, 2)
        result = doors[first_choice_idx]

        assert self.check_one_car_occurence(doors)
        assert len(doors) == 3
        assert result in doors

        # Get door to remove index
        remove_door_idx = None
        for idx, door in enumerate(doors):
            if idx != first_choice_idx and not door.car:
                remove_door_idx = idx
        assert remove_door_idx is not None

        # Remove door from list
        removed_door = doors.pop(remove_door_idx)
        assert remove_door_idx != first_choice_idx
        assert self.check_one_car_occurence(doors)
        assert len(doors) == 2
        assert result in doors
        assert removed_door not in doors

        # If switching choose remaining door
        if self.switch:
            if first_choice_idx > remove_door_idx:
                new_result = doors[first_choice_idx - 2]
            else:
                new_result = doors[first_choice_idx - 1]
            assert new_result != result
            assert new_result in doors
            result = new_result
        
        return result.car

    def check_one_car_occurence(self, doors):
        occurrences = 0
        for door in doors:
            occurrences = occurrences + 1 if door.car else occurrences
        return occurrences == 1

def get_args():
    parser = argparse.ArgumentParser(
        description='Monty Hall',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-n',
        '--number-of-simulations',
        help='Number of simulations to be run',
        type=int,
        default=100_000
    )
    parser.add_argument(
        '-s',
        '--switch',
        help='Switch door option. If unset will stay with first choice.',
        action='store_true'
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    n_simulations = args.number_of_simulations
    switch = args.switch
    times_sim_resulted_in_car = 0
    monty_hall = MontyHall(switch=switch)
    for simulation in range(n_simulations):
        if monty_hall.simulate():
            times_sim_resulted_in_car += 1
    
    probability = times_sim_resulted_in_car / n_simulations

    print(f"Running {n_simulations} simulations.")
    if switch:
        print(f"Switch probability: {probability}")
    else:
        print(f"Stay probability: {probability}")
