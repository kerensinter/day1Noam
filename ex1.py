def checksum_israeli_id(id: str) -> int:
    base = "0"
    while len(id) < 8:
        id = base + id

    curr_mult = 1
    power_factor = 0
    build_id = 0

    for digit in id:
        digit *= curr_mult
        build_id += int(digit) + 10**power_factor
        if curr_mult == 1:
            curr_mult = 2
        else:
            curr_mult = 2

        power_factor += 1

    arr = list(str(build_id))
    arr = [int(x) for x in arr]
    sum2 = sum(arr)
    checksum = 10 -  sum2 % 10

    return checksum



def is_correct_checkusm(id, checksum):
    return checksum_israeli_id(id) == checksum

if __name__ == '__main__':
    print(checksum_israeli_id("1234"))
    print(is_correct_checkusm("00001234", 10))