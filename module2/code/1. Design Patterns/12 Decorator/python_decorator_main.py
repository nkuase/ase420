def FullBorder(f):
    def wrapped(*args, **kwargs):
        s = f(*args, **kwargs)
        line = "+" + "-" * len(s) + "+"
        return f"{line}\n|{s}|\n{line}"
    return wrapped

def SideBorder(ch="#"):
    def deco(f):
        def wrapped(*args, **kwargs):
            s = f(*args, **kwargs)
            return f"{ch}{s}{ch}"
        return wrapped
    return deco

@FullBorder
@SideBorder("#")
def make_text():
    return "Hello, world."

print(make_text())