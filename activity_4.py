# sum of two numbers that will get the target.
def sum_two_for_target(num_arr: list[int], target: int) -> list:
    seen = {}
    result = []

    for num in num_arr:
        complement = target - num

        if complement in seen:
            import pdb; pdb.set_trace()
            result.append((num, complement))

        seen[num] = True

    return result
