def check_if_in_subsets(B,C):
    length = 0
    for Bi in B:
        if any(i in Bi for i in C):
            length += 1
    if length >= len(B):
        return True
    return False

def check_if_in_subset(Bi,C):
    if any(i in Bi for i in C):
        return True
    return False

def hitting_set_bt(B,k,actual_solution, solution):
    if k >= len(B):
        return False
    if check_if_in_subset(B[k],actual_solution):
        return hitting_set_bt(B,k+1,actual_solution, solution)
    for i in B[k]:
        if len(solution) != 0 and len(actual_solution) +1>= len(solution): 
            return False
        actual_solution.append(i)
        if check_if_in_subsets(B[k:], actual_solution):
            solution[:] = actual_solution
        else:
            hitting_set_bt(B, k+1, actual_solution, solution)
        actual_solution.pop()

    return True