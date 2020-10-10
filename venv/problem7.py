
import os


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, pathlist, handler_input):

        current_node = self.root
        for i in pathlist:
            if i not in current_node.children:
                current_node.children[i] = RouteTrieNode()
                current_node = current_node.children[i]
            else:
                #current_node = current_node.children[i]
                current_node.handler = handler_input


        return current_node



        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

    def find(self, pathlist):

        current_node = self.root
        for letter in pathlist:

            if letter not in current_node.children:
                return None
            else:
                current_node = current_node.children[letter]

        return current_node.handler

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
    def __init__(self, handler_init):

        self.router = RouteTrie()
        self.router.root.handler = handler_init

    def add_handler(self, path, handler):

        pathlist = []

        pathlist += self.split_path(path)
        node1 = self.router.insert(pathlist, handler)
        node1.handler = handler

        return node1

        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        pass

    def lookup(self, path):

        #m = self.router.find(path)
        list1 = self.split_path(path)
        #print(list1)
        m = self.router.find(list1)
        current_node = self.router
        if current_node.find(list1):
            return current_node.find(list1)
        else:
            return None



    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler
        pass

    def split_path(self, path):
        #path1 = path.split("/")
        #print(path1)


        return [y for y in path.split("/") if y]



#newrouter = Router()
#newrouter.add_handler("www.hahaha.com/the/bababab", "hi")
#print(newrouter.lookup('www.hahaha.com/the/bababab'))


# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

