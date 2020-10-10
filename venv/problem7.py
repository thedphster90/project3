
import os


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, pathlist, handler_input):

        current_node = self.root
        for i in pathlist:
            if not i in pathlist:
                current_node.children[i] = RouteTrieNode()
                current_node = current_node.children[i]
            else:
                current_node = current_node.children[i]
                current_node.handler = handler_input



        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

    def find(self, pathlist):

        current_node = self.root
        for letter in pathlist:

            if letter not in pathlist:
                current_node = current_node.children[letter]
        return current_node

        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
    pass
# A  RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):

        self.children = {}
        self.handler = None
        # Initialize the node with children as before, plus a handler

    def insert(self, char):
        self.children[char] = RouteTrieNode()
        # Insert the node as before


class Router:
    def __init__(self, handler_init = ''):

        self.router = RouteTrie()
        self.router.root.handler = handler_init
        self.handlerroot = self.router.root.handler

    def add_handler(self, path, handler):

        handlerlist = []

        handlerlist += self.split_path(path)
        node1 = self.router.insert(handlerlist, handler)

        print(handlerlist)



        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        pass

    def lookup(self, path):

        #m = self.router.find(path)
        list1 = self.split_path(path)
        print(list1)
        m = self.router.find(list1)
       # if self.router.root.handler == None:
            #return None

        if not m:
            return print("handler not found")
        else:
            return print(m)



    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler
        pass

    def split_path(self, path):
        return [y for y in path.split("/") if y]



newrouter = Router()
newrouter.add_handler("www.hello.com/the/train/came/to/the/station")
print(newrouter.lookup('the'))

newrouter1 = Router()
print(newrouter1.lookup('the'))
newrouter1.lookup('hi')
