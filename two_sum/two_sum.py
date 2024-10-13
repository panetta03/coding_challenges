def sum_two_num(nums,target):
        
        seen = {}
        n = len(nums)

        for indx, num in enumerate(nums):
                complement = target - num
                print(f"Index: {indx}, Number: {num}, Complement: {complement}, Seen: {seen}")
                if complement in seen:
                    return [seen[complement], indx]
                seen[num] = indx