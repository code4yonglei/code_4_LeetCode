'''

'''

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        smallest={}
        for x in string.ascii_lowercase:
            smallest[x]=x

        def get_small(x):
            if smallest[x] != x:
                smallest[x]=get_small(smallest[x])
            return smallest[x]

        for a,b in zip(s1,s2):
            smaller=min(get_small(a),get_small(b))
            smallest[get_small(a)]=smaller
            smallest[get_small(b)]=smaller
        res=[]
        for x in baseStr:
            res.append(get_small(x))
        return "".join(res)
      
