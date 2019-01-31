def optimizeBubbleSort(nums):
	n = len(nums)

	last = n-1

	for i in range(n):
		isSorted = True
		curr = -1

		for j in range(last):
			if nums[j] > nums[j+1]:
				temp = nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = temp
				isSorted = False
				curr = j

		if isSorted:
			return

		last = curr



if __name__ == '__main__':
	nums = input("Enter list of unsorted integers seperated by space: ")

	nums = nums.split()

	nums = [int(nums[i]) for i in range(len(nums))]

	optimizeBubbleSort(nums)

	print ("Sorted array: " + str(nums))