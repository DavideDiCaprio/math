import random

def throw_dice(num_faces: int = 6) -> int:
    '''Simulate throwing a single die '''
    if num_faces < 1:
        raise ValueError("Number of faces must be at least 1")
    return random.randint(1, num_faces)


def sum_throw_two_dice(num_faces: int = 6) -> int:
    '''Simulate throwing two dice and sum their results. '''
    return throw_dice(num_faces) + throw_dice(num_faces)


def throw_n_dice(num_dice: int, num_faces: int = 6) -> list[int]:
    '''Simulate throwing multiple dice. '''
    if num_dice < 1:
        raise ValueError("Number of dice must be at least 1")
    return [throw_dice(num_faces) for _ in range(num_dice)]


def measure_frequency_of_outcome(outcome: int, list_of_outcomes: list[int]) -> None:
    ''' Measure and print the frequency of a specific outcome. '''
    if not list_of_outcomes:
        print("No outcomes to measure")
        return

    count = sum(1 for x in list_of_outcomes if x == outcome)
    frequency = count / len(list_of_outcomes)
    print(f'The frequency of {outcome} is {frequency:.2%}')


def measure_frequency_of_outcomes(list_of_outcomes: list[int]) -> None:
    ''' Measure and print frequencies of all outcomes. '''
    if not list_of_outcomes:
        print("No outcomes to measure")
        return

    for outcome in sorted(set(list_of_outcomes)):
        measure_frequency_of_outcome(outcome, list_of_outcomes)


def estimate_probability_of_dice_faces(n_throws: int, num_faces: int = 6) -> None:
    ''' Estimate probability distribution of dice faces through simulation. '''
    if n_throws < 1:
        raise ValueError("Number of throws must be at least 1")

    print(f'\nEstimating with {n_throws:,} throws')
    outcomes = throw_n_dice(n_throws, num_faces)
    measure_frequency_of_outcomes(outcomes)


def main() -> None:
    """Run demonstrations of all dice-related functions."""
    print("\n1. Basic dice throw (6 faces):")
    result = throw_dice()
    print(f"Single throw result: {result}")
    
    print("\n2. Dice throw with custom faces (10 faces):")
    result = throw_dice(num_faces=10)
    print(f"Single throw result with 10 faces: {result}")
    
    print("\n3. Sum of two dice throws:")
    result = sum_throw_two_dice()
    print(f"Sum of two dice: {result}")
    
    print("\n4. Throwing multiple dice:")
    results = throw_n_dice(num_dice=3)
    print(f"Results of throwing 3 dice: {results}")
    
    print("\n5. Measuring frequency of a specific outcome:")
    outcomes = throw_n_dice(num_dice=1000)
    measure_frequency_of_outcome(6, outcomes)
    
    print("\n6. Measuring frequencies of all outcomes:")
    outcomes = throw_n_dice(num_dice=1000)
    measure_frequency_of_outcomes(outcomes)
    
    print("\n7. Running probability estimations with different sample sizes:")
    throw_counts = [20, 50, 100, 500, 1000]
    for n_throws in throw_counts:
        estimate_probability_of_dice_faces(n_throws=n_throws, num_faces=6)


if __name__ == "__main__":
    main()