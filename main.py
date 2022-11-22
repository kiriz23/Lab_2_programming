"""This program is designed by Kirill Krocha to calculate
sum from var-10 of lab-2 with given param x and precision eps"""
A = -1
B = 1


def s(x: float, eps: float) -> float:
    """This function calculates sum for given param x and precision eps.
     x should be from [-1;1] interval and eps > 0,
     otherwise a function loop is possible"""
    a = x
    sum = a
    k4 = 4   # k4 saves the value of k*4
    x = x*x  # x now saves value of x**2 to save memory
    while a >= eps or -a >= eps:
        a *= x/(k4+2)
        sum += a
        k4 += 4
    return sum


def input_to_float(prompt: str) -> float:
    """Function checks for errors in input data and if there is a
    problem, raises exception, else converts input to float type, and
    if there is a problem with converting, raises exception, else
    returns input data in float type"""
    try:
        input_data = input(prompt)
    except KeyboardInterrupt:
        raise Exception('Input was aborted')
    except:
        raise Exception('There are no input to convert to float.')

    try:
        float_data = float(input_data)
    except ValueError:
        raise Exception(f'Input [{input_data}] could not be converted to float')

    return float_data


def _check_x(x: float) -> bool:
    """Secondary function, takes float x
        and returns bool of A <= x <= B"""
    return A <= x <= B


def _check_eps(eps: float) -> bool:
    """Secondary function, takes float eps
    and returns bool of eps > 0"""
    return eps > 0


def input_with_check(prompt: str, error_message: str, _check=_check_x) -> float:
    """This function requests input data with given prompt,
    then converts it to float using input_to_float function.
    Then checks for data being in domain using
    given in call _check function(by default its _check_x)
    and if float value satisfies the conditions,
    function returns that value, else function
    raises ValueError with given error message"""
    float_data = input_to_float(prompt)
    if not _check(float_data):
        raise ValueError(error_message)
    return float_data


def main():
    """Main function that uses all functions to solve lab-2 task. If there
    is any type of problem, prints error message with diagnostic. Else prints
    given x and eps, and prints result for this input data."""
    print('This program is coded by Kirill Krocha')
    print('This program calculates sum from variant-10 of Lab-2', end=' ')
    print('for input param x and precision eps')
    try:
        prompt_x = 'Enter float param x from [-1;1] interval\n'       # prompts for input x and eps,
        prompt_eps = 'Enter precision of calculations eps (eps>0)\n'  # was made to make func call shorter
        x = input_with_check(prompt_x, 'Incorrect value of x (x is out of [-1;1] interval)')
        eps = input_with_check(prompt_eps, 'Incorrect value of eps (eps<=0 was given)', _check_eps)
        print('***** do calculations ... ', end='')
        res = s(x, eps)
        print('done')
        print('for x = ', end='')
        print(f"{x:.{5}f}")
        print('for eps = ', end='')
        print("{:.4e}".format(eps))
        print('result = ', end='')
        print(f"{res:.{9}f}")
    except Exception as e:
        print('***** Error')
        print(e)
    except BaseException:
        print('Something went wrong')


main()