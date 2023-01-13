class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        dim, mas = '', ''

        vol = length * width * height
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or vol >= 10**9:
            dim = "Bulky"
        if mass >= 100:
            mas = "Heavy"

        if dim == "Bulky" and mas == "Heavy":
            rst = 'Both'
        if dim == "Bulky" and mas != "Heavy":
            rst = 'Bulky'
        if dim != "Bulky" and mas == "Heavy":
            rst = 'Heavy'
        if dim != "Bulky" and mas != "Heavy":
            rst = 'Neither'
        return rst
