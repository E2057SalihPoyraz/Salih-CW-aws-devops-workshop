vote_list = ["A", "A", "A", "B", "C", "A"]

def majority_vote(vote_list):
    return sorted([[i,vote_list.count(i)] for i in set(sorted(vote_list))],key=lambda x:x[1], reverse=True)[0][0]

print(majority_vote(vote_list))