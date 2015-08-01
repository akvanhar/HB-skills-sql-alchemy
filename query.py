"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
brand_id_of_8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
corvette_and_chevrolet = Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.
older_than_1960 = Model.query.filter(Model.year < 1960).all()

#When I run this, I get 2 models, then this error: UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 28: ordinal not in range(128)
#I think that means there's something weird in the database... but I don't want to dive into that rabbit hole

# Get all brands that were founded after 1920.
brand_founded_after_1920 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
cor_models = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
brands_in_1903_not_yet_dc = Brand.query.filter(Brand.founded == '1903',
												Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
brands_dc_or_founded_pre1950 = Brand.query.filter(db.or_(Brand.discontinued < 1950,
												  Brand.founded < 1950)).all()

#Same ascii error. I bet that the same car has the same issue.
#Oh. I think it's the Citroen. The dots over the e I think are causing this error.

# Get any model whose brand_name is not Chevrolet.
brand_name_not_chevrolet = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    print db.session.query(Model.name, 
    					   Model.brand_name, 
    					   Brand.headquarters).join(Brand).filter(Model.year == year).all()

    return

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
	
	print db.session.query(Model.brand_name, Model.name).order_by(Model.brand_name).all()):
    return

# -------------------------------------------------------------------

# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
	return Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()

def get_models_between(start_year, end_year):
	return Model.query.filter(Model.year > start_year,
							  Model.year < end_year).all()
    

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

#Return value: <flask_sqlalchemy.BaseQuery object at 0x10e27ecd0>
#Datatype: it's a query object! Need to specify .all(), .first(), .one() 
#to get a Brand object where the name = Ford.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

#An association table is a table that associates two other tables that have a many-to-many relationship.
#For example, the ratings table was an association table between Movies and Users.
