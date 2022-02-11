def swap(value):

	leftmost = (value & int('0x000000FF', 16)) >> 0
	left_middle = (value & int('0x0000FF00', 16)) >> 8
	right_middle = (value & int('0x00FF0000', 16))>> 16
	rightmost = (value & int('0xFF000000', 16))>> 24

	leftmost <<= 24
	left_middle <<= 16
	right_middle <<= 8
	rightmost <<= 0

	return (leftmost | left_middle | right_middle | rightmost)


def builtin_swap(value):

	byte_val = (value).to_bytes(4, byteorder='little')
	big_end_val = int.from_bytes(byte_val, byteorder='big')
	little_end_val = int.from_bytes(byte_val, byteorder='little')

	return (big_end_val, little_end_val)


if __name__ == '__main__':

	nums = [255, 150, 128, 100, 64, 55, 40, 25, 16, 10]
	big_end_custom = []
	lit_end_custom = []
	big_end_builtin = []
	lit_end_builtin = []

	for num in nums:

		# Using custom little to big endian and vice versa function
		big_end = swap(num)
		little_end = swap(big_end)

		big_end_custom.append(big_end)
		lit_end_custom.append(little_end)

		# Using little to big endian and vice versa function with built-in methods inside
		big_end, little_end = builtin_swap(num)
		big_end_builtin.append(big_end)
		lit_end_builtin.append(little_end)

	print('nums: ', nums)
	print('big endian using custom func: \n', big_end_custom)
	print('big endian using built-in methods: \n', big_end_builtin)
	print('little endian using custom func: \n', lit_end_custom)
	print('little endian using built-in methods: \n', lit_end_builtin)

