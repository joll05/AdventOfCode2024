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


insertion_index = 0
while insertion_index < len(blocks) - 1:
    block_before = blocks[insertion_index]
    block_after = blocks[insertion_index + 1]
    block_to_move = blocks[-1]

    available_space = block_after.start - block_before.end()

    if block_to_move.size <= available_space:
        # if there is space, move the whole block to the
        blocks.insert(insertion_index + 1, Block(block_to_move.block_id, block_before.end(), block_to_move.size))
        blocks.pop()
    elif available_space != 0:
        blocks.insert(insertion_index + 1, Block(block_to_move.block_id, block_before.end(), available_space))
        block_to_move.size = block_to_move.size - available_space

    insertion_index += 1 # move the insertion index to after the newly inserted block (or to after the "after" block if there was no space)

print(sum(block.checksum() for block in blocks))