filename = 'initial_input'

lines = open(filename).read().split('\n\n')
elf_list = [[int(x) for x in elf.split()] for elf in lines]
print(sum(sorted([sum(elf) for elf in elf_list], reverse = True)[:3]))