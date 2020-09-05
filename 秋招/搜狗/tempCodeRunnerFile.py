
        # nums[2] -= nums[0]
        # nums[0] = 0
        res += self.helper([0, nums[1] - nums[0], nums[2] - nums[0]])
        