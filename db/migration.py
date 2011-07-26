import sqlalchemy

def update(saveddata_engine):
    checkPriceFailures(saveddata_engine)

def checkPriceFailures(saveddata_engine):
    # Check if we have 'failed' column
    try:
        saveddata_engine.execute("SELECT failed FROM prices")
    except sqlalchemy.exc.OperationalError:
        # As we don't have any important data there, let's just drop
        # and recreate whole table
        from eos.db.saveddata.price import prices_table
        prices_table.drop(saveddata_engine)
        prices_table.create(saveddata_engine)
