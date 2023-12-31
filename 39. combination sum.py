class Solution:
    def combinationSum(self, candidates, target):
        results = []

        # prune candidates
        candidates = [c for c in candidates if c <= target]

        # sort candidates. this will help avoid unnecessary branches in the tree (see below code)
        candidates.sort()

        # this memo stores the frequencies
        # if we have crossed over a particular frequency pattern before, we don't need to traverse that tree
        # this will help avoid saving results that are actually the same, but have different ordering
        memo = []

        def backtrack(sumList, sum, freq):
            if sum == target:
                # print(sumList)
                results.append([x for x in sumList])
                return True
            
            if sum >= target:
                return False

            for candidate in candidates:
                sum += candidate
                sumList.append(candidate)
                freq[candidate] += 1

                if freq in memo:
                    # don't traverse tree if frequency pattern has already been covered
                    # continue to next candidate neighbour
                    sum -= candidate
                    sumList.pop()
                    freq[candidate] -= 1
                    continue

                succeded = backtrack(sumList, sum, freq)

                if sum > target and not succeded:
                    # remember candidates are sorted
                    # if the sum was greater than the target for the current branch, and we didn't succeed, then there's no point in going to the neighbour branches, because they will obviously give larger sums
                    sum -= candidate
                    sumList.pop()
                    freq[candidate] -= 1
                    break
                
                if freq not in memo: memo.append({k:freq[k] for k in freq})
                sum -= candidate
                sumList.pop()
                freq[candidate] -= 1


        backtrack([], 0, {candidate: 0 for candidate in candidates})
        return results

print(Solution().combinationSum([36,21,2,3,23,24,38,22,11,14,15,25,32,19,35,26,31,13,34,29,12,37,17,20,39,30,40,28,27,33], 35))