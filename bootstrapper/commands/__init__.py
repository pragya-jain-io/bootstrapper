# are you wondering why __init__.py exists ?
# python treats a folder with __init__.py as a package
# even if its empty it allows you to do imports
# without it python wont recognize commands as a package and imports will fail
# sometimes we can put shared command-level utilities in it as well