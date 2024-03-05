from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, lpSum, PULP_CBC_CMD

def get_elements(B):
    A=[]
    for Bi in B:
        for i in Bi:
            if i not in A:
                A.append(i)
    return A
    
def hitting_set_PLE(B):
    prob = LpProblem("hitting_Set", LpMinimize)
    A = get_elements(B)
    i = LpVariable.dicts("i", A, cat='Binary')
    
    prob += lpSum(i[j] for j in A)
    for Bi in B:
        prob += lpSum(i[j] for j in Bi if j in A) >= 1

    prob.solve(PULP_CBC_CMD(msg=False))

    if LpStatus[prob.status] == 'Optimal':
        return [j for j in A if i[j].value() == 1]
    return None