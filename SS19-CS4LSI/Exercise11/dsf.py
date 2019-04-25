class DSF:
    def __init__(self, comp=False, rbu=False): 
        self.parent = {}
        self.rank = {}
        self.comp = comp
        self.rbu = rbu

    def find(self, val):
        if self.parent[val] == val:
            return val
        else:
            res = self.find(self.parent[val])
            if self.comp: self.parent[val] = res				# Path compression
            return res
    def union(self, val1, val2):
        rep1, rep2 = self.find(val1), self.find(val2)
        if self.rbu and rep1 == rep2:
        	return
        rnk1, rnk2 = self.rank[rep1], self.rank[rep2]
        if self.rbu and rnk1 < rnk2:
            self.parent[rep1] = rep2
        elif self.rbu and rnk2 < rnk1: 
            self.parent[rep2] = rep1
        else:
            self.parent[rep1] = rep2
            if self.rbu: self.rank[rep2] += 1

    def make_set(self, val):
        self.parent[val] = val
        self.rank[val] = 0
        

