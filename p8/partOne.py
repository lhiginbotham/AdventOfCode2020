inp = []
with open('input.txt') as f:
	inp = f.readlines()
	for i in range(0, len(inp)):
		inp[i] = inp[i].rstrip()

class State:
	def __init__(self):
		self.accum = 0
		self.curr_instr = 0

class Op:
	NOP = 0
	JMP = 1
	ACC = 2

	@staticmethod
	def _op_str_to_enum(op_str):
		if op_str == 'nop':
			return Op.NOP
		elif op_str == 'jmp':
			return Op.JMP
		elif op_str == 'acc':
			return Op.ACC
		return -1

	def __init__(self, op_str, op_arg_str, global_state):
		self.op = Op._op_str_to_enum(op_str)
		self.op_arg = int(op_arg_str)
		self.instruction_hit_count = 0
		self.global_state = global_state

	def execute(self):
		self.instruction_hit_count += 1
		if self.op == Op.NOP:
			pass
		elif self.op == Op.JMP:
			self.global_state.curr_instr += self.op_arg
			return
		elif self.op == Op.ACC:
			self.global_state.accum += self.op_arg
		self.global_state.curr_instr += 1

ops = []
state = State()
for op in inp:
	op_str, op_arg_str = op.split(' ')
	ops.append(Op(op_str, op_arg_str, state))

while state.curr_instr < len(ops) and ops[state.curr_instr].instruction_hit_count < 1:
	ops[state.curr_instr].execute()

print(state.accum)