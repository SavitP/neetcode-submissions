class Solution:
    def trap(self, height: List[int]) -> int:
        toReturn = 0
        l = 0
        r = len(height) - 1
        lc = 1
        rc = r - 1
        while rc >= lc:
            if (height[l] < height[r]):
                if (height[l] < height[lc]):
                    l = lc
                    lc = l + 1
                else:
                    lc += 1
            else:
                if (height[r] < height[rc]):
                    r = rc
                    rc = r - 1
                else:
                    rc -= 1
        print(l)
        print(r)
        for i in range(l + 1, r):
            toReturn += (min(height[l], height[r]) - height[i])
        while l > 0:
            ll = 0
            llc = 1
            while llc != l:
                if (height[llc] > height[ll]):
                    ll = llc
                    llc = ll + 1
                else:
                    llc += 1
            for i in range(ll + 1, l):
                toReturn += (height[ll] - height[i])
            l = ll
        while r < len(height) - 1:
            rr = len(height) - 1
            rrc = rr - 1
            while rrc != r:
                if (height[rrc] > height[rr]):
                    rr = rrc
                    rrc = rr - 1
                else:
                    rrc -= 1
            for i in range(r + 1, rr):
                toReturn += (height[rr] - height[i])
            r = rr
        return toReturn
        