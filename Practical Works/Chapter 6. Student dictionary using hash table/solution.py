import sys

# Computes the hash index of a string key using the given polynomial hash formula.
def hash_function(key, table_size):
    p = 31
    # Return hash value of key
    hash_value = 0
    p_pow = 1
    for char in key:
        hash_value = (hash_value + ord(char) * p_pow) % table_size
        p_pow = (p_pow * p) % table_size
    return hash_value
  
# Inserts a new student into the hash table.
# If the student_id already exists, the function updates the student’s name and returns "ALREADY EXIST".
def insert_student(table, table_size, student_id, name):
    # to do by student
    idx = hash_function(student_id, table_size)
    
    for i in range(len(table[idx])):
        if table[idx][i][0] == student_id:
            table[idx][i][1] = name
            return "ALREADY EXIST"
            
    table[idx].append([student_id, name])
    return None
  
# Returns the student’s name if the ID exists.Otherwise, return NOT FOUND
def search_student(table, table_size, student_id):
    # to do by student
    idx = hash_function(student_id, table_size)
    
    for student in table[idx]:
        if student[0] == student_id:
            return student[1]
            
    return "NOT FOUND"
  
# Deletes a student from the hash table using the given student_id.
# If the student ID does not exist, the function does nothing.
def delete_student(table, table_size, student_id):
    # to do by student
    idx = hash_function(student_id, table_size)
    
    for i in range(len(table[idx])):
        if table[idx][i][0] == student_id:
            table[idx].pop(i)
            return
          
def main():
    lines = sys.stdin.read().strip().splitlines()

    if not lines:
        return

    M, Q = map(int, lines[0].split())
    table = [[] for _ in range(M)]
    output = []

    for line in lines[1:1 + Q]:
        command = line.split()

        if command[0] == "INSERT":
            student_id = command[1]
            name = command[2]

            result = insert_student(table, M, student_id, name)

            if result is not None:
                output.append(result)

        elif command[0] == "SEARCH":
            student_id = command[1]
            output.append(search_student(table, M, student_id))

        elif command[0] == "DELETE":
            student_id = command[1]
            delete_student(table, M, student_id)

    print("\n".join(output))


if __name__ == "__main__":
    main()
