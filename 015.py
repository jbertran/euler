lattice = [[{'neighbors':[], 'origin'=[]} for i in range(20)] for j in range(20)]

# graph setup
for i in lattice:
    for j in lattice[i]:
        node = lattice[i][j]
        # Left
        if j > 0:
            node['neighbors'].append(lattice[i][j-1])
        # right
        if j < len(lattice[i] - 1):
            node['neighbors'].append(lattice[i][j+1])
        # up
        if i > 0:
            node['neighbors'].append(lattice[i-1][j])
        # down
        if i < len(lattice - 1):
            node['neighbors'].append(lattice[i+1][j])

print(lattice)
