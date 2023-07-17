# def ucs(self,start,end):
#     pq = [[start],0]
#     while pq:
#         pq = sorted(pq, key = lamda x:x[1])
#         front = pq.pop(0)
#         front_path = front[0]
#         curr_node = front_path[-1]
#         if(curr_node == end):
#             return "Node found", front
#         else:
#             for adj_node in grap_dict[curr_node]:
#                 update_cost = front[1]+adj_node[1]
#                 pq.append([front_path + [adj_node[0]], update_cost])
#     return "Node Not found", [[], 0]

def ucs(self, start, end):
    pq = [[start], 0]

    while pq:
        pq = sorted(pq, key=lambda x: x[1])
        front = pq.pop(0)
        front_path = front[0]
        curr_node = front_path[-1]

        if curr_node == end:
            return "Node found", front

        else:
            for adj_node in self.edges[curr_node]:
                update_cost = front[1] + adj_node[1]
                pq.append([front_path + [adj_node[0]], update_cost])

    return "Node not found", [[], 0]
