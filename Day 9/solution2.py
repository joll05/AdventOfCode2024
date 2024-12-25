from dataclasses import dataclass

@dataclass
class Block:
    block_id: int
    start: int
    size: int

    def end(self):
        return self.start + self.size

    def checksum(self):
        return self.block_id * sum(i for i in range(self.start, self.end()))

with open("input.txt") as f:
    raw_input = f.read().rstrip()

blocks: list[Block] = []

pointer = 0
for i, char in enumerate(raw_input):
    size = int(char)

    if i % 2 == 0:
        block_id = i // 2
        blocks.append(Block(block_id, pointer, size))
    
    pointer += size

order_to_move: list[Block] = blocks.copy()
order_to_move.reverse()

first_with_space = 0

for i, block_to_move in enumerate(order_to_move):
    prev_end = 0
    for block in blocks:
        if block.start < prev_end:
            print("WTF")
        
        prev_end = block.end()
    
    is_moved = False

    if i % 100 == 0:
        print(f"{i}/{len(blocks)}")

    for insertion_index in range(first_with_space, blocks.index(block_to_move)):
        block_before = blocks[insertion_index]
        block_after = blocks[insertion_index + 1]

        available_space = block_after.start - block_before.end()

        if insertion_index == first_with_space and available_space == 0:
            first_with_space += 1

        if block_to_move.size <= available_space:
            block_to_move.start = block_before.end()
            blocks.remove(block_to_move)
            blocks.insert(insertion_index + 1, block_to_move)
            break
    # s = ["."] * 70

    # for block in blocks:
    #     for i in range(block.start, block.end()):
    #         s[i] = str(block.block_id)

    # print("".join(s))



print(sum(block.checksum() for block in blocks))