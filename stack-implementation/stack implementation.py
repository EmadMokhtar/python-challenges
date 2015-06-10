class Stack(object):
	def __init__(self):
		self._items = []

	def pop(self):
		return self._items.pop(-1)

	def push(self, item):
		self._items.append(item)

	def __str__(self):
		return ' '.join([i for i in self._items])

	def __len__(self):
		return len(self._items)


with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		stack = Stack()
		poped_items = []

		for item in line.rstrip().split(' '):
			stack.push(item)

		for i in xrange(0, len(stack)):
			if i % 2 == 0:
				poped_items.append(stack.pop())
			else:
				stack.pop()

		print ' '.join([i for i in poped_items])