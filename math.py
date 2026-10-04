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

def solve_linear(a, b):
    """
    Solve the linear equation a*x + b = 0 for x.

    Args:
        a: Coefficient of x (must be nonzero)
        b: Constant term

    Returns:
        The solution x = -b / a
    """
    return -b / a


def rearrange_percent(part, whole):
    """
    Rearrange "part is what percentage of whole" into a decimal proportion.
    percentage (decimal) = part / whole

    Args:
        part: The part value (e.g. 25)
        whole: The whole value (e.g. 200)

    Returns:
        part / whole as a decimal (e.g. 0.125, not 12.5)
    """
    return part / whole

Portfolio allocation. A client has £50,000 and wants a 6% return using a 4% bond fund and an 8% equity fund. 
The two equations are total invested and total return:

def solve_two_by_two(a11, a12, b1, a21, a22, b2):
    """
    Solve the 2x2 system of linear equations:
        a11*x + a12*y = b1
        a21*x + a22*y = b2

    Use substitution, elimination, or Cramer's rule:
        D  = a11*a22 - a12*a21
        x  = (b1*a22 - a12*b2) / D
        y  = (a11*b2 - a21*b1) / D

    Args:
        a11, a12: Coefficients of x and y in the first equation
        b1: Right-hand side of the first equation
        a21, a22: Coefficients of x and y in the second equation
        b2: Right-hand side of the second equation

    Returns:
        A tuple (x, y) with the solution
    """
    determinant = a11 * a22 - a12 * a21
    x = (b1 * a22 - a12 * b2) / determinant
    y = (a11 * b2 - a21 * b1) / determinant
    return (x, y)


def isolate_rate(pv, fv, t):
    """
    Solve FV = PV * (1 + r) ** t for the rate r.
    r = (FV / PV) ** (1 / t) - 1

    Args:
        pv: Present value (PV), must be positive
        fv: Future value (FV), must be positive
        t: Number of periods, must be nonzero

    Returns:
        The implied rate r as a decimal (e.g. 0.10 for 10%)
    """
    return (fv / pv) ** (1 / t) - 1


def satisfies_inequality(x, lo, hi):
    """
    Check whether x falls within the closed range [lo, hi].

    Args:
        x: The value to check
        lo: Lower bound (inclusive)
        hi: Upper bound (inclusive)

    Returns:
        True if lo <= x <= hi, False otherwise
    """
    return lo <= x <= hi
