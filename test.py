import scrypy

shock_list = scrypy.name_search('radha')
print(shock_list)
modern_legal = scrypy.advanced_search('set:m21')
print(modern_legal)

both = shock_list.in_both(modern_legal)

print(both)