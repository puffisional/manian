from node import Node
from session import Session
from manian.volume import Volume as V

sess = Session()
node1 = Node(1, "USD")
print(V(60, "EUR").to("USD"))