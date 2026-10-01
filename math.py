def simple_return(old_price, new_price):
    """
    Compute the simple return from old_price to new_price.
    """
    return (new_price - old_price) / old_price


def portfolio_value(quantities, prices):
    """
    Compute the total value of a portfolio given quantities and prices.
    """
    return sum(q * p for q, p in zip(quantities, prices))


def weights_from_values(values):
    """
    Convert a list of asset values into portfolio weights that sum to 1.
    """
    total = sum(values)
    return [v / total for v in values]
