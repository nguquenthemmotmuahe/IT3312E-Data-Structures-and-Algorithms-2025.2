# Disjoint Set Union / Union-Find
# Customer Account Consolidation

N, Q = map(int, input().split())

# parent[i] = parent of account i
parent = [0] * (N + 1)

# sz[i] = size of the set whose root is i
sz = [1] * (N + 1)

# Initially, every account is its own parent
for i in range(1, N + 1):
    parent[i] = i

# Initially, there are N separate customer profiles
number_of_profiles = N

def find(x):
    #  Return the root (representative) of the profile containing x.
  
    #  to do by student
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
  
def union(x, y):
    # Union two different sets with id= x and id=y.
    # Use union by size.
  
    # to do by student
    if sz[x] < sz[y]:
        x, y = y, x
    parent[y] = x
    sz[x] += sz[y]
  
def merge_account(x, y):
    # Merge the customer profiles containing accounts x and y.
    # Return True if two different profiles are merged.
    # Return False if x and y already belong to the same profile.

    # to do by student
    global number_of_profiles
    root_x = find(x)
    root_y = find(y)
    
    if root_x != root_y:
        union(root_x, root_y)
        number_of_profiles -= 1
        return True
    return False
  
def same_profile(x, y):
     # Return  True if x and y belong to the same customer profile.
  
     # to do by student
     return find(x) == find(y)
  
def profile_size(x):
    # Return the number of accounts in the profile containing x.
  
    # to do by student
     return sz[find(x)]
  
def count_profiles():
    # Return the current number of distinct customer profiles.

    return number_of_profiles

answers = []

for _ in range(Q):
    operation = input().split()

    if operation[0] == "MERGE":
        x = int(operation[1])
        y = int(operation[2])

        merge_account(x, y)

    elif operation[0] == "SAME":
        x = int(operation[1])
        y = int(operation[2])

        if same_profile(x, y):
            answers.append("YES")
        else:
            answers.append("NO")

    elif operation[0] == "SIZE":
        x = int(operation[1])

        answers.append(str(profile_size(x)))

    elif operation[0] == "COUNT":
        answers.append(str(count_profiles()))

print("\n".join(answers))
