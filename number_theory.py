from typing import List, Tuple
import string, re

def find_values2(number, base):
	res = []
	while number > 0:
		res.append(number % base)
		number //= base
	return res[::-1]

def gcd(a: int, b: int, nums: Tuple[int, int]=None, show_steps: bool = True) -> int:
	# a = bq + r
	if b == 0:
		if show_steps:
			print(f'GCD: {a}\ndone.')
		return a
	elif b == 1:
		print(f'{nums[0]} and {nums[1]} are relatively prime.')
		return 1
	else:
		if show_steps:
			print(f'{a} = {b}({a//b}) + {a % b}')
		return gcd(b, a % b, (a, b), show_steps)

def lcm(a, b):
	return abs(a * b) // gcd(a, b)

def convert_bases(curr_base: int, val: str, to_base: int, digits: List[str]=[]) -> str:
	if int(val) // to_base == 0:
		digits.append(f'{int(val) % to_base}')
		return ''.join(digits)[::-1]
	elif to_base == 10:
		places = find_values2(int(val), to_base)
		result = 0
		idx = len(places) - 1
		for i, e in enumerate(places):
			result += (7**i)*places[idx]
			idx -= 1
		return result
	else:
		if curr_base < 10:
			digits.append(f'{int(val) % to_base}')
			print('base is greater than 10')
			return convert_bases(curr_base, int(val) // to_base, to_base)
		else:
			alpha = [chr(i) for i in range(97, 123)]
			num = int(val)
			print(f'val: {alpha[(num % curr_base) - 10]}, num: {num}')
			digits.append(f'{alpha[(num % curr_base) - 10]}') if num % curr_base > 9 else digits.append(f'{num % curr_base}')
			return convert_bases(curr_base, num // to_base, to_base)

def diophantine_eq(a:int, b: int, c: int):
	d = gcd(a, b)
	if c % d == 0:
		print(f'{a}x + {b}y = {c} has a solution.')
	else:
		print(f'{a}x + {b}y = {c} has no solution.')


# newVal = convert_bases(10, '2019', 8)
# print(f'2019 in base 10 to base 8 is: {newVal}')

# gcd(3171, 1953)
# diophantine_eq(35, 63, 210)
print(f'lcm(3171, 1953): {lcm(12, 15)}')
