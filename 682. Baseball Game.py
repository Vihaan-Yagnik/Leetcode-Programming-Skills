class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for i in operations:
            if i=="C":
                st.pop()
            elif i=="D":
                st.append(st[-1]*2)
            elif i=="+":
                sm=st[-2]+st[-1]
                st.append(sm)
            else:
                st.append(int(i))
        print(st)
        return sum(st)
