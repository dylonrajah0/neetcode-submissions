class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        st = []

        opSet = set()
        opSet.add("+")
        opSet.add("-")
        opSet.add("*")
        opSet.add("/")

        for i in range(0, len(tokens)):

            if tokens[i] in opSet:
                right = st.pop()
                left = st.pop()

                resNum = 0
                if tokens[i] == "-":
                    resNum = left - right
                elif tokens[i] == "+":
                    resNum = left + right
                elif tokens[i] == "*":
                    resNum = left * right
                else:
                    resNum = int(left/right)

                st.append(resNum)
            else:
                st.append(int(tokens[i]))

        return st.pop()
