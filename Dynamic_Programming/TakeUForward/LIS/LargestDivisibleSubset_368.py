#O(n^2)
def divisible_set(nums):

    if len(nums) == 0: return []
    nums.sort()
    sol = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                sol[i] = sol[j] + [nums[i]]
    return max(sol, key=len)

if __name__ == "__main__":
    # Legge l'array da tastiera
    arr = list(map(int, input("Inserisci gli elementi dell'array separati da spazi: ").split()))

    ans = divisible_set(arr)

    print("Gli elementi del sottoinsieme divisibile più lungo sono: ", end="")
    for i in ans:
        print(i, end=" ")
    print()