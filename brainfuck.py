import sys

class Brainfuck:
    def __init__(self):
        self.memory = [0] * 30000
        self.pointer = 0
        self.instructions = ""
        self.instruction_pointer = 0

    def set_instructions(self, instructions):
        self.instructions = instructions

    def run(self):
        while self.instruction_pointer < len(self.instructions):
            instruction = self.instructions[self.instruction_pointer]

            if instruction == ">":
                self.pointer += 1
            elif instruction == "<":
                self.pointer -= 1
            elif instruction == "+":
                self.memory[self.pointer] += 1
            elif instruction == "-":
                self.memory[self.pointer] -= 1
            elif instruction == ".":
                sys.stdout.write(chr(self.memory[self.pointer]))
            elif instruction == ",":
                self.memory[self.pointer] = ord(sys.stdin.read(1))
            elif instruction == "[":
                if self.memory[self.pointer] == 0:
                    loop_depth = 1
                    while loop_depth > 0:
                        self.instruction_pointer += 1
                        if self.instructions[self.instruction_pointer] == "[":
                            loop_depth += 1
                        elif self.instructions[self.instruction_pointer] == "]":
                            loop_depth -= 1
            elif instruction == "]":
                loop_depth = 1
                while loop_depth > 0:
                    self.instruction_pointer -= 1
                    if self.instructions[self.instruction_pointer] == "[":
                        loop_depth -= 1
                    elif self.instructions[self.instruction_pointer] == "]":
                        loop_depth += 1
                self.instruction_pointer -= 1

            self.instruction_pointer += 1