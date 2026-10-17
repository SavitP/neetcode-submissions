class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s1) + len(s2) != len(s3):
            return False
        def explore(ns1, ns2, ns3):
            if ns3 == "":
                return True
            if (ns1, ns2, ns3) in dp:
                return dp[(ns1, ns2, ns3)]
            if ns1 == "" or ns1[0] != ns3[0]:
                if ns2 != "" and ns2[0] == ns3[0]:
                    dp[(ns1, ns2, ns3)] = explore(ns1, ns2[1:], ns3[1:])
                    return dp[(ns1, ns2, ns3)]
                else:
                    dp[(ns1, ns2, ns3)] = False
                    return False
            if ns2 == "" or ns2[0] != ns3[0]:
                if ns1[0] == ns3[0]:
                    dp[(ns1, ns2, ns3)] = explore(ns1[1:], ns2, ns3[1:])
                    return dp[(ns1, ns2, ns3)]
                else:
                    dp[(ns1, ns2, ns3)] = False
                    return False
            else:
                dp[(ns1, ns2, ns3)] = explore(ns1[1:], ns2, ns3[1:]) or explore(ns1, ns2[1:], ns3[1:])
                return dp[(ns1, ns2, ns3)]
            
        return explore(s1, s2, s3)
