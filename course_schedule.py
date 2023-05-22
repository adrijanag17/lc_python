# time - O(n + p) space - O()  where n = len(numCourses) and p = len(prerequisites)
def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    pre_map = {i: [] for i in range(num_courses)}

    for crs, pre in prerequisites:
        pre_map[crs].append(pre)

    visited = set()

    def doable_dfs(crs):
        if crs in visited:
            return False
        if pre_map[crs] == []:
            return True
        visited.add(crs)

        for p in pre_map[crs]:
            if not doable_dfs(p): return False
        
        visited.remove(crs)
        pre_map[crs] = []
        return True

    for i in range(num_courses):
        if not doable_dfs(i): return False
    return True

def main():

    print(can_finish(5, [[0, 1],[0, 2], [1, 3], [1, 4], [3, 4]]))


main()